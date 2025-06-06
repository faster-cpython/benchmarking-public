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
<td align="right">201,201</td>
<td align="right">258,715</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,678,169</td>
<td align="right">11,270,985</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">61</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,162,591</td>
<td align="right">17,907,503</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,418,127</td>
<td align="right">9,290,125</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">15,070,697</td>
<td align="right">14,878,572</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,861,974</td>
<td align="right">10,730,521</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,669,722</td>
<td align="right">43,111,166</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,666</td>
<td align="right">4,139,217</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,507,664</td>
<td align="right">5,453,478</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">57,183,595</td>
<td align="right">57,715,626</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">994</td>
<td align="right">1,002</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,533,808</td>
<td align="right">44,874,378</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,962</td>
<td align="right">2,982</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,625,656</td>
<td align="right">44,342,330</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,131,560</td>
<td align="right">30,301,376</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,485,283</td>
<td align="right">17,583,270</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,289,153</td>
<td align="right">28,443,538</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,068</td>
<td align="right">18,165</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,705,205</td>
<td align="right">45,466,172</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">18,886,853</td>
<td align="right">18,984,648</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,738,093</td>
<td align="right">17,824,516</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,738,943</td>
<td align="right">21,644,653</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,960</td>
<td align="right">8,997</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,322,518</td>
<td align="right">13,270,812</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,798</td>
<td align="right">23,884</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,951,774</td>
<td align="right">37,081,149</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">172,424,753</td>
<td align="right">171,890,577</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,065</td>
<td align="right">11,098</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">172,494,258</td>
<td align="right">172,994,485</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,373,610</td>
<td align="right">51,227,791</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">57,413,182</td>
<td align="right">57,253,936</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,972,675</td>
<td align="right">17,927,488</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">38,770,717</td>
<td align="right">38,674,880</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">55,223,100</td>
<td align="right">55,101,966</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">56,734,082</td>
<td align="right">56,612,079</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,914,825</td>
<td align="right">7,897,896</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,078,615</td>
<td align="right">8,061,612</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86,120,665</td>
<td align="right">85,948,242</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,157,752</td>
<td align="right">43,238,588</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">143,588,663</td>
<td align="right">143,843,858</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">9,563,923</td>
<td align="right">9,547,022</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,653,025</td>
<td align="right">9,636,069</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">41,581,727</td>
<td align="right">41,508,721</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">31,385,091</td>
<td align="right">31,333,024</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">48,127,316</td>
<td align="right">48,052,610</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">123,466,242</td>
<td align="right">123,277,025</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,465,175</td>
<td align="right">11,448,217</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,409,090</td>
<td align="right">12,391,896</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,823,028</td>
<td align="right">53,762,911</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,244</td>
<td align="right">40,282</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">67,265,819</td>
<td align="right">67,206,286</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,970,303</td>
<td align="right">59,918,498</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,488,569</td>
<td align="right">17,475,032</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,723</td>
<td align="right">165,599</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">34,148,948</td>
<td align="right">34,174,088</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,239,478</td>
<td align="right">23,222,548</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">24,481,597</td>
<td align="right">24,463,857</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,824,402</td>
<td align="right">181,694,948</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,446</td>
<td align="right">1,445</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,733,922</td>
<td align="right">24,717,212</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220,137,366</td>
<td align="right">219,997,886</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,337</td>
<td align="right">495,025</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">50,960,332</td>
<td align="right">50,930,064</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">239,300,599</td>
<td align="right">239,160,726</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,247,030</td>
<td align="right">75,203,325</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,029,129</td>
<td align="right">53,000,155</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">642,839,899</td>
<td align="right">642,567,999</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,324</td>
<td align="right">1,287,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,759,203</td>
<td align="right">1,758,690</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,022</td>
<td align="right">171,977</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,227</td>
<td align="right">655,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,227</td>
<td align="right">655,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,227</td>
<td align="right">655,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,711,361</td>
<td align="right">21,715,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,400,433</td>
<td align="right">22,395,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">198,974,112</td>
<td align="right">198,942,682</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,274</td>
<td align="right">175,299</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,944</td>
<td align="right">745,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,555,252</td>
<td align="right">1,555,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,096</td>
<td align="right">83,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,779</td>
<td align="right">4,469,263</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,950</td>
<td align="right">389,907</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,568,811</td>
<td align="right">15,567,197</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,316</td>
<td align="right">2,995,023</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,680</td>
<td align="right">20,678</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,553</td>
<td align="right">2,008,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,897</td>
<td align="right">4,001,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">13,936,123</td>
<td align="right">13,937,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,503</td>
<td align="right">1,222,398</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,182</td>
<td align="right">2,585,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,073</td>
<td align="right">6,026,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,419</td>
<td align="right">2,418,224</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,813,525</td>
<td align="right">6,812,988</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,977</td>
<td align="right">6,589,469</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,585,473</td>
<td align="right">1,585,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,070</td>
<td align="right">6,622,622</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,334</td>
<td align="right">5,752,958</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,367</td>
<td align="right">746,324</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,784</td>
<td align="right">1,389,708</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,109,407</td>
<td align="right">49,106,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,900,136</td>
<td align="right">9,899,605</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,657</td>
<td align="right">78,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,588,645</td>
<td align="right">2,588,514</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,499</td>
<td align="right">654,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,515</td>
<td align="right">654,482</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,982</td>
<td align="right">1,029,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,029,873</td>
<td align="right">1,029,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,870,958</td>
<td align="right">10,871,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,562</td>
<td align="right">7,541,337</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,608</td>
<td align="right">942,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,785,918</td>
<td align="right">6,786,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,921,003</td>
<td align="right">10,920,713</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,297</td>
<td align="right">3,728,209</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,138,447</td>
<td align="right">33,137,770</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,282,801</td>
<td align="right">5,282,695</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,586,079</td>
<td align="right">4,585,989</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,564</td>
<td align="right">2,281,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,115,857</td>
<td align="right">15,116,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,618,006</td>
<td align="right">2,618,051</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,528</td>
<td align="right">598,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,390</td>
<td align="right">141,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,310</td>
<td align="right">1,323,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,740,958</td>
<td align="right">78,739,914</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,960</td>
<td align="right">745,951</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,170</td>
<td align="right">2,195,145</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,550</td>
<td align="right">427,546</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,524</td>
<td align="right">1,754,539</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,038,637</td>
<td align="right">11,038,549</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,410</td>
<td align="right">21,985,582</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,933,171</td>
<td align="right">8,933,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,912,117</td>
<td align="right">15,912,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,284</td>
<td align="right">6,744,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,442</td>
<td align="right">4,497,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,024</td>
<td align="right">21,977,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,523</td>
<td align="right">1,244,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,005,523</td>
<td align="right">21,005,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">32,099,335</td>
<td align="right">32,099,215</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,543</td>
<td align="right">456,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,792,653</td>
<td align="right">24,792,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,631,763</td>
<td align="right">18,631,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,881,425</td>
<td align="right">15,881,404</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,923</td>
<td align="right">9,777,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,762</td>
<td align="right">2,007,762</td>
<td align="right">0.0%</td>
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
<td align="right">60,266</td>
<td align="right">0.1%</td>
<td align="right">60,732</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44,594,424</td>
<td align="right">38.5%</td>
<td align="right">44,311,147</td>
<td align="right">38.3%</td>
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
<td align="right">71,190,107</td>
<td align="right">61.4%</td>
<td align="right">71,154,729</td>
<td align="right">61.6%</td>
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
<td align="right">3,235</td>
<td align="right">10.0%</td>
<td align="right">3,281</td>
<td align="right">10.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">29,138</td>
<td align="right">90.0%</td>
<td align="right">29,045</td>
<td align="right">89.9%</td>
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
<td align="left">subscr list slice</td>
<td align="right">272</td>
<td align="right">0.9%</td>
<td align="right">277</td>
<td align="right">1.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">0.7%</td>
<td align="right">210</td>
<td align="right">0.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,559</td>
<td align="right">15.6%</td>
<td align="right">4,495</td>
<td align="right">15.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,925</td>
<td align="right">13.5%</td>
<td align="right">3,881</td>
<td align="right">13.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.2%</td>
<td align="right">367</td>
<td align="right">1.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">92</td>
<td align="right">0.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,755</td>
<td align="right">6.0%</td>
<td align="right">1,741</td>
<td align="right">6.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">989</td>
<td align="right">3.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">704</td>
<td align="right">2.4%</td>
<td align="right">708</td>
<td align="right">2.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">567</td>
<td align="right">1.9%</td>
<td align="right">569</td>
<td align="right">2.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,208</td>
<td align="right">4.1%</td>
<td align="right">1,212</td>
<td align="right">4.2%</td>
<td align="right">0.3%</td>
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
<td align="left">add different types</td>
<td align="right">1,012</td>
<td align="right">3.5%</td>
<td align="right">1,013</td>
<td align="right">3.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,895</td>
<td align="right">9.9%</td>
<td align="right">2,896</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">3.7%</td>
<td align="right">1,086</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">1.4%</td>
<td align="right">422</td>
<td align="right">1.5%</td>
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
<td align="left">subscr array</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,618,100</td>
<td align="right">11.4%</td>
<td align="right">35,717,834</td>
<td align="right">11.4%</td>
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
<td align="right">36,294,386</td>
<td align="right">11.6%</td>
<td align="right">36,396,000</td>
<td align="right">11.6%</td>
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
<td align="right">276,347,914</td>
<td align="right">88.4%</td>
<td align="right">276,185,712</td>
<td align="right">88.3%</td>
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
<td align="left">Success</td>
<td align="right">700,084</td>
<td align="right">100.0%</td>
<td align="right">702,050</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">3,185</td>
<td align="right">74.9%</td>
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
<td align="right">1,068</td>
<td align="right">100.0%</td>
<td align="right">1,065</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">30,092,989</td>
<td align="right">36.9%</td>
<td align="right">30,262,769</td>
<td align="right">37.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">410,720</td>
<td align="right">0.5%</td>
<td align="right">409,704</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,034,612</td>
<td align="right">62.6%</td>
<td align="right">51,033,816</td>
<td align="right">62.4%</td>
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
<td align="right">8,861</td>
<td align="right">19.2%</td>
<td align="right">8,852</td>
<td align="right">19.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,403</td>
<td align="right">80.8%</td>
<td align="right">37,428</td>
<td align="right">80.9%</td>
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
<td align="left">bool</td>
<td align="right">1,446</td>
<td align="right">3.9%</td>
<td align="right">1,417</td>
<td align="right">3.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">117</td>
<td align="right">0.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,393</td>
<td align="right">17.1%</td>
<td align="right">6,471</td>
<td align="right">17.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,254</td>
<td align="right">11.4%</td>
<td align="right">4,272</td>
<td align="right">11.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,140</td>
<td align="right">37.8%</td>
<td align="right">14,097</td>
<td align="right">37.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,167</td>
<td align="right">8.5%</td>
<td align="right">3,164</td>
<td align="right">8.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,856,467</td>
<td align="right">31.6%</td>
<td align="right">10,725,041</td>
<td align="right">31.3%</td>
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
<td align="right">23,499,530</td>
<td align="right">68.4%</td>
<td align="right">23,499,761</td>
<td align="right">68.6%</td>
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
<td align="right">5,385</td>
<td align="right">97.8%</td>
<td align="right">5,358</td>
<td align="right">97.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">2.2%</td>
<td align="right">122</td>
<td align="right">2.2%</td>
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
<td align="right">3,434</td>
<td align="right">63.8%</td>
<td align="right">3,403</td>
<td align="right">63.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,470</td>
<td align="right">27.3%</td>
<td align="right">1,474</td>
<td align="right">27.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">5.6%</td>
<td align="right">299</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">3.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,223,653</td>
<td align="right">1.1%</td>
<td align="right">1,232,440</td>
<td align="right">1.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,654,564</td>
<td align="right">41.1%</td>
<td align="right">45,414,935</td>
<td align="right">41.0%</td>
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
<td align="right">64,067,501</td>
<td align="right">57.7%</td>
<td align="right">63,959,935</td>
<td align="right">57.8%</td>
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
<td align="left">Failure</td>
<td align="right">49,819</td>
<td align="right">67.7%</td>
<td align="right">50,410</td>
<td align="right">67.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23,823</td>
<td align="right">32.3%</td>
<td align="right">23,999</td>
<td align="right">32.3%</td>
<td align="right">0.7%</td>
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
<td align="left">dict items</td>
<td align="right">37,477</td>
<td align="right">75.2%</td>
<td align="right">38,112</td>
<td align="right">75.6%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,706</td>
<td align="right">5.4%</td>
<td align="right">2,664</td>
<td align="right">5.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,355</td>
<td align="right">2.7%</td>
<td align="right">1,356</td>
<td align="right">2.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,288</td>
<td align="right">12.6%</td>
<td align="right">6,285</td>
<td align="right">12.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
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
<td align="right">224,033,943</td>
<td align="right">66.7%</td>
<td align="right">206,668,059</td>
<td align="right">64.8%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,129,857</td>
<td align="right">15.5%</td>
<td align="right">52,587,670</td>
<td align="right">16.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,910,035</td>
<td align="right">17.8%</td>
<td align="right">59,858,149</td>
<td align="right">18.8%</td>
<td align="right">-0.1%</td>
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
<td align="left">Success</td>
<td align="right">994,408</td>
<td align="right">95.7%</td>
<td align="right">1,003,034</td>
<td align="right">95.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,067</td>
<td align="right">4.3%</td>
<td align="right">45,102</td>
<td align="right">4.3%</td>
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
<td align="left">overridden</td>
<td align="right">3,100</td>
<td align="right">6.9%</td>
<td align="right">3,106</td>
<td align="right">6.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,735</td>
<td align="right">6.1%</td>
<td align="right">2,740</td>
<td align="right">6.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,403</td>
<td align="right">47.5%</td>
<td align="right">21,431</td>
<td align="right">47.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,125</td>
<td align="right">6.9%</td>
<td align="right">3,122</td>
<td align="right">6.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,065</td>
<td align="right">9.0%</td>
<td align="right">4,064</td>
<td align="right">9.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,832</td>
<td align="right">15.2%</td>
<td align="right">6,832</td>
<td align="right">15.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">206</td>
<td align="right">0.5%</td>
<td align="right">206</td>
<td align="right">0.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,532</td>
<td align="right">0.0%</td>
<td align="right">4,597</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,302</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">260,051,521</td>
<td align="right">100.0%</td>
<td align="right">260,379,311</td>
<td align="right">100.0%</td>
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
<td align="right">13,584</td>
<td align="right">100.0%</td>
<td align="right">13,618</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,918</td>
<td align="right">100.0%</td>
<td align="right">2,265,964</td>
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
<td align="right">731,656</td>
<td align="right">72.0%</td>
<td align="right">731,613</td>
<td align="right">72.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,576,962</td>
<td align="right">17.4%</td>
<td align="right">1,575,777</td>
<td align="right">17.4%</td>
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
<td align="right">173,967</td>
<td align="right">1.9%</td>
<td align="right">173,997</td>
<td align="right">1.9%</td>
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
<td align="right">7,327,672</td>
<td align="right">80.7%</td>
<td align="right">7,328,365</td>
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
<td align="right">971</td>
<td align="right">3.1%</td>
<td align="right">966</td>
<td align="right">3.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,010</td>
<td align="right">96.9%</td>
<td align="right">29,977</td>
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
<td align="right">292</td>
<td align="right">30.1%</td>
<td align="right">290</td>
<td align="right">30.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">518</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,583,063</td>
<td align="right">12.7%</td>
<td align="right">2,583,284</td>
<td align="right">12.7%</td>
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
<td align="right">17,739,993</td>
<td align="right">87.3%</td>
<td align="right">17,740,125</td>
<td align="right">87.3%</td>
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
<td align="right">169,286,140</td>
<td align="right">94.2%</td>
<td align="right">167,851,963</td>
<td align="right">94.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">623,355</td>
<td align="right">0.3%</td>
<td align="right">623,481</td>
<td align="right">0.3%</td>
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
<td align="right">9,755,881</td>
<td align="right">5.4%</td>
<td align="right">9,755,839</td>
<td align="right">5.5%</td>
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
<td align="right">18,968</td>
<td align="right">57.1%</td>
<td align="right">19,006</td>
<td align="right">57.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,274</td>
<td align="right">42.9%</td>
<td align="right">14,295</td>
<td align="right">42.9%</td>
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
<td align="left">number</td>
<td align="right">1,253</td>
<td align="right">8.8%</td>
<td align="right">1,262</td>
<td align="right">8.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,620</td>
<td align="right">18.4%</td>
<td align="right">2,607</td>
<td align="right">18.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,986</td>
<td align="right">55.9%</td>
<td align="right">8,011</td>
<td align="right">56.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">721</td>
<td align="right">5.1%</td>
<td align="right">723</td>
<td align="right">5.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">725</td>
<td align="right">5.1%</td>
<td align="right">723</td>
<td align="right">5.1%</td>
<td align="right">-0.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,264</td>
<td align="right">0.0%</td>
<td align="right">6,293</td>
<td align="right">0.0%</td>
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
<td align="right">83,458,944</td>
<td align="right">100.0%</td>
<td align="right">83,397,294</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">2,391</td>
<td align="right">88.7%</td>
<td align="right">2,399</td>
<td align="right">88.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">305</td>
<td align="right">11.3%</td>
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
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">43</td>
<td align="right">14.1%</td>
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
<td align="right">92,339,032</td>
<td align="right">2.2%</td>
<td align="right">92,905,644</td>
<td align="right">2.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">204,168,133</td>
<td align="right">4.8%</td>
<td align="right">203,632,808</td>
<td align="right">4.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,421,125,995</td>
<td align="right">56.7%</td>
<td align="right">2,420,104,694</td>
<td align="right">56.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,554,685,518</td>
<td align="right">36.4%</td>
<td align="right">1,554,818,489</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
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
<td align="right">10,856,467</td>
<td align="right">4.5%</td>
<td align="right">10,725,041</td>
<td align="right">4.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,594,424</td>
<td align="right">18.6%</td>
<td align="right">44,311,147</td>
<td align="right">18.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,092,989</td>
<td align="right">12.6%</td>
<td align="right">30,262,769</td>
<td align="right">12.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,654,564</td>
<td align="right">19.1%</td>
<td align="right">45,414,935</td>
<td align="right">19.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,618,100</td>
<td align="right">14.9%</td>
<td align="right">35,717,834</td>
<td align="right">14.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,910,035</td>
<td align="right">25.0%</td>
<td align="right">59,858,149</td>
<td align="right">25.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,967</td>
<td align="right">0.1%</td>
<td align="right">173,997</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,063</td>
<td align="right">1.1%</td>
<td align="right">2,583,284</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,881</td>
<td align="right">4.1%</td>
<td align="right">9,755,839</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">12,275,744</td>
<td align="right">13.3%</td>
<td align="right">12,749,027</td>
<td align="right">13.7%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,130,861</td>
<td align="right">12.1%</td>
<td align="right">11,231,056</td>
<td align="right">12.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,211,249</td>
<td align="right">3.5%</td>
<td align="right">3,214,471</td>
<td align="right">3.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,576,183</td>
<td align="right">1.7%</td>
<td align="right">1,574,998</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,913,652</td>
<td align="right">31.3%</td>
<td align="right">28,894,739</td>
<td align="right">31.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,701,093</td>
<td align="right">12.7%</td>
<td align="right">11,702,285</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,149,157</td>
<td align="right">6.7%</td>
<td align="right">6,149,429</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,010</td>
<td align="right">7.9%</td>
<td align="right">7,312,311</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,667</td>
<td align="right">5.5%</td>
<td align="right">5,102,581</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,571</td>
<td align="right">2.3%</td>
<td align="right">2,103,575</td>
<td align="right">2.3%</td>
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
<td align="left">Frames pushed</td>
<td align="right">187,626,826</td>
<td align="right">89.3%</td>
<td align="right">187,480,708</td>
<td align="right">89.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,172,618</td>
<td align="right">62.4%</td>
<td align="right">131,125,286</td>
<td align="right">62.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,295</td>
<td align="right">0.5%</td>
<td align="right">950,138</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,141,940</td>
<td align="right">19.6%</td>
<td align="right">41,141,044</td>
<td align="right">19.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,425,786</td>
<td align="right">35.9%</td>
<td align="right">75,424,785</td>
<td align="right">35.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,426,571</td>
<td align="right">35.9%</td>
<td align="right">75,425,570</td>
<td align="right">35.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,895,373</td>
<td align="right">37.6%</td>
<td align="right">78,894,333</td>
<td align="right">37.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,895,373</td>
<td align="right">37.6%</td>
<td align="right">78,894,333</td>
<td align="right">37.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,802</td>
<td align="right">1.7%</td>
<td align="right">3,468,763</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,962</td>
<td align="right">4.4%</td>
<td align="right">9,332,016</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,580</td>
<td align="right">8.8%</td>
<td align="right">18,490,476</td>
<td align="right">8.8%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">1,841,901</td>
<td align="right"></td>
<td align="right">2,038,107</td>
<td align="right"></td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,356,014</td>
<td align="right"></td>
<td align="right">4,654,998</td>
<td align="right"></td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,515,602</td>
<td align="right"></td>
<td align="right">2,618,521</td>
<td align="right"></td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">756,920</td>
<td align="right">0.2%</td>
<td align="right">750,201</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">149,170,113</td>
<td align="right"></td>
<td align="right">149,522,866</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,429,988</td>
<td align="right">1.3%</td>
<td align="right">51,549,068</td>
<td align="right">1.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,354,457</td>
<td align="right"></td>
<td align="right">248,028,793</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,395,454,344</td>
<td align="right">34.3%</td>
<td align="right">1,393,866,564</td>
<td align="right">34.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,279,123,859</td>
<td align="right">36.1%</td>
<td align="right">1,277,792,126</td>
<td align="right">36.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,177,395</td>
<td align="right">25.9%</td>
<td align="right">129,106,160</td>
<td align="right">25.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,411,627</td>
<td align="right">25.7%</td>
<td align="right">128,347,111</td>
<td align="right">25.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,816,324</td>
<td align="right"></td>
<td align="right">141,745,315</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">76,051,715</td>
<td align="right">2.1%</td>
<td align="right">76,016,444</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">972,123,589</td>
<td align="right">27.4%</td>
<td align="right">972,536,634</td>
<td align="right">27.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,537,533,579</td>
<td align="right">37.8%</td>
<td align="right">1,538,064,003</td>
<td align="right">37.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,214,311,536</td>
<td align="right">34.3%</td>
<td align="right">1,214,708,474</td>
<td align="right">34.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,083,789,854</td>
<td align="right">26.6%</td>
<td align="right">1,083,594,046</td>
<td align="right">26.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">370,514,792</td>
<td align="right">74.1%</td>
<td align="right">370,456,319</td>
<td align="right">74.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">370,549,580</td>
<td align="right"></td>
<td align="right">370,491,107</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,301</td>
<td align="right"></td>
<td align="right">866,287</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,848</td>
<td align="right">0.0%</td>
<td align="right">8,848</td>
<td align="right">0.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">115</td>
<td align="right">0.6%</td>
<td align="right">136</td>
<td align="right">0.7%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,858</td>
<td align="right">31.3%</td>
<td align="right">5,936</td>
<td align="right">31.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">49,557,742</td>
<td align="right"></td>
<td align="right">49,053,679</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,652,695,639</td>
<td align="right">3,334.9%</td>
<td align="right">1,661,969,922</td>
<td align="right">3,388.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,723</td>
<td align="right"></td>
<td align="right">18,796</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,879</td>
<td align="right">10.0%</td>
<td align="right">1,885</td>
<td align="right">10.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,847</td>
<td align="right">9.9%</td>
<td align="right">1,852</td>
<td align="right">9.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">9,139</td>
<td align="right">48.8%</td>
<td align="right">9,123</td>
<td align="right">48.5%</td>
<td align="right">-0.2%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">152</td>
<td align="right">0.8%</td>
<td align="right">152</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">1,816</td>
<td align="right">96.6%</td>
<td align="right">1,726</td>
<td align="right">91.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,879</td>
<td align="right"></td>
<td align="right">1,885</td>
<td align="right"></td>
<td align="right">0.3%</td>
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
<td align="right">15,024,128</td>
<td align="right">80.5%</td>
<td align="right">13,111,296</td>
<td align="right">78.3%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">14,356,382</td>
<td align="right">76.9%</td>
<td align="right">12,687,132</td>
<td align="right">75.8%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">18,669,568</td>
<td align="right"></td>
<td align="right">16,736,256</td>
<td align="right"></td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">425,544</td>
<td align="right">2.3%</td>
<td align="right">387,048</td>
<td align="right">2.3%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,887,642</td>
<td align="right">20.8%</td>
<td align="right">3,662,076</td>
<td align="right">21.9%</td>
<td align="right">-5.8%</td>
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
<td align="left">383</td>
<td align="right">21.1%</td>
<td align="left">404</td>
<td align="right">23.4%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">707</td>
<td align="right">38.9%</td>
<td align="left">846</td>
<td align="right">49.0%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">533</td>
<td align="right">29.4%</td>
<td align="left">304</td>
<td align="right">17.6%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">172</td>
<td align="right">9.5%</td>
<td align="left">151</td>
<td align="right">8.7%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">1.2%</td>
<td align="left">21</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
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
<td align="right">67</td>
<td align="right">3.6%</td>
<td align="right">81</td>
<td align="right">4.3%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">117</td>
<td align="right">6.2%</td>
<td align="right">231</td>
<td align="right">12.3%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">400</td>
<td align="right">21.3%</td>
<td align="right">390</td>
<td align="right">20.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">908</td>
<td align="right">48.3%</td>
<td align="right">796</td>
<td align="right">42.2%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">321</td>
<td align="right">17.1%</td>
<td align="right">321</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">45</td>
<td align="right">2.4%</td>
<td align="right">45</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21</td>
<td align="right">1.1%</td>
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
<td align="left"><= 4</td>
<td align="right">67</td>
<td align="right">3.6%</td>
<td align="right">81</td>
<td align="right">4.3%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">111</td>
<td align="right">5.9%</td>
<td align="right">111 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">252</td>
<td align="right">13.4%</td>
<td align="right">208</td>
<td align="right">11.0%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">855</td>
<td align="right">45.5%</td>
<td align="right">769</td>
<td align="right">40.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">362</td>
<td align="right">19.3%</td>
<td align="right">277</td>
<td align="right">14.7%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">259</td>
<td align="right">13.8%</td>
<td align="right">259</td>
<td align="right">13.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
<td align="right">297,718</td>
<td align="right">1,081</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">15,523,189</td>
<td align="right">2,178,765</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">3,954,835</td>
<td align="right">5,509,714</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,030,722</td>
<td align="right">1,437,886</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">6,158,597</td>
<td align="right">4,470,786</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,303</td>
<td align="right">1,081</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,114,288</td>
<td align="right">1,756,084</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,685,373</td>
<td align="right">3,968,012</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">317,151</td>
<td align="right">362,001</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,687,455</td>
<td align="right">2,391,040</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">23,589,470</td>
<td align="right">21,797,005</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">7,700</td>
<td align="right">7,255</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,609,443</td>
<td align="right">1,680,695</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">300,008,492</td>
<td align="right">313,030,609</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,254,240</td>
<td align="right">1,201,231</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,254,240</td>
<td align="right">1,201,231</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,686,386</td>
<td align="right">1,757,638</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,129,106</td>
<td align="right">2,998,213</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,145,005</td>
<td align="right">3,014,112</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,210,021</td>
<td align="right">4,993,238</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">330,948,757</td>
<td align="right">344,485,422</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,105,006</td>
<td align="right">1,149,856</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,251,316</td>
<td align="right">3,120,423</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">14,062,759</td>
<td align="right">13,637,947</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,361,599</td>
<td align="right">12,054,063</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,936,089</td>
<td align="right">6,788,448</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">4,991,554</td>
<td align="right">5,085,661</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,986,870</td>
<td align="right">4,061,244</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,064,675</td>
<td align="right">3,011,655</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">12,056,186</td>
<td align="right">12,257,468</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,056,186</td>
<td align="right">12,257,468</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">10,050,636</td>
<td align="right">10,205,103</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">5,530,870</td>
<td align="right">5,614,760</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,290,523</td>
<td align="right">8,407,639</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">39,846,337</td>
<td align="right">40,356,680</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,231,154</td>
<td align="right">6,305,527</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,910,582</td>
<td align="right">10,013,640</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">4,991,554</td>
<td align="right">5,043,213</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">49,557,742</td>
<td align="right">49,053,679</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">49,557,742</td>
<td align="right">49,053,679</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,054,133</td>
<td align="right">6,105,791</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,495,946</td>
<td align="right">6,547,599</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">30,981,432</td>
<td align="right">31,223,869</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,608,946</td>
<td align="right">7,660,600</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,161,272</td>
<td align="right">26,033,148</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,826,521</td>
<td align="right">10,878,163</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">35,838,942</td>
<td align="right">35,995,554</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,914,229</td>
<td align="right">17,968,642</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">26,084,209</td>
<td align="right">26,144,182</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">26,806,130</td>
<td align="right">26,866,101</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">26,806,130</td>
<td align="right">26,866,101</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,716,373</td>
<td align="right">11,691,508</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">80,149,142</td>
<td align="right">80,313,556</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,415,044</td>
<td align="right">24,378,253</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,974,084</td>
<td align="right">5,968,273</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,803,327</td>
<td align="right">15,788,971</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">8,563</td>
<td align="right">8,556</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">31,049,462</td>
<td align="right">31,028,290</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,499,414</td>
<td align="right">6,503,253</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,382,856</td>
<td align="right">7,386,695</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">32,550,141</td>
<td align="right">32,535,785</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">22,416,832</td>
<td align="right">22,420,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">26,096,249</td>
<td align="right">26,100,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">26,096,249</td>
<td align="right">26,100,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,037,141</td>
<td align="right">5,036,685</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">89,404,079</td>
<td align="right">89,410,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,646</td>
<td align="right">2,513,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,350,610</td>
<td align="right">3,350,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,072,552</td>
<td align="right">1,072,545</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,437,892</td>
<td align="right">1,437,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,567,856</td>
<td align="right">1,567,850</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,567,856</td>
<td align="right">1,567,850</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,398,793</td>
<td align="right">13,398,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,209,506</td>
<td align="right">2,209,499</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,763,663</td>
<td align="right">1,763,658</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,763,663</td>
<td align="right">1,763,658</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,279,125</td>
<td align="right">2,279,119</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,449,407</td>
<td align="right">2,449,401</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,828,631</td>
<td align="right">1,828,629</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,125,157</td>
<td align="right">2,125,155</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,125,158</td>
<td align="right">2,125,156</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,062,579</td>
<td align="right">1,062,578</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,231,521</td>
<td align="right">3,231,518</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,340,642</td>
<td align="right">3,340,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,398,793</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,849,482</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,254,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">833,316</td>
<td align="right">833,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">174,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">155,735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">144,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">128,958</td>
<td align="right">128,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">90,320</td>
<td align="right">90,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">73,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">52,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">45,128</td>
<td align="right">45,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">45,128</td>
<td align="right">45,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">39,898</td>
<td align="right">39,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">36,456</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">35,660</td>
<td align="right">35,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">28,192</td>
<td align="right">28,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">28,192</td>
<td align="right">28,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">18,228</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,384</td>
<td align="right">7,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">5,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,096</td>
<td align="right">3,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">13,398,837</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right"></td>
<td align="right">1,963,439</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">1,512,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">42,448</td>
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
<td align="right">567</td>
<td align="right">553</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,480</td>
<td align="right">1,495</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">21</td>
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
Stats gathered on: 2025-04-25
