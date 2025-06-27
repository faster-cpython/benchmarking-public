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
<td align="left">LOAD_LOCALS</td>
<td align="right">298</td>
<td align="right">6,258</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">175</td>
<td align="right">3,675</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">2,457</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">74</td>
<td align="right">1,554</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">336</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">14</td>
<td align="right">294</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">189</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">25,302</td>
<td align="right">521,094</td>
<td align="right">1,959.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,055</td>
<td align="right">62,734</td>
<td align="right">1,953.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">499</td>
<td align="right">10,019</td>
<td align="right">1,907.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,526</td>
<td align="right">455,616</td>
<td align="right">1,836.6%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,335</td>
<td align="right">25,473</td>
<td align="right">1,808.1%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">348</td>
<td align="right">6,027</td>
<td align="right">1,631.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">39,010</td>
<td align="right">386,916</td>
<td align="right">891.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">2,079</td>
<td align="right">702.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">98</td>
<td align="right">777</td>
<td align="right">692.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,074</td>
<td align="right">11,554</td>
<td align="right">457.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,681</td>
<td align="right">115,830</td>
<td align="right">434.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,436</td>
<td align="right">50,064</td>
<td align="right">379.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,670,243</td>
<td align="right">5,462,352</td>
<td align="right">227.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,831,488</td>
<td align="right">5,753,475</td>
<td align="right">214.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">36,236</td>
<td align="right">88,431</td>
<td align="right">144.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">27,626</td>
<td align="right">66,465</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,141</td>
<td align="right">15,960</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">257,895</td>
<td align="right">501,619</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">703,203</td>
<td align="right">1,228,374</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,987</td>
<td align="right">50,251</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,473</td>
<td align="right">37,170</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">152,965</td>
<td align="right">261,862</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,488,263</td>
<td align="right">5,145,336</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">14,055,631</td>
<td align="right">20,264,110</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,865</td>
<td align="right">114,345</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">85,415</td>
<td align="right">121,770</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">346,538</td>
<td align="right">479,872</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,593</td>
<td align="right">48,027</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">42</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">771,188</td>
<td align="right">1,012,880</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,795,369</td>
<td align="right">2,336,901</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,506,138</td>
<td align="right">3,220,528</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,698,989</td>
<td align="right">7,293,999</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">641,274</td>
<td align="right">814,246</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">119,001</td>
<td align="right">149,667</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,051,102</td>
<td align="right">3,826,557</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,356,668</td>
<td align="right">4,159,428</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,088,446</td>
<td align="right">1,329,665</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,264,113</td>
<td align="right">5,185,858</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,982,306</td>
<td align="right">5,883,842</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,744,861</td>
<td align="right">2,043,552</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">598,966</td>
<td align="right">693,168</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,498,533</td>
<td align="right">2,886,693</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,745</td>
<td align="right">636,846</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">147</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,432</td>
<td align="right">268,926</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,356,136</td>
<td align="right">1,527,981</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,566,181</td>
<td align="right">1,736,522</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,696</td>
<td align="right">26,208</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,667</td>
<td align="right">292,824</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,482,379</td>
<td align="right">4,911,437</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,496,293</td>
<td align="right">23,418,066</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">893,153</td>
<td align="right">970,368</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">728,750</td>
<td align="right">791,301</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,115,821</td>
<td align="right">4,461,011</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,504,685</td>
<td align="right">3,771,836</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">744,012</td>
<td align="right">800,260</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">25,358,144</td>
<td align="right">27,148,511</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,256</td>
<td align="right">8,631</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,985</td>
<td align="right">82,047</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,470,462</td>
<td align="right">4,762,634</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,830</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,747,975</td>
<td align="right">7,174,813</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,654,873</td>
<td align="right">10,251,900</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,089,724</td>
<td align="right">5,404,104</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,512,507</td>
<td align="right">1,605,926</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">2,019,480</td>
<td align="right">2,141,685</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">25,183</td>
<td align="right">26,691</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,581,572</td>
<td align="right">2,724,498</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,852</td>
<td align="right">528,898</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,624</td>
<td align="right">157,374</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,663,992</td>
<td align="right">5,943,030</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,480</td>
<td align="right">152,838</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">171,190,050</td>
<td align="right">177,904,036</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,752</td>
<td align="right">1,134,400</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">74,871,795</td>
<td align="right">77,674,731</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">115,032,428</td>
<td align="right">119,328,183</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,991,302</td>
<td align="right">11,388,227</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">101,035,101</td>
<td align="right">104,570,540</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,771,478</td>
<td align="right">4,925,870</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,724</td>
<td align="right">859,927</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,587,285</td>
<td align="right">19,082,292</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,277,896</td>
<td align="right">3,360,444</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">10,561</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,651,485</td>
<td align="right">9,869,469</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">14,190,549</td>
<td align="right">14,501,918</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,851,503</td>
<td align="right">66,250,264</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">176,631,714</td>
<td align="right">180,226,755</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">50,353,459</td>
<td align="right">51,353,822</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">166,706,499</td>
<td align="right">169,795,904</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,774,932</td>
<td align="right">18,089,982</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,318,107</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,687,394</td>
<td align="right">2,642,388</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">83,055</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">10,092,115</td>
<td align="right">10,250,394</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,560</td>
<td align="right">2,520</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,205</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,888,516</td>
<td align="right">38,282,244</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">61,068,659</td>
<td align="right">60,118,084</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,220,608</td>
<td align="right">9,364,019</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,529,039</td>
<td align="right">38,929,372</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">601,071,498</td>
<td align="right">610,007,243</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,682,087</td>
<td align="right">7,569,380</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,851</td>
<td align="right">5,599,881</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,568,625</td>
<td align="right">5,490,197</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,681,604</td>
<td align="right">22,362,992</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,085</td>
<td align="right">130,851</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">192,022</td>
<td align="right">194,586</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,753,821</td>
<td align="right">127,420,633</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,825</td>
<td align="right">16,743,237</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,558,371</td>
<td align="right">6,642,698</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">16,191</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">87,169,018</td>
<td align="right">86,127,913</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">88,938,723</td>
<td align="right">87,902,812</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,745</td>
<td align="right">300,198</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,798</td>
<td align="right">7,224,041</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,610</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,706</td>
<td align="right">8,610</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">11,075,172</td>
<td align="right">11,195,952</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">87,035,864</td>
<td align="right">86,108,146</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">2,164,748</td>
<td align="right">2,186,247</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,745,945</td>
<td align="right">11,861,408</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,960,117</td>
<td align="right">2,931,841</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,114,356</td>
<td align="right">38,756,886</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,391,617</td>
<td align="right">1,379,280</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,344,080</td>
<td align="right">15,212,218</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">35,907,018</td>
<td align="right">35,607,307</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,271,698</td>
<td align="right">1,261,155</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">11,031,725</td>
<td align="right">11,119,017</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">74,074,301</td>
<td align="right">73,496,911</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,565</td>
<td align="right">1,270,584</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">196,240</td>
<td align="right">194,775</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">141,312,632</td>
<td align="right">140,260,253</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,623,514</td>
<td align="right">1,635,556</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">49,021,717</td>
<td align="right">48,662,966</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,668,717</td>
<td align="right">1,680,433</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,668,717</td>
<td align="right">1,680,433</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,335,310</td>
<td align="right">17,215,983</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,267,357</td>
<td align="right">1,276,077</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,024</td>
<td align="right">2,669,058</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,873,478</td>
<td align="right">20,741,154</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,489,315</td>
<td align="right">16,389,793</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">101,968,361</td>
<td align="right">102,538,636</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,566,501</td>
<td align="right">156,431,527</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,533,759</td>
<td align="right">3,514,432</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,148</td>
<td align="right">2,957,001</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">78,583,093</td>
<td align="right">78,161,792</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,427,856</td>
<td align="right">8,388,743</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,366,577</td>
<td align="right">10,318,749</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,644,824</td>
<td align="right">4,623,789</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,599</td>
<td align="right">2,962,124</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,311</td>
<td align="right">5,925,804</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,435</td>
<td align="right">157,941</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,578,726</td>
<td align="right">4,592,490</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">170,348</td>
<td align="right">169,848</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">55,552,935</td>
<td align="right">55,691,286</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,054,833</td>
<td align="right">180,468,057</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">39,964,533</td>
<td align="right">40,049,777</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,540,232</td>
<td align="right">4,548,873</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">17,570,847</td>
<td align="right">17,539,272</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">13,398,906</td>
<td align="right">13,375,413</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">137,874,669</td>
<td align="right">137,639,099</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,982,200</td>
<td align="right">18,011,771</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,708,097</td>
<td align="right">28,751,078</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">481,258</td>
<td align="right">481,004</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,508,922</td>
<td align="right">84,471,570</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,415,041</td>
<td align="right">17,419,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">13,633,951</td>
<td align="right">13,636,998</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,032,966</td>
<td align="right">38,037,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,187</td>
<td align="right">1,133,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">66,719,618</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,270,875</td>
<td align="right">5.0%</td>
<td align="right">3,473,658</td>
<td align="right">5.0%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">53,401,490</td>
<td align="right">81.0%</td>
<td align="right">56,516,148</td>
<td align="right">81.5%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,181,982</td>
<td align="right">13.9%</td>
<td align="right">9,293,236</td>
<td align="right">13.4%</td>
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
<td align="right">36,634</td>
<td align="right">36.6%</td>
<td align="right">55,491</td>
<td align="right">40.8%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,550</td>
<td align="right">63.4%</td>
<td align="right">80,392</td>
<td align="right">59.2%</td>
<td align="right">26.5%</td>
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
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">666.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">130</td>
<td align="right">0.4%</td>
<td align="right">489</td>
<td align="right">0.9%</td>
<td align="right">276.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">196</td>
<td align="right">0.5%</td>
<td align="right">693</td>
<td align="right">1.2%</td>
<td align="right">253.6%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">698</td>
<td align="right">1.9%</td>
<td align="right">2,352</td>
<td align="right">4.2%</td>
<td align="right">237.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,504</td>
<td align="right">4.1%</td>
<td align="right">4,515</td>
<td align="right">8.1%</td>
<td align="right">200.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">535</td>
<td align="right">1.5%</td>
<td align="right">1,512</td>
<td align="right">2.7%</td>
<td align="right">182.6%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">315</td>
<td align="right">0.6%</td>
<td align="right">171.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">9.3%</td>
<td align="right">8,966</td>
<td align="right">16.2%</td>
<td align="right">163.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,349</td>
<td align="right">6.4%</td>
<td align="right">6,069</td>
<td align="right">10.9%</td>
<td align="right">158.4%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">254</td>
<td align="right">0.7%</td>
<td align="right">651</td>
<td align="right">1.2%</td>
<td align="right">156.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">0.6%</td>
<td align="right">546</td>
<td align="right">1.0%</td>
<td align="right">138.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">272</td>
<td align="right">0.7%</td>
<td align="right">630</td>
<td align="right">1.1%</td>
<td align="right">131.6%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">92</td>
<td align="right">0.3%</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">126</td>
<td align="right">0.2%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,632</td>
<td align="right">7.2%</td>
<td align="right">3,654</td>
<td align="right">6.6%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">23,921</td>
<td align="right">65.3%</td>
<td align="right">24,108</td>
<td align="right">43.4%</td>
<td align="right">0.8%</td>
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
<td align="right">3,504,685</td>
<td align="right">100.0%</td>
<td align="right">3,771,836</td>
<td align="right">100.0%</td>
<td align="right">7.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,897,757</td>
<td align="right">0.8%</td>
<td align="right">2,235,141</td>
<td align="right">0.9%</td>
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
<td align="right">1,918,972</td>
<td align="right">0.8%</td>
<td align="right">1,965,490</td>
<td align="right">0.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">240,324,770</td>
<td align="right">99.2%</td>
<td align="right">242,640,064</td>
<td align="right">99.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,965,490</td>
<td align="right">0.8%</td>
<td align="right"></td>
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
<td align="right">60,225</td>
<td align="right">100.0%</td>
<td align="right">117,265</td>
<td align="right">100.0%</td>
<td align="right">94.7%</td>
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
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">1,344</td>
<td align="right">1,344 / 0 !!</td>
<td align="right">217.0%</td>
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
<td align="right">386</td>
<td align="right">18.1%</td>
<td align="right">6,785</td>
<td align="right">58.4%</td>
<td align="right">1,657.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64</td>
<td align="right">3.0%</td>
<td align="right">63</td>
<td align="right">0.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">0.5%</td>
<td align="right"></td>
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
<td align="right">1,752</td>
<td align="right">100.0%</td>
<td align="right">4,832</td>
<td align="right">100.0%</td>
<td align="right">175.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,063</td>
<td align="right">0.1%</td>
<td align="right">11,757</td>
<td align="right">0.1%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">637,370</td>
<td align="right">5.5%</td>
<td align="right">801,814</td>
<td align="right">5.9%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,927,130</td>
<td align="right">94.4%</td>
<td align="right">12,839,184</td>
<td align="right">94.0%</td>
<td align="right">17.5%</td>
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
<td align="right">1,345</td>
<td align="right">33.3%</td>
<td align="right">6,801</td>
<td align="right">53.9%</td>
<td align="right">405.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,690</td>
<td align="right">66.7%</td>
<td align="right">5,820</td>
<td align="right">46.1%</td>
<td align="right">116.4%</td>
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
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27</td>
<td align="right">1.0%</td>
<td align="right">147</td>
<td align="right">2.5%</td>
<td align="right">444.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">107</td>
<td align="right">4.0%</td>
<td align="right">426</td>
<td align="right">7.3%</td>
<td align="right">298.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.6%</td>
<td align="right">777</td>
<td align="right">13.4%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">251</td>
<td align="right">9.3%</td>
<td align="right">630</td>
<td align="right">10.8%</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">156</td>
<td align="right">5.8%</td>
<td align="right">336</td>
<td align="right">5.8%</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,825</td>
<td align="right">67.8%</td>
<td align="right">3,399</td>
<td align="right">58.4%</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">63</td>
<td align="right">1.1%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
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
<td align="right">4,476,768</td>
<td align="right">27.6%</td>
<td align="right">4,892,978</td>
<td align="right">28.4%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,734,928</td>
<td align="right">72.4%</td>
<td align="right">12,347,391</td>
<td align="right">71.5%</td>
<td align="right">5.2%</td>
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
<td align="right">529</td>
<td align="right">9.4%</td>
<td align="right">2,709</td>
<td align="right">14.7%</td>
<td align="right">412.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,082</td>
<td align="right">90.6%</td>
<td align="right">15,750</td>
<td align="right">85.3%</td>
<td align="right">209.9%</td>
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
<td align="right">1,487</td>
<td align="right">29.3%</td>
<td align="right">4,893</td>
<td align="right">31.1%</td>
<td align="right">229.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,238</td>
<td align="right">44.0%</td>
<td align="right">6,972</td>
<td align="right">44.3%</td>
<td align="right">211.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">730</td>
<td align="right">14.4%</td>
<td align="right">2,205</td>
<td align="right">14.0%</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">627</td>
<td align="right">12.3%</td>
<td align="right">1,680</td>
<td align="right">10.7%</td>
<td align="right">167.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">144,857,629</td>
<td align="right">77.7%</td>
<td align="right">147,380,370</td>
<td align="right">78.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,023,837</td>
<td align="right">15.0%</td>
<td align="right">27,595,407</td>
<td align="right">14.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,626,778</td>
<td align="right">7.3%</td>
<td align="right">13,613,456</td>
<td align="right">7.2%</td>
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
<td align="right">6,518</td>
<td align="right">1.2%</td>
<td align="right">16,047</td>
<td align="right">2.9%</td>
<td align="right">146.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">529,386</td>
<td align="right">98.8%</td>
<td align="right">528,085</td>
<td align="right">97.1%</td>
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
<td align="left">other</td>
<td align="right">60</td>
<td align="right">0.9%</td>
<td align="right">420</td>
<td align="right">2.6%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">51</td>
<td align="right">0.8%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">49</td>
<td align="right">0.8%</td>
<td align="right">189</td>
<td align="right">1.2%</td>
<td align="right">285.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">5.4%</td>
<td align="right">987</td>
<td align="right">6.2%</td>
<td align="right">181.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,653</td>
<td align="right">25.4%</td>
<td align="right">4,641</td>
<td align="right">28.9%</td>
<td align="right">180.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">7.2%</td>
<td align="right">1,281</td>
<td align="right">8.0%</td>
<td align="right">173.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.5%</td>
<td align="right">255</td>
<td align="right">1.6%</td>
<td align="right">162.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.2%</td>
<td align="right">651</td>
<td align="right">4.1%</td>
<td align="right">139.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">594</td>
<td align="right">9.1%</td>
<td align="right">1,407</td>
<td align="right">8.8%</td>
<td align="right">136.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">794</td>
<td align="right">12.2%</td>
<td align="right">1,806</td>
<td align="right">11.3%</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">319</td>
<td align="right">4.9%</td>
<td align="right">714</td>
<td align="right">4.4%</td>
<td align="right">123.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,809</td>
<td align="right">27.8%</td>
<td align="right">3,486</td>
<td align="right">21.7%</td>
<td align="right">92.7%</td>
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
<td align="right">33,626</td>
<td align="right">33,626 / 0 !!</td>
<td align="right">44,890</td>
<td align="right">44,890 / 0 !!</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">39,247,173</td>
<td align="right">39,247,173 / 0 !!</td>
<td align="right">38,634,036</td>
<td align="right">38,634,036 / 0 !!</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,653,374</td>
<td align="right">3,653,374 / 0 !!</td>
<td align="right">3,706,416</td>
<td align="right">3,706,416 / 0 !!</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">21,178,627</td>
<td align="right">21,178,627 / 0 !!</td>
<td align="right">20,927,193</td>
<td align="right">20,927,193 / 0 !!</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">149,323</td>
<td align="right">149,323 / 0 !!</td>
<td align="right">151,053</td>
<td align="right">151,053 / 0 !!</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">218,685</td>
<td align="right">218,685 / 0 !!</td>
<td align="right">216,249</td>
<td align="right">216,249 / 0 !!</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">24,403,476</td>
<td align="right">24,403,476 / 0 !!</td>
<td align="right">24,168,606</td>
<td align="right">24,168,606 / 0 !!</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,730</td>
<td align="right">1,730 / 0 !!</td>
<td align="right">1,743</td>
<td align="right">1,743 / 0 !!</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">52,709</td>
<td align="right">52,709 / 0 !!</td>
<td align="right">52,626</td>
<td align="right">52,626 / 0 !!</td>
<td align="right">-0.2%</td>
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
<td align="right">64,390</td>
<td align="right">0.0%</td>
<td align="right">62,727</td>
<td align="right">0.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140,840,380</td>
<td align="right">34.6%</td>
<td align="right">138,917,247</td>
<td align="right">34.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">216,725,976</td>
<td align="right">53.3%</td>
<td align="right">219,186,999</td>
<td align="right">53.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">48,436,238</td>
<td align="right">11.9%</td>
<td align="right">47,980,773</td>
<td align="right">11.8%</td>
<td align="right">-0.9%</td>
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
<td align="right">181,814</td>
<td align="right">6.4%</td>
<td align="right">198,348</td>
<td align="right">6.8%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,660,422</td>
<td align="right">93.6%</td>
<td align="right">2,702,201</td>
<td align="right">93.2%</td>
<td align="right">1.6%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">504</td>
<td align="right">0.3%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">210</td>
<td align="right">0.1%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,314</td>
<td align="right">0.7%</td>
<td align="right">3,780</td>
<td align="right">1.9%</td>
<td align="right">187.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,250</td>
<td align="right">1.8%</td>
<td align="right">8,274</td>
<td align="right">4.2%</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">996</td>
<td align="right">0.5%</td>
<td align="right">2,268</td>
<td align="right">1.1%</td>
<td align="right">127.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,860</td>
<td align="right">1.6%</td>
<td align="right">5,922</td>
<td align="right">3.0%</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">66</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">646</td>
<td align="right">0.4%</td>
<td align="right">1,176</td>
<td align="right">0.6%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">764</td>
<td align="right">0.4%</td>
<td align="right">1,074</td>
<td align="right">0.5%</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">0.2%</td>
<td align="right">399</td>
<td align="right">0.2%</td>
<td align="right">23.5%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,812</td>
<td align="right">0.0%</td>
<td align="right">58,198</td>
<td align="right">0.0%</td>
<td align="right">1,969.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,994</td>
<td align="right">0.0%</td>
<td align="right">111,384</td>
<td align="right">0.1%</td>
<td align="right">695.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">212,732,470</td>
<td align="right">100.0%</td>
<td align="right">215,202,446</td>
<td align="right">99.9%</td>
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
<td align="left">Success</td>
<td align="right">19,337</td>
<td align="right">100.0%</td>
<td align="right">59,858</td>
<td align="right">100.0%</td>
<td align="right">209.6%</td>
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
<td align="right">50</td>
<td align="right">0.0%</td>
<td align="right">1,050</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">425,102</td>
<td align="right">99.9%</td>
<td align="right">450,765</td>
<td align="right">99.5%</td>
<td align="right">6.0%</td>
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
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">1,029</td>
<td align="right">100.0%</td>
<td align="right">392.3%</td>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
<td align="right">4,620</td>
<td align="right">30.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
<td align="right">10,561</td>
<td align="right">68.6%</td>
<td align="right">-2.3%</td>
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
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">84</td>
<td align="right">40.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
<td align="right">126</td>
<td align="right">60.0%</td>
<td align="right">168.1%</td>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">168.1%</td>
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
<td align="right">14,061,839</td>
<td align="right">41.3%</td>
<td align="right">16,133,668</td>
<td align="right">44.9%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,609,951</td>
<td align="right">28.2%</td>
<td align="right">9,462,432</td>
<td align="right">26.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,351,515</td>
<td align="right">30.4%</td>
<td align="right">10,279,626</td>
<td align="right">28.6%</td>
<td align="right">-0.7%</td>
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
<td align="right">9,915</td>
<td align="right">5.1%</td>
<td align="right">23,856</td>
<td align="right">11.0%</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">185,984</td>
<td align="right">94.9%</td>
<td align="right">192,612</td>
<td align="right">89.0%</td>
<td align="right">3.6%</td>
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
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">105</td>
<td align="right">0.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">290</td>
<td align="right">2.9%</td>
<td align="right">2,667</td>
<td align="right">11.2%</td>
<td align="right">819.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">119</td>
<td align="right">1.2%</td>
<td align="right">378</td>
<td align="right">1.6%</td>
<td align="right">217.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.9%</td>
<td align="right">273</td>
<td align="right">1.1%</td>
<td align="right">190.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">5,037</td>
<td align="right">50.8%</td>
<td align="right">12,201</td>
<td align="right">51.1%</td>
<td align="right">142.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.5%</td>
<td align="right">1,512</td>
<td align="right">6.3%</td>
<td align="right">135.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">311</td>
<td align="right">3.1%</td>
<td align="right">651</td>
<td align="right">2.7%</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.5%</td>
<td align="right">4,263</td>
<td align="right">17.9%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">170,810</td>
<td align="right">1,722.7%</td>
<td align="right">172,788</td>
<td align="right">724.3%</td>
<td align="right">1.2%</td>
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
<td align="right">196,240</td>
<td align="right">100.0%</td>
<td align="right">194,775</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,666,247</td>
<td align="right">15.4%</td>
<td align="right">5,450,046</td>
<td align="right">37.2%</td>
<td align="right">227.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,606</td>
<td align="right">84.6%</td>
<td align="right">9,180,044</td>
<td align="right">62.7%</td>
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
<td align="right">475</td>
<td align="right">11.9%</td>
<td align="right">2,835</td>
<td align="right">23.0%</td>
<td align="right">496.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,521</td>
<td align="right">88.1%</td>
<td align="right">9,471</td>
<td align="right">77.0%</td>
<td align="right">169.0%</td>
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
<td align="right">59</td>
<td align="right">1.7%</td>
<td align="right">1,239</td>
<td align="right">13.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,962</td>
<td align="right">84.1%</td>
<td align="right">7,119</td>
<td align="right">75.2%</td>
<td align="right">140.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">46</td>
<td align="right">1.3%</td>
<td align="right">105</td>
<td align="right">1.1%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.2%</td>
<td align="right">252</td>
<td align="right">2.7%</td>
<td align="right">123.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.7%</td>
<td align="right">756</td>
<td align="right">8.0%</td>
<td align="right">121.7%</td>
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
<td align="right">15,192,519</td>
<td align="right">8.0%</td>
<td align="right">15,035,626</td>
<td align="right">7.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,516,596</td>
<td align="right">2.9%</td>
<td align="right">5,491,983</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,017,952</td>
<td align="right">89.0%</td>
<td align="right">168,454,342</td>
<td align="right">89.1%</td>
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
<td align="right">107,968</td>
<td align="right">42.2%</td>
<td align="right">126,213</td>
<td align="right">45.1%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">147,599</td>
<td align="right">57.8%</td>
<td align="right">153,531</td>
<td align="right">54.9%</td>
<td align="right">4.0%</td>
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
<td align="right">243</td>
<td align="right">0.2%</td>
<td align="right">1,281</td>
<td align="right">0.8%</td>
<td align="right">427.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">118</td>
<td align="right">0.1%</td>
<td align="right">336</td>
<td align="right">0.2%</td>
<td align="right">184.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">4,956</td>
<td align="right">3.2%</td>
<td align="right">138.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">880</td>
<td align="right">0.6%</td>
<td align="right">1,512</td>
<td align="right">1.0%</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,929</td>
<td align="right">6.7%</td>
<td align="right">11,676</td>
<td align="right">7.6%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">134,241</td>
<td align="right">90.9%</td>
<td align="right">133,623</td>
<td align="right">87.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">14,609,475</td>
<td align="right">98.0%</td>
<td align="right">14,985,714</td>
<td align="right">98.0%</td>
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
<td align="right">296,267</td>
<td align="right">2.0%</td>
<td align="right">295,661</td>
<td align="right">1.9%</td>
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
<td align="right">381</td>
<td align="right">79.7%</td>
<td align="right">4,201</td>
<td align="right">92.6%</td>
<td align="right">1,002.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">20.3%</td>
<td align="right">336</td>
<td align="right">7.4%</td>
<td align="right">246.4%</td>
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
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">273</td>
<td align="right">81.2%</td>
<td align="right">268.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">63</td>
<td align="right">18.8%</td>
<td align="right">173.9%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,084,923,593</td>
<td align="right">53.7%</td>
<td align="right">2,195,478,763</td>
<td align="right">54.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">197,384,787</td>
<td align="right">5.1%</td>
<td align="right">201,073,815</td>
<td align="right">5.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,408,599,749</td>
<td align="right">36.3%</td>
<td align="right">1,428,867,807</td>
<td align="right">35.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">189,204,799</td>
<td align="right">4.9%</td>
<td align="right">187,031,524</td>
<td align="right">4.7%</td>
<td align="right">-1.1%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">1,666,247</td>
<td align="right">1.5%</td>
<td align="right">5,450,046</td>
<td align="right">4.8%</td>
<td align="right">227.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">637,370</td>
<td align="right">0.6%</td>
<td align="right">801,814</td>
<td align="right">0.7%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,897,757</td>
<td align="right">1.7%</td>
<td align="right">2,235,141</td>
<td align="right">2.0%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,476,768</td>
<td align="right">4.1%</td>
<td align="right">4,892,978</td>
<td align="right">4.3%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,504,685</td>
<td align="right">3.2%</td>
<td align="right">3,771,836</td>
<td align="right">3.3%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,181,982</td>
<td align="right">8.4%</td>
<td align="right">9,293,236</td>
<td align="right">8.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,192,519</td>
<td align="right">13.9%</td>
<td align="right">15,035,626</td>
<td align="right">13.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,436,238</td>
<td align="right">44.2%</td>
<td align="right">47,980,773</td>
<td align="right">42.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,351,515</td>
<td align="right">9.5%</td>
<td align="right">10,279,626</td>
<td align="right">9.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">13,626,778</td>
<td align="right">12.4%</td>
<td align="right">13,613,456</td>
<td align="right">12.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">55,576,202</td>
<td align="right">29.4%</td>
<td align="right">54,675,306</td>
<td align="right">29.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,348,805</td>
<td align="right">5.5%</td>
<td align="right">10,183,383</td>
<td align="right">5.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">5.1%</td>
<td align="right">9,406,950</td>
<td align="right">5.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,011,338</td>
<td align="right">7.4%</td>
<td align="right">13,794,816</td>
<td align="right">7.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">14,012,499</td>
<td align="right">7.4%</td>
<td align="right">13,800,591</td>
<td align="right">7.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">42,021,300</td>
<td align="right">22.2%</td>
<td align="right">41,393,772</td>
<td align="right">22.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,738</td>
<td align="right">4.1%</td>
<td align="right">7,587,951</td>
<td align="right">4.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,462,137</td>
<td align="right">2.4%</td>
<td align="right">4,407,396</td>
<td align="right">2.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,518,033</td>
<td align="right">12.4%</td>
<td align="right">23,384,508</td>
<td align="right">12.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,342,054</td>
<td align="right">1.2%</td>
<td align="right">2,345,112</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">5,376</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,335</td>
<td align="right">0.0%</td>
<td align="right">25,473</td>
<td align="right">0.0%</td>
<td align="right">1,808.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">387</td>
<td align="right">0.0%</td>
<td align="right">6,846</td>
<td align="right">0.0%</td>
<td align="right">1,669.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">543,391</td>
<td align="right">0.2%</td>
<td align="right">584,980</td>
<td align="right">0.3%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,548,632</td>
<td align="right">8.4%</td>
<td align="right">18,307,548</td>
<td align="right">8.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,485,129</td>
<td align="right">4.8%</td>
<td align="right">10,614,999</td>
<td align="right">4.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,520,187</td>
<td align="right">72.2%</td>
<td align="right">159,385,358</td>
<td align="right">72.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,516</td>
<td align="right">0.2%</td>
<td align="right">500,829</td>
<td align="right">0.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,756,689</td>
<td align="right">3.1%</td>
<td align="right">6,770,069</td>
<td align="right">3.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,612,057</td>
<td align="right">18.0%</td>
<td align="right">39,553,309</td>
<td align="right">18.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">179,431,101</td>
<td align="right">81.7%</td>
<td align="right">179,290,878</td>
<td align="right">81.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,613,779</td>
<td align="right">18.0%</td>
<td align="right">39,585,628</td>
<td align="right">18.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,157,170</td>
<td align="right">18.3%</td>
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,157,170</td>
<td align="right">18.3%</td>
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,111</td>
<td align="right">0.0%</td>
<td align="right">84,871</td>
<td align="right">0.0%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,419,309</td>
<td align="right">0.6%</td>
<td align="right">1,549,096</td>
<td align="right">0.6%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,913,364</td>
<td align="right"></td>
<td align="right">9,049,466</td>
<td align="right"></td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">12,266,888</td>
<td align="right"></td>
<td align="right">11,245,187</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,080,765</td>
<td align="right"></td>
<td align="right">3,323,355</td>
<td align="right"></td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,355,189</td>
<td align="right"></td>
<td align="right">2,216,640</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">108,430,748</td>
<td align="right"></td>
<td align="right">114,189,395</td>
<td align="right"></td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">108,451,554</td>
<td align="right">45.1%</td>
<td align="right">114,082,294</td>
<td align="right">45.5%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">131,792,824</td>
<td align="right">54.9%</td>
<td align="right">136,698,659</td>
<td align="right">54.5%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">130,311,404</td>
<td align="right">54.2%</td>
<td align="right">135,064,692</td>
<td align="right">53.9%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">612,222,289</td>
<td align="right">24.7%</td>
<td align="right">624,037,870</td>
<td align="right">24.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,323</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">97,356</td>
<td align="right">2.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,135</td>
<td align="right">32.4%</td>
<td align="right">981,855</td>
<td align="right">29.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">142,452,942</td>
<td align="right"></td>
<td align="right">141,037,304</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">746,986,081</td>
<td align="right">29.2%</td>
<td align="right">752,971,156</td>
<td align="right">29.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">878,885,170</td>
<td align="right">35.5%</td>
<td align="right">885,735,762</td>
<td align="right">35.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,198,954,141</td>
<td align="right">46.8%</td>
<td align="right">1,207,842,705</td>
<td align="right">46.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">859,958,146</td>
<td align="right">34.7%</td>
<td align="right">866,313,862</td>
<td align="right">34.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">197,759,559</td>
<td align="right"></td>
<td align="right">196,530,409</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">126,464,660</td>
<td align="right">5.1%</td>
<td align="right">127,097,421</td>
<td align="right">5.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,400,466</td>
<td align="right"></td>
<td align="right">154,776,622</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">531,512,319</td>
<td align="right">20.8%</td>
<td align="right">533,357,842</td>
<td align="right">20.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">83,035,884</td>
<td align="right">3.2%</td>
<td align="right">82,920,901</td>
<td align="right">3.2%</td>
<td align="right">-0.1%</td>
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
<td align="right">6,279</td>
<td align="right">12,990,190</td>
<td align="right">262,790,956</td>
<td align="right">16,291,282</td>
<td align="right">23,794,020</td>
<td align="right">6,823</td>
<td align="right">11,052,781</td>
<td align="right">272,257,194</td>
<td align="right">19,797,219</td>
<td align="right">21,391,212</td>
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
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">22</td>
<td align="right">462</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">23</td>
<td align="right">483</td>
<td align="right">2,000.0%</td>
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
<td align="right">22,239</td>
<td align="right">-1.6%</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-27
