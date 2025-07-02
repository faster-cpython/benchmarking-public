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
<td align="left">NOT_TAKEN</td>
<td align="right">527,194</td>
<td align="right">1,605,708</td>
<td align="right">204.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">187,761</td>
<td align="right">83,832</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,984,279</td>
<td align="right">1,650,199</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">11,601,790</td>
<td align="right">7,396,134</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,775,133</td>
<td align="right">1,795,675</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">15,684</td>
<td align="right">10,158</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,002,542</td>
<td align="right">4,044,647</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">214,755</td>
<td align="right">145,298</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,968,110</td>
<td align="right">1,345,364</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">63,586,005</td>
<td align="right">49,077,595</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,762,648</td>
<td align="right">2,183,345</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,137,343</td>
<td align="right">9,734,936</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">2,103</td>
<td align="right">1,704</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">184,485</td>
<td align="right">149,793</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,639,366</td>
<td align="right">2,192,241</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">25,214,118</td>
<td align="right">21,459,351</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">48,773,130</td>
<td align="right">41,548,127</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">58,577</td>
<td align="right">50,034</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,973,401</td>
<td align="right">10,409,187</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">16,120,939</td>
<td align="right">14,060,301</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60,792,527</td>
<td align="right">53,612,469</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">488,627</td>
<td align="right">433,841</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,930,527</td>
<td align="right">2,628,919</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">56,840,201</td>
<td align="right">51,111,725</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">58,399,536</td>
<td align="right">52,688,814</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,077,709</td>
<td align="right">30,789,226</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">9,671,371</td>
<td align="right">8,765,173</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,438,040</td>
<td align="right">32,151,294</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,634,549</td>
<td align="right">4,214,886</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">25,599</td>
<td align="right">23,373</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">176,377,402</td>
<td align="right">161,458,601</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">33,690,176</td>
<td align="right">30,888,526</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,391,455</td>
<td align="right">9,578,890</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">90,471</td>
<td align="right">83,562</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,863,426</td>
<td align="right">14,666,066</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,899,923</td>
<td align="right">41,574,529</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,946,540</td>
<td align="right">9,212,861</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,466</td>
<td align="right">5,067</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,738,560</td>
<td align="right">10,916,173</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,996,990</td>
<td align="right">22,345,220</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">63,402,565</td>
<td align="right">59,136,062</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,197,815</td>
<td align="right">16,998,350</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">53,098,316</td>
<td align="right">49,700,148</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">18,008,849</td>
<td align="right">16,900,866</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,761,109</td>
<td align="right">42,950,305</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,825,624</td>
<td align="right">1,716,940</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,594,049</td>
<td align="right">28,789,474</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">54,812,745</td>
<td align="right">51,634,374</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,492,355</td>
<td align="right">14,604,936</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">16,182,418</td>
<td align="right">15,324,061</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,815</td>
<td align="right">2,081,960</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">43,183,837</td>
<td align="right">41,049,800</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,528,984</td>
<td align="right">15,760,730</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">69,377,378</td>
<td align="right">66,223,295</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,935,496</td>
<td align="right">21,095,836</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">227,035,235</td>
<td align="right">218,733,408</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">50,942,157</td>
<td align="right">49,084,618</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,203,530</td>
<td align="right">4,051,965</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">148,671,756</td>
<td align="right">143,513,477</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">38,018,940</td>
<td align="right">36,760,850</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">90,394,821</td>
<td align="right">87,435,392</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">14,898,135</td>
<td align="right">14,417,551</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">769,622</td>
<td align="right">747,186</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,379,673</td>
<td align="right">7,184,024</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">62,289,943</td>
<td align="right">60,639,214</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">246,475,016</td>
<td align="right">239,991,641</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">39,365,817</td>
<td align="right">38,345,676</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,256,914</td>
<td align="right">2,201,111</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">182,091,203</td>
<td align="right">177,611,125</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,045,809</td>
<td align="right">44,929,036</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">647,522,810</td>
<td align="right">633,830,851</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,620,598</td>
<td align="right">18,230,912</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,290,501</td>
<td align="right">1,263,590</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">61,240,755</td>
<td align="right">60,004,851</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">743,814</td>
<td align="right">728,983</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">10,137,855</td>
<td align="right">9,945,694</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">10,164,164</td>
<td align="right">9,972,012</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,472,768</td>
<td align="right">13,223,026</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">41,393,560</td>
<td align="right">40,639,944</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,932,296</td>
<td align="right">21,544,743</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">464,739</td>
<td align="right">457,371</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">205,893,910</td>
<td align="right">202,737,416</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">50,273,960</td>
<td align="right">49,507,568</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">386,497</td>
<td align="right">380,866</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">154,825,720</td>
<td align="right">152,746,182</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,554,008</td>
<td align="right">18,335,290</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">25,931,457</td>
<td align="right">25,667,718</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,595,162</td>
<td align="right">4,548,933</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">89,519</td>
<td align="right">88,654</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,575,138</td>
<td align="right">12,457,430</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">187,730,831</td>
<td align="right">186,261,230</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">444,276</td>
<td align="right">440,895</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,095,405</td>
<td align="right">5,056,635</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">11,695,295</td>
<td align="right">11,613,687</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,086,973</td>
<td align="right">6,045,621</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,923,638</td>
<td align="right">75,483,152</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">34,783,429</td>
<td align="right">34,586,181</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,455,512</td>
<td align="right">1,448,484</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,780,164</td>
<td align="right">3,761,956</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,813,354</td>
<td align="right">44,624,275</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22,505,426</td>
<td align="right">22,416,082</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,135,970</td>
<td align="right">2,127,843</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">18,587,705</td>
<td align="right">18,657,581</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,547,078</td>
<td align="right">19,616,874</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,025,096</td>
<td align="right">9,992,594</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,891,095</td>
<td align="right">6,869,173</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,265</td>
<td align="right">1,261</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">440,463</td>
<td align="right">439,242</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,249,612</td>
<td align="right">1,247,395</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">191,367</td>
<td align="right">191,104</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,119,231</td>
<td align="right">8,127,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,284,467</td>
<td align="right">8,292,395</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,744</td>
<td align="right">20,727</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,357,030</td>
<td align="right">22,375,124</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">143,089</td>
<td align="right">142,975</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">272,936</td>
<td align="right">272,729</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">50,150</td>
<td align="right">50,114</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,450</td>
<td align="right">13,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">81,361,012</td>
<td align="right">81,314,905</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,987,090</td>
<td align="right">2,985,485</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">120,324</td>
<td align="right">120,261</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">241,194</td>
<td align="right">241,068</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">241,236</td>
<td align="right">241,110</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">7,254,078</td>
<td align="right">7,250,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">166,684</td>
<td align="right">166,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,861,117</td>
<td align="right">11,857,824</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">98,266</td>
<td align="right">98,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">184,135</td>
<td align="right">184,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,233,635</td>
<td align="right">1,233,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">742,919</td>
<td align="right">743,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">742,919</td>
<td align="right">743,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">742,919</td>
<td align="right">743,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">25,295,573</td>
<td align="right">25,291,815</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,259,757</td>
<td align="right">7,260,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,275,493</td>
<td align="right">6,275,972</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,360,028</td>
<td align="right">7,360,556</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,737,118</td>
<td align="right">1,737,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">736,671</td>
<td align="right">736,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">736,333</td>
<td align="right">736,382</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,432,977</td>
<td align="right">3,433,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,080,501</td>
<td align="right">1,080,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,082,319</td>
<td align="right">1,082,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,885,345</td>
<td align="right">4,885,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">848,545</td>
<td align="right">848,578</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,795,402</td>
<td align="right">7,795,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">3,086,987</td>
<td align="right">3,087,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,969</td>
<td align="right">39,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,477,397</td>
<td align="right">1,477,361</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,866,131</td>
<td align="right">7,865,962</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,779,524</td>
<td align="right">18,779,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">945,777</td>
<td align="right">945,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">22,224,342</td>
<td align="right">22,224,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,981</td>
<td align="right">164,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">932,307</td>
<td align="right">932,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">431,847</td>
<td align="right">431,843</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,028,007</td>
<td align="right">1,028,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">427,533</td>
<td align="right">427,533</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">378,841</td>
<td align="right">378,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">202,050</td>
<td align="right">202,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">87,150</td>
<td align="right">87,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">6,993</td>
<td align="right">6,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,200</td>
<td align="right">4,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,793</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,667</td>
<td align="right">2,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,142</td>
<td align="right">2,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,932</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,653</td>
<td align="right">1,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">231</td>
<td align="right">231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">475,943</td>
<td align="right">0.4%</td>
<td align="right">332,608</td>
<td align="right">0.3%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,678,532</td>
<td align="right">38.0%</td>
<td align="right">42,872,047</td>
<td align="right">36.5%</td>
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
<td align="right">74,017,283</td>
<td align="right">61.6%</td>
<td align="right">74,107,907</td>
<td align="right">63.1%</td>
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
<td align="right">24,881</td>
<td align="right">27.3%</td>
<td align="right">22,032</td>
<td align="right">26.1%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">66,362</td>
<td align="right">72.7%</td>
<td align="right">62,233</td>
<td align="right">73.9%</td>
<td align="right">-6.2%</td>
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
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,822</td>
<td align="right">5.8%</td>
<td align="right">2,058</td>
<td align="right">3.3%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4,049</td>
<td align="right">6.1%</td>
<td align="right">3,459</td>
<td align="right">5.6%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,923</td>
<td align="right">11.9%</td>
<td align="right">7,156</td>
<td align="right">11.5%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,157</td>
<td align="right">3.3%</td>
<td align="right">1,985</td>
<td align="right">3.2%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,253</td>
<td align="right">1.9%</td>
<td align="right">1,182</td>
<td align="right">1.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,991</td>
<td align="right">9.0%</td>
<td align="right">5,675</td>
<td align="right">9.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,373</td>
<td align="right">3.6%</td>
<td align="right">2,270</td>
<td align="right">3.6%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">198</td>
<td align="right">0.3%</td>
<td align="right">192</td>
<td align="right">0.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">2,063</td>
<td align="right">3.1%</td>
<td align="right">2,019</td>
<td align="right">3.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">4,868</td>
<td align="right">7.3%</td>
<td align="right">4,772</td>
<td align="right">7.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,430</td>
<td align="right">14.2%</td>
<td align="right">9,251</td>
<td align="right">14.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">359</td>
<td align="right">0.5%</td>
<td align="right">362</td>
<td align="right">0.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,923</td>
<td align="right">2.9%</td>
<td align="right">1,936</td>
<td align="right">3.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,736</td>
<td align="right">5.6%</td>
<td align="right">3,712</td>
<td align="right">6.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,940</td>
<td align="right">4.4%</td>
<td align="right">2,926</td>
<td align="right">4.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,170</td>
<td align="right">1.8%</td>
<td align="right">1,173</td>
<td align="right">1.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,261</td>
<td align="right">9.4%</td>
<td align="right">6,261</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">3,173</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">2,355</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">294</td>
<td align="right">0.4%</td>
<td align="right">294</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">90,471</td>
<td align="right">100.0%</td>
<td align="right">83,562</td>
<td align="right">100.0%</td>
<td align="right">-7.6%</td>
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
<td align="right">37,096,957</td>
<td align="right">11.5%</td>
<td align="right">37,160,083</td>
<td align="right">11.5%</td>
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
<td align="right">36,573,131</td>
<td align="right">11.3%</td>
<td align="right">36,634,950</td>
<td align="right">11.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">285,899,102</td>
<td align="right">88.4%</td>
<td align="right">285,853,529</td>
<td align="right">88.4%</td>
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
<td align="right">796,762</td>
<td align="right">100.0%</td>
<td align="right">797,862</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">11,352</td>
<td align="right">69.1%</td>
<td align="right">11,348</td>
<td align="right">69.1%</td>
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
<td align="right">2,988</td>
<td align="right">18.2%</td>
<td align="right">2,988</td>
<td align="right">18.2%</td>
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
<td align="right">5,086</td>
<td align="right">100.0%</td>
<td align="right">5,082</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,520,571</td>
<td align="right">36.4%</td>
<td align="right">28,716,481</td>
<td align="right">35.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">52,869,553</td>
<td align="right">63.0%</td>
<td align="right">52,862,757</td>
<td align="right">64.4%</td>
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
<td align="right">432,290</td>
<td align="right">0.5%</td>
<td align="right">432,299</td>
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
<td align="right">63,580</td>
<td align="right">78.0%</td>
<td align="right">63,127</td>
<td align="right">77.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">17,896</td>
<td align="right">22.0%</td>
<td align="right">17,866</td>
<td align="right">22.1%</td>
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
<td align="right">1,769</td>
<td align="right">2.8%</td>
<td align="right">1,637</td>
<td align="right">2.6%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,424</td>
<td align="right">22.7%</td>
<td align="right">14,105</td>
<td align="right">22.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">292</td>
<td align="right">0.5%</td>
<td align="right">291</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">15,818</td>
<td align="right">24.9%</td>
<td align="right">15,798</td>
<td align="right">25.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,083</td>
<td align="right">19.0%</td>
<td align="right">12,094</td>
<td align="right">19.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,996</td>
<td align="right">15.7%</td>
<td align="right">10,004</td>
<td align="right">15.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">8,316</td>
<td align="right">13.1%</td>
<td align="right">8,316</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">315</td>
<td align="right">0.5%</td>
<td align="right">315</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">231</td>
<td align="right">0.4%</td>
<td align="right">231</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">63</td>
<td align="right">0.1%</td>
<td align="right">63</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,587,775</td>
<td align="right">33.0%</td>
<td align="right">7,383,197</td>
<td align="right">23.9%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,522,119</td>
<td align="right">67.0%</td>
<td align="right">23,522,009</td>
<td align="right">76.1%</td>
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
<td align="right">924</td>
<td align="right">0.0%</td>
<td align="right">924</td>
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
<td align="right">12,650</td>
<td align="right">90.3%</td>
<td align="right">11,572</td>
<td align="right">89.4%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365</td>
<td align="right">9.7%</td>
<td align="right">1,365</td>
<td align="right">10.6%</td>
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
<td align="right">5,570</td>
<td align="right">44.0%</td>
<td align="right">4,706</td>
<td align="right">40.7%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,197</td>
<td align="right">9.5%</td>
<td align="right">1,071</td>
<td align="right">9.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,526</td>
<td align="right">43.7%</td>
<td align="right">5,438</td>
<td align="right">47.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">357</td>
<td align="right">2.8%</td>
<td align="right">357</td>
<td align="right">3.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,244,069</td>
<td align="right">1.0%</td>
<td align="right">798,096</td>
<td align="right">0.8%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">48,680,702</td>
<td align="right">40.8%</td>
<td align="right">41,460,924</td>
<td align="right">39.3%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">69,309,437</td>
<td align="right">58.1%</td>
<td align="right">63,103,603</td>
<td align="right">59.8%</td>
<td align="right">-9.0%</td>
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
<td align="right">37,439</td>
<td align="right">32.3%</td>
<td align="right">28,997</td>
<td align="right">28.4%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">78,343</td>
<td align="right">67.7%</td>
<td align="right">73,153</td>
<td align="right">71.6%</td>
<td align="right">-6.6%</td>
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
<td align="right">714</td>
<td align="right">0.9%</td>
<td align="right">567</td>
<td align="right">0.8%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,618</td>
<td align="right">2.1%</td>
<td align="right">1,449</td>
<td align="right">2.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">5,190</td>
<td align="right">6.6%</td>
<td align="right">4,705</td>
<td align="right">6.4%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51,862</td>
<td align="right">66.2%</td>
<td align="right">48,283</td>
<td align="right">66.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,557</td>
<td align="right">9.6%</td>
<td align="right">7,042</td>
<td align="right">9.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,302</td>
<td align="right">5.5%</td>
<td align="right">4,134</td>
<td align="right">5.7%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,773</td>
<td align="right">3.5%</td>
<td align="right">2,688</td>
<td align="right">3.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,828</td>
<td align="right">2.3%</td>
<td align="right">1,786</td>
<td align="right">2.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,344</td>
<td align="right">1.7%</td>
<td align="right">1,344</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">903</td>
<td align="right">1.2%</td>
<td align="right">903</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">84</td>
<td align="right">0.1%</td>
<td align="right">84</td>
<td align="right">0.1%</td>
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
<td align="left">set</td>
<td align="right">7,338,284</td>
<td align="right">7,338,284 / 0 !!</td>
<td align="right">7,349,428</td>
<td align="right">7,349,428 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">72,742</td>
<td align="right">72,742 / 0 !!</td>
<td align="right">72,679</td>
<td align="right">72,679 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">166,009</td>
<td align="right">166,009 / 0 !!</td>
<td align="right">166,040</td>
<td align="right">166,040 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,945,579</td>
<td align="right">8,945,579 / 0 !!</td>
<td align="right">8,945,815</td>
<td align="right">8,945,815 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,458,988</td>
<td align="right">12,458,988 / 0 !!</td>
<td align="right">12,459,098</td>
<td align="right">12,459,098 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,175,564</td>
<td align="right">9,175,564 / 0 !!</td>
<td align="right">9,175,622</td>
<td align="right">9,175,622 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,562,907</td>
<td align="right">9,562,907 / 0 !!</td>
<td align="right">9,562,861</td>
<td align="right">9,562,861 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,174</td>
<td align="right">6,174 / 0 !!</td>
<td align="right">6,174</td>
<td align="right">6,174 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4,119</td>
<td align="right">4,119 / 0 !!</td>
<td align="right">4,119</td>
<td align="right">4,119 / 0 !!</td>
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
<td align="right">52,911,293</td>
<td align="right">16.1%</td>
<td align="right">51,097,533</td>
<td align="right">16.0%</td>
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
<td align="right">213,766,675</td>
<td align="right">65.2%</td>
<td align="right">207,967,165</td>
<td align="right">65.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,016,938</td>
<td align="right">18.6%</td>
<td align="right">59,782,029</td>
<td align="right">18.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">1,085,026</td>
<td align="right">89.7%</td>
<td align="right">1,050,709</td>
<td align="right">89.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">124,966</td>
<td align="right">10.3%</td>
<td align="right">124,570</td>
<td align="right">10.6%</td>
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
<td align="left">builtin class method</td>
<td align="right">903</td>
<td align="right">0.7%</td>
<td align="right">861</td>
<td align="right">0.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">588</td>
<td align="right">0.5%</td>
<td align="right">567</td>
<td align="right">0.5%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,391</td>
<td align="right">3.5%</td>
<td align="right">4,349</td>
<td align="right">3.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,535</td>
<td align="right">7.6%</td>
<td align="right">9,453</td>
<td align="right">7.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">14,856</td>
<td align="right">11.9%</td>
<td align="right">14,773</td>
<td align="right">11.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,566</td>
<td align="right">6.1%</td>
<td align="right">7,542</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,309</td>
<td align="right">49.1%</td>
<td align="right">61,205</td>
<td align="right">49.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,877</td>
<td align="right">7.1%</td>
<td align="right">8,881</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">12,351</td>
<td align="right">9.9%</td>
<td align="right">12,349</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">106</td>
<td align="right">0.1%</td>
<td align="right">106</td>
<td align="right">0.1%</td>
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
<td align="right">273,727,099</td>
<td align="right">99.9%</td>
<td align="right">266,487,674</td>
<td align="right">99.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">94,803</td>
<td align="right">0.0%</td>
<td align="right">94,674</td>
<td align="right">0.0%</td>
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
<td align="right">21,462</td>
<td align="right">0.0%</td>
<td align="right">21,462</td>
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
<td align="right">96,732</td>
<td align="right">100.0%</td>
<td align="right">96,598</td>
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
<td align="right">635</td>
<td align="right">0.0%</td>
<td align="right">631</td>
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
<td align="right">2,409,704</td>
<td align="right">99.9%</td>
<td align="right">2,409,677</td>
<td align="right">99.9%</td>
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
<td align="right">630</td>
<td align="right">100.0%</td>
<td align="right">630</td>
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
<td align="right">821,124</td>
<td align="right">66.9%</td>
<td align="right">821,157</td>
<td align="right">66.9%</td>
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
<td align="right">375,973</td>
<td align="right">30.6%</td>
<td align="right">375,973</td>
<td align="right">30.6%</td>
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
<td align="right">2.2%</td>
<td align="right">27,421</td>
<td align="right">2.2%</td>
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
<td align="right">569</td>
<td align="right">16.9%</td>
<td align="right">569</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,805</td>
<td align="right">83.1%</td>
<td align="right">2,805</td>
<td align="right">83.1%</td>
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
<td align="right">2,805</td>
<td align="right">100.0%</td>
<td align="right">2,805</td>
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
<td align="right">377,472</td>
<td align="right">3.5%</td>
<td align="right">371,843</td>
<td align="right">3.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,822,911</td>
<td align="right">17.0%</td>
<td align="right">1,821,922</td>
<td align="right">17.0%</td>
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
<td align="right">8,524,207</td>
<td align="right">79.4%</td>
<td align="right">8,525,841</td>
<td align="right">79.5%</td>
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
<td align="right">39,688</td>
<td align="right">91.6%</td>
<td align="right">39,664</td>
<td align="right">91.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,649</td>
<td align="right">8.4%</td>
<td align="right">3,647</td>
<td align="right">8.4%</td>
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
<td align="right">1,402</td>
<td align="right">38.4%</td>
<td align="right">1,400</td>
<td align="right">38.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,953</td>
<td align="right">53.5%</td>
<td align="right">1,953</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">462</td>
<td align="right">12.7%</td>
<td align="right">462</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">63</td>
<td align="right">1.7%</td>
<td align="right">63</td>
<td align="right">1.7%</td>
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
<td align="right">2,103</td>
<td align="right">100.0%</td>
<td align="right">1,704</td>
<td align="right">100.0%</td>
<td align="right">-19.0%</td>
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
<td align="right">2,756,278</td>
<td align="right">13.2%</td>
<td align="right">2,177,104</td>
<td align="right">10.7%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,076,229</td>
<td align="right">86.7%</td>
<td align="right">18,076,127</td>
<td align="right">89.2%</td>
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
<td align="right">3,510</td>
<td align="right">55.1%</td>
<td align="right">3,385</td>
<td align="right">54.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,860</td>
<td align="right">44.9%</td>
<td align="right">2,856</td>
<td align="right">45.8%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">3,510</td>
<td align="right">100.0%</td>
<td align="right">3,385</td>
<td align="right">100.0%</td>
<td align="right">-3.6%</td>
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
<td align="right">168,845,801</td>
<td align="right">94.0%</td>
<td align="right">166,880,792</td>
<td align="right">94.0%</td>
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
<td align="right">9,940,712</td>
<td align="right">5.5%</td>
<td align="right">9,908,355</td>
<td align="right">5.6%</td>
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
<td align="right">668,259</td>
<td align="right">0.4%</td>
<td align="right">668,152</td>
<td align="right">0.4%</td>
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
<td align="right">27,178</td>
<td align="right">28.4%</td>
<td align="right">27,090</td>
<td align="right">28.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,659</td>
<td align="right">71.6%</td>
<td align="right">68,601</td>
<td align="right">71.7%</td>
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
<td align="left">dict</td>
<td align="right">2,352</td>
<td align="right">8.7%</td>
<td align="right">2,289</td>
<td align="right">8.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,118</td>
<td align="right">11.5%</td>
<td align="right">3,075</td>
<td align="right">11.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,390</td>
<td align="right">5.1%</td>
<td align="right">1,393</td>
<td align="right">5.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">13,490</td>
<td align="right">49.6%</td>
<td align="right">13,507</td>
<td align="right">49.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,363</td>
<td align="right">12.4%</td>
<td align="right">3,361</td>
<td align="right">12.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,339</td>
<td align="right">12.3%</td>
<td align="right">3,339</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,728,407</td>
<td align="right">100.0%</td>
<td align="right">83,828,241</td>
<td align="right">100.0%</td>
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
<td align="right">27,287</td>
<td align="right">0.0%</td>
<td align="right">27,306</td>
<td align="right">0.0%</td>
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
<td align="right">743</td>
<td align="right">5.9%</td>
<td align="right">749</td>
<td align="right">5.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,939</td>
<td align="right">94.1%</td>
<td align="right">11,915</td>
<td align="right">94.1%</td>
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
<td align="left">sequence</td>
<td align="right">680</td>
<td align="right">91.5%</td>
<td align="right">686</td>
<td align="right">91.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">63</td>
<td align="right">8.5%</td>
<td align="right">63</td>
<td align="right">8.4%</td>
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
<td align="right">258,181,285</td>
<td align="right">5.8%</td>
<td align="right">239,157,345</td>
<td align="right">5.6%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,474,590,463</td>
<td align="right">33.1%</td>
<td align="right">1,403,804,905</td>
<td align="right">32.8%</td>
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
<td align="right">2,625,344,972</td>
<td align="right">59.0%</td>
<td align="right">2,541,415,727</td>
<td align="right">59.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">94,704,521</td>
<td align="right">2.1%</td>
<td align="right">92,363,495</td>
<td align="right">2.2%</td>
<td align="right">-2.5%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">11,587,775</td>
<td align="right">4.7%</td>
<td align="right">7,383,197</td>
<td align="right">3.2%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,756,278</td>
<td align="right">1.1%</td>
<td align="right">2,177,104</td>
<td align="right">0.9%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">48,680,702</td>
<td align="right">19.7%</td>
<td align="right">41,460,924</td>
<td align="right">18.0%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,678,532</td>
<td align="right">18.4%</td>
<td align="right">42,872,047</td>
<td align="right">18.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,520,571</td>
<td align="right">12.3%</td>
<td align="right">28,716,481</td>
<td align="right">12.5%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">61,016,938</td>
<td align="right">24.6%</td>
<td align="right">59,782,029</td>
<td align="right">26.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">377,472</td>
<td align="right">0.2%</td>
<td align="right">371,843</td>
<td align="right">0.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,940,712</td>
<td align="right">4.0%</td>
<td align="right">9,908,355</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,573,131</td>
<td align="right">14.8%</td>
<td align="right">36,634,950</td>
<td align="right">15.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">375,973</td>
<td align="right">0.2%</td>
<td align="right">375,973</td>
<td align="right">0.2%</td>
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
<td align="right">12,927,332</td>
<td align="right">13.7%</td>
<td align="right">11,290,067</td>
<td align="right">12.2%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,300,495</td>
<td align="right">3.5%</td>
<td align="right">3,270,771</td>
<td align="right">3.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,583,529</td>
<td align="right">12.2%</td>
<td align="right">11,654,482</td>
<td align="right">12.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,852,160</td>
<td align="right">30.5%</td>
<td align="right">28,714,174</td>
<td align="right">31.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,903,209</td>
<td align="right">12.6%</td>
<td align="right">11,895,238</td>
<td align="right">12.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,822,125</td>
<td align="right">1.9%</td>
<td align="right">1,821,136</td>
<td align="right">2.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,314,221</td>
<td align="right">7.7%</td>
<td align="right">7,315,039</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,183,306</td>
<td align="right">6.5%</td>
<td align="right">6,183,132</td>
<td align="right">6.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,164,097</td>
<td align="right">5.5%</td>
<td align="right">5,164,177</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,105,455</td>
<td align="right">2.2%</td>
<td align="right">2,105,437</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">42,022,737</td>
<td align="right">19.3%</td>
<td align="right">41,976,036</td>
<td align="right">19.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">135,845,445</td>
<td align="right">62.5%</td>
<td align="right">135,992,995</td>
<td align="right">62.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">77,471,639</td>
<td align="right">35.6%</td>
<td align="right">77,425,371</td>
<td align="right">35.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">77,479,157</td>
<td align="right">35.6%</td>
<td align="right">77,432,889</td>
<td align="right">35.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">81,525,316</td>
<td align="right">37.5%</td>
<td align="right">81,479,203</td>
<td align="right">37.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">81,525,316</td>
<td align="right">37.5%</td>
<td align="right">81,479,203</td>
<td align="right">37.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">193,680,877</td>
<td align="right">89.1%</td>
<td align="right">193,712,379</td>
<td align="right">89.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,047,202</td>
<td align="right">0.5%</td>
<td align="right">1,047,261</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">4,046,159</td>
<td align="right">1.9%</td>
<td align="right">4,046,314</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,923,325</td>
<td align="right">8.7%</td>
<td align="right">18,923,639</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,359,072</td>
<td align="right">4.3%</td>
<td align="right">9,359,140</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">8,736</td>
<td align="right">0.0%</td>
<td align="right">8,736</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">53,525,302</td>
<td align="right">1.4%</td>
<td align="right">50,884,558</td>
<td align="right">1.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,739,873</td>
<td align="right"></td>
<td align="right">3,557,514</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,707,916</td>
<td align="right"></td>
<td align="right">4,554,293</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">971,833</td>
<td align="right"></td>
<td align="right">1,000,388</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,245,697,256</td>
<td align="right">35.1%</td>
<td align="right">1,281,823,881</td>
<td align="right">36.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,375,130,292</td>
<td align="right">36.0%</td>
<td align="right">1,413,367,596</td>
<td align="right">37.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,221,851,790</td>
<td align="right">34.4%</td>
<td align="right">1,189,897,918</td>
<td align="right">33.4%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,522,168,291</td>
<td align="right">39.9%</td>
<td align="right">1,488,167,670</td>
<td align="right">38.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">80,190,177</td>
<td align="right">2.3%</td>
<td align="right">78,530,923</td>
<td align="right">2.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">23,547</td>
<td align="right">0.0%</td>
<td align="right">23,778</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">852,468</td>
<td align="right">0.2%</td>
<td align="right">859,426</td>
<td align="right">0.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">153,793,783</td>
<td align="right"></td>
<td align="right">154,548,116</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">867,877,234</td>
<td align="right">22.7%</td>
<td align="right">871,034,968</td>
<td align="right">22.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,005,618,475</td>
<td align="right">28.3%</td>
<td align="right">1,008,397,305</td>
<td align="right">28.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">135,512,992</td>
<td align="right">27.3%</td>
<td align="right">135,549,861</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">146,019,903</td>
<td align="right"></td>
<td align="right">146,053,113</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">134,636,977</td>
<td align="right">27.1%</td>
<td align="right">134,666,657</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,186,542</td>
<td align="right"></td>
<td align="right">1,186,630</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">361,348,192</td>
<td align="right">72.7%</td>
<td align="right">361,371,161</td>
<td align="right">72.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">361,601,665</td>
<td align="right"></td>
<td align="right">361,624,634</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">256,096,091</td>
<td align="right"></td>
<td align="right">256,088,503</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,765</td>
<td align="right">14.7%</td>
<td align="right">13,917</td>
<td align="right">21.9%</td>
<td align="right">403.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">599</td>
<td align="right">0.9%</td>
<td align="right">274.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">1,583</td>
<td align="right">8.4%</td>
<td align="right">5,575</td>
<td align="right">8.8%</td>
<td align="right">252.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,841</td>
<td align="right"></td>
<td align="right">63,649</td>
<td align="right"></td>
<td align="right">237.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,617</td>
<td align="right">29.8%</td>
<td align="right">18,740</td>
<td align="right">29.4%</td>
<td align="right">233.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">168</td>
<td align="right">0.9%</td>
<td align="right">514</td>
<td align="right">0.8%</td>
<td align="right">206.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">8,876</td>
<td align="right">47.1%</td>
<td align="right">25,417</td>
<td align="right">39.9%</td>
<td align="right">186.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">43,518,971</td>
<td align="right"></td>
<td align="right">72,059,494</td>
<td align="right"></td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,514,952,589</td>
<td align="right">3,481.1%</td>
<td align="right">2,069,138,988</td>
<td align="right">2,871.4%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">127</td>
<td align="right">0.2%</td>
<td align="right">127 / 0 !!</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">88</td>
<td align="right">0.6%</td>
<td align="right">88 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,765</td>
<td align="right"></td>
<td align="right">13,917</td>
<td align="right"></td>
<td align="right">403.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,599</td>
<td align="right">94.0%</td>
<td align="right">12,406</td>
<td align="right">89.1%</td>
<td align="right">377.3%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">172,032</td>
<td align="right">0.8%</td>
<td align="right">53,985,280</td>
<td align="right">48.7%</td>
<td align="right">31,281.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">15,432,290</td>
<td align="right">70.4%</td>
<td align="right">79,789,222</td>
<td align="right">72.0%</td>
<td align="right">417.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">485,312</td>
<td align="right">2.2%</td>
<td align="right">2,476,464</td>
<td align="right">2.2%</td>
<td align="right">410.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">21,921,792</td>
<td align="right"></td>
<td align="right">110,784,512</td>
<td align="right"></td>
<td align="right">405.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">6,004,190</td>
<td align="right">27.4%</td>
<td align="right">28,518,826</td>
<td align="right">25.7%</td>
<td align="right">375.0%</td>
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
<td align="left">749</td>
<td align="right">28.8%</td>
<td align="left">3,075</td>
<td align="right">24.8%</td>
<td align="right">310.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">1,388</td>
<td align="right">53.4%</td>
<td align="left">6,361</td>
<td align="right">51.3%</td>
<td align="right">358.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">378</td>
<td align="right">14.5%</td>
<td align="left">2,571</td>
<td align="right">20.7%</td>
<td align="right">580.2%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">84</td>
<td align="right">3.2%</td>
<td align="left">399</td>
<td align="right">3.2%</td>
<td align="right">375.0%</td>
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
<td align="right">136</td>
<td align="right">4.9%</td>
<td align="right">796</td>
<td align="right">5.7%</td>
<td align="right">485.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">259</td>
<td align="right">9.4%</td>
<td align="right">1,485</td>
<td align="right">10.7%</td>
<td align="right">473.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">783</td>
<td align="right">28.3%</td>
<td align="right">1,911</td>
<td align="right">13.7%</td>
<td align="right">144.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,167</td>
<td align="right">42.2%</td>
<td align="right">6,460</td>
<td align="right">46.4%</td>
<td align="right">453.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">336</td>
<td align="right">12.2%</td>
<td align="right">2,216</td>
<td align="right">15.9%</td>
<td align="right">559.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">2.3%</td>
<td align="right">881</td>
<td align="right">6.3%</td>
<td align="right">1,298.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">168</td>
<td align="right">1.2%</td>
<td align="right">700.0%</td>
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
<td align="right">94</td>
<td align="right">3.4%</td>
<td align="right">711</td>
<td align="right">5.1%</td>
<td align="right">656.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">151</td>
<td align="right">5.5%</td>
<td align="right">895</td>
<td align="right">6.4%</td>
<td align="right">492.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">244</td>
<td align="right">8.8%</td>
<td align="right">1,003</td>
<td align="right">7.2%</td>
<td align="right">311.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,586</td>
<td align="right">57.4%</td>
<td align="right">6,418</td>
<td align="right">46.1%</td>
<td align="right">304.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">230</td>
<td align="right">8.3%</td>
<td align="right">1,975</td>
<td align="right">14.2%</td>
<td align="right">758.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">273</td>
<td align="right">9.9%</td>
<td align="right">1,257</td>
<td align="right">9.0%</td>
<td align="right">360.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">147</td>
<td align="right">1.1%</td>
<td align="right">600.0%</td>
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
<td align="left">_COMPARE_OP</td>
<td align="right">22,356</td>
<td align="right">1,847,206</td>
<td align="right">8,162.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">44,712</td>
<td align="right">3,313,227</td>
<td align="right">7,310.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">28,056</td>
<td align="right">532,038</td>
<td align="right">1,796.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">28,056</td>
<td align="right">475,296</td>
<td align="right">1,594.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">446,553</td>
<td align="right">1,566.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">28,119</td>
<td align="right">388,542</td>
<td align="right">1,281.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">68,187</td>
<td align="right">926,436</td>
<td align="right">1,258.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,311</td>
<td align="right">675,339</td>
<td align="right">1,191.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">276,885</td>
<td align="right">3,494,587</td>
<td align="right">1,162.1%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">133,854</td>
<td align="right">1,647,618</td>
<td align="right">1,130.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">18,228</td>
<td align="right">214,587</td>
<td align="right">1,077.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">60,024</td>
<td align="right">1,061.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">80,262</td>
<td align="right">860,223</td>
<td align="right">971.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">185,556</td>
<td align="right">1,845,249</td>
<td align="right">894.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">172,620</td>
<td align="right">1,035,584</td>
<td align="right">499.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">65,016</td>
<td align="right">382,704</td>
<td align="right">488.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">206,514</td>
<td align="right">1,112,667</td>
<td align="right">438.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">206,514</td>
<td align="right">1,112,667</td>
<td align="right">438.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">183,183</td>
<td align="right">900,213</td>
<td align="right">391.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">453,033</td>
<td align="right">1,993,836</td>
<td align="right">340.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,029,778</td>
<td align="right">4,022,408</td>
<td align="right">290.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,192,437</td>
<td align="right">4,560,506</td>
<td align="right">282.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,192,437</td>
<td align="right">4,560,506</td>
<td align="right">282.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,262,537</td>
<td align="right">4,729,460</td>
<td align="right">274.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,262,537</td>
<td align="right">4,729,460</td>
<td align="right">274.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,262,537</td>
<td align="right">4,729,460</td>
<td align="right">274.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">72,808</td>
<td align="right">271,124</td>
<td align="right">272.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,262,537</td>
<td align="right">4,622,186</td>
<td align="right">266.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,896,503</td>
<td align="right">10,168,739</td>
<td align="right">251.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">155,064</td>
<td align="right">539,113</td>
<td align="right">247.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,675,311</td>
<td align="right">5,755,878</td>
<td align="right">243.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">2,857,846</td>
<td align="right">9,208,087</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">4,534,195</td>
<td align="right">14,159,094</td>
<td align="right">212.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,039,500</td>
<td align="right">3,083,861</td>
<td align="right">196.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,605,742</td>
<td align="right">13,094,213</td>
<td align="right">184.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,262,537</td>
<td align="right">3,583,269</td>
<td align="right">183.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">276,885</td>
<td align="right">714,215</td>
<td align="right">157.9%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">887,313</td>
<td align="right">2,119,139</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,705,500</td>
<td align="right">19,499,955</td>
<td align="right">124.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">959,553</td>
<td align="right">2,067,629</td>
<td align="right">115.5%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">937,839</td>
<td align="right">1,948,517</td>
<td align="right">107.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">937,839</td>
<td align="right">1,945,241</td>
<td align="right">107.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,067,660</td>
<td align="right">4,213,310</td>
<td align="right">103.8%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">22,356</td>
<td align="right">44,415</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">1,690,563</td>
<td align="right">3,260,841</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,307,103</td>
<td align="right">2,504,522</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,122,825</td>
<td align="right">3,976,186</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,090,949</td>
<td align="right">5,687,635</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">4,111,007</td>
<td align="right">7,371,753</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,180,219</td>
<td align="right">5,626,706</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,552,818</td>
<td align="right">2,745,330</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,035,824</td>
<td align="right">5,255,749</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,998,188</td>
<td align="right">3,389,045</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">20,945,673</td>
<td align="right">35,242,487</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,684,557</td>
<td align="right">2,812,800</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,318,444</td>
<td align="right">10,543,139</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,353,680</td>
<td align="right">3,920,402</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">43,518,971</td>
<td align="right">72,059,494</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">43,518,971</td>
<td align="right">71,970,488</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">1,944,655</td>
<td align="right">3,101,930</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,244,126</td>
<td align="right">3,578,298</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,455,542</td>
<td align="right">14,722,357</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,391,225</td>
<td align="right">2,159,665</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,391,225</td>
<td align="right">2,159,665</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">3,849,782</td>
<td align="right">5,945,079</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,467,075</td>
<td align="right">2,250,960</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">820,386</td>
<td align="right">1,247,042</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,640,772</td>
<td align="right">2,480,565</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,640,772</td>
<td align="right">2,463,412</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">12,791,879</td>
<td align="right">18,771,835</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,989,939</td>
<td align="right">4,240,915</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,144,206</td>
<td align="right">9,998,603</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,924,751</td>
<td align="right">2,691,076</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">82,708,712</td>
<td align="right">114,466,579</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,230,123</td>
<td align="right">13,846,380</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,497,974</td>
<td align="right">8,792,819</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">10,972,639</td>
<td align="right">14,753,216</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">23,648,003</td>
<td align="right">31,312,760</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">315,571,106</td>
<td align="right">414,986,987</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,295,445</td>
<td align="right">8,227,703</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">286,440,625</td>
<td align="right">366,874,468</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,230,724</td>
<td align="right">4,122,499</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,267,367</td>
<td align="right">9,095,620</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,813,209</td>
<td align="right">7,197,683</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">76,173,660</td>
<td align="right">93,906,338</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">25,454,616</td>
<td align="right">31,309,804</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">25,454,616</td>
<td align="right">31,282,630</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">33,817,054</td>
<td align="right">41,363,175</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">30,022,778</td>
<td align="right">36,661,403</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,802,246</td>
<td align="right">4,569,668</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,262,537</td>
<td align="right">1,503,611</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,262,537</td>
<td align="right">1,498,214</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">24,997,049</td>
<td align="right">29,477,309</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,790,497</td>
<td align="right">6,825,768</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">25,040,447</td>
<td align="right">29,513,386</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,558,098</td>
<td align="right">1,825,330</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,558,098</td>
<td align="right">1,825,092</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">11,588,212</td>
<td align="right">13,431,101</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">11,588,212</td>
<td align="right">13,431,101</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,262,537</td>
<td align="right">1,462,630</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,262,537</td>
<td align="right">1,462,619</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,262,537</td>
<td align="right">1,462,619</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,262,537</td>
<td align="right">1,462,619</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">7,967,437</td>
<td align="right">9,216,615</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">24,997,049</td>
<td align="right">28,738,508</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">21,573,038</td>
<td align="right">24,512,747</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">28,746,133</td>
<td align="right">32,626,607</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,305,746</td>
<td align="right">19,263,520</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">25,223,553</td>
<td align="right">27,448,862</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">39,189,741</td>
<td align="right">42,407,085</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">4,970,111</td>
<td align="right">5,357,926</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">4,970,111</td>
<td align="right">5,219,990</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">31,681,474</td>
<td align="right">32,439,080</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,497,667</td>
<td align="right">15,755,271</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">11,500,661</td>
<td align="right">11,591,245</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,462,334</td>
<td align="right">2,480,817</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">3,250,037</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">3,231,257</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">3,090,162</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">1,493,247</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">1,071,449</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">579,093</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">151,546</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">136,128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">116,592</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">108,690</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right"></td>
<td align="right">106,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">103,929</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">89,346</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">84,219</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">69,468</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">63,084</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">59,136</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right"></td>
<td align="right">58,370</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">55,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">46,536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">39,144</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">34,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">32,445</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">27,216</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">26,674</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">25,922</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">14,826</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">14,826</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">14,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">11,808</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">8,610</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">8,601</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">8,169</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">7,992</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">7,368</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">7,053</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">6,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">5,670</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">5,526</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">5,115</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">5,052</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">3,624</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">3,456</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">3,414</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">3,414</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">2,499</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">2,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">2,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right"></td>
<td align="right">1,848</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">1,407</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">1,221</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">861</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">861</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TUPLE_1</td>
<td align="right"></td>
<td align="right">597</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right"></td>
<td align="right">597</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">399</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">399</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">105</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">63</td>
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
<td align="right">363</td>
<td align="right">2,639</td>
<td align="right">627.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">105</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,451</td>
<td align="right">4,032</td>
<td align="right">177.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">315</td>
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
Stats gathered on: 2025-07-02
