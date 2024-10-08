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
<td align="left">UNARY_NOT</td>
<td align="right">8,592,402</td>
<td align="right">42,380,746</td>
<td align="right">393.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,016,840</td>
<td align="right">2,639,635</td>
<td align="right">159.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">31,950,049</td>
<td align="right">46,174,419</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">47,536,327</td>
<td align="right">65,965,533</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">147,875,538</td>
<td align="right">92,142,883</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">76,854,335</td>
<td align="right">105,791,269</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">49,664,326</td>
<td align="right">65,913,193</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">298,142,648</td>
<td align="right">393,617,136</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,595,127</td>
<td align="right">418,860,136</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,812,638</td>
<td align="right">2,798,350</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">28,606,818</td>
<td align="right">35,304,770</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,834,981</td>
<td align="right">191,963,612</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">249,130,695</td>
<td align="right">303,529,709</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">47,916,488</td>
<td align="right">57,903,098</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">47,086,340</td>
<td align="right">56,181,131</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,722,019,911</td>
<td align="right">4,347,274,363</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">616,480,822</td>
<td align="right">717,947,345</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">38,983,259</td>
<td align="right">45,243,724</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,499,109</td>
<td align="right">43,520,596</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">164,193,009</td>
<td align="right">189,236,330</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">420,642,747</td>
<td align="right">482,468,726</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">217,216,610</td>
<td align="right">249,041,817</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">214,332,381</td>
<td align="right">244,591,157</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">403,386,487</td>
<td align="right">459,174,538</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">46,580,291</td>
<td align="right">52,821,890</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">292,552,174</td>
<td align="right">329,369,861</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">238,820,575</td>
<td align="right">268,158,585</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">51,222,129</td>
<td align="right">57,447,992</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">222,479,894</td>
<td align="right">244,013,786</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">632,323,882</td>
<td align="right">691,497,768</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">759,527,224</td>
<td align="right">830,491,201</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,060,892,889</td>
<td align="right">2,784,739,912</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">75,411,573</td>
<td align="right">82,180,241</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">39,863,441</td>
<td align="right">43,313,561</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">138,098</td>
<td align="right">150,038</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,383,630,296</td>
<td align="right">2,587,474,427</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">983,237,034</td>
<td align="right">1,066,454,401</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,730,405,612</td>
<td align="right">1,874,342,169</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,601,768,201</td>
<td align="right">4,913,500,361</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,737,548,165</td>
<td align="right">17,796,492,066</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,834,798</td>
<td align="right">125,036,996</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">338,100,648</td>
<td align="right">358,670,479</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">329,942,681</td>
<td align="right">348,570,485</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">708,718,124</td>
<td align="right">747,766,941</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">132,589,444</td>
<td align="right">139,312,876</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">211,498,940</td>
<td align="right">221,999,396</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">110,049,138</td>
<td align="right">115,293,063</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,426,396</td>
<td align="right">2,541,099</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,016,280</td>
<td align="right">128,773,308</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,631,108</td>
<td align="right">221,060,037</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,972,563,877</td>
<td align="right">5,188,414,799</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">176,285,015</td>
<td align="right">183,893,540</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">144,617,407</td>
<td align="right">138,991,485</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">195,545,971</td>
<td align="right">202,735,045</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,021,554,370</td>
<td align="right">4,163,371,385</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">363,140,936</td>
<td align="right">375,771,994</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">756,710,372</td>
<td align="right">781,040,589</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">195,025,230</td>
<td align="right">200,866,378</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,257,713</td>
<td align="right">53,794,831</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,806,435,638</td>
<td align="right">2,888,306,090</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">124,803,368</td>
<td align="right">121,426,100</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">200,496,760</td>
<td align="right">205,235,709</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,709,087</td>
<td align="right">4,818,563</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,701,171</td>
<td align="right">9,919,730</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,063,445</td>
<td align="right">1,086,630</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">320,047,205</td>
<td align="right">326,482,086</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">267,328,936</td>
<td align="right">272,602,100</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,289,851</td>
<td align="right">9,470,930</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,067,174,440</td>
<td align="right">1,087,448,038</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">232,239,132</td>
<td align="right">236,624,915</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">548,217,386</td>
<td align="right">558,419,514</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,975,428,357</td>
<td align="right">3,029,007,930</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">297,456,258</td>
<td align="right">302,222,198</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">449,514,152</td>
<td align="right">456,470,059</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">166,518,338</td>
<td align="right">169,049,151</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">836,474,356</td>
<td align="right">848,694,819</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,897,780,605</td>
<td align="right">1,870,356,572</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,822,184</td>
<td align="right">15,032,964</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">39,133,656</td>
<td align="right">39,622,391</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,926,993,385</td>
<td align="right">3,882,170,469</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">61,109,887</td>
<td align="right">61,788,255</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,489,000</td>
<td align="right">105,433,716</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,334,326,820</td>
<td align="right">2,313,673,461</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">41,780,192</td>
<td align="right">42,149,372</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">73,129</td>
<td align="right">72,491</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,539,603</td>
<td align="right">47,941,643</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60,192,335</td>
<td align="right">59,708,435</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,606,781</td>
<td align="right">142,660,768</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">542,597,012</td>
<td align="right">546,374,201</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,439,071</td>
<td align="right">35,193,355</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">50,294,647</td>
<td align="right">49,949,078</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,655,959</td>
<td align="right">48,965,891</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,889,555</td>
<td align="right">72,339,040</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">355,256,918</td>
<td align="right">357,378,895</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">477,643,513</td>
<td align="right">480,440,285</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">829,457,042</td>
<td align="right">834,005,336</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,550,089</td>
<td align="right">7,590,219</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">643,016,103</td>
<td align="right">646,315,966</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">55,625,339</td>
<td align="right">55,365,112</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">367,131,012</td>
<td align="right">368,802,308</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">651,671,775</td>
<td align="right">654,575,545</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,532,059</td>
<td align="right">108,008,613</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">838,281,650</td>
<td align="right">841,966,417</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">918,891</td>
<td align="right">914,926</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">500,894,246</td>
<td align="right">503,008,630</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">850,550,483</td>
<td align="right">854,100,876</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">272,923,013</td>
<td align="right">274,011,122</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,175,872,286</td>
<td align="right">5,155,647,151</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,416,748</td>
<td align="right">1,421,615</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,857,163,352</td>
<td align="right">2,866,680,939</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">119,503,633</td>
<td align="right">119,112,568</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,326,504</td>
<td align="right">143,776,831</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">909,427,408</td>
<td align="right">912,240,702</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">201,825,949</td>
<td align="right">202,442,807</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,035,995</td>
<td align="right">92,299,041</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,310,740</td>
<td align="right">10,339,140</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">28,797,337</td>
<td align="right">28,859,563</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,291,789</td>
<td align="right">20,333,046</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,390,120,319</td>
<td align="right">1,392,939,397</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">277,685,723</td>
<td align="right">278,176,942</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">182,856</td>
<td align="right">182,555</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">85,690,715</td>
<td align="right">85,559,221</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">99,891,659</td>
<td align="right">100,022,589</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">127,526,941</td>
<td align="right">127,392,249</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,368,245</td>
<td align="right">11,378,855</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,074,133,065</td>
<td align="right">1,073,178,667</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,295,038,850</td>
<td align="right">2,293,236,631</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">494,651,842</td>
<td align="right">494,995,090</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">355,110,269</td>
<td align="right">354,869,752</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">20,521,080</td>
<td align="right">20,533,248</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">210,191,975</td>
<td align="right">210,311,309</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,706,955</td>
<td align="right">10,712,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">231,735</td>
<td align="right">231,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,411,056</td>
<td align="right">11,415,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">403,007,384</td>
<td align="right">403,166,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">153,629,832</td>
<td align="right">153,688,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,943,657</td>
<td align="right">3,945,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">206,019,469</td>
<td align="right">206,088,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,798,330</td>
<td align="right">21,792,553</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,237,345</td>
<td align="right">22,231,714</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,245,690</td>
<td align="right">22,240,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">83,020,308</td>
<td align="right">83,040,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,900,649</td>
<td align="right">82,920,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">151,913,463</td>
<td align="right">151,940,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">158,640</td>
<td align="right">158,616</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,373,572,028</td>
<td align="right">1,373,398,545</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,284,792</td>
<td align="right">35,280,433</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">194,581</td>
<td align="right">194,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">71,749,391</td>
<td align="right">71,743,937</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">291,940</td>
<td align="right">291,921</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,836,842</td>
<td align="right">5,837,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,905</td>
<td align="right">16,904</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,719,302</td>
<td align="right">268,732,692</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,950,806</td>
<td align="right">91,946,813</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,927,280</td>
<td align="right">173,920,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,748,167</td>
<td align="right">3,748,045</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">235,105,514</td>
<td align="right">235,099,678</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,091,846</td>
<td align="right">136,094,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,461,383</td>
<td align="right">20,461,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,467,079</td>
<td align="right">82,468,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,527,824</td>
<td align="right">225,530,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,643,486</td>
<td align="right">402,639,375</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,176,520</td>
<td align="right">92,176,408</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,459,560</td>
<td align="right">94,459,448</td>
<td align="right">-0.0%</td>
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
<td align="right">3,465,700</td>
<td align="right">3,465,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">807,420</td>
<td align="right">807,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">640,820</td>
<td align="right">640,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">101,260</td>
<td align="right">101,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,880</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,420</td>
<td align="right">21,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">390,917,923</td>
<td align="right">4.0%</td>
<td align="right">403,614,908</td>
<td align="right">4.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,506,663</td>
<td align="right">0.3%</td>
<td align="right">29,582,820</td>
<td align="right">0.3%</td>
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
<td align="right">9,405,559,214</td>
<td align="right">96.0%</td>
<td align="right">9,405,555,645</td>
<td align="right">95.9%</td>
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
<td align="right">1,126,934</td>
<td align="right">65.2%</td>
<td align="right">1,135,824</td>
<td align="right">65.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">602,742</td>
<td align="right">34.8%</td>
<td align="right">604,082</td>
<td align="right">34.7%</td>
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
<td align="left">and int</td>
<td align="right">33,175</td>
<td align="right">2.9%</td>
<td align="right">34,884</td>
<td align="right">3.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,165</td>
<td align="right">4.3%</td>
<td align="right">50,549</td>
<td align="right">4.5%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">47,912</td>
<td align="right">4.3%</td>
<td align="right">50,263</td>
<td align="right">4.4%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,851</td>
<td align="right">0.6%</td>
<td align="right">7,070</td>
<td align="right">0.6%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,166</td>
<td align="right">0.5%</td>
<td align="right">6,346</td>
<td align="right">0.6%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,705</td>
<td align="right">0.9%</td>
<td align="right">9,901</td>
<td align="right">0.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,701</td>
<td align="right">7.4%</td>
<td align="right">85,118</td>
<td align="right">7.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,793</td>
<td align="right">2.9%</td>
<td align="right">33,033</td>
<td align="right">2.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,438</td>
<td align="right">0.3%</td>
<td align="right">3,414</td>
<td align="right">0.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">16,500</td>
<td align="right">1.5%</td>
<td align="right">16,613</td>
<td align="right">1.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">21,361</td>
<td align="right">1.9%</td>
<td align="right">21,492</td>
<td align="right">1.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,748</td>
<td align="right">0.5%</td>
<td align="right">5,734</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">916</td>
<td align="right">0.1%</td>
<td align="right">918</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,514</td>
<td align="right">1.1%</td>
<td align="right">12,503</td>
<td align="right">1.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,124</td>
<td align="right">0.5%</td>
<td align="right">5,122</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,444</td>
<td align="right">0.7%</td>
<td align="right">7,442</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">782,381</td>
<td align="right">69.4%</td>
<td align="right">782,382</td>
<td align="right">68.9%</td>
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
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
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
<td align="right">656,053,670</td>
<td align="right">9.5%</td>
<td align="right">658,954,973</td>
<td align="right">9.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,793,226</td>
<td align="right">0.1%</td>
<td align="right">4,793,287</td>
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
<td align="right">6,216,544,883</td>
<td align="right">90.4%</td>
<td align="right">6,216,556,727</td>
<td align="right">90.4%</td>
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
<td align="right">224,746</td>
<td align="right">54.6%</td>
<td align="right">227,323</td>
<td align="right">54.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,585</td>
<td align="right">45.4%</td>
<td align="right">186,536</td>
<td align="right">45.1%</td>
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
<td align="left">buffer int</td>
<td align="right">21,731</td>
<td align="right">9.7%</td>
<td align="right">22,321</td>
<td align="right">9.8%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">820</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,180</td>
<td align="right">0.5%</td>
<td align="right">1,200</td>
<td align="right">0.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,991</td>
<td align="right">49.4%</td>
<td align="right">112,520</td>
<td align="right">49.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,140</td>
<td align="right">25.9%</td>
<td align="right">58,600</td>
<td align="right">25.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">11.9%</td>
<td align="right">26,640</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">720</td>
<td align="right">0.3%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">178,917,909</td>
<td align="right">1.3%</td>
<td align="right">173,588,474</td>
<td align="right">1.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">669,427,596</td>
<td align="right">4.7%</td>
<td align="right">664,542,086</td>
<td align="right">4.7%</td>
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
<td align="right">13,555,669,041</td>
<td align="right">95.3%</td>
<td align="right">13,560,057,025</td>
<td align="right">95.3%</td>
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
<td align="right">3,964,985</td>
<td align="right">95.7%</td>
<td align="right">3,864,226</td>
<td align="right">95.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">177,170</td>
<td align="right">4.3%</td>
<td align="right">177,252</td>
<td align="right">4.4%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">165,010</td>
<td align="right">93.1%</td>
<td align="right">165,092</td>
<td align="right">93.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,580</td>
<td align="right">6.5%</td>
<td align="right">11,580</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">580</td>
<td align="right">0.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,192,670</td>
<td align="right">0.0%</td>
<td align="right">1,334,342</td>
<td align="right">0.0%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">105,434,680</td>
<td align="right">1.8%</td>
<td align="right">106,511,121</td>
<td align="right">1.8%</td>
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
<td align="right">5,738,741,958</td>
<td align="right">98.2%</td>
<td align="right">5,738,729,123</td>
<td align="right">98.2%</td>
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
<td align="right">163,244</td>
<td align="right">66.1%</td>
<td align="right">170,528</td>
<td align="right">66.4%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">83,746</td>
<td align="right">33.9%</td>
<td align="right">86,409</td>
<td align="right">33.6%</td>
<td align="right">3.2%</td>
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
<td align="left">big int</td>
<td align="right">27,897</td>
<td align="right">17.1%</td>
<td align="right">34,058</td>
<td align="right">20.0%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">920</td>
<td align="right">0.6%</td>
<td align="right">980</td>
<td align="right">0.6%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,464</td>
<td align="right">0.9%</td>
<td align="right">1,556</td>
<td align="right">0.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,479</td>
<td align="right">10.7%</td>
<td align="right">17,867</td>
<td align="right">10.5%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">20,142</td>
<td align="right">12.3%</td>
<td align="right">20,423</td>
<td align="right">12.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,946</td>
<td align="right">30.0%</td>
<td align="right">49,201</td>
<td align="right">28.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">16,178</td>
<td align="right">9.9%</td>
<td align="right">16,221</td>
<td align="right">9.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,278</td>
<td align="right">7.5%</td>
<td align="right">12,282</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.5%</td>
<td align="right">10,680</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">3,060</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,640</td>
<td align="right">1.6%</td>
<td align="right">2,640</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,560</td>
<td align="right">1.0%</td>
<td align="right">1,560</td>
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
<td align="right">48,979,873</td>
<td align="right">1.9%</td>
<td align="right">55,218,886</td>
<td align="right">2.2%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,493,804,526</td>
<td align="right">98.1%</td>
<td align="right">2,493,814,257</td>
<td align="right">97.8%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,546,240</td>
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
<td align="right">83,558</td>
<td align="right">57.0%</td>
<td align="right">86,149</td>
<td align="right">57.7%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,100</td>
<td align="right">43.0%</td>
<td align="right">63,095</td>
<td align="right">42.3%</td>
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
<td align="left">str</td>
<td align="right">18,900</td>
<td align="right">22.6%</td>
<td align="right">20,840</td>
<td align="right">24.2%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,160</td>
<td align="right">16.9%</td>
<td align="right">14,520</td>
<td align="right">16.9%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,616</td>
<td align="right">37.8%</td>
<td align="right">31,826</td>
<td align="right">36.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">18,882</td>
<td align="right">22.6%</td>
<td align="right">18,963</td>
<td align="right">22.0%</td>
<td align="right">0.4%</td>
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
<td align="right">2,602,566</td>
<td align="right">0.2%</td>
<td align="right">6,737,030</td>
<td align="right">0.6%</td>
<td align="right">158.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">479,932,922</td>
<td align="right">45.6%</td>
<td align="right">486,784,225</td>
<td align="right">45.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">571,244,708</td>
<td align="right">54.3%</td>
<td align="right">577,422,104</td>
<td align="right">54.2%</td>
<td align="right">1.1%</td>
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
<td align="right">100,895</td>
<td align="right">32.2%</td>
<td align="right">178,867</td>
<td align="right">45.5%</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">212,262</td>
<td align="right">67.8%</td>
<td align="right">214,223</td>
<td align="right">54.5%</td>
<td align="right">0.9%</td>
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
<td align="right">4,220</td>
<td align="right">2.0%</td>
<td align="right">4,580</td>
<td align="right">2.1%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,133</td>
<td align="right">8.5%</td>
<td align="right">19,171</td>
<td align="right">8.9%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,860</td>
<td align="right">1.3%</td>
<td align="right">2,920</td>
<td align="right">1.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,965</td>
<td align="right">5.6%</td>
<td align="right">12,167</td>
<td align="right">5.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,960</td>
<td align="right">2.8%</td>
<td align="right">6,000</td>
<td align="right">2.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">39,846</td>
<td align="right">18.8%</td>
<td align="right">40,088</td>
<td align="right">18.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,180</td>
<td align="right">2.4%</td>
<td align="right">5,200</td>
<td align="right">2.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">819</td>
<td align="right">0.4%</td>
<td align="right">818</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">105,820</td>
<td align="right">49.9%</td>
<td align="right">105,820</td>
<td align="right">49.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,039</td>
<td align="right">3.3%</td>
<td align="right">7,039</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,920</td>
<td align="right">3.3%</td>
<td align="right">6,920</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,460</td>
<td align="right">1.2%</td>
<td align="right">2,460</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">740</td>
<td align="right">0.3%</td>
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
<td align="right">387,074,272</td>
<td align="right">2.4%</td>
<td align="right">464,200,336</td>
<td align="right">2.9%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,010,509,215</td>
<td align="right">6.3%</td>
<td align="right">1,145,333,065</td>
<td align="right">7.0%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,970,967,453</td>
<td align="right">93.6%</td>
<td align="right">15,130,274,017</td>
<td align="right">92.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">303,840</td>
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
<td align="right">8,000,124</td>
<td align="right">90.0%</td>
<td align="right">9,454,702</td>
<td align="right">91.2%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">888,815</td>
<td align="right">10.0%</td>
<td align="right">910,337</td>
<td align="right">8.8%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">172,074</td>
<td align="right">19.4%</td>
<td align="right">184,315</td>
<td align="right">20.2%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">77,690</td>
<td align="right">8.7%</td>
<td align="right">79,726</td>
<td align="right">8.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">162,177</td>
<td align="right">18.2%</td>
<td align="right">165,605</td>
<td align="right">18.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">157,268</td>
<td align="right">17.7%</td>
<td align="right">159,758</td>
<td align="right">17.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">90,929</td>
<td align="right">10.2%</td>
<td align="right">91,830</td>
<td align="right">10.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,570</td>
<td align="right">1.8%</td>
<td align="right">15,701</td>
<td align="right">1.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">18,060</td>
<td align="right">2.0%</td>
<td align="right">18,180</td>
<td align="right">2.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">3,120</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,311</td>
<td align="right">0.4%</td>
<td align="right">3,324</td>
<td align="right">0.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">104,414</td>
<td align="right">11.7%</td>
<td align="right">104,577</td>
<td align="right">11.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,746</td>
<td align="right">0.8%</td>
<td align="right">6,742</td>
<td align="right">0.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">19,111</td>
<td align="right">2.2%</td>
<td align="right">19,113</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,505</td>
<td align="right">2.3%</td>
<td align="right">20,506</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">27,940</td>
<td align="right">3.1%</td>
<td align="right">27,940</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">7,660</td>
<td align="right">0.9%</td>
<td align="right">7,660</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
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
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">4,766,444,838</td>
<td align="right">99.6%</td>
<td align="right">4,977,856,526</td>
<td align="right">99.6%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">422,987</td>
<td align="right">0.0%</td>
<td align="right">423,105</td>
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
<td align="right">20,363,600</td>
<td align="right">0.4%</td>
<td align="right">20,363,584</td>
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
<td align="right">9,860</td>
<td align="right">0.0%</td>
<td align="right">9,860</td>
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
<td align="right">520,770</td>
<td align="right">100.0%</td>
<td align="right">520,585</td>
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
<td align="right">86,798,395</td>
<td align="right">100.0%</td>
<td align="right">86,818,689</td>
<td align="right">100.0%</td>
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
<td align="right">8,445</td>
<td align="right">0.0%</td>
<td align="right">8,444</td>
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
<td align="right">8,460</td>
<td align="right">100.0%</td>
<td align="right">8,460</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,720</td>
<td align="right">0.0%</td>
<td align="right">30,880</td>
<td align="right">0.0%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,886,028</td>
<td align="right">18.1%</td>
<td align="right">173,882,534</td>
<td align="right">18.1%</td>
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
<td align="right">786,855,809</td>
<td align="right">81.9%</td>
<td align="right">786,851,267</td>
<td align="right">81.9%</td>
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
<td align="right">7,088</td>
<td align="right">10.3%</td>
<td align="right">7,132</td>
<td align="right">10.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,884</td>
<td align="right">89.7%</td>
<td align="right">61,829</td>
<td align="right">89.7%</td>
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
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.3%</td>
<td align="right">10,020</td>
<td align="right">16.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,124</td>
<td align="right">26.1%</td>
<td align="right">16,129</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">53.6%</td>
<td align="right">33,180</td>
<td align="right">53.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">189,717,180</td>
<td align="right">7.2%</td>
<td align="right">191,455,574</td>
<td align="right">7.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,447,467,422</td>
<td align="right">92.7%</td>
<td align="right">2,455,143,059</td>
<td align="right">92.7%</td>
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
<td align="right">140,324,676</td>
<td align="right">5.3%</td>
<td align="right">140,530,073</td>
<td align="right">5.3%</td>
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
<td align="right">99,935</td>
<td align="right">3.5%</td>
<td align="right">100,365</td>
<td align="right">3.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,765,274</td>
<td align="right">96.5%</td>
<td align="right">2,768,965</td>
<td align="right">96.5%</td>
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
<td align="left">property</td>
<td align="right">4,400</td>
<td align="right">4.4%</td>
<td align="right">4,540</td>
<td align="right">4.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,060</td>
<td align="right">32.1%</td>
<td align="right">32,340</td>
<td align="right">32.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,747</td>
<td align="right">8.8%</td>
<td align="right">8,761</td>
<td align="right">8.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,888</td>
<td align="right">9.9%</td>
<td align="right">9,884</td>
<td align="right">9.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,640</td>
<td align="right">14.6%</td>
<td align="right">14,640</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">10,900</td>
<td align="right">10.9%</td>
<td align="right">10,900</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,820</td>
<td align="right">6.8%</td>
<td align="right">6,820</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,820</td>
<td align="right">5.8%</td>
<td align="right">5,820</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,060</td>
<td align="right">5.1%</td>
<td align="right">5,060</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,540</td>
<td align="right">1.5%</td>
<td align="right">1,540</td>
<td align="right">1.5%</td>
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
<td align="right">267,204,356</td>
<td align="right">23.3%</td>
<td align="right">272,475,406</td>
<td align="right">23.6%</td>
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
<td align="right">880,046,636</td>
<td align="right">76.7%</td>
<td align="right">880,045,042</td>
<td align="right">76.3%</td>
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
<td align="right">110,759</td>
<td align="right">86.9%</td>
<td align="right">112,870</td>
<td align="right">87.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,721</td>
<td align="right">13.1%</td>
<td align="right">16,724</td>
<td align="right">12.9%</td>
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
<td align="left">bytearray int</td>
<td align="right">1,360</td>
<td align="right">1.2%</td>
<td align="right">1,640</td>
<td align="right">1.5%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">13,140</td>
<td align="right">11.9%</td>
<td align="right">14,280</td>
<td align="right">12.7%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">8,603</td>
<td align="right">7.8%</td>
<td align="right">9,013</td>
<td align="right">8.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,500</td>
<td align="right">1.4%</td>
<td align="right">1,540</td>
<td align="right">1.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,716</td>
<td align="right">38.6%</td>
<td align="right">42,957</td>
<td align="right">38.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,440</td>
<td align="right">39.2%</td>
<td align="right">43,440</td>
<td align="right">38.5%</td>
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
<td align="right">187,883,531</td>
<td align="right">3.2%</td>
<td align="right">214,213,440</td>
<td align="right">3.6%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,609,039</td>
<td align="right">0.4%</td>
<td align="right">25,962,562</td>
<td align="right">0.4%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,707,337,180</td>
<td align="right">96.8%</td>
<td align="right">5,765,914,218</td>
<td align="right">96.4%</td>
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
<td align="left">Failure</td>
<td align="right">242,080</td>
<td align="right">26.4%</td>
<td align="right">283,433</td>
<td align="right">28.8%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">676,437</td>
<td align="right">73.6%</td>
<td align="right">702,019</td>
<td align="right">71.2%</td>
<td align="right">3.8%</td>
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
<td align="right">7,819</td>
<td align="right">3.2%</td>
<td align="right">37,552</td>
<td align="right">13.2%</td>
<td align="right">380.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,725</td>
<td align="right">6.1%</td>
<td align="right">20,858</td>
<td align="right">7.4%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,208</td>
<td align="right">2.2%</td>
<td align="right">6,448</td>
<td align="right">2.3%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">84,285</td>
<td align="right">34.8%</td>
<td align="right">87,883</td>
<td align="right">31.0%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">22,921</td>
<td align="right">9.5%</td>
<td align="right">23,240</td>
<td align="right">8.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">14,840</td>
<td align="right">6.1%</td>
<td align="right">14,994</td>
<td align="right">5.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">56,701</td>
<td align="right">23.4%</td>
<td align="right">56,868</td>
<td align="right">20.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,338</td>
<td align="right">1.0%</td>
<td align="right">2,334</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">31,903</td>
<td align="right">13.2%</td>
<td align="right">31,916</td>
<td align="right">11.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">920</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
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
<td align="right">199,751</td>
<td align="right">0.0%</td>
<td align="right">199,661</td>
<td align="right">0.0%</td>
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
<td align="right">1,535,527,642</td>
<td align="right">100.0%</td>
<td align="right">1,535,424,219</td>
<td align="right">100.0%</td>
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
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">2,096</td>
<td align="right">6.0%</td>
<td align="right">2,098</td>
<td align="right">6.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">32,968</td>
<td align="right">94.0%</td>
<td align="right">32,945</td>
<td align="right">94.0%</td>
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
<td align="right">1,216</td>
<td align="right">58.0%</td>
<td align="right">1,218</td>
<td align="right">58.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">23.9%</td>
<td align="right">500</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">18.1%</td>
<td align="right">380</td>
<td align="right">18.1%</td>
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
<td align="right">772,232,297</td>
<td align="right">0.8%</td>
<td align="right">849,944,302</td>
<td align="right">0.8%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,010,004,295</td>
<td align="right">9.1%</td>
<td align="right">9,871,496,124</td>
<td align="right">9.6%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,745,664,787</td>
<td align="right">56.4%</td>
<td align="right">57,529,736,308</td>
<td align="right">56.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">33,238,538,587</td>
<td align="right">33.7%</td>
<td align="right">34,244,136,026</td>
<td align="right">33.4%</td>
<td align="right">3.0%</td>
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
<td align="right">187,883,531</td>
<td align="right">4.5%</td>
<td align="right">214,213,440</td>
<td align="right">4.9%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,010,509,215</td>
<td align="right">24.1%</td>
<td align="right">1,145,333,065</td>
<td align="right">26.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">390,917,923</td>
<td align="right">9.3%</td>
<td align="right">403,614,908</td>
<td align="right">9.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">267,204,356</td>
<td align="right">6.4%</td>
<td align="right">272,475,406</td>
<td align="right">6.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">479,932,922</td>
<td align="right">11.4%</td>
<td align="right">486,784,225</td>
<td align="right">11.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,434,680</td>
<td align="right">2.5%</td>
<td align="right">106,511,121</td>
<td align="right">2.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">189,717,180</td>
<td align="right">4.5%</td>
<td align="right">191,455,574</td>
<td align="right">4.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">669,427,596</td>
<td align="right">15.9%</td>
<td align="right">664,542,086</td>
<td align="right">15.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">656,053,670</td>
<td align="right">15.6%</td>
<td align="right">658,954,973</td>
<td align="right">15.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,886,028</td>
<td align="right">4.1%</td>
<td align="right">173,882,534</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">113,592,308</td>
<td align="right">14.7%</td>
<td align="right">158,845,605</td>
<td align="right">18.7%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">173,666,711</td>
<td align="right">22.5%</td>
<td align="right">196,136,663</td>
<td align="right">23.1%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,978,160</td>
<td align="right">4.7%</td>
<td align="right">38,679,246</td>
<td align="right">4.5%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,132,574</td>
<td align="right">3.3%</td>
<td align="right">24,664,785</td>
<td align="right">2.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,239,671</td>
<td align="right">2.4%</td>
<td align="right">18,070,776</td>
<td align="right">2.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">115,163,881</td>
<td align="right">14.9%</td>
<td align="right">115,837,100</td>
<td align="right">13.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,366,827</td>
<td align="right">4.6%</td>
<td align="right">35,517,791</td>
<td align="right">4.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">103,543,608</td>
<td align="right">13.4%</td>
<td align="right">103,116,172</td>
<td align="right">12.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,600,017</td>
<td align="right">3.6%</td>
<td align="right">27,598,588</td>
<td align="right">3.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,179,360</td>
<td align="right">2.6%</td>
<td align="right">20,179,360</td>
<td align="right">2.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">340,915,978</td>
<td align="right">4.0%</td>
<td align="right">339,327,053</td>
<td align="right">4.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,441,003,377</td>
<td align="right">16.9%</td>
<td align="right">1,439,384,530</td>
<td align="right">16.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,445,451,617</td>
<td align="right">17.0%</td>
<td align="right">1,443,832,770</td>
<td align="right">17.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,299,125,326</td>
<td align="right">27.0%</td>
<td align="right">2,297,323,725</td>
<td align="right">27.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,299,125,326</td>
<td align="right">27.0%</td>
<td align="right">2,297,323,725</td>
<td align="right">27.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">36,883,315</td>
<td align="right">0.4%</td>
<td align="right">36,870,374</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,210,639,167</td>
<td align="right">73.0%</td>
<td align="right">6,212,540,736</td>
<td align="right">73.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">853,673,709</td>
<td align="right">10.0%</td>
<td align="right">853,490,955</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">86,076,473</td>
<td align="right">1.0%</td>
<td align="right">86,069,887</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">177,002,570</td>
<td align="right">2.1%</td>
<td align="right">176,990,942</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,746,769,382</td>
<td align="right">79.3%</td>
<td align="right">6,747,045,271</td>
<td align="right">79.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">335,036,165</td>
<td align="right">3.9%</td>
<td align="right">335,026,387</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,360</td>
<td align="right">0.1%</td>
<td align="right">4,418,360</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
<td align="right">29,880</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">9,415,949</td>
<td align="right"></td>
<td align="right">7,524,302</td>
<td align="right"></td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">77,002,373</td>
<td align="right"></td>
<td align="right">72,370,086</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,881,047,331</td>
<td align="right"></td>
<td align="right">2,740,729,166</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">68,581,832</td>
<td align="right"></td>
<td align="right">65,840,282</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">45,604,068,891</td>
<td align="right">33.0%</td>
<td align="right">46,521,961,605</td>
<td align="right">33.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,533,964,611</td>
<td align="right">67.0%</td>
<td align="right">91,037,314,781</td>
<td align="right">66.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">61,460,068,639</td>
<td align="right">38.2%</td>
<td align="right">62,404,319,622</td>
<td align="right">38.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">99,363,445,564</td>
<td align="right">61.8%</td>
<td align="right">97,841,312,040</td>
<td align="right">61.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,410,629,925</td>
<td align="right"></td>
<td align="right">4,392,108,893</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">93,839,036</td>
<td align="right">0.4%</td>
<td align="right">93,877,402</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,741,395,041</td>
<td align="right"></td>
<td align="right">11,742,290,609</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,739,388,426</td>
<td align="right">47.5%</td>
<td align="right">11,740,275,118</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,049,769</td>
<td align="right"></td>
<td align="right">174,062,515</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,636,398</td>
<td align="right">0.1%</td>
<td align="right">15,637,262</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,993,725,414</td>
<td align="right">52.5%</td>
<td align="right">12,993,936,869</td>
<td align="right">52.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,884,249,980</td>
<td align="right">52.1%</td>
<td align="right">12,884,422,205</td>
<td align="right">52.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,689,657,680</td>
<td align="right"></td>
<td align="right">13,689,793,457</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">128,160</td>
<td align="right">0.1%</td>
<td align="right">128,160</td>
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
<td align="right">115,796,352</td>
<td align="right">19,760,677,352</td>
<td align="right">0</td>
<td align="right">115,695,723</td>
<td align="right">19,753,768,189</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,725,588</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,817,760</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,840</td>
<td align="right">0.2%</td>
<td align="right">4,920</td>
<td align="right">0.5%</td>
<td align="right">167.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">18,550</td>
<td align="right">1.8%</td>
<td align="right">26,747</td>
<td align="right">2.6%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">17,186</td>
<td align="right">1.7%</td>
<td align="right">24,750</td>
<td align="right">2.4%</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">151,532</td>
<td align="right">15.1%</td>
<td align="right">203,361</td>
<td align="right">20.0%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,170</td>
<td align="right">0.1%</td>
<td align="right">1,556</td>
<td align="right">0.2%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,312</td>
<td align="right">4.8%</td>
<td align="right">9,492</td>
<td align="right">4.7%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">852,301</td>
<td align="right">84.8%</td>
<td align="right">809,354</td>
<td align="right">79.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,370,699,021</td>
<td align="right"></td>
<td align="right">7,137,354,477</td>
<td align="right"></td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">622,340</td>
<td align="right">61.9%</td>
<td align="right">604,085</td>
<td align="right">59.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">268,373,890,571</td>
<td align="right">3,641.1%</td>
<td align="right">262,665,110,482</td>
<td align="right">3,680.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,005,003</td>
<td align="right"></td>
<td align="right">1,014,271</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
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
<td align="right">131,522</td>
<td align="right">86.8%</td>
<td align="right">179,551</td>
<td align="right">88.3%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">151,532</td>
<td align="right"></td>
<td align="right">203,361</td>
<td align="right"></td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,527</td>
<td align="right">1.7%</td>
<td align="right">2,633</td>
<td align="right">1.3%</td>
<td align="right">4.2%</td>
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
<td align="right">16,078</td>
<td align="right">10.6%</td>
<td align="right">21,930</td>
<td align="right">10.8%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">12,737</td>
<td align="right">8.4%</td>
<td align="right">16,482</td>
<td align="right">8.1%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">41,784</td>
<td align="right">27.6%</td>
<td align="right">50,591</td>
<td align="right">24.9%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">35,634</td>
<td align="right">23.5%</td>
<td align="right">47,256</td>
<td align="right">23.2%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">28,335</td>
<td align="right">18.7%</td>
<td align="right">43,245</td>
<td align="right">21.3%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,064</td>
<td align="right">9.3%</td>
<td align="right">19,297</td>
<td align="right">9.5%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">4,380</td>
<td align="right">2.2%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">180</td>
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
<td align="right">10,390</td>
<td align="right">6.9%</td>
<td align="right">16,639</td>
<td align="right">8.2%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">11,727</td>
<td align="right">7.7%</td>
<td align="right">13,421</td>
<td align="right">6.6%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">26,888</td>
<td align="right">17.7%</td>
<td align="right">32,922</td>
<td align="right">16.2%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">41,148</td>
<td align="right">27.2%</td>
<td align="right">53,424</td>
<td align="right">26.3%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,832</td>
<td align="right">16.4%</td>
<td align="right">35,596</td>
<td align="right">17.5%</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">12,223</td>
<td align="right">8.1%</td>
<td align="right">19,786</td>
<td align="right">9.7%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,774</td>
<td align="right">2.5%</td>
<td align="right">6,963</td>
<td align="right">3.4%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">48.1%</td>
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
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">8,516,700</td>
<td align="right">64,283,620</td>
<td align="right">654.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">10,205,180</td>
<td align="right">66,214,100</td>
<td align="right">548.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">73,431,620</td>
<td align="right">151,024,440</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,147,057</td>
<td align="right">127,417,646</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,943,340</td>
<td align="right">4,636,560</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">252,645,205</td>
<td align="right">101,732,920</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,470,459</td>
<td align="right">34,684,918</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">382,091,562</td>
<td align="right">218,577,573</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">502,394</td>
<td align="right">323,331</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">179,298,861</td>
<td align="right">237,256,523</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">51,232,560</td>
<td align="right">37,846,180</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">36,947,538</td>
<td align="right">27,460,959</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,701,920</td>
<td align="right">2,023,380</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,098,788</td>
<td align="right">341,181,999</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">49,191,209</td>
<td align="right">61,194,313</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,339,452</td>
<td align="right">103,707,199</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,339,452</td>
<td align="right">103,707,199</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,351,740</td>
<td align="right">5,728,945</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">438,623,573</td>
<td align="right">530,509,496</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,424,862,273</td>
<td align="right">1,132,778,622</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">517,557,908</td>
<td align="right">610,385,630</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">205,836,373</td>
<td align="right">170,403,310</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,541,942</td>
<td align="right">104,112,742</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,010,449</td>
<td align="right">2,559,398</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">365,314,447</td>
<td align="right">310,972,471</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">274,852,656</td>
<td align="right">315,167,397</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">15,053,609</td>
<td align="right">13,137,069</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">316,906,509</td>
<td align="right">281,506,545</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">397,336,144</td>
<td align="right">439,498,784</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,081,664,090</td>
<td align="right">969,860,849</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">122,882</td>
<td align="right">110,942</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">96,676,288</td>
<td align="right">105,998,223</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,890,429</td>
<td align="right">4,437,758</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">59,739,081</td>
<td align="right">54,308,980</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">82,131,756</td>
<td align="right">74,933,473</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">269,842</td>
<td align="right">246,662</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">850,954,213</td>
<td align="right">923,488,899</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,504,434,217</td>
<td align="right">4,127,039,633</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,258,801,927</td>
<td align="right">2,074,550,912</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,543,960,856</td>
<td align="right">1,419,900,622</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">475,812,974</td>
<td align="right">439,033,343</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,229,533,955</td>
<td align="right">1,323,725,281</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,347,644,821</td>
<td align="right">1,450,863,075</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,594,636</td>
<td align="right">42,144,440</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,369,280,523</td>
<td align="right">1,471,890,102</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,221,645</td>
<td align="right">9,469,272</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">762,899,895</td>
<td align="right">707,087,016</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,924,400</td>
<td align="right">59,282,620</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,682,490,612</td>
<td align="right">7,134,761,329</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,342,878,844</td>
<td align="right">1,252,597,715</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,623,509</td>
<td align="right">38,026,810</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,004,187,930</td>
<td align="right">942,346,399</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,820,707,072</td>
<td align="right">7,354,434,449</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">179,739,747</td>
<td align="right">190,230,998</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">196,491,111</td>
<td align="right">185,024,032</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">150,540</td>
<td align="right">141,760</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,554,871,850</td>
<td align="right">3,349,785,822</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,090,874,439</td>
<td align="right">15,165,777,467</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,678,759,867</td>
<td align="right">1,583,282,596</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,012,172,726</td>
<td align="right">1,907,826,898</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,386,177,769</td>
<td align="right">1,315,351,275</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">143,720,731</td>
<td align="right">136,505,478</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">924,611,269</td>
<td align="right">879,666,091</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,860,268</td>
<td align="right">125,598,418</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,385,213,496</td>
<td align="right">6,084,586,283</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,508,870,468</td>
<td align="right">18,606,921,948</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">111,270,619</td>
<td align="right">106,456,493</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">165,039,517</td>
<td align="right">172,093,744</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">286,284,716</td>
<td align="right">274,076,092</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">148,615,435</td>
<td align="right">142,574,606</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,312,626,977</td>
<td align="right">7,019,252,657</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">250,764,641</td>
<td align="right">240,794,030</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,422,650,756</td>
<td align="right">6,182,889,882</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,915,863,345</td>
<td align="right">1,844,916,708</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,446,558</td>
<td align="right">10,061,761</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,974,696,132</td>
<td align="right">1,906,252,462</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,974,040</td>
<td align="right">167,951,400</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,123,663,663</td>
<td align="right">3,015,609,223</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,012,845,148</td>
<td align="right">1,046,896,287</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,370,699,021</td>
<td align="right">7,137,354,477</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">649,622,450</td>
<td align="right">629,179,446</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,077,789</td>
<td align="right">723,637,176</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,089,882,585</td>
<td align="right">2,148,998,320</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,247,640</td>
<td align="right">107,159,240</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,688,903,389</td>
<td align="right">4,558,980,279</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,852,829,835</td>
<td align="right">3,751,423,606</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">98,641,215</td>
<td align="right">96,084,052</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,778,040</td>
<td align="right">8,559,290</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,565,326,825</td>
<td align="right">14,228,803,511</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">7,009,391</td>
<td align="right">6,847,955</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">463,454</td>
<td align="right">452,970</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,216,461,198</td>
<td align="right">9,986,407,237</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">99,213,355</td>
<td align="right">96,988,732</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">830,595,752</td>
<td align="right">848,708,362</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,496,622,585</td>
<td align="right">1,466,350,398</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,734,961,301</td>
<td align="right">1,769,668,611</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">383,963,594</td>
<td align="right">376,479,187</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">385,190,854</td>
<td align="right">377,706,447</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,664,140</td>
<td align="right">53,605,441</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,657,540</td>
<td align="right">53,601,501</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">576,136,083</td>
<td align="right">565,604,664</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,409,276</td>
<td align="right">233,508,824</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">322,731,904</td>
<td align="right">328,494,667</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,557,914,600</td>
<td align="right">1,531,650,182</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,799,640</td>
<td align="right">1,771,240</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">950,289,974</td>
<td align="right">935,335,684</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,980</td>
<td align="right">5,548,420</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">225,089,604</td>
<td align="right">228,473,322</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,597,105</td>
<td align="right">28,008,743</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">396,464,311</td>
<td align="right">390,719,797</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,342,956,687</td>
<td align="right">2,309,529,431</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,529,974,748</td>
<td align="right">4,466,895,078</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">254,307,704</td>
<td align="right">250,845,492</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,058,027,636</td>
<td align="right">1,043,661,018</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">48,009,284</td>
<td align="right">47,394,617</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">166,792,900</td>
<td align="right">164,661,869</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">8,400,393</td>
<td align="right">8,507,270</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,062,878</td>
<td align="right">35,479,644</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">538,013,280</td>
<td align="right">531,777,440</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,102,565,267</td>
<td align="right">1,089,921,359</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">843,484,718</td>
<td align="right">853,058,688</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,015,393,524</td>
<td align="right">2,038,095,034</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,741,377,526</td>
<td align="right">1,722,745,939</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,331,186,980</td>
<td align="right">3,365,158,202</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,372,744,172</td>
<td align="right">2,348,726,505</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,837,227,911</td>
<td align="right">2,809,832,412</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">238,874,960</td>
<td align="right">236,661,711</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">991,823,422</td>
<td align="right">982,897,888</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,650,660</td>
<td align="right">5,601,680</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">609,155,425</td>
<td align="right">603,883,609</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">416,029,956</td>
<td align="right">412,520,514</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">465,745,596</td>
<td align="right">461,960,117</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,719,960,059</td>
<td align="right">2,741,590,288</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">967,925,784</td>
<td align="right">960,312,930</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,630,694,498</td>
<td align="right">3,602,435,271</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,353,755,941</td>
<td align="right">1,343,255,239</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,820,771,403</td>
<td align="right">1,834,890,454</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,659,158,686</td>
<td align="right">3,631,053,630</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">704,516</td>
<td align="right">699,285</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,688,800</td>
<td align="right">12,595,980</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">119,222,600</td>
<td align="right">120,006,786</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,670,879</td>
<td align="right">986,240,098</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,700,400</td>
<td align="right">32,489,700</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">891,847,665</td>
<td align="right">886,422,326</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,907,332,393</td>
<td align="right">2,890,317,157</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,364,679</td>
<td align="right">85,866,689</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">64,772,564</td>
<td align="right">64,422,228</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,727,021</td>
<td align="right">13,801,248</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,727,021</td>
<td align="right">13,801,248</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">870,172,196</td>
<td align="right">865,479,298</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,127,168,590</td>
<td align="right">1,121,313,617</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,544,385</td>
<td align="right">95,001,643</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,995,166</td>
<td align="right">79,315,565</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,631,470,446</td>
<td align="right">9,593,154,065</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,102,567,169</td>
<td align="right">1,098,250,778</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">438,275,344</td>
<td align="right">436,563,222</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,150,326</td>
<td align="right">162,524,198</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,595,911,070</td>
<td align="right">1,601,841,183</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,601,276,670</td>
<td align="right">5,580,741,422</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">902,786,136</td>
<td align="right">905,990,211</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">675,937,470</td>
<td align="right">673,544,748</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">831,615,619</td>
<td align="right">828,766,568</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,290,988,755</td>
<td align="right">2,298,769,572</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">111,513,239</td>
<td align="right">111,878,033</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">110,151,804</td>
<td align="right">109,838,877</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,828,443,427</td>
<td align="right">1,823,681,035</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">95,449,532</td>
<td align="right">95,684,227</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,866,588</td>
<td align="right">210,373,782</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,441,474,605</td>
<td align="right">1,438,611,496</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,250,351,269</td>
<td align="right">1,247,913,925</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,029,007,844</td>
<td align="right">3,023,205,067</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">557,006,008</td>
<td align="right">555,979,769</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,893,254</td>
<td align="right">97,717,498</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">691,631,990</td>
<td align="right">690,442,054</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,280,467</td>
<td align="right">4,273,615</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,857,677,598</td>
<td align="right">1,854,824,051</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,793,431</td>
<td align="right">161,035,725</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,521,271,255</td>
<td align="right">2,517,743,899</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,732,865</td>
<td align="right">350,258,172</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,855,317,613</td>
<td align="right">2,851,473,357</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,016,240</td>
<td align="right">3,012,960</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,287,186</td>
<td align="right">163,430,261</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,027,169,901</td>
<td align="right">2,028,929,157</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">98,894,461</td>
<td align="right">98,814,278</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,942,561</td>
<td align="right">98,862,378</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,874,858</td>
<td align="right">3,872,102</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,167,808,419</td>
<td align="right">5,170,847,049</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,431,684</td>
<td align="right">198,536,891</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">238,562,549</td>
<td align="right">238,457,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,482,689</td>
<td align="right">733,178,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">780,172,797</td>
<td align="right">779,873,731</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">55,262,500</td>
<td align="right">55,283,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,472,669</td>
<td align="right">603,249,416</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">557,752,500</td>
<td align="right">557,560,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,505,936</td>
<td align="right">1,505,450</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,320,687</td>
<td align="right">518,154,595</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,920,900</td>
<td align="right">154,880,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,627,677</td>
<td align="right">780,437,551</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,552,908</td>
<td align="right">1,552,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,822,481</td>
<td align="right">32,817,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,704,660</td>
<td align="right">532,635,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,995,600</td>
<td align="right">1,995,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,389,418</td>
<td align="right">90,382,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,009,260</td>
<td align="right">81,004,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,778,260</td>
<td align="right">57,777,360</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">131,769,148</td>
<td align="right">131,768,678</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
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
<td align="right">581,940</td>
<td align="right">581,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">375,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right">78,400</td>
<td align="right">78,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
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
<td align="right">1,560</td>
<td align="right">11,880</td>
<td align="right">661.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">158,503</td>
<td align="right">130,484</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">920</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">36,411</td>
<td align="right">38,544</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,560</td>
<td align="right">34,400</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,662</td>
<td align="right">44,866</td>
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
<td align="right">1,106</td>
<td align="right">1,108</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,106</td>
<td align="right">1,108</td>
<td align="right">0.2%</td>
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
<td align="right">1,820</td>
<td align="right">1,820</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-02
