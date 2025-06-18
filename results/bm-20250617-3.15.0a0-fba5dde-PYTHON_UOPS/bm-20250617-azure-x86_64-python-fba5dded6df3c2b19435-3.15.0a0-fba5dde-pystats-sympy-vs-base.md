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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">135,099,815</td>
<td align="right">2,418,418</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,016,805</td>
<td align="right">2,618,133</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,421,861</td>
<td align="right">5,500,217</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,034,883</td>
<td align="right">1,585,875</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,473,890</td>
<td align="right">22,353,512</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,329,488</td>
<td align="right">1,555,801</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,623,392</td>
<td align="right">17,492,364</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,112,255</td>
<td align="right">15,064,420</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,764,248</td>
<td align="right">46,036,307</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,241,833</td>
<td align="right">3,728,189</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,413,198</td>
<td align="right">10,882,783</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,197,994</td>
<td align="right">55,580,482</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,708,465</td>
<td align="right">57,090,807</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,961,050</td>
<td align="right">57,874,865</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,314,040</td>
<td align="right">13,257,779</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,099,564</td>
<td align="right">86,032,197</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,323</td>
<td align="right">21,674,152</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,163,577</td>
<td align="right">11,038,861</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">46,453,940</td>
<td align="right">39,253,203</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,799,233</td>
<td align="right">59,906,753</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,394,397</td>
<td align="right">62,258,932</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,846,409</td>
<td align="right">38,727,530</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,012,453</td>
<td align="right">9,579,687</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,101,498</td>
<td align="right">9,668,698</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">273,570,516</td>
<td align="right">239,314,305</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,708,708</td>
<td align="right">11,271,539</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">192,604,952</td>
<td align="right">171,827,632</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,945,002</td>
<td align="right">15,117,262</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,439,344</td>
<td align="right">32,111,543</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,130,127</td>
<td align="right">21,007,104</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,134</td>
<td align="right">15,881,713</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">678,968,048</td>
<td align="right">624,746,877</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,093,301</td>
<td align="right">36,966,818</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,114,010</td>
<td align="right">48,104,138</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">15,007,385</td>
<td align="right">13,939,437</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">44,480,791</td>
<td align="right">41,601,683</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,955,422</td>
<td align="right">67,329,363</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,077,459</td>
<td align="right">18,031,092</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,230,698</td>
<td align="right">24,794,382</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">232,561,796</td>
<td align="right">220,677,554</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">47,047,816</td>
<td align="right">44,882,782</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">149,889,432</td>
<td align="right">144,447,466</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">45,064,178</td>
<td align="right">43,508,877</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,608,356</td>
<td align="right">173,082,726</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,413,113</td>
<td align="right">45,015,152</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,586,600</td>
<td align="right">34,525,119</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,360</td>
<td align="right">1,758,788</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,873,439</td>
<td align="right">51,423,195</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,803,612</td>
<td align="right">44,688,308</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,601,355</td>
<td align="right">18,162,841</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60,565,267</td>
<td align="right">59,681,061</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,617,437</td>
<td align="right">17,820,486</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,878,782</td>
<td align="right">18,082,813</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,620,027</td>
<td align="right">11,490,570</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,742,156</td>
<td align="right">15,567,491</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,717</td>
<td align="right">456,654</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,616,724</td>
<td align="right">2,588,745</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,018,965</td>
<td align="right">19,221,938</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">149,476,038</td>
<td align="right">148,025,202</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,961</td>
<td align="right">9,041</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,991,788</td>
<td align="right">9,913,134</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">990</td>
<td align="right">996</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,612,902</td>
<td align="right">4,586,045</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,378,464</td>
<td align="right">23,262,931</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,977,963</td>
<td align="right">8,934,935</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,984,822</td>
<td align="right">15,920,293</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,299,812</td>
<td align="right">49,115,049</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,574,187</td>
<td align="right">75,317,100</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,219,514</td>
<td align="right">53,397,563</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">41,126</td>
<td align="right">41,249</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,831,297</td>
<td align="right">6,813,794</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,468,664</td>
<td align="right">9,449,907</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,109</td>
<td align="right">7,119</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,437,846</td>
<td align="right">12,424,398</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,220,945</td>
<td align="right">1,222,250</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,141,570</td>
<td align="right">199,334,486</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">1,443</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,481,378</td>
<td align="right">30,461,090</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,693,582</td>
<td align="right">21,707,293</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,925,483</td>
<td align="right">7,930,398</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,089,193</td>
<td align="right">8,094,090</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,271</td>
<td align="right">175,361</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,063</td>
<td align="right">18,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,098</td>
<td align="right">83,134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,976,583</td>
<td align="right">5,974,134</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,214</td>
<td align="right">655,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,214</td>
<td align="right">655,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,214</td>
<td align="right">655,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,958</td>
<td align="right">2,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,972</td>
<td align="right">744,729</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,744,515</td>
<td align="right">24,750,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">79,530</td>
<td align="right">79,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,146,478</td>
<td align="right">33,138,849</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,873,613</td>
<td align="right">10,871,159</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,655</td>
<td align="right">165,621</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,488</td>
<td align="right">2,008,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,188</td>
<td align="right">2,585,681</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,590</td>
<td align="right">2,007,971</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,172</td>
<td align="right">495,083</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,995</td>
<td align="right">1,029,178</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,029,886</td>
<td align="right">1,030,069</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,799</td>
<td align="right">23,803</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,120</td>
<td align="right">6,786,079</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,088</td>
<td align="right">6,026,918</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,276</td>
<td align="right">4,497,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,629,760</td>
<td align="right">18,631,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,446</td>
<td align="right">654,510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,462</td>
<td align="right">654,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,680</td>
<td align="right">20,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,052</td>
<td align="right">1,287,928</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,616</td>
<td align="right">942,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,724</td>
<td align="right">1,389,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,390</td>
<td align="right">141,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,590</td>
<td align="right">6,590,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,449</td>
<td align="right">2,281,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,061</td>
<td align="right">5,753,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,717</td>
<td align="right">6,623,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,958</td>
<td align="right">746,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,895</td>
<td align="right">389,919</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,859,645</td>
<td align="right">181,849,505</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,347</td>
<td align="right">7,541,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,116</td>
<td align="right">2,995,249</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,295</td>
<td align="right">6,744,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,525</td>
<td align="right">598,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,696</td>
<td align="right">4,001,832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,312</td>
<td align="right">746,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,041</td>
<td align="right">21,977,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,920,782</td>
<td align="right">10,921,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,675</td>
<td align="right">4,181,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,518</td>
<td align="right">1,754,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,561</td>
<td align="right">21,985,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,547</td>
<td align="right">427,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,783</td>
<td align="right">9,777,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,306</td>
<td align="right">1,323,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,524</td>
<td align="right">1,244,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,050</td>
<td align="right">172,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,199,443</td>
<td align="right">2,199,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,735,772</td>
<td align="right">78,735,332</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,431</td>
<td align="right">4,469,414</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">388,827</td>
<td align="right">388,827</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">341,720</td>
<td align="right">341,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,532</td>
<td align="right">178,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">133,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,009</td>
<td align="right">89,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">14,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,037</td>
<td align="right">12,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,550</td>
<td align="right">5,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,150</td>
<td align="right">4,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">58,007,701</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">28,392,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">207,412</td>
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
<td align="right">45,772,386</td>
<td align="right">39.1%</td>
<td align="right">44,657,339</td>
<td align="right">38.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">70,886,414</td>
<td align="right">60.5%</td>
<td align="right">70,496,213</td>
<td align="right">61.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">396,358</td>
<td align="right">0.3%</td>
<td align="right">396,319</td>
<td align="right">0.3%</td>
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
<td align="right">29,101</td>
<td align="right">75.3%</td>
<td align="right">28,844</td>
<td align="right">75.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,563</td>
<td align="right">24.7%</td>
<td align="right">9,558</td>
<td align="right">24.9%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,353</td>
<td align="right">8.1%</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">738</td>
<td align="right">2.5%</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,006</td>
<td align="right">3.5%</td>
<td align="right">1,017</td>
<td align="right">3.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">210</td>
<td align="right">0.7%</td>
<td align="right">212</td>
<td align="right">0.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,750</td>
<td align="right">6.0%</td>
<td align="right">1,765</td>
<td align="right">6.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,904</td>
<td align="right">13.4%</td>
<td align="right">3,871</td>
<td align="right">13.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,221</td>
<td align="right">4.2%</td>
<td align="right">1,211</td>
<td align="right">4.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">571</td>
<td align="right">2.0%</td>
<td align="right">569</td>
<td align="right">2.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">624</td>
<td align="right">2.1%</td>
<td align="right">626</td>
<td align="right">2.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">709</td>
<td align="right">2.4%</td>
<td align="right">707</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,579</td>
<td align="right">15.7%</td>
<td align="right">4,570</td>
<td align="right">15.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,085</td>
<td align="right">3.7%</td>
<td align="right">1,086</td>
<td align="right">3.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,891</td>
<td align="right">9.9%</td>
<td align="right">2,892</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">3,221</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.6%</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.2%</td>
<td align="right">363</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">12,037</td>
<td align="right">100.0%</td>
<td align="right">12,037</td>
<td align="right">100.0%</td>
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
<td align="right">276,405,060</td>
<td align="right">88.3%</td>
<td align="right">265,214,741</td>
<td align="right">87.9%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">36,433,245</td>
<td align="right">11.6%</td>
<td align="right">36,643,197</td>
<td align="right">12.1%</td>
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
<td align="right">35,754,338</td>
<td align="right">11.4%</td>
<td align="right">35,960,340</td>
<td align="right">11.9%</td>
<td align="right">0.6%</td>
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
<td align="right">702,706</td>
<td align="right">100.0%</td>
<td align="right">706,660</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">3,183</td>
<td align="right">74.9%</td>
<td align="right">3,183</td>
<td align="right">74.9%</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,805</td>
<td align="right">66.0%</td>
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
<td align="right">1,066</td>
<td align="right">100.0%</td>
<td align="right">1,065</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,031,983</td>
<td align="right">62.3%</td>
<td align="right">47,905,774</td>
<td align="right">60.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,442,758</td>
<td align="right">37.2%</td>
<td align="right">30,422,484</td>
<td align="right">38.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,647</td>
<td align="right">0.5%</td>
<td align="right">409,674</td>
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
<td align="right">37,453</td>
<td align="right">80.9%</td>
<td align="right">37,436</td>
<td align="right">80.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,840</td>
<td align="right">19.1%</td>
<td align="right">8,843</td>
<td align="right">19.1%</td>
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
<td align="left">baseobject</td>
<td align="right">117</td>
<td align="right">0.3%</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,461</td>
<td align="right">3.9%</td>
<td align="right">1,454</td>
<td align="right">3.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,250</td>
<td align="right">11.3%</td>
<td align="right">4,269</td>
<td align="right">11.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,155</td>
<td align="right">8.4%</td>
<td align="right">3,145</td>
<td align="right">8.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,473</td>
<td align="right">17.3%</td>
<td align="right">6,466</td>
<td align="right">17.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,107</td>
<td align="right">37.7%</td>
<td align="right">14,096</td>
<td align="right">37.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
<td align="right">0.1%</td>
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
<td align="right">23,500,371</td>
<td align="right">57.4%</td>
<td align="right">5,578,746</td>
<td align="right">33.9%</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,406,083</td>
<td align="right">42.5%</td>
<td align="right">10,877,257</td>
<td align="right">66.1%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">6,990</td>
<td align="right">98.2%</td>
<td align="right">5,401</td>
<td align="right">97.7%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">125</td>
<td align="right">1.8%</td>
<td align="right">125</td>
<td align="right">2.3%</td>
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
<td align="right">5,035</td>
<td align="right">72.0%</td>
<td align="right">3,446</td>
<td align="right">63.8%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,474</td>
<td align="right">21.1%</td>
<td align="right">1,474</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">299</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">2.6%</td>
<td align="right">182</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
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
<td align="right">81,704,249</td>
<td align="right">44.1%</td>
<td align="right">45,984,726</td>
<td align="right">41.2%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">102,361,550</td>
<td align="right">55.2%</td>
<td align="right">64,338,258</td>
<td align="right">57.6%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,221,523</td>
<td align="right">0.7%</td>
<td align="right">1,236,547</td>
<td align="right">1.1%</td>
<td align="right">1.2%</td>
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
<td align="right">59,205</td>
<td align="right">71.4%</td>
<td align="right">50,790</td>
<td align="right">67.9%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23,751</td>
<td align="right">28.6%</td>
<td align="right">24,040</td>
<td align="right">32.1%</td>
<td align="right">1.2%</td>
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
<td align="right">4,200</td>
<td align="right">7.1%</td>
<td align="right">2,687</td>
<td align="right">5.3%</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">45,054</td>
<td align="right">76.1%</td>
<td align="right">38,104</td>
<td align="right">75.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,344</td>
<td align="right">10.7%</td>
<td align="right">6,389</td>
<td align="right">12.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,355</td>
<td align="right">2.3%</td>
<td align="right">1,359</td>
<td align="right">2.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.3%</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">194</td>
<td align="right">0.3%</td>
<td align="right">194</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">64</td>
<td align="right">0.1%</td>
<td align="right">64</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="left">enumerate</td>
<td align="right">157,916</td>
<td align="right">157,916 / 0 !!</td>
<td align="right">157,971</td>
<td align="right">157,971 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,186,578</td>
<td align="right">7,186,578 / 0 !!</td>
<td align="right">7,188,820</td>
<td align="right">7,188,820 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,496</td>
<td align="right">70,496 / 0 !!</td>
<td align="right">70,507</td>
<td align="right">70,507 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,715,666</td>
<td align="right">8,715,666 / 0 !!</td>
<td align="right">8,716,493</td>
<td align="right">8,716,493 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,354</td>
<td align="right">9,440,354 / 0 !!</td>
<td align="right">9,440,788</td>
<td align="right">9,440,788 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,233,818</td>
<td align="right">9,233,818 / 0 !!</td>
<td align="right">9,234,045</td>
<td align="right">9,234,045 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,236,517</td>
<td align="right">12,236,517 / 0 !!</td>
<td align="right">12,236,632</td>
<td align="right">12,236,632 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">70,736,325</td>
<td align="right">20.4%</td>
<td align="right">59,846,484</td>
<td align="right">19.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">223,130,840</td>
<td align="right">64.3%</td>
<td align="right">202,908,490</td>
<td align="right">64.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,240,890</td>
<td align="right">15.3%</td>
<td align="right">52,737,861</td>
<td align="right">16.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">47,737</td>
<td align="right">4.5%</td>
<td align="right">45,067</td>
<td align="right">4.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,015,300</td>
<td align="right">95.5%</td>
<td align="right">1,005,884</td>
<td align="right">95.7%</td>
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
<td align="left">builtin class method</td>
<td align="right">566</td>
<td align="right">1.2%</td>
<td align="right">206</td>
<td align="right">0.5%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,355</td>
<td align="right">9.1%</td>
<td align="right">3,112</td>
<td align="right">6.9%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,684</td>
<td align="right">5.6%</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,093</td>
<td align="right">14.9%</td>
<td align="right">6,815</td>
<td align="right">15.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,866</td>
<td align="right">45.8%</td>
<td align="right">21,422</td>
<td align="right">47.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,732</td>
<td align="right">5.7%</td>
<td align="right">2,739</td>
<td align="right">6.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,060</td>
<td align="right">8.5%</td>
<td align="right">4,067</td>
<td align="right">9.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,103</td>
<td align="right">6.5%</td>
<td align="right">3,103</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">291,706,621</td>
<td align="right">100.0%</td>
<td align="right">259,113,624</td>
<td align="right">100.0%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,534</td>
<td align="right">0.0%</td>
<td align="right">4,537</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,299</td>
<td align="right">0.0%</td>
<td align="right">1,299</td>
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
<td align="right">13,579</td>
<td align="right">100.0%</td>
<td align="right">13,584</td>
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
<td align="right">2,265,922</td>
<td align="right">100.0%</td>
<td align="right">2,266,032</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
<td align="right">731,601</td>
<td align="right">72.0%</td>
<td align="right">731,625</td>
<td align="right">72.0%</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
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
<td align="right">1.4%</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">1,108</td>
<td align="right">100.0%</td>
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
<td align="right">173,968</td>
<td align="right">1.9%</td>
<td align="right">174,053</td>
<td align="right">1.9%</td>
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
<td align="right">1,575,539</td>
<td align="right">17.4%</td>
<td align="right">1,574,913</td>
<td align="right">17.3%</td>
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
<td align="right">7,328,627</td>
<td align="right">80.7%</td>
<td align="right">7,329,893</td>
<td align="right">80.7%</td>
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
<td align="right">967</td>
<td align="right">3.1%</td>
<td align="right">972</td>
<td align="right">3.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">29,976</td>
<td align="right">96.9%</td>
<td align="right">29,961</td>
<td align="right">96.9%</td>
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
<td align="left">not managed dict</td>
<td align="right">290</td>
<td align="right">30.0%</td>
<td align="right">296</td>
<td align="right">30.5%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.6%</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">17,739,340</td>
<td align="right">87.3%</td>
<td align="right">17,674,847</td>
<td align="right">87.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,583,069</td>
<td align="right">12.7%</td>
<td align="right">2,583,562</td>
<td align="right">12.8%</td>
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
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,543</td>
<td align="right">72.8%</td>
<td align="right">1,543</td>
<td align="right">72.8%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,543</td>
<td align="right">100.0%</td>
<td align="right">1,543</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,427,216</td>
<td align="right">94.2%</td>
<td align="right">163,810,957</td>
<td align="right">94.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">623,358</td>
<td align="right">0.3%</td>
<td align="right">623,765</td>
<td align="right">0.4%</td>
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
<td align="right">9,755,754</td>
<td align="right">5.4%</td>
<td align="right">9,755,883</td>
<td align="right">5.6%</td>
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
<td align="right">14,274</td>
<td align="right">43.0%</td>
<td align="right">14,301</td>
<td align="right">43.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,958</td>
<td align="right">57.0%</td>
<td align="right">18,981</td>
<td align="right">57.0%</td>
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
<td align="left">set</td>
<td align="right">710</td>
<td align="right">5.0%</td>
<td align="right">723</td>
<td align="right">5.1%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,261</td>
<td align="right">8.8%</td>
<td align="right">1,267</td>
<td align="right">8.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">724</td>
<td align="right">5.1%</td>
<td align="right">725</td>
<td align="right">5.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,608</td>
<td align="right">18.3%</td>
<td align="right">2,610</td>
<td align="right">18.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,002</td>
<td align="right">56.1%</td>
<td align="right">8,007</td>
<td align="right">56.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">83,627,436</td>
<td align="right">100.0%</td>
<td align="right">57,009,812</td>
<td align="right">100.0%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,268</td>
<td align="right">0.0%</td>
<td align="right">6,343</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
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
<td align="right">302</td>
<td align="right">11.2%</td>
<td align="right">307</td>
<td align="right">11.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,391</td>
<td align="right">88.8%</td>
<td align="right">2,391</td>
<td align="right">88.6%</td>
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
<td align="right">259</td>
<td align="right">85.8%</td>
<td align="right">264</td>
<td align="right">86.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.2%</td>
<td align="right">43</td>
<td align="right">14.0%</td>
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
<td align="right">306,182,778</td>
<td align="right">6.4%</td>
<td align="right">249,732,164</td>
<td align="right">5.8%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,642,167,899</td>
<td align="right">34.2%</td>
<td align="right">1,410,469,653</td>
<td align="right">32.9%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,756,743,460</td>
<td align="right">57.4%</td>
<td align="right">2,536,311,251</td>
<td align="right">59.1%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">93,920,395</td>
<td align="right">2.0%</td>
<td align="right">93,642,111</td>
<td align="right">2.2%</td>
<td align="right">-0.3%</td>
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
<td align="right">81,704,249</td>
<td align="right">27.7%</td>
<td align="right">45,984,726</td>
<td align="right">19.1%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,406,083</td>
<td align="right">5.9%</td>
<td align="right">10,877,257</td>
<td align="right">4.5%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,736,325</td>
<td align="right">24.0%</td>
<td align="right">59,846,484</td>
<td align="right">24.9%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,772,386</td>
<td align="right">15.5%</td>
<td align="right">44,657,339</td>
<td align="right">18.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,754,338</td>
<td align="right">12.1%</td>
<td align="right">35,960,340</td>
<td align="right">14.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,442,758</td>
<td align="right">10.3%</td>
<td align="right">30,422,484</td>
<td align="right">12.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,968</td>
<td align="right">0.1%</td>
<td align="right">174,053</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,069</td>
<td align="right">0.9%</td>
<td align="right">2,583,562</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,754</td>
<td align="right">3.3%</td>
<td align="right">9,755,883</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,291,014</td>
<td align="right">14.2%</td>
<td align="right">12,855,340</td>
<td align="right">13.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,265,813</td>
<td align="right">12.0%</td>
<td align="right">11,472,265</td>
<td align="right">12.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,201,669</td>
<td align="right">3.4%</td>
<td align="right">3,210,441</td>
<td align="right">3.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,019,854</td>
<td align="right">30.9%</td>
<td align="right">28,941,703</td>
<td align="right">30.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,574,760</td>
<td align="right">1.7%</td>
<td align="right">1,574,134</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,701,049</td>
<td align="right">12.5%</td>
<td align="right">11,704,349</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,384</td>
<td align="right">7.8%</td>
<td align="right">7,313,416</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,150,816</td>
<td align="right">6.5%</td>
<td align="right">6,150,935</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,559</td>
<td align="right">5.4%</td>
<td align="right">5,102,610</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,571</td>
<td align="right">2.2%</td>
<td align="right">2,103,591</td>
<td align="right">2.2%</td>
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
<td align="right">131,355,839</td>
<td align="right">62.5%</td>
<td align="right">131,554,290</td>
<td align="right">62.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,277</td>
<td align="right">0.5%</td>
<td align="right">950,436</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,702</td>
<td align="right">1.6%</td>
<td align="right">3,468,967</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,137,062</td>
<td align="right">19.6%</td>
<td align="right">41,135,416</td>
<td align="right">19.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,373</td>
<td align="right">8.8%</td>
<td align="right">18,490,979</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,672,851</td>
<td align="right">89.3%</td>
<td align="right">187,667,664</td>
<td align="right">89.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,972</td>
<td align="right">4.4%</td>
<td align="right">9,332,170</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,420,700</td>
<td align="right">35.9%</td>
<td align="right">75,419,995</td>
<td align="right">35.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,421,485</td>
<td align="right">35.9%</td>
<td align="right">75,420,780</td>
<td align="right">35.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,890,187</td>
<td align="right">37.5%</td>
<td align="right">78,889,747</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,890,187</td>
<td align="right">37.5%</td>
<td align="right">78,889,747</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">416</td>
<td align="right">0.0%</td>
<td align="right">416</td>
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
<td align="right">2,257,293</td>
<td align="right"></td>
<td align="right">2,588,102</td>
<td align="right"></td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,519,733</td>
<td align="right"></td>
<td align="right">3,806,681</td>
<td align="right"></td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,263,865</td>
<td align="right"></td>
<td align="right">1,220,030</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">758,899</td>
<td align="right">0.2%</td>
<td align="right">769,357</td>
<td align="right">0.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,283,223,314</td>
<td align="right">37.4%</td>
<td align="right">1,271,665,673</td>
<td align="right">37.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,600,795,705</td>
<td align="right">40.9%</td>
<td align="right">1,589,448,734</td>
<td align="right">40.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">150,541,025</td>
<td align="right"></td>
<td align="right">149,706,015</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,931</td>
<td align="right">0.0%</td>
<td align="right">8,976</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">970,331,007</td>
<td align="right">28.3%</td>
<td align="right">969,854,044</td>
<td align="right">28.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,084,650</td>
<td align="right">26.8%</td>
<td align="right">129,111,740</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,099,927,247</td>
<td align="right">32.0%</td>
<td align="right">1,100,132,372</td>
<td align="right">32.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,739,488</td>
<td align="right"></td>
<td align="right">141,765,385</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,248</td>
<td align="right"></td>
<td align="right">866,393</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,968,587</td>
<td align="right"></td>
<td align="right">249,002,274</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,316,820</td>
<td align="right">26.6%</td>
<td align="right">128,333,407</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">79,098,721</td>
<td align="right">2.3%</td>
<td align="right">79,107,100</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,424,109</td>
<td align="right">1.3%</td>
<td align="right">51,419,872</td>
<td align="right">1.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,055,507,610</td>
<td align="right">27.0%</td>
<td align="right">1,055,471,252</td>
<td align="right">27.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">352,550,148</td>
<td align="right"></td>
<td align="right">352,556,077</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">352,514,962</td>
<td align="right">73.2%</td>
<td align="right">352,520,888</td>
<td align="right">73.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,203,828,349</td>
<td align="right">30.8%</td>
<td align="right">1,203,843,918</td>
<td align="right">30.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">2</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-18
