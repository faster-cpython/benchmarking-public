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
<td align="right">245,891</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,678,169</td>
<td align="right">11,271,464</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">15,070,697</td>
<td align="right">14,831,401</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,738,093</td>
<td align="right">18,018,500</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,162,591</td>
<td align="right">17,875,992</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,485,283</td>
<td align="right">17,752,005</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">18,886,853</td>
<td align="right">19,153,506</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,131,560</td>
<td align="right">30,508,270</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">34,148,948</td>
<td align="right">34,539,777</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,666</td>
<td align="right">4,134,021</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,960</td>
<td align="right">9,059</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,669,722</td>
<td align="right">43,113,185</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">57,183,595</td>
<td align="right">57,770,368</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,418,127</td>
<td align="right">9,496,747</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,289,153</td>
<td align="right">28,524,828</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,533,808</td>
<td align="right">44,862,059</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,861,974</td>
<td align="right">10,940,535</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,823,028</td>
<td align="right">54,193,208</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,157,752</td>
<td align="right">43,440,266</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,029,129</td>
<td align="right">53,375,292</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,507,664</td>
<td align="right">5,472,986</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,738,943</td>
<td align="right">21,621,383</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,322,518</td>
<td align="right">13,252,772</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">55,223,100</td>
<td align="right">55,508,349</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">56,734,082</td>
<td align="right">57,018,926</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">57,413,182</td>
<td align="right">57,683,212</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,625,656</td>
<td align="right">44,798,753</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,705,205</td>
<td align="right">45,859,684</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,972,675</td>
<td align="right">17,913,417</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">172,494,258</td>
<td align="right">173,033,208</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">994</td>
<td align="right">997</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">143,588,663</td>
<td align="right">144,017,653</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,244</td>
<td align="right">40,363</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,951,774</td>
<td align="right">37,056,274</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86,120,665</td>
<td align="right">85,929,792</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">31,385,091</td>
<td align="right">31,317,117</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">172,424,753</td>
<td align="right">172,776,155</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220,137,366</td>
<td align="right">220,566,598</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,914,825</td>
<td align="right">7,930,164</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,078,615</td>
<td align="right">8,093,894</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,373,610</td>
<td align="right">51,467,439</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">198,974,112</td>
<td align="right">199,324,047</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,068</td>
<td align="right">18,099</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">9,563,923</td>
<td align="right">9,579,514</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,653,025</td>
<td align="right">9,668,491</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">48,127,316</td>
<td align="right">48,054,067</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,446</td>
<td align="right">1,444</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,962</td>
<td align="right">2,966</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,465,175</td>
<td align="right">11,480,570</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,065</td>
<td align="right">11,079</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,409,090</td>
<td align="right">12,424,361</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,798</td>
<td align="right">23,826</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,970,303</td>
<td align="right">59,901,741</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,400,433</td>
<td align="right">22,424,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">38,770,717</td>
<td align="right">38,733,392</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,247,030</td>
<td align="right">75,188,877</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">67,265,819</td>
<td align="right">67,215,611</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,239,478</td>
<td align="right">23,256,613</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,680</td>
<td align="right">20,694</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">24,481,597</td>
<td align="right">24,497,592</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,733,922</td>
<td align="right">24,749,905</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">642,839,899</td>
<td align="right">643,207,902</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">41,581,727</td>
<td align="right">41,558,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">239,300,599</td>
<td align="right">239,170,132</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,488,569</td>
<td align="right">17,497,602</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,274</td>
<td align="right">175,362</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">50,960,332</td>
<td align="right">50,985,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,096</td>
<td align="right">83,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,824,402</td>
<td align="right">181,907,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,711,361</td>
<td align="right">21,720,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,503</td>
<td align="right">1,222,001</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">123,466,242</td>
<td align="right">123,515,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,944</td>
<td align="right">745,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,227</td>
<td align="right">655,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,227</td>
<td align="right">655,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,227</td>
<td align="right">655,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,657</td>
<td align="right">78,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,723</td>
<td align="right">165,669</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,337</td>
<td align="right">495,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,555,252</td>
<td align="right">1,555,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,585,473</td>
<td align="right">1,585,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,022</td>
<td align="right">171,983</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">13,936,123</td>
<td align="right">13,939,182</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,982</td>
<td align="right">1,029,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,029,873</td>
<td align="right">1,030,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,324</td>
<td align="right">1,288,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,553</td>
<td align="right">2,008,818</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,950</td>
<td align="right">389,902</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,912,117</td>
<td align="right">15,913,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,759,203</td>
<td align="right">1,758,998</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,933,171</td>
<td align="right">8,934,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,390</td>
<td align="right">141,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,073</td>
<td align="right">6,026,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,442</td>
<td align="right">4,497,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,182</td>
<td align="right">2,585,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,960</td>
<td align="right">746,028</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,543</td>
<td align="right">456,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,813,525</td>
<td align="right">6,814,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,900,136</td>
<td align="right">9,900,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,779</td>
<td align="right">4,469,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,334</td>
<td align="right">5,753,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,784</td>
<td align="right">1,389,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,977</td>
<td align="right">6,590,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,367</td>
<td align="right">746,319</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,870,958</td>
<td align="right">10,871,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,608</td>
<td align="right">942,668</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,785,918</td>
<td align="right">6,786,325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,631,763</td>
<td align="right">18,632,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,762</td>
<td align="right">2,007,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,115,857</td>
<td align="right">15,116,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,419</td>
<td align="right">2,418,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">32,099,335</td>
<td align="right">32,100,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,568,811</td>
<td align="right">15,568,083</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,792,653</td>
<td align="right">24,793,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,588,645</td>
<td align="right">2,588,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,897</td>
<td align="right">4,002,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,618,006</td>
<td align="right">2,618,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,005,523</td>
<td align="right">21,006,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,881,425</td>
<td align="right">15,881,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,070</td>
<td align="right">6,623,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,297</td>
<td align="right">3,728,167</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,024</td>
<td align="right">21,977,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,499</td>
<td align="right">654,519</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,515</td>
<td align="right">654,535</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,138,447</td>
<td align="right">33,139,251</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,562</td>
<td align="right">7,541,738</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,109,407</td>
<td align="right">49,110,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,564</td>
<td align="right">2,281,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,410</td>
<td align="right">21,985,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,284</td>
<td align="right">6,744,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,921,003</td>
<td align="right">10,921,189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,170</td>
<td align="right">2,195,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,528</td>
<td align="right">598,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,923</td>
<td align="right">9,778,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,038,637</td>
<td align="right">11,038,794</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,523</td>
<td align="right">1,244,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,550</td>
<td align="right">427,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,740,958</td>
<td align="right">78,740,497</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,524</td>
<td align="right">1,754,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,586,079</td>
<td align="right">4,586,066</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,310</td>
<td align="right">1,323,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,282,801</td>
<td align="right">5,282,791</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,316</td>
<td align="right">2,995,320</td>
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
<td align="right">60,614</td>
<td align="right">0.1%</td>
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
<td align="right">44,594,424</td>
<td align="right">38.5%</td>
<td align="right">44,767,481</td>
<td align="right">38.6%</td>
<td align="right">0.4%</td>
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
<td align="right">71,225,043</td>
<td align="right">61.4%</td>
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
<td align="right">3,235</td>
<td align="right">10.0%</td>
<td align="right">3,240</td>
<td align="right">10.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">29,138</td>
<td align="right">90.0%</td>
<td align="right">29,178</td>
<td align="right">90.0%</td>
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
<td align="left">subscr list slice</td>
<td align="right">272</td>
<td align="right">0.9%</td>
<td align="right">275</td>
<td align="right">0.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,559</td>
<td align="right">15.6%</td>
<td align="right">4,603</td>
<td align="right">15.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">0.7%</td>
<td align="right">211</td>
<td align="right">0.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,755</td>
<td align="right">6.0%</td>
<td align="right">1,766</td>
<td align="right">6.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,925</td>
<td align="right">13.5%</td>
<td align="right">3,905</td>
<td align="right">13.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,012</td>
<td align="right">3.5%</td>
<td align="right">1,009</td>
<td align="right">3.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,208</td>
<td align="right">4.1%</td>
<td align="right">1,211</td>
<td align="right">4.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">567</td>
<td align="right">1.9%</td>
<td align="right">568</td>
<td align="right">1.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">624</td>
<td align="right">2.1%</td>
<td align="right">625</td>
<td align="right">2.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">704</td>
<td align="right">2.4%</td>
<td align="right">705</td>
<td align="right">2.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,895</td>
<td align="right">9.9%</td>
<td align="right">2,896</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">3,221</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.6%</td>
<td align="right">2,225</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">2,142</td>
<td align="right">7.3%</td>
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
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">982</td>
<td align="right">3.4%</td>
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
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.2%</td>
<td align="right">363</td>
<td align="right">1.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">36,294,386</td>
<td align="right">11.6%</td>
<td align="right">36,569,652</td>
<td align="right">11.7%</td>
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
<td align="right">35,618,100</td>
<td align="right">11.4%</td>
<td align="right">35,888,177</td>
<td align="right">11.5%</td>
<td align="right">0.8%</td>
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
<td align="right">276,456,378</td>
<td align="right">88.3%</td>
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
<td align="right">700,084</td>
<td align="right">100.0%</td>
<td align="right">705,301</td>
<td align="right">100.0%</td>
<td align="right">0.7%</td>
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
<td align="right">1,068</td>
<td align="right">100.0%</td>
<td align="right">1,066</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">30,469,654</td>
<td align="right">37.2%</td>
<td align="right">1.3%</td>
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
<td align="right">409,661</td>
<td align="right">0.5%</td>
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
<td align="right">51,034,612</td>
<td align="right">62.6%</td>
<td align="right">51,036,550</td>
<td align="right">62.3%</td>
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
<td align="right">8,861</td>
<td align="right">19.2%</td>
<td align="right">8,840</td>
<td align="right">19.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,403</td>
<td align="right">80.8%</td>
<td align="right">37,449</td>
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
<td align="right">1,468</td>
<td align="right">3.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,393</td>
<td align="right">17.1%</td>
<td align="right">6,482</td>
<td align="right">17.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,167</td>
<td align="right">8.5%</td>
<td align="right">3,145</td>
<td align="right">8.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,140</td>
<td align="right">37.8%</td>
<td align="right">14,103</td>
<td align="right">37.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,254</td>
<td align="right">11.4%</td>
<td align="right">4,247</td>
<td align="right">11.3%</td>
<td align="right">-0.2%</td>
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
<td align="left">baseobject</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">115</td>
<td align="right">0.3%</td>
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
<td align="right">10,935,005</td>
<td align="right">31.7%</td>
<td align="right">0.7%</td>
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
<td align="right">23,499,831</td>
<td align="right">68.2%</td>
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
<td align="right">5,408</td>
<td align="right">97.8%</td>
<td align="right">0.4%</td>
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
<td align="right">3,455</td>
<td align="right">63.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,470</td>
<td align="right">27.3%</td>
<td align="right">1,472</td>
<td align="right">27.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">5.6%</td>
<td align="right">299</td>
<td align="right">5.5%</td>
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
<td align="right">1,249,943</td>
<td align="right">1.1%</td>
<td align="right">2.1%</td>
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
<td align="right">45,807,529</td>
<td align="right">41.2%</td>
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
<td align="right">64,067,501</td>
<td align="right">57.7%</td>
<td align="right">64,093,402</td>
<td align="right">57.6%</td>
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
<td align="right">49,819</td>
<td align="right">67.7%</td>
<td align="right">51,335</td>
<td align="right">67.9%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23,823</td>
<td align="right">32.3%</td>
<td align="right">24,316</td>
<td align="right">32.1%</td>
<td align="right">2.1%</td>
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
<td align="right">38,924</td>
<td align="right">75.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,288</td>
<td align="right">12.6%</td>
<td align="right">6,393</td>
<td align="right">12.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,706</td>
<td align="right">5.4%</td>
<td align="right">2,664</td>
<td align="right">5.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,355</td>
<td align="right">2.7%</td>
<td align="right">1,361</td>
<td align="right">2.7%</td>
<td align="right">0.4%</td>
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
<td align="right">0.7%</td>
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
<td align="right">209,039,081</td>
<td align="right">65.0%</td>
<td align="right">-6.7%</td>
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
<td align="right">52,572,337</td>
<td align="right">16.4%</td>
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
<td align="right">59,910,035</td>
<td align="right">17.8%</td>
<td align="right">59,841,421</td>
<td align="right">18.6%</td>
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
<td align="right">1,002,743</td>
<td align="right">95.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,067</td>
<td align="right">4.3%</td>
<td align="right">45,108</td>
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
<td align="left">method</td>
<td align="right">2,735</td>
<td align="right">6.1%</td>
<td align="right">2,748</td>
<td align="right">6.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,125</td>
<td align="right">6.9%</td>
<td align="right">3,118</td>
<td align="right">6.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,403</td>
<td align="right">47.5%</td>
<td align="right">21,441</td>
<td align="right">47.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,065</td>
<td align="right">9.0%</td>
<td align="right">4,060</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,100</td>
<td align="right">6.9%</td>
<td align="right">3,101</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
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
<td align="right">4,546</td>
<td align="right">0.0%</td>
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
<td align="right">260,051,521</td>
<td align="right">100.0%</td>
<td align="right">260,399,587</td>
<td align="right">100.0%</td>
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
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,294</td>
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
<td align="right">13,584</td>
<td align="right">100.0%</td>
<td align="right">13,601</td>
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
<td align="right">2,265,918</td>
<td align="right">100.0%</td>
<td align="right">2,265,981</td>
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
<td align="right">731,656</td>
<td align="right">72.0%</td>
<td align="right">731,608</td>
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
<td align="right">1,575,839</td>
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
<td align="right">174,049</td>
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
<td align="right">7,329,076</td>
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
<td align="right">977</td>
<td align="right">3.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,010</td>
<td align="right">96.9%</td>
<td align="right">29,977</td>
<td align="right">96.8%</td>
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
<td align="right">300</td>
<td align="right">30.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">518</td>
<td align="right">53.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.4%</td>
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
<td align="right">17,739,993</td>
<td align="right">87.3%</td>
<td align="right">17,741,864</td>
<td align="right">87.3%</td>
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
<td align="right">2,583,063</td>
<td align="right">12.7%</td>
<td align="right">2,583,305</td>
<td align="right">12.7%</td>
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
<td align="right">168,046,598</td>
<td align="right">94.2%</td>
<td align="right">-0.7%</td>
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
<td align="right">623,471</td>
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
<td align="right">9,756,000</td>
<td align="right">5.5%</td>
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
<td align="right">42.9%</td>
<td align="right">14,297</td>
<td align="right">42.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,968</td>
<td align="right">57.1%</td>
<td align="right">18,991</td>
<td align="right">57.1%</td>
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
<td align="right">1,268</td>
<td align="right">8.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">721</td>
<td align="right">5.1%</td>
<td align="right">727</td>
<td align="right">5.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">725</td>
<td align="right">5.1%</td>
<td align="right">720</td>
<td align="right">5.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,620</td>
<td align="right">18.4%</td>
<td align="right">2,604</td>
<td align="right">18.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,986</td>
<td align="right">55.9%</td>
<td align="right">8,009</td>
<td align="right">56.0%</td>
<td align="right">0.3%</td>
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
<td align="right">6,365</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
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
<td align="right">83,817,212</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">303</td>
<td align="right">11.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,391</td>
<td align="right">88.7%</td>
<td align="right">2,391</td>
<td align="right">88.8%</td>
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
<td align="right">260</td>
<td align="right">85.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">43</td>
<td align="right">14.2%</td>
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
<td align="right">93,081,348</td>
<td align="right">2.2%</td>
<td align="right">0.8%</td>
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
<td align="right">204,883,060</td>
<td align="right">4.8%</td>
<td align="right">0.4%</td>
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
<td align="right">1,557,296,039</td>
<td align="right">36.4%</td>
<td align="right">0.2%</td>
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
<td align="right">2,424,668,373</td>
<td align="right">56.7%</td>
<td align="right">0.1%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">30,092,989</td>
<td align="right">12.6%</td>
<td align="right">30,469,654</td>
<td align="right">12.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,618,100</td>
<td align="right">14.9%</td>
<td align="right">35,888,177</td>
<td align="right">14.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,856,467</td>
<td align="right">4.5%</td>
<td align="right">10,935,005</td>
<td align="right">4.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,594,424</td>
<td align="right">18.6%</td>
<td align="right">44,767,481</td>
<td align="right">18.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,654,564</td>
<td align="right">19.1%</td>
<td align="right">45,807,529</td>
<td align="right">19.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,910,035</td>
<td align="right">25.0%</td>
<td align="right">59,841,421</td>
<td align="right">24.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,967</td>
<td align="right">0.1%</td>
<td align="right">174,049</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,063</td>
<td align="right">1.1%</td>
<td align="right">2,583,305</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,881</td>
<td align="right">4.1%</td>
<td align="right">9,756,000</td>
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
<td align="right">12,275,744</td>
<td align="right">13.3%</td>
<td align="right">12,736,391</td>
<td align="right">13.7%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,130,861</td>
<td align="right">12.1%</td>
<td align="right">11,402,493</td>
<td align="right">12.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,211,249</td>
<td align="right">3.5%</td>
<td align="right">3,216,871</td>
<td align="right">3.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,913,652</td>
<td align="right">31.3%</td>
<td align="right">28,889,869</td>
<td align="right">31.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,576,183</td>
<td align="right">1.7%</td>
<td align="right">1,575,060</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,701,093</td>
<td align="right">12.7%</td>
<td align="right">11,704,078</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,149,157</td>
<td align="right">6.7%</td>
<td align="right">6,149,694</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,667</td>
<td align="right">5.5%</td>
<td align="right">5,102,586</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,010</td>
<td align="right">7.9%</td>
<td align="right">7,311,959</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,571</td>
<td align="right">2.3%</td>
<td align="right">2,103,584</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,172,618</td>
<td align="right">62.4%</td>
<td align="right">131,538,473</td>
<td align="right">62.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,626,826</td>
<td align="right">89.3%</td>
<td align="right">187,725,410</td>
<td align="right">89.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,295</td>
<td align="right">0.5%</td>
<td align="right">950,443</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,802</td>
<td align="right">1.7%</td>
<td align="right">3,469,027</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,141,940</td>
<td align="right">19.6%</td>
<td align="right">41,140,541</td>
<td align="right">19.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,962</td>
<td align="right">4.4%</td>
<td align="right">9,332,180</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,580</td>
<td align="right">8.8%</td>
<td align="right">18,490,889</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,425,786</td>
<td align="right">35.9%</td>
<td align="right">75,425,100</td>
<td align="right">35.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,426,571</td>
<td align="right">35.9%</td>
<td align="right">75,425,885</td>
<td align="right">35.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,895,373</td>
<td align="right">37.6%</td>
<td align="right">78,894,912</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,895,373</td>
<td align="right">37.6%</td>
<td align="right">78,894,912</td>
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
<td align="right">2,515,602</td>
<td align="right"></td>
<td align="right">2,437,671</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,356,014</td>
<td align="right"></td>
<td align="right">4,271,786</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">756,920</td>
<td align="right">0.2%</td>
<td align="right">763,233</td>
<td align="right">0.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,429,988</td>
<td align="right">1.3%</td>
<td align="right">51,852,480</td>
<td align="right">1.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">149,170,113</td>
<td align="right"></td>
<td align="right">149,692,275</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,841,901</td>
<td align="right"></td>
<td align="right">1,835,778</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,537,533,579</td>
<td align="right">37.8%</td>
<td align="right">1,540,437,418</td>
<td align="right">37.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,214,311,536</td>
<td align="right">34.3%</td>
<td align="right">1,216,494,318</td>
<td align="right">34.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">972,123,589</td>
<td align="right">27.4%</td>
<td align="right">973,847,714</td>
<td align="right">27.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,083,789,854</td>
<td align="right">26.6%</td>
<td align="right">1,084,616,860</td>
<td align="right">26.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,395,454,344</td>
<td align="right">34.3%</td>
<td align="right">1,394,542,590</td>
<td align="right">34.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,177,395</td>
<td align="right">25.9%</td>
<td align="right">129,241,327</td>
<td align="right">25.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,816,324</td>
<td align="right"></td>
<td align="right">141,880,480</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,411,627</td>
<td align="right">25.7%</td>
<td align="right">128,469,246</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">76,051,715</td>
<td align="right">2.1%</td>
<td align="right">76,080,820</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,354,457</td>
<td align="right"></td>
<td align="right">248,446,327</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,279,123,859</td>
<td align="right">36.1%</td>
<td align="right">1,278,829,543</td>
<td align="right">36.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,301</td>
<td align="right"></td>
<td align="right">866,412</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">370,514,792</td>
<td align="right">74.1%</td>
<td align="right">370,562,044</td>
<td align="right">74.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">370,549,580</td>
<td align="right"></td>
<td align="right">370,596,825</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">135</td>
<td align="right">0.7%</td>
<td align="right">17.4%</td>
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
<td align="right">5,973</td>
<td align="right">31.6%</td>
<td align="right">2.0%</td>
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
<td align="right">150</td>
<td align="right">0.8%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,867</td>
<td align="right">9.9%</td>
<td align="right">1.1%</td>
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
<td align="right">18,919</td>
<td align="right"></td>
<td align="right">1.0%</td>
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
<td align="right">1,862</td>
<td align="right">9.8%</td>
<td align="right">-0.9%</td>
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
<td align="right">9,217</td>
<td align="right">48.7%</td>
<td align="right">0.9%</td>
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
<td align="right">1,664,133,444</td>
<td align="right">3,368.9%</td>
<td align="right">0.7%</td>
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
<td align="right">49,397,055</td>
<td align="right"></td>
<td align="right">-0.3%</td>
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
<td align="right">1,702</td>
<td align="right">91.4%</td>
<td align="right">-6.3%</td>
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
<td align="right">1,862</td>
<td align="right"></td>
<td align="right">-0.9%</td>
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
<td align="right">12,775,424</td>
<td align="right">77.2%</td>
<td align="right">-15.0%</td>
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
<td align="right">12,563,088</td>
<td align="right">75.9%</td>
<td align="right">-12.5%</td>
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
<td align="right">16,551,936</td>
<td align="right"></td>
<td align="right">-11.3%</td>
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
<td align="right">383,040</td>
<td align="right">2.3%</td>
<td align="right">-10.0%</td>
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
<td align="right">3,605,808</td>
<td align="right">21.8%</td>
<td align="right">-7.2%</td>
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
<td align="left">401</td>
<td align="right">23.6%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">707</td>
<td align="right">38.9%</td>
<td align="left">825</td>
<td align="right">48.5%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">533</td>
<td align="right">29.4%</td>
<td align="left">304</td>
<td align="right">17.9%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">172</td>
<td align="right">9.5%</td>
<td align="left">151</td>
<td align="right">8.9%</td>
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
<td align="right">76</td>
<td align="right">4.1%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">117</td>
<td align="right">6.2%</td>
<td align="right">228</td>
<td align="right">12.2%</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">400</td>
<td align="right">21.3%</td>
<td align="right">396</td>
<td align="right">21.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">908</td>
<td align="right">48.3%</td>
<td align="right">775</td>
<td align="right">41.6%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">321</td>
<td align="right">17.1%</td>
<td align="right">321</td>
<td align="right">17.2%</td>
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
<td align="right">76</td>
<td align="right">4.1%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">111</td>
<td align="right">6.0%</td>
<td align="right">111 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">252</td>
<td align="right">13.4%</td>
<td align="right">210</td>
<td align="right">11.3%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">855</td>
<td align="right">45.5%</td>
<td align="right">748</td>
<td align="right">40.2%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">362</td>
<td align="right">19.3%</td>
<td align="right">277</td>
<td align="right">14.9%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">259</td>
<td align="right">13.8%</td>
<td align="right">259</td>
<td align="right">13.9%</td>
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
<td align="right">1,052</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">15,523,189</td>
<td align="right">2,159,226</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">3,954,835</td>
<td align="right">5,525,758</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,030,722</td>
<td align="right">1,437,881</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">6,158,597</td>
<td align="right">4,490,574</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,303</td>
<td align="right">1,052</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">317,151</td>
<td align="right">376,272</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,114,288</td>
<td align="right">1,761,394</td>
<td align="right">-16.7%</td>
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
<td align="right">21,231,236</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">7,700</td>
<td align="right">7,200</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,105,006</td>
<td align="right">1,164,127</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,609,443</td>
<td align="right">1,689,604</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,686,386</td>
<td align="right">1,766,547</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">300,008,492</td>
<td align="right">313,262,088</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">330,948,757</td>
<td align="right">344,817,324</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,254,240</td>
<td align="right">1,211,819</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,254,240</td>
<td align="right">1,211,819</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,254,240</td>
<td align="right">1,211,819</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,129,106</td>
<td align="right">3,025,296</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,145,005</td>
<td align="right">3,041,195</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,251,316</td>
<td align="right">3,147,506</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">14,062,759</td>
<td align="right">13,661,750</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,210,021</td>
<td align="right">5,079,495</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">4,991,554</td>
<td align="right">5,109,317</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,361,599</td>
<td align="right">12,640,709</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">5,530,870</td>
<td align="right">5,655,129</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">12,056,186</td>
<td align="right">12,318,768</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,056,186</td>
<td align="right">12,318,768</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,936,089</td>
<td align="right">6,788,656</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">10,050,636</td>
<td align="right">10,253,671</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,290,523</td>
<td align="right">8,446,708</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,986,870</td>
<td align="right">4,061,452</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">4,991,554</td>
<td align="right">5,061,563</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,064,675</td>
<td align="right">3,022,256</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,685,373</td>
<td align="right">4,744,493</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,231,154</td>
<td align="right">6,305,736</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,054,133</td>
<td align="right">6,124,142</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,495,946</td>
<td align="right">6,565,959</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,910,582</td>
<td align="right">10,004,908</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,608,946</td>
<td align="right">7,678,956</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">30,981,432</td>
<td align="right">31,247,967</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">39,846,337</td>
<td align="right">40,135,186</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,826,521</td>
<td align="right">10,896,510</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">35,838,942</td>
<td align="right">36,008,762</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,161,272</td>
<td align="right">26,057,061</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">80,149,142</td>
<td align="right">80,410,071</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">49,557,742</td>
<td align="right">49,397,055</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">49,557,742</td>
<td align="right">49,397,055</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">26,084,209</td>
<td align="right">26,157,413</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">26,806,130</td>
<td align="right">26,879,335</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">26,806,130</td>
<td align="right">26,879,335</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,914,229</td>
<td align="right">17,949,181</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">89,404,079</td>
<td align="right">89,532,241</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,974,084</td>
<td align="right">5,980,101</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,415,044</td>
<td align="right">24,429,503</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">8,563</td>
<td align="right">8,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,646</td>
<td align="right">2,514,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">31,049,462</td>
<td align="right">31,054,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,350,610</td>
<td align="right">3,351,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,803,327</td>
<td align="right">15,801,550</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,037,141</td>
<td align="right">5,036,617</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,716,373</td>
<td align="right">11,717,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,499,414</td>
<td align="right">6,499,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,382,856</td>
<td align="right">7,383,231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">32,550,141</td>
<td align="right">32,548,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">26,096,249</td>
<td align="right">26,096,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">26,096,249</td>
<td align="right">26,096,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">22,416,832</td>
<td align="right">22,417,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,398,793</td>
<td align="right">13,398,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,437,892</td>
<td align="right">1,437,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,567,856</td>
<td align="right">1,567,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,567,856</td>
<td align="right">1,567,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,279,125</td>
<td align="right">2,279,113</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,209,506</td>
<td align="right">2,209,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,763,663</td>
<td align="right">1,763,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,763,663</td>
<td align="right">1,763,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,449,407</td>
<td align="right">2,449,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,125,157</td>
<td align="right">2,125,156</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,231,521</td>
<td align="right">3,231,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,398,793</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,340,642</td>
<td align="right">3,340,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,125,158</td>
<td align="right">2,125,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,849,482</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,828,631</td>
<td align="right">1,828,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,072,552</td>
<td align="right">1,072,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,062,579</td>
<td align="right">1,062,579</td>
<td align="right">0.0%</td>
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
<td align="right">13,398,915</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">1,523,169</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">47,754</td>
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
<td align="right">1,480</td>
<td align="right">1,493</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">567</td>
<td align="right">565</td>
<td align="right">-0.4%</td>
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
Stats gathered on: 2025-04-24
