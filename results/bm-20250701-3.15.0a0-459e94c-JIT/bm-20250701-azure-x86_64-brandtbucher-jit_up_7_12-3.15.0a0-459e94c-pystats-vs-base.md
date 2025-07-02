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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2,332,004</td>
<td align="right">810,417</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,315,340</td>
<td align="right">528,401</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">21,535,496</td>
<td align="right">29,093,035</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,349,805</td>
<td align="right">1,039,305</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,265,188</td>
<td align="right">976,257</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,354,001</td>
<td align="right">2,716,926</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">57,327,364</td>
<td align="right">47,018,431</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">124,871,671</td>
<td align="right">103,150,992</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">207,957,783</td>
<td align="right">173,058,120</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220,246,698</td>
<td align="right">186,589,374</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,807,102</td>
<td align="right">2,386,903</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">369,954,636</td>
<td align="right">319,967,062</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">42,025,370</td>
<td align="right">36,760,693</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">124,153,260</td>
<td align="right">109,849,502</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,311,927</td>
<td align="right">83,579,324</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">372,813,493</td>
<td align="right">332,074,388</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">197,567,460</td>
<td align="right">176,599,359</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">111,699,135</td>
<td align="right">100,242,811</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">449,939,615</td>
<td align="right">403,921,491</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">178,177,806</td>
<td align="right">160,508,023</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,734,678</td>
<td align="right">45,125,775</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,070,159</td>
<td align="right">33,636,418</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,099,922,867</td>
<td align="right">1,000,650,448</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">209,837,953</td>
<td align="right">191,661,353</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">297,390,974</td>
<td align="right">271,859,204</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">164,689,544</td>
<td align="right">150,552,822</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,840,180</td>
<td align="right">2,608,700</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">182,621,912</td>
<td align="right">167,753,164</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">14,297,526</td>
<td align="right">13,153,414</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">77,863,075</td>
<td align="right">71,855,600</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">163,945,034</td>
<td align="right">152,110,319</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">957,654,786</td>
<td align="right">890,609,173</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,283,939</td>
<td align="right">79,350,186</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,217,724</td>
<td align="right">158,926,598</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,090,483,630</td>
<td align="right">1,020,781,366</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,871,386</td>
<td align="right">90,725,829</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,571,619</td>
<td align="right">25,834,279</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">373,881,548</td>
<td align="right">350,741,957</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,035,674,002</td>
<td align="right">1,910,544,520</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,049,994,079</td>
<td align="right">1,924,621,621</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">624,059,745</td>
<td align="right">586,080,387</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">220,719,607</td>
<td align="right">207,634,289</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">709,897,881</td>
<td align="right">668,742,488</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,562,154</td>
<td align="right">99,461,283</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">148,537,414</td>
<td align="right">140,275,608</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">878,207,320</td>
<td align="right">834,409,032</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">467,975,397</td>
<td align="right">445,240,074</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">383,888,736</td>
<td align="right">365,295,539</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">907,099,296</td>
<td align="right">863,199,567</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,544,932</td>
<td align="right">5,276,774</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">274,430,759</td>
<td align="right">261,743,701</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">55,469,573</td>
<td align="right">52,946,615</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">42,727,340</td>
<td align="right">40,786,122</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,163,960</td>
<td align="right">10,678,511</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,001,033</td>
<td align="right">24,880,617</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,154,551,351</td>
<td align="right">3,986,147,476</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,880,262</td>
<td align="right">63,332,971</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">431,759,287</td>
<td align="right">414,682,304</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,088,363,503</td>
<td align="right">4,887,789,837</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">919,629,220</td>
<td align="right">883,572,720</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">37,576,131</td>
<td align="right">36,110,341</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">658,003,425</td>
<td align="right">632,644,655</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,245,700</td>
<td align="right">6,007,620</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">424,197,537</td>
<td align="right">408,048,404</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,516,861</td>
<td align="right">4,349,231</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,877,728,302</td>
<td align="right">16,255,420,871</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">352,815,775</td>
<td align="right">340,267,684</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,729,160</td>
<td align="right">9,393,622</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,387,660</td>
<td align="right">18,721,455</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">78,915</td>
<td align="right">76,206</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">207,570,809</td>
<td align="right">200,458,796</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,408,781</td>
<td align="right">456,711,467</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">134,670,752</td>
<td align="right">130,246,726</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,191,708,326</td>
<td align="right">4,056,571,025</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">168,432,590</td>
<td align="right">163,185,816</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">173,731,396</td>
<td align="right">168,340,025</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">852,853,951</td>
<td align="right">879,262,275</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,560,932</td>
<td align="right">9,266,667</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">127,900,098</td>
<td align="right">123,981,154</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">924,067,033</td>
<td align="right">896,159,833</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">119,116,381</td>
<td align="right">115,738,595</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,958,212</td>
<td align="right">257,753,575</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">281,033,223</td>
<td align="right">273,746,836</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">462,070,383</td>
<td align="right">473,721,665</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,278,437</td>
<td align="right">47,064,450</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">179,363,972</td>
<td align="right">175,058,306</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">77,451,619</td>
<td align="right">75,690,031</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,653,286</td>
<td align="right">94,512,706</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,745,426,082</td>
<td align="right">3,663,374,922</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">279,175,484</td>
<td align="right">273,091,647</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,504,350</td>
<td align="right">546,537,328</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">69,035,271</td>
<td align="right">67,612,152</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,338,476,900</td>
<td align="right">2,291,174,402</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,387,602,242</td>
<td align="right">3,320,872,485</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">52,652,481</td>
<td align="right">51,639,478</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">112,289,889</td>
<td align="right">110,246,567</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">179,235,008</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">927,739,606</td>
<td align="right">910,949,266</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,164</td>
<td align="right">550,105</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">910,283,530</td>
<td align="right">894,458,968</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">508,784,561</td>
<td align="right">499,993,562</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,747,882</td>
<td align="right">242,627,847</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">115,592,511</td>
<td align="right">113,700,968</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">561,252,265</td>
<td align="right">552,088,554</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">346,654,349</td>
<td align="right">341,106,889</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,013,031</td>
<td align="right">258,970,841</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">64,309,172</td>
<td align="right">63,325,691</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,041,508</td>
<td align="right">30,604,952</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,713,139,684</td>
<td align="right">4,648,566,035</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">811,093,912</td>
<td align="right">800,324,598</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">137,139,376</td>
<td align="right">135,412,930</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,739,597</td>
<td align="right">61,045,290</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">71,659,486</td>
<td align="right">70,890,383</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">256,775,015</td>
<td align="right">254,052,331</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,664,671,264</td>
<td align="right">2,639,583,738</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,417,966</td>
<td align="right">280,793,659</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,470,442</td>
<td align="right">80,718,503</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,308,077</td>
<td align="right">69,731,120</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">833,067,438</td>
<td align="right">826,262,408</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,445,686</td>
<td align="right">41,148,862</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,115,545</td>
<td align="right">74,581,399</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,531,045,079</td>
<td align="right">2,514,242,482</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">621,768,803</td>
<td align="right">617,898,664</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,023,632,559</td>
<td align="right">2,011,476,936</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">262,522,015</td>
<td align="right">261,068,126</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,446,284</td>
<td align="right">119,780,079</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,136,625,291</td>
<td align="right">1,131,010,041</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">141,371,283</td>
<td align="right">140,719,224</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,075,598</td>
<td align="right">51,841,818</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,145,807</td>
<td align="right">70,833,339</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,184,173</td>
<td align="right">123,667,858</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,715,231</td>
<td align="right">10,673,408</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">368,501,623</td>
<td align="right">367,252,817</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">114,350,367</td>
<td align="right">113,982,760</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,055,566,867</td>
<td align="right">5,040,213,551</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">292,970,077</td>
<td align="right">293,768,324</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,529,308,299</td>
<td align="right">1,525,183,558</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">672,358,104</td>
<td align="right">671,421,111</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,127,556</td>
<td align="right">332,437,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,512,998</td>
<td align="right">68,466,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">384,319,805</td>
<td align="right">384,519,092</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">126,964,760</td>
<td align="right">126,902,728</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,158</td>
<td align="right">14,153</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,081</td>
<td align="right">92,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,107,626,231</td>
<td align="right">1,107,937,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,439,741</td>
<td align="right">28,446,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,576,539</td>
<td align="right">1,576,259</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,833,463</td>
<td align="right">69,844,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">323,893</td>
<td align="right">323,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,599,289</td>
<td align="right">190,571,378</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,450,765</td>
<td align="right">3,450,285</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,925,954</td>
<td align="right">35,921,982</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106,196</td>
<td align="right">106,186</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,147,679</td>
<td align="right">21,146,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,423,284</td>
<td align="right">21,422,564</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,423,305</td>
<td align="right">21,422,585</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,619,526</td>
<td align="right">15,619,149</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,680,537</td>
<td align="right">6,680,452</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,523,652</td>
<td align="right">13,523,501</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">333,541</td>
<td align="right">333,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,540,620,411</td>
<td align="right">1,540,607,369</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,682,739</td>
<td align="right">114,682,070</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,401</td>
<td align="right">3,100,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">11,838,596</td>
<td align="right">11,838,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,705,679</td>
<td align="right">418,705,614</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">243,419,240</td>
<td align="right">243,419,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">241,369,152</td>
<td align="right">241,369,178</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,462,202</td>
<td align="right">591,462,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,078,481</td>
<td align="right">155,078,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,552,075</td>
<td align="right">302,552,075</td>
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
<td align="right">129,310,545</td>
<td align="right">129,310,545</td>
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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,951,274</td>
<td align="right">8,951,274</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,279,017</td>
<td align="right">6,279,017</td>
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
<td align="right">19,258</td>
<td align="right">19,258</td>
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
<td align="right">1,089,672,394</td>
<td align="right">6.3%</td>
<td align="right">1,020,028,795</td>
<td align="right">5.9%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,513,558</td>
<td align="right">0.4%</td>
<td align="right">69,201,021</td>
<td align="right">0.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,139,704,256</td>
<td align="right">93.3%</td>
<td align="right">16,137,421,595</td>
<td align="right">93.7%</td>
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
<td align="right">653,866</td>
<td align="right">32.0%</td>
<td align="right">595,455</td>
<td align="right">29.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,391,549</td>
<td align="right">68.0%</td>
<td align="right">1,460,937</td>
<td align="right">71.0%</td>
<td align="right">5.0%</td>
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
<td align="right">29,721</td>
<td align="right">4.5%</td>
<td align="right">8,325</td>
<td align="right">1.4%</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">25,123</td>
<td align="right">3.8%</td>
<td align="right">15,943</td>
<td align="right">2.7%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,181</td>
<td align="right">2.3%</td>
<td align="right">11,548</td>
<td align="right">1.9%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">5,212</td>
<td align="right">0.8%</td>
<td align="right">4,172</td>
<td align="right">0.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">39,645</td>
<td align="right">6.1%</td>
<td align="right">32,728</td>
<td align="right">5.5%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,139</td>
<td align="right">2.3%</td>
<td align="right">13,544</td>
<td align="right">2.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">56,721</td>
<td align="right">8.7%</td>
<td align="right">51,759</td>
<td align="right">8.7%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">4,921</td>
<td align="right">0.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,464</td>
<td align="right">2.4%</td>
<td align="right">14,357</td>
<td align="right">2.4%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">3,093</td>
<td align="right">0.5%</td>
<td align="right">2,873</td>
<td align="right">0.5%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">33,181</td>
<td align="right">5.1%</td>
<td align="right">31,186</td>
<td align="right">5.2%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,119</td>
<td align="right">9.0%</td>
<td align="right">56,228</td>
<td align="right">9.4%</td>
<td align="right">-4.9%</td>
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
<td align="left">subscr mappingproxy</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">540</td>
<td align="right">0.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">16,575</td>
<td align="right">2.5%</td>
<td align="right">16,167</td>
<td align="right">2.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,784</td>
<td align="right">7.5%</td>
<td align="right">47,586</td>
<td align="right">8.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,181</td>
<td align="right">0.8%</td>
<td align="right">5,079</td>
<td align="right">0.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,464</td>
<td align="right">1.3%</td>
<td align="right">8,339</td>
<td align="right">1.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">28,112</td>
<td align="right">4.3%</td>
<td align="right">27,726</td>
<td align="right">4.7%</td>
<td align="right">-1.4%</td>
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
<td align="right">71,308</td>
<td align="right">10.9%</td>
<td align="right">70,779</td>
<td align="right">11.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">29,084</td>
<td align="right">4.4%</td>
<td align="right">28,937</td>
<td align="right">4.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,953</td>
<td align="right">1.7%</td>
<td align="right">10,913</td>
<td align="right">1.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,417</td>
<td align="right">0.2%</td>
<td align="right">1,412</td>
<td align="right">0.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,041</td>
<td align="right">0.2%</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">109,863</td>
<td align="right">16.8%</td>
<td align="right">109,839</td>
<td align="right">18.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,634</td>
<td align="right">0.9%</td>
<td align="right">5,634</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,765</td>
<td align="right">0.6%</td>
<td align="right">3,765</td>
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
<td align="right">343</td>
<td align="right">0.1%</td>
<td align="right">343</td>
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
<td align="right">182,542,876</td>
<td align="right">100.0%</td>
<td align="right">179,235,008</td>
<td align="right">100.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">163,291,096</td>
<td align="right">1.5%</td>
<td align="right">167,829,299</td>
<td align="right">1.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">161,190,588</td>
<td align="right">1.5%</td>
<td align="right">165,642,963</td>
<td align="right">1.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,948,151,433</td>
<td align="right">98.5%</td>
<td align="right">10,945,121,926</td>
<td align="right">98.5%</td>
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
<td align="right">3,676,881</td>
<td align="right">100.0%</td>
<td align="right">3,762,429</td>
<td align="right">100.0%</td>
<td align="right">2.3%</td>
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
<td align="right">685,038</td>
<td align="right">91.8%</td>
<td align="right">685,032</td>
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
<td align="right">61,496</td>
<td align="right">100.0%</td>
<td align="right">61,492</td>
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
<td align="right">96,636,766</td>
<td align="right">2.1%</td>
<td align="right">90,493,002</td>
<td align="right">2.0%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,317,091</td>
<td align="right">0.0%</td>
<td align="right">1,309,948</td>
<td align="right">0.0%</td>
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
<td align="right">4,500,056,897</td>
<td align="right">97.9%</td>
<td align="right">4,499,358,761</td>
<td align="right">98.0%</td>
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
<td align="right">169,282</td>
<td align="right">65.4%</td>
<td align="right">167,511</td>
<td align="right">65.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">89,711</td>
<td align="right">34.6%</td>
<td align="right">89,567</td>
<td align="right">34.8%</td>
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
<td align="left">bool</td>
<td align="right">2,848</td>
<td align="right">1.7%</td>
<td align="right">2,563</td>
<td align="right">1.5%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,244</td>
<td align="right">0.7%</td>
<td align="right">1,143</td>
<td align="right">0.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">12,209</td>
<td align="right">7.2%</td>
<td align="right">11,703</td>
<td align="right">7.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">15,628</td>
<td align="right">9.2%</td>
<td align="right">15,166</td>
<td align="right">9.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,394</td>
<td align="right">7.3%</td>
<td align="right">12,212</td>
<td align="right">7.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">8,883</td>
<td align="right">5.2%</td>
<td align="right">8,841</td>
<td align="right">5.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">62,979</td>
<td align="right">37.2%</td>
<td align="right">62,721</td>
<td align="right">37.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,339</td>
<td align="right">16.1%</td>
<td align="right">27,413</td>
<td align="right">16.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,251</td>
<td align="right">11.4%</td>
<td align="right">19,241</td>
<td align="right">11.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,151</td>
<td align="right">1.9%</td>
<td align="right">3,152</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,842</td>
<td align="right">1.7%</td>
<td align="right">2,842</td>
<td align="right">1.7%</td>
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
<td align="right">94,191,901</td>
<td align="right">4.1%</td>
<td align="right">83,462,184</td>
<td align="right">3.7%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,177,558,546</td>
<td align="right">95.8%</td>
<td align="right">2,177,557,124</td>
<td align="right">96.3%</td>
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
<td align="right">1,043,801</td>
<td align="right">0.0%</td>
<td align="right">1,043,801</td>
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
<td align="right">104,336</td>
<td align="right">74.7%</td>
<td align="right">101,450</td>
<td align="right">74.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">35,271</td>
<td align="right">25.3%</td>
<td align="right">35,271</td>
<td align="right">25.8%</td>
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
<td align="right">18,063</td>
<td align="right">17.3%</td>
<td align="right">16,947</td>
<td align="right">16.7%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">23,849</td>
<td align="right">22.9%</td>
<td align="right">23,242</td>
<td align="right">22.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">31,479</td>
<td align="right">30.2%</td>
<td align="right">30,787</td>
<td align="right">30.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,945</td>
<td align="right">29.7%</td>
<td align="right">30,474</td>
<td align="right">30.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">219,979,742</td>
<td align="right">13.5%</td>
<td align="right">186,340,946</td>
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
<td align="right">1,341,351,150</td>
<td align="right">82.6%</td>
<td align="right">1,283,082,170</td>
<td align="right">83.8%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,660,171</td>
<td align="right">3.9%</td>
<td align="right">60,909,495</td>
<td align="right">4.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">207,398</td>
<td align="right">14.3%</td>
<td align="right">188,868</td>
<td align="right">13.5%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,241,392</td>
<td align="right">85.7%</td>
<td align="right">1,208,377</td>
<td align="right">86.5%</td>
<td align="right">-2.7%</td>
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
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">14,829</td>
<td align="right">7.2%</td>
<td align="right">10,350</td>
<td align="right">5.5%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">847</td>
<td align="right">0.4%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,646</td>
<td align="right">1.8%</td>
<td align="right">3,054</td>
<td align="right">1.6%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">18,890</td>
<td align="right">9.1%</td>
<td align="right">16,723</td>
<td align="right">8.9%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,042</td>
<td align="right">5.3%</td>
<td align="right">9,913</td>
<td align="right">5.2%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">10,336</td>
<td align="right">5.0%</td>
<td align="right">9,355</td>
<td align="right">5.0%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,926</td>
<td align="right">3.8%</td>
<td align="right">7,253</td>
<td align="right">3.8%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">78,599</td>
<td align="right">37.9%</td>
<td align="right">73,088</td>
<td align="right">38.7%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,675</td>
<td align="right">2.7%</td>
<td align="right">5,289</td>
<td align="right">2.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
<td align="right">1,096</td>
<td align="right">0.6%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">17,570</td>
<td align="right">8.5%</td>
<td align="right">16,644</td>
<td align="right">8.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,577</td>
<td align="right">9.0%</td>
<td align="right">17,615</td>
<td align="right">9.3%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,496</td>
<td align="right">2.2%</td>
<td align="right">4,435</td>
<td align="right">2.3%</td>
<td align="right">-1.4%</td>
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
<td align="right">12,372,891</td>
<td align="right">12,372,891 / 0 !!</td>
<td align="right">12,380,604</td>
<td align="right">12,380,604 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">173,347,660</td>
<td align="right">173,347,660 / 0 !!</td>
<td align="right">173,313,629</td>
<td align="right">173,313,629 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,510,719</td>
<td align="right">305,510,719 / 0 !!</td>
<td align="right">305,510,153</td>
<td align="right">305,510,153 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,484,574</td>
<td align="right">116,484,574 / 0 !!</td>
<td align="right">116,484,682</td>
<td align="right">116,484,682 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,990,206</td>
<td align="right">336,990,206 / 0 !!</td>
<td align="right">336,989,961</td>
<td align="right">336,989,961 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,671,555</td>
<td align="right">101,671,555 / 0 !!</td>
<td align="right">101,671,495</td>
<td align="right">101,671,495 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,205,175</td>
<td align="right">34,205,175 / 0 !!</td>
<td align="right">34,205,175</td>
<td align="right">34,205,175 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,649,325</td>
<td align="right">5,649,325 / 0 !!</td>
<td align="right">5,649,325</td>
<td align="right">5,649,325 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,297,294</td>
<td align="right">2,297,294 / 0 !!</td>
<td align="right">2,297,294</td>
<td align="right">2,297,294 / 0 !!</td>
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
<td align="right">645,871,089</td>
<td align="right">5.6%</td>
<td align="right">698,074,736</td>
<td align="right">6.1%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">555,790,065</td>
<td align="right">4.8%</td>
<td align="right">543,855,610</td>
<td align="right">4.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,322,429,880</td>
<td align="right">89.6%</td>
<td align="right">10,209,442,759</td>
<td align="right">89.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,133,675</td>
<td align="right">0.0%</td>
<td align="right">1,133,675</td>
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
<td align="right">12,793,776</td>
<td align="right">94.3%</td>
<td align="right">13,778,617</td>
<td align="right">94.8%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">766,906</td>
<td align="right">5.7%</td>
<td align="right">761,876</td>
<td align="right">5.2%</td>
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
<td align="right">78,458</td>
<td align="right">10.2%</td>
<td align="right">75,993</td>
<td align="right">10.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,856</td>
<td align="right">0.4%</td>
<td align="right">2,814</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">76,204</td>
<td align="right">9.9%</td>
<td align="right">75,174</td>
<td align="right">9.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">41,197</td>
<td align="right">5.4%</td>
<td align="right">41,726</td>
<td align="right">5.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,745</td>
<td align="right">0.6%</td>
<td align="right">4,703</td>
<td align="right">0.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,083</td>
<td align="right">2.0%</td>
<td align="right">14,978</td>
<td align="right">2.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">30,642</td>
<td align="right">4.0%</td>
<td align="right">30,487</td>
<td align="right">4.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">12,303</td>
<td align="right">1.6%</td>
<td align="right">12,244</td>
<td align="right">1.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,884</td>
<td align="right">18.1%</td>
<td align="right">138,230</td>
<td align="right">18.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">4,327</td>
<td align="right">0.6%</td>
<td align="right">4,307</td>
<td align="right">0.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,886</td>
<td align="right">2.9%</td>
<td align="right">21,926</td>
<td align="right">2.9%</td>
<td align="right">0.2%</td>
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
<td align="left">non object slot</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
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
<td align="right">4,680,322,846</td>
<td align="right">99.7%</td>
<td align="right">4,546,287,936</td>
<td align="right">99.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,098,961</td>
<td align="right">0.3%</td>
<td align="right">15,098,755</td>
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
<td align="right">302,514</td>
<td align="right">0.0%</td>
<td align="right">302,514</td>
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
<td align="right">525,508</td>
<td align="right">100.0%</td>
<td align="right">525,337</td>
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
<td align="right">6,983</td>
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
<td align="right">67,201,443</td>
<td align="right">100.0%</td>
<td align="right">67,201,375</td>
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
<td align="right">591,434,781</td>
<td align="right">82.1%</td>
<td align="right">591,434,832</td>
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
<td align="right">129,260,570</td>
<td align="right">17.9%</td>
<td align="right">129,260,570</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,527,711</td>
<td align="right">3.1%</td>
<td align="right">60,833,894</td>
<td align="right">3.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">121,306,811</td>
<td align="right">6.1%</td>
<td align="right">120,478,780</td>
<td align="right">6.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,242,980</td>
<td align="right">90.8%</td>
<td align="right">1,813,055,186</td>
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
<td align="left">Success</td>
<td align="right">2,395,070</td>
<td align="right">95.9%</td>
<td align="right">2,379,443</td>
<td align="right">95.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">101,541</td>
<td align="right">4.1%</td>
<td align="right">101,051</td>
<td align="right">4.1%</td>
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
<td align="right">8,313</td>
<td align="right">8.2%</td>
<td align="right">7,830</td>
<td align="right">7.7%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">310,943</td>
<td align="right">306.2%</td>
<td align="right">309,979</td>
<td align="right">306.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
<td align="right">11,033</td>
<td align="right">10.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,627</td>
<td align="right">43.0%</td>
<td align="right">43,626</td>
<td align="right">43.2%</td>
<td align="right">-0.0%</td>
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
<td align="right">7.9%</td>
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
<td align="right">1,039,305</td>
<td align="right">100.0%</td>
<td align="right">-23.0%</td>
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
<td align="right">105,467,002</td>
<td align="right">10.3%</td>
<td align="right">99,368,483</td>
<td align="right">9.8%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">914,511,045</td>
<td align="right">89.7%</td>
<td align="right">914,502,192</td>
<td align="right">90.2%</td>
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
<td align="right">79,984</td>
<td align="right">84.0%</td>
<td align="right">77,636</td>
<td align="right">83.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">16.0%</td>
<td align="right">15,204</td>
<td align="right">16.4%</td>
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
<td align="right">850</td>
<td align="right">1.1%</td>
<td align="right">703</td>
<td align="right">0.9%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">147</td>
<td align="right">0.2%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">2,282</td>
<td align="right">2.9%</td>
<td align="right">2,038</td>
<td align="right">2.6%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,174</td>
<td align="right">20.2%</td>
<td align="right">14,771</td>
<td align="right">19.0%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">7,396</td>
<td align="right">9.5%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
<td align="right">4,445</td>
<td align="right">5.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,076</td>
<td align="right">56.4%</td>
<td align="right">45,076</td>
<td align="right">58.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,060</td>
<td align="right">3.8%</td>
<td align="right">3,060</td>
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
<td align="right">71,625,985</td>
<td align="right">1.6%</td>
<td align="right">70,156,303</td>
<td align="right">1.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">136,350,544</td>
<td align="right">3.1%</td>
<td align="right">134,730,740</td>
<td align="right">3.1%</td>
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
<td align="right">4,188,193,923</td>
<td align="right">95.3%</td>
<td align="right">4,161,559,673</td>
<td align="right">95.3%</td>
<td align="right">-0.6%</td>
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
<td align="right">564,865</td>
<td align="right">26.5%</td>
<td align="right">458,337</td>
<td align="right">22.9%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,569,587</td>
<td align="right">73.5%</td>
<td align="right">1,541,638</td>
<td align="right">77.1%</td>
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
<td align="left">mapping</td>
<td align="right">81,561</td>
<td align="right">14.4%</td>
<td align="right">18,714</td>
<td align="right">4.1%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80,050</td>
<td align="right">14.2%</td>
<td align="right">37,261</td>
<td align="right">8.1%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">6,816</td>
<td align="right">1.2%</td>
<td align="right">6,356</td>
<td align="right">1.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,602</td>
<td align="right">2.1%</td>
<td align="right">11,497</td>
<td align="right">2.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">18,579</td>
<td align="right">3.3%</td>
<td align="right">18,435</td>
<td align="right">4.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">86,823</td>
<td align="right">15.4%</td>
<td align="right">86,674</td>
<td align="right">18.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,930</td>
<td align="right">3.5%</td>
<td align="right">19,905</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,442</td>
<td align="right">45.6%</td>
<td align="right">257,433</td>
<td align="right">56.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.3%</td>
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
<td align="right">1,275,710</td>
<td align="right">0.1%</td>
<td align="right">489,119</td>
<td align="right">0.0%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,240,929,579</td>
<td align="right">99.9%</td>
<td align="right">1,241,271,287</td>
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
<td align="right">2,473</td>
<td align="right">6.2%</td>
<td align="right">2,157</td>
<td align="right">5.5%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,197</td>
<td align="right">93.8%</td>
<td align="right">37,165</td>
<td align="right">94.5%</td>
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
<td align="right">1,779</td>
<td align="right">71.9%</td>
<td align="right">1,463</td>
<td align="right">67.8%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">15.3%</td>
<td align="right">378</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">316</td>
<td align="right">12.8%</td>
<td align="right">316</td>
<td align="right">14.6%</td>
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
<td align="right">1,133,769,264</td>
<td align="right">1.1%</td>
<td align="right">1,190,134,407</td>
<td align="right">1.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,257,946,368</td>
<td align="right">3.2%</td>
<td align="right">3,103,650,284</td>
<td align="right">3.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">36,448,705,546</td>
<td align="right">36.1%</td>
<td align="right">35,290,344,452</td>
<td align="right">36.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">60,098,417,259</td>
<td align="right">59.5%</td>
<td align="right">58,416,611,088</td>
<td align="right">59.6%</td>
<td align="right">-2.8%</td>
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
<td align="right">219,979,742</td>
<td align="right">7.7%</td>
<td align="right">186,340,946</td>
<td align="right">6.9%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,191,901</td>
<td align="right">3.3%</td>
<td align="right">83,462,184</td>
<td align="right">3.1%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,089,672,394</td>
<td align="right">38.2%</td>
<td align="right">1,020,028,795</td>
<td align="right">37.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,636,766</td>
<td align="right">3.4%</td>
<td align="right">90,493,002</td>
<td align="right">3.3%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,467,002</td>
<td align="right">3.7%</td>
<td align="right">99,368,483</td>
<td align="right">3.7%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">161,190,588</td>
<td align="right">5.7%</td>
<td align="right">165,642,963</td>
<td align="right">6.1%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">555,790,065</td>
<td align="right">19.5%</td>
<td align="right">543,855,610</td>
<td align="right">20.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">6.4%</td>
<td align="right">179,235,008</td>
<td align="right">6.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">136,350,544</td>
<td align="right">4.8%</td>
<td align="right">134,730,740</td>
<td align="right">5.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,260,570</td>
<td align="right">4.5%</td>
<td align="right">129,260,570</td>
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
<td align="right">188,926,271</td>
<td align="right">16.7%</td>
<td align="right">210,782,633</td>
<td align="right">17.7%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">238,585,082</td>
<td align="right">21.0%</td>
<td align="right">264,772,936</td>
<td align="right">22.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,304,809</td>
<td align="right">5.5%</td>
<td align="right">67,891,056</td>
<td align="right">5.7%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,344,721</td>
<td align="right">2.8%</td>
<td align="right">30,378,918</td>
<td align="right">2.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,085,095</td>
<td align="right">7.2%</td>
<td align="right">84,573,904</td>
<td align="right">7.1%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">33,621,454</td>
<td align="right">3.0%</td>
<td align="right">32,609,063</td>
<td align="right">2.7%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,871,265</td>
<td align="right">7.0%</td>
<td align="right">81,020,488</td>
<td align="right">6.8%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,233,202</td>
<td align="right">2.8%</td>
<td align="right">30,448,329</td>
<td align="right">2.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">103,205,504</td>
<td align="right">9.1%</td>
<td align="right">102,354,504</td>
<td align="right">8.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">31,597,052</td>
<td align="right">2.8%</td>
<td align="right">31,839,971</td>
<td align="right">2.7%</td>
<td align="right">0.8%</td>
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
<td align="right">5,133,642,506</td>
<td align="right">76.9%</td>
<td align="right">5,133,932,946</td>
<td align="right">76.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,287,383</td>
<td align="right">4.1%</td>
<td align="right">274,274,478</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">956,853,359</td>
<td align="right">14.3%</td>
<td align="right">956,840,257</td>
<td align="right">14.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">961,127,596</td>
<td align="right">14.4%</td>
<td align="right">961,114,494</td>
<td align="right">14.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,547,793</td>
<td align="right">1.1%</td>
<td align="right">71,547,039</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,292,361</td>
<td align="right">23.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,292,361</td>
<td align="right">23.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,412,593,406</td>
<td align="right">81.0%</td>
<td align="right">5,412,560,568</td>
<td align="right">81.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,808,724</td>
<td align="right">0.4%</td>
<td align="right">23,808,701</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,534,148</td>
<td align="right">3.9%</td>
<td align="right">259,534,169</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,177,825</td>
<td align="right">8.7%</td>
<td align="right">584,177,867</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,223,922</td>
<td align="right">0.1%</td>
<td align="right">4,223,922</td>
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
<td align="right">2.0%</td>
<td align="right">131,916,029</td>
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
<td align="right">5,413,778</td>
<td align="right"></td>
<td align="right">5,956,406</td>
<td align="right"></td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,944,917</td>
<td align="right"></td>
<td align="right">62,258,243</td>
<td align="right"></td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,219,901</td>
<td align="right"></td>
<td align="right">56,992,577</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,222,621,787</td>
<td align="right">1.2%</td>
<td align="right">1,201,354,214</td>
<td align="right">1.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,058,718,317</td>
<td align="right">27.4%</td>
<td align="right">24,651,461,831</td>
<td align="right">26.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,097,666,436</td>
<td align="right"></td>
<td align="right">2,125,831,352</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,450,943,535</td>
<td align="right">31.7%</td>
<td align="right">33,027,122,845</td>
<td align="right">31.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">39,457,744,597</td>
<td align="right">43.1%</td>
<td align="right">39,915,040,602</td>
<td align="right">43.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,959,789,714</td>
<td align="right">3.2%</td>
<td align="right">2,925,945,131</td>
<td align="right">3.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,749,828,742</td>
<td align="right">46.1%</td>
<td align="right">49,224,320,808</td>
<td align="right">46.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,107,028,623</td>
<td align="right">26.3%</td>
<td align="right">24,167,605,121</td>
<td align="right">26.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">22,223,934,265</td>
<td align="right">21.0%</td>
<td align="right">22,272,997,580</td>
<td align="right">21.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,369,279,297</td>
<td align="right"></td>
<td align="right">2,371,518,808</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,604,905</td>
<td align="right">0.0%</td>
<td align="right">6,609,919</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,699,735</td>
<td align="right">0.4%</td>
<td align="right">71,741,238</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,110,276,873</td>
<td align="right"></td>
<td align="right">6,110,760,362</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,453,235,141</td>
<td align="right"></td>
<td align="right">13,453,044,598</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,451,523,783</td>
<td align="right">70.8%</td>
<td align="right">13,451,383,515</td>
<td align="right">70.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,473,463,657</td>
<td align="right">28.8%</td>
<td align="right">5,473,425,543</td>
<td align="right">28.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,551,768,297</td>
<td align="right">29.2%</td>
<td align="right">5,551,776,700</td>
<td align="right">29.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,375,775</td>
<td align="right"></td>
<td align="right">177,375,800</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,639,155</td>
<td align="right">2.1%</td>
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
<td align="right">366,958</td>
<td align="right">93,688,569</td>
<td align="right">9,728,604,736</td>
<td align="right">813,026,789</td>
<td align="right">753,520,155</td>
<td align="right">366,907</td>
<td align="right">94,016,194</td>
<td align="right">9,754,380,831</td>
<td align="right">810,034,558</td>
<td align="right">757,763,867</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,441,612</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,434,428</td>
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
<td align="right">601</td>
<td align="right">1.7%</td>
<td align="right">3,105</td>
<td align="right">3.8%</td>
<td align="right">416.6%</td>
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
<td align="right">827</td>
<td align="right">0.2%</td>
<td align="right">313.5%</td>
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
<td align="right">703</td>
<td align="right">0.1%</td>
<td align="right">286.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">848</td>
<td align="right">0.2%</td>
<td align="right">1,968</td>
<td align="right">0.4%</td>
<td align="right">132.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">36,288</td>
<td align="right">8.2%</td>
<td align="right">82,621</td>
<td align="right">15.2%</td>
<td align="right">127.7%</td>
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
<td align="right">6,704</td>
<td align="right">1.2%</td>
<td align="right">110.5%</td>
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
<td align="right">1,870</td>
<td align="right">0.3%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">133,907</td>
<td align="right">30.4%</td>
<td align="right">185,731</td>
<td align="right">34.1%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">440,652</td>
<td align="right"></td>
<td align="right">544,367</td>
<td align="right"></td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">246,170,805,405</td>
<td align="right">6,387.5%</td>
<td align="right">252,832,945,331</td>
<td align="right">6,496.9%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">223,409</td>
<td align="right">50.7%</td>
<td align="right">228,401</td>
<td align="right">42.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,853,951,237</td>
<td align="right"></td>
<td align="right">3,891,596,556</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">46,848</td>
<td align="right">10.6%</td>
<td align="right">46,787</td>
<td align="right">8.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">30,661</td>
<td align="right">84.5%</td>
<td align="right">72,194</td>
<td align="right">87.4%</td>
<td align="right">135.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">36,288</td>
<td align="right"></td>
<td align="right">82,621</td>
<td align="right"></td>
<td align="right">127.7%</td>
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
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">65,955,637</td>
<td align="right">16.0%</td>
<td align="right">154,546,835</td>
<td align="right">16.3%</td>
<td align="right">134.3%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">8,681,176</td>
<td align="right">2.1%</td>
<td align="right">20,166,064</td>
<td align="right">2.1%</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">411,242,496</td>
<td align="right"></td>
<td align="right">946,274,304</td>
<td align="right"></td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">336,605,683</td>
<td align="right">81.9%</td>
<td align="right">771,561,405</td>
<td align="right">81.5%</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">4,169,728</td>
<td align="right">1.0%</td>
<td align="right">4,866,048</td>
<td align="right">0.5%</td>
<td align="right">16.7%</td>
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
<td align="left">6,721</td>
<td align="right">21.9%</td>
<td align="left">10,337</td>
<td align="right">14.3%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">9,538</td>
<td align="right">31.1%</td>
<td align="left">27,301</td>
<td align="right">37.8%</td>
<td align="right">186.2%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,470</td>
<td align="right">27.6%</td>
<td align="left">22,767</td>
<td align="right">31.5%</td>
<td align="right">168.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,081</td>
<td align="right">13.3%</td>
<td align="left">8,811</td>
<td align="right">12.2%</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,691</td>
<td align="right">5.5%</td>
<td align="left">2,538</td>
<td align="right">3.5%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">160</td>
<td align="right">0.5%</td>
<td align="left">440</td>
<td align="right">0.6%</td>
<td align="right">175.0%</td>
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
<td align="right">1,423</td>
<td align="right">3.9%</td>
<td align="right">1,767</td>
<td align="right">2.1%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,481</td>
<td align="right">4.1%</td>
<td align="right">1,808</td>
<td align="right">2.2%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,422</td>
<td align="right">14.9%</td>
<td align="right">10,063</td>
<td align="right">12.2%</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,375</td>
<td align="right">28.6%</td>
<td align="right">30,465</td>
<td align="right">36.9%</td>
<td align="right">193.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,395</td>
<td align="right">20.4%</td>
<td align="right">19,149</td>
<td align="right">23.2%</td>
<td align="right">158.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,994</td>
<td align="right">19.3%</td>
<td align="right">14,486</td>
<td align="right">17.5%</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,691</td>
<td align="right">7.4%</td>
<td align="right">3,675</td>
<td align="right">4.4%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">507</td>
<td align="right">1.4%</td>
<td align="right">1,208</td>
<td align="right">1.5%</td>
<td align="right">138.3%</td>
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
<td align="right">800</td>
<td align="right">2.2%</td>
<td align="right">1,023</td>
<td align="right">1.2%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,120</td>
<td align="right">3.1%</td>
<td align="right">1,337</td>
<td align="right">1.6%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,653</td>
<td align="right">7.3%</td>
<td align="right">3,426</td>
<td align="right">4.1%</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,072</td>
<td align="right">27.8%</td>
<td align="right">26,534</td>
<td align="right">32.1%</td>
<td align="right">163.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,433</td>
<td align="right">23.2%</td>
<td align="right">24,093</td>
<td align="right">29.2%</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,222</td>
<td align="right">11.6%</td>
<td align="right">10,187</td>
<td align="right">12.3%</td>
<td align="right">141.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,831</td>
<td align="right">7.8%</td>
<td align="right">4,487</td>
<td align="right">5.4%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">530</td>
<td align="right">1.5%</td>
<td align="right">1,107</td>
<td align="right">1.3%</td>
<td align="right">108.9%</td>
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
<td align="right">23,212</td>
<td align="right">296,772</td>
<td align="right">1,178.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">295,029</td>
<td align="right">1,001.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,614,520</td>
<td align="right">36,209,220</td>
<td align="right">447.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">158,441</td>
<td align="right">493,979</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">4,011</td>
<td align="right">208.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">1,169,280</td>
<td align="right">205.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,508,076</td>
<td align="right">3,688,559</td>
<td align="right">144.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">577,331</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,220,780</td>
<td align="right">768,020</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">52,938</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">105,202</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">1,791,620</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,342,889</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">85,608</td>
<td align="right">132,082</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">53,040</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,310,575</td>
<td align="right">1,623,086</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">30,032,954</td>
<td align="right">37,100,323</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,890,144</td>
<td align="right">3,527,219</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">35,266,120</td>
<td align="right">27,708,503</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,001,422</td>
<td align="right">14,292,103</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,961,160</td>
<td align="right">5,861,592</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">25,999,567</td>
<td align="right">30,699,890</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">3,156,992</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,688,088</td>
<td align="right">72,402,361</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">92,672,199</td>
<td align="right">108,642,981</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">91,976,259</td>
<td align="right">107,784,781</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,976,259</td>
<td align="right">107,784,781</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">5,014,896</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">66,306,036</td>
<td align="right">56,378,337</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">256,380,769</td>
<td align="right">290,743,973</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,374,659</td>
<td align="right">8,358,140</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">142,536,503</td>
<td align="right">161,439,084</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,571,606</td>
<td align="right">13,099,986</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">115,502,589</td>
<td align="right">130,750,061</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">162,702,378</td>
<td align="right">183,751,528</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">55,721,213</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">55,721,213</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,001,870</td>
<td align="right">5,578,719</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">41,429,630</td>
<td align="right">46,038,269</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">236,844,758</td>
<td align="right">262,647,127</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">202,428,941</td>
<td align="right">180,393,181</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,111,777</td>
<td align="right">219,079,751</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">486,650,286</td>
<td align="right">537,229,932</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,818,132</td>
<td align="right">77,026,812</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">565,765,041</td>
<td align="right">622,781,811</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">641,796,101</td>
<td align="right">706,329,865</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">43,824,341</td>
<td align="right">39,474,290</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">111,244,816</td>
<td align="right">122,014,345</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,115,165</td>
<td align="right">47,234,733</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,956,010</td>
<td align="right">7,601,861</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">116,173,764</td>
<td align="right">126,830,393</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">249,694,147</td>
<td align="right">272,315,906</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">149,494,909</td>
<td align="right">163,008,932</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">339,011,007</td>
<td align="right">369,579,177</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">362,500</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,012,080</td>
<td align="right">3,269,160</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">227,548,352</td>
<td align="right">246,620,564</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">399,613,664</td>
<td align="right">431,637,270</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">200,489,676</td>
<td align="right">185,129,773</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">11,508,290</td>
<td align="right">10,649,119</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">153,190,275</td>
<td align="right">164,577,896</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">45,824,616</td>
<td align="right">49,200,091</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">314,923,603</td>
<td align="right">338,000,773</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">808,811,386</td>
<td align="right">865,592,178</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">252,435,301</td>
<td align="right">270,103,662</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,545,300</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">234,976,012</td>
<td align="right">251,088,127</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">295,017,830</td>
<td align="right">314,805,327</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,922,208</td>
<td align="right">4,185,005</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">180,319,232</td>
<td align="right">168,347,936</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">107,112,198</td>
<td align="right">114,187,904</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,770,516</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">18,771,684</td>
<td align="right">19,958,057</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">23,550,310</td>
<td align="right">25,016,087</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">23,550,310</td>
<td align="right">25,016,087</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,052,929</td>
<td align="right">6,423,675</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">36,763,718</td>
<td align="right">38,999,677</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">399,379,185</td>
<td align="right">423,606,186</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">338,666,797</td>
<td align="right">359,200,608</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,822,600</td>
<td align="right">2,990,200</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,822,600</td>
<td align="right">2,990,200</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">701,495,336</td>
<td align="right">741,423,596</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">735,007,110</td>
<td align="right">775,745,678</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,241,707,913</td>
<td align="right">1,310,074,286</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">73,369,959</td>
<td align="right">77,310,458</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">278,554,136</td>
<td align="right">293,092,130</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,425,772,334</td>
<td align="right">1,498,042,285</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,425,395,783</td>
<td align="right">1,497,580,673</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">553,034,326</td>
<td align="right">580,985,231</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">100,976,530</td>
<td align="right">106,003,445</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">143,855,102</td>
<td align="right">150,881,397</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">541,777,961</td>
<td align="right">567,146,017</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,106,940</td>
<td align="right">44,057,574</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">36,367,438</td>
<td align="right">37,988,546</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">412,052,824</td>
<td align="right">430,275,083</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,713,627</td>
<td align="right">36,209,392</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">444,050,141</td>
<td align="right">461,809,723</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,416,888,642</td>
<td align="right">1,473,493,197</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">43,982,703</td>
<td align="right">45,706,546</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,065,840</td>
<td align="right">48,803,180</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">390,330,773</td>
<td align="right">404,591,444</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,004,730</td>
<td align="right">149,247,244</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">166,103,292</td>
<td align="right">172,138,133</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,991,098,869</td>
<td align="right">7,243,189,279</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,864,801,136</td>
<td align="right">1,931,455,504</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,833,921,008</td>
<td align="right">3,968,818,880</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,295,551,573</td>
<td align="right">1,340,904,730</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,460,483</td>
<td align="right">57,401,690</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,769,162,246</td>
<td align="right">3,900,890,742</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">966,635,522</td>
<td align="right">999,952,036</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,341,207,748</td>
<td align="right">36,551,429,319</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">966,500,562</td>
<td align="right">999,441,062</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">148,138,116</td>
<td align="right">143,159,554</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,790,704,815</td>
<td align="right">2,882,983,003</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">467,492,443</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">467,492,443</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">431,668,601</td>
<td align="right">445,380,019</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">29,768,070</td>
<td align="right">30,699,535</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">29,768,070</td>
<td align="right">30,699,535</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,978,645,153</td>
<td align="right">4,099,366,708</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,476,152</td>
<td align="right">48,905,561</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,370,578,180</td>
<td align="right">41,571,091,549</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,697,295</td>
<td align="right">38,810,334</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">188,493,771</td>
<td align="right">194,047,945</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,549,838</td>
<td align="right">120,983,576</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,863,459,040</td>
<td align="right">8,091,885,626</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">39,305,461</td>
<td align="right">40,425,502</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,961,242,711</td>
<td align="right">11,271,794,148</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,794,882,981</td>
<td align="right">1,845,486,842</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,546,104,524</td>
<td align="right">1,589,032,936</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">13,260,066</td>
<td align="right">13,627,601</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">453,847,045</td>
<td align="right">466,290,470</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">461,592,496</td>
<td align="right">474,216,584</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,394,828</td>
<td align="right">48,649,988</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">757,567,708</td>
<td align="right">777,471,567</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,034,320</td>
<td align="right">74,913,260</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,383,174</td>
<td align="right">658,531,991</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,450,393,988</td>
<td align="right">3,536,363,745</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,350,347,856</td>
<td align="right">1,383,839,154</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,220,887,308</td>
<td align="right">1,250,964,357</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,798,940,417</td>
<td align="right">1,842,147,554</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,876,523,140</td>
<td align="right">2,945,483,725</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">352,930,430</td>
<td align="right">361,191,696</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">296,755,796</td>
<td align="right">289,916,397</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,193,684</td>
<td align="right">47,213,119</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,953,138,076</td>
<td align="right">3,017,695,255</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">317,001,818</td>
<td align="right">310,284,777</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,075,674,646</td>
<td align="right">1,098,161,145</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,348,454,898</td>
<td align="right">4,439,041,121</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,264,815</td>
<td align="right">56,400,521</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,243,616,102</td>
<td align="right">2,289,604,972</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,454,808,392</td>
<td align="right">2,503,931,602</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,010,421,801</td>
<td align="right">1,030,291,014</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,154,167,843</td>
<td align="right">2,196,354,031</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,220,144</td>
<td align="right">3,282,173</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">39,464,124</td>
<td align="right">40,216,063</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,913,472,764</td>
<td align="right">3,987,852,285</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">73,836,596</td>
<td align="right">72,465,006</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">136,640,971</td>
<td align="right">139,138,639</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,016,106,830</td>
<td align="right">2,051,403,684</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">528,091,463</td>
<td align="right">537,228,093</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,249,948,372</td>
<td align="right">1,269,975,532</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,249,948,372</td>
<td align="right">1,269,975,532</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,172,826,339</td>
<td align="right">1,191,573,840</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">846,845,553</td>
<td align="right">860,225,465</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,139,612,007</td>
<td align="right">1,157,576,164</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">406,927,868</td>
<td align="right">413,101,877</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,339,808,206</td>
<td align="right">1,359,960,137</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,960,962</td>
<td align="right">20,257,786</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">54,918,418</td>
<td align="right">54,125,687</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,237,946,950</td>
<td align="right">1,255,683,429</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,342,629,585</td>
<td align="right">2,376,078,914</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,205,621,742</td>
<td align="right">1,222,698,501</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,110,691,604</td>
<td align="right">1,126,280,438</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,957,410</td>
<td align="right">34,471,524</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,308,759,629</td>
<td align="right">6,395,528,158</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,871,924</td>
<td align="right">39,406,070</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,771,141</td>
<td align="right">528,902,016</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,831,083,876</td>
<td align="right">2,869,080,338</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,186,716</td>
<td align="right">140,016,387</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">952,750,306</td>
<td align="right">965,296,028</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,002,700,616</td>
<td align="right">1,015,203,254</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">971,534,463</td>
<td align="right">982,716,184</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,276,662</td>
<td align="right">1,180,360,866</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">494,105,970</td>
<td align="right">499,469,279</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">460,952,104</td>
<td align="right">465,921,069</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">593,441,283</td>
<td align="right">599,539,518</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,818,970,615</td>
<td align="right">3,856,828,260</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,853,951,237</td>
<td align="right">3,891,596,556</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">69,571,394</td>
<td align="right">70,237,582</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">69,571,394</td>
<td align="right">70,237,582</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">46,728,468</td>
<td align="right">47,165,023</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,401,747,121</td>
<td align="right">4,442,728,108</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">357,814,305</td>
<td align="right">361,122,173</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">427,994,534</td>
<td align="right">431,836,993</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">769,932,725</td>
<td align="right">775,892,085</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">644,193,077</td>
<td align="right">649,156,177</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">254,794,593</td>
<td align="right">256,754,048</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">966,661,248</td>
<td align="right">974,007,599</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">911,622,888</td>
<td align="right">918,293,332</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,546,900</td>
<td align="right">59,967,087</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">911,622,888</td>
<td align="right">917,920,855</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,052,114,763</td>
<td align="right">1,059,226,143</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">150,369,864</td>
<td align="right">149,359,118</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">1,557,554,920</td>
<td align="right">1,567,859,636</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,003,700</td>
<td align="right">3,023,520</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">71,532,780</td>
<td align="right">71,985,060</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,473,111,819</td>
<td align="right">2,487,253,782</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,341,749,232</td>
<td align="right">1,348,953,785</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">168,158,180</td>
<td align="right">169,008,909</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">488,377,932</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">467,890,537</td>
<td align="right">470,022,271</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,468,813,756</td>
<td align="right">1,474,897,593</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">17,372,080</td>
<td align="right">17,425,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,376,320</td>
<td align="right">111,686,820</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,195,783,677</td>
<td align="right">1,199,086,775</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,171,220</td>
<td align="right">3,162,960</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,263,836</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,263,836</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">93,891,060</td>
<td align="right">94,129,140</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">225,785,209</td>
<td align="right">226,301,517</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">106,388,800</td>
<td align="right">106,622,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,294,340,277</td>
<td align="right">1,296,475,775</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">749,042,877</td>
<td align="right">749,706,935</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">169,036,781</td>
<td align="right">169,141,225</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,285,386</td>
<td align="right">746,635,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,997,705,814</td>
<td align="right">1,998,465,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">28,969,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right"></td>
<td align="right">1,521,587</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">1,521,587</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TYPE_1</td>
<td align="right"></td>
<td align="right">257,252</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">88,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">88,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">10,059</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">4,023</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">2,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">480</td>
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
<td align="right">23,356</td>
<td align="right">25,713</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,728</td>
<td align="right">1,672</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,981</td>
<td align="right">23,104</td>
<td align="right">0.5%</td>
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
<td align="right">625</td>
<td align="right">55.9%</td>
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
<td align="right">625</td>
<td align="right">55.9%</td>
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
