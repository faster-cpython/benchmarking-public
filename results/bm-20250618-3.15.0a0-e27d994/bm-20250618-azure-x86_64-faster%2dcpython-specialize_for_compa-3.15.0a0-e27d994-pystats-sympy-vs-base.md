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
<td align="right">9,038</td>
<td align="right">8,986</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,938,573</td>
<td align="right">18,026,869</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,681,141</td>
<td align="right">17,764,070</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,082,233</td>
<td align="right">19,165,340</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">996</td>
<td align="right">999</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,621,556</td>
<td align="right">35,726,093</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,438,272</td>
<td align="right">9,461,597</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,220,468</td>
<td align="right">1,223,208</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">45,118,069</td>
<td align="right">45,212,794</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60,584,325</td>
<td align="right">60,706,487</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,253,480</td>
<td align="right">53,360,029</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,965</td>
<td align="right">2,960</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,742,007</td>
<td align="right">81,874,379</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,232,577</td>
<td align="right">82,365,148</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,742,529</td>
<td align="right">83,875,427</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,915,513</td>
<td align="right">7,927,330</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,079,219</td>
<td align="right">8,091,072</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">135,220,711</td>
<td align="right">135,412,610</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,383,294</td>
<td align="right">17,407,818</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">41,233</td>
<td align="right">41,182</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,733,003</td>
<td align="right">45,787,667</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,002,664</td>
<td align="right">11,014,468</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,091,651</td>
<td align="right">11,103,533</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,610,040</td>
<td align="right">11,621,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,444,609</td>
<td align="right">30,474,165</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,427,672</td>
<td align="right">12,439,512</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,109</td>
<td align="right">7,115</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,443</td>
<td align="right">1,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,833,248</td>
<td align="right">52,869,375</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,971,805</td>
<td align="right">5,975,823</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">149,944,406</td>
<td align="right">150,038,873</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,369,298</td>
<td align="right">23,383,674</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">232,557,229</td>
<td align="right">232,699,344</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,067</td>
<td align="right">18,078</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">192,472,089</td>
<td align="right">192,586,883</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,178,208</td>
<td align="right">199,286,429</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,630,485</td>
<td align="right">36,649,068</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,735,130</td>
<td align="right">24,747,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,826,843</td>
<td align="right">44,846,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,688</td>
<td align="right">20,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">679,047,670</td>
<td align="right">679,295,449</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">44,466,576</td>
<td align="right">44,482,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">47,033,888</td>
<td align="right">47,049,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,691</td>
<td align="right">744,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">149,428,538</td>
<td align="right">149,475,828</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">46,445,089</td>
<td align="right">46,458,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,199,392</td>
<td align="right">2,199,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,349</td>
<td align="right">175,303</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,577</td>
<td align="right">165,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,132</td>
<td align="right">83,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,824</td>
<td align="right">461,732</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,100,875</td>
<td align="right">40,093,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">494,972</td>
<td align="right">495,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,384,545</td>
<td align="right">72,397,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,485,034</td>
<td align="right">48,493,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,559</td>
<td align="right">2,007,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">79,551</td>
<td align="right">79,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,985,877</td>
<td align="right">15,988,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,992,015</td>
<td align="right">9,993,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,951,442</td>
<td align="right">80,963,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,978,534</td>
<td align="right">8,979,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,832,568</td>
<td align="right">181,857,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,798</td>
<td align="right">23,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,287,751</td>
<td align="right">1,287,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,158,054</td>
<td align="right">27,155,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,895</td>
<td align="right">389,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">15,009,202</td>
<td align="right">15,007,842</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,950,879</td>
<td align="right">71,956,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,159</td>
<td align="right">1,029,081</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,030,050</td>
<td align="right">1,029,972</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,630,342</td>
<td align="right">18,631,696</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,355</td>
<td align="right">2,585,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,994,843</td>
<td align="right">2,995,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,601,799</td>
<td align="right">178,613,249</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,090</td>
<td align="right">1,811,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,412,203</td>
<td align="right">46,409,361</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,130,701</td>
<td align="right">23,132,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">273,566,749</td>
<td align="right">273,582,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,318</td>
<td align="right">6,026,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,312</td>
<td align="right">746,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,616,684</td>
<td align="right">2,616,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,831,328</td>
<td align="right">6,831,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,200</td>
<td align="right">4,469,389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,697,677</td>
<td align="right">21,696,825</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,440,571</td>
<td align="right">35,441,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,299,427</td>
<td align="right">49,301,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,539</td>
<td align="right">427,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,052</td>
<td align="right">172,047</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,741,142</td>
<td align="right">15,741,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,644</td>
<td align="right">2,008,698</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,574,000</td>
<td align="right">75,575,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,035,197</td>
<td align="right">4,035,104</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,282</td>
<td align="right">5,753,169</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,329,745</td>
<td align="right">3,329,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,376</td>
<td align="right">655,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,376</td>
<td align="right">655,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,376</td>
<td align="right">655,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,242,033</td>
<td align="right">6,241,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,857</td>
<td align="right">6,589,737</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,387</td>
<td align="right">17,449,129</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,496</td>
<td align="right">654,505</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,512</td>
<td align="right">654,521</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,350</td>
<td align="right">6,744,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,422,076</td>
<td align="right">23,422,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,077,112</td>
<td align="right">19,077,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,773</td>
<td align="right">1,389,756</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,709,286</td>
<td align="right">12,709,141</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,570</td>
<td align="right">2,281,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,516</td>
<td align="right">7,541,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,601,775</td>
<td align="right">18,601,592</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,920,900</td>
<td align="right">10,920,793</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,671</td>
<td align="right">942,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,555</td>
<td align="right">21,977,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,945,639</td>
<td align="right">16,945,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,231,595</td>
<td align="right">26,231,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,612,955</td>
<td align="right">4,612,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,709</td>
<td align="right">4,181,743</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,678</td>
<td align="right">4,001,648</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,401</td>
<td align="right">141,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,115,136</td>
<td align="right">52,114,797</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,709</td>
<td align="right">4,497,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,163,868</td>
<td align="right">13,163,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,100,073</td>
<td align="right">113,100,597</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,314,187</td>
<td align="right">18,314,104</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,537</td>
<td align="right">1,244,532</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,768</td>
<td align="right">21,985,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,835</td>
<td align="right">6,622,811</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,147,026</td>
<td align="right">33,146,911</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,319</td>
<td align="right">6,787,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,314</td>
<td align="right">1,323,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,873,705</td>
<td align="right">10,873,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,800,140</td>
<td align="right">70,799,992</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,017,016</td>
<td align="right">16,017,035</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,531</td>
<td align="right">1,754,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,816</td>
<td align="right">9,777,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,736,994</td>
<td align="right">78,736,964</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,483</td>
<td align="right">26,730,489</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,996</td>
<td align="right">745,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,537</td>
<td align="right">598,537</td>
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
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="right">396,470</td>
<td align="right">0.3%</td>
<td align="right">437,392</td>
<td align="right">0.4%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,701,810</td>
<td align="right">39.1%</td>
<td align="right">45,756,468</td>
<td align="right">39.1%</td>
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
<td align="right">70,867,616</td>
<td align="right">60.6%</td>
<td align="right">70,899,030</td>
<td align="right">60.5%</td>
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
<td align="right">9,560</td>
<td align="right">24.7%</td>
<td align="right">10,352</td>
<td align="right">26.3%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">29,068</td>
<td align="right">75.3%</td>
<td align="right">29,073</td>
<td align="right">73.7%</td>
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
<td align="left">subscr</td>
<td align="right">4,561</td>
<td align="right">15.7%</td>
<td align="right">4,585</td>
<td align="right">15.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,764</td>
<td align="right">6.1%</td>
<td align="right">1,755</td>
<td align="right">6.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">0.7%</td>
<td align="right">212</td>
<td align="right">0.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,209</td>
<td align="right">4.2%</td>
<td align="right">1,214</td>
<td align="right">4.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,003</td>
<td align="right">3.5%</td>
<td align="right">1,000</td>
<td align="right">3.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">705</td>
<td align="right">2.4%</td>
<td align="right">703</td>
<td align="right">2.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">566</td>
<td align="right">1.9%</td>
<td align="right">565</td>
<td align="right">1.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,901</td>
<td align="right">10.0%</td>
<td align="right">2,896</td>
<td align="right">10.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,884</td>
<td align="right">13.4%</td>
<td align="right">3,881</td>
<td align="right">13.3%</td>
<td align="right">-0.1%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,353</td>
<td align="right">8.1%</td>
<td align="right">2,353</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
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
<td align="right">738</td>
<td align="right">2.5%</td>
<td align="right">738</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">625</td>
<td align="right">2.2%</td>
<td align="right">625</td>
<td align="right">2.1%</td>
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
<td align="right">36,499,509</td>
<td align="right">11.7%</td>
<td align="right">36,583,416</td>
<td align="right">11.7%</td>
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
<td align="right">35,819,364</td>
<td align="right">11.4%</td>
<td align="right">35,901,689</td>
<td align="right">11.5%</td>
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
<td align="right">276,364,092</td>
<td align="right">88.3%</td>
<td align="right">276,407,576</td>
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
<td align="right">703,943</td>
<td align="right">100.0%</td>
<td align="right">705,528</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">1,065</td>
<td align="right">100.0%</td>
<td align="right">1,064</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">412,636</td>
<td align="right">0.5%</td>
<td align="right">409,615</td>
<td align="right">0.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,405,903</td>
<td align="right">37.1%</td>
<td align="right">30,435,581</td>
<td align="right">37.2%</td>
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
<td align="right">51,036,678</td>
<td align="right">62.3%</td>
<td align="right">51,032,345</td>
<td align="right">62.3%</td>
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
<td align="right">8,890</td>
<td align="right">19.1%</td>
<td align="right">8,829</td>
<td align="right">19.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,545</td>
<td align="right">80.9%</td>
<td align="right">37,428</td>
<td align="right">80.9%</td>
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
<td align="left">set</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">134</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,254</td>
<td align="right">11.3%</td>
<td align="right">4,218</td>
<td align="right">11.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,204</td>
<td align="right">37.8%</td>
<td align="right">14,117</td>
<td align="right">37.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,474</td>
<td align="right">17.2%</td>
<td align="right">6,486</td>
<td align="right">17.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,155</td>
<td align="right">8.4%</td>
<td align="right">3,151</td>
<td align="right">8.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">19.9%</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,455</td>
<td align="right">3.9%</td>
<td align="right">1,455</td>
<td align="right">3.9%</td>
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
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">114</td>
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
<td align="right">17,376,186</td>
<td align="right">42.5%</td>
<td align="right">17,400,705</td>
<td align="right">42.5%</td>
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
<td align="right">23,500,607</td>
<td align="right">57.5%</td>
<td align="right">23,500,906</td>
<td align="right">57.4%</td>
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
<td align="right">6,983</td>
<td align="right">98.2%</td>
<td align="right">6,988</td>
<td align="right">98.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">125</td>
<td align="right">1.8%</td>
<td align="right">125</td>
<td align="right">1.8%</td>
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
<td align="left">tuple</td>
<td align="right">1,469</td>
<td align="right">21.0%</td>
<td align="right">1,471</td>
<td align="right">21.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,033</td>
<td align="right">72.1%</td>
<td align="right">5,036</td>
<td align="right">72.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">2.6%</td>
<td align="right">182</td>
<td align="right">2.6%</td>
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
<td align="right">81,680,001</td>
<td align="right">44.0%</td>
<td align="right">81,812,488</td>
<td align="right">44.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,600</td>
<td align="right">0.7%</td>
<td align="right">1,264,057</td>
<td align="right">0.7%</td>
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
<td align="right">102,441,255</td>
<td align="right">55.2%</td>
<td align="right">102,529,553</td>
<td align="right">55.2%</td>
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
<td align="right">61,212</td>
<td align="right">71.4%</td>
<td align="right">61,099</td>
<td align="right">71.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,531</td>
<td align="right">28.6%</td>
<td align="right">24,561</td>
<td align="right">28.7%</td>
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
<td align="left">dict items</td>
<td align="right">47,042</td>
<td align="right">76.9%</td>
<td align="right">46,912</td>
<td align="right">76.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,359</td>
<td align="right">10.4%</td>
<td align="right">6,374</td>
<td align="right">10.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,359</td>
<td align="right">2.2%</td>
<td align="right">1,361</td>
<td align="right">2.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,200</td>
<td align="right">6.9%</td>
<td align="right">4,200</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.2%</td>
<td align="right">758</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">194</td>
<td align="right">0.3%</td>
<td align="right">194</td>
<td align="right">0.3%</td>
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
<td align="right">0.0%</td>
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
<td align="left">set</td>
<td align="right">7,171,643</td>
<td align="right">7,171,643 / 0 !!</td>
<td align="right">7,187,428</td>
<td align="right">7,187,428 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,488</td>
<td align="right">70,488 / 0 !!</td>
<td align="right">70,538</td>
<td align="right">70,538 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">157,971</td>
<td align="right">157,971 / 0 !!</td>
<td align="right">157,940</td>
<td align="right">157,940 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,233,924</td>
<td align="right">9,233,924 / 0 !!</td>
<td align="right">9,234,016</td>
<td align="right">9,234,016 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,236,550</td>
<td align="right">12,236,550 / 0 !!</td>
<td align="right">12,236,666</td>
<td align="right">12,236,666 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,716,222</td>
<td align="right">8,716,222 / 0 !!</td>
<td align="right">8,716,177</td>
<td align="right">8,716,177 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,619</td>
<td align="right">9,440,619 / 0 !!</td>
<td align="right">9,440,604</td>
<td align="right">9,440,604 / 0 !!</td>
<td align="right">-0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">223,160,442</td>
<td align="right">64.3%</td>
<td align="right">223,272,009</td>
<td align="right">64.3%</td>
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
<td align="right">53,244,512</td>
<td align="right">15.3%</td>
<td align="right">53,244,927</td>
<td align="right">15.3%</td>
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
<td align="right">70,737,224</td>
<td align="right">20.4%</td>
<td align="right">70,737,096</td>
<td align="right">20.4%</td>
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
<td align="right">47,748</td>
<td align="right">4.5%</td>
<td align="right">47,710</td>
<td align="right">4.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,015,399</td>
<td align="right">95.5%</td>
<td align="right">1,015,411</td>
<td align="right">95.5%</td>
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
<td align="left">method</td>
<td align="right">2,741</td>
<td align="right">5.7%</td>
<td align="right">2,735</td>
<td align="right">5.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,067</td>
<td align="right">8.5%</td>
<td align="right">4,060</td>
<td align="right">8.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,353</td>
<td align="right">9.1%</td>
<td align="right">4,347</td>
<td align="right">9.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,868</td>
<td align="right">45.8%</td>
<td align="right">21,849</td>
<td align="right">45.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,099</td>
<td align="right">6.5%</td>
<td align="right">3,101</td>
<td align="right">6.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,093</td>
<td align="right">14.9%</td>
<td align="right">7,093</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,684</td>
<td align="right">5.6%</td>
<td align="right">2,684</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">566</td>
<td align="right">1.2%</td>
<td align="right">566</td>
<td align="right">1.2%</td>
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
<td align="right">4,535</td>
<td align="right">0.0%</td>
<td align="right">4,538</td>
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
<td align="right">291,700,573</td>
<td align="right">100.0%</td>
<td align="right">291,712,547</td>
<td align="right">100.0%</td>
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
<td align="right">13,582</td>
<td align="right">100.0%</td>
<td align="right">13,590</td>
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
<td align="right">2,265,985</td>
<td align="right">100.0%</td>
<td align="right">2,265,980</td>
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
<td align="right">731,644</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,576,753</td>
<td align="right">17.4%</td>
<td align="right">1,575,511</td>
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
<td align="right">174,041</td>
<td align="right">1.9%</td>
<td align="right">174,002</td>
<td align="right">1.9%</td>
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
<td align="right">7,327,652</td>
<td align="right">80.7%</td>
<td align="right">7,328,893</td>
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
<td align="right">972</td>
<td align="right">3.1%</td>
<td align="right">965</td>
<td align="right">3.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,007</td>
<td align="right">96.9%</td>
<td align="right">29,981</td>
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
<td align="right">296</td>
<td align="right">30.5%</td>
<td align="right">290</td>
<td align="right">30.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">518</td>
<td align="right">53.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,408</td>
<td align="right">87.3%</td>
<td align="right">17,742,944</td>
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
<td align="right">2,583,236</td>
<td align="right">12.7%</td>
<td align="right">2,583,421</td>
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
<td align="right">169,481,194</td>
<td align="right">94.2%</td>
<td align="right">169,576,358</td>
<td align="right">94.2%</td>
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
<td align="right">623,465</td>
<td align="right">0.3%</td>
<td align="right">623,585</td>
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
<td align="right">9,755,773</td>
<td align="right">5.4%</td>
<td align="right">9,755,786</td>
<td align="right">5.4%</td>
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
<td align="right">14,286</td>
<td align="right">43.0%</td>
<td align="right">14,276</td>
<td align="right">42.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,964</td>
<td align="right">57.0%</td>
<td align="right">18,965</td>
<td align="right">57.1%</td>
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
<td align="left">set</td>
<td align="right">721</td>
<td align="right">5.0%</td>
<td align="right">714</td>
<td align="right">5.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,263</td>
<td align="right">8.8%</td>
<td align="right">1,269</td>
<td align="right">8.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">723</td>
<td align="right">5.1%</td>
<td align="right">721</td>
<td align="right">5.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,613</td>
<td align="right">18.3%</td>
<td align="right">2,620</td>
<td align="right">18.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,997</td>
<td align="right">56.0%</td>
<td align="right">7,983</td>
<td align="right">55.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">6,348</td>
<td align="right">0.0%</td>
<td align="right">6,300</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,661,729</td>
<td align="right">100.0%</td>
<td align="right">83,794,450</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">299</td>
<td align="right">11.1%</td>
<td align="right">295</td>
<td align="right">11.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,391</td>
<td align="right">88.9%</td>
<td align="right">2,391</td>
<td align="right">89.0%</td>
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
<td align="right">256</td>
<td align="right">85.6%</td>
<td align="right">252</td>
<td align="right">85.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.4%</td>
<td align="right">43</td>
<td align="right">14.6%</td>
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
<td align="right">94,035,780</td>
<td align="right">2.0%</td>
<td align="right">94,158,338</td>
<td align="right">2.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">306,010,591</td>
<td align="right">6.4%</td>
<td align="right">306,267,615</td>
<td align="right">6.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,756,660,654</td>
<td align="right">57.4%</td>
<td align="right">2,757,998,536</td>
<td align="right">57.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,642,471,176</td>
<td align="right">34.2%</td>
<td align="right">1,643,228,843</td>
<td align="right">34.2%</td>
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
<td align="left">CALL</td>
<td align="right">35,819,364</td>
<td align="right">12.2%</td>
<td align="right">35,901,689</td>
<td align="right">12.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,680,001</td>
<td align="right">27.7%</td>
<td align="right">81,812,488</td>
<td align="right">27.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,376,186</td>
<td align="right">5.9%</td>
<td align="right">17,400,705</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,701,810</td>
<td align="right">15.5%</td>
<td align="right">45,756,468</td>
<td align="right">15.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,405,903</td>
<td align="right">10.3%</td>
<td align="right">30,435,581</td>
<td align="right">10.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,041</td>
<td align="right">0.1%</td>
<td align="right">174,002</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,236</td>
<td align="right">0.9%</td>
<td align="right">2,583,421</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,737,224</td>
<td align="right">24.0%</td>
<td align="right">70,737,096</td>
<td align="right">24.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,773</td>
<td align="right">3.3%</td>
<td align="right">9,755,786</td>
<td align="right">3.3%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,330,381</td>
<td align="right">12.0%</td>
<td align="right">11,414,808</td>
<td align="right">12.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,575,974</td>
<td align="right">1.7%</td>
<td align="right">1,574,732</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,204,185</td>
<td align="right">3.4%</td>
<td align="right">3,203,623</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,150,788</td>
<td align="right">6.5%</td>
<td align="right">6,151,522</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,289,672</td>
<td align="right">14.1%</td>
<td align="right">13,288,100</td>
<td align="right">14.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,702,810</td>
<td align="right">12.4%</td>
<td align="right">11,701,496</td>
<td align="right">12.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,479</td>
<td align="right">7.8%</td>
<td align="right">7,312,745</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,566</td>
<td align="right">5.4%</td>
<td align="right">5,102,642</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,022,244</td>
<td align="right">30.9%</td>
<td align="right">29,022,558</td>
<td align="right">30.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,582</td>
<td align="right">2.2%</td>
<td align="right">2,103,594</td>
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
<td align="right">131,381,415</td>
<td align="right">62.5%</td>
<td align="right">131,501,543</td>
<td align="right">62.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,636,187</td>
<td align="right">89.2%</td>
<td align="right">187,673,202</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,354</td>
<td align="right">0.5%</td>
<td align="right">950,411</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,946</td>
<td align="right">1.6%</td>
<td align="right">3,468,888</td>
<td align="right">1.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,149</td>
<td align="right">4.4%</td>
<td align="right">9,332,060</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,137,433</td>
<td align="right">19.6%</td>
<td align="right">41,137,580</td>
<td align="right">19.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,737</td>
<td align="right">8.8%</td>
<td align="right">18,490,728</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,891,409</td>
<td align="right">37.5%</td>
<td align="right">78,891,379</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,891,409</td>
<td align="right">37.5%</td>
<td align="right">78,891,379</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,421,678</td>
<td align="right">35.9%</td>
<td align="right">75,421,706</td>
<td align="right">35.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,422,463</td>
<td align="right">35.9%</td>
<td align="right">75,422,491</td>
<td align="right">35.8%</td>
<td align="right">0.0%</td>
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
<td align="right">1,403,312</td>
<td align="right"></td>
<td align="right">1,566,446</td>
<td align="right"></td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,753,828</td>
<td align="right"></td>
<td align="right">3,919,221</td>
<td align="right"></td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">760,111</td>
<td align="right">0.2%</td>
<td align="right">761,364</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,360,798</td>
<td align="right">1.3%</td>
<td align="right">51,422,492</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,352,090</td>
<td align="right"></td>
<td align="right">2,354,289</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,803,859</td>
<td align="right"></td>
<td align="right">248,663,869</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">970,291,526</td>
<td align="right">28.3%</td>
<td align="right">970,786,353</td>
<td align="right">28.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,600,782,275</td>
<td align="right">40.9%</td>
<td align="right">1,601,450,664</td>
<td align="right">40.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,283,213,812</td>
<td align="right">37.4%</td>
<td align="right">1,283,713,702</td>
<td align="right">37.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,100,015,765</td>
<td align="right">32.0%</td>
<td align="right">1,100,442,892</td>
<td align="right">32.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,054,003</td>
<td align="right">26.8%</td>
<td align="right">129,094,430</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">79,078,912</td>
<td align="right">2.3%</td>
<td align="right">79,103,556</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,284,961</td>
<td align="right">26.6%</td>
<td align="right">128,324,135</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,708,921</td>
<td align="right"></td>
<td align="right">141,749,459</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,055,627,798</td>
<td align="right">27.0%</td>
<td align="right">1,055,924,312</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,203,867,984</td>
<td align="right">30.8%</td>
<td align="right">1,204,189,836</td>
<td align="right">30.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">352,495,146</td>
<td align="right">73.2%</td>
<td align="right">352,519,039</td>
<td align="right">73.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">352,530,335</td>
<td align="right"></td>
<td align="right">352,554,221</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,373</td>
<td align="right"></td>
<td align="right">866,343</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">150,452,763</td>
<td align="right"></td>
<td align="right">150,449,469</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,931</td>
<td align="right">0.0%</td>
<td align="right">8,931</td>
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
