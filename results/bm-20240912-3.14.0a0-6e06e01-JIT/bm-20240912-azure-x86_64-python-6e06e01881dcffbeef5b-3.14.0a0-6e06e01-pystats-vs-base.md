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
<td align="right">6,767,940,151</td>
<td align="right">2,886,971</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">162,427,163</td>
<td align="right">7,519,623</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,364,150,032</td>
<td align="right">77,160,129</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">834,006,211</td>
<td align="right">47,450,742</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,220,336,482</td>
<td align="right">187,438,566</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">133,515,680</td>
<td align="right">8,000,960</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,579,615,724</td>
<td align="right">170,165,849</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">233,699,425</td>
<td align="right">18,775,681</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">589,497,782</td>
<td align="right">56,017,370</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,498,494,101</td>
<td align="right">265,328,025</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">876,096,079</td>
<td align="right">93,420,601</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">481,857,733</td>
<td align="right">52,704,627</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">77,071,828</td>
<td align="right">8,718,893</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,480,461,585</td>
<td align="right">533,325,938</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,702,661</td>
<td align="right">70,946,296</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,680,798,983</td>
<td align="right">357,055,484</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,783,996</td>
<td align="right">239,211</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,713,289,663</td>
<td align="right">231,701,094</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">665,661,998</td>
<td align="right">90,953,716</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,980,481,827</td>
<td align="right">275,117,852</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,565,802,447</td>
<td align="right">219,844,821</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,126,617,225</td>
<td align="right">301,834,479</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,382,308,283</td>
<td align="right">197,308,884</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">663,753,433</td>
<td align="right">103,618,786</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,144,338,048</td>
<td align="right">181,108,786</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">340,971,820</td>
<td align="right">56,344,479</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">652,818,360</td>
<td align="right">107,903,679</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,069,941,167</td>
<td align="right">354,413,092</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">194,732,726</td>
<td align="right">33,579,972</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">838,220,405</td>
<td align="right">154,145,301</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">119,395,066</td>
<td align="right">22,062,117</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">289,932,397</td>
<td align="right">53,628,567</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">192,242,501</td>
<td align="right">36,221,632</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,316,006,224</td>
<td align="right">260,856,675</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">461,379,682</td>
<td align="right">93,298,956</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,674,378,992</td>
<td align="right">338,859,618</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">211,754,444</td>
<td align="right">43,448,701</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,095,023,514</td>
<td align="right">474,449,459</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,375,291,040</td>
<td align="right">765,794,353</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,252,437,726</td>
<td align="right">742,497,352</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,745,272,931</td>
<td align="right">4,346,807,382</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,108,385</td>
<td align="right">3,507,858</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">515,872,744</td>
<td align="right">119,985,579</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,113,899,839</td>
<td align="right">1,660,312,267</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">457,488,241</td>
<td align="right">107,205,847</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,118,251,359</td>
<td align="right">745,182,838</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">961,761,173</td>
<td align="right">238,933,970</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">112,892,129</td>
<td align="right">28,214,682</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">43,435,709</td>
<td align="right">10,996,060</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">169,437,657</td>
<td align="right">44,067,676</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,395,471,528</td>
<td align="right">370,140,957</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,781,108,606</td>
<td align="right">3,725,501,829</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,642,793,681</td>
<td align="right">4,606,375,349</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">132,915,984</td>
<td align="right">37,383,998</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2,693,156</td>
<td align="right">763,376</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,842,710,922</td>
<td align="right">3,648,087,546</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">95,881,863</td>
<td align="right">27,658,994</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">474,593,630</td>
<td align="right">136,996,459</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,750,920</td>
<td align="right">524,790</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,428,116,301</td>
<td align="right">435,359,248</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,520,762</td>
<td align="right">14,931,982</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">549,496</td>
<td align="right">173,470</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,244,277,871</td>
<td align="right">394,846,526</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">86,705,107</td>
<td align="right">28,212,110</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">47,686,882,158</td>
<td align="right">15,740,390,796</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">360,738,842</td>
<td align="right">119,859,583</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">248,787,497</td>
<td align="right">84,333,950</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,263,255</td>
<td align="right">268,166,131</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">127,669,683</td>
<td align="right">43,623,587</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,368,285</td>
<td align="right">2,893,309</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">152,855,344</td>
<td align="right">53,169,763</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">25,899,659</td>
<td align="right">9,034,937</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,175,160,526</td>
<td align="right">410,100,866</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">98,023,610</td>
<td align="right">35,029,928</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">169,990,354</td>
<td align="right">62,071,546</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,689,767,773</td>
<td align="right">618,155,320</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">766,101,991</td>
<td align="right">280,603,598</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">498,463,605</td>
<td align="right">183,238,003</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">281,331,161</td>
<td align="right">103,575,199</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">234,458,791</td>
<td align="right">91,862,793</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">638,014,626</td>
<td align="right">250,865,133</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">768,163,273</td>
<td align="right">305,370,875</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">464,750,732</td>
<td align="right">189,574,553</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,312,032,282</td>
<td align="right">2,576,970,887</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,149,887,059</td>
<td align="right">1,313,435,677</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">374,707,032</td>
<td align="right">157,962,910</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">8,204,768</td>
<td align="right">3,464,948</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">435,650,607</td>
<td align="right">189,694,813</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">288,574,672</td>
<td align="right">127,201,188</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">10,076,094</td>
<td align="right">4,464,283</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,138,819,430</td>
<td align="right">956,407,156</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,265,453,538</td>
<td align="right">566,444,172</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,299,989,481</td>
<td align="right">586,048,573</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,860,257,066</td>
<td align="right">2,220,800,914</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">328,656,165</td>
<td align="right">150,503,365</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,581,615,576</td>
<td align="right">1,653,986,163</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,751,742,482</td>
<td align="right">823,244,817</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,153,717,553</td>
<td align="right">1,031,964,011</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,040,910,650</td>
<td align="right">1,950,234,151</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">401,201,171</td>
<td align="right">197,873,513</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">932,692,081</td>
<td align="right">468,645,672</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">98,928,656</td>
<td align="right">50,028,553</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">18,113,808</td>
<td align="right">9,209,111</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,239,772</td>
<td align="right">642,892</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">373,346,861</td>
<td align="right">197,258,448</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,008,442,162</td>
<td align="right">534,576,682</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,041,440</td>
<td align="right">552,520</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">193,693,892</td>
<td align="right">103,409,829</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">622,141,962</td>
<td align="right">340,732,389</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">668,657,697</td>
<td align="right">367,548,883</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">111,245,807</td>
<td align="right">61,497,107</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,945,689,937</td>
<td align="right">4,563,478,712</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">98,994,020</td>
<td align="right">57,574,722</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">88,656,330</td>
<td align="right">52,077,621</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">332,229,479</td>
<td align="right">196,248,303</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">251,011,354</td>
<td align="right">150,191,763</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">230,148,884</td>
<td align="right">138,337,103</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">243,803,865</td>
<td align="right">147,001,263</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">114,056,977</td>
<td align="right">69,482,384</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,203,601,262</td>
<td align="right">2,607,287,294</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">104,444,883</td>
<td align="right">65,073,249</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">118,870,457</td>
<td align="right">76,064,797</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">83,242</td>
<td align="right">58,580</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">640,625,548</td>
<td align="right">453,710,408</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">195,763,412</td>
<td align="right">141,535,704</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,935,109,474</td>
<td align="right">2,859,888,019</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,179,923</td>
<td align="right">10,337,503</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">134,138,271</td>
<td align="right">99,103,548</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,211,614</td>
<td align="right">45,254,124</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">447,600,275</td>
<td align="right">331,590,915</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">344,178,028</td>
<td align="right">262,499,283</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">43,407,047</td>
<td align="right">33,170,874</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">74,010,569</td>
<td align="right">58,913,723</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">100</td>
<td align="right">80</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,627,898,229</td>
<td align="right">3,713,447,387</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">500,062,752</td>
<td align="right">402,558,651</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,295,545,311</td>
<td align="right">1,053,111,781</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,169,322</td>
<td align="right">8,538,794</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,147,569</td>
<td align="right">3,585,982</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,479,941</td>
<td align="right">71,162,210</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,011,333,776</td>
<td align="right">1,831,031,980</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,577,830</td>
<td align="right">16,184,608</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">89,610,726</td>
<td align="right">83,141,273</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">94,846,571</td>
<td align="right">88,068,929</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,208,123</td>
<td align="right">10,422,444</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">74,653,153</td>
<td align="right">71,480,673</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,139,789</td>
<td align="right">141,978,129</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">139,550,838</td>
<td align="right">134,319,738</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,629,436</td>
<td align="right">11,258,115</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,269,975</td>
<td align="right">225,010,783</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,397,242,247</td>
<td align="right">1,372,037,937</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">730,901</td>
<td align="right">720,489</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,669</td>
<td align="right">29,249</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,270,935,761</td>
<td align="right">2,263,087,535</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,726</td>
<td align="right">27,686</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,538,703</td>
<td align="right">82,460,945</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,376,735</td>
<td align="right">198,220,141</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,400,248</td>
<td align="right">21,388,062</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,162,066</td>
<td align="right">102,113,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,262,392</td>
<td align="right">1,261,988</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,086,023</td>
<td align="right">21,081,901</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,400,388</td>
<td align="right">21,396,403</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,865</td>
<td align="right">3,744,587</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,164</td>
<td align="right">15,165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,251</td>
<td align="right">268,238</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66,754</td>
<td align="right">66,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,829,607</td>
<td align="right">5,829,439</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,356,229</td>
<td align="right">20,356,125</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,398,738</td>
<td align="right">173,398,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,868,300</td>
<td align="right">10,868,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,928</td>
<td align="right">402,103,980</td>
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
<td align="left">LOAD_LOCALS</td>
<td align="right">21,656</td>
<td align="right">21,656</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">2,463,400,258</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,393,728,897</td>
<td align="right">12.8%</td>
<td align="right">368,982,134</td>
<td align="right">3.8%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">50,340,310</td>
<td align="right">0.5%</td>
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,461,333,198</td>
<td align="right">86.7%</td>
<td align="right">9,415,858,801</td>
<td align="right">95.9%</td>
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
<td align="right">992,208</td>
<td align="right">36.9%</td>
<td align="right">598,531</td>
<td align="right">34.9%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,700,023</td>
<td align="right">63.1%</td>
<td align="right">1,116,372</td>
<td align="right">65.1%</td>
<td align="right">-34.3%</td>
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
<td align="right">17,769</td>
<td align="right">1.0%</td>
<td align="right">2,827</td>
<td align="right">0.3%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">216,607</td>
<td align="right">12.7%</td>
<td align="right">49,190</td>
<td align="right">4.4%</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">37,206</td>
<td align="right">2.2%</td>
<td align="right">8,465</td>
<td align="right">0.8%</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">29,503</td>
<td align="right">1.7%</td>
<td align="right">6,722</td>
<td align="right">0.6%</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">29,365</td>
<td align="right">1.7%</td>
<td align="right">8,548</td>
<td align="right">0.8%</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">65,320</td>
<td align="right">3.8%</td>
<td align="right">19,978</td>
<td align="right">1.8%</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">247,141</td>
<td align="right">14.5%</td>
<td align="right">81,581</td>
<td align="right">7.3%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">29,501</td>
<td align="right">1.7%</td>
<td align="right">10,821</td>
<td align="right">1.0%</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">13,566</td>
<td align="right">0.8%</td>
<td align="right">5,599</td>
<td align="right">0.5%</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,936</td>
<td align="right">0.1%</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">70,909</td>
<td align="right">4.2%</td>
<td align="right">31,531</td>
<td align="right">2.8%</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">53,232</td>
<td align="right">3.1%</td>
<td align="right">31,701</td>
<td align="right">2.8%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">15,282</td>
<td align="right">0.9%</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">69,083</td>
<td align="right">4.1%</td>
<td align="right">47,037</td>
<td align="right">4.2%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">16,665</td>
<td align="right">1.0%</td>
<td align="right">14,487</td>
<td align="right">1.3%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,083</td>
<td align="right">0.2%</td>
<td align="right">2,723</td>
<td align="right">0.2%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">777,954</td>
<td align="right">45.8%</td>
<td align="right">781,603</td>
<td align="right">70.0%</td>
<td align="right">0.5%</td>
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
<td align="right">1,144,338,048</td>
<td align="right">100.0%</td>
<td align="right">181,108,786</td>
<td align="right">100.0%</td>
<td align="right">-84.2%</td>
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
<td align="right">2,094,349,520</td>
<td align="right">25.2%</td>
<td align="right">474,179,536</td>
<td align="right">7.1%</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,033,657</td>
<td align="right">0.1%</td>
<td align="right">4,792,411</td>
<td align="right">0.1%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,226,955,363</td>
<td align="right">74.8%</td>
<td align="right">6,201,948,173</td>
<td align="right">92.8%</td>
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
<td align="right">582,224</td>
<td align="right">75.8%</td>
<td align="right">178,276</td>
<td align="right">49.5%</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,251</td>
<td align="right">24.2%</td>
<td align="right">181,608</td>
<td align="right">50.5%</td>
<td align="right">-2.5%</td>
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
<td align="right">35,100</td>
<td align="right">6.0%</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">157,600</td>
<td align="right">27.1%</td>
<td align="right">26,640</td>
<td align="right">14.9%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">261,441</td>
<td align="right">44.9%</td>
<td align="right">65,356</td>
<td align="right">36.7%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">48,034</td>
<td align="right">8.3%</td>
<td align="right">21,332</td>
<td align="right">12.0%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">74,206</td>
<td align="right">12.7%</td>
<td align="right">58,346</td>
<td align="right">32.7%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">0.7%</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.1%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
<td align="right">206,575,087</td>
<td align="right">1.5%</td>
<td align="right">149,957,046</td>
<td align="right">1.1%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,300</td>
<td align="right">0.0%</td>
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,516,581,435</td>
<td align="right">98.5%</td>
<td align="right">13,535,277,811</td>
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
<td align="right">716,769</td>
<td align="right">0.0%</td>
<td align="right">716,638</td>
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
<td align="right">4,482,487</td>
<td align="right">100.0%</td>
<td align="right">3,407,133</td>
<td align="right">100.0%</td>
<td align="right">-24.0%</td>
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
<td align="right">802,800</td>
<td align="right">92.3%</td>
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,411</td>
<td align="right">4.2%</td>
<td align="right">36,409</td>
<td align="right">7.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">663,392,587</td>
<td align="right">10.3%</td>
<td align="right">103,412,236</td>
<td align="right">1.8%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,373,053</td>
<td align="right">0.0%</td>
<td align="right">1,026,714</td>
<td align="right">0.0%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,751,546,566</td>
<td align="right">89.6%</td>
<td align="right">5,733,823,690</td>
<td align="right">98.2%</td>
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
<td align="right">305,466</td>
<td align="right">79.1%</td>
<td align="right">151,285</td>
<td align="right">67.1%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">80,891</td>
<td align="right">20.9%</td>
<td align="right">74,299</td>
<td align="right">32.9%</td>
<td align="right">-8.1%</td>
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
<td align="right">9,760</td>
<td align="right">3.2%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120,464</td>
<td align="right">39.4%</td>
<td align="right">12,102</td>
<td align="right">8.0%</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,235</td>
<td align="right">1.1%</td>
<td align="right">1,538</td>
<td align="right">1.0%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27,729</td>
<td align="right">9.1%</td>
<td align="right">19,189</td>
<td align="right">12.7%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">52,570</td>
<td align="right">17.2%</td>
<td align="right">38,365</td>
<td align="right">25.4%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">19,116</td>
<td align="right">6.3%</td>
<td align="right">14,512</td>
<td align="right">9.6%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,320</td>
<td align="right">1.4%</td>
<td align="right">3,540</td>
<td align="right">2.3%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">34,246</td>
<td align="right">11.2%</td>
<td align="right">29,773</td>
<td align="right">19.7%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,876</td>
<td align="right">6.5%</td>
<td align="right">17,416</td>
<td align="right">11.5%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">530</td>
<td align="right">0.2%</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,880</td>
<td align="right">3.6%</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,740</td>
<td align="right">0.9%</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">-0.7%</td>
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
<td align="right">192,113,929</td>
<td align="right">7.1%</td>
<td align="right">36,137,034</td>
<td align="right">1.4%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,493,808,331</td>
<td align="right">92.8%</td>
<td align="right">2,486,643,490</td>
<td align="right">98.5%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,544,260</td>
<td align="right">0.1%</td>
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
<td align="right">115,393</td>
<td align="right">65.4%</td>
<td align="right">71,419</td>
<td align="right">53.9%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,139</td>
<td align="right">34.6%</td>
<td align="right">61,099</td>
<td align="right">46.1%</td>
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
<td align="left">str</td>
<td align="right">35,182</td>
<td align="right">30.5%</td>
<td align="right">14,522</td>
<td align="right">20.3%</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">27,971</td>
<td align="right">24.2%</td>
<td align="right">14,470</td>
<td align="right">20.3%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,595</td>
<td align="right">18.7%</td>
<td align="right">15,276</td>
<td align="right">21.4%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,645</td>
<td align="right">26.6%</td>
<td align="right">27,151</td>
<td align="right">38.0%</td>
<td align="right">-11.4%</td>
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
<td align="right">173,273,018</td>
<td align="right">3.1%</td>
<td align="right">6,738,018</td>
<td align="right">1.1%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,363,602,488</td>
<td align="right">24.1%</td>
<td align="right">77,009,322</td>
<td align="right">12.5%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,127,626,068</td>
<td align="right">72.9%</td>
<td align="right">533,331,558</td>
<td align="right">86.4%</td>
<td align="right">-87.1%</td>
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
<td align="right">3,317,882</td>
<td align="right">86.9%</td>
<td align="right">175,733</td>
<td align="right">63.3%</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">498,549</td>
<td align="right">13.1%</td>
<td align="right">101,905</td>
<td align="right">36.7%</td>
<td align="right">-79.6%</td>
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
<td align="right">219,168</td>
<td align="right">44.0%</td>
<td align="right">7,602</td>
<td align="right">7.5%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">30,160</td>
<td align="right">6.0%</td>
<td align="right">3,981</td>
<td align="right">3.9%</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,501</td>
<td align="right">0.5%</td>
<td align="right">616</td>
<td align="right">0.6%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">44,786</td>
<td align="right">9.0%</td>
<td align="right">11,373</td>
<td align="right">11.2%</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20,965</td>
<td align="right">4.2%</td>
<td align="right">6,625</td>
<td align="right">6.5%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">2,280</td>
<td align="right">0.5%</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">108,334</td>
<td align="right">21.7%</td>
<td align="right">36,672</td>
<td align="right">36.0%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">13,056</td>
<td align="right">2.6%</td>
<td align="right">4,936</td>
<td align="right">4.8%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">28,079</td>
<td align="right">5.6%</td>
<td align="right">11,070</td>
<td align="right">10.9%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,747</td>
<td align="right">1.2%</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">520</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">6,084</td>
<td align="right">1.2%</td>
<td align="right">3,484</td>
<td align="right">3.4%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">10,071</td>
<td align="right">2.0%</td>
<td align="right">6,737</td>
<td align="right">6.6%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,778</td>
<td align="right">1.4%</td>
<td align="right">5,222</td>
<td align="right">5.1%</td>
<td align="right">-23.0%</td>
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
<td align="right">989,562,798</td>
<td align="right">5.7%</td>
<td align="right">320,065,302</td>
<td align="right">2.0%</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">930,314,698</td>
<td align="right">5.3%</td>
<td align="right">466,517,227</td>
<td align="right">2.9%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,909,520</td>
<td align="right">0.0%</td>
<td align="right">1,289,180</td>
<td align="right">0.0%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,520,313,851</td>
<td align="right">89.0%</td>
<td align="right">15,541,652,771</td>
<td align="right">95.2%</td>
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
<td align="right">20,427,442</td>
<td align="right">97.2%</td>
<td align="right">7,673,095</td>
<td align="right">94.3%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">585,216</td>
<td align="right">2.8%</td>
<td align="right">459,616</td>
<td align="right">5.7%</td>
<td align="right">-21.5%</td>
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
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">141,214</td>
<td align="right">24.1%</td>
<td align="right">84,144</td>
<td align="right">18.3%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">43,918</td>
<td align="right">7.5%</td>
<td align="right">31,224</td>
<td align="right">6.8%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">118,506</td>
<td align="right">20.2%</td>
<td align="right">88,020</td>
<td align="right">19.2%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,316</td>
<td align="right">0.6%</td>
<td align="right">2,755</td>
<td align="right">0.6%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,484</td>
<td align="right">0.6%</td>
<td align="right">2,924</td>
<td align="right">0.6%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,096</td>
<td align="right">2.9%</td>
<td align="right">14,969</td>
<td align="right">3.3%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">17,430</td>
<td align="right">3.0%</td>
<td align="right">15,280</td>
<td align="right">3.3%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,803</td>
<td align="right">0.5%</td>
<td align="right">2,543</td>
<td align="right">0.6%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">35,276</td>
<td align="right">6.0%</td>
<td align="right">32,281</td>
<td align="right">7.0%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">151,336</td>
<td align="right">25.9%</td>
<td align="right">138,603</td>
<td align="right">30.2%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,760</td>
<td align="right">1.0%</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,718</td>
<td align="right">1.0%</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,962</td>
<td align="right">3.8%</td>
<td align="right">20,880</td>
<td align="right">4.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">700</td>
<td align="right">0.1%</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
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
<td align="right">11,317,109,121</td>
<td align="right">99.8%</td>
<td align="right">4,512,723,471</td>
<td align="right">99.5%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">391,980</td>
<td align="right">0.0%</td>
<td align="right">391,104</td>
<td align="right">0.0%</td>
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
<td align="right">19,894,872</td>
<td align="right">0.2%</td>
<td align="right">19,894,779</td>
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
<td align="right">467,055</td>
<td align="right">100.0%</td>
<td align="right">467,046</td>
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
<td align="right">86,224,806</td>
<td align="right">100.0%</td>
<td align="right">86,070,017</td>
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
<td align="right">7,623</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,663</td>
<td align="right">0.0%</td>
<td align="right">30,643</td>
<td align="right">0.0%</td>
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
<td align="right">173,334,007</td>
<td align="right">18.1%</td>
<td align="right">173,334,095</td>
<td align="right">18.1%</td>
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
<td align="right">786,232,592</td>
<td align="right">81.9%</td>
<td align="right">786,232,612</td>
<td align="right">81.9%</td>
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
<td align="right">59,754</td>
<td align="right">91.5%</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
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
<td align="left">list</td>
<td align="right">10,040</td>
<td align="right">16.8%</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">-0.2%</td>
</tr>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,022,159</td>
<td align="right">2.3%</td>
<td align="right">45,066,991</td>
<td align="right">1.7%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,910,024</td>
<td align="right">6.2%</td>
<td align="right">121,957,216</td>
<td align="right">4.6%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,441,493,068</td>
<td align="right">91.5%</td>
<td align="right">2,465,648,468</td>
<td align="right">93.6%</td>
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
<td align="left">Success</td>
<td align="right">3,212,076</td>
<td align="right">97.4%</td>
<td align="right">2,401,347</td>
<td align="right">96.6%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">85,849</td>
<td align="right">2.6%</td>
<td align="right">83,987</td>
<td align="right">3.4%</td>
<td align="right">-2.2%</td>
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
<td align="right">13,605</td>
<td align="right">15.8%</td>
<td align="right">17,045</td>
<td align="right">20.3%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,743</td>
<td align="right">12.5%</td>
<td align="right">8,363</td>
<td align="right">10.0%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">34,424</td>
<td align="right">40.1%</td>
<td align="right">31,884</td>
<td align="right">38.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">844</td>
<td align="right">1.0%</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,325</td>
<td align="right">3.9%</td>
<td align="right">3,185</td>
<td align="right">3.8%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,180</td>
<td align="right">2.5%</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">780</td>
<td align="right">0.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,035</td>
<td align="right">5.9%</td>
<td align="right">4,955</td>
<td align="right">5.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">5,021</td>
<td align="right">5.8%</td>
<td align="right">5,001</td>
<td align="right">6.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,812</td>
<td align="right">11.4%</td>
<td align="right">9,810</td>
<td align="right">11.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">162,427,163</td>
<td align="right">100.0%</td>
<td align="right">7,519,623</td>
<td align="right">100.0%</td>
<td align="right">-95.4%</td>
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
<td align="right">875,821,523</td>
<td align="right">49.9%</td>
<td align="right">93,340,508</td>
<td align="right">9.6%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">878,069,554</td>
<td align="right">50.1%</td>
<td align="right">875,193,754</td>
<td align="right">90.4%</td>
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
<td align="right">261,229</td>
<td align="right">95.1%</td>
<td align="right">66,761</td>
<td align="right">83.3%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,367</td>
<td align="right">4.9%</td>
<td align="right">13,372</td>
<td align="right">16.7%</td>
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
<td align="right">108,740</td>
<td align="right">41.6%</td>
<td align="right">640</td>
<td align="right">1.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">9,660</td>
<td align="right">3.7%</td>
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">66,240</td>
<td align="right">25.4%</td>
<td align="right">14,160</td>
<td align="right">21.2%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">30,005</td>
<td align="right">11.5%</td>
<td align="right">6,718</td>
<td align="right">10.1%</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,240</td>
<td align="right">1.2%</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">43,344</td>
<td align="right">16.6%</td>
<td align="right">42,243</td>
<td align="right">63.3%</td>
<td align="right">-2.5%</td>
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
<td align="right">146,000,108</td>
<td align="right">2.3%</td>
<td align="right">24,400,885</td>
<td align="right">0.4%</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">327,818,488</td>
<td align="right">5.1%</td>
<td align="right">150,097,201</td>
<td align="right">2.5%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,955,327,889</td>
<td align="right">92.6%</td>
<td align="right">5,752,269,782</td>
<td align="right">97.0%</td>
<td align="right">-3.4%</td>
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
<td align="right">2,947,664</td>
<td align="right">82.2%</td>
<td align="right">653,651</td>
<td align="right">75.9%</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">639,437</td>
<td align="right">17.8%</td>
<td align="right">208,091</td>
<td align="right">24.1%</td>
<td align="right">-67.5%</td>
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
<td align="right">175,816</td>
<td align="right">27.5%</td>
<td align="right">5,999</td>
<td align="right">2.9%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">96,877</td>
<td align="right">15.2%</td>
<td align="right">14,910</td>
<td align="right">7.2%</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">164,869</td>
<td align="right">25.8%</td>
<td align="right">37,270</td>
<td align="right">17.9%</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,805</td>
<td align="right">2.2%</td>
<td align="right">7,328</td>
<td align="right">3.5%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">27,045</td>
<td align="right">4.2%</td>
<td align="right">16,145</td>
<td align="right">7.8%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,043</td>
<td align="right">0.2%</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">28,347</td>
<td align="right">4.4%</td>
<td align="right">19,131</td>
<td align="right">9.2%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">104,702</td>
<td align="right">16.4%</td>
<td align="right">82,826</td>
<td align="right">39.8%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,764</td>
<td align="right">3.9%</td>
<td align="right">21,710</td>
<td align="right">10.4%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.3%</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
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
<td align="right">1,742,796</td>
<td align="right">0.1%</td>
<td align="right">198,733</td>
<td align="right">0.0%</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,972,240</td>
<td align="right">0.1%</td>
<td align="right">433,280</td>
<td align="right">0.0%</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,069,068,952</td>
<td align="right">99.8%</td>
<td align="right">2,058,086,852</td>
<td align="right">100.0%</td>
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
<td align="right">94,795</td>
<td align="right">97.4%</td>
<td align="right">46,735</td>
<td align="right">96.4%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,485</td>
<td align="right">2.6%</td>
<td align="right">1,763</td>
<td align="right">3.6%</td>
<td align="right">-29.1%</td>
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
<td align="right">1,836</td>
<td align="right">73.9%</td>
<td align="right">1,116</td>
<td align="right">63.3%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">269</td>
<td align="right">10.8%</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">15.3%</td>
<td align="right">380</td>
<td align="right">21.6%</td>
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
<td align="right">9,412,945,431</td>
<td align="right">3.6%</td>
<td align="right">2,203,381,205</td>
<td align="right">2.4%</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">90,460,600,977</td>
<td align="right">34.6%</td>
<td align="right">30,732,225,983</td>
<td align="right">33.8%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">160,164,463,024</td>
<td align="right">61.2%</td>
<td align="right">57,346,803,700</td>
<td align="right">63.1%</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,744,019,496</td>
<td align="right">0.7%</td>
<td align="right">662,460,456</td>
<td align="right">0.7%</td>
<td align="right">-62.0%</td>
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
<td align="right">1,363,602,488</td>
<td align="right">14.5%</td>
<td align="right">77,009,322</td>
<td align="right">3.5%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">875,821,523</td>
<td align="right">9.3%</td>
<td align="right">93,340,508</td>
<td align="right">4.2%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">663,392,587</td>
<td align="right">7.1%</td>
<td align="right">103,412,236</td>
<td align="right">4.7%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,144,338,048</td>
<td align="right">12.2%</td>
<td align="right">181,108,786</td>
<td align="right">8.2%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,094,349,520</td>
<td align="right">22.3%</td>
<td align="right">474,179,536</td>
<td align="right">21.6%</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,393,728,897</td>
<td align="right">14.8%</td>
<td align="right">368,982,134</td>
<td align="right">16.8%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">327,818,488</td>
<td align="right">3.5%</td>
<td align="right">150,097,201</td>
<td align="right">6.8%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">930,314,698</td>
<td align="right">9.9%</td>
<td align="right">466,517,227</td>
<td align="right">21.2%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,007</td>
<td align="right">1.8%</td>
<td align="right">173,334,095</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">192,113,929</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">45,066,991</td>
<td align="right">2.1%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">301,901,142</td>
<td align="right">17.3%</td>
<td align="right">82,628,700</td>
<td align="right">12.5%</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">427,338,544</td>
<td align="right">24.5%</td>
<td align="right">120,149,214</td>
<td align="right">18.1%</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">111,080,371</td>
<td align="right">6.4%</td>
<td align="right">38,071,252</td>
<td align="right">5.7%</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">88,051,377</td>
<td align="right">5.0%</td>
<td align="right">40,280,504</td>
<td align="right">6.1%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">110,868,756</td>
<td align="right">6.4%</td>
<td align="right">79,489,860</td>
<td align="right">12.0%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">134,358,884</td>
<td align="right">7.7%</td>
<td align="right">98,114,304</td>
<td align="right">14.8%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">86,709,312</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">86,456,041</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">69,183,157</td>
<td align="right">4.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">68,117,861</td>
<td align="right">3.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">27,496,932</td>
<td align="right">4.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">23,838,306</td>
<td align="right">3.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,177,240</td>
<td align="right">3.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,135,025</td>
<td align="right">2.7%</td>
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
<td align="right">5,298,052</td>
<td align="right">0.1%</td>
<td align="right">4,418,012</td>
<td align="right">0.1%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,033,906</td>
<td align="right">1.0%</td>
<td align="right">84,754,719</td>
<td align="right">1.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,210,937,605</td>
<td align="right">73.2%</td>
<td align="right">6,168,366,911</td>
<td align="right">73.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">856,884,347</td>
<td align="right">10.1%</td>
<td align="right">851,924,816</td>
<td align="right">10.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,709,858,827</td>
<td align="right">79.1%</td>
<td align="right">6,684,676,491</td>
<td align="right">79.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,274,313,711</td>
<td align="right">26.8%</td>
<td align="right">2,266,903,453</td>
<td align="right">26.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,274,313,711</td>
<td align="right">26.8%</td>
<td align="right">2,266,903,453</td>
<td align="right">26.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,989,531</td>
<td align="right">3.9%</td>
<td align="right">333,905,278</td>
<td align="right">4.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,417,429,364</td>
<td align="right">16.7%</td>
<td align="right">1,414,978,637</td>
<td align="right">16.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,412,101,643</td>
<td align="right">16.6%</td>
<td align="right">1,410,530,956</td>
<td align="right">16.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,648,339</td>
<td align="right">3.9%</td>
<td align="right">331,636,493</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,099,269</td>
<td align="right">0.4%</td>
<td align="right">31,098,736</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,388</td>
<td align="right">2.1%</td>
<td align="right">175,480,276</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">14,168,501</td>
<td align="right"></td>
<td align="right">58,349,759</td>
<td align="right"></td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">31,137,991,861</td>
<td align="right">31,137,991,861 / 0 !!</td>
<td align="right">98,041,458,383</td>
<td align="right">98,041,458,383 / 0 !!</td>
<td align="right">214.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">38,394,154,740</td>
<td align="right">38,394,154,740 / 0 !!</td>
<td align="right">105,618,021,547</td>
<td align="right">105,618,021,547 / 0 !!</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">97,202,593,070</td>
<td align="right">97,202,593,070 / 0 !!</td>
<td align="right">41,463,178,143</td>
<td align="right">41,463,178,143 / 0 !!</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">79,673,621</td>
<td align="right"></td>
<td align="right">124,604,671</td>
<td align="right"></td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">112,804,605,653</td>
<td align="right">112,804,605,653 / 0 !!</td>
<td align="right">56,723,699,450</td>
<td align="right">56,723,699,450 / 0 !!</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,685,813,031</td>
<td align="right"></td>
<td align="right">2,391,904,750</td>
<td align="right"></td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">66,510,204</td>
<td align="right"></td>
<td align="right">69,772,053</td>
<td align="right"></td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,732,346,387</td>
<td align="right"></td>
<td align="right">3,668,367,332</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,991,328,684</td>
<td align="right"></td>
<td align="right">13,956,654,138</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,095,061,009</td>
<td align="right">52.4%</td>
<td align="right">13,064,684,521</td>
<td align="right">52.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,219,783,984</td>
<td align="right">52.9%</td>
<td align="right">13,189,386,658</td>
<td align="right">52.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">236,250,674</td>
<td align="right"></td>
<td align="right">235,930,734</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,625,467</td>
<td align="right">0.4%</td>
<td align="right">103,606,818</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,766,776,442</td>
<td align="right">47.1%</td>
<td align="right">11,765,055,836</td>
<td align="right">47.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,768,644,559</td>
<td align="right"></td>
<td align="right">11,766,929,659</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">21,097,508</td>
<td align="right">0.1%</td>
<td align="right">21,095,319</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">454,929</td>
<td align="right">112,653,184</td>
<td align="right">19,143,809,968</td>
<td align="right">453,966</td>
<td align="right">112,212,307</td>
<td align="right">19,099,975,281</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,957,511,288</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,959,114,560</td>
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
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">1,152</td>
<td align="right">1,152 / 0 !!</td>
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
<td align="right">1,152</td>
<td align="right">1,152 / 0 !!</td>
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
Stats gathered on: 2024-10-21
