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
<td align="right">1,315,340</td>
<td align="right">723,975</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,349,805</td>
<td align="right">928,605</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">57,327,364</td>
<td align="right">47,130,975</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">449,939,615</td>
<td align="right">387,307,480</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">124,153,260</td>
<td align="right">108,609,253</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,265,188</td>
<td align="right">1,111,899</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">207,957,783</td>
<td align="right">184,956,718</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,807,102</td>
<td align="right">2,498,598</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">209,837,953</td>
<td align="right">187,403,831</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">164,689,544</td>
<td align="right">147,225,399</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,354,001</td>
<td align="right">3,002,295</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220,246,698</td>
<td align="right">199,439,052</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,571,619</td>
<td align="right">25,279,199</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">114,350,367</td>
<td align="right">123,843,348</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">14,297,526</td>
<td align="right">13,129,858</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">178,177,806</td>
<td align="right">163,915,346</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,653,286</td>
<td align="right">89,194,419</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,090,483,630</td>
<td align="right">1,007,588,015</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">111,699,135</td>
<td align="right">103,383,799</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">77,863,075</td>
<td align="right">72,422,557</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,070,159</td>
<td align="right">34,500,999</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">21,535,496</td>
<td align="right">22,991,086</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,311,927</td>
<td align="right">88,552,839</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,099,922,867</td>
<td align="right">1,033,575,078</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,840,180</td>
<td align="right">2,678,920</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,075,598</td>
<td align="right">54,951,498</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">182,621,912</td>
<td align="right">172,557,088</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,880,262</td>
<td align="right">64,101,020</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">148,537,414</td>
<td align="right">141,037,051</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">163,945,034</td>
<td align="right">155,880,968</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">624,059,745</td>
<td align="right">593,834,756</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">220,719,607</td>
<td align="right">210,123,995</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">42,025,370</td>
<td align="right">40,082,278</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,035,674,002</td>
<td align="right">1,945,254,504</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">878,207,320</td>
<td align="right">839,468,498</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">274,430,759</td>
<td align="right">262,364,623</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">127,900,098</td>
<td align="right">122,460,250</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,163,960</td>
<td align="right">10,701,124</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,871,386</td>
<td align="right">92,889,062</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">709,897,881</td>
<td align="right">681,613,424</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">424,197,537</td>
<td align="right">408,963,248</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">42,727,340</td>
<td align="right">41,203,526</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">119,116,381</td>
<td align="right">115,006,327</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">137,139,376</td>
<td align="right">132,497,710</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,734,678</td>
<td align="right">48,052,067</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,562,154</td>
<td align="right">102,025,164</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">383,888,736</td>
<td align="right">371,298,661</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,217,724</td>
<td align="right">154,092,822</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">907,099,296</td>
<td align="right">877,959,988</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">373,881,548</td>
<td align="right">362,085,950</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">467,975,397</td>
<td align="right">453,289,067</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,001,033</td>
<td align="right">25,190,271</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,408,781</td>
<td align="right">457,944,354</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,245,700</td>
<td align="right">6,061,380</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,504,350</td>
<td align="right">542,433,227</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,516,861</td>
<td align="right">4,389,491</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">134,670,752</td>
<td align="right">130,913,323</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">957,654,786</td>
<td align="right">931,878,384</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">352,815,775</td>
<td align="right">343,369,671</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,544,932</td>
<td align="right">5,396,787</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,387,660</td>
<td align="right">18,883,294</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">126,964,760</td>
<td align="right">130,161,920</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">462,070,383</td>
<td align="right">473,701,866</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">852,853,951</td>
<td align="right">873,563,554</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,560,932</td>
<td align="right">9,333,499</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">369,954,636</td>
<td align="right">362,483,495</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,278,437</td>
<td align="right">47,340,762</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,729,160</td>
<td align="right">9,545,216</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">173,731,396</td>
<td align="right">170,505,435</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">207,570,809</td>
<td align="right">203,728,395</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,877,728,302</td>
<td align="right">16,565,707,396</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,745,426,082</td>
<td align="right">3,677,443,672</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">37,576,131</td>
<td align="right">36,896,380</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">910,283,530</td>
<td align="right">894,052,617</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,958,212</td>
<td align="right">260,334,381</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">168,432,590</td>
<td align="right">165,588,100</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">256,775,015</td>
<td align="right">252,863,805</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">55,469,573</td>
<td align="right">54,635,523</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,338,476,900</td>
<td align="right">2,371,612,899</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">52,652,481</td>
<td align="right">51,911,142</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,088,363,503</td>
<td align="right">5,017,175,653</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">69,035,271</td>
<td align="right">68,075,126</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">431,759,287</td>
<td align="right">425,836,416</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">346,654,349</td>
<td align="right">341,908,269</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">924,067,033</td>
<td align="right">911,738,318</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">919,629,220</td>
<td align="right">907,360,592</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,387,602,242</td>
<td align="right">3,343,090,212</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">115,592,511</td>
<td align="right">114,209,430</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">561,252,265</td>
<td align="right">554,645,999</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">279,175,484</td>
<td align="right">275,951,318</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">508,784,561</td>
<td align="right">503,238,428</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,747,882</td>
<td align="right">244,060,783</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,013,031</td>
<td align="right">257,786,833</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">297,390,974</td>
<td align="right">294,174,036</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,041,508</td>
<td align="right">30,714,635</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">179,363,972</td>
<td align="right">177,518,146</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">124,871,671</td>
<td align="right">123,611,115</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">184,321,670</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">927,739,606</td>
<td align="right">918,808,043</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,154,551,351</td>
<td align="right">4,117,894,488</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">77,451,619</td>
<td align="right">76,778,534</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,417,966</td>
<td align="right">280,958,677</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,739,597</td>
<td align="right">61,211,692</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">112,289,889</td>
<td align="right">111,363,501</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">658,003,425</td>
<td align="right">652,614,877</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">71,659,486</td>
<td align="right">71,100,588</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,049,994,079</td>
<td align="right">2,034,077,902</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">64,309,172</td>
<td align="right">63,812,789</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">292,970,077</td>
<td align="right">294,961,572</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">281,033,223</td>
<td align="right">279,170,035</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">811,093,912</td>
<td align="right">806,241,467</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,470,442</td>
<td align="right">81,023,955</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,191,708,326</td>
<td align="right">4,168,970,833</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">672,358,104</td>
<td align="right">675,870,555</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,445,686</td>
<td align="right">41,246,900</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">197,567,460</td>
<td align="right">196,690,394</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,446,284</td>
<td align="right">119,941,918</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,115,545</td>
<td align="right">74,802,723</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">621,768,803</td>
<td align="right">619,259,211</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,308,077</td>
<td align="right">70,055,068</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,664,671,264</td>
<td align="right">2,655,951,996</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,529,308,299</td>
<td align="right">1,534,177,102</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,283,939</td>
<td align="right">85,021,408</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,715,231</td>
<td align="right">10,682,743</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,713,139,684</td>
<td align="right">4,698,882,458</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,145,807</td>
<td align="right">70,942,259</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">368,501,623</td>
<td align="right">367,564,279</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">141,371,283</td>
<td align="right">141,047,595</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,531,045,079</td>
<td align="right">2,535,712,957</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">384,319,805</td>
<td align="right">383,614,624</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">833,067,438</td>
<td align="right">831,619,812</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,055,566,867</td>
<td align="right">5,048,338,959</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,599,289</td>
<td align="right">190,405,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">262,522,015</td>
<td align="right">262,281,488</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">372,813,493</td>
<td align="right">373,130,798</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,136,625,291</td>
<td align="right">1,137,442,727</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,023,632,559</td>
<td align="right">2,022,240,549</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,512,998</td>
<td align="right">68,482,415</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,184,173</td>
<td align="right">124,219,090</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,833,463</td>
<td align="right">69,814,006</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,439,741</td>
<td align="right">28,434,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,081</td>
<td align="right">92,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,164</td>
<td align="right">560,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,147,679</td>
<td align="right">21,146,649</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,423,284</td>
<td align="right">21,422,254</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,423,305</td>
<td align="right">21,422,275</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,401</td>
<td align="right">3,100,313</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">323,893</td>
<td align="right">323,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,680,537</td>
<td align="right">6,680,413</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,523,652</td>
<td align="right">13,523,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">333,541</td>
<td align="right">333,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,127,556</td>
<td align="right">332,124,971</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,576,539</td>
<td align="right">1,576,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,682,739</td>
<td align="right">114,682,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,450,765</td>
<td align="right">3,450,754</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">241,369,152</td>
<td align="right">241,368,408</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">243,419,240</td>
<td align="right">243,418,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,279,017</td>
<td align="right">6,279,001</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,925,954</td>
<td align="right">35,926,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,107,626,231</td>
<td align="right">1,107,624,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,619,526</td>
<td align="right">15,619,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,540,620,411</td>
<td align="right">1,540,621,742</td>
<td align="right">0.0%</td>
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
<td align="right">418,705,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,462,202</td>
<td align="right">591,462,289</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,078,481</td>
<td align="right">155,078,487</td>
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
<td align="right">2,332,004</td>
<td align="right">2,332,004</td>
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
<td align="left">CALL_KW</td>
<td align="right">106,196</td>
<td align="right">106,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">78,915</td>
<td align="right">78,915</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,158</td>
<td align="right">14,158</td>
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
<td align="right">1,006,830,931</td>
<td align="right">5.8%</td>
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
<td align="right">65,513,558</td>
<td align="right">0.4%</td>
<td align="right">69,303,171</td>
<td align="right">0.4%</td>
<td align="right">5.8%</td>
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
<td align="right">16,135,818,350</td>
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
<td align="right">599,783</td>
<td align="right">29.1%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,391,549</td>
<td align="right">68.0%</td>
<td align="right">1,463,024</td>
<td align="right">70.9%</td>
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
<td align="left">xor int</td>
<td align="right">25,123</td>
<td align="right">3.8%</td>
<td align="right">7,583</td>
<td align="right">1.3%</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,721</td>
<td align="right">4.5%</td>
<td align="right">9,002</td>
<td align="right">1.5%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,181</td>
<td align="right">2.3%</td>
<td align="right">12,402</td>
<td align="right">2.1%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">5,212</td>
<td align="right">0.8%</td>
<td align="right">4,372</td>
<td align="right">0.7%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">39,645</td>
<td align="right">6.1%</td>
<td align="right">36,348</td>
<td align="right">6.1%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">56,721</td>
<td align="right">8.7%</td>
<td align="right">52,089</td>
<td align="right">8.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,139</td>
<td align="right">2.3%</td>
<td align="right">14,374</td>
<td align="right">2.4%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">3,093</td>
<td align="right">0.5%</td>
<td align="right">2,951</td>
<td align="right">0.5%</td>
<td align="right">-4.6%</td>
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
<td align="left">true divide float</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">5,189</td>
<td align="right">0.9%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,464</td>
<td align="right">2.4%</td>
<td align="right">15,173</td>
<td align="right">2.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">33,181</td>
<td align="right">5.1%</td>
<td align="right">32,593</td>
<td align="right">5.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,784</td>
<td align="right">7.5%</td>
<td align="right">48,078</td>
<td align="right">8.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,119</td>
<td align="right">9.0%</td>
<td align="right">58,285</td>
<td align="right">9.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,417</td>
<td align="right">0.2%</td>
<td align="right">1,406</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">28,112</td>
<td align="right">4.3%</td>
<td align="right">27,903</td>
<td align="right">4.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,181</td>
<td align="right">0.8%</td>
<td align="right">5,148</td>
<td align="right">0.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">71,308</td>
<td align="right">10.9%</td>
<td align="right">70,957</td>
<td align="right">11.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">4,237</td>
<td align="right">0.6%</td>
<td align="right">4,217</td>
<td align="right">0.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">29,084</td>
<td align="right">4.4%</td>
<td align="right">29,000</td>
<td align="right">4.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,464</td>
<td align="right">1.3%</td>
<td align="right">8,443</td>
<td align="right">1.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,953</td>
<td align="right">1.7%</td>
<td align="right">10,933</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">16,575</td>
<td align="right">2.5%</td>
<td align="right">16,556</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
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
<td align="right">109,864</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
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
<td align="left">subscr mappingproxy</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">560</td>
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
<td align="right">184,321,670</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">167,540,527</td>
<td align="right">1.5%</td>
<td align="right">2.6%</td>
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
<td align="right">165,359,845</td>
<td align="right">1.5%</td>
<td align="right">2.6%</td>
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
<td align="right">10,943,884,647</td>
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
<td align="right">3,757,066</td>
<td align="right">100.0%</td>
<td align="right">2.2%</td>
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
<td align="right">685,040</td>
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
<td align="right">61,496</td>
<td align="right">100.0%</td>
<td align="right">61,494</td>
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
<td align="right">92,655,349</td>
<td align="right">2.0%</td>
<td align="right">-4.1%</td>
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
<td align="right">1,313,616</td>
<td align="right">0.0%</td>
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
<td align="right">4,500,056,897</td>
<td align="right">97.9%</td>
<td align="right">4,499,473,676</td>
<td align="right">97.9%</td>
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
<td align="right">168,385</td>
<td align="right">65.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">89,711</td>
<td align="right">34.6%</td>
<td align="right">89,642</td>
<td align="right">34.7%</td>
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
<td align="right">1,244</td>
<td align="right">0.7%</td>
<td align="right">1,203</td>
<td align="right">0.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">12,209</td>
<td align="right">7.2%</td>
<td align="right">11,946</td>
<td align="right">7.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">15,628</td>
<td align="right">9.2%</td>
<td align="right">15,440</td>
<td align="right">9.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,394</td>
<td align="right">7.3%</td>
<td align="right">12,271</td>
<td align="right">7.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,848</td>
<td align="right">1.7%</td>
<td align="right">2,826</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,339</td>
<td align="right">16.1%</td>
<td align="right">27,252</td>
<td align="right">16.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">8,883</td>
<td align="right">5.2%</td>
<td align="right">8,862</td>
<td align="right">5.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">62,979</td>
<td align="right">37.2%</td>
<td align="right">62,836</td>
<td align="right">37.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,251</td>
<td align="right">11.4%</td>
<td align="right">19,242</td>
<td align="right">11.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,151</td>
<td align="right">1.9%</td>
<td align="right">3,151</td>
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
<td align="right">88,434,302</td>
<td align="right">3.9%</td>
<td align="right">-6.1%</td>
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
<td align="right">2,177,556,349</td>
<td align="right">96.0%</td>
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
<td align="right">102,847</td>
<td align="right">74.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">35,271</td>
<td align="right">25.3%</td>
<td align="right">35,271</td>
<td align="right">25.5%</td>
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
<td align="right">17,721</td>
<td align="right">17.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">23,849</td>
<td align="right">22.9%</td>
<td align="right">23,449</td>
<td align="right">22.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">31,479</td>
<td align="right">30.2%</td>
<td align="right">30,953</td>
<td align="right">30.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,945</td>
<td align="right">29.7%</td>
<td align="right">30,724</td>
<td align="right">29.9%</td>
<td align="right">-0.7%</td>
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
<td align="right">199,181,318</td>
<td align="right">12.7%</td>
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
<td align="right">1,341,351,150</td>
<td align="right">82.6%</td>
<td align="right">1,302,150,434</td>
<td align="right">83.3%</td>
<td align="right">-2.9%</td>
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
<td align="right">61,663,195</td>
<td align="right">3.9%</td>
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
<td align="left">Failure</td>
<td align="right">207,398</td>
<td align="right">14.3%</td>
<td align="right">198,186</td>
<td align="right">13.9%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,241,392</td>
<td align="right">85.7%</td>
<td align="right">1,222,542</td>
<td align="right">86.1%</td>
<td align="right">-1.5%</td>
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
<td align="right">14,829</td>
<td align="right">7.2%</td>
<td align="right">11,857</td>
<td align="right">6.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">973</td>
<td align="right">0.5%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,496</td>
<td align="right">2.2%</td>
<td align="right">4,056</td>
<td align="right">2.0%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,646</td>
<td align="right">1.8%</td>
<td align="right">3,341</td>
<td align="right">1.7%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">18,890</td>
<td align="right">9.1%</td>
<td align="right">17,740</td>
<td align="right">9.0%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,042</td>
<td align="right">5.3%</td>
<td align="right">10,541</td>
<td align="right">5.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">10,336</td>
<td align="right">5.0%</td>
<td align="right">9,872</td>
<td align="right">5.0%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,675</td>
<td align="right">2.7%</td>
<td align="right">5,475</td>
<td align="right">2.8%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,577</td>
<td align="right">9.0%</td>
<td align="right">17,993</td>
<td align="right">9.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">17,570</td>
<td align="right">8.5%</td>
<td align="right">17,134</td>
<td align="right">8.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">78,599</td>
<td align="right">37.9%</td>
<td align="right">76,875</td>
<td align="right">38.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,926</td>
<td align="right">3.8%</td>
<td align="right">7,780</td>
<td align="right">3.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,829</td>
<td align="right">0.9%</td>
<td align="right">1,849</td>
<td align="right">0.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">11,401</td>
<td align="right">5.5%</td>
<td align="right">11,341</td>
<td align="right">5.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
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
<td align="left">tuple</td>
<td align="right">173,347,660</td>
<td align="right">173,347,660 / 0 !!</td>
<td align="right">173,110,716</td>
<td align="right">173,110,716 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,372,891</td>
<td align="right">12,372,891 / 0 !!</td>
<td align="right">12,357,527</td>
<td align="right">12,357,527 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,649,325</td>
<td align="right">5,649,325 / 0 !!</td>
<td align="right">5,647,424</td>
<td align="right">5,647,424 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,510,719</td>
<td align="right">305,510,719 / 0 !!</td>
<td align="right">305,506,700</td>
<td align="right">305,506,700 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,671,555</td>
<td align="right">101,671,555 / 0 !!</td>
<td align="right">101,671,372</td>
<td align="right">101,671,372 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,484,574</td>
<td align="right">116,484,574 / 0 !!</td>
<td align="right">116,484,783</td>
<td align="right">116,484,783 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,990,206</td>
<td align="right">336,990,206 / 0 !!</td>
<td align="right">336,989,836</td>
<td align="right">336,989,836 / 0 !!</td>
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
<td align="right">687,413,626</td>
<td align="right">6.0%</td>
<td align="right">6.4%</td>
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
<td align="right">539,739,462</td>
<td align="right">4.7%</td>
<td align="right">-2.9%</td>
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
<td align="right">10,241,895,361</td>
<td align="right">89.3%</td>
<td align="right">-0.8%</td>
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
<td align="right">13,577,396</td>
<td align="right">94.7%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">766,906</td>
<td align="right">5.7%</td>
<td align="right">764,582</td>
<td align="right">5.3%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">78,458</td>
<td align="right">10.2%</td>
<td align="right">76,461</td>
<td align="right">10.0%</td>
<td align="right">-2.5%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">41,197</td>
<td align="right">5.4%</td>
<td align="right">41,580</td>
<td align="right">5.4%</td>
<td align="right">0.9%</td>
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
<td align="left">method</td>
<td align="right">76,204</td>
<td align="right">9.9%</td>
<td align="right">75,730</td>
<td align="right">9.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">30,642</td>
<td align="right">4.0%</td>
<td align="right">30,720</td>
<td align="right">4.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,083</td>
<td align="right">2.0%</td>
<td align="right">15,047</td>
<td align="right">2.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,884</td>
<td align="right">18.1%</td>
<td align="right">138,668</td>
<td align="right">18.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">12,303</td>
<td align="right">1.6%</td>
<td align="right">12,287</td>
<td align="right">1.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,886</td>
<td align="right">2.9%</td>
<td align="right">21,886</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
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
<td align="left">not managed dict</td>
<td align="right">4,327</td>
<td align="right">0.6%</td>
<td align="right">4,327</td>
<td align="right">0.6%</td>
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
<td align="right">4,673,444,525</td>
<td align="right">99.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">15,099,006</td>
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
<td align="right">525,489</td>
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
<td align="right">67,201,443</td>
<td align="right">100.0%</td>
<td align="right">67,201,333</td>
<td align="right">100.0%</td>
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
<td align="right">6,988</td>
<td align="right">0.0%</td>
<td align="right">6,988</td>
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
<td align="right">591,434,868</td>
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
<td align="right">61,000,057</td>
<td align="right">3.1%</td>
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
<td align="right">121,306,811</td>
<td align="right">6.1%</td>
<td align="right">121,478,445</td>
<td align="right">6.1%</td>
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
<td align="right">1,812,242,980</td>
<td align="right">90.8%</td>
<td align="right">1,812,070,082</td>
<td align="right">90.8%</td>
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
<td align="right">101,541</td>
<td align="right">4.1%</td>
<td align="right">101,290</td>
<td align="right">4.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,395,070</td>
<td align="right">95.9%</td>
<td align="right">2,398,310</td>
<td align="right">95.9%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">8,313</td>
<td align="right">8.2%</td>
<td align="right">8,103</td>
<td align="right">8.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">7,974</td>
<td align="right">7.9%</td>
<td align="right">7,954</td>
<td align="right">7.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,627</td>
<td align="right">43.0%</td>
<td align="right">43,606</td>
<td align="right">43.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">310,943</td>
<td align="right">306.2%</td>
<td align="right">311,023</td>
<td align="right">307.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">14,124</td>
<td align="right">13.9%</td>
<td align="right">14,124</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
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
<td align="right">3.0%</td>
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
<td align="right">928,605</td>
<td align="right">100.0%</td>
<td align="right">-31.2%</td>
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
<td align="right">101,930,915</td>
<td align="right">10.0%</td>
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
<td align="right">914,511,045</td>
<td align="right">89.7%</td>
<td align="right">914,498,287</td>
<td align="right">90.0%</td>
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
<td align="right">79,083</td>
<td align="right">83.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">16.0%</td>
<td align="right">15,206</td>
<td align="right">16.1%</td>
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
<td align="right">766</td>
<td align="right">1.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">2,282</td>
<td align="right">2.9%</td>
<td align="right">2,100</td>
<td align="right">2.7%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">7,609</td>
<td align="right">9.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,174</td>
<td align="right">20.2%</td>
<td align="right">15,839</td>
<td align="right">20.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,076</td>
<td align="right">56.4%</td>
<td align="right">45,076</td>
<td align="right">57.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
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
<tr>
<td align="left">array slice</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">168</td>
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
<td align="right">136,350,544</td>
<td align="right">3.1%</td>
<td align="right">131,765,211</td>
<td align="right">3.0%</td>
<td align="right">-3.4%</td>
</tr>
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
<td align="right">70,397,031</td>
<td align="right">1.6%</td>
<td align="right">-1.7%</td>
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
<td align="right">4,202,790,856</td>
<td align="right">95.4%</td>
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
<td align="right">564,865</td>
<td align="right">26.5%</td>
<td align="right">508,540</td>
<td align="right">24.7%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,569,587</td>
<td align="right">73.5%</td>
<td align="right">1,546,478</td>
<td align="right">75.3%</td>
<td align="right">-1.5%</td>
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
<td align="right">80,050</td>
<td align="right">14.2%</td>
<td align="right">24,432</td>
<td align="right">4.8%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">6,816</td>
<td align="right">1.2%</td>
<td align="right">6,316</td>
<td align="right">1.2%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,602</td>
<td align="right">2.1%</td>
<td align="right">11,559</td>
<td align="right">2.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">18,579</td>
<td align="right">3.3%</td>
<td align="right">18,539</td>
<td align="right">3.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">86,823</td>
<td align="right">15.4%</td>
<td align="right">86,679</td>
<td align="right">17.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">81,561</td>
<td align="right">14.4%</td>
<td align="right">81,581</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,930</td>
<td align="right">3.5%</td>
<td align="right">19,926</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,442</td>
<td align="right">45.6%</td>
<td align="right">257,446</td>
<td align="right">50.6%</td>
<td align="right">0.0%</td>
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
<td align="right">684,507</td>
<td align="right">0.1%</td>
<td align="right">-46.3%</td>
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
<td align="right">1,240,839,871</td>
<td align="right">99.9%</td>
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
<td align="right">2,307</td>
<td align="right">5.8%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,197</td>
<td align="right">93.8%</td>
<td align="right">37,201</td>
<td align="right">94.2%</td>
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
<td align="right">1,779</td>
<td align="right">71.9%</td>
<td align="right">1,613</td>
<td align="right">69.9%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">15.3%</td>
<td align="right">378</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">316</td>
<td align="right">12.8%</td>
<td align="right">316</td>
<td align="right">13.7%</td>
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
<td align="right">3,257,946,368</td>
<td align="right">3.2%</td>
<td align="right">3,113,884,011</td>
<td align="right">3.1%</td>
<td align="right">-4.4%</td>
</tr>
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
<td align="right">1,181,294,763</td>
<td align="right">1.2%</td>
<td align="right">4.2%</td>
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
<td align="right">35,839,182,450</td>
<td align="right">36.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">59,380,362,438</td>
<td align="right">59.7%</td>
<td align="right">-1.2%</td>
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
<td align="right">199,181,318</td>
<td align="right">7.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,089,672,394</td>
<td align="right">38.2%</td>
<td align="right">1,006,830,931</td>
<td align="right">37.0%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,191,901</td>
<td align="right">3.3%</td>
<td align="right">88,434,302</td>
<td align="right">3.3%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,636,766</td>
<td align="right">3.4%</td>
<td align="right">92,655,349</td>
<td align="right">3.4%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">136,350,544</td>
<td align="right">4.8%</td>
<td align="right">131,765,211</td>
<td align="right">4.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,467,002</td>
<td align="right">3.7%</td>
<td align="right">101,930,915</td>
<td align="right">3.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">555,790,065</td>
<td align="right">19.5%</td>
<td align="right">539,739,462</td>
<td align="right">19.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">161,190,588</td>
<td align="right">5.7%</td>
<td align="right">165,359,845</td>
<td align="right">6.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">6.4%</td>
<td align="right">184,321,670</td>
<td align="right">6.8%</td>
<td align="right">1.0%</td>
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
<td align="right">209,234,950</td>
<td align="right">17.7%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,304,809</td>
<td align="right">5.5%</td>
<td align="right">67,437,530</td>
<td align="right">5.7%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">238,585,082</td>
<td align="right">21.0%</td>
<td align="right">256,102,121</td>
<td align="right">21.7%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">33,621,454</td>
<td align="right">3.0%</td>
<td align="right">32,173,762</td>
<td align="right">2.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,085,095</td>
<td align="right">7.2%</td>
<td align="right">84,053,556</td>
<td align="right">7.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,871,265</td>
<td align="right">7.0%</td>
<td align="right">80,471,677</td>
<td align="right">6.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,344,721</td>
<td align="right">2.8%</td>
<td align="right">30,799,004</td>
<td align="right">2.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,233,202</td>
<td align="right">2.8%</td>
<td align="right">30,792,543</td>
<td align="right">2.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">31,597,052</td>
<td align="right">2.8%</td>
<td align="right">31,833,357</td>
<td align="right">2.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">103,205,504</td>
<td align="right">9.1%</td>
<td align="right">103,246,804</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
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
<td align="right">5,133,125,925</td>
<td align="right">76.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,412,593,406</td>
<td align="right">81.0%</td>
<td align="right">5,412,079,798</td>
<td align="right">81.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,547,793</td>
<td align="right">1.1%</td>
<td align="right">71,546,798</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,287,383</td>
<td align="right">4.1%</td>
<td align="right">274,289,086</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,808,724</td>
<td align="right">0.4%</td>
<td align="right">23,808,613</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">956,853,359</td>
<td align="right">14.3%</td>
<td align="right">956,854,578</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">961,127,596</td>
<td align="right">14.4%</td>
<td align="right">961,128,815</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,306,748</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,306,748</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,534,148</td>
<td align="right">3.9%</td>
<td align="right">259,533,998</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,177,825</td>
<td align="right">8.7%</td>
<td align="right">584,177,933</td>
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
<td align="left">Method cache misses</td>
<td align="right">55,219,901</td>
<td align="right"></td>
<td align="right">58,807,691</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,944,917</td>
<td align="right"></td>
<td align="right">63,622,492</td>
<td align="right"></td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,097,666,436</td>
<td align="right"></td>
<td align="right">2,136,599,250</td>
<td align="right"></td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,413,778</td>
<td align="right"></td>
<td align="right">5,505,837</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,222,621,787</td>
<td align="right">1.2%</td>
<td align="right">1,208,541,794</td>
<td align="right">1.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,058,718,317</td>
<td align="right">27.4%</td>
<td align="right">24,815,101,475</td>
<td align="right">27.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,450,943,535</td>
<td align="right">31.7%</td>
<td align="right">33,145,740,856</td>
<td align="right">31.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">39,457,744,597</td>
<td align="right">43.1%</td>
<td align="right">39,735,056,324</td>
<td align="right">43.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,749,828,742</td>
<td align="right">46.1%</td>
<td align="right">49,088,038,331</td>
<td align="right">46.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,959,789,714</td>
<td align="right">3.2%</td>
<td align="right">2,949,245,974</td>
<td align="right">3.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,107,028,623</td>
<td align="right">26.3%</td>
<td align="right">24,158,027,147</td>
<td align="right">26.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">22,223,934,265</td>
<td align="right">21.0%</td>
<td align="right">22,268,597,248</td>
<td align="right">21.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,369,279,297</td>
<td align="right"></td>
<td align="right">2,370,781,491</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,604,905</td>
<td align="right">0.0%</td>
<td align="right">6,606,819</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,699,735</td>
<td align="right">0.4%</td>
<td align="right">71,712,563</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,453,235,141</td>
<td align="right"></td>
<td align="right">13,451,757,695</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,451,523,783</td>
<td align="right">70.8%</td>
<td align="right">13,450,070,980</td>
<td align="right">70.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,110,276,873</td>
<td align="right"></td>
<td align="right">6,110,633,538</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,473,463,657</td>
<td align="right">28.8%</td>
<td align="right">5,473,402,811</td>
<td align="right">28.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,375,775</td>
<td align="right"></td>
<td align="right">177,374,053</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,551,768,297</td>
<td align="right">29.2%</td>
<td align="right">5,551,722,193</td>
<td align="right">29.2%</td>
<td align="right">-0.0%</td>
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
<td align="right">366,936</td>
<td align="right">94,008,212</td>
<td align="right">9,770,390,595</td>
<td align="right">818,293,629</td>
<td align="right">755,791,841</td>
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
<td align="right">5,666,443,904</td>
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
<td align="right">982</td>
<td align="right">1.9%</td>
<td align="right">63.4%</td>
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
<td align="right">1,368</td>
<td align="right">0.3%</td>
<td align="right">61.3%</td>
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
<td align="right">5,088</td>
<td align="right">1.1%</td>
<td align="right">59.7%</td>
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
<td align="right">52,235</td>
<td align="right">11.1%</td>
<td align="right">43.9%</td>
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
<td align="right">283</td>
<td align="right">0.1%</td>
<td align="right">41.5%</td>
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
<td align="right">1,669</td>
<td align="right">0.4%</td>
<td align="right">24.6%</td>
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
<td align="right">222</td>
<td align="right">0.0%</td>
<td align="right">22.0%</td>
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
<td align="right">145,898</td>
<td align="right">30.9%</td>
<td align="right">9.0%</td>
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
<td align="right">4,132,174,919</td>
<td align="right"></td>
<td align="right">7.2%</td>
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
<td align="right">471,782</td>
<td align="right"></td>
<td align="right">7.1%</td>
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
<td align="right">250,387,287,295</td>
<td align="right">6,059.5%</td>
<td align="right">1.7%</td>
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
<td align="right">226,642</td>
<td align="right">48.0%</td>
<td align="right">1.4%</td>
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
<td align="right">46,724</td>
<td align="right">9.9%</td>
<td align="right">-0.3%</td>
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
<td align="right">44,833</td>
<td align="right">85.8%</td>
<td align="right">46.2%</td>
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
<td align="right">52,235</td>
<td align="right"></td>
<td align="right">43.9%</td>
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
<td align="right">65,955,637</td>
<td align="right">16.0%</td>
<td align="right">97,233,903</td>
<td align="right">16.4%</td>
<td align="right">47.4%</td>
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
<td align="right">12,545,104</td>
<td align="right">2.1%</td>
<td align="right">44.5%</td>
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
<td align="right">592,519,168</td>
<td align="right"></td>
<td align="right">44.1%</td>
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
<td align="right">482,740,161</td>
<td align="right">81.5%</td>
<td align="right">43.4%</td>
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
<td align="right">3,358,720</td>
<td align="right">0.6%</td>
<td align="right">-19.4%</td>
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
<td align="left">8,478</td>
<td align="right">18.9%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">9,538</td>
<td align="right">31.1%</td>
<td align="left">14,778</td>
<td align="right">33.0%</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,470</td>
<td align="right">27.6%</td>
<td align="left">13,370</td>
<td align="right">29.8%</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,081</td>
<td align="right">13.3%</td>
<td align="left">6,175</td>
<td align="right">13.8%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,691</td>
<td align="right">5.5%</td>
<td align="left">1,832</td>
<td align="right">4.1%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">160</td>
<td align="right">0.5%</td>
<td align="left">200</td>
<td align="right">0.4%</td>
<td align="right">25.0%</td>
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
<td align="right">1,707</td>
<td align="right">3.3%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,481</td>
<td align="right">4.1%</td>
<td align="right">1,821</td>
<td align="right">3.5%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,422</td>
<td align="right">14.9%</td>
<td align="right">7,130</td>
<td align="right">13.6%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,375</td>
<td align="right">28.6%</td>
<td align="right">16,900</td>
<td align="right">32.4%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,395</td>
<td align="right">20.4%</td>
<td align="right">11,418</td>
<td align="right">21.9%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,994</td>
<td align="right">19.3%</td>
<td align="right">9,523</td>
<td align="right">18.2%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,691</td>
<td align="right">7.4%</td>
<td align="right">3,049</td>
<td align="right">5.8%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">507</td>
<td align="right">1.4%</td>
<td align="right">687</td>
<td align="right">1.3%</td>
<td align="right">35.5%</td>
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
<td align="right">1,125</td>
<td align="right">2.2%</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,120</td>
<td align="right">3.1%</td>
<td align="right">1,336</td>
<td align="right">2.6%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,653</td>
<td align="right">7.3%</td>
<td align="right">2,954</td>
<td align="right">5.7%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,072</td>
<td align="right">27.8%</td>
<td align="right">15,030</td>
<td align="right">28.8%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,433</td>
<td align="right">23.2%</td>
<td align="right">13,753</td>
<td align="right">26.3%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,222</td>
<td align="right">11.6%</td>
<td align="right">6,320</td>
<td align="right">12.1%</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,831</td>
<td align="right">7.8%</td>
<td align="right">3,626</td>
<td align="right">6.9%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">530</td>
<td align="right">1.5%</td>
<td align="right">689</td>
<td align="right">1.3%</td>
<td align="right">30.0%</td>
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
<td align="right">175,098</td>
<td align="right">553.4%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">23,212</td>
<td align="right">102,668</td>
<td align="right">342.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">973,917</td>
<td align="right">154.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">158,441</td>
<td align="right">342,385</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,220,144</td>
<td align="right">22,281</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">45,066</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">13,260,066</td>
<td align="right">3,766,950</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">8,088,280</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,508,076</td>
<td align="right">2,439,370</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">29,340</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,320,276</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">441,689</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">95,794</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">85,608</td>
<td align="right">116,367</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,957,410</td>
<td align="right">22,938,269</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">92,672,199</td>
<td align="right">109,201,188</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">91,976,259</td>
<td align="right">108,204,068</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,976,259</td>
<td align="right">108,204,068</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">43,824,341</td>
<td align="right">36,699,448</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">142,536,503</td>
<td align="right">165,263,231</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,310,575</td>
<td align="right">1,514,210</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,186,716</td>
<td align="right">156,977,647</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">73,836,596</td>
<td align="right">64,435,396</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">162,702,378</td>
<td align="right">182,768,138</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">55,886,227</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">55,886,227</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,890,144</td>
<td align="right">3,241,850</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">4,844,623</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">30,032,954</td>
<td align="right">33,388,745</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">202,428,941</td>
<td align="right">182,570,512</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">45,824,616</td>
<td align="right">49,929,423</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,688,088</td>
<td align="right">67,152,752</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">115,502,589</td>
<td align="right">125,668,314</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">116,173,764</td>
<td align="right">126,320,648</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,571,606</td>
<td align="right">12,545,756</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">701,495,336</td>
<td align="right">760,357,603</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,818,970,615</td>
<td align="right">4,109,133,982</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">169,036,781</td>
<td align="right">181,753,599</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">25,999,567</td>
<td align="right">27,942,945</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,171,220</td>
<td align="right">3,404,800</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">295,017,830</td>
<td align="right">316,433,410</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,853,951,237</td>
<td align="right">4,132,174,919</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">256,380,769</td>
<td align="right">274,340,242</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,697,295</td>
<td align="right">40,271,804</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,374,659</td>
<td align="right">7,869,162</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,241,707,913</td>
<td align="right">1,324,284,117</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,961,160</td>
<td align="right">5,284,820</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,852,580</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">107,112,198</td>
<td align="right">113,973,582</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,790,704,815</td>
<td align="right">2,968,983,362</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,012,080</td>
<td align="right">3,203,420</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,115,165</td>
<td align="right">45,801,591</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">11,508,290</td>
<td align="right">10,792,056</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">353,600</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,614,520</td>
<td align="right">7,005,400</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">317,001,818</td>
<td align="right">335,731,407</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">252,435,301</td>
<td align="right">266,695,569</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,818,132</td>
<td align="right">73,734,620</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">234,976,012</td>
<td align="right">248,129,504</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,052,929</td>
<td align="right">6,391,425</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">278,554,136</td>
<td align="right">293,462,035</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">808,811,386</td>
<td align="right">851,709,098</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,106,940</td>
<td align="right">44,265,840</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">153,190,275</td>
<td align="right">161,030,755</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,001,870</td>
<td align="right">5,254,700</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">143,855,102</td>
<td align="right">151,092,837</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">148,138,116</td>
<td align="right">155,408,024</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,065,840</td>
<td align="right">49,358,260</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,475,080</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,560,234</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,560,234</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">314,923,603</td>
<td align="right">329,520,338</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,822,600</td>
<td align="right">2,949,940</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,822,600</td>
<td align="right">2,949,940</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">66,306,036</td>
<td align="right">63,351,315</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">73,369,959</td>
<td align="right">76,609,195</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">111,244,816</td>
<td align="right">116,099,101</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">35,266,120</td>
<td align="right">33,810,393</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">41,429,630</td>
<td align="right">43,112,043</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">412,052,824</td>
<td align="right">428,694,407</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,956,010</td>
<td align="right">7,236,600</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">18,771,684</td>
<td align="right">19,515,845</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">399,379,185</td>
<td align="right">414,043,604</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">54,918,418</td>
<td align="right">52,919,949</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">390,330,773</td>
<td align="right">404,528,508</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,922,208</td>
<td align="right">4,064,553</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,864,801,136</td>
<td align="right">1,932,312,624</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,308,759,629</td>
<td align="right">6,536,506,240</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">180,319,232</td>
<td align="right">174,035,550</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">36,763,718</td>
<td align="right">38,026,763</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,713,627</td>
<td align="right">35,862,665</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">17,372,080</td>
<td align="right">17,937,080</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">23,550,310</td>
<td align="right">24,230,044</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">23,550,310</td>
<td align="right">24,230,044</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,425,772,334</td>
<td align="right">1,465,855,992</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,425,395,783</td>
<td align="right">1,465,354,892</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,243,616,102</td>
<td align="right">2,306,129,641</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,460,483</td>
<td align="right">56,984,285</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">106,388,800</td>
<td align="right">103,512,900</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">188,493,771</td>
<td align="right">193,583,688</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">339,011,007</td>
<td align="right">348,158,326</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,953,138,076</td>
<td align="right">3,030,241,227</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">296,755,796</td>
<td align="right">289,220,843</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,348,454,898</td>
<td align="right">4,242,240,609</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">565,765,041</td>
<td align="right">579,374,945</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,383,174</td>
<td align="right">657,616,990</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">757,567,708</td>
<td align="right">775,527,640</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">553,034,326</td>
<td align="right">565,413,169</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">462,686,207</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">462,686,207</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,978,645,153</td>
<td align="right">4,066,777,179</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,549,838</td>
<td align="right">120,117,015</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">431,668,601</td>
<td align="right">440,965,734</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">168,158,180</td>
<td align="right">164,545,505</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">641,796,101</td>
<td align="right">655,544,609</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">352,930,430</td>
<td align="right">360,430,733</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,220,887,308</td>
<td align="right">1,246,813,613</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">39,305,461</td>
<td align="right">40,115,911</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,454,808,392</td>
<td align="right">2,404,331,321</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">399,613,664</td>
<td align="right">407,703,474</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,476,152</td>
<td align="right">48,430,970</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">100,976,530</td>
<td align="right">102,967,443</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,004,730</td>
<td align="right">146,843,105</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,294,340,277</td>
<td align="right">1,319,819,287</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,394,828</td>
<td align="right">48,326,859</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">461,592,496</td>
<td align="right">470,591,723</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,794,882,981</td>
<td align="right">1,829,718,025</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">453,847,045</td>
<td align="right">462,502,985</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,034,320</td>
<td align="right">74,413,180</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,341,207,748</td>
<td align="right">35,985,966,566</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,416,888,642</td>
<td align="right">1,442,061,128</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,154,167,843</td>
<td align="right">2,191,862,755</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,991,098,869</td>
<td align="right">7,109,259,162</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,370,578,180</td>
<td align="right">41,035,733,318</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,546,104,524</td>
<td align="right">1,571,447,369</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">444,050,141</td>
<td align="right">451,327,339</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">486,650,286</td>
<td align="right">494,583,184</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,193,684</td>
<td align="right">46,929,931</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">467,890,537</td>
<td align="right">475,336,682</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,798,940,417</td>
<td align="right">1,827,498,425</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">29,768,070</td>
<td align="right">30,221,560</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">29,768,070</td>
<td align="right">30,221,560</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">43,982,703</td>
<td align="right">44,650,538</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">966,635,522</td>
<td align="right">981,025,448</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">966,500,562</td>
<td align="right">980,706,748</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,295,551,573</td>
<td align="right">1,314,096,733</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,863,459,040</td>
<td align="right">7,969,435,887</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">136,640,971</td>
<td align="right">138,474,038</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,473,111,819</td>
<td align="right">2,504,561,483</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">644,193,077</td>
<td align="right">652,286,646</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">236,844,758</td>
<td align="right">239,731,760</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">149,494,909</td>
<td align="right">147,682,434</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">528,091,463</td>
<td align="right">534,439,157</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">39,464,124</td>
<td align="right">39,910,611</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,010,421,801</td>
<td align="right">998,996,783</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,450,393,988</td>
<td align="right">3,487,979,559</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,961,242,711</td>
<td align="right">11,080,223,345</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,831,083,876</td>
<td align="right">2,861,318,473</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,833,921,008</td>
<td align="right">3,873,572,625</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,960,962</td>
<td align="right">20,159,748</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">541,777,961</td>
<td align="right">547,141,219</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">406,927,868</td>
<td align="right">410,818,804</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">460,952,104</td>
<td align="right">465,194,907</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,276,662</td>
<td align="right">1,177,829,933</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">36,367,438</td>
<td align="right">36,691,853</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,110,691,604</td>
<td align="right">1,120,565,051</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,350,347,856</td>
<td align="right">1,361,869,622</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,016,106,830</td>
<td align="right">2,032,871,590</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,139,612,007</td>
<td align="right">1,148,930,188</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,871,924</td>
<td align="right">39,184,746</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,769,162,246</td>
<td align="right">3,799,191,610</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">952,750,306</td>
<td align="right">960,079,658</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">249,694,147</td>
<td align="right">251,571,533</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,002,700,616</td>
<td align="right">1,010,104,779</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">69,571,394</td>
<td align="right">70,075,650</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">69,571,394</td>
<td align="right">70,075,650</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">150,369,864</td>
<td align="right">151,426,376</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">46,728,468</td>
<td align="right">47,055,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">846,845,553</td>
<td align="right">852,751,822</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,913,472,764</td>
<td align="right">3,939,697,999</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,339,808,206</td>
<td align="right">1,348,494,733</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,401,747,121</td>
<td align="right">4,430,212,139</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">494,105,970</td>
<td align="right">497,136,625</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">769,932,725</td>
<td align="right">774,603,910</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">971,534,463</td>
<td align="right">977,419,618</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">593,441,283</td>
<td align="right">596,976,866</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,264,815</td>
<td align="right">54,939,974</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,249,948,372</td>
<td align="right">1,257,275,923</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,249,948,372</td>
<td align="right">1,257,275,923</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,237,946,950</td>
<td align="right">1,244,715,689</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">427,994,534</td>
<td align="right">430,245,258</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">1,557,554,920</td>
<td align="right">1,565,710,424</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,546,900</td>
<td align="right">59,855,400</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,003,700</td>
<td align="right">3,019,080</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">227,548,352</td>
<td align="right">226,417,123</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">357,814,305</td>
<td align="right">356,035,511</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,205,621,742</td>
<td align="right">1,211,544,488</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">71,532,780</td>
<td align="right">71,883,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,111,777</td>
<td align="right">198,988,734</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,876,523,140</td>
<td align="right">2,888,279,808</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">911,622,888</td>
<td align="right">915,343,896</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">911,622,888</td>
<td align="right">915,301,136</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,376,320</td>
<td align="right">111,797,520</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,052,114,763</td>
<td align="right">1,055,954,784</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,341,749,232</td>
<td align="right">1,346,371,888</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">200,489,676</td>
<td align="right">199,808,990</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,172,826,339</td>
<td align="right">1,176,371,770</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">254,794,593</td>
<td align="right">255,471,112</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,287,384</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,287,384</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,771,141</td>
<td align="right">523,119,699</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,342,629,585</td>
<td align="right">2,348,282,742</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">338,666,797</td>
<td align="right">337,899,265</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,468,813,756</td>
<td align="right">1,472,037,917</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">749,042,877</td>
<td align="right">750,647,558</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">486,892,224</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">93,891,060</td>
<td align="right">94,075,380</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">966,661,248</td>
<td align="right">968,524,861</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,195,783,677</td>
<td align="right">1,198,043,014</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">166,103,292</td>
<td align="right">166,346,341</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,075,674,646</td>
<td align="right">1,074,190,115</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">735,007,110</td>
<td align="right">734,687,764</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,997,705,814</td>
<td align="right">1,998,274,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,285,386</td>
<td align="right">746,438,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">225,785,209</td>
<td align="right">225,750,256</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,220,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">1,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">225,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">225,640</td>
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
<td align="right">1,728</td>
<td align="right">1,526</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,356</td>
<td align="right">24,156</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,981</td>
<td align="right">23,043</td>
<td align="right">0.3%</td>
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
<td align="right">501</td>
<td align="right">24.9%</td>
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
<td align="right">501</td>
<td align="right">24.9%</td>
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
Stats gathered on: 2025-06-30
