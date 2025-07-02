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
<td align="right">504,310</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,322,630</td>
<td align="right">89,967,541</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,265,068</td>
<td align="right">956,119</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,075,598</td>
<td align="right">39,547,538</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,349,805</td>
<td align="right">1,033,866</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,644,738</td>
<td align="right">80,187,204</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">56,417,177</td>
<td align="right">47,348,133</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,807,652</td>
<td align="right">2,368,674</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220,699,126</td>
<td align="right">186,993,363</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,587,473</td>
<td align="right">3,110,696</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">376,588,810</td>
<td align="right">328,339,785</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">150,122,923</td>
<td align="right">131,452,752</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">314,166,728</td>
<td align="right">275,655,278</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">461,046,077</td>
<td align="right">406,285,206</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">111,924,190</td>
<td align="right">100,091,027</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">126,964,985</td>
<td align="right">114,610,478</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">202,341,510</td>
<td align="right">182,954,017</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,097,872</td>
<td align="right">33,548,194</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">123,010,138</td>
<td align="right">111,281,620</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,105,223,871</td>
<td align="right">1,000,082,481</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">14,315,303</td>
<td align="right">13,107,486</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,840,180</td>
<td align="right">2,604,900</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">187,345,539</td>
<td align="right">171,948,817</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">55,931,808</td>
<td align="right">51,456,790</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">77,865,122</td>
<td align="right">71,808,695</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">903,802,655</td>
<td align="right">833,645,230</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">198,025,212</td>
<td align="right">183,255,071</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">165,915,658</td>
<td align="right">154,489,090</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,758,604</td>
<td align="right">46,398,959</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">180,375,961</td>
<td align="right">168,465,891</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">180,668,101</td>
<td align="right">168,878,171</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">78,915</td>
<td align="right">73,770</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">710,099,548</td>
<td align="right">665,083,237</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,513,661,969</td>
<td align="right">2,360,055,968</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,163,920</td>
<td align="right">10,509,231</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,560,100</td>
<td align="right">99,620,053</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">402,673,928</td>
<td align="right">380,081,559</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">148,539,462</td>
<td align="right">140,420,741</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,175,652,389</td>
<td align="right">1,111,782,703</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">277,567,008</td>
<td align="right">263,129,355</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,288,719</td>
<td align="right">30,636,779</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">127,298,230</td>
<td align="right">120,831,812</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,545,028</td>
<td align="right">5,264,949</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,430,866,539</td>
<td align="right">1,360,750,884</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">127,641,316</td>
<td align="right">121,418,123</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">413,419,054</td>
<td align="right">393,916,945</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">855,458,697</td>
<td align="right">895,698,164</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,357,151,603</td>
<td align="right">1,293,476,699</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">126,693,683</td>
<td align="right">121,032,921</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">745,439,463</td>
<td align="right">714,322,742</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">495,630,664</td>
<td align="right">475,011,187</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">911,268,516</td>
<td align="right">874,121,927</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,000,672,710</td>
<td align="right">5,757,642,703</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,865,042,200</td>
<td align="right">3,713,478,244</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,844,466,412</td>
<td align="right">20,995,615,045</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,245,700</td>
<td align="right">6,003,780</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,521,988</td>
<td align="right">4,348,038</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,729,160</td>
<td align="right">9,377,530</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">686,467,498</td>
<td align="right">661,820,892</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">308,783,005</td>
<td align="right">297,739,585</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">543,887,020</td>
<td align="right">524,606,585</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">287,085,488</td>
<td align="right">277,322,354</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">42,342,411</td>
<td align="right">40,925,532</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,408,781</td>
<td align="right">456,932,024</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,003,558,710</td>
<td align="right">970,810,708</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">150,056,920</td>
<td align="right">145,237,182</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,587,487</td>
<td align="right">9,288,456</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">169,692,872</td>
<td align="right">164,406,083</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">70,279,273</td>
<td align="right">68,097,855</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,127,590,624</td>
<td align="right">1,092,964,346</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">379,033,731</td>
<td align="right">367,653,777</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,750,548,853</td>
<td align="right">4,615,283,283</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,058</td>
<td align="right">544,279</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">162,258,182</td>
<td align="right">157,904,634</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,319,826,786</td>
<td align="right">5,178,423,098</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">204,694,960</td>
<td align="right">199,392,974</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">77,570,208</td>
<td align="right">75,572,867</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,307,060</td>
<td align="right">47,092,291</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,022,498,980</td>
<td align="right">997,189,937</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">279,814,286</td>
<td align="right">273,158,345</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,160,271</td>
<td align="right">83,204,291</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,194,260</td>
<td align="right">261,032,266</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">460,495,946</td>
<td align="right">450,126,032</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,200,812,186</td>
<td align="right">4,111,970,105</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,658,584,614</td>
<td align="right">1,624,158,299</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">52,659,895</td>
<td align="right">51,616,957</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">69,122,262</td>
<td align="right">67,771,425</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,367,235,774</td>
<td align="right">2,321,816,586</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">208,029,113</td>
<td align="right">204,318,628</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,134,973,425</td>
<td align="right">3,080,766,894</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">355,102,174</td>
<td align="right">361,177,764</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,749,042</td>
<td align="right">242,554,280</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">509,533,514</td>
<td align="right">500,890,179</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">561,774,783</td>
<td align="right">552,351,190</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">115,592,412</td>
<td align="right">113,667,732</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">505,997,641</td>
<td align="right">497,607,084</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">340,970,920</td>
<td align="right">335,476,306</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,093,418,408</td>
<td align="right">3,043,738,759</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">179,456,344</td>
<td align="right">176,580,136</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">43,268,121</td>
<td align="right">42,584,815</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,886,278,891</td>
<td align="right">2,840,850,456</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">691,860,214</td>
<td align="right">681,094,289</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">582,617,664</td>
<td align="right">573,666,275</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,002,984</td>
<td align="right">25,604,134</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">112,619,552</td>
<td align="right">110,962,975</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,880,274</td>
<td align="right">61,760,041</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,653,126,775</td>
<td align="right">5,572,574,242</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">216,294,785</td>
<td align="right">213,363,985</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,155,044,767</td>
<td align="right">3,112,793,440</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">290,235,754</td>
<td align="right">286,478,483</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">21,547,631</td>
<td align="right">21,818,060</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,741,390</td>
<td align="right">61,025,308</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,859,527,763</td>
<td align="right">2,827,737,859</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">834,225,425</td>
<td align="right">825,476,322</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,536,315</td>
<td align="right">280,768,480</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">325,444,414</td>
<td align="right">322,312,642</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">82,162,534</td>
<td align="right">81,373,529</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">256,917,370</td>
<td align="right">254,482,575</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,531,042</td>
<td align="right">69,884,460</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,475,625,014</td>
<td align="right">1,462,470,669</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">105,475,401</td>
<td align="right">104,538,565</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">364,805,250</td>
<td align="right">361,619,160</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">110,571,492</td>
<td align="right">109,627,240</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,923,024,292</td>
<td align="right">5,877,907,926</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,113,365</td>
<td align="right">74,555,131</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,914,678</td>
<td align="right">41,604,483</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">622,782,529</td>
<td align="right">618,539,605</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">523,694,640</td>
<td align="right">520,202,830</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,175,359,190</td>
<td align="right">1,167,802,977</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">141,656,128</td>
<td align="right">140,910,174</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">144,322,670</td>
<td align="right">143,639,364</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">97,368,923</td>
<td align="right">96,922,104</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,179,477</td>
<td align="right">70,859,076</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,716,461</td>
<td align="right">10,675,703</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">368,593,190</td>
<td align="right">367,302,733</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">996,950,166</td>
<td align="right">993,959,693</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">292,986,322</td>
<td align="right">292,154,088</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,463,459</td>
<td align="right">3,459,004</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,430,767</td>
<td align="right">28,449,799</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">148,232,665</td>
<td align="right">148,324,090</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">378,359,772</td>
<td align="right">378,132,809</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,863,001</td>
<td align="right">68,831,142</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">214,755,660</td>
<td align="right">214,673,465</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,328,501</td>
<td align="right">332,383,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,522,603</td>
<td align="right">13,524,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,679,416</td>
<td align="right">6,680,232</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,751,476</td>
<td align="right">70,746,021</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,158</td>
<td align="right">14,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,044</td>
<td align="right">92,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,107,987,306</td>
<td align="right">1,108,040,901</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,168,904</td>
<td align="right">21,169,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,444,509</td>
<td align="right">21,444,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,444,530</td>
<td align="right">21,444,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106,356</td>
<td align="right">106,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,688,509</td>
<td align="right">114,689,754</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,330</td>
<td align="right">3,100,361</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">324,432</td>
<td align="right">324,430</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,278,985</td>
<td align="right">6,279,017</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,580,198</td>
<td align="right">1,580,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,622,717</td>
<td align="right">15,622,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,928,080</td>
<td align="right">35,928,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">314,669,797</td>
<td align="right">314,669,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">312,619,709</td>
<td align="right">312,619,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,719,955</td>
<td align="right">418,720,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,082,570</td>
<td align="right">155,082,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,866,491,065</td>
<td align="right">1,866,490,894</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,478,601</td>
<td align="right">591,478,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,554,186</td>
<td align="right">302,554,186</td>
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
<td align="left">DICT_UPDATE</td>
<td align="right">23,354</td>
<td align="right">23,354</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,519,872</td>
<td align="right">0.4%</td>
<td align="right">69,272,460</td>
<td align="right">0.4%</td>
<td align="right">5.7%</td>
</tr>
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
<td align="right">1,110,998,442</td>
<td align="right">6.1%</td>
<td align="right">-5.4%</td>
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
<td align="right">16,891,665,583</td>
<td align="right">93.5%</td>
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
<td align="right">676,145</td>
<td align="right">32.7%</td>
<td align="right">626,046</td>
<td align="right">30.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,392,698</td>
<td align="right">67.3%</td>
<td align="right">1,463,449</td>
<td align="right">70.0%</td>
<td align="right">5.1%</td>
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
<td align="right">11,326</td>
<td align="right">1.8%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,182</td>
<td align="right">2.2%</td>
<td align="right">11,456</td>
<td align="right">1.8%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">5,212</td>
<td align="right">0.8%</td>
<td align="right">4,032</td>
<td align="right">0.6%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">25,123</td>
<td align="right">3.7%</td>
<td align="right">20,623</td>
<td align="right">3.3%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">39,634</td>
<td align="right">5.9%</td>
<td align="right">33,708</td>
<td align="right">5.4%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,139</td>
<td align="right">2.2%</td>
<td align="right">13,493</td>
<td align="right">2.2%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">4,864</td>
<td align="right">0.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">56,725</td>
<td align="right">8.4%</td>
<td align="right">52,022</td>
<td align="right">8.3%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">33,181</td>
<td align="right">4.9%</td>
<td align="right">30,831</td>
<td align="right">4.9%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,099</td>
<td align="right">8.7%</td>
<td align="right">55,621</td>
<td align="right">8.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,421</td>
<td align="right">2.3%</td>
<td align="right">14,654</td>
<td align="right">2.3%</td>
<td align="right">-5.0%</td>
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
<td align="left">multiply other</td>
<td align="right">4,813</td>
<td align="right">0.7%</td>
<td align="right">4,710</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,464</td>
<td align="right">1.3%</td>
<td align="right">8,296</td>
<td align="right">1.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">28,111</td>
<td align="right">4.2%</td>
<td align="right">27,599</td>
<td align="right">4.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">24,994</td>
<td align="right">3.7%</td>
<td align="right">24,546</td>
<td align="right">3.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">53,291</td>
<td align="right">7.9%</td>
<td align="right">52,583</td>
<td align="right">8.4%</td>
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
<td align="left">subscr defaultdict</td>
<td align="right">71,296</td>
<td align="right">10.5%</td>
<td align="right">70,684</td>
<td align="right">11.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">12,881</td>
<td align="right">1.9%</td>
<td align="right">12,781</td>
<td align="right">2.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">29,084</td>
<td align="right">4.3%</td>
<td align="right">28,916</td>
<td align="right">4.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,410</td>
<td align="right">0.2%</td>
<td align="right">1,414</td>
<td align="right">0.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,953</td>
<td align="right">1.6%</td>
<td align="right">10,933</td>
<td align="right">1.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">109,863</td>
<td align="right">16.2%</td>
<td align="right">109,821</td>
<td align="right">17.5%</td>
<td align="right">-0.0%</td>
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
<td align="right">0.4%</td>
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
<td align="left">and other</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">1,040</td>
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
<td align="left">subscr mappingproxy</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">560</td>
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
<td align="right">183,255,071</td>
<td align="right">100.0%</td>
<td align="right">-7.5%</td>
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
<td align="right">169,679,257</td>
<td align="right">1.4%</td>
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
<td align="right">167,366,537</td>
<td align="right">1.4%</td>
<td align="right">167,460,014</td>
<td align="right">1.4%</td>
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
<td align="right">12,199,679,343</td>
<td align="right">98.6%</td>
<td align="right">12,202,650,687</td>
<td align="right">98.6%</td>
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
<td align="right">3,799,279</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">685,118</td>
<td align="right">91.8%</td>
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
<td align="right">61,578</td>
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
<td align="right">120,791,239</td>
<td align="right">2.3%</td>
<td align="right">-4.5%</td>
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
<td align="right">1,311,032</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">5,195,815,587</td>
<td align="right">97.7%</td>
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
<td align="right">177,226</td>
<td align="right">66.2%</td>
<td align="right">175,687</td>
<td align="right">66.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">90,469</td>
<td align="right">33.8%</td>
<td align="right">90,332</td>
<td align="right">34.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,163</td>
<td align="right">0.7%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,827</td>
<td align="right">1.6%</td>
<td align="right">2,710</td>
<td align="right">1.5%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">12,209</td>
<td align="right">6.9%</td>
<td align="right">11,801</td>
<td align="right">6.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">16,374</td>
<td align="right">9.2%</td>
<td align="right">15,867</td>
<td align="right">9.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,404</td>
<td align="right">7.0%</td>
<td align="right">12,240</td>
<td align="right">7.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">64,443</td>
<td align="right">36.4%</td>
<td align="right">64,123</td>
<td align="right">36.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,368</td>
<td align="right">15.4%</td>
<td align="right">27,473</td>
<td align="right">15.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">11,543</td>
<td align="right">6.5%</td>
<td align="right">11,501</td>
<td align="right">6.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,246</td>
<td align="right">12.6%</td>
<td align="right">22,241</td>
<td align="right">12.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,212</td>
<td align="right">1.8%</td>
<td align="right">3,212</td>
<td align="right">1.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">122,882,522</td>
<td align="right">5.3%</td>
<td align="right">111,157,222</td>
<td align="right">4.8%</td>
<td align="right">-9.5%</td>
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
<td align="right">2,181,106,406</td>
<td align="right">95.1%</td>
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
<td align="right">1,369,433</td>
<td align="right">0.1%</td>
<td align="right">1,369,433</td>
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
<td align="right">111,946</td>
<td align="right">73.0%</td>
<td align="right">108,728</td>
<td align="right">72.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,395</td>
<td align="right">27.0%</td>
<td align="right">41,395</td>
<td align="right">27.6%</td>
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
<td align="right">18,057</td>
<td align="right">16.1%</td>
<td align="right">16,949</td>
<td align="right">15.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">29,930</td>
<td align="right">26.7%</td>
<td align="right">29,118</td>
<td align="right">26.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">32,976</td>
<td align="right">29.5%</td>
<td align="right">32,210</td>
<td align="right">29.6%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,983</td>
<td align="right">27.7%</td>
<td align="right">30,451</td>
<td align="right">28.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">186,745,600</td>
<td align="right">12.2%</td>
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
<td align="right">1,346,557,862</td>
<td align="right">82.6%</td>
<td align="right">1,284,499,521</td>
<td align="right">83.8%</td>
<td align="right">-4.6%</td>
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
<td align="right">61,495,822</td>
<td align="right">4.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">188,207</td>
<td align="right">13.4%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,241,612</td>
<td align="right">85.6%</td>
<td align="right">1,219,497</td>
<td align="right">86.6%</td>
<td align="right">-1.8%</td>
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
<td align="left">bytes</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">805</td>
<td align="right">0.4%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">15,385</td>
<td align="right">7.4%</td>
<td align="right">11,207</td>
<td align="right">6.0%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,577</td>
<td align="right">8.9%</td>
<td align="right">14,455</td>
<td align="right">7.7%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,710</td>
<td align="right">1.8%</td>
<td align="right">3,078</td>
<td align="right">1.6%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">18,907</td>
<td align="right">9.1%</td>
<td align="right">16,310</td>
<td align="right">8.7%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,042</td>
<td align="right">5.3%</td>
<td align="right">9,787</td>
<td align="right">5.2%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">10,328</td>
<td align="right">4.9%</td>
<td align="right">9,230</td>
<td align="right">4.9%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,675</td>
<td align="right">2.7%</td>
<td align="right">5,167</td>
<td align="right">2.7%</td>
<td align="right">-9.0%</td>
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
<td align="right">16,616</td>
<td align="right">8.8%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">79,545</td>
<td align="right">38.1%</td>
<td align="right">75,441</td>
<td align="right">40.1%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,926</td>
<td align="right">3.8%</td>
<td align="right">7,634</td>
<td align="right">4.1%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,336</td>
<td align="right">2.1%</td>
<td align="right">4,215</td>
<td align="right">2.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">11,401</td>
<td align="right">5.5%</td>
<td align="right">11,258</td>
<td align="right">6.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,829</td>
<td align="right">0.9%</td>
<td align="right">1,828</td>
<td align="right">1.0%</td>
<td align="right">-0.1%</td>
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
<td align="left">set</td>
<td align="right">12,352,657</td>
<td align="right">12,352,657 / 0 !!</td>
<td align="right">12,377,121</td>
<td align="right">12,377,121 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">173,420,310</td>
<td align="right">173,420,310 / 0 !!</td>
<td align="right">173,320,015</td>
<td align="right">173,320,015 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,653,518</td>
<td align="right">5,653,518 / 0 !!</td>
<td align="right">5,653,571</td>
<td align="right">5,653,571 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,698,672</td>
<td align="right">305,698,672 / 0 !!</td>
<td align="right">305,699,147</td>
<td align="right">305,699,147 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,055,957</td>
<td align="right">117,055,957 / 0 !!</td>
<td align="right">117,056,038</td>
<td align="right">117,056,038 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,989,877</td>
<td align="right">336,989,877 / 0 !!</td>
<td align="right">336,990,044</td>
<td align="right">336,990,044 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,677,864</td>
<td align="right">101,677,864 / 0 !!</td>
<td align="right">101,677,871</td>
<td align="right">101,677,871 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,399,895</td>
<td align="right">34,399,895 / 0 !!</td>
<td align="right">34,399,895</td>
<td align="right">34,399,895 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,799,014</td>
<td align="right">2,799,014 / 0 !!</td>
<td align="right">2,799,014</td>
<td align="right">2,799,014 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">648,781,221</td>
<td align="right">4.5%</td>
<td align="right">667,329,147</td>
<td align="right">4.6%</td>
<td align="right">2.9%</td>
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
<td align="right">570,974,344</td>
<td align="right">4.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">13,184,763,940</td>
<td align="right">91.4%</td>
<td align="right">-0.6%</td>
</tr>
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
<td align="right">1,386,949</td>
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
<td align="right">12,851,971</td>
<td align="right">94.3%</td>
<td align="right">13,201,702</td>
<td align="right">94.5%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">773,596</td>
<td align="right">5.7%</td>
<td align="right">769,651</td>
<td align="right">5.5%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">78,198</td>
<td align="right">10.1%</td>
<td align="right">76,284</td>
<td align="right">9.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">41,227</td>
<td align="right">5.3%</td>
<td align="right">42,010</td>
<td align="right">5.5%</td>
<td align="right">1.9%</td>
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
<td align="left">method</td>
<td align="right">82,231</td>
<td align="right">10.6%</td>
<td align="right">81,219</td>
<td align="right">10.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">1,653</td>
<td align="right">0.2%</td>
<td align="right">-1.2%</td>
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
<td align="left">expected error</td>
<td align="right">4,766</td>
<td align="right">0.6%</td>
<td align="right">4,724</td>
<td align="right">0.6%</td>
<td align="right">-0.9%</td>
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
<td align="left">class method obj</td>
<td align="right">30,745</td>
<td align="right">4.0%</td>
<td align="right">30,543</td>
<td align="right">4.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">140,874</td>
<td align="right">18.2%</td>
<td align="right">140,188</td>
<td align="right">18.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,878</td>
<td align="right">1.9%</td>
<td align="right">14,824</td>
<td align="right">1.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,802</td>
<td align="right">2.8%</td>
<td align="right">21,865</td>
<td align="right">2.8%</td>
<td align="right">0.3%</td>
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
<td align="right">6,272,253,389</td>
<td align="right">99.7%</td>
<td align="right">-1.2%</td>
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
<td align="right">15,100,593</td>
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
<td align="right">527,260</td>
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
<td align="right">6,988</td>
<td align="right">0.0%</td>
<td align="right">6,989</td>
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
<td align="right">67,201,384</td>
<td align="right">100.0%</td>
<td align="right">67,201,422</td>
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
<td align="right">591,451,192</td>
<td align="right">82.1%</td>
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
<td align="right">117,544,810</td>
<td align="right">4.4%</td>
<td align="right">-4.2%</td>
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
<td align="right">60,813,309</td>
<td align="right">2.3%</td>
<td align="right">-1.2%</td>
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
<td align="right">2,493,009,898</td>
<td align="right">93.3%</td>
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
<td align="right">2,420,930</td>
<td align="right">96.0%</td>
<td align="right">2,324,486</td>
<td align="right">95.8%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">101,720</td>
<td align="right">4.0%</td>
<td align="right">101,134</td>
<td align="right">4.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">8,313</td>
<td align="right">8.2%</td>
<td align="right">7,725</td>
<td align="right">7.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">310,091</td>
<td align="right">304.8%</td>
<td align="right">309,455</td>
<td align="right">306.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
<td align="right">11,041</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,626</td>
<td align="right">42.9%</td>
<td align="right">43,626</td>
<td align="right">43.1%</td>
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
<td align="left">split dict</td>
<td align="right">7,974</td>
<td align="right">7.8%</td>
<td align="right">7,974</td>
<td align="right">7.9%</td>
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
<td align="right">1,033,866</td>
<td align="right">100.0%</td>
<td align="right">-23.4%</td>
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
<td align="right">99,527,562</td>
<td align="right">9.6%</td>
<td align="right">-5.6%</td>
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
<td align="right">938,468,056</td>
<td align="right">90.4%</td>
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
<td align="right">77,321</td>
<td align="right">83.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">16.0%</td>
<td align="right">15,210</td>
<td align="right">16.4%</td>
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
<td align="left">array int</td>
<td align="right">16,174</td>
<td align="right">20.3%</td>
<td align="right">14,667</td>
<td align="right">19.0%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">7,307</td>
<td align="right">9.5%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">2,203</td>
<td align="right">2.8%</td>
<td align="right">2,099</td>
<td align="right">2.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,016</td>
<td align="right">56.5%</td>
<td align="right">45,016</td>
<td align="right">58.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
<td align="right">4,465</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,959</td>
<td align="right">3.7%</td>
<td align="right">2,959</td>
<td align="right">3.8%</td>
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
<td align="right">324,632,157</td>
<td align="right">5.9%</td>
<td align="right">321,493,032</td>
<td align="right">5.9%</td>
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
<td align="right">5,082,509,945</td>
<td align="right">92.7%</td>
<td align="right">5,034,819,648</td>
<td align="right">92.7%</td>
<td align="right">-0.9%</td>
</tr>
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
<td align="right">72,594,506</td>
<td align="right">1.3%</td>
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
<td align="right">587,614</td>
<td align="right">26.9%</td>
<td align="right">594,985</td>
<td align="right">27.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,594,517</td>
<td align="right">73.1%</td>
<td align="right">1,588,619</td>
<td align="right">72.8%</td>
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
<td align="left">other</td>
<td align="right">55,969</td>
<td align="right">9.5%</td>
<td align="right">64,120</td>
<td align="right">10.8%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">6,816</td>
<td align="right">1.2%</td>
<td align="right">6,356</td>
<td align="right">1.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,623</td>
<td align="right">2.0%</td>
<td align="right">11,518</td>
<td align="right">1.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">18,416</td>
<td align="right">3.1%</td>
<td align="right">18,252</td>
<td align="right">3.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,925</td>
<td align="right">3.4%</td>
<td align="right">19,910</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">85,683</td>
<td align="right">14.6%</td>
<td align="right">85,630</td>
<td align="right">14.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">81,278</td>
<td align="right">13.8%</td>
<td align="right">81,298</td>
<td align="right">13.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">305,842</td>
<td align="right">52.0%</td>
<td align="right">305,839</td>
<td align="right">51.4%</td>
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
<td align="left">float</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.1%</td>
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
<td align="right">465,012</td>
<td align="right">0.0%</td>
<td align="right">-63.5%</td>
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
<td align="right">1,270,926,923</td>
<td align="right">100.0%</td>
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
<td align="right">2,097</td>
<td align="right">5.3%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,237</td>
<td align="right">93.8%</td>
<td align="right">37,241</td>
<td align="right">94.7%</td>
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
<td align="right">1,772</td>
<td align="right">71.9%</td>
<td align="right">1,403</td>
<td align="right">66.9%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">15.3%</td>
<td align="right">378</td>
<td align="right">18.0%</td>
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
<td align="right">3,471,493,442</td>
<td align="right">2.9%</td>
<td align="right">-4.4%</td>
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
<td align="right">69,564,393,547</td>
<td align="right">58.2%</td>
<td align="right">-2.9%</td>
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
<td align="right">45,230,637,650</td>
<td align="right">37.9%</td>
<td align="right">-2.8%</td>
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
<td align="right">1,161,739,817</td>
<td align="right">1.0%</td>
<td align="right">1.4%</td>
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
<td align="right">186,745,600</td>
<td align="right">6.1%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">122,882,522</td>
<td align="right">3.8%</td>
<td align="right">111,157,222</td>
<td align="right">3.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">198,025,212</td>
<td align="right">6.1%</td>
<td align="right">183,255,071</td>
<td align="right">6.0%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,465,188</td>
<td align="right">3.3%</td>
<td align="right">99,527,562</td>
<td align="right">3.2%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,174,817,914</td>
<td align="right">36.4%</td>
<td align="right">1,110,998,442</td>
<td align="right">36.1%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">126,450,463</td>
<td align="right">3.9%</td>
<td align="right">120,791,239</td>
<td align="right">3.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">579,893,223</td>
<td align="right">18.0%</td>
<td align="right">570,974,344</td>
<td align="right">18.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">324,632,157</td>
<td align="right">10.1%</td>
<td align="right">321,493,032</td>
<td align="right">10.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">167,366,537</td>
<td align="right">5.2%</td>
<td align="right">167,460,014</td>
<td align="right">5.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,260,696</td>
<td align="right">4.0%</td>
<td align="right">129,260,696</td>
<td align="right">4.2%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,308,414</td>
<td align="right">6.0%</td>
<td align="right">71,757,587</td>
<td align="right">6.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">103,212,182</td>
<td align="right">9.0%</td>
<td align="right">98,222,062</td>
<td align="right">8.5%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">189,693,899</td>
<td align="right">16.6%</td>
<td align="right">198,555,440</td>
<td align="right">17.1%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">83,403,062</td>
<td align="right">7.3%</td>
<td align="right">86,996,033</td>
<td align="right">7.5%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">79,640,674</td>
<td align="right">6.9%</td>
<td align="right">82,582,969</td>
<td align="right">7.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,342,634</td>
<td align="right">2.7%</td>
<td align="right">30,732,116</td>
<td align="right">2.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,247,188</td>
<td align="right">2.7%</td>
<td align="right">30,681,458</td>
<td align="right">2.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">238,533,247</td>
<td align="right">20.8%</td>
<td align="right">242,060,436</td>
<td align="right">20.8%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">32,436,922</td>
<td align="right">2.8%</td>
<td align="right">32,283,706</td>
<td align="right">2.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">33,711,677</td>
<td align="right">2.9%</td>
<td align="right">33,569,115</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
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
<td align="left">Frames pushed</td>
<td align="right">6,354,772,061</td>
<td align="right">84.2%</td>
<td align="right">6,354,701,816</td>
<td align="right">84.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,814,679</td>
<td align="right">0.3%</td>
<td align="right">23,814,836</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,569,068</td>
<td align="right">0.9%</td>
<td align="right">71,569,461</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">463,651,742</td>
<td align="right">6.1%</td>
<td align="right">463,650,245</td>
<td align="right">6.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,679,160,884</td>
<td align="right">75.2%</td>
<td align="right">5,679,145,639</td>
<td align="right">75.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">307,733,768</td>
<td align="right">4.1%</td>
<td align="right">307,734,345</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,421,410</td>
<td align="right">7.7%</td>
<td align="right">584,421,643</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,282,480,443</td>
<td align="right">17.0%</td>
<td align="right">1,282,480,043</td>
<td align="right">17.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,286,754,660</td>
<td align="right">17.0%</td>
<td align="right">1,286,754,260</td>
<td align="right">17.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,871,176,070</td>
<td align="right">24.8%</td>
<td align="right">1,871,175,903</td>
<td align="right">24.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,871,176,070</td>
<td align="right">24.8%</td>
<td align="right">1,871,175,903</td>
<td align="right">24.8%</td>
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
<td align="right">1.7%</td>
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
<td align="right">1,279,061,356</td>
<td align="right">1.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,874,532</td>
<td align="right"></td>
<td align="right">60,488,073</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">3,760,289,358</td>
<td align="right">3.8%</td>
<td align="right">3,665,412,347</td>
<td align="right">3.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">64,708,870</td>
<td align="right"></td>
<td align="right">66,223,989</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">29,552,166,644</td>
<td align="right">29.8%</td>
<td align="right">29,079,662,222</td>
<td align="right">29.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,530,021</td>
<td align="right"></td>
<td align="right">6,431,223</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">40,849,915,447</td>
<td align="right">41.2%</td>
<td align="right">41,379,588,610</td>
<td align="right">41.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">38,799,085,008</td>
<td align="right">34.0%</td>
<td align="right">38,342,196,218</td>
<td align="right">33.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">50,284,662,501</td>
<td align="right">44.1%</td>
<td align="right">50,798,384,956</td>
<td align="right">44.5%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,127,351,789</td>
<td align="right"></td>
<td align="right">2,138,902,289</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,911,605,069</td>
<td align="right">25.1%</td>
<td align="right">24,987,437,370</td>
<td align="right">25.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,632,536,056</td>
<td align="right">20.7%</td>
<td align="right">23,675,301,168</td>
<td align="right">20.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,892,884,058</td>
<td align="right"></td>
<td align="right">2,896,470,264</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,604,946</td>
<td align="right">0.0%</td>
<td align="right">6,611,588</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,717,335</td>
<td align="right">0.4%</td>
<td align="right">71,768,692</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,476,887,819</td>
<td align="right"></td>
<td align="right">6,476,440,920</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,824,602,603</td>
<td align="right">29.1%</td>
<td align="right">5,824,245,556</td>
<td align="right">29.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,902,924,884</td>
<td align="right">29.5%</td>
<td align="right">5,902,625,836</td>
<td align="right">29.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,139,562,328</td>
<td align="right"></td>
<td align="right">14,139,404,135</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,137,885,263</td>
<td align="right">70.5%</td>
<td align="right">14,137,729,070</td>
<td align="right">70.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,717,617</td>
<td align="right"></td>
<td align="right">177,717,756</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,639,155</td>
<td align="right">2.0%</td>
<td align="right">3,639,155</td>
<td align="right">2.0%</td>
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
<td align="right">367,286</td>
<td align="right">94,983,556</td>
<td align="right">9,789,312,611</td>
<td align="right">810,167,402</td>
<td align="right">759,048,079</td>
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
<td align="right">5,703,371,314</td>
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
<td align="right">4,045</td>
<td align="right">4.1%</td>
<td align="right">531.0%</td>
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
<td align="right">950</td>
<td align="right">0.2%</td>
<td align="right">375.0%</td>
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
<td align="right">843</td>
<td align="right">0.1%</td>
<td align="right">363.2%</td>
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
<td align="right">2,548</td>
<td align="right">0.4%</td>
<td align="right">183.1%</td>
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
<td align="right">98,724</td>
<td align="right">16.8%</td>
<td align="right">167.3%</td>
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
<td align="right">5,698</td>
<td align="right">1.0%</td>
<td align="right">78.9%</td>
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
<td align="right">2,105</td>
<td align="right">0.4%</td>
<td align="right">57.2%</td>
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
<td align="right">206,877</td>
<td align="right">35.3%</td>
<td align="right">53.5%</td>
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
<td align="right">586,122</td>
<td align="right"></td>
<td align="right">32.5%</td>
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
<td align="right">232,837</td>
<td align="right">39.7%</td>
<td align="right">4.2%</td>
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
<td align="right">253,962,460,862</td>
<td align="right">6,476.5%</td>
<td align="right">3.2%</td>
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
<td align="right">3,921,283,770</td>
<td align="right"></td>
<td align="right">1.7%</td>
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
<td align="right">46,734</td>
<td align="right">8.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">85,825</td>
<td align="right">86.9%</td>
<td align="right">175.2%</td>
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
<td align="right">98,724</td>
<td align="right"></td>
<td align="right">167.3%</td>
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
<td align="right">103</td>
<td align="right">0.1%</td>
<td align="right">103 / 0 !!</td>
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
<td align="right">66,866,251</td>
<td align="right">16.0%</td>
<td align="right">185,999,851</td>
<td align="right">16.7%</td>
<td align="right">178.2%</td>
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
<td align="right">23,698,224</td>
<td align="right">2.1%</td>
<td align="right">168.1%</td>
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
<td align="right">1,111,126,016</td>
<td align="right"></td>
<td align="right">165.4%</td>
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
<td align="right">901,427,941</td>
<td align="right">81.1%</td>
<td align="right">162.8%</td>
</tr>
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
<td align="right">4,681,728</td>
<td align="right">0.4%</td>
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
<td align="left">6,903</td>
<td align="right">22.1%</td>
<td align="left">11,141</td>
<td align="right">13.0%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">9,591</td>
<td align="right">30.8%</td>
<td align="left">34,206</td>
<td align="right">39.9%</td>
<td align="right">256.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,657</td>
<td align="right">27.8%</td>
<td align="left">26,669</td>
<td align="right">31.1%</td>
<td align="right">208.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,142</td>
<td align="right">13.3%</td>
<td align="left">10,565</td>
<td align="right">12.3%</td>
<td align="right">155.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,732</td>
<td align="right">5.6%</td>
<td align="left">2,724</td>
<td align="right">3.2%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">160</td>
<td align="right">0.5%</td>
<td align="left">520</td>
<td align="right">0.6%</td>
<td align="right">225.0%</td>
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
<td align="right">1,800</td>
<td align="right">1.8%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,565</td>
<td align="right">4.2%</td>
<td align="right">1,997</td>
<td align="right">2.0%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,519</td>
<td align="right">14.9%</td>
<td align="right">12,252</td>
<td align="right">12.4%</td>
<td align="right">122.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,426</td>
<td align="right">28.2%</td>
<td align="right">37,837</td>
<td align="right">38.3%</td>
<td align="right">262.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,580</td>
<td align="right">20.5%</td>
<td align="right">21,966</td>
<td align="right">22.2%</td>
<td align="right">189.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,155</td>
<td align="right">19.4%</td>
<td align="right">16,935</td>
<td align="right">17.2%</td>
<td align="right">136.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,773</td>
<td align="right">7.5%</td>
<td align="right">4,568</td>
<td align="right">4.6%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">507</td>
<td align="right">1.4%</td>
<td align="right">1,369</td>
<td align="right">1.4%</td>
<td align="right">170.0%</td>
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
<td align="right">1,153</td>
<td align="right">1.2%</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,093</td>
<td align="right">3.0%</td>
<td align="right">1,275</td>
<td align="right">1.3%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,795</td>
<td align="right">7.6%</td>
<td align="right">3,453</td>
<td align="right">3.5%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,183</td>
<td align="right">27.6%</td>
<td align="right">32,892</td>
<td align="right">33.3%</td>
<td align="right">223.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,597</td>
<td align="right">23.3%</td>
<td align="right">28,739</td>
<td align="right">29.1%</td>
<td align="right">234.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,303</td>
<td align="right">11.6%</td>
<td align="right">12,147</td>
<td align="right">12.3%</td>
<td align="right">182.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,872</td>
<td align="right">7.8%</td>
<td align="right">4,957</td>
<td align="right">5.0%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">530</td>
<td align="right">1.4%</td>
<td align="right">1,209</td>
<td align="right">1.2%</td>
<td align="right">128.1%</td>
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
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">306,978</td>
<td align="right">1,045.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,680</td>
<td align="right">837,900</td>
<td align="right">889.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">23,582</td>
<td align="right">211,888</td>
<td align="right">798.5%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">6,447</td>
<td align="right">395.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,220,144</td>
<td align="right">15,574,651</td>
<td align="right">383.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">13,260,066</td>
<td align="right">50,615,325</td>
<td align="right">281.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">158,441</td>
<td align="right">510,071</td>
<td align="right">221.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">1,193,472</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">11,116,120</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,597,702</td>
<td align="right">3,587,876</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">597,349</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,512,129</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">53,070</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">98,457,639</td>
<td align="right">168,521,011</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">98,457,639</td>
<td align="right">168,521,011</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">99,153,579</td>
<td align="right">169,098,311</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">106,030</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">85,608</td>
<td align="right">118,053</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">339,252,499</td>
<td align="right">463,915,751</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,220,780</td>
<td align="right">2,341,020</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,311,576</td>
<td align="right">1,632,200</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,073,505</td>
<td align="right">62,507,507</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,073,505</td>
<td align="right">62,507,507</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,794,181</td>
<td align="right">85,137,983</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,646,825</td>
<td align="right">73,326,824</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">32,996,194</td>
<td align="right">38,755,619</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">276,480</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">5,036,652</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,972,064</td>
<td align="right">3,448,841</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">38,051,764</td>
<td align="right">32,125,407</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">28,704,759</td>
<td align="right">33,173,670</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">110,785,869</td>
<td align="right">126,006,562</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">149,938,351</td>
<td align="right">170,296,703</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,003,931</td>
<td align="right">5,650,931</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,689,455</td>
<td align="right">42,528,143</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,374,659</td>
<td align="right">8,318,911</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">643,996,033</td>
<td align="right">724,460,362</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">11,424,529</td>
<td align="right">10,004,568</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,961,160</td>
<td align="right">5,576,518</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,571,606</td>
<td align="right">12,997,415</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">106,388,800</td>
<td align="right">118,916,860</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">66,289</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">162,619,918</td>
<td align="right">181,450,583</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">162,828,532</td>
<td align="right">181,602,363</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,427,979,858</td>
<td align="right">1,584,915,388</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,428,444,273</td>
<td align="right">1,585,094,616</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">123,812,404</td>
<td align="right">136,966,524</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">141,870,917</td>
<td align="right">156,764,809</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,957,511</td>
<td align="right">7,685,697</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">486,595,537</td>
<td align="right">535,446,200</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">193,394,637</td>
<td align="right">212,783,446</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">35,095,856</td>
<td align="right">31,591,468</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,113,485</td>
<td align="right">47,308,488</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,614,620</td>
<td align="right">7,248,500</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">116,173,764</td>
<td align="right">126,546,478</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">564,221,893</td>
<td align="right">613,217,755</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,907,980</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">202,706,849</td>
<td align="right">220,045,753</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">296,944,110</td>
<td align="right">322,305,757</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">41,429,630</td>
<td align="right">44,789,798</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">46,485,112</td>
<td align="right">50,245,866</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,939,012</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,939,012</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">281,228,492</td>
<td align="right">302,678,026</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">144,778,189</td>
<td align="right">155,819,170</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">153,157,508</td>
<td align="right">164,788,213</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">18,915,070</td>
<td align="right">20,331,956</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">18,915,070</td>
<td align="right">20,331,956</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,549,100</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">74,057,780</td>
<td align="right">79,142,976</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,922,208</td>
<td align="right">4,187,611</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,012,080</td>
<td align="right">3,214,558</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">317,091,300</td>
<td align="right">337,826,935</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">227,718,937</td>
<td align="right">242,031,064</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,052,929</td>
<td align="right">6,431,547</td>
<td align="right">6.3%</td>
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
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">36,762,038</td>
<td align="right">39,009,938</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">18,814,170</td>
<td align="right">19,946,362</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">296,755,785</td>
<td align="right">313,524,178</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">584,418,003</td>
<td align="right">616,030,864</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,776,129,929</td>
<td align="right">8,192,372,198</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">73,677,990</td>
<td align="right">77,606,456</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">700,253,798</td>
<td align="right">736,766,578</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,211,388,790</td>
<td align="right">1,274,427,603</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,025,143,415</td>
<td align="right">4,232,899,455</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">396,829,742</td>
<td align="right">417,223,601</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">645,273,570</td>
<td align="right">678,311,922</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">43,982,703</td>
<td align="right">46,177,779</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">445,968,892</td>
<td align="right">467,787,128</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">256,299,201</td>
<td align="right">268,533,997</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">106,993,748</td>
<td align="right">112,031,798</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">253,470,175</td>
<td align="right">265,380,925</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">541,690,328</td>
<td align="right">566,368,368</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,775,789,287</td>
<td align="right">3,947,141,107</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">338,908,369</td>
<td align="right">353,852,380</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">235,251,428</td>
<td align="right">245,523,242</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,106,940</td>
<td align="right">43,941,487</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">412,052,824</td>
<td align="right">429,975,670</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,417,240,723</td>
<td align="right">1,478,350,123</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">444,490,589</td>
<td align="right">463,423,015</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">452,550,515</td>
<td align="right">471,798,731</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,713,621</td>
<td align="right">36,185,641</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,958,738,636</td>
<td align="right">3,081,484,135</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">357,815,241</td>
<td align="right">372,585,382</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">966,667,557</td>
<td align="right">1,005,367,624</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,297,640,951</td>
<td align="right">36,704,119,746</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">966,530,417</td>
<td align="right">1,004,839,033</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">42,348,720</td>
<td align="right">44,000,660</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,870,311,560</td>
<td align="right">1,942,001,802</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">316,917,034</td>
<td align="right">329,026,825</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">399,836,526</td>
<td align="right">415,025,406</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">29,768,070</td>
<td align="right">30,895,839</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">29,768,070</td>
<td align="right">30,895,839</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">100,975,970</td>
<td align="right">104,772,539</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,295,836,310</td>
<td align="right">1,344,451,024</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,253,780,151</td>
<td align="right">1,300,638,104</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,253,780,151</td>
<td align="right">1,300,638,104</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,241,778,729</td>
<td align="right">1,287,699,092</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">808,172,234</td>
<td align="right">837,817,901</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,306,907</td>
<td align="right">149,595,474</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,392,283</td>
<td align="right">57,349,198</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">467,890,637</td>
<td align="right">484,351,469</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,803,742,945</td>
<td align="right">1,866,556,469</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">447,902,296</td>
<td align="right">463,300,783</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">447,902,296</td>
<td align="right">463,300,783</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,327,180,931</td>
<td align="right">41,670,247,514</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">426,944,037</td>
<td align="right">441,129,933</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,176,665,969</td>
<td align="right">1,215,546,453</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,794,170,090</td>
<td align="right">2,886,439,882</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,462,984,798</td>
<td align="right">3,576,328,744</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,546,456,605</td>
<td align="right">1,496,114,168</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,549,878</td>
<td align="right">121,099,556</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,165,435,695</td>
<td align="right">2,230,742,812</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,973,269,909</td>
<td align="right">7,183,363,204</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">188,493,771</td>
<td align="right">194,089,158</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,793,583,118</td>
<td align="right">1,846,199,001</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,763,171,905</td>
<td align="right">3,873,460,549</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,476,141</td>
<td align="right">48,846,224</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,078,138,952</td>
<td align="right">1,109,127,928</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,337,233,822</td>
<td align="right">1,375,012,383</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,944,384,647</td>
<td align="right">11,250,071,149</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,394,817</td>
<td align="right">48,704,467</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,034,320</td>
<td align="right">74,944,420</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">757,567,708</td>
<td align="right">777,258,671</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,740,666</td>
<td align="right">1,238,858,673</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,239,990,502</td>
<td align="right">2,294,226,933</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">390,244,432</td>
<td align="right">399,511,093</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">144,953,608</td>
<td align="right">148,311,514</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,006,876,445</td>
<td align="right">2,053,291,908</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,339,729,502</td>
<td align="right">1,370,627,064</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">352,930,430</td>
<td align="right">361,049,251</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,193,684</td>
<td align="right">47,255,664</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">236,847,542</td>
<td align="right">242,277,899</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">17,372,080</td>
<td align="right">17,769,600</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,872,908,460</td>
<td align="right">2,938,415,347</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">182,526,544</td>
<td align="right">186,678,494</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">43,760,440</td>
<td align="right">42,846,356</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,230,122,013</td>
<td align="right">1,254,811,616</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">39,466,304</td>
<td align="right">40,255,309</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,139,983,372</td>
<td align="right">1,162,076,740</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,819,487,206</td>
<td align="right">3,889,480,414</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">136,640,971</td>
<td align="right">139,070,927</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">529,087,310</td>
<td align="right">538,435,855</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,854,606,644</td>
<td align="right">3,921,283,770</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">168,746,470</td>
<td align="right">171,649,283</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,784,955</td>
<td align="right">530,622,075</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">847,283,418</td>
<td align="right">861,527,569</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,111,896,433</td>
<td align="right">1,129,990,843</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,348,895,214</td>
<td align="right">4,419,666,678</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,339,454</td>
<td align="right">652,710,175</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,469,624,667</td>
<td align="right">2,508,203,641</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,960,962</td>
<td align="right">20,271,157</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">54,924,324</td>
<td align="right">55,776,484</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,309,576,004</td>
<td align="right">6,406,391,695</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">249,694,147</td>
<td align="right">253,522,460</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,874,104</td>
<td align="right">39,432,338</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">403,763,061</td>
<td align="right">409,472,195</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">957,305,821</td>
<td align="right">970,232,171</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">976,764,571</td>
<td align="right">989,879,573</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,835,430,452</td>
<td align="right">2,872,660,403</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,002,630,307</td>
<td align="right">1,015,465,392</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,454,969,360</td>
<td align="right">2,485,107,925</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,677,032</td>
<td align="right">140,229,964</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">460,952,104</td>
<td align="right">465,981,207</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,397,435,108</td>
<td align="right">4,445,373,754</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">494,153,654</td>
<td align="right">499,373,514</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,390,939</td>
<td align="right">54,818,236</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">39,305,011</td>
<td align="right">39,704,453</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">971,076,168</td>
<td align="right">980,900,883</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">593,442,788</td>
<td align="right">599,380,629</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">69,571,391</td>
<td align="right">70,254,838</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">69,571,391</td>
<td align="right">70,254,838</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,115,122</td>
<td align="right">1,178,497,132</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">428,218,018</td>
<td align="right">432,387,026</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">46,728,468</td>
<td align="right">47,175,287</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,339,524,257</td>
<td align="right">2,360,664,050</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">769,932,726</td>
<td align="right">776,262,395</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">35,266,120</td>
<td align="right">34,995,909</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,546,340</td>
<td align="right">59,985,324</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">169,038,286</td>
<td align="right">170,283,540</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">1,557,554,920</td>
<td align="right">1,568,275,347</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,907,960,521</td>
<td align="right">3,934,285,490</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,003,700</td>
<td align="right">3,023,860</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">71,532,780</td>
<td align="right">71,992,800</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,012,332,418</td>
<td align="right">1,018,756,688</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,342,482,500</td>
<td align="right">1,350,874,215</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">254,837,086</td>
<td align="right">256,354,523</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,468,814,716</td>
<td align="right">1,475,470,678</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">487,991,448</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,297,335,052</td>
<td align="right">1,302,577,637</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">911,776,396</td>
<td align="right">915,310,033</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,052,268,311</td>
<td align="right">1,055,979,928</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">911,776,396</td>
<td align="right">914,917,988</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,195,783,997</td>
<td align="right">1,199,394,499</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">65,697,542</td>
<td align="right">65,894,834</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,376,320</td>
<td align="right">111,692,259</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">440,104,015</td>
<td align="right">441,311,829</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">440,104,015</td>
<td align="right">441,311,829</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">93,891,060</td>
<td align="right">94,132,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,171,220</td>
<td align="right">3,164,860</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">749,182,847</td>
<td align="right">750,168,603</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">225,698,868</td>
<td align="right">225,607,453</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,058,846</td>
<td align="right">745,757,563</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,997,705,254</td>
<td align="right">1,998,366,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">730,099,878</td>
<td align="right">730,329,822</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">150,369,864</td>
<td align="right">150,322,894</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">206,850,103</td>
<td align="right">206,830,370</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">19,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">19,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">15,876</td>
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
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">4,466</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,365</td>
<td align="right">26,320</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,781</td>
<td align="right">1,842</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,981</td>
<td align="right">23,083</td>
<td align="right">0.4%</td>
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
