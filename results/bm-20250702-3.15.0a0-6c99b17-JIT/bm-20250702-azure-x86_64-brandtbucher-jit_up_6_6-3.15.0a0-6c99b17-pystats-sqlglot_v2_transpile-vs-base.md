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
<td align="left">BINARY_OP</td>
<td align="right">91,354</td>
<td align="right">5,138</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">135,114</td>
<td align="right">8,766</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">124,824</td>
<td align="right">8,640</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">860,055</td>
<td align="right">88,599</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">3,070,560</td>
<td align="right">337,226</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,621,199</td>
<td align="right">329,359</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">620,985</td>
<td align="right">92,201</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,207,498</td>
<td align="right">525,379</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,144,980</td>
<td align="right">823,411</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,070,425</td>
<td align="right">226,853</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">911,169</td>
<td align="right">228,253</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,411,112</td>
<td align="right">1,419,224</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,828,845</td>
<td align="right">1,333,324</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">16,190,587</td>
<td align="right">4,528,619</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,959,717</td>
<td align="right">1,399,341</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,332,520</td>
<td align="right">683,844</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,472,781</td>
<td align="right">751,830</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,931,977</td>
<td align="right">908,620</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,558,944</td>
<td align="right">794,985</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,973,243</td>
<td align="right">945,548</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,267,747</td>
<td align="right">1,360,836</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,701,748</td>
<td align="right">1,504,963</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,143</td>
<td align="right">1,370</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,688,115</td>
<td align="right">1,643,938</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,318,098</td>
<td align="right">472,175</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">357,446</td>
<td align="right">130,243</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">60,554,624</td>
<td align="right">22,198,077</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,015,962</td>
<td align="right">2,624,103</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,704,743</td>
<td align="right">1,784,823</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,307,463</td>
<td align="right">6,586,072</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,013,376</td>
<td align="right">392,332</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,527,504</td>
<td align="right">595,494</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">140,478,302</td>
<td align="right">54,903,144</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">6,061,671</td>
<td align="right">2,373,682</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,584,749</td>
<td align="right">3,377,036</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,779,117</td>
<td align="right">4,945,239</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,539,564</td>
<td align="right">2,764,757</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,514,168</td>
<td align="right">1,063,129</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,973,039</td>
<td align="right">1,273,847</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">24,906,742</td>
<td align="right">10,673,575</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">36,651,058</td>
<td align="right">15,845,599</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">541,569</td>
<td align="right">234,471</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,706,948</td>
<td align="right">1,178,401</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">184,149</td>
<td align="right">80,316</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,213,538</td>
<td align="right">969,255</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,726,907</td>
<td align="right">8,682,804</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">752,745</td>
<td align="right">334,858</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,609</td>
<td align="right">10,954</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,076,222</td>
<td align="right">5,857,352</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">634,662</td>
<td align="right">290,664</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">4,607,195</td>
<td align="right">2,116,737</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,068,133</td>
<td align="right">6,039,236</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,772,181</td>
<td align="right">3,617,313</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">237,411</td>
<td align="right">110,900</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">22,934,046</td>
<td align="right">10,846,911</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,345,289</td>
<td align="right">4,425,384</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">809,619</td>
<td align="right">383,624</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,077,963</td>
<td align="right">14,738,841</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,539,012</td>
<td align="right">1,679,437</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,606,869</td>
<td align="right">15,023,135</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,868,475</td>
<td align="right">6,623,181</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,745,613</td>
<td align="right">2,269,222</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,279,817</td>
<td align="right">613,259</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,427,571</td>
<td align="right">5,058,859</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,469,768</td>
<td align="right">1,202,295</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,181,616</td>
<td align="right">8,859,627</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">777,231</td>
<td align="right">380,018</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,510,269</td>
<td align="right">749,055</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">511,119</td>
<td align="right">253,755</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,071</td>
<td align="right">2,023</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,074</td>
<td align="right">2,026</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,074</td>
<td align="right">2,026</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">335,859</td>
<td align="right">167,356</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">450,450</td>
<td align="right">224,487</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,169</td>
<td align="right">4,073</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">548,730</td>
<td align="right">273,615</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">920,672</td>
<td align="right">459,083</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">53,130</td>
<td align="right">26,506</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,558,408</td>
<td align="right">1,775,484</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">28,623</td>
<td align="right">14,287</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">49,098</td>
<td align="right">24,522</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">81,837</td>
<td align="right">40,877</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">24,555</td>
<td align="right">12,266</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">32,739</td>
<td align="right">16,355</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,313,366</td>
<td align="right">1,655,294</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">261,933</td>
<td align="right">130,861</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">114,597</td>
<td align="right">57,253</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">630,441</td>
<td align="right">315,049</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,838,340</td>
<td align="right">918,788</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,281,609</td>
<td align="right">640,539</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,740,483</td>
<td align="right">869,954</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">565,089</td>
<td align="right">282,465</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">565,089</td>
<td align="right">282,465</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">565,089</td>
<td align="right">282,465</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">714,403</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,388,205</td>
<td align="right">693,933</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">937,755</td>
<td align="right">468,763</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">401,310</td>
<td align="right">200,606</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">200,655</td>
<td align="right">100,303</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">118,755</td>
<td align="right">59,363</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">45,045</td>
<td align="right">22,517</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">45,045</td>
<td align="right">22,517</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">45,045</td>
<td align="right">22,517</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">32,760</td>
<td align="right">16,376</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,665</td>
<td align="right">14,329</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,570</td>
<td align="right">12,282</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,570</td>
<td align="right">12,282</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">12,285</td>
<td align="right">6,141</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">8,190</td>
<td align="right">4,094</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">4,095</td>
<td align="right">2,047</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4,095</td>
<td align="right">2,047</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,095</td>
<td align="right">2,047</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,095</td>
<td align="right">2,047</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,227,818</td>
<td align="right">1,113,704</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,801,622</td>
<td align="right">1,400,591</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,431,210</td>
<td align="right">2,215,274</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">700,314</td>
<td align="right">350,105</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">462,873</td>
<td align="right">231,447</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">192,534</td>
<td align="right">96,277</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">69,684</td>
<td align="right">34,867</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">65,589</td>
<td align="right">32,820</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,829</td>
<td align="right">16,444</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">20,544</td>
<td align="right">10,303</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">12,354</td>
<td align="right">6,209</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,138</td>
<td align="right">24,762</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,164</td>
<td align="right">2,115</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,802</td>
<td align="right">19,328</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">11,429</td>
<td align="right">6,186</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">83,399</td>
<td align="right">46,471</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">48</td>
<td align="right">47</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">18,816</td>
<td align="right">18,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,576</td>
<td align="right">9,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,801</td>
<td align="right">3,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,247</td>
<td align="right">2,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,806</td>
<td align="right">1,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,008</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">90,303</td>
<td align="right">0.2%</td>
<td align="right">4,192</td>
<td align="right">0.0%</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,374,960</td>
<td align="right">99.7%</td>
<td align="right">18,182,576</td>
<td align="right">99.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,565</td>
<td align="right">0.0%</td>
<td align="right">6,293</td>
<td align="right">0.0%</td>
<td align="right">-49.9%</td>
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
<td align="right">232</td>
<td align="right">18.1%</td>
<td align="right">127</td>
<td align="right">12.1%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,053</td>
<td align="right">81.9%</td>
<td align="right">926</td>
<td align="right">87.9%</td>
<td align="right">-12.1%</td>
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
<td align="right">231</td>
<td align="right">99.6%</td>
<td align="right">126</td>
<td align="right">99.2%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.8%</td>
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
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
<td align="right">714,403</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">45,839,545</td>
<td align="right">97.2%</td>
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,303,082</td>
<td align="right">2.8%</td>
<td align="right">651,317</td>
<td align="right">2.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,287,942</td>
<td align="right">2.7%</td>
<td align="right">648,506</td>
<td align="right">2.8%</td>
<td align="right">-49.6%</td>
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
<td align="right">33,956</td>
<td align="right">100.0%</td>
<td align="right">21,627</td>
<td align="right">100.0%</td>
<td align="right">-36.3%</td>
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
<td align="right">903</td>
<td align="right">50.0%</td>
<td align="right">903</td>
<td align="right">50.0%</td>
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
<td align="right">903</td>
<td align="right">100.0%</td>
<td align="right">903</td>
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
<td align="right">6,535,551</td>
<td align="right">30.5%</td>
<td align="right">2,761,827</td>
<td align="right">27.5%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,901,180</td>
<td align="right">69.5%</td>
<td align="right">7,279,762</td>
<td align="right">72.5%</td>
<td align="right">-51.1%</td>
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
<td align="right">3,488</td>
<td align="right">86.9%</td>
<td align="right">2,405</td>
<td align="right">82.1%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">525</td>
<td align="right">13.1%</td>
<td align="right">525</td>
<td align="right">17.9%</td>
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
<td align="left">different types</td>
<td align="right">316</td>
<td align="right">9.1%</td>
<td align="right">168</td>
<td align="right">7.0%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">3,172</td>
<td align="right">90.9%</td>
<td align="right">2,237</td>
<td align="right">93.0%</td>
<td align="right">-29.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">650,861</td>
<td align="right">8.4%</td>
<td align="right">325,229</td>
<td align="right">8.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,092,449</td>
<td align="right">91.1%</td>
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">37,170</td>
<td align="right">0.5%</td>
<td align="right">18,738</td>
<td align="right">0.5%</td>
<td align="right">-49.6%</td>
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
<td align="right">12,580</td>
<td align="right">97.5%</td>
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">317</td>
<td align="right">2.5%</td>
<td align="right">275</td>
<td align="right">4.1%</td>
<td align="right">-13.2%</td>
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
<td align="right">127</td>
<td align="right">40.1%</td>
<td align="right">106</td>
<td align="right">38.5%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">190</td>
<td align="right">59.9%</td>
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">-11.1%</td>
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
<td align="right">1,291,519</td>
<td align="right">30.6%</td>
<td align="right">277,866</td>
<td align="right">23.4%</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,929,111</td>
<td align="right">69.4%</td>
<td align="right">906,450</td>
<td align="right">76.4%</td>
<td align="right">-69.1%</td>
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
<td align="right">2,404</td>
<td align="right">83.9%</td>
<td align="right">1,708</td>
<td align="right">78.7%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">462</td>
<td align="right">16.1%</td>
<td align="right">462</td>
<td align="right">21.3%</td>
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
<td align="left">enumerate</td>
<td align="right">400</td>
<td align="right">16.6%</td>
<td align="right">254</td>
<td align="right">14.9%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,138</td>
<td align="right">47.3%</td>
<td align="right">779</td>
<td align="right">45.6%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">380</td>
<td align="right">15.8%</td>
<td align="right">274</td>
<td align="right">16.0%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">464</td>
<td align="right">19.3%</td>
<td align="right">379</td>
<td align="right">22.2%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">0.9%</td>
<td align="right">22</td>
<td align="right">1.3%</td>
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
<td align="left">string</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">389,025</td>
<td align="right">389,025 / 0 !!</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">376,740</td>
<td align="right">376,740 / 0 !!</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8,190</td>
<td align="right">8,190 / 0 !!</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,142,574</td>
<td align="right">1,142,574 / 0 !!</td>
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">-50.0%</td>
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
<td align="right">4,517,371</td>
<td align="right">2.6%</td>
<td align="right">1,564,733</td>
<td align="right">1.9%</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,737,561</td>
<td align="right">4.5%</td>
<td align="right">3,585,451</td>
<td align="right">4.3%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">158,872,692</td>
<td align="right">92.8%</td>
<td align="right">77,589,966</td>
<td align="right">93.7%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">506,772</td>
<td align="right">0.3%</td>
<td align="right">253,498</td>
<td align="right">0.3%</td>
<td align="right">-50.0%</td>
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
<td align="right">98,556</td>
<td align="right">82.3%</td>
<td align="right">42,894</td>
<td align="right">70.0%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,138</td>
<td align="right">17.7%</td>
<td align="right">18,380</td>
<td align="right">30.0%</td>
<td align="right">-13.0%</td>
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
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">697</td>
<td align="right">3.3%</td>
<td align="right">591</td>
<td align="right">3.2%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,042</td>
<td align="right">14.4%</td>
<td align="right">2,642</td>
<td align="right">14.4%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">16,996</td>
<td align="right">80.4%</td>
<td align="right">14,807</td>
<td align="right">80.6%</td>
<td align="right">-12.9%</td>
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
<td align="right">26,932,156</td>
<td align="right">99.9%</td>
<td align="right">12,657,965</td>
<td align="right">99.9%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
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
<td align="right">4,452</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">4,872</td>
<td align="right">100.0%</td>
<td align="right">4,872</td>
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
<td align="right">32,739</td>
<td align="right">99.9%</td>
<td align="right">16,355</td>
<td align="right">99.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
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
<td align="left">Success</td>
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
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
<td align="right">2,684,280</td>
<td align="right">6.8%</td>
<td align="right">902,257</td>
<td align="right">4.7%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,591,399</td>
<td align="right">93.2%</td>
<td align="right">18,342,621</td>
<td align="right">95.3%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
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
<td align="right">51,921</td>
<td align="right">100.0%</td>
<td align="right">18,318</td>
<td align="right">100.0%</td>
<td align="right">-64.7%</td>
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
<td align="right">184,149</td>
<td align="right">99.9%</td>
<td align="right">91,989</td>
<td align="right">99.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
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
<td align="left">Success</td>
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">126</td>
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
<td align="right">3,894,870</td>
<td align="right">9.7%</td>
<td align="right">1,787,005</td>
<td align="right">9.0%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,327,137</td>
<td align="right">90.1%</td>
<td align="right">18,051,734</td>
<td align="right">90.8%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">78,315</td>
<td align="right">0.2%</td>
<td align="right">41,450</td>
<td align="right">0.2%</td>
<td align="right">-47.1%</td>
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
<td align="right">77,676</td>
<td align="right">99.4%</td>
<td align="right">37,880</td>
<td align="right">98.9%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">485</td>
<td align="right">0.6%</td>
<td align="right">422</td>
<td align="right">1.1%</td>
<td align="right">-13.0%</td>
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
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">231</td>
<td align="right">47.6%</td>
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">-9.1%</td>
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
<td align="right">4,148,073</td>
<td align="right">100.0%</td>
<td align="right">2,073,448</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">231</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">231</td>
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
<td align="right">13,067,549</td>
<td align="right">2.0%</td>
<td align="right">5,241,373</td>
<td align="right">1.9%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">279,977,494</td>
<td align="right">42.4%</td>
<td align="right">113,614,989</td>
<td align="right">41.9%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">346,600,246</td>
<td align="right">52.4%</td>
<td align="right">143,058,429</td>
<td align="right">52.8%</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">21,432,801</td>
<td align="right">3.2%</td>
<td align="right">9,172,360</td>
<td align="right">3.4%</td>
<td align="right">-57.2%</td>
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
<td align="right">90,303</td>
<td align="right">0.4%</td>
<td align="right">4,192</td>
<td align="right">0.0%</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,929,111</td>
<td align="right">14.5%</td>
<td align="right">906,450</td>
<td align="right">10.4%</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,535,551</td>
<td align="right">32.5%</td>
<td align="right">2,761,827</td>
<td align="right">31.8%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,737,561</td>
<td align="right">38.4%</td>
<td align="right">3,585,451</td>
<td align="right">41.3%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">7.1%</td>
<td align="right">714,403</td>
<td align="right">8.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,287,942</td>
<td align="right">6.4%</td>
<td align="right">648,506</td>
<td align="right">7.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,170</td>
<td align="right">0.2%</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">78,315</td>
<td align="right">0.4%</td>
<td align="right">41,450</td>
<td align="right">0.5%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,410,027</td>
<td align="right">10.8%</td>
<td align="right">286,447</td>
<td align="right">5.5%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,684,280</td>
<td align="right">20.5%</td>
<td align="right">902,257</td>
<td align="right">17.2%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,517,391</td>
<td align="right">19.3%</td>
<td align="right">982,633</td>
<td align="right">18.7%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,501,950</td>
<td align="right">11.5%</td>
<td align="right">670,694</td>
<td align="right">12.8%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,691,950</td>
<td align="right">12.9%</td>
<td align="right">769,937</td>
<td align="right">14.7%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">418,900</td>
<td align="right">3.2%</td>
<td align="right">207,627</td>
<td align="right">4.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">650,565</td>
<td align="right">5.0%</td>
<td align="right">324,298</td>
<td align="right">6.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">565,310</td>
<td align="right">4.3%</td>
<td align="right">282,563</td>
<td align="right">5.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">325,579</td>
<td align="right">2.5%</td>
<td align="right">162,763</td>
<td align="right">3.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">638,542</td>
<td align="right">4.9%</td>
<td align="right">319,627</td>
<td align="right">6.1%</td>
<td align="right">-49.9%</td>
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
<td align="right">31,359,504</td>
<td align="right">87.6%</td>
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">45,045</td>
<td align="right">0.1%</td>
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">35,753,907</td>
<td align="right">99.9%</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">450,471</td>
<td align="right">1.3%</td>
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,752,155</td>
<td align="right">7.7%</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">487,368</td>
<td align="right">1.4%</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">12,354</td>
<td align="right">0.0%</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">14,843,057</td>
<td align="right">3.4%</td>
<td align="right">4,463,498</td>
<td align="right">2.0%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,395,927</td>
<td align="right">3.0%</td>
<td align="right">3,755,482</td>
<td align="right">1.8%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">170</td>
<td align="right">0.0%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">204,487,833</td>
<td align="right">46.8%</td>
<td align="right">91,140,234</td>
<td align="right">41.8%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">169,697,792</td>
<td align="right">40.8%</td>
<td align="right">75,918,166</td>
<td align="right">36.5%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,780,037</td>
<td align="right"></td>
<td align="right">7,320,598</td>
<td align="right"></td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">27,241,048</td>
<td align="right"></td>
<td align="right">13,602,201</td>
<td align="right"></td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,266,386</td>
<td align="right"></td>
<td align="right">5,628,230</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,087,579</td>
<td align="right">39.9%</td>
<td align="right">7,540,286</td>
<td align="right">39.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,116,774</td>
<td align="right">40.0%</td>
<td align="right">7,555,962</td>
<td align="right">40.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">683,865</td>
<td align="right"></td>
<td align="right">341,849</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,675,234</td>
<td align="right"></td>
<td align="right">11,334,885</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,674,904</td>
<td align="right">60.0%</td>
<td align="right">11,337,168</td>
<td align="right">60.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,048,278</td>
<td align="right"></td>
<td align="right">542,134</td>
<td align="right"></td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">978,457</td>
<td align="right"></td>
<td align="right">506,081</td>
<td align="right"></td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">101,389,240</td>
<td align="right">24.4%</td>
<td align="right">53,095,911</td>
<td align="right">25.5%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,090</td>
<td align="right">0.1%</td>
<td align="right">15,506</td>
<td align="right">0.1%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">85,184,034</td>
<td align="right">19.5%</td>
<td align="right">45,452,897</td>
<td align="right">20.8%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">74,341</td>
<td align="right"></td>
<td align="right">40,149</td>
<td align="right"></td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">132,668,942</td>
<td align="right">31.9%</td>
<td align="right">75,296,863</td>
<td align="right">36.2%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">132,030,467</td>
<td align="right">30.2%</td>
<td align="right">77,066,132</td>
<td align="right">35.3%</td>
<td align="right">-41.6%</td>
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
<td align="right">661</td>
<td align="right">1,115,397</td>
<td align="right">12,705,694</td>
<td align="right">775,377</td>
<td align="right">1,254,936</td>
<td align="right">320</td>
<td align="right">523,485</td>
<td align="right">4,222,371</td>
<td align="right">98,381</td>
<td align="right">601,808</td>
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">172</td>
<td align="right">14.4%</td>
<td align="right">1,224</td>
<td align="right">25.0%</td>
<td align="right">611.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">384</td>
<td align="right">32.2%</td>
<td align="right">1,711</td>
<td align="right">35.0%</td>
<td align="right">345.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,191</td>
<td align="right"></td>
<td align="right">4,891</td>
<td align="right"></td>
<td align="right">310.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">635</td>
<td align="right">53.3%</td>
<td align="right">1,872</td>
<td align="right">38.3%</td>
<td align="right">194.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,445,961</td>
<td align="right"></td>
<td align="right">6,550,090</td>
<td align="right"></td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">750,305,899</td>
<td align="right">16,876.1%</td>
<td align="right">514,758,689</td>
<td align="right">7,858.8%</td>
<td align="right">-31.4%</td>
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
<td align="right">84</td>
<td align="right">1.7%</td>
<td align="right">84 / 0 !!</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">1.8%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">168</td>
<td align="right">3.4%</td>
<td align="right">168 / 0 !!</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">107</td>
<td align="right">2.2%</td>
<td align="right">107 / 0 !!</td>
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
<td align="right">530</td>
<td align="right">83.5%</td>
<td align="right">1,620</td>
<td align="right">86.5%</td>
<td align="right">205.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">635</td>
<td align="right"></td>
<td align="right">1,872</td>
<td align="right"></td>
<td align="right">194.8%</td>
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
<td align="right">1,122,699</td>
<td align="right">15.1%</td>
<td align="right">3,378,763</td>
<td align="right">21.0%</td>
<td align="right">201.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">159,376</td>
<td align="right">2.1%</td>
<td align="right">349,488</td>
<td align="right">2.2%</td>
<td align="right">119.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">7,438,336</td>
<td align="right"></td>
<td align="right">16,084,992</td>
<td align="right"></td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">6,156,261</td>
<td align="right">82.8%</td>
<td align="right">12,356,741</td>
<td align="right">76.8%</td>
<td align="right">100.7%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">86,016</td>
<td align="right">0.5%</td>
<td align="right">86,016 / 0 !!</td>
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
<td align="left">107</td>
<td align="right">20.2%</td>
<td align="left">630</td>
<td align="right">38.9%</td>
<td align="right">488.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">148</td>
<td align="right">27.9%</td>
<td align="left">547</td>
<td align="right">33.8%</td>
<td align="right">269.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">170</td>
<td align="right">32.1%</td>
<td align="left">273</td>
<td align="right">16.9%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">42</td>
<td align="right">7.9%</td>
<td align="left">85</td>
<td align="right">5.2%</td>
<td align="right">102.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">63</td>
<td align="right">11.9%</td>
<td align="left">85</td>
<td align="right">5.2%</td>
<td align="right">34.9%</td>
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
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">3.5%</td>
<td align="right">252</td>
<td align="right">13.5%</td>
<td align="right">1,045.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">149</td>
<td align="right">23.5%</td>
<td align="right">273</td>
<td align="right">14.6%</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">128</td>
<td align="right">20.2%</td>
<td align="right">484</td>
<td align="right">25.9%</td>
<td align="right">278.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">23.1%</td>
<td align="right">357</td>
<td align="right">19.1%</td>
<td align="right">142.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">3.3%</td>
<td align="right">127</td>
<td align="right">6.8%</td>
<td align="right">504.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">168</td>
<td align="right">26.5%</td>
<td align="right">126</td>
<td align="right">6.7%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">252</td>
<td align="right">13.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left"><= 16</td>
<td align="right">86</td>
<td align="right">13.5%</td>
<td align="right">336</td>
<td align="right">17.9%</td>
<td align="right">290.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">150</td>
<td align="right">23.6%</td>
<td align="right">442</td>
<td align="right">23.6%</td>
<td align="right">194.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">168</td>
<td align="right">26.5%</td>
<td align="right">357</td>
<td align="right">19.1%</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">6.6%</td>
<td align="right">106</td>
<td align="right">5.7%</td>
<td align="right">152.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">84</td>
<td align="right">13.2%</td>
<td align="right">105</td>
<td align="right">5.6%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">3.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">210</td>
<td align="right">11.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,910</td>
<td align="right">452,884</td>
<td align="right">15,463.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,725</td>
<td align="right">189,142</td>
<td align="right">3,903.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,180</td>
<td align="right">230,343</td>
<td align="right">3,627.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">10,905</td>
<td align="right">242,898</td>
<td align="right">2,127.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">9,450</td>
<td align="right">200,449</td>
<td align="right">2,021.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">9,450</td>
<td align="right">192,702</td>
<td align="right">1,939.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">4,725</td>
<td align="right">27,441</td>
<td align="right">480.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">59,438</td>
<td align="right">337,762</td>
<td align="right">468.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">59,438</td>
<td align="right">337,762</td>
<td align="right">468.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">14,406</td>
<td align="right">60,958</td>
<td align="right">323.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">16,380</td>
<td align="right">66,952</td>
<td align="right">308.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">16,380</td>
<td align="right">66,952</td>
<td align="right">308.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">54,665</td>
<td align="right">206,064</td>
<td align="right">277.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">4,725</td>
<td align="right">11,988</td>
<td align="right">153.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,445,961</td>
<td align="right">6,550,090</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,445,961</td>
<td align="right">6,550,090</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,697,574</td>
<td align="right">2,628,440</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">471,534</td>
<td align="right">277,069</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">277,069</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">277,069</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">471,534</td>
<td align="right">277,069</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">471,534</td>
<td align="right">277,071</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">82,551</td>
<td align="right">49,684</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,302,819</td>
<td align="right">784,277</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">356,265</td>
<td align="right">219,753</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">356,265</td>
<td align="right">219,755</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,716,828</td>
<td align="right">2,309,579</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,718,954</td>
<td align="right">1,700,458</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,470</td>
<td align="right">303,660</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">4,053,294</td>
<td align="right">2,564,186</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">8,106,924</td>
<td align="right">5,130,419</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">16,214,184</td>
<td align="right">10,262,888</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">8,107,260</td>
<td align="right">5,132,467</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,107,260</td>
<td align="right">5,132,468</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">8,107,260</td>
<td align="right">5,133,149</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,053,630</td>
<td align="right">2,566,957</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">20,357,169</td>
<td align="right">12,913,342</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">57,413,543</td>
<td align="right">36,446,849</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">359,390</td>
<td align="right">490,279</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">8,196,279</td>
<td align="right">5,213,917</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">23,085,092</td>
<td align="right">14,716,259</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">75,909,852</td>
<td align="right">48,448,779</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,053,630</td>
<td align="right">2,592,792</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,771,407</td>
<td align="right">2,417,168</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,856,835</td>
<td align="right">2,485,959</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">8,476,356</td>
<td align="right">5,465,433</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">6,930,483</td>
<td align="right">4,511,670</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,776,899</td>
<td align="right">5,724,330</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,042,900</td>
<td align="right">3,292,559</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">12,629,843</td>
<td align="right">8,289,297</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">5,323,313</td>
<td align="right">3,546,848</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">365,715</td>
<td align="right">243,708</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">140,857,015</td>
<td align="right">94,056,704</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,508,364</td>
<td align="right">3,019,684</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,156,677</td>
<td align="right">8,818,914</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">595,502</td>
<td align="right">789,680</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">4,508,364</td>
<td align="right">3,046,947</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,508,364</td>
<td align="right">3,048,311</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">4,508,364</td>
<td align="right">3,048,311</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,508,364</td>
<td align="right">3,048,311</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,834,334</td>
<td align="right">1,922,234</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,121,853</td>
<td align="right">6,210,654</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">145,398,833</td>
<td align="right">99,264,456</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,778,549</td>
<td align="right">1,217,630</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,147,038</td>
<td align="right">2,849,677</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,495,055</td>
<td align="right">3,092,032</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,459,112</td>
<td align="right">9,294,247</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">169,890</td>
<td align="right">222,235</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">928,720</td>
<td align="right">650,282</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,560,695</td>
<td align="right">1,095,619</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,648,811</td>
<td align="right">5,400,868</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,611,752</td>
<td align="right">1,158,778</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,384,575</td>
<td align="right">2,445,593</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">5,653,474</td>
<td align="right">4,136,111</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,294,435</td>
<td align="right">957,012</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">370,671</td>
<td align="right">280,711</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">16,550,777</td>
<td align="right">12,698,224</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,604,236</td>
<td align="right">2,028,438</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,560,695</td>
<td align="right">1,264,365</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,357,859</td>
<td align="right">1,921,197</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,550,637</td>
<td align="right">2,176,718</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,836,004</td>
<td align="right">2,432,388</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,775,378</td>
<td align="right">1,586,787</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">89,019</td>
<td align="right">80,725</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">280,413</td>
<td align="right">254,289</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">425,481</td>
<td align="right">387,307</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">98,469</td>
<td align="right">105,387</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">695,357</td>
<td align="right">738,519</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">525,525</td>
<td align="right">494,065</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">430,206</td>
<td align="right">408,732</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">127,050</td>
<td align="right">129,999</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">127,050</td>
<td align="right">129,999</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">127,050</td>
<td align="right">129,999</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,143,535</td>
<td align="right">9,178,530</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">454,734</td>
<td align="right">453,470</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">379,406</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">168,746</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">168,105</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">129,013</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">61,357</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">27,263</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">26,558</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">26,558</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">11,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">9,436</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">7,726</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">3,212</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right"></td>
<td align="right">1,889</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">683</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">683</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">566</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">46</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">2</td>
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
<td align="right"></td>
<td align="right">43</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-02
