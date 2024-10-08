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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,333,950</td>
<td align="right">105,930,152</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">80</td>
<td align="right">100</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">107,903,679</td>
<td align="right">128,930,264</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,507,858</td>
<td align="right">2,841,620</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,165,849</td>
<td align="right">197,255,098</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">93,298,956</td>
<td align="right">79,281,793</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,886,971</td>
<td align="right">2,462,792</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">394,846,526</td>
<td align="right">443,067,325</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">260,856,675</td>
<td align="right">233,553,650</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">136,996,459</td>
<td align="right">123,734,925</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,658,994</td>
<td align="right">30,259,555</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">250,865,133</td>
<td align="right">237,729,568</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">182,293</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,660,312,267</td>
<td align="right">1,578,015,137</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,117,852</td>
<td align="right">261,518,627</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">280,603,598</td>
<td align="right">266,846,395</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">69,482,384</td>
<td align="right">72,718,054</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,575,199</td>
<td align="right">108,331,247</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">410,100,866</td>
<td align="right">396,734,191</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,184,608</td>
<td align="right">15,659,170</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">435,359,248</td>
<td align="right">421,278,750</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,344,479</td>
<td align="right">54,662,398</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">58,913,723</td>
<td align="right">57,427,417</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,535,704</td>
<td align="right">138,037,825</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,464,283</td>
<td align="right">4,361,581</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">15,800</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,574,722</td>
<td align="right">58,700,816</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,538,794</td>
<td align="right">8,411,009</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,313,435,677</td>
<td align="right">1,293,830,225</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,950,234,151</td>
<td align="right">1,921,440,778</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,648,087,546</td>
<td align="right">3,594,564,495</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,725,501,829</td>
<td align="right">3,674,830,107</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,346,807,382</td>
<td align="right">4,290,329,841</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">956,407,156</td>
<td align="right">968,684,452</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,463,400,258</td>
<td align="right">2,435,530,572</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">189,574,553</td>
<td align="right">191,704,844</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,337,103</td>
<td align="right">136,810,446</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">340,732,389</td>
<td align="right">344,409,308</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,309</td>
<td align="right">2,923,545</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,220,800,914</td>
<td align="right">2,197,635,273</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">71,162,210</td>
<td align="right">70,495,813</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,587</td>
<td align="right">3,710,161</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,713,447,387</td>
<td align="right">3,680,504,390</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,606,375,349</td>
<td align="right">4,565,511,368</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,062,117</td>
<td align="right">21,869,899</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,221,632</td>
<td align="right">36,532,378</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">305,370,875</td>
<td align="right">307,964,212</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">187,438,566</td>
<td align="right">185,885,160</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">154,145,301</td>
<td align="right">155,381,981</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,563,478,712</td>
<td align="right">4,528,158,400</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">763,376</td>
<td align="right">768,876</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">370,140,957</td>
<td align="right">367,545,588</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,031,964,011</td>
<td align="right">1,038,047,566</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,607,287,294</td>
<td align="right">2,592,109,701</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,576,970,887</td>
<td align="right">2,591,250,130</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">52,704,627</td>
<td align="right">52,992,110</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,519,623</td>
<td align="right">7,559,323</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,740,390,796</td>
<td align="right">15,661,881,074</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,623,587</td>
<td align="right">43,411,633</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">28,212,110</td>
<td align="right">28,346,167</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,480,673</td>
<td align="right">71,820,313</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,254,124</td>
<td align="right">45,462,452</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,053,111,781</td>
<td align="right">1,057,896,372</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">745,182,838</td>
<td align="right">748,248,396</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">52,077,621</td>
<td align="right">51,884,029</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">586,048,573</td>
<td align="right">588,036,594</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,618,786</td>
<td align="right">103,965,965</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,775,681</td>
<td align="right">18,837,959</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,628,567</td>
<td align="right">53,452,681</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">331,590,915</td>
<td align="right">330,508,451</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">534,576,682</td>
<td align="right">536,173,703</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">197,873,513</td>
<td align="right">197,290,362</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">119,985,579</td>
<td align="right">120,325,310</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,579,972</td>
<td align="right">33,486,846</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">265,328,025</td>
<td align="right">266,063,366</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,028,553</td>
<td align="right">49,894,634</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">28,214,682</td>
<td align="right">28,139,931</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,209,111</td>
<td align="right">9,233,178</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">103,409,829</td>
<td align="right">103,143,735</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">77,160,129</td>
<td align="right">77,355,837</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,108,786</td>
<td align="right">181,558,171</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">141,978,129</td>
<td align="right">142,316,769</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,169,763</td>
<td align="right">53,047,539</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,718,893</td>
<td align="right">8,699,089</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,017,370</td>
<td align="right">56,136,203</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">301,834,479</td>
<td align="right">302,470,650</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">618,155,320</td>
<td align="right">616,860,379</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">566,444,172</td>
<td align="right">565,307,744</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">524,790</td>
<td align="right">523,745</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">742,497,352</td>
<td align="right">741,037,888</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">765,794,353</td>
<td align="right">764,320,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">76,064,797</td>
<td align="right">76,193,016</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">533,325,938</td>
<td align="right">534,222,653</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,383,998</td>
<td align="right">37,323,114</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">357,055,484</td>
<td align="right">357,629,709</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,686</td>
<td align="right">27,726</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">354,413,092</td>
<td align="right">354,921,340</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,931,982</td>
<td align="right">14,953,090</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">127,201,188</td>
<td align="right">127,030,306</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">453,710,408</td>
<td align="right">453,134,526</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,831,031,980</td>
<td align="right">1,828,837,444</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,248,303</td>
<td align="right">196,044,671</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">119,859,583</td>
<td align="right">119,981,612</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,450,742</td>
<td align="right">47,498,532</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,263,087,535</td>
<td align="right">2,260,811,037</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">338,859,618</td>
<td align="right">339,196,147</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,953,716</td>
<td align="right">90,865,185</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,205,847</td>
<td align="right">107,111,087</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">157,962,910</td>
<td align="right">158,098,805</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">720,489</td>
<td align="right">721,074</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">61,497,107</td>
<td align="right">61,450,546</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">150,503,365</td>
<td align="right">150,612,094</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">367,548,883</td>
<td align="right">367,309,541</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">238,933,970</td>
<td align="right">239,087,464</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,388,062</td>
<td align="right">21,375,033</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,396,403</td>
<td align="right">21,383,373</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,081,901</td>
<td align="right">21,069,151</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">823,244,817</td>
<td align="right">822,755,747</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,220,141</td>
<td align="right">198,335,777</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">99,103,548</td>
<td align="right">99,047,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,141,273</td>
<td align="right">83,095,207</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">642,892</td>
<td align="right">642,552</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">183,238,003</td>
<td align="right">183,329,887</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,859,888,019</td>
<td align="right">2,858,573,895</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">231,701,094</td>
<td align="right">231,788,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,422,444</td>
<td align="right">10,418,872</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,258,115</td>
<td align="right">11,254,597</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,037,937</td>
<td align="right">1,371,610,961</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">239,211</td>
<td align="right">239,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">468,645,672</td>
<td align="right">468,782,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,653,986,163</td>
<td align="right">1,654,452,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,585,982</td>
<td align="right">3,585,019</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">197,258,448</td>
<td align="right">197,302,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,701</td>
<td align="right">43,458,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,034,937</td>
<td align="right">9,036,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">219,844,821</td>
<td align="right">219,888,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">62,071,546</td>
<td align="right">62,083,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,170,874</td>
<td align="right">33,164,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,862,793</td>
<td align="right">91,879,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,946,296</td>
<td align="right">70,933,599</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,261,988</td>
<td align="right">1,262,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">189,694,813</td>
<td align="right">189,712,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,238</td>
<td align="right">268,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,067,676</td>
<td align="right">44,070,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,996,060</td>
<td align="right">10,996,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,420,601</td>
<td align="right">93,424,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,449,459</td>
<td align="right">474,429,217</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,113,846</td>
<td align="right">102,109,532</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,829,439</td>
<td align="right">5,829,245</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,558,651</td>
<td align="right">402,568,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,001,263</td>
<td align="right">146,998,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">134,319,738</td>
<td align="right">134,317,738</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">65,073,249</td>
<td align="right">65,072,315</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,029,928</td>
<td align="right">35,029,474</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">197,308,884</td>
<td align="right">197,306,974</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,948</td>
<td align="right">3,464,928</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,356,125</td>
<td align="right">20,356,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,337,503</td>
<td align="right">10,337,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,191,763</td>
<td align="right">150,191,263</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">88,068,929</td>
<td align="right">88,069,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">262,499,283</td>
<td align="right">262,499,487</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,131</td>
<td align="right">268,166,333</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,398,826</td>
<td align="right">173,398,742</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,460,945</td>
<td align="right">82,460,974</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,783</td>
<td align="right">225,010,861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,980</td>
<td align="right">402,103,934</td>
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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,868,298</td>
<td align="right">10,868,298</td>
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
<td align="left">UNPACK_EX</td>
<td align="right">552,520</td>
<td align="right">552,520</td>
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
<td align="left">CALL_KW</td>
<td align="right">66,756</td>
<td align="right">66,756</td>
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
<td align="right">29,249</td>
<td align="right">29,249</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,656</td>
<td align="right">21,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,165</td>
<td align="right">15,165</td>
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
<td align="right">1,122</td>
<td align="right">1,122</td>
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
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3</td>
<td align="right">3</td>
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
<td align="right">368,982,134</td>
<td align="right">3.8%</td>
<td align="right">366,387,386</td>
<td align="right">3.7%</td>
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
<td align="right">9,415,858,801</td>
<td align="right">95.9%</td>
<td align="right">9,415,506,617</td>
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
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">29,480,870</td>
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
<td align="right">1,116,372</td>
<td align="right">65.1%</td>
<td align="right">1,115,725</td>
<td align="right">65.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598,531</td>
<td align="right">34.9%</td>
<td align="right">598,557</td>
<td align="right">34.9%</td>
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
<td align="left">or</td>
<td align="right">14,487</td>
<td align="right">1.3%</td>
<td align="right">14,251</td>
<td align="right">1.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,531</td>
<td align="right">2.8%</td>
<td align="right">31,113</td>
<td align="right">2.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,723</td>
<td align="right">0.2%</td>
<td align="right">2,742</td>
<td align="right">0.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">19,978</td>
<td align="right">1.8%</td>
<td align="right">20,044</td>
<td align="right">1.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,465</td>
<td align="right">0.8%</td>
<td align="right">8,448</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">835</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,599</td>
<td align="right">0.5%</td>
<td align="right">5,605</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,190</td>
<td align="right">4.4%</td>
<td align="right">49,155</td>
<td align="right">4.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,701</td>
<td align="right">2.8%</td>
<td align="right">31,684</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,037</td>
<td align="right">4.2%</td>
<td align="right">47,018</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,827</td>
<td align="right">0.3%</td>
<td align="right">2,828</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,821</td>
<td align="right">1.0%</td>
<td align="right">10,823</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,722</td>
<td align="right">0.6%</td>
<td align="right">6,723</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,548</td>
<td align="right">0.8%</td>
<td align="right">8,547</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,581</td>
<td align="right">7.3%</td>
<td align="right">81,584</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,603</td>
<td align="right">70.0%</td>
<td align="right">781,602</td>
<td align="right">70.1%</td>
<td align="right">-0.0%</td>
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
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,580</td>
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
<td align="right">181,108,786</td>
<td align="right">100.0%</td>
<td align="right">181,558,171</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,411</td>
<td align="right">0.1%</td>
<td align="right">4,797,665</td>
<td align="right">0.1%</td>
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
<td align="right">474,179,536</td>
<td align="right">7.1%</td>
<td align="right">474,160,050</td>
<td align="right">7.1%</td>
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
<td align="right">6,201,948,173</td>
<td align="right">92.8%</td>
<td align="right">6,201,742,506</td>
<td align="right">92.8%</td>
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
<td align="right">178,276</td>
<td align="right">49.5%</td>
<td align="right">177,516</td>
<td align="right">49.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,608</td>
<td align="right">50.5%</td>
<td align="right">181,712</td>
<td align="right">50.6%</td>
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
<td align="left">out of range</td>
<td align="right">58,346</td>
<td align="right">32.7%</td>
<td align="right">57,585</td>
<td align="right">32.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,332</td>
<td align="right">12.0%</td>
<td align="right">21,285</td>
<td align="right">12.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,356</td>
<td align="right">36.7%</td>
<td align="right">65,403</td>
<td align="right">36.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">14.9%</td>
<td align="right">26,640</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">149,957,046</td>
<td align="right">1.1%</td>
<td align="right">144,961,226</td>
<td align="right">1.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
<td align="right">0.0%</td>
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
<td align="right">716,638</td>
<td align="right">0.0%</td>
<td align="right">716,754</td>
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
<td align="right">13,535,277,811</td>
<td align="right">98.9%</td>
<td align="right">13,533,981,239</td>
<td align="right">98.9%</td>
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
<td align="right">3,407,133</td>
<td align="right">100.0%</td>
<td align="right">3,312,940</td>
<td align="right">100.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">363</td>
<td align="right">0.0%</td>
<td align="right">363</td>
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
<td align="left">init not inline values</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">100.0%</td>
<td align="right">363</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">437,080</td>
<td align="right">86.8%</td>
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
<td align="right">36,409</td>
<td align="right">7.3%</td>
<td align="right">36,411</td>
<td align="right">7.2%</td>
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
<td align="right">103,412,236</td>
<td align="right">1.8%</td>
<td align="right">103,759,147</td>
<td align="right">1.8%</td>
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
<td align="right">1,026,714</td>
<td align="right">0.0%</td>
<td align="right">1,028,129</td>
<td align="right">0.0%</td>
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
<td align="right">5,733,823,690</td>
<td align="right">98.2%</td>
<td align="right">5,732,597,911</td>
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
<td align="right">151,285</td>
<td align="right">67.1%</td>
<td align="right">151,552</td>
<td align="right">67.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">74,299</td>
<td align="right">32.9%</td>
<td align="right">74,336</td>
<td align="right">32.9%</td>
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
<td align="left">bool</td>
<td align="right">1,538</td>
<td align="right">1.0%</td>
<td align="right">1,562</td>
<td align="right">1.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,189</td>
<td align="right">12.7%</td>
<td align="right">19,349</td>
<td align="right">12.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,540</td>
<td align="right">2.3%</td>
<td align="right">3,520</td>
<td align="right">2.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">38,365</td>
<td align="right">25.4%</td>
<td align="right">38,564</td>
<td align="right">25.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">29,773</td>
<td align="right">19.7%</td>
<td align="right">29,713</td>
<td align="right">19.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,512</td>
<td align="right">9.6%</td>
<td align="right">14,483</td>
<td align="right">9.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,102</td>
<td align="right">8.0%</td>
<td align="right">12,096</td>
<td align="right">8.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,416</td>
<td align="right">11.5%</td>
<td align="right">17,415</td>
<td align="right">11.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">490</td>
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
<td align="right">36,137,034</td>
<td align="right">1.4%</td>
<td align="right">36,447,368</td>
<td align="right">1.4%</td>
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
<td align="right">2,486,643,490</td>
<td align="right">98.5%</td>
<td align="right">2,486,139,217</td>
<td align="right">98.5%</td>
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
<td align="right">2,544,260</td>
<td align="right">0.1%</td>
<td align="right">2,544,100</td>
<td align="right">0.1%</td>
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
<td align="right">71,419</td>
<td align="right">53.9%</td>
<td align="right">71,831</td>
<td align="right">54.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,099</td>
<td align="right">46.1%</td>
<td align="right">61,099</td>
<td align="right">46.0%</td>
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
<td align="right">14,522</td>
<td align="right">20.3%</td>
<td align="right">14,702</td>
<td align="right">20.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,470</td>
<td align="right">20.3%</td>
<td align="right">14,550</td>
<td align="right">20.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,151</td>
<td align="right">38.0%</td>
<td align="right">27,257</td>
<td align="right">37.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,276</td>
<td align="right">21.4%</td>
<td align="right">15,322</td>
<td align="right">21.3%</td>
<td align="right">0.3%</td>
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
<td align="right">6,738,018</td>
<td align="right">1.1%</td>
<td align="right">29,342,780</td>
<td align="right">4.4%</td>
<td align="right">335.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">533,331,558</td>
<td align="right">86.4%</td>
<td align="right">558,552,094</td>
<td align="right">84.0%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,009,322</td>
<td align="right">12.5%</td>
<td align="right">77,204,966</td>
<td align="right">11.6%</td>
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
<td align="left">Success</td>
<td align="right">175,733</td>
<td align="right">63.3%</td>
<td align="right">602,196</td>
<td align="right">85.5%</td>
<td align="right">242.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">101,905</td>
<td align="right">36.7%</td>
<td align="right">101,979</td>
<td align="right">14.5%</td>
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
<td align="left">seq iter</td>
<td align="right">3,981</td>
<td align="right">3.9%</td>
<td align="right">3,941</td>
<td align="right">3.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">616</td>
<td align="right">0.6%</td>
<td align="right">614</td>
<td align="right">0.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">6.6%</td>
<td align="right">6,717</td>
<td align="right">6.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,672</td>
<td align="right">36.0%</td>
<td align="right">36,768</td>
<td align="right">36.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,373</td>
<td align="right">11.2%</td>
<td align="right">11,397</td>
<td align="right">11.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,070</td>
<td align="right">10.9%</td>
<td align="right">11,086</td>
<td align="right">10.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,602</td>
<td align="right">7.5%</td>
<td align="right">7,602</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,625</td>
<td align="right">6.5%</td>
<td align="right">6,625</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">5.1%</td>
<td align="right">5,222</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,936</td>
<td align="right">4.8%</td>
<td align="right">4,936</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,484</td>
<td align="right">3.4%</td>
<td align="right">3,484</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">280</td>
<td align="right">0.3%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,289,180</td>
<td align="right">0.0%</td>
<td align="right">1,557,760</td>
<td align="right">0.0%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">320,065,302</td>
<td align="right">2.0%</td>
<td align="right">364,963,215</td>
<td align="right">2.2%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,541,652,771</td>
<td align="right">95.2%</td>
<td align="right">15,573,238,357</td>
<td align="right">94.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">466,517,227</td>
<td align="right">2.9%</td>
<td align="right">466,635,413</td>
<td align="right">2.8%</td>
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
<td align="right">7,673,095</td>
<td align="right">94.3%</td>
<td align="right">8,539,407</td>
<td align="right">94.9%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">459,616</td>
<td align="right">5.7%</td>
<td align="right">459,274</td>
<td align="right">5.1%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
<td align="right">1,120</td>
<td align="right">0.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,543</td>
<td align="right">0.6%</td>
<td align="right">2,502</td>
<td align="right">0.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,755</td>
<td align="right">0.6%</td>
<td align="right">2,714</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,280</td>
<td align="right">3.3%</td>
<td align="right">15,166</td>
<td align="right">3.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,924</td>
<td align="right">0.6%</td>
<td align="right">2,944</td>
<td align="right">0.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">31,224</td>
<td align="right">6.8%</td>
<td align="right">31,406</td>
<td align="right">6.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">84,144</td>
<td align="right">18.3%</td>
<td align="right">83,958</td>
<td align="right">18.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">88,020</td>
<td align="right">19.2%</td>
<td align="right">87,828</td>
<td align="right">19.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,969</td>
<td align="right">3.3%</td>
<td align="right">14,989</td>
<td align="right">3.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,603</td>
<td align="right">30.2%</td>
<td align="right">138,757</td>
<td align="right">30.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,880</td>
<td align="right">4.5%</td>
<td align="right">20,900</td>
<td align="right">4.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,281</td>
<td align="right">7.0%</td>
<td align="right">32,306</td>
<td align="right">7.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
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
<td align="right">4,512,723,471</td>
<td align="right">99.5%</td>
<td align="right">4,411,172,666</td>
<td align="right">99.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">391,104</td>
<td align="right">0.0%</td>
<td align="right">387,934</td>
<td align="right">0.0%</td>
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
<td align="right">19,894,779</td>
<td align="right">0.4%</td>
<td align="right">19,894,859</td>
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
<td align="right">9,234</td>
<td align="right">0.0%</td>
<td align="right">9,234</td>
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
<td align="right">467,046</td>
<td align="right">100.0%</td>
<td align="right">467,038</td>
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
<td align="right">86,070,017</td>
<td align="right">100.0%</td>
<td align="right">85,368,994</td>
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
<td align="right">7,624</td>
<td align="right">0.0%</td>
<td align="right">7,624</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,334,095</td>
<td align="right">18.1%</td>
<td align="right">173,334,011</td>
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
<td align="right">786,232,612</td>
<td align="right">81.9%</td>
<td align="right">786,232,570</td>
<td align="right">81.9%</td>
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
<td align="right">121,957,216</td>
<td align="right">4.6%</td>
<td align="right">125,860,259</td>
<td align="right">4.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,066,991</td>
<td align="right">1.7%</td>
<td align="right">45,275,878</td>
<td align="right">1.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,465,648,468</td>
<td align="right">93.6%</td>
<td align="right">2,464,954,278</td>
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
<td align="left">Success</td>
<td align="right">2,401,347</td>
<td align="right">96.6%</td>
<td align="right">2,475,264</td>
<td align="right">96.7%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">83,987</td>
<td align="right">3.4%</td>
<td align="right">83,208</td>
<td align="right">3.3%</td>
<td align="right">-0.9%</td>
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
<td align="left">not in dict</td>
<td align="right">17,045</td>
<td align="right">20.3%</td>
<td align="right">16,285</td>
<td align="right">19.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">3.8%</td>
<td align="right">3,085</td>
<td align="right">3.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,955</td>
<td align="right">5.9%</td>
<td align="right">4,935</td>
<td align="right">5.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,884</td>
<td align="right">38.0%</td>
<td align="right">31,984</td>
<td align="right">38.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,810</td>
<td align="right">11.7%</td>
<td align="right">9,811</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,363</td>
<td align="right">10.0%</td>
<td align="right">8,363</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">5,001</td>
<td align="right">6.0%</td>
<td align="right">5,001</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">0.9%</td>
<td align="right">780</td>
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
<td align="right">7,519,623</td>
<td align="right">100.0%</td>
<td align="right">7,559,323</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">875,193,754</td>
<td align="right">90.4%</td>
<td align="right">874,726,927</td>
<td align="right">90.3%</td>
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
<td align="right">93,340,508</td>
<td align="right">9.6%</td>
<td align="right">93,344,784</td>
<td align="right">9.6%</td>
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
<td align="right">66,761</td>
<td align="right">83.3%</td>
<td align="right">66,745</td>
<td align="right">83.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,372</td>
<td align="right">16.7%</td>
<td align="right">13,370</td>
<td align="right">16.7%</td>
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
<td align="right">640</td>
<td align="right">1.0%</td>
<td align="right">620</td>
<td align="right">0.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">1,500</td>
<td align="right">2.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,243</td>
<td align="right">63.3%</td>
<td align="right">42,225</td>
<td align="right">63.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,718</td>
<td align="right">10.1%</td>
<td align="right">6,720</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,160</td>
<td align="right">21.2%</td>
<td align="right">14,160</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
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
<td align="right">24,400,885</td>
<td align="right">0.4%</td>
<td align="right">29,883,817</td>
<td align="right">0.5%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">150,097,201</td>
<td align="right">2.5%</td>
<td align="right">150,202,918</td>
<td align="right">2.5%</td>
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
<td align="right">5,752,269,782</td>
<td align="right">97.0%</td>
<td align="right">5,753,199,798</td>
<td align="right">97.0%</td>
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
<td align="right">653,651</td>
<td align="right">75.9%</td>
<td align="right">757,013</td>
<td align="right">78.2%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">208,091</td>
<td align="right">24.1%</td>
<td align="right">211,088</td>
<td align="right">21.8%</td>
<td align="right">1.4%</td>
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
<td align="right">82,826</td>
<td align="right">39.8%</td>
<td align="right">85,657</td>
<td align="right">40.6%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,999</td>
<td align="right">2.9%</td>
<td align="right">6,032</td>
<td align="right">2.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">37,270</td>
<td align="right">17.9%</td>
<td align="right">37,455</td>
<td align="right">17.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">7,328</td>
<td align="right">3.5%</td>
<td align="right">7,309</td>
<td align="right">3.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,910</td>
<td align="right">7.2%</td>
<td align="right">14,877</td>
<td align="right">7.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,145</td>
<td align="right">7.8%</td>
<td align="right">16,165</td>
<td align="right">7.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21,710</td>
<td align="right">10.4%</td>
<td align="right">21,689</td>
<td align="right">10.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,131</td>
<td align="right">9.2%</td>
<td align="right">19,132</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">198,733</td>
<td align="right">0.0%</td>
<td align="right">198,803</td>
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
<td align="right">2,058,086,852</td>
<td align="right">100.0%</td>
<td align="right">2,057,474,883</td>
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
<td align="right">433,280</td>
<td align="right">0.0%</td>
<td align="right">433,280</td>
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
<td align="right">1,763</td>
<td align="right">3.6%</td>
<td align="right">1,762</td>
<td align="right">3.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46,735</td>
<td align="right">96.4%</td>
<td align="right">46,739</td>
<td align="right">96.4%</td>
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
<td align="right">1,116</td>
<td align="right">63.3%</td>
<td align="right">1,115</td>
<td align="right">63.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">267</td>
<td align="right">15.2%</td>
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
<td align="right">662,460,456</td>
<td align="right">0.7%</td>
<td align="right">734,409,520</td>
<td align="right">0.8%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,732,225,983</td>
<td align="right">33.8%</td>
<td align="right">30,470,379,798</td>
<td align="right">33.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,346,803,700</td>
<td align="right">63.1%</td>
<td align="right">57,030,060,669</td>
<td align="right">63.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,203,381,205</td>
<td align="right">2.4%</td>
<td align="right">2,202,566,875</td>
<td align="right">2.4%</td>
<td align="right">-0.0%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">368,982,134</td>
<td align="right">16.8%</td>
<td align="right">366,387,386</td>
<td align="right">16.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,066,991</td>
<td align="right">2.1%</td>
<td align="right">45,275,878</td>
<td align="right">2.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,412,236</td>
<td align="right">4.7%</td>
<td align="right">103,759,147</td>
<td align="right">4.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">77,009,322</td>
<td align="right">3.5%</td>
<td align="right">77,204,966</td>
<td align="right">3.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,108,786</td>
<td align="right">8.2%</td>
<td align="right">181,558,171</td>
<td align="right">8.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">150,097,201</td>
<td align="right">6.8%</td>
<td align="right">150,202,918</td>
<td align="right">6.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">466,517,227</td>
<td align="right">21.2%</td>
<td align="right">466,635,413</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,340,508</td>
<td align="right">4.2%</td>
<td align="right">93,344,784</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,179,536</td>
<td align="right">21.6%</td>
<td align="right">474,160,050</td>
<td align="right">21.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,095</td>
<td align="right">7.9%</td>
<td align="right">173,334,011</td>
<td align="right">7.9%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,280,504</td>
<td align="right">6.1%</td>
<td align="right">52,848,800</td>
<td align="right">7.2%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120,149,214</td>
<td align="right">18.1%</td>
<td align="right">145,217,906</td>
<td align="right">19.8%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,838,306</td>
<td align="right">3.6%</td>
<td align="right">27,082,830</td>
<td align="right">3.7%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">82,628,700</td>
<td align="right">12.5%</td>
<td align="right">88,468,503</td>
<td align="right">12.0%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,071,252</td>
<td align="right">5.7%</td>
<td align="right">40,079,928</td>
<td align="right">5.5%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">79,489,860</td>
<td align="right">12.0%</td>
<td align="right">75,939,563</td>
<td align="right">10.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">98,114,304</td>
<td align="right">14.8%</td>
<td align="right">98,772,824</td>
<td align="right">13.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,135,025</td>
<td align="right">2.7%</td>
<td align="right">18,093,653</td>
<td align="right">2.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,932</td>
<td align="right">4.1%</td>
<td align="right">27,496,781</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.0%</td>
<td align="right">20,177,240</td>
<td align="right">2.7%</td>
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
<td align="right">333,905,278</td>
<td align="right">4.0%</td>
<td align="right">332,644,564</td>
<td align="right">3.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,410,530,956</td>
<td align="right">16.7%</td>
<td align="right">1,408,331,048</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,414,978,637</td>
<td align="right">16.8%</td>
<td align="right">1,412,778,689</td>
<td align="right">16.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,684,676,491</td>
<td align="right">79.2%</td>
<td align="right">6,677,464,073</td>
<td align="right">79.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,266,903,453</td>
<td align="right">26.9%</td>
<td align="right">2,264,626,717</td>
<td align="right">26.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,266,903,453</td>
<td align="right">26.9%</td>
<td align="right">2,264,626,717</td>
<td align="right">26.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,168,366,911</td>
<td align="right">73.1%</td>
<td align="right">6,163,007,627</td>
<td align="right">73.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,754,719</td>
<td align="right">1.0%</td>
<td align="right">84,741,878</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,636,493</td>
<td align="right">3.9%</td>
<td align="right">331,600,100</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,924,816</td>
<td align="right">10.1%</td>
<td align="right">851,848,028</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,098,736</td>
<td align="right">0.4%</td>
<td align="right">31,097,561</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,012</td>
<td align="right">0.1%</td>
<td align="right">4,417,972</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,276</td>
<td align="right">2.1%</td>
<td align="right">175,480,272</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">29,669</td>
<td align="right">0.0%</td>
<td align="right">29,669</td>
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
<td align="left">Method cache misses</td>
<td align="right">69,772,053</td>
<td align="right"></td>
<td align="right">62,492,986</td>
<td align="right"></td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">124,604,671</td>
<td align="right"></td>
<td align="right">115,718,209</td>
<td align="right"></td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">58,349,759</td>
<td align="right"></td>
<td align="right">56,629,898</td>
<td align="right"></td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">98,041,458,383</td>
<td align="right">70.3%</td>
<td align="right">95,213,994,289</td>
<td align="right">69.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">105,618,021,547</td>
<td align="right">65.1%</td>
<td align="right">102,626,184,383</td>
<td align="right">64.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,391,904,750</td>
<td align="right"></td>
<td align="right">2,356,918,106</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">41,463,178,143</td>
<td align="right">29.7%</td>
<td align="right">41,272,793,763</td>
<td align="right">30.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">21,095,319</td>
<td align="right">0.1%</td>
<td align="right">21,053,275</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,668,367,332</td>
<td align="right"></td>
<td align="right">3,661,555,905</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">235,930,734</td>
<td align="right"></td>
<td align="right">235,504,479</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">56,723,699,450</td>
<td align="right">34.9%</td>
<td align="right">56,698,351,148</td>
<td align="right">35.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,064,684,521</td>
<td align="right">52.4%</td>
<td align="right">13,060,684,692</td>
<td align="right">52.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,189,386,658</td>
<td align="right">52.9%</td>
<td align="right">13,185,356,389</td>
<td align="right">52.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,765,055,836</td>
<td align="right">47.1%</td>
<td align="right">11,762,619,666</td>
<td align="right">47.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,766,929,659</td>
<td align="right"></td>
<td align="right">11,764,557,706</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,606,818</td>
<td align="right">0.4%</td>
<td align="right">103,618,422</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,956,654,138</td>
<td align="right"></td>
<td align="right">13,957,021,677</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,160</td>
<td align="right">1.4%</td>
<td align="right">3,382,160</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">198,360</td>
<td align="right">0.1%</td>
<td align="right">198,360</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">16,243</td>
<td align="right">0.0%</td>
<td align="right">16,243</td>
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
<td align="right">453,966</td>
<td align="right">112,212,307</td>
<td align="right">19,099,975,281</td>
<td align="right">796,197</td>
<td align="right">114,403,702</td>
<td align="right">23,898,072,544</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,959,114,560</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,958,751,240</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,466,086,299</td>
<td align="right"></td>
<td align="right">6,359,079,932</td>
<td align="right"></td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,741</td>
<td align="right">0.4%</td>
<td align="right">4,925</td>
<td align="right">0.5%</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">180,153</td>
<td align="right">19.9%</td>
<td align="right">216,342</td>
<td align="right">21.5%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,022</td>
<td align="right">0.1%</td>
<td align="right">1,141</td>
<td align="right">0.1%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">906,691</td>
<td align="right"></td>
<td align="right">1,006,766</td>
<td align="right"></td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">661,832</td>
<td align="right">73.0%</td>
<td align="right">730,953</td>
<td align="right">72.6%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">724,642</td>
<td align="right">79.9%</td>
<td align="right">788,502</td>
<td align="right">78.3%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,167</td>
<td align="right">1.3%</td>
<td align="right">12,929</td>
<td align="right">1.3%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">9,475</td>
<td align="right">5.3%</td>
<td align="right">9,159</td>
<td align="right">4.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">1,922</td>
<td align="right">0.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">306,093,866,498</td>
<td align="right">3,233.6%</td>
<td align="right">302,095,160,364</td>
<td align="right">4,750.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">580</td>
<td align="right">0.1%</td>
<td align="right">580</td>
<td align="right">0.1%</td>
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
<td align="right">168,354</td>
<td align="right">93.5%</td>
<td align="right">202,904</td>
<td align="right">93.8%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">180,153</td>
<td align="right"></td>
<td align="right">216,342</td>
<td align="right"></td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,560</td>
<td align="right">1.4%</td>
<td align="right">2,651</td>
<td align="right">1.2%</td>
<td align="right">3.6%</td>
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
<td align="right">3,715</td>
<td align="right">2.1%</td>
<td align="right">3,360</td>
<td align="right">1.6%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">23,274</td>
<td align="right">12.9%</td>
<td align="right">25,913</td>
<td align="right">12.0%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,941</td>
<td align="right">11.6%</td>
<td align="right">32,086</td>
<td align="right">14.8%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">48,705</td>
<td align="right">27.0%</td>
<td align="right">60,072</td>
<td align="right">27.8%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">41,014</td>
<td align="right">22.8%</td>
<td align="right">46,414</td>
<td align="right">21.5%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24,168</td>
<td align="right">13.4%</td>
<td align="right">26,619</td>
<td align="right">12.3%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,836</td>
<td align="right">8.2%</td>
<td align="right">17,780</td>
<td align="right">8.2%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,880</td>
<td align="right">1.6%</td>
<td align="right">3,458</td>
<td align="right">1.6%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">3.2%</td>
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
<td align="right">20,144</td>
<td align="right">11.2%</td>
<td align="right">20,248</td>
<td align="right">9.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,895</td>
<td align="right">9.4%</td>
<td align="right">26,888</td>
<td align="right">12.4%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">31,217</td>
<td align="right">17.3%</td>
<td align="right">40,902</td>
<td align="right">18.9%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50,477</td>
<td align="right">28.0%</td>
<td align="right">57,624</td>
<td align="right">26.6%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,055</td>
<td align="right">16.7%</td>
<td align="right">34,331</td>
<td align="right">15.9%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,786</td>
<td align="right">7.7%</td>
<td align="right">16,189</td>
<td align="right">7.5%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,780</td>
<td align="right">2.7%</td>
<td align="right">5,642</td>
<td align="right">2.6%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">980</td>
<td align="right">0.5%</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">8.2%</td>
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
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">114,601,053</td>
<td align="right">179,937,881</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">167,207,329</td>
<td align="right">237,782,865</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,472,029,619</td>
<td align="right">5,356,727,108</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,466,086,299</td>
<td align="right">6,359,079,932</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,895,008,034</td>
<td align="right">3,604,005,166</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,951,640</td>
<td align="right">5,564,080</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">24,448,572</td>
<td align="right">20,005,009</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">48,952,985</td>
<td align="right">56,725,024</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,949,560</td>
<td align="right">2,607,080</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">2,106,285</td>
<td align="right">1,872,518</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">865,322,910</td>
<td align="right">774,041,118</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">658,309,824</td>
<td align="right">594,022,887</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,230,920</td>
<td align="right">2,033,800</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,611,816</td>
<td align="right">13,699,318</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,490,261,205</td>
<td align="right">2,700,849,972</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">304,256,837</td>
<td align="right">329,222,667</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,220,003</td>
<td align="right">57,717,898</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,224,243</td>
<td align="right">57,722,118</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">204,279,302</td>
<td align="right">191,515,794</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,715,800</td>
<td align="right">5,372,460</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">845,106,005</td>
<td align="right">796,443,810</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,263,223,735</td>
<td align="right">8,724,755,495</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">37,717,404</td>
<td align="right">35,686,076</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">39,166,464</td>
<td align="right">37,102,776</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">529,636,404</td>
<td align="right">503,844,351</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,626,340</td>
<td align="right">608,618,220</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,639,944</td>
<td align="right">2,764,092</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">359,290,109</td>
<td align="right">375,737,164</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">10,164</td>
<td align="right">9,704</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">351,212,620</td>
<td align="right">365,481,875</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">366,165,666</td>
<td align="right">380,403,732</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">353,764,826</td>
<td align="right">367,226,256</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">362,400</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">132,815,949</td>
<td align="right">128,465,176</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,073,377</td>
<td align="right">37,941,212</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">947,059,279</td>
<td align="right">919,634,625</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">476,476,662</td>
<td align="right">490,168,242</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,069,573,363</td>
<td align="right">1,097,501,895</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,049,808,092</td>
<td align="right">1,076,450,645</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">108,181,473</td>
<td align="right">110,796,341</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">307,662,280</td>
<td align="right">300,645,403</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,789,067,804</td>
<td align="right">1,823,655,888</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,779,952,504</td>
<td align="right">1,814,332,179</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">112,959,255</td>
<td align="right">115,093,494</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,883,051</td>
<td align="right">59,732,831</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">770,549,808</td>
<td align="right">783,903,375</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,757,145,886</td>
<td align="right">3,692,947,525</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,652,264,609</td>
<td align="right">1,680,181,370</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">245,515,014</td>
<td align="right">241,435,762</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">341,651,334</td>
<td align="right">336,361,636</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">953,734,421</td>
<td align="right">968,092,624</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,116,199,596</td>
<td align="right">2,147,585,787</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">891,516,628</td>
<td align="right">904,348,308</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">68,680,740</td>
<td align="right">67,700,598</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">50,304,988</td>
<td align="right">51,022,282</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">979,797,426</td>
<td align="right">993,190,486</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,261,891</td>
<td align="right">136,066,831</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">388,308,682</td>
<td align="right">383,151,571</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,081,263,122</td>
<td align="right">2,054,255,208</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,640,194,825</td>
<td align="right">25,966,405,167</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,165,325,094</td>
<td align="right">2,191,248,858</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,376,594,264</td>
<td align="right">2,348,349,837</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,390,325,840</td>
<td align="right">2,362,264,604</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,555,292,396</td>
<td align="right">3,594,304,431</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,427,063,791</td>
<td align="right">2,453,253,792</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,446,895,092</td>
<td align="right">4,491,273,391</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,299,931,333</td>
<td align="right">2,277,225,024</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,417,625</td>
<td align="right">9,324,794</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,423,120,434</td>
<td align="right">1,436,969,459</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,161,211,644</td>
<td align="right">3,190,540,476</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,413,538,749</td>
<td align="right">2,435,163,175</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,418,439,495</td>
<td align="right">1,430,582,309</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,699,918,989</td>
<td align="right">1,713,517,909</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">238,390,003</td>
<td align="right">236,487,646</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,268,189,717</td>
<td align="right">5,308,994,798</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">171,276,320</td>
<td align="right">169,982,905</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,738,573,054</td>
<td align="right">1,751,646,572</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">247,046,401</td>
<td align="right">248,849,346</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,564,888,207</td>
<td align="right">3,590,182,314</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,513,422,519</td>
<td align="right">3,538,151,064</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,904,564</td>
<td align="right">8,847,264</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,467,298</td>
<td align="right">6,508,703</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">6,553,395,599</td>
<td align="right">6,593,062,287</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,844,246,131</td>
<td align="right">3,866,422,488</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">451,898,926</td>
<td align="right">449,298,222</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,896</td>
<td align="right">5,441,700</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,733,450,209</td>
<td align="right">14,816,901,902</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">44,427,020</td>
<td align="right">44,176,284</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">44,427,020</td>
<td align="right">44,176,284</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">43,496,542</td>
<td align="right">43,262,681</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">42,811,122</td>
<td align="right">42,601,721</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,587,500</td>
<td align="right">5,560,700</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">469,239,481</td>
<td align="right">467,165,877</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,196,754,749</td>
<td align="right">8,232,909,183</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,670,076,189</td>
<td align="right">5,694,929,277</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">698,652,793</td>
<td align="right">695,592,721</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,117,166,457</td>
<td align="right">1,121,826,691</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">153,858,167</td>
<td align="right">153,226,884</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,319,901,615</td>
<td align="right">1,325,113,664</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,292,002</td>
<td align="right">32,169,381</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">160,116,715</td>
<td align="right">160,714,921</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">36,438,382</td>
<td align="right">36,566,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">217,667,214</td>
<td align="right">216,906,294</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,360,246,331</td>
<td align="right">10,395,966,587</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">89,336,926</td>
<td align="right">89,030,701</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">114,745,104</td>
<td align="right">115,125,826</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,352,462,158</td>
<td align="right">21,285,704,036</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">205,794,368</td>
<td align="right">205,162,506</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,215,682,190</td>
<td align="right">1,211,984,466</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,740,142,976</td>
<td align="right">3,728,906,539</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">837,936,400</td>
<td align="right">835,419,069</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,709,693</td>
<td align="right">122,354,413</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">893,634,507</td>
<td align="right">891,200,318</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,064,281,361</td>
<td align="right">1,067,161,896</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">290,634,359</td>
<td align="right">289,874,054</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,226,568,094</td>
<td align="right">8,247,439,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">84,042,601</td>
<td align="right">84,251,241</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,699,065</td>
<td align="right">112,970,586</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">56,752,437</td>
<td align="right">56,616,780</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">699,187,029</td>
<td align="right">697,525,627</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">682,009,533</td>
<td align="right">680,421,115</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,368,450,774</td>
<td align="right">6,353,874,469</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">25,192,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">394,320,870</td>
<td align="right">393,477,011</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">728,448,467</td>
<td align="right">726,956,031</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">158,951,730</td>
<td align="right">158,640,852</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,357,657,651</td>
<td align="right">2,353,268,739</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">236,056,197</td>
<td align="right">236,473,497</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,626,305</td>
<td align="right">46,703,306</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">74,421,928</td>
<td align="right">74,305,419</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">209,606,099</td>
<td align="right">209,863,072</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,681,446</td>
<td align="right">99,797,772</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">558,073,850</td>
<td align="right">557,424,547</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,331,585</td>
<td align="right">68,255,792</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,309,063</td>
<td align="right">281,006,129</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">155,524,312</td>
<td align="right">155,368,955</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">721,622,939</td>
<td align="right">720,922,988</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,321,169,130</td>
<td align="right">2,319,085,176</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,526,219,182</td>
<td align="right">1,524,849,212</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">704,234,989</td>
<td align="right">703,603,387</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">576,179,664</td>
<td align="right">576,636,900</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">49,748,268</td>
<td align="right">49,787,365</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">49,748,268</td>
<td align="right">49,787,365</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,226,781</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">6,776,739</td>
<td align="right">6,771,911</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,229,541,759</td>
<td align="right">2,227,962,148</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,256,930,776</td>
<td align="right">10,263,958,531</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">48,861,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">48,861,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,588,820</td>
<td align="right">32,567,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">987,676,693</td>
<td align="right">987,043,462</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,628,686,340</td>
<td align="right">3,626,600,527</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,947,927,109</td>
<td align="right">1,946,842,117</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">917,281,276</td>
<td align="right">916,773,099</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">229,356,044</td>
<td align="right">229,233,984</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,622,984,296</td>
<td align="right">1,622,217,649</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,647,788</td>
<td align="right">94,603,368</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">962,379,158</td>
<td align="right">961,928,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,815,531,696</td>
<td align="right">3,817,299,249</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,469,187</td>
<td align="right">1,071,947,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,817,328,480</td>
<td align="right">1,816,527,401</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,035,706,097</td>
<td align="right">3,037,030,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">942,463,751</td>
<td align="right">942,863,708</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,788,514</td>
<td align="right">394,622,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">786,484,440</td>
<td align="right">786,157,149</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">787,842,200</td>
<td align="right">787,514,909</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,715,262,386</td>
<td align="right">1,714,637,541</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,785,180</td>
<td align="right">4,783,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,154,798</td>
<td align="right">10,158,131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">740,056,470</td>
<td align="right">739,823,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">692,229,964</td>
<td align="right">692,027,407</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">166,005,834</td>
<td align="right">165,958,091</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,332,322,814</td>
<td align="right">1,331,955,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,907,540</td>
<td align="right">154,867,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,943,206,509</td>
<td align="right">3,942,282,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,478,751,839</td>
<td align="right">1,478,432,473</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">533,026,366</td>
<td align="right">532,922,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,083,871,681</td>
<td align="right">1,083,673,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,598,990,618</td>
<td align="right">2,599,405,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">11,447,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,420,466</td>
<td align="right">97,406,724</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,680</td>
<td align="right">1,994,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,464,920</td>
<td align="right">1,617,277,234</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">107,918,687</td>
<td align="right">107,906,638</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,344,804,878</td>
<td align="right">1,344,665,776</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">39,144,213</td>
<td align="right">39,140,673</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">41,164,573</td>
<td align="right">41,160,953</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,305,650</td>
<td align="right">1,305,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,949</td>
<td align="right">167,915,428</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,369,780</td>
<td align="right">125,364,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,240,357</td>
<td align="right">97,242,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,288,457</td>
<td align="right">97,290,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">885,043,118</td>
<td align="right">885,022,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">370,526</td>
<td align="right">370,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,204</td>
<td align="right">4,259,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,163,220</td>
<td align="right">11,163,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,437,130</td>
<td align="right">32,436,645</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">205,062,540</td>
<td align="right">205,065,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">785,050</td>
<td align="right">785,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">566,899,980</td>
<td align="right">566,892,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,984,920</td>
<td align="right">1,143,971,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,889,867,101</td>
<td align="right">4,889,826,570</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,480,693</td>
<td align="right">782,475,153</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">62,993,920</td>
<td align="right">62,993,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,007,640</td>
<td align="right">81,007,547</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,264</td>
<td align="right">518,102,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">100,794,768</td>
<td align="right">100,794,774</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,930</td>
<td align="right">603,439,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">350,232,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">72,855,500</td>
<td align="right">72,855,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,840</td>
<td align="right">4,739,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">2,849,145</td>
<td align="right">2,849,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,842,060</td>
<td align="right">1,842,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">915,052</td>
<td align="right">915,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">597,220</td>
<td align="right">597,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">488,920</td>
<td align="right">488,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">24,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">19,524</td>
<td align="right">17,575</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,020</td>
<td align="right">1,120</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,109</td>
<td align="right">46,923</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,580</td>
<td align="right">34,460</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">60</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,152</td>
<td align="right">1,168</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,152</td>
<td align="right">1,168</td>
<td align="right">1.4%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">400</td>
<td align="right">400</td>
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
<td align="right">1,941</td>
<td align="right">1,941</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-19
