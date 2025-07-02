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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,315,343</td>
<td align="right">504,220</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,349,805</td>
<td align="right">546,406</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">21,547,631</td>
<td align="right">32,269,218</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,587,473</td>
<td align="right">2,464,039</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,322,630</td>
<td align="right">88,842,584</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">56,417,177</td>
<td align="right">41,476,093</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,075,598</td>
<td align="right">39,059,898</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,265,068</td>
<td align="right">956,119</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">14,315,303</td>
<td align="right">10,896,815</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,644,738</td>
<td align="right">77,479,751</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,807,652</td>
<td align="right">2,287,379</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">127,641,316</td>
<td align="right">104,331,177</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220,699,126</td>
<td align="right">180,545,091</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">23,354</td>
<td align="right">19,258</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">55,931,808</td>
<td align="right">46,766,910</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">461,046,077</td>
<td align="right">388,104,327</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">376,588,810</td>
<td align="right">317,384,604</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">150,122,923</td>
<td align="right">128,088,686</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">314,166,728</td>
<td align="right">269,387,126</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">903,802,655</td>
<td align="right">778,660,307</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">123,010,138</td>
<td align="right">106,636,792</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">111,924,190</td>
<td align="right">97,657,884</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">180,375,961</td>
<td align="right">158,484,972</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">70,279,273</td>
<td align="right">61,848,915</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">78,915</td>
<td align="right">69,504</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">202,341,510</td>
<td align="right">179,019,088</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">165,915,658</td>
<td align="right">147,990,522</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">126,964,985</td>
<td align="right">113,811,159</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">198,025,212</td>
<td align="right">177,778,427</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,758,604</td>
<td align="right">44,736,789</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,097,872</td>
<td align="right">33,463,340</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,105,223,871</td>
<td align="right">997,947,025</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">277,567,008</td>
<td align="right">250,995,350</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">127,298,230</td>
<td align="right">115,712,247</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">187,345,539</td>
<td align="right">170,477,449</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,430,866,539</td>
<td align="right">1,304,839,354</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,163,920</td>
<td align="right">10,181,151</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">180,668,101</td>
<td align="right">164,844,472</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">126,693,683</td>
<td align="right">115,903,847</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,288,719</td>
<td align="right">29,569,419</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,840,180</td>
<td align="right">2,604,900</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">77,865,122</td>
<td align="right">71,472,243</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">150,056,920</td>
<td align="right">137,770,457</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">413,419,054</td>
<td align="right">379,871,906</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,545,028</td>
<td align="right">5,095,755</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,513,661,969</td>
<td align="right">2,319,396,144</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">402,673,928</td>
<td align="right">372,220,158</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">710,099,548</td>
<td align="right">659,245,792</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,560,100</td>
<td align="right">98,193,562</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,127,590,624</td>
<td align="right">1,049,349,554</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">148,539,462</td>
<td align="right">138,660,057</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">911,268,516</td>
<td align="right">852,497,113</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,175,652,389</td>
<td align="right">1,101,107,994</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">495,630,664</td>
<td align="right">464,776,874</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,357,151,603</td>
<td align="right">1,273,185,913</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">308,783,005</td>
<td align="right">289,765,696</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">208,029,113</td>
<td align="right">195,379,984</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">364,805,250</td>
<td align="right">342,690,565</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">543,887,020</td>
<td align="right">511,340,217</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,307,060</td>
<td align="right">45,434,149</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">204,694,960</td>
<td align="right">192,536,906</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,000,672,710</td>
<td align="right">5,646,460,602</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,844,466,412</td>
<td align="right">20,556,716,375</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,865,042,200</td>
<td align="right">3,648,778,678</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,658,584,614</td>
<td align="right">1,567,525,485</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">169,692,872</td>
<td align="right">160,563,867</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,003,558,710</td>
<td align="right">951,630,573</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">112,619,552</td>
<td align="right">106,800,652</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">379,033,731</td>
<td align="right">359,710,264</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">582,617,664</td>
<td align="right">553,541,847</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">745,439,463</td>
<td align="right">708,282,937</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">42,342,411</td>
<td align="right">40,287,414</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">523,694,640</td>
<td align="right">498,386,064</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">686,467,498</td>
<td align="right">654,934,294</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">43,268,121</td>
<td align="right">41,341,276</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,367,235,774</td>
<td align="right">2,261,825,301</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,160,271</td>
<td align="right">81,397,116</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">256,917,370</td>
<td align="right">245,961,466</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">460,495,946</td>
<td align="right">441,021,890</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,750,548,853</td>
<td align="right">4,550,955,510</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">77,570,208</td>
<td align="right">74,319,665</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">52,659,895</td>
<td align="right">50,486,686</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">561,774,783</td>
<td align="right">538,663,605</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,200,812,186</td>
<td align="right">4,030,374,538</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">279,814,286</td>
<td align="right">268,527,313</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,521,988</td>
<td align="right">4,342,541</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">148,232,665</td>
<td align="right">142,420,181</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">69,122,262</td>
<td align="right">66,412,451</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">287,085,488</td>
<td align="right">275,932,504</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,245,700</td>
<td align="right">6,003,780</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,729,160</td>
<td align="right">9,360,110</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,408,781</td>
<td align="right">454,955,272</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,880,274</td>
<td align="right">58,694,178</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,093,418,408</td>
<td align="right">2,982,421,139</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">855,458,697</td>
<td align="right">824,882,190</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,587,487</td>
<td align="right">9,259,255</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">162,258,182</td>
<td align="right">156,719,712</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,319,826,786</td>
<td align="right">5,138,689,540</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,022,498,980</td>
<td align="right">987,972,063</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">378,359,772</td>
<td align="right">365,648,405</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">622,782,529</td>
<td align="right">602,364,735</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">340,970,920</td>
<td align="right">330,109,996</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">216,294,785</td>
<td align="right">209,892,866</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">290,235,754</td>
<td align="right">281,737,088</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,058</td>
<td align="right">544,228</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,175,359,190</td>
<td align="right">1,142,309,544</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,463,459</td>
<td align="right">3,369,182</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">325,444,414</td>
<td align="right">317,050,404</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">179,456,344</td>
<td align="right">174,915,459</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">509,533,514</td>
<td align="right">497,071,977</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,859,527,763</td>
<td align="right">2,791,430,116</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,002,984</td>
<td align="right">25,385,832</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,863,001</td>
<td align="right">67,229,359</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,155,044,767</td>
<td align="right">3,082,365,524</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">505,997,641</td>
<td align="right">494,609,825</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,914,678</td>
<td align="right">40,996,639</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">115,592,412</td>
<td align="right">113,088,788</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,923,024,292</td>
<td align="right">5,796,013,150</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">82,162,534</td>
<td align="right">80,403,989</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,749,042</td>
<td align="right">241,592,226</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">834,225,425</td>
<td align="right">818,325,912</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">355,102,174</td>
<td align="right">348,339,099</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">292,986,322</td>
<td align="right">287,706,830</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,886,278,891</td>
<td align="right">2,834,402,854</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,653,126,775</td>
<td align="right">5,551,661,102</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">996,950,166</td>
<td align="right">979,553,945</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">105,475,401</td>
<td align="right">103,731,713</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">110,571,492</td>
<td align="right">108,868,784</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,134,973,425</td>
<td align="right">3,087,500,256</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,536,315</td>
<td align="right">279,283,691</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,475,625,014</td>
<td align="right">1,454,182,896</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">144,322,670</td>
<td align="right">142,399,921</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,531,042</td>
<td align="right">69,607,419</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,751,476</td>
<td align="right">69,850,018</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,741,390</td>
<td align="right">60,969,461</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">141,656,128</td>
<td align="right">139,970,428</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">691,860,214</td>
<td align="right">684,168,996</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,113,365</td>
<td align="right">74,282,887</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,179,477</td>
<td align="right">70,606,227</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">368,593,190</td>
<td align="right">366,287,368</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,194,260</td>
<td align="right">256,430,936</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">97,368,923</td>
<td align="right">96,908,986</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,716,461</td>
<td align="right">10,672,400</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">214,755,660</td>
<td align="right">214,441,563</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,866,491,065</td>
<td align="right">1,864,229,028</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,168,904</td>
<td align="right">21,146,978</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,444,509</td>
<td align="right">21,422,583</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,444,530</td>
<td align="right">21,422,604</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">312,619,709</td>
<td align="right">312,337,134</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">314,669,797</td>
<td align="right">314,387,224</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,158</td>
<td align="right">14,154</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,430,767</td>
<td align="right">28,438,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,044</td>
<td align="right">92,027</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,928,080</td>
<td align="right">35,922,651</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,580,198</td>
<td align="right">1,579,986</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,107,987,306</td>
<td align="right">1,107,856,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">324,432</td>
<td align="right">324,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,328,501</td>
<td align="right">332,357,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106,356</td>
<td align="right">106,348</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,688,509</td>
<td align="right">114,682,459</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,522,603</td>
<td align="right">13,523,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,719,955</td>
<td align="right">418,705,632</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,679,416</td>
<td align="right">6,679,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,478,601</td>
<td align="right">591,462,250</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,082,570</td>
<td align="right">155,078,482</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,622,717</td>
<td align="right">15,622,451</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,554,186</td>
<td align="right">302,552,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,278,985</td>
<td align="right">6,279,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,330</td>
<td align="right">3,100,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,636,886</td>
<td align="right">172,636,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,310,671</td>
<td align="right">129,310,671</td>
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
<td align="right">41,858,530</td>
<td align="right">41,858,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,660</td>
<td align="right">29,134,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">11,838,226</td>
<td align="right">11,838,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,951,274</td>
<td align="right">8,951,274</td>
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
<td align="left">RERAISE</td>
<td align="right">4,130,887</td>
<td align="right">4,130,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2,332,025</td>
<td align="right">2,332,025</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">333,538</td>
<td align="right">333,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">120,759</td>
<td align="right">120,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">115,623</td>
<td align="right">115,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">74,319</td>
<td align="right">74,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">73,792</td>
<td align="right">73,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">50,315</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">23,410</td>
<td align="right">23,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,959</td>
<td align="right">5,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">3,696</td>
<td align="right">3,696</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,776</td>
<td align="right">1,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">725</td>
<td align="right">725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
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
<td align="right">1,174,817,914</td>
<td align="right">6.5%</td>
<td align="right">1,100,340,022</td>
<td align="right">6.1%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,519,872</td>
<td align="right">0.4%</td>
<td align="right">68,401,425</td>
<td align="right">0.4%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,894,910,967</td>
<td align="right">93.2%</td>
<td align="right">16,873,358,801</td>
<td align="right">93.5%</td>
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
<td align="right">676,145</td>
<td align="right">32.7%</td>
<td align="right">609,832</td>
<td align="right">29.6%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,392,698</td>
<td align="right">67.3%</td>
<td align="right">1,446,962</td>
<td align="right">70.4%</td>
<td align="right">3.9%</td>
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
<td align="left">and int</td>
<td align="right">29,725</td>
<td align="right">4.4%</td>
<td align="right">10,695</td>
<td align="right">1.8%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">25,123</td>
<td align="right">3.7%</td>
<td align="right">14,343</td>
<td align="right">2.4%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,182</td>
<td align="right">2.2%</td>
<td align="right">10,288</td>
<td align="right">1.7%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">5,212</td>
<td align="right">0.8%</td>
<td align="right">3,632</td>
<td align="right">0.6%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">39,634</td>
<td align="right">5.9%</td>
<td align="right">30,627</td>
<td align="right">5.0%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">440</td>
<td align="right">0.1%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,139</td>
<td align="right">2.2%</td>
<td align="right">13,205</td>
<td align="right">2.2%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">923</td>
<td align="right">0.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">56,725</td>
<td align="right">8.4%</td>
<td align="right">51,402</td>
<td align="right">8.4%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">4,862</td>
<td align="right">0.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">33,181</td>
<td align="right">4.9%</td>
<td align="right">30,327</td>
<td align="right">5.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,421</td>
<td align="right">2.3%</td>
<td align="right">14,374</td>
<td align="right">2.4%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,099</td>
<td align="right">8.7%</td>
<td align="right">55,480</td>
<td align="right">9.1%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,464</td>
<td align="right">1.3%</td>
<td align="right">8,002</td>
<td align="right">1.3%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">588</td>
<td align="right">0.1%</td>
<td align="right">567</td>
<td align="right">0.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">53,291</td>
<td align="right">7.9%</td>
<td align="right">51,452</td>
<td align="right">8.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">24,994</td>
<td align="right">3.7%</td>
<td align="right">24,212</td>
<td align="right">4.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">28,111</td>
<td align="right">4.2%</td>
<td align="right">27,266</td>
<td align="right">4.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">4,813</td>
<td align="right">0.7%</td>
<td align="right">4,670</td>
<td align="right">0.8%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">71,296</td>
<td align="right">10.5%</td>
<td align="right">70,377</td>
<td align="right">11.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">4,237</td>
<td align="right">0.6%</td>
<td align="right">4,197</td>
<td align="right">0.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">12,881</td>
<td align="right">1.9%</td>
<td align="right">12,767</td>
<td align="right">2.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">29,084</td>
<td align="right">4.3%</td>
<td align="right">28,916</td>
<td align="right">4.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,410</td>
<td align="right">0.2%</td>
<td align="right">1,413</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,953</td>
<td align="right">1.6%</td>
<td align="right">10,933</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">109,863</td>
<td align="right">16.2%</td>
<td align="right">109,693</td>
<td align="right">18.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,634</td>
<td align="right">0.8%</td>
<td align="right">5,634</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,764</td>
<td align="right">0.6%</td>
<td align="right">3,764</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,756</td>
<td align="right">0.4%</td>
<td align="right">2,756</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">1,207</td>
<td align="right">0.2%</td>
<td align="right">1,207</td>
<td align="right">0.2%</td>
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
<td align="left">and different types</td>
<td align="right">363</td>
<td align="right">0.1%</td>
<td align="right">363</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
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
<td align="right">198,025,212</td>
<td align="right">100.0%</td>
<td align="right">177,778,427</td>
<td align="right">100.0%</td>
<td align="right">-10.2%</td>
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
<td align="right">169,583,912</td>
<td align="right">1.4%</td>
<td align="right">162,898,293</td>
<td align="right">1.3%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">167,366,537</td>
<td align="right">1.4%</td>
<td align="right">160,806,891</td>
<td align="right">1.3%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,199,679,343</td>
<td align="right">98.6%</td>
<td align="right">12,187,519,233</td>
<td align="right">98.7%</td>
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
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
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
<td align="right">3,797,407</td>
<td align="right">100.0%</td>
<td align="right">3,671,222</td>
<td align="right">100.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">166</td>
<td align="right">0.0%</td>
<td align="right">166</td>
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
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">166</td>
<td align="right">100.0%</td>
<td align="right">166</td>
<td align="right">100.0%</td>
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
<td align="right">685,118</td>
<td align="right">91.8%</td>
<td align="right">685,114</td>
<td align="right">91.8%</td>
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
<td align="right">640,338</td>
<td align="right">85.8%</td>
<td align="right">640,338</td>
<td align="right">85.8%</td>
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
<td align="right">61,576</td>
<td align="right">100.0%</td>
<td align="right">61,572</td>
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
<td align="right">126,450,463</td>
<td align="right">2.4%</td>
<td align="right">115,664,413</td>
<td align="right">2.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,318,804</td>
<td align="right">0.0%</td>
<td align="right">1,301,953</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,196,682,617</td>
<td align="right">97.6%</td>
<td align="right">5,188,142,605</td>
<td align="right">97.8%</td>
<td align="right">-0.2%</td>
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
<td align="right">177,226</td>
<td align="right">66.2%</td>
<td align="right">173,492</td>
<td align="right">65.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">90,469</td>
<td align="right">33.8%</td>
<td align="right">90,119</td>
<td align="right">34.2%</td>
<td align="right">-0.4%</td>
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
<td align="right">1,244</td>
<td align="right">0.7%</td>
<td align="right">1,082</td>
<td align="right">0.6%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">16,374</td>
<td align="right">9.2%</td>
<td align="right">15,020</td>
<td align="right">8.7%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">12,209</td>
<td align="right">6.9%</td>
<td align="right">11,301</td>
<td align="right">6.5%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,827</td>
<td align="right">1.6%</td>
<td align="right">2,675</td>
<td align="right">1.5%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,404</td>
<td align="right">7.0%</td>
<td align="right">12,202</td>
<td align="right">7.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">11,543</td>
<td align="right">6.5%</td>
<td align="right">11,375</td>
<td align="right">6.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,246</td>
<td align="right">12.6%</td>
<td align="right">21,927</td>
<td align="right">12.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">64,443</td>
<td align="right">36.4%</td>
<td align="right">63,876</td>
<td align="right">36.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,368</td>
<td align="right">15.4%</td>
<td align="right">27,466</td>
<td align="right">15.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,212</td>
<td align="right">1.8%</td>
<td align="right">3,212</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,842</td>
<td align="right">1.6%</td>
<td align="right">2,842</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">514</td>
<td align="right">0.3%</td>
<td align="right">514</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,369,433</td>
<td align="right">0.1%</td>
<td align="right">1,043,801</td>
<td align="right">0.0%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">122,882,522</td>
<td align="right">5.3%</td>
<td align="right">106,515,945</td>
<td align="right">4.7%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,181,105,705</td>
<td align="right">94.6%</td>
<td align="right">2,177,558,459</td>
<td align="right">95.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">41,395</td>
<td align="right">27.0%</td>
<td align="right">35,251</td>
<td align="right">25.1%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">111,946</td>
<td align="right">73.0%</td>
<td align="right">105,177</td>
<td align="right">74.9%</td>
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
<td align="left">str</td>
<td align="right">32,976</td>
<td align="right">29.5%</td>
<td align="right">29,332</td>
<td align="right">27.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">18,057</td>
<td align="right">16.1%</td>
<td align="right">16,954</td>
<td align="right">16.1%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">29,930</td>
<td align="right">26.7%</td>
<td align="right">28,793</td>
<td align="right">27.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,983</td>
<td align="right">27.7%</td>
<td align="right">30,098</td>
<td align="right">28.6%</td>
<td align="right">-2.9%</td>
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
<td align="right">220,430,650</td>
<td align="right">13.5%</td>
<td align="right">180,304,205</td>
<td align="right">11.9%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,346,557,862</td>
<td align="right">82.6%</td>
<td align="right">1,276,586,140</td>
<td align="right">84.1%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,672,070</td>
<td align="right">3.8%</td>
<td align="right">60,409,897</td>
<td align="right">4.0%</td>
<td align="right">-3.6%</td>
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
<td align="right">208,913</td>
<td align="right">14.4%</td>
<td align="right">181,295</td>
<td align="right">13.1%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,241,612</td>
<td align="right">85.6%</td>
<td align="right">1,199,042</td>
<td align="right">86.9%</td>
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
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">15,385</td>
<td align="right">7.4%</td>
<td align="right">7,692</td>
<td align="right">4.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">805</td>
<td align="right">0.4%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,577</td>
<td align="right">8.9%</td>
<td align="right">14,664</td>
<td align="right">8.1%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,710</td>
<td align="right">1.8%</td>
<td align="right">3,014</td>
<td align="right">1.7%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">18,907</td>
<td align="right">9.1%</td>
<td align="right">15,812</td>
<td align="right">8.7%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,042</td>
<td align="right">5.3%</td>
<td align="right">9,661</td>
<td align="right">5.3%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">10,328</td>
<td align="right">4.9%</td>
<td align="right">9,251</td>
<td align="right">5.1%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,675</td>
<td align="right">2.7%</td>
<td align="right">5,107</td>
<td align="right">2.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">79,545</td>
<td align="right">38.1%</td>
<td align="right">72,956</td>
<td align="right">40.2%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,336</td>
<td align="right">2.1%</td>
<td align="right">4,015</td>
<td align="right">2.2%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
<td align="right">1,076</td>
<td align="right">0.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">17,670</td>
<td align="right">8.5%</td>
<td align="right">16,443</td>
<td align="right">9.1%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,926</td>
<td align="right">3.8%</td>
<td align="right">7,634</td>
<td align="right">4.2%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">11,401</td>
<td align="right">5.5%</td>
<td align="right">11,258</td>
<td align="right">6.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,829</td>
<td align="right">0.9%</td>
<td align="right">1,807</td>
<td align="right">1.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">string</td>
<td align="right">2,799,014</td>
<td align="right">2,799,014 / 0 !!</td>
<td align="right">2,297,254</td>
<td align="right">2,297,254 / 0 !!</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,399,895</td>
<td align="right">34,399,895 / 0 !!</td>
<td align="right">34,205,335</td>
<td align="right">34,205,335 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,055,957</td>
<td align="right">117,055,957 / 0 !!</td>
<td align="right">116,484,674</td>
<td align="right">116,484,674 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,352,657</td>
<td align="right">12,352,657 / 0 !!</td>
<td align="right">12,363,801</td>
<td align="right">12,363,801 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,653,518</td>
<td align="right">5,653,518 / 0 !!</td>
<td align="right">5,649,453</td>
<td align="right">5,649,453 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">173,420,310</td>
<td align="right">173,420,310 / 0 !!</td>
<td align="right">173,313,032</td>
<td align="right">173,313,032 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,698,672</td>
<td align="right">305,698,672 / 0 !!</td>
<td align="right">305,510,210</td>
<td align="right">305,510,210 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,677,864</td>
<td align="right">101,677,864 / 0 !!</td>
<td align="right">101,671,657</td>
<td align="right">101,671,657 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,989,877</td>
<td align="right">336,989,877 / 0 !!</td>
<td align="right">336,989,935</td>
<td align="right">336,989,935 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,386,949</td>
<td align="right">0.0%</td>
<td align="right">1,131,176</td>
<td align="right">0.0%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">579,893,223</td>
<td align="right">4.0%</td>
<td align="right">550,864,541</td>
<td align="right">3.9%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">648,781,221</td>
<td align="right">4.5%</td>
<td align="right">624,726,422</td>
<td align="right">4.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,268,396,677</td>
<td align="right">91.5%</td>
<td align="right">13,061,457,991</td>
<td align="right">91.7%</td>
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
<td align="right">12,851,971</td>
<td align="right">94.3%</td>
<td align="right">12,397,977</td>
<td align="right">94.2%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">773,596</td>
<td align="right">5.7%</td>
<td align="right">758,029</td>
<td align="right">5.8%</td>
<td align="right">-2.0%</td>
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
<td align="right">78,198</td>
<td align="right">10.1%</td>
<td align="right">74,057</td>
<td align="right">9.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">82,231</td>
<td align="right">10.6%</td>
<td align="right">79,615</td>
<td align="right">10.5%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">1,632</td>
<td align="right">0.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">140,874</td>
<td align="right">18.2%</td>
<td align="right">138,226</td>
<td align="right">18.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,774</td>
<td align="right">0.4%</td>
<td align="right">2,732</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,766</td>
<td align="right">0.6%</td>
<td align="right">4,703</td>
<td align="right">0.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">30,745</td>
<td align="right">4.0%</td>
<td align="right">30,455</td>
<td align="right">4.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">4,306</td>
<td align="right">0.6%</td>
<td align="right">4,268</td>
<td align="right">0.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">41,227</td>
<td align="right">5.3%</td>
<td align="right">41,550</td>
<td align="right">5.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">12,305</td>
<td align="right">1.6%</td>
<td align="right">12,223</td>
<td align="right">1.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,878</td>
<td align="right">1.9%</td>
<td align="right">14,801</td>
<td align="right">2.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,802</td>
<td align="right">2.8%</td>
<td align="right">21,886</td>
<td align="right">2.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">9,020</td>
<td align="right">1.2%</td>
<td align="right">9,020</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">106</td>
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
<td align="right">6,347,712,794</td>
<td align="right">99.7%</td>
<td align="right">6,187,005,595</td>
<td align="right">99.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,100,597</td>
<td align="right">0.2%</td>
<td align="right">15,100,466</td>
<td align="right">0.2%</td>
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
<td align="right">5,094</td>
<td align="right">0.0%</td>
<td align="right">5,094</td>
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
<td align="right">312,632</td>
<td align="right">0.0%</td>
<td align="right">312,632</td>
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
<td align="right">527,243</td>
<td align="right">100.0%</td>
<td align="right">527,108</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,988</td>
<td align="right">0.0%</td>
<td align="right">6,984</td>
<td align="right">0.0%</td>
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
<td align="right">67,201,384</td>
<td align="right">100.0%</td>
<td align="right">67,201,357</td>
<td align="right">100.0%</td>
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
<td align="right">7,170</td>
<td align="right">100.0%</td>
<td align="right">7,170</td>
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
<td align="right">591,451,180</td>
<td align="right">82.1%</td>
<td align="right">591,434,829</td>
<td align="right">82.1%</td>
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
<td align="right">129,260,696</td>
<td align="right">17.9%</td>
<td align="right">129,260,696</td>
<td align="right">17.9%</td>
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
<td align="right">27,421</td>
<td align="right">0.0%</td>
<td align="right">27,421</td>
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
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
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
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
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
<td align="right">122,651,146</td>
<td align="right">4.6%</td>
<td align="right">108,471,060</td>
<td align="right">4.1%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,528,805</td>
<td align="right">2.3%</td>
<td align="right">60,757,547</td>
<td align="right">2.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,487,997,840</td>
<td align="right">93.1%</td>
<td align="right">2,481,283,804</td>
<td align="right">93.6%</td>
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
<td align="right">2,420,930</td>
<td align="right">96.0%</td>
<td align="right">2,153,495</td>
<td align="right">95.5%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">101,720</td>
<td align="right">4.0%</td>
<td align="right">101,049</td>
<td align="right">4.5%</td>
<td align="right">-0.7%</td>
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
<td align="right">8,313</td>
<td align="right">8.2%</td>
<td align="right">7,704</td>
<td align="right">7.6%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">310,091</td>
<td align="right">304.8%</td>
<td align="right">304,236</td>
<td align="right">301.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">7,974</td>
<td align="right">7.8%</td>
<td align="right">7,914</td>
<td align="right">7.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
<td align="right">11,037</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,626</td>
<td align="right">42.9%</td>
<td align="right">43,626</td>
<td align="right">43.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">14,124</td>
<td align="right">13.9%</td>
<td align="right">14,124</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">7,044</td>
<td align="right">6.9%</td>
<td align="right">7,044</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,088</td>
<td align="right">3.0%</td>
<td align="right">3,088</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">251</td>
<td align="right">0.2%</td>
<td align="right">251</td>
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
<td align="right">1,349,805</td>
<td align="right">100.0%</td>
<td align="right">546,406</td>
<td align="right">100.0%</td>
<td align="right">-59.5%</td>
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
<td align="right">105,465,188</td>
<td align="right">10.1%</td>
<td align="right">98,102,270</td>
<td align="right">9.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">938,464,748</td>
<td align="right">89.9%</td>
<td align="right">938,372,486</td>
<td align="right">90.5%</td>
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
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
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
<td align="right">79,744</td>
<td align="right">84.0%</td>
<td align="right">76,128</td>
<td align="right">83.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">16.0%</td>
<td align="right">15,204</td>
<td align="right">16.6%</td>
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
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">126</td>
<td align="right">0.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">850</td>
<td align="right">1.1%</td>
<td align="right">682</td>
<td align="right">0.9%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">2,203</td>
<td align="right">2.8%</td>
<td align="right">1,791</td>
<td align="right">2.4%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">6,944</td>
<td align="right">9.1%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,174</td>
<td align="right">20.3%</td>
<td align="right">14,205</td>
<td align="right">18.7%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
<td align="right">4,445</td>
<td align="right">5.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,016</td>
<td align="right">56.5%</td>
<td align="right">44,976</td>
<td align="right">59.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,959</td>
<td align="right">3.7%</td>
<td align="right">2,959</td>
<td align="right">3.9%</td>
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
<td align="right">72,909,161</td>
<td align="right">1.3%</td>
<td align="right">62,215,343</td>
<td align="right">1.2%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">324,632,157</td>
<td align="right">5.9%</td>
<td align="right">316,287,118</td>
<td align="right">5.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,082,509,945</td>
<td align="right">92.7%</td>
<td align="right">5,013,216,884</td>
<td align="right">93.0%</td>
<td align="right">-1.4%</td>
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
<td align="right">1,594,517</td>
<td align="right">73.1%</td>
<td align="right">1,392,823</td>
<td align="right">72.1%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">587,614</td>
<td align="right">26.9%</td>
<td align="right">538,721</td>
<td align="right">27.9%</td>
<td align="right">-8.3%</td>
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
<td align="right">55,969</td>
<td align="right">9.5%</td>
<td align="right">8,980</td>
<td align="right">1.7%</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">402</td>
<td align="right">0.1%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">6,816</td>
<td align="right">1.2%</td>
<td align="right">6,136</td>
<td align="right">1.1%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">18,416</td>
<td align="right">3.1%</td>
<td align="right">17,939</td>
<td align="right">3.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,623</td>
<td align="right">2.0%</td>
<td align="right">11,497</td>
<td align="right">2.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">85,683</td>
<td align="right">14.6%</td>
<td align="right">85,343</td>
<td align="right">15.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,925</td>
<td align="right">3.4%</td>
<td align="right">19,886</td>
<td align="right">3.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">81,278</td>
<td align="right">13.8%</td>
<td align="right">81,258</td>
<td align="right">15.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">305,842</td>
<td align="right">52.0%</td>
<td align="right">305,840</td>
<td align="right">56.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
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
<td align="right">1,275,680</td>
<td align="right">0.1%</td>
<td align="right">464,953</td>
<td align="right">0.0%</td>
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
<td align="right">1,270,809,443</td>
<td align="right">99.9%</td>
<td align="right">1,268,836,398</td>
<td align="right">100.0%</td>
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
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
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
<td align="right">2,466</td>
<td align="right">6.2%</td>
<td align="right">2,094</td>
<td align="right">5.3%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,237</td>
<td align="right">93.8%</td>
<td align="right">37,213</td>
<td align="right">94.7%</td>
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
<td align="right">1,772</td>
<td align="right">71.9%</td>
<td align="right">1,400</td>
<td align="right">66.9%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">15.3%</td>
<td align="right">378</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">316</td>
<td align="right">12.8%</td>
<td align="right">316</td>
<td align="right">15.1%</td>
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
<td align="right">3,630,518,147</td>
<td align="right">3.0%</td>
<td align="right">3,398,075,266</td>
<td align="right">2.9%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,145,947,474</td>
<td align="right">0.9%</td>
<td align="right">1,090,621,676</td>
<td align="right">0.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">71,648,253,179</td>
<td align="right">58.3%</td>
<td align="right">68,441,087,125</td>
<td align="right">58.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">46,519,405,483</td>
<td align="right">37.8%</td>
<td align="right">44,479,419,031</td>
<td align="right">37.9%</td>
<td align="right">-4.4%</td>
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
<td align="right">220,430,650</td>
<td align="right">6.8%</td>
<td align="right">180,304,205</td>
<td align="right">6.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">122,882,522</td>
<td align="right">3.8%</td>
<td align="right">106,515,945</td>
<td align="right">3.5%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">198,025,212</td>
<td align="right">6.1%</td>
<td align="right">177,778,427</td>
<td align="right">5.9%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">126,450,463</td>
<td align="right">3.9%</td>
<td align="right">115,664,413</td>
<td align="right">3.8%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,465,188</td>
<td align="right">3.3%</td>
<td align="right">98,102,270</td>
<td align="right">3.3%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,174,817,914</td>
<td align="right">36.4%</td>
<td align="right">1,100,340,022</td>
<td align="right">36.5%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">579,893,223</td>
<td align="right">18.0%</td>
<td align="right">550,864,541</td>
<td align="right">18.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">167,366,537</td>
<td align="right">5.2%</td>
<td align="right">160,806,891</td>
<td align="right">5.3%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">324,632,157</td>
<td align="right">10.1%</td>
<td align="right">316,287,118</td>
<td align="right">10.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,260,696</td>
<td align="right">4.0%</td>
<td align="right">129,260,696</td>
<td align="right">4.3%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">33,711,677</td>
<td align="right">2.9%</td>
<td align="right">28,200,720</td>
<td align="right">2.6%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">32,436,922</td>
<td align="right">2.8%</td>
<td align="right">27,789,962</td>
<td align="right">2.5%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">103,212,182</td>
<td align="right">9.0%</td>
<td align="right">91,735,422</td>
<td align="right">8.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">189,693,899</td>
<td align="right">16.6%</td>
<td align="right">173,500,182</td>
<td align="right">15.9%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,342,634</td>
<td align="right">2.7%</td>
<td align="right">30,168,958</td>
<td align="right">2.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,247,188</td>
<td align="right">2.7%</td>
<td align="right">30,202,151</td>
<td align="right">2.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">83,403,062</td>
<td align="right">7.3%</td>
<td align="right">81,497,616</td>
<td align="right">7.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">79,640,674</td>
<td align="right">6.9%</td>
<td align="right">78,131,238</td>
<td align="right">7.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,308,414</td>
<td align="right">6.0%</td>
<td align="right">67,144,899</td>
<td align="right">6.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">238,533,247</td>
<td align="right">20.8%</td>
<td align="right">237,166,110</td>
<td align="right">21.7%</td>
<td align="right">-0.6%</td>
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
<td align="right">463,651,742</td>
<td align="right">6.1%</td>
<td align="right">462,228,785</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,354,772,061</td>
<td align="right">84.2%</td>
<td align="right">6,336,785,200</td>
<td align="right">84.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,679,160,884</td>
<td align="right">75.2%</td>
<td align="right">5,663,487,570</td>
<td align="right">75.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,282,480,443</td>
<td align="right">17.0%</td>
<td align="right">1,280,461,956</td>
<td align="right">17.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,286,754,660</td>
<td align="right">17.0%</td>
<td align="right">1,284,736,173</td>
<td align="right">17.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,871,176,070</td>
<td align="right">24.8%</td>
<td align="right">1,868,914,026</td>
<td align="right">24.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,871,176,070</td>
<td align="right">24.8%</td>
<td align="right">1,868,914,026</td>
<td align="right">24.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">307,733,768</td>
<td align="right">4.1%</td>
<td align="right">307,508,808</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,421,410</td>
<td align="right">7.7%</td>
<td align="right">584,177,853</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,569,068</td>
<td align="right">0.9%</td>
<td align="right">71,547,079</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,814,679</td>
<td align="right">0.3%</td>
<td align="right">23,808,602</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,223,902</td>
<td align="right">0.1%</td>
<td align="right">4,223,902</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">131,916,029</td>
<td align="right">1.7%</td>
<td align="right">131,916,029</td>
<td align="right">1.8%</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,322,975,840</td>
<td align="right">1.2%</td>
<td align="right">1,253,364,827</td>
<td align="right">1.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">3,760,289,358</td>
<td align="right">3.8%</td>
<td align="right">3,612,812,572</td>
<td align="right">3.7%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">29,552,166,644</td>
<td align="right">29.8%</td>
<td align="right">28,712,280,485</td>
<td align="right">29.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">38,799,085,008</td>
<td align="right">34.0%</td>
<td align="right">38,034,467,388</td>
<td align="right">33.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">40,849,915,447</td>
<td align="right">41.2%</td>
<td align="right">41,636,786,887</td>
<td align="right">42.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">50,284,662,501</td>
<td align="right">44.1%</td>
<td align="right">50,978,580,860</td>
<td align="right">44.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,874,532</td>
<td align="right"></td>
<td align="right">58,382,219</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">64,708,870</td>
<td align="right"></td>
<td align="right">64,183,131</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,530,021</td>
<td align="right"></td>
<td align="right">6,495,492</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,127,351,789</td>
<td align="right"></td>
<td align="right">2,137,848,067</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,911,605,069</td>
<td align="right">25.1%</td>
<td align="right">24,977,305,207</td>
<td align="right">25.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,717,617</td>
<td align="right"></td>
<td align="right">177,375,689</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,604,946</td>
<td align="right">0.0%</td>
<td align="right">6,616,553</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,892,884,058</td>
<td align="right"></td>
<td align="right">2,888,834,955</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,824,602,603</td>
<td align="right">29.1%</td>
<td align="right">5,816,828,871</td>
<td align="right">29.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,902,924,884</td>
<td align="right">29.5%</td>
<td align="right">5,895,226,151</td>
<td align="right">29.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,476,887,819</td>
<td align="right"></td>
<td align="right">6,469,058,785</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,717,335</td>
<td align="right">0.4%</td>
<td align="right">71,780,727</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,139,562,328</td>
<td align="right"></td>
<td align="right">14,127,888,922</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,137,885,263</td>
<td align="right">70.5%</td>
<td align="right">14,126,233,258</td>
<td align="right">70.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,632,536,056</td>
<td align="right">20.7%</td>
<td align="right">23,637,112,525</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,639,155</td>
<td align="right">2.0%</td>
<td align="right">3,639,155</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,383</td>
<td align="right">0.0%</td>
<td align="right">4,383</td>
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
<td align="right">367,241</td>
<td align="right">94,992,586</td>
<td align="right">9,739,216,679</td>
<td align="right">801,883,122</td>
<td align="right">758,102,612</td>
<td align="right">366,933</td>
<td align="right">94,312,587</td>
<td align="right">9,781,726,368</td>
<td align="right">808,708,313</td>
<td align="right">758,635,100</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,934</td>
<td align="right">4,304,865</td>
<td align="right">5,703,368,378</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,304,865</td>
<td align="right">5,703,542,370</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">641</td>
<td align="right">1.7%</td>
<td align="right">4,846</td>
<td align="right">3.4%</td>
<td align="right">656.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">1,144</td>
<td align="right">0.1%</td>
<td align="right">528.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">949</td>
<td align="right">0.1%</td>
<td align="right">374.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">36,939</td>
<td align="right">8.4%</td>
<td align="right">142,638</td>
<td align="right">18.6%</td>
<td align="right">286.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">900</td>
<td align="right">0.2%</td>
<td align="right">3,292</td>
<td align="right">0.4%</td>
<td align="right">265.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,339</td>
<td align="right">0.3%</td>
<td align="right">3,364</td>
<td align="right">0.4%</td>
<td align="right">151.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">3,185</td>
<td align="right">0.7%</td>
<td align="right">6,893</td>
<td align="right">0.9%</td>
<td align="right">116.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">442,297</td>
<td align="right"></td>
<td align="right">768,459</td>
<td align="right"></td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">134,794</td>
<td align="right">30.5%</td>
<td align="right">231,648</td>
<td align="right">30.1%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">223,453</td>
<td align="right">50.5%</td>
<td align="right">330,462</td>
<td align="right">43.0%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">46,911</td>
<td align="right">10.6%</td>
<td align="right">62,762</td>
<td align="right">8.2%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">245,997,436,689</td>
<td align="right">6,381.9%</td>
<td align="right">258,074,943,413</td>
<td align="right">6,405.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,854,606,644</td>
<td align="right"></td>
<td align="right">4,029,163,578</td>
<td align="right"></td>
<td align="right">4.5%</td>
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
<td align="right">31,185</td>
<td align="right">84.4%</td>
<td align="right">128,714</td>
<td align="right">90.2%</td>
<td align="right">312.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">36,939</td>
<td align="right"></td>
<td align="right">142,638</td>
<td align="right"></td>
<td align="right">286.1%</td>
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
<td align="right">208</td>
<td align="right">0.1%</td>
<td align="right">208 / 0 !!</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">4,083,712</td>
<td align="right">1.0%</td>
<td align="right">232,841,216</td>
<td align="right">15.0%</td>
<td align="right">5,601.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">66,866,251</td>
<td align="right">16.0%</td>
<td align="right">284,537,203</td>
<td align="right">18.3%</td>
<td align="right">325.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">8,839,160</td>
<td align="right">2.1%</td>
<td align="right">33,066,480</td>
<td align="right">2.1%</td>
<td align="right">274.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">418,713,600</td>
<td align="right"></td>
<td align="right">1,553,063,936</td>
<td align="right"></td>
<td align="right">270.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">343,008,189</td>
<td align="right">81.9%</td>
<td align="right">1,235,460,253</td>
<td align="right">79.5%</td>
<td align="right">260.2%</td>
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
<td align="left">6,903</td>
<td align="right">22.1%</td>
<td align="left">26,153</td>
<td align="right">20.3%</td>
<td align="right">278.9%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">9,591</td>
<td align="right">30.8%</td>
<td align="left">50,096</td>
<td align="right">38.9%</td>
<td align="right">422.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,657</td>
<td align="right">27.8%</td>
<td align="left">33,800</td>
<td align="right">26.3%</td>
<td align="right">290.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,142</td>
<td align="right">13.3%</td>
<td align="left">14,311</td>
<td align="right">11.1%</td>
<td align="right">245.5%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,732</td>
<td align="right">5.6%</td>
<td align="left">3,593</td>
<td align="right">2.8%</td>
<td align="right">107.4%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">160</td>
<td align="right">0.5%</td>
<td align="left">761</td>
<td align="right">0.6%</td>
<td align="right">375.6%</td>
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
<td align="right">1,414</td>
<td align="right">3.8%</td>
<td align="right">5,988</td>
<td align="right">4.2%</td>
<td align="right">323.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,565</td>
<td align="right">4.2%</td>
<td align="right">8,190</td>
<td align="right">5.7%</td>
<td align="right">423.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,519</td>
<td align="right">14.9%</td>
<td align="right">18,908</td>
<td align="right">13.3%</td>
<td align="right">242.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,426</td>
<td align="right">28.2%</td>
<td align="right">53,772</td>
<td align="right">37.7%</td>
<td align="right">415.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,580</td>
<td align="right">20.5%</td>
<td align="right">28,239</td>
<td align="right">19.8%</td>
<td align="right">272.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,155</td>
<td align="right">19.4%</td>
<td align="right">19,351</td>
<td align="right">13.6%</td>
<td align="right">170.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,773</td>
<td align="right">7.5%</td>
<td align="right">6,318</td>
<td align="right">4.4%</td>
<td align="right">127.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">507</td>
<td align="right">1.4%</td>
<td align="right">1,872</td>
<td align="right">1.3%</td>
<td align="right">269.2%</td>
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
<td align="right">812</td>
<td align="right">2.2%</td>
<td align="right">3,038</td>
<td align="right">2.1%</td>
<td align="right">274.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,093</td>
<td align="right">3.0%</td>
<td align="right">5,734</td>
<td align="right">4.0%</td>
<td align="right">424.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,795</td>
<td align="right">7.6%</td>
<td align="right">11,448</td>
<td align="right">8.0%</td>
<td align="right">309.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,183</td>
<td align="right">27.6%</td>
<td align="right">47,904</td>
<td align="right">33.6%</td>
<td align="right">370.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,597</td>
<td align="right">23.3%</td>
<td align="right">35,634</td>
<td align="right">25.0%</td>
<td align="right">314.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,303</td>
<td align="right">11.6%</td>
<td align="right">16,097</td>
<td align="right">11.3%</td>
<td align="right">274.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,872</td>
<td align="right">7.8%</td>
<td align="right">7,287</td>
<td align="right">5.1%</td>
<td align="right">153.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">530</td>
<td align="right">1.4%</td>
<td align="right">1,572</td>
<td align="right">1.1%</td>
<td align="right">196.6%</td>
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
<td align="left">_ERROR_POP_N</td>
<td align="right">23,582</td>
<td align="right">526,313</td>
<td align="right">2,131.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">476,163</td>
<td align="right">1,677.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">85,608</td>
<td align="right">1,369,279</td>
<td align="right">1,499.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,680</td>
<td align="right">835,380</td>
<td align="right">886.5%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">10,713</td>
<td align="right">722.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">534,262</td>
<td align="right">611.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,220,144</td>
<td align="right">16,373,970</td>
<td align="right">408.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">13,260,066</td>
<td align="right">51,740,184</td>
<td align="right">290.2%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">158,441</td>
<td align="right">527,491</td>
<td align="right">232.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">1,193,471</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">14,301,000</td>
<td align="right">191.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">98,457,639</td>
<td align="right">223,383,604</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">98,457,639</td>
<td align="right">223,383,604</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">99,153,579</td>
<td align="right">224,908,484</td>
<td align="right">126.8%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,840,209</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">597,349</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,597,702</td>
<td align="right">3,115,136</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">576,900</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,220,780</td>
<td align="right">5,406,840</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">106,030</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,961,160</td>
<td align="right">7,560,044</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">202,706,849</td>
<td align="right">289,044,846</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">149,938,351</td>
<td align="right">211,836,020</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">6,101,950</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,311,576</td>
<td align="right">1,850,146</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,073,505</td>
<td align="right">69,164,383</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,073,505</td>
<td align="right">69,140,323</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">242,532</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">35,266,120</td>
<td align="right">24,532,226</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,794,181</td>
<td align="right">90,201,493</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,972,064</td>
<td align="right">3,780,106</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,646,825</td>
<td align="right">77,933,895</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,171,220</td>
<td align="right">4,003,460</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">316,917,034</td>
<td align="right">400,048,544</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,677,032</td>
<td align="right">173,859,464</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,374,659</td>
<td align="right">9,077,367</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,614,620</td>
<td align="right">8,118,800</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">74,057,780</td>
<td align="right">90,409,593</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">32,996,194</td>
<td align="right">40,259,149</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">339,252,499</td>
<td align="right">411,132,056</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">106,993,748</td>
<td align="right">129,464,402</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">43,760,440</td>
<td align="right">52,798,761</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,689,455</td>
<td align="right">45,396,657</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,957,511</td>
<td align="right">8,350,609</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,571,606</td>
<td align="right">13,729,463</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,922,208</td>
<td align="right">4,649,654</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">46,485,112</td>
<td align="right">54,973,194</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">65,697,542</td>
<td align="right">77,558,822</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">141,870,917</td>
<td align="right">166,432,208</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">110,785,869</td>
<td align="right">129,853,703</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,012,080</td>
<td align="right">3,510,924</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">28,704,759</td>
<td align="right">33,153,406</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,427,979,858</td>
<td align="right">1,641,303,688</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,428,444,273</td>
<td align="right">1,641,520,135</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">18,814,170</td>
<td align="right">21,588,006</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">296,944,110</td>
<td align="right">340,014,684</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">162,619,918</td>
<td align="right">185,391,628</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,003,931</td>
<td align="right">5,702,411</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">296,755,785</td>
<td align="right">335,737,285</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">3,026,937</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">643,996,033</td>
<td align="right">727,466,989</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">162,828,532</td>
<td align="right">183,194,215</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,001,422</td>
<td align="right">13,489,396</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,001,422</td>
<td align="right">13,489,396</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">106,388,800</td>
<td align="right">119,404,500</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">486,595,537</td>
<td align="right">546,043,709</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">41,429,630</td>
<td align="right">46,426,935</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">193,394,637</td>
<td align="right">216,660,020</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,113,485</td>
<td align="right">48,270,313</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">11,424,529</td>
<td align="right">12,780,680</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">281,228,492</td>
<td align="right">313,892,577</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">73,677,990</td>
<td align="right">81,482,491</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">564,221,893</td>
<td align="right">623,925,090</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">144,778,189</td>
<td align="right">159,667,614</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">645,273,570</td>
<td align="right">711,595,402</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">116,173,764</td>
<td align="right">128,077,998</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">18,915,070</td>
<td align="right">20,838,990</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">18,915,070</td>
<td align="right">20,838,990</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">54,924,324</td>
<td align="right">60,179,097</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">700,253,798</td>
<td align="right">766,439,977</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,958,738,636</td>
<td align="right">3,235,840,157</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,713,621</td>
<td align="right">37,890,102</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">153,157,508</td>
<td align="right">167,162,722</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">317,091,300</td>
<td align="right">346,029,093</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,253,780,151</td>
<td align="right">1,364,821,835</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,253,780,151</td>
<td align="right">1,364,821,835</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,241,778,729</td>
<td align="right">1,351,332,439</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">35,095,856</td>
<td align="right">32,017,454</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">168,746,470</td>
<td align="right">183,280,939</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">29,768,070</td>
<td align="right">32,330,071</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">29,768,070</td>
<td align="right">32,330,071</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">227,718,937</td>
<td align="right">247,309,408</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,176,665,969</td>
<td align="right">1,276,450,979</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">144,953,608</td>
<td align="right">156,828,258</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">445,968,892</td>
<td align="right">482,405,944</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,052,929</td>
<td align="right">6,536,667</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">396,829,742</td>
<td align="right">428,031,706</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">36,762,038</td>
<td align="right">39,643,920</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">452,550,515</td>
<td align="right">486,114,385</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,025,143,415</td>
<td align="right">4,321,974,202</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">253,470,175</td>
<td align="right">272,128,275</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">235,251,428</td>
<td align="right">252,487,293</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">444,490,589</td>
<td align="right">476,678,606</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,390,939</td>
<td align="right">59,392,409</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,549,100</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">38,051,764</td>
<td align="right">40,582,261</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,776,129,929</td>
<td align="right">8,284,656,076</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">256,299,201</td>
<td align="right">272,941,593</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">42,348,720</td>
<td align="right">45,068,020</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">43,982,703</td>
<td align="right">46,759,154</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,392,283</td>
<td align="right">58,873,121</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">808,172,234</td>
<td align="right">858,918,386</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">338,908,369</td>
<td align="right">360,062,807</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">206,850,103</td>
<td align="right">193,993,000</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,822,620</td>
<td align="right">2,996,900</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,822,620</td>
<td align="right">2,996,900</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,211,388,790</td>
<td align="right">1,285,745,030</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,775,789,287</td>
<td align="right">3,995,928,864</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">966,667,557</td>
<td align="right">1,022,563,695</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">399,836,526</td>
<td align="right">422,791,683</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">966,530,417</td>
<td align="right">1,021,866,741</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">541,690,328</td>
<td align="right">572,577,162</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,306,907</td>
<td align="right">152,448,024</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,462,984,798</td>
<td align="right">3,658,215,995</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,476,141</td>
<td align="right">50,097,627</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,297,640,951</td>
<td align="right">37,245,631,924</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,793,583,118</td>
<td align="right">1,891,698,854</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">100,975,970</td>
<td align="right">106,490,557</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">357,815,241</td>
<td align="right">377,347,274</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,106,940</td>
<td align="right">44,356,954</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,327,180,931</td>
<td align="right">42,392,883,395</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">390,244,432</td>
<td align="right">410,128,227</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,417,240,723</td>
<td align="right">1,485,536,818</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,763,171,905</td>
<td align="right">3,942,666,724</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">412,052,824</td>
<td align="right">431,597,322</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,193,684</td>
<td align="right">48,358,436</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,394,817</td>
<td align="right">49,608,217</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,870,311,560</td>
<td align="right">1,957,377,605</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,819,487,206</td>
<td align="right">3,996,619,811</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">169,038,286</td>
<td align="right">161,258,910</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,854,606,644</td>
<td align="right">4,029,163,578</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">236,847,542</td>
<td align="right">247,480,210</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">428,218,018</td>
<td align="right">447,354,111</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,295,836,310</td>
<td align="right">1,351,548,950</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,006,876,445</td>
<td align="right">2,092,819,109</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,794,170,090</td>
<td align="right">2,913,776,176</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,803,742,945</td>
<td align="right">1,880,203,253</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,078,138,952</td>
<td align="right">1,123,119,603</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,872,908,460</td>
<td align="right">2,992,591,823</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">467,890,637</td>
<td align="right">487,055,516</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,230,122,013</td>
<td align="right">1,280,433,661</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">529,087,310</td>
<td align="right">550,636,075</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,337,233,822</td>
<td align="right">1,389,869,382</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,165,435,695</td>
<td align="right">2,248,717,419</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">447,902,296</td>
<td align="right">464,767,712</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">447,902,296</td>
<td align="right">464,767,712</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,944,384,647</td>
<td align="right">11,353,464,593</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,973,269,909</td>
<td align="right">7,232,247,706</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">426,944,037</td>
<td align="right">442,508,729</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">182,526,544</td>
<td align="right">175,957,034</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,003,700</td>
<td align="right">3,104,521</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,309,576,004</td>
<td align="right">6,520,109,092</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,239,990,502</td>
<td align="right">2,311,520,042</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">188,493,771</td>
<td align="right">194,423,562</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,549,878</td>
<td align="right">121,159,834</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">249,694,147</td>
<td align="right">257,204,067</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,339,454</td>
<td align="right">661,383,545</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">757,567,708</td>
<td align="right">779,816,839</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,034,320</td>
<td align="right">75,133,240</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,111,896,433</td>
<td align="right">1,143,654,381</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,784,955</td>
<td align="right">536,660,498</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">352,930,430</td>
<td align="right">362,808,987</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,740,666</td>
<td align="right">1,241,383,106</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">69,571,391</td>
<td align="right">71,488,060</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">69,571,391</td>
<td align="right">71,488,060</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,139,983,372</td>
<td align="right">1,171,009,662</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,339,729,502</td>
<td align="right">1,376,064,897</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">39,466,304</td>
<td align="right">40,530,577</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,339,524,257</td>
<td align="right">2,399,936,863</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,469,624,667</td>
<td align="right">2,532,850,060</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">136,640,971</td>
<td align="right">140,128,578</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">225,698,868</td>
<td align="right">231,419,198</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">17,372,080</td>
<td align="right">17,802,240</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">847,283,418</td>
<td align="right">867,886,926</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,348,895,214</td>
<td align="right">4,453,602,450</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">494,153,654</td>
<td align="right">505,770,070</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,960,962</td>
<td align="right">20,410,009</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,546,456,605</td>
<td align="right">1,511,719,460</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,874,104</td>
<td align="right">39,704,582</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">254,837,086</td>
<td align="right">260,173,927</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,002,630,307</td>
<td align="right">1,022,689,912</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">957,305,821</td>
<td align="right">976,071,447</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">150,369,864</td>
<td align="right">147,557,546</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,835,430,452</td>
<td align="right">2,886,897,243</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,397,435,108</td>
<td align="right">4,474,039,798</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">730,099,878</td>
<td align="right">742,171,337</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,907,960,521</td>
<td align="right">3,972,337,828</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,115,122</td>
<td align="right">1,186,123,287</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">403,763,061</td>
<td align="right">410,288,420</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">39,305,011</td>
<td align="right">39,920,390</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,454,969,360</td>
<td align="right">2,490,945,514</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">911,776,396</td>
<td align="right">923,179,753</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">593,442,788</td>
<td align="right">600,805,625</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">460,952,104</td>
<td align="right">466,667,319</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">911,776,396</td>
<td align="right">922,452,756</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">584,418,003</td>
<td align="right">591,241,504</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,052,268,311</td>
<td align="right">1,064,305,188</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">976,764,571</td>
<td align="right">987,820,863</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">491,292,795</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">769,932,726</td>
<td align="right">778,338,734</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">46,728,468</td>
<td align="right">47,174,069</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">1,557,554,920</td>
<td align="right">1,571,556,857</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,546,340</td>
<td align="right">60,066,604</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,342,482,500</td>
<td align="right">1,353,223,539</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">749,182,847</td>
<td align="right">755,054,485</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">440,104,015</td>
<td align="right">443,520,451</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">440,104,015</td>
<td align="right">443,520,451</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,468,814,716</td>
<td align="right">1,479,461,700</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,376,320</td>
<td align="right">112,179,719</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">71,532,780</td>
<td align="right">71,992,800</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">123,812,404</td>
<td align="right">124,576,783</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">971,076,168</td>
<td align="right">976,632,149</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,058,846</td>
<td align="right">750,084,486</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,195,783,997</td>
<td align="right">1,201,469,069</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">93,891,060</td>
<td align="right">94,132,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,297,335,052</td>
<td align="right">1,299,048,357</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,012,332,418</td>
<td align="right">1,011,276,605</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,997,705,254</td>
<td align="right">1,998,639,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">138,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">138,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">81,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">65,928</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_THIRD_NULL</td>
<td align="right"></td>
<td align="right">40,509</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">15,897</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">10,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TYPE_1</td>
<td align="right"></td>
<td align="right">4,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">3,414</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TUPLE_1</td>
<td align="right"></td>
<td align="right">597</td>
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
<td align="right">1,781</td>
<td align="right">6,877</td>
<td align="right">286.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,365</td>
<td align="right">37,330</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,981</td>
<td align="right">23,425</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">1,417</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right"></td>
<td align="right">21</td>
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
<td align="right">401</td>
<td align="right">708</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">401</td>
<td align="right">708</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,239</td>
<td align="right">22,239</td>
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
<td align="right">714</td>
<td align="right">714</td>
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
<td align="right">901</td>
<td align="right">901</td>
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
<td align="right">2,337</td>
<td align="right">2,337</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-02
