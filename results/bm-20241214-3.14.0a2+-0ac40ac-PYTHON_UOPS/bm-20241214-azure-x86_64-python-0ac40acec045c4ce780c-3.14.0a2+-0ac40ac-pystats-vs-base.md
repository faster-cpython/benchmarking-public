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
<td align="right">112,686,498</td>
<td align="right">1,194,074</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,826,705,619</td>
<td align="right">210,376,406</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">69,928,275</td>
<td align="right">3,256,405</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,733,808,454</td>
<td align="right">214,146,719</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">635,440,230</td>
<td align="right">55,976,875</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,498,504,455</td>
<td align="right">137,997,265</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,289,305</td>
<td align="right">61,722,091</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,758,213,645</td>
<td align="right">197,325,705</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,279,350,723</td>
<td align="right">291,081,461</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,497,513,209</td>
<td align="right">455,962,996</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,780,243</td>
<td align="right">236,080</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,188,601,011</td>
<td align="right">300,178,507</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">420,264,585</td>
<td align="right">58,583,927</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,275,854,894</td>
<td align="right">320,808,771</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,425,095,672</td>
<td align="right">202,483,150</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,378,248</td>
<td align="right">158,212,337</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,290,078,837</td>
<td align="right">195,706,353</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,611,844,621</td>
<td align="right">253,203,056</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">200,976,213</td>
<td align="right">31,630,238</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">375,914,524</td>
<td align="right">63,762,585</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,663,276,738</td>
<td align="right">288,325,345</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">702,706,756</td>
<td align="right">135,262,102</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">397,376,960</td>
<td align="right">76,561,022</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">544,240,428</td>
<td align="right">107,621,402</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">510,779,425</td>
<td align="right">101,288,014</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">352,903,006</td>
<td align="right">72,428,473</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,972,143</td>
<td align="right">18,791,317</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,381,353,986</td>
<td align="right">500,292,257</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,261,395,424</td>
<td align="right">267,178,736</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,820,196</td>
<td align="right">33,284,515</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,353,098,006</td>
<td align="right">1,617,802,208</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,348,960</td>
<td align="right">2,692,098</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,785,690,159</td>
<td align="right">661,443,714</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,069,958,913</td>
<td align="right">260,318,528</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">156,182,589</td>
<td align="right">38,232,005</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">260,655,931</td>
<td align="right">66,263,367</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">380,060,601</td>
<td align="right">96,878,551</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">554,510,589</td>
<td align="right">142,155,485</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,458,059</td>
<td align="right">34,324,371</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">709,019,690</td>
<td align="right">188,929,991</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,528,750,688</td>
<td align="right">682,997,190</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,811,554,364</td>
<td align="right">490,593,842</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,778,117,661</td>
<td align="right">3,998,440,802</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,055,158,429</td>
<td align="right">1,763,403,400</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,671,027,670</td>
<td align="right">778,379,867</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,354,059,403</td>
<td align="right">3,326,993,334</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">794,749,422</td>
<td align="right">232,949,440</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">238,606,028</td>
<td align="right">71,797,469</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">360,319,267</td>
<td align="right">108,817,372</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,152,422,349</td>
<td align="right">348,093,003</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,082,656,335</td>
<td align="right">330,674,419</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">457,693,041</td>
<td align="right">140,105,657</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,041,734,712</td>
<td align="right">3,397,620,404</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,102,823</td>
<td align="right">23,579,734</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">928,277,818</td>
<td align="right">294,685,558</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,419</td>
<td align="right">36,600,185</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,977,752</td>
<td align="right">23,917,604</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">278,058,041</td>
<td align="right">89,706,146</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,965,692</td>
<td align="right">11,645,005</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,616,933</td>
<td align="right">24,078,351</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,544,409</td>
<td align="right">206,703,671</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">123,763,240</td>
<td align="right">43,861,782</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">183,463,271</td>
<td align="right">65,657,914</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">63,155,511</td>
<td align="right">22,609,730</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,202,978,126</td>
<td align="right">434,349,160</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">38,942,185,365</td>
<td align="right">14,668,228,288</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">552,232,067</td>
<td align="right">208,680,753</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">225,801,305</td>
<td align="right">85,803,030</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">809,831,506</td>
<td align="right">309,389,553</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,640,865</td>
<td align="right">49,188,919</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">277,030,710</td>
<td align="right">110,438,102</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">118,345,567</td>
<td align="right">47,192,576</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">829,027,876</td>
<td align="right">336,294,460</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,203,385,841</td>
<td align="right">900,948,343</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,573,040</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,504,827</td>
<td align="right">169,934,747</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">408,634,354</td>
<td align="right">172,823,767</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,940,305,647</td>
<td align="right">3,169,029,439</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,002,954,820</td>
<td align="right">2,314,246,685</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">83,489,232</td>
<td align="right">38,714,654</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,394,696,574</td>
<td align="right">655,721,399</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">75,780,326</td>
<td align="right">35,940,090</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">242,605,553</td>
<td align="right">115,226,176</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,447,791,849</td>
<td align="right">689,935,060</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">335,670,500</td>
<td align="right">160,716,459</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">405,853,736</td>
<td align="right">195,010,031</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">338,852,091</td>
<td align="right">164,590,512</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,755</td>
<td align="right">4,866,975</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,088,596,273</td>
<td align="right">2,049,699,007</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,749,094</td>
<td align="right">3,901,052</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,341,634,320</td>
<td align="right">678,482,747</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,576,149,568</td>
<td align="right">1,312,161,501</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">83,382,949</td>
<td align="right">42,797,489</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,421,333</td>
<td align="right">97,908,478</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">296,887,208</td>
<td align="right">159,640,696</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">224,190,845</td>
<td align="right">125,245,113</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,199,729</td>
<td align="right">4,103,992</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">192,130,972</td>
<td align="right">109,842,844</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,431,472,489</td>
<td align="right">1,964,559,058</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,909,761,203</td>
<td align="right">1,117,498,849</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">315,292,529</td>
<td align="right">184,928,997</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">188,702,515</td>
<td align="right">115,327,022</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,185,896</td>
<td align="right">112,073,920</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">122,654,770</td>
<td align="right">75,094,601</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,025,693,735</td>
<td align="right">633,147,789</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">34,914,304</td>
<td align="right">21,726,246</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">804,700,778</td>
<td align="right">501,226,938</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,660,701,314</td>
<td align="right">4,173,700,764</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">100,238,909</td>
<td align="right">63,125,477</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">101,155,709</td>
<td align="right">63,822,174</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">119,052,406</td>
<td align="right">76,360,147</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">331,233,786</td>
<td align="right">218,654,087</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">517,528,551</td>
<td align="right">344,103,429</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,617,452,488</td>
<td align="right">2,408,224,927</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">80,924,400</td>
<td align="right">54,683,738</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">965,748,471</td>
<td align="right">658,159,789</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">586,056,347</td>
<td align="right">419,739,465</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">541,084,645</td>
<td align="right">395,841,941</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,117,453</td>
<td align="right">2,285,362</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,539,395</td>
<td align="right">139,897,220</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,346,416,083</td>
<td align="right">2,483,674,878</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">83,063,462</td>
<td align="right">61,718,887</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">26,405,087</td>
<td align="right">19,751,952</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,532,313</td>
<td align="right">117,353,343</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,987,040</td>
<td align="right">58,924,253</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">117,118,918</td>
<td align="right">90,263,940</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,875,293</td>
<td align="right">1,486,457</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">37,985,818</td>
<td align="right">30,802,377</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">97,957,178</td>
<td align="right">80,265,456</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,319,365,002</td>
<td align="right">1,120,849,464</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,607,543,697</td>
<td align="right">4,832,989,263</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">1,436,308</td>
<td align="right">1,282,641</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86,497,587</td>
<td align="right">79,071,363</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">6,351,447</td>
<td align="right">5,812,930</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,193,002</td>
<td align="right">9,349,611</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">93,035,033</td>
<td align="right">85,625,216</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">10,000,414</td>
<td align="right">9,255,525</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">399,252,319</td>
<td align="right">370,658,660</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">422,124,966</td>
<td align="right">398,437,807</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">75,402,619</td>
<td align="right">72,199,578</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,812,576</td>
<td align="right">3,969,320</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">78,851,646</td>
<td align="right">75,828,365</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">102,408,984</td>
<td align="right">98,528,963</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,119,780,416</td>
<td align="right">1,078,217,141</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">15,748,096</td>
<td align="right">15,283,638</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,650</td>
<td align="right">2,708</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">170,068,018</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,859,108,875</td>
<td align="right">1,844,313,202</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">155,575,252</td>
<td align="right">154,629,584</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">78,405,240</td>
<td align="right">78,097,889</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">107,119,821</td>
<td align="right">106,721,692</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,034,256</td>
<td align="right">100,838,189</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,780</td>
<td align="right">120,879</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,731</td>
<td align="right">33,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,490</td>
<td align="right">14,760,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,829,668</td>
<td align="right">1,829,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,482,455</td>
<td align="right">21,481,943</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,813,076</td>
<td align="right">21,812,564</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,813,055</td>
<td align="right">21,812,544</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">183,507,687</td>
<td align="right">183,508,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,183,528</td>
<td align="right">6,183,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">5,919,256</td>
<td align="right">5,919,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,662,579</td>
<td align="right">302,662,579</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,591</td>
<td align="right">128,850,591</td>
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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">9,778,041</td>
<td align="right">9,778,041</td>
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
<td align="left">DELETE_FAST</td>
<td align="right">1,200,677</td>
<td align="right">1,200,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">793,140</td>
<td align="right">793,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,673</td>
<td align="right">84,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,193</td>
<td align="right">57,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
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
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">3,832</td>
<td align="right">3,832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,642</td>
<td align="right">3,642</td>
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
<td align="right">150</td>
<td align="right">150</td>
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
<td align="right">44</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">1,975,689,442</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,400,900,632</td>
<td align="right">86.8%</td>
<td align="right">1,185,492,748</td>
<td align="right">77.1%</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,081,441,478</td>
<td align="right">12.7%</td>
<td align="right">329,866,772</td>
<td align="right">21.5%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,988,090</td>
<td align="right">0.4%</td>
<td align="right">20,474,645</td>
<td align="right">1.3%</td>
<td align="right">-46.1%</td>
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
<td align="right">723,851</td>
<td align="right">37.5%</td>
<td align="right">393,424</td>
<td align="right">33.0%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,207,756</td>
<td align="right">62.5%</td>
<td align="right">800,578</td>
<td align="right">67.0%</td>
<td align="right">-33.7%</td>
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
<td align="left">xor</td>
<td align="right">18,902</td>
<td align="right">1.6%</td>
<td align="right">1,331</td>
<td align="right">0.2%</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,588</td>
<td align="right">1.0%</td>
<td align="right">1,407</td>
<td align="right">0.2%</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,518</td>
<td align="right">1.9%</td>
<td align="right">3,299</td>
<td align="right">0.4%</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,491</td>
<td align="right">1.6%</td>
<td align="right">4,912</td>
<td align="right">0.6%</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">176,805</td>
<td align="right">14.6%</td>
<td align="right">45,595</td>
<td align="right">5.7%</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">34,857</td>
<td align="right">2.9%</td>
<td align="right">9,883</td>
<td align="right">1.2%</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,210</td>
<td align="right">0.7%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">176,052</td>
<td align="right">14.6%</td>
<td align="right">52,014</td>
<td align="right">6.5%</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">19,948</td>
<td align="right">1.7%</td>
<td align="right">6,087</td>
<td align="right">0.8%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,624</td>
<td align="right">3.6%</td>
<td align="right">13,731</td>
<td align="right">1.7%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,408</td>
<td align="right">0.1%</td>
<td align="right">649</td>
<td align="right">0.1%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,728</td>
<td align="right">0.7%</td>
<td align="right">4,428</td>
<td align="right">0.6%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,984</td>
<td align="right">2.8%</td>
<td align="right">19,859</td>
<td align="right">2.5%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">38,106</td>
<td align="right">3.2%</td>
<td align="right">24,960</td>
<td align="right">3.1%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">7,784</td>
<td align="right">0.6%</td>
<td align="right">6,914</td>
<td align="right">0.9%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">580,547</td>
<td align="right">48.1%</td>
<td align="right">600,803</td>
<td align="right">75.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,403</td>
<td align="right">0.1%</td>
<td align="right">1,404</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">123</td>
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
<td align="right">182,421,333</td>
<td align="right">100.0%</td>
<td align="right">97,908,478</td>
<td align="right">100.0%</td>
<td align="right">-46.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,595,117,076</td>
<td align="right">70.1%</td>
<td align="right">1,100,587,289</td>
<td align="right">68.5%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,380,726,896</td>
<td align="right">29.8%</td>
<td align="right">500,124,249</td>
<td align="right">31.1%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,928,672</td>
<td align="right">0.1%</td>
<td align="right">5,825,208</td>
<td align="right">0.4%</td>
<td align="right">-1.7%</td>
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
<td align="right">618,820</td>
<td align="right">83.8%</td>
<td align="right">158,766</td>
<td align="right">57.2%</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,919</td>
<td align="right">16.2%</td>
<td align="right">118,915</td>
<td align="right">42.8%</td>
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
<td align="right">195,406</td>
<td align="right">31.6%</td>
<td align="right">8,753</td>
<td align="right">5.5%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">28,685</td>
<td align="right">4.6%</td>
<td align="right">3,864</td>
<td align="right">2.4%</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">121,418</td>
<td align="right">19.6%</td>
<td align="right">24,070</td>
<td align="right">15.2%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">199,971</td>
<td align="right">32.3%</td>
<td align="right">61,061</td>
<td align="right">38.5%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1,013</td>
<td align="right">0.2%</td>
<td align="right">769</td>
<td align="right">0.5%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">52,740</td>
<td align="right">8.5%</td>
<td align="right">40,666</td>
<td align="right">25.6%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,488</td>
<td align="right">2.0%</td>
<td align="right">12,484</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,789</td>
<td align="right">0.6%</td>
<td align="right">3,789</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">0.5%</td>
<td align="right">2,941</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">348</td>
<td align="right">0.1%</td>
<td align="right">348</td>
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,397,618,813</td>
<td align="right">96.9%</td>
<td align="right">4,553,670,514</td>
<td align="right">93.1%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">183,644,008</td>
<td align="right">1.6%</td>
<td align="right">156,475,263</td>
<td align="right">3.2%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">183,280,081</td>
<td align="right">1.6%</td>
<td align="right">183,278,419</td>
<td align="right">3.7%</td>
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
<td align="right">3,634,781</td>
<td align="right">98.5%</td>
<td align="right">3,124,685</td>
<td align="right">98.3%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">55,045</td>
<td align="right">1.5%</td>
<td align="right">55,021</td>
<td align="right">1.7%</td>
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
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">0.5%</td>
<td align="right">287</td>
<td align="right">0.5%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">54,599</td>
<td align="right">99.2%</td>
<td align="right">54,575</td>
<td align="right">99.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">55,165</td>
<td align="right">100.2%</td>
<td align="right">55,141</td>
<td align="right">100.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">1.4%</td>
<td align="right">752</td>
<td align="right">1.4%</td>
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
<td align="right">111,572</td>
<td align="right">15.8%</td>
<td align="right">111,570</td>
<td align="right">15.8%</td>
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
<td align="right">584,207</td>
<td align="right">82.9%</td>
<td align="right">584,207</td>
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
<td align="right">20,068</td>
<td align="right">99.4%</td>
<td align="right">20,169</td>
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
<td align="right">543,979,647</td>
<td align="right">10.6%</td>
<td align="right">107,470,381</td>
<td align="right">9.2%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,584,385,780</td>
<td align="right">89.4%</td>
<td align="right">1,053,004,755</td>
<td align="right">90.6%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,688,395</td>
<td align="right">0.0%</td>
<td align="right">1,539,235</td>
<td align="right">0.1%</td>
<td align="right">-8.8%</td>
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
<td align="right">242,813</td>
<td align="right">83.1%</td>
<td align="right">132,759</td>
<td align="right">73.9%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">49,510</td>
<td align="right">16.9%</td>
<td align="right">46,993</td>
<td align="right">26.1%</td>
<td align="right">-5.1%</td>
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
<td align="right">91,405</td>
<td align="right">37.6%</td>
<td align="right">5,090</td>
<td align="right">3.8%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,862</td>
<td align="right">2.8%</td>
<td align="right">402</td>
<td align="right">0.3%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,110</td>
<td align="right">0.9%</td>
<td align="right">1,046</td>
<td align="right">0.8%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,496</td>
<td align="right">6.0%</td>
<td align="right">7,322</td>
<td align="right">5.5%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">15,226</td>
<td align="right">6.3%</td>
<td align="right">9,702</td>
<td align="right">7.3%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,221</td>
<td align="right">0.9%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.1%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">51,386</td>
<td align="right">21.2%</td>
<td align="right">49,488</td>
<td align="right">37.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40,141</td>
<td align="right">16.5%</td>
<td align="right">38,791</td>
<td align="right">29.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,748</td>
<td align="right">0.7%</td>
<td align="right">1,728</td>
<td align="right">1.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,077</td>
<td align="right">4.2%</td>
<td align="right">9,996</td>
<td align="right">7.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.1%</td>
<td align="right">7,639</td>
<td align="right">5.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,213,989,699</td>
<td align="right">92.3%</td>
<td align="right">335,514,375</td>
<td align="right">83.2%</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">183,389,604</td>
<td align="right">7.6%</td>
<td align="right">65,612,694</td>
<td align="right">16.3%</td>
<td align="right">-64.2%</td>
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
<td align="right">0.5%</td>
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
<td align="right">71,606</td>
<td align="right">65.2%</td>
<td align="right">42,959</td>
<td align="right">52.8%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,235</td>
<td align="right">34.8%</td>
<td align="right">38,435</td>
<td align="right">47.2%</td>
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
<td align="right">24,776</td>
<td align="right">34.6%</td>
<td align="right">10,775</td>
<td align="right">25.1%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">16,096</td>
<td align="right">22.5%</td>
<td align="right">7,269</td>
<td align="right">16.9%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,788</td>
<td align="right">20.7%</td>
<td align="right">9,428</td>
<td align="right">21.9%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">15,946</td>
<td align="right">22.3%</td>
<td align="right">15,487</td>
<td align="right">36.1%</td>
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
<td align="right">1,498,056,241</td>
<td align="right">28.8%</td>
<td align="right">137,884,842</td>
<td align="right">18.6%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,546,439,609</td>
<td align="right">68.1%</td>
<td align="right">571,143,753</td>
<td align="right">76.9%</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">165,467,486</td>
<td align="right">3.2%</td>
<td align="right">33,296,244</td>
<td align="right">4.5%</td>
<td align="right">-79.9%</td>
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
<td align="right">3,126,922</td>
<td align="right">87.6%</td>
<td align="right">633,165</td>
<td align="right">85.5%</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">443,131</td>
<td align="right">12.4%</td>
<td align="right">107,351</td>
<td align="right">14.5%</td>
<td align="right">-75.8%</td>
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
<td align="right">175,001</td>
<td align="right">39.5%</td>
<td align="right">6,492</td>
<td align="right">6.0%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">84,548</td>
<td align="right">19.1%</td>
<td align="right">3,584</td>
<td align="right">3.3%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,365</td>
<td align="right">2.6%</td>
<td align="right">2,287</td>
<td align="right">2.1%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">37,667</td>
<td align="right">8.5%</td>
<td align="right">8,510</td>
<td align="right">7.9%</td>
<td align="right">-77.4%</td>
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
<td align="left">seq iter</td>
<td align="right">14,961</td>
<td align="right">3.4%</td>
<td align="right">4,163</td>
<td align="right">3.9%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">1,547</td>
<td align="right">1.4%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,368</td>
<td align="right">1.0%</td>
<td align="right">2,494</td>
<td align="right">2.3%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,302</td>
<td align="right">5.5%</td>
<td align="right">15,463</td>
<td align="right">14.4%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">5,319</td>
<td align="right">1.2%</td>
<td align="right">3,585</td>
<td align="right">3.3%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,188</td>
<td align="right">1.6%</td>
<td align="right">5,143</td>
<td align="right">4.8%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">72,891</td>
<td align="right">16.4%</td>
<td align="right">53,448</td>
<td align="right">49.8%</td>
<td align="right">-26.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,756,085,624</td>
<td align="right">88.0%</td>
<td align="right">5,728,759,280</td>
<td align="right">82.7%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">802,915,209</td>
<td align="right">5.5%</td>
<td align="right">499,526,298</td>
<td align="right">7.2%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">931,523,513</td>
<td align="right">6.4%</td>
<td align="right">700,272,181</td>
<td align="right">10.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,406,846</td>
<td align="right">0.0%</td>
<td align="right">1,406,846</td>
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
<td align="right">17,655,504</td>
<td align="right">98.3%</td>
<td align="right">13,298,076</td>
<td align="right">98.3%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">309,503</td>
<td align="right">1.7%</td>
<td align="right">234,996</td>
<td align="right">1.7%</td>
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
<td align="left">method</td>
<td align="right">84,181</td>
<td align="right">27.2%</td>
<td align="right">43,735</td>
<td align="right">18.6%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">61,499</td>
<td align="right">19.9%</td>
<td align="right">41,751</td>
<td align="right">17.8%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,180</td>
<td align="right">0.4%</td>
<td align="right">858</td>
<td align="right">0.4%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,308</td>
<td align="right">2.4%</td>
<td align="right">6,107</td>
<td align="right">2.6%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">19,415</td>
<td align="right">6.3%</td>
<td align="right">16,643</td>
<td align="right">7.1%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,317</td>
<td align="right">3.0%</td>
<td align="right">8,139</td>
<td align="right">3.5%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.9%</td>
<td align="right">2,407</td>
<td align="right">1.0%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">68,411</td>
<td align="right">22.1%</td>
<td align="right">62,253</td>
<td align="right">26.5%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,960</td>
<td align="right">0.6%</td>
<td align="right">1,786</td>
<td align="right">0.8%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,360</td>
<td align="right">8.2%</td>
<td align="right">23,957</td>
<td align="right">10.2%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2,490</td>
<td align="right">0.8%</td>
<td align="right">2,486</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,230</td>
<td align="right">0.4%</td>
<td align="right">1,229</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,625</td>
<td align="right">2.5%</td>
<td align="right">7,625</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">5,005</td>
<td align="right">1.6%</td>
<td align="right">5,005</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.4%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
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
<td align="right">151</td>
<td align="right">0.0%</td>
<td align="right">151</td>
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
<td align="right">9,672,557,087</td>
<td align="right">99.8%</td>
<td align="right">4,171,575,089</td>
<td align="right">99.6%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,830</td>
<td align="right">0.0%</td>
<td align="right">53,238</td>
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
<td align="right">14,622,740</td>
<td align="right">0.2%</td>
<td align="right">14,622,704</td>
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
<td align="right">1,854</td>
<td align="right">0.0%</td>
<td align="right">1,854</td>
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
<td align="right">136,558</td>
<td align="right">100.0%</td>
<td align="right">138,475</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">110,237,274</td>
<td align="right">100.0%</td>
<td align="right">109,007,054</td>
<td align="right">100.0%</td>
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
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">593,529,698</td>
<td align="right">82.2%</td>
<td align="right">206,688,960</td>
<td align="right">61.6%</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,799</td>
<td align="right">17.8%</td>
<td align="right">128,815,799</td>
<td align="right">38.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,151,121,538</td>
<td align="right">88.1%</td>
<td align="right">1,560,742,708</td>
<td align="right">84.7%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">86,393,708</td>
<td align="right">3.5%</td>
<td align="right">78,967,719</td>
<td align="right">4.3%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">203,715,240</td>
<td align="right">8.3%</td>
<td align="right">203,032,586</td>
<td align="right">11.0%</td>
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
<td align="right">63,047</td>
<td align="right">1.1%</td>
<td align="right">61,228</td>
<td align="right">1.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,743,659</td>
<td align="right">98.9%</td>
<td align="right">5,733,844</td>
<td align="right">98.9%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">6,033</td>
<td align="right">9.6%</td>
<td align="right">4,954</td>
<td align="right">8.1%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.2%</td>
<td align="right">699</td>
<td align="right">1.1%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,562</td>
<td align="right">8.8%</td>
<td align="right">5,318</td>
<td align="right">8.7%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,894</td>
<td align="right">4.6%</td>
<td align="right">2,848</td>
<td align="right">4.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">27,914</td>
<td align="right">44.3%</td>
<td align="right">27,514</td>
<td align="right">44.9%</td>
<td align="right">-1.4%</td>
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
<td align="right">5.3%</td>
<td align="right">3,350</td>
<td align="right">5.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,932</td>
<td align="right">3.1%</td>
<td align="right">1,933</td>
<td align="right">3.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">11,722</td>
<td align="right">18.6%</td>
<td align="right">11,722</td>
<td align="right">19.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,061</td>
<td align="right">1.7%</td>
<td align="right">1,061</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">889</td>
<td align="right">1.4%</td>
<td align="right">889</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.2%</td>
<td align="right">730</td>
<td align="right">1.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">926,606,352</td>
<td align="right">56.9%</td>
<td align="right">170,537,243</td>
<td align="right">55.8%</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">702,521,554</td>
<td align="right">43.1%</td>
<td align="right">135,215,303</td>
<td align="right">44.2%</td>
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
<td align="right">183,166</td>
<td align="right">98.9%</td>
<td align="right">44,642</td>
<td align="right">95.3%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,076</td>
<td align="right">1.1%</td>
<td align="right">2,197</td>
<td align="right">4.7%</td>
<td align="right">5.8%</td>
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
<td align="right">47.3%</td>
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
<td align="right">26.7%</td>
<td align="right">8,142</td>
<td align="right">18.2%</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,916</td>
<td align="right">1.0%</td>
<td align="right">735</td>
<td align="right">1.6%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,936</td>
<td align="right">10.9%</td>
<td align="right">15,347</td>
<td align="right">34.4%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">16,703</td>
<td align="right">37.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,070</td>
<td align="right">1.7%</td>
<td align="right">3,070</td>
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
<td align="right">115,534,647</td>
<td align="right">2.1%</td>
<td align="right">42,664,193</td>
<td align="right">1.6%</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">276,328,284</td>
<td align="right">5.1%</td>
<td align="right">109,952,819</td>
<td align="right">4.1%</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,004,507,964</td>
<td align="right">92.7%</td>
<td align="right">2,519,564,925</td>
<td align="right">94.3%</td>
<td align="right">-49.7%</td>
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
<td align="right">2,227,737</td>
<td align="right">77.3%</td>
<td align="right">853,451</td>
<td align="right">66.2%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">652,742</td>
<td align="right">22.7%</td>
<td align="right">435,029</td>
<td align="right">33.8%</td>
<td align="right">-33.4%</td>
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
<td align="right">78,593</td>
<td align="right">12.0%</td>
<td align="right">9,551</td>
<td align="right">2.2%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">134,976</td>
<td align="right">20.7%</td>
<td align="right">18,382</td>
<td align="right">4.2%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,921</td>
<td align="right">2.9%</td>
<td align="right">4,540</td>
<td align="right">1.0%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,075</td>
<td align="right">1.5%</td>
<td align="right">5,691</td>
<td align="right">1.3%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">22,259</td>
<td align="right">3.4%</td>
<td align="right">14,935</td>
<td align="right">3.4%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">14,295</td>
<td align="right">2.2%</td>
<td align="right">13,341</td>
<td align="right">3.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">105,158</td>
<td align="right">16.1%</td>
<td align="right">100,836</td>
<td align="right">23.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">266,623</td>
<td align="right">40.8%</td>
<td align="right">265,911</td>
<td align="right">61.1%</td>
<td align="right">-0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,269,178,824</td>
<td align="right">99.9%</td>
<td align="right">406,136,892</td>
<td align="right">99.6%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,862,528</td>
<td align="right">0.1%</td>
<td align="right">1,473,755</td>
<td align="right">0.4%</td>
<td align="right">-20.9%</td>
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
<td align="right">1,272</td>
<td align="right">9.9%</td>
<td align="right">1,141</td>
<td align="right">8.9%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,573</td>
<td align="right">90.1%</td>
<td align="right">11,641</td>
<td align="right">91.1%</td>
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
<td align="right">887</td>
<td align="right">69.7%</td>
<td align="right">756</td>
<td align="right">66.3%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">255</td>
<td align="right">20.0%</td>
<td align="right">255</td>
<td align="right">22.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">130</td>
<td align="right">10.2%</td>
<td align="right">130</td>
<td align="right">11.4%</td>
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
<td align="right">8,185,377,628</td>
<td align="right">3.8%</td>
<td align="right">2,396,073,808</td>
<td align="right">2.8%</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">82,190,090,899</td>
<td align="right">37.9%</td>
<td align="right">31,674,061,100</td>
<td align="right">37.6%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">125,076,190,265</td>
<td align="right">57.6%</td>
<td align="right">49,056,772,942</td>
<td align="right">58.2%</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,648,195,887</td>
<td align="right">0.8%</td>
<td align="right">1,166,312,344</td>
<td align="right">1.4%</td>
<td align="right">-29.2%</td>
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
<td align="right">1,498,056,241</td>
<td align="right">18.3%</td>
<td align="right">137,884,842</td>
<td align="right">5.8%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">702,521,554</td>
<td align="right">8.6%</td>
<td align="right">135,215,303</td>
<td align="right">5.7%</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">543,979,647</td>
<td align="right">6.7%</td>
<td align="right">107,470,381</td>
<td align="right">4.5%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,380,726,896</td>
<td align="right">29.1%</td>
<td align="right">500,124,249</td>
<td align="right">20.9%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,081,441,478</td>
<td align="right">13.2%</td>
<td align="right">329,866,772</td>
<td align="right">13.8%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">276,328,284</td>
<td align="right">3.4%</td>
<td align="right">109,952,819</td>
<td align="right">4.6%</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,421,333</td>
<td align="right">2.2%</td>
<td align="right">97,908,478</td>
<td align="right">4.1%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">802,915,209</td>
<td align="right">9.8%</td>
<td align="right">499,526,298</td>
<td align="right">20.9%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">183,280,081</td>
<td align="right">2.2%</td>
<td align="right">183,278,419</td>
<td align="right">7.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">183,389,604</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">128,815,799</td>
<td align="right">5.4%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,388,645</td>
<td align="right">3.4%</td>
<td align="right">19,705,569</td>
<td align="right">1.7%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">291,001,387</td>
<td align="right">17.7%</td>
<td align="right">204,627,159</td>
<td align="right">17.5%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">391,442,055</td>
<td align="right">23.7%</td>
<td align="right">276,682,153</td>
<td align="right">23.7%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">93,166,517</td>
<td align="right">5.7%</td>
<td align="right">78,649,299</td>
<td align="right">6.7%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">105,018,357</td>
<td align="right">6.4%</td>
<td align="right">91,822,812</td>
<td align="right">7.9%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,192,844</td>
<td align="right">5.2%</td>
<td align="right">75,030,576</td>
<td align="right">6.4%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">107,185,314</td>
<td align="right">6.5%</td>
<td align="right">106,508,034</td>
<td align="right">9.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">96,480,631</td>
<td align="right">5.9%</td>
<td align="right">96,475,257</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,756,971</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">82,625,466</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">22,794,676</td>
<td align="right">2.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21,063,228</td>
<td align="right">1.8%</td>
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
<td align="right">4,273,445</td>
<td align="right">0.1%</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,248,558,337</td>
<td align="right">73.8%</td>
<td align="right">5,140,763,521</td>
<td align="right">73.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,665,144,392</td>
<td align="right">79.7%</td>
<td align="right">5,581,289,935</td>
<td align="right">79.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">689,755,015</td>
<td align="right">9.7%</td>
<td align="right">681,200,677</td>
<td align="right">9.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,863,605,488</td>
<td align="right">26.2%</td>
<td align="right">1,848,966,548</td>
<td align="right">26.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,863,605,488</td>
<td align="right">26.2%</td>
<td align="right">1,848,966,548</td>
<td align="right">26.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,173,850,473</td>
<td align="right">16.5%</td>
<td align="right">1,167,765,871</td>
<td align="right">16.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">296,145,719</td>
<td align="right">4.2%</td>
<td align="right">294,746,492</td>
<td align="right">4.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">72,255,933</td>
<td align="right">1.0%</td>
<td align="right">72,564,819</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,169,573,132</td>
<td align="right">16.4%</td>
<td align="right">1,165,633,725</td>
<td align="right">16.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">265,400,619</td>
<td align="right">3.7%</td>
<td align="right">265,392,800</td>
<td align="right">3.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,738,489</td>
<td align="right">0.4%</td>
<td align="right">25,738,264</td>
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
<td align="right">1.9%</td>
<td align="right">132,513,139</td>
<td align="right">1.9%</td>
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
<td align="right">22,194,124</td>
<td align="right"></td>
<td align="right">12,653,839</td>
<td align="right"></td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">98,497,287</td>
<td align="right"></td>
<td align="right">73,784,955</td>
<td align="right"></td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">88,295,606</td>
<td align="right"></td>
<td align="right">73,123,308</td>
<td align="right"></td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">83,350,727,092</td>
<td align="right">50.8%</td>
<td align="right">89,195,292,884</td>
<td align="right">53.3%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">28,288,186,275</td>
<td align="right">17.2%</td>
<td align="right">26,359,055,588</td>
<td align="right">15.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">92,993,317,420</td>
<td align="right">46.5%</td>
<td align="right">98,322,837,214</td>
<td align="right">47.6%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,401,015,431</td>
<td align="right"></td>
<td align="right">2,291,048,006</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">46,360,965,903</td>
<td align="right">23.2%</td>
<td align="right">48,129,093,789</td>
<td align="right">23.3%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">187,359,101</td>
<td align="right"></td>
<td align="right">182,534,689</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,925,962,302</td>
<td align="right"></td>
<td align="right">10,764,932,752</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,925,784,652</td>
<td align="right">57.3%</td>
<td align="right">10,764,759,431</td>
<td align="right">57.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">25,132,303,693</td>
<td align="right">15.3%</td>
<td align="right">24,802,425,101</td>
<td align="right">14.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">27,252,377,825</td>
<td align="right">16.6%</td>
<td align="right">26,905,195,328</td>
<td align="right">16.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,315,921,404</td>
<td align="right">12.7%</td>
<td align="right">25,074,110,541</td>
<td align="right">12.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">8,066,852,094</td>
<td align="right">42.3%</td>
<td align="right">8,013,587,225</td>
<td align="right">42.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">8,145,549,381</td>
<td align="right">42.7%</td>
<td align="right">8,092,226,557</td>
<td align="right">42.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">8,713,405,529</td>
<td align="right"></td>
<td align="right">8,657,572,574</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">72,145,612</td>
<td align="right">0.4%</td>
<td align="right">72,088,850</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">35,268,005,376</td>
<td align="right">17.6%</td>
<td align="right">35,244,822,784</td>
<td align="right">17.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,551,675</td>
<td align="right">0.0%</td>
<td align="right">6,550,482</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,217,895,904</td>
<td align="right"></td>
<td align="right">3,218,228,619</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,390</td>
<td align="right">2.4%</td>
<td align="right">4,444,390</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,375</td>
<td align="right">0.3%</td>
<td align="right">476,375</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,884</td>
<td align="right">0.0%</td>
<td align="right">4,884</td>
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
<td align="right">364,946</td>
<td align="right">104,167,343</td>
<td align="right">9,980,321,545</td>
<td align="right">783,896,539</td>
<td align="right">785,887,858</td>
<td align="right">364,003</td>
<td align="right">103,853,906</td>
<td align="right">9,994,701,398</td>
<td align="right">786,094,628</td>
<td align="right">785,637,956</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,600,574,956</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,601,141,114</td>
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
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">2,496</td>
<td align="right">2,496</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-12-15
