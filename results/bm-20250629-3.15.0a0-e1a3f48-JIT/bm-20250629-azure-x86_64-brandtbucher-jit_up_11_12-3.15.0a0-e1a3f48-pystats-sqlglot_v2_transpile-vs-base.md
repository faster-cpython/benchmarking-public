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
<td align="right">118,902</td>
<td align="right">562,627</td>
<td align="right">373.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,430,957</td>
<td align="right">4,330,561</td>
<td align="right">202.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,023</td>
<td align="right">4,071</td>
<td align="right">101.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">2,026</td>
<td align="right">4,074</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,026</td>
<td align="right">4,074</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,073</td>
<td align="right">8,169</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">26,506</td>
<td align="right">53,130</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">255,119</td>
<td align="right">511,119</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">14,287</td>
<td align="right">28,623</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">459,788</td>
<td align="right">920,672</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">24,522</td>
<td align="right">49,098</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">40,877</td>
<td align="right">81,837</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,266</td>
<td align="right">24,555</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">91,989</td>
<td align="right">184,149</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">16,355</td>
<td align="right">32,739</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,655,294</td>
<td align="right">3,313,366</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">130,861</td>
<td align="right">261,933</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">57,253</td>
<td align="right">114,597</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">754,555</td>
<td align="right">1,510,269</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">315,049</td>
<td align="right">630,441</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">918,788</td>
<td align="right">1,838,340</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">640,585</td>
<td align="right">1,281,609</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">869,956</td>
<td align="right">1,740,483</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,778,696</td>
<td align="right">3,558,408</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">282,465</td>
<td align="right">565,089</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">282,465</td>
<td align="right">565,089</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">282,465</td>
<td align="right">565,089</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">693,933</td>
<td align="right">1,388,205</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">468,763</td>
<td align="right">937,755</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">274,298</td>
<td align="right">548,730</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">225,170</td>
<td align="right">450,450</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">200,606</td>
<td align="right">401,310</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">100,303</td>
<td align="right">200,655</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">59,363</td>
<td align="right">118,755</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">22,517</td>
<td align="right">45,045</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,517</td>
<td align="right">45,045</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,517</td>
<td align="right">45,045</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">16,376</td>
<td align="right">32,760</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">14,329</td>
<td align="right">28,665</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,282</td>
<td align="right">24,570</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,282</td>
<td align="right">24,570</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,141</td>
<td align="right">12,285</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">4,094</td>
<td align="right">8,190</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,047</td>
<td align="right">4,095</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,047</td>
<td align="right">4,095</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,047</td>
<td align="right">4,095</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,047</td>
<td align="right">4,095</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">763,599</td>
<td align="right">1,527,504</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,113,704</td>
<td align="right">2,227,818</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">311,144</td>
<td align="right">622,392</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,400,591</td>
<td align="right">2,801,622</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,215,274</td>
<td align="right">4,431,210</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">350,105</td>
<td align="right">700,314</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,212,350</td>
<td align="right">10,426,206</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">167,922</td>
<td align="right">335,859</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">231,447</td>
<td align="right">462,873</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">96,277</td>
<td align="right">192,534</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">34,867</td>
<td align="right">69,684</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">32,820</td>
<td align="right">65,589</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,318</td>
<td align="right">24,609</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">16,444</td>
<td align="right">32,829</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">10,303</td>
<td align="right">20,544</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,234,817</td>
<td align="right">2,460,276</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">6,209</td>
<td align="right">12,354</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">639,817</td>
<td align="right">1,270,325</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,762</td>
<td align="right">49,138</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">118,626</td>
<td align="right">235,374</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,094</td>
<td align="right">4,143</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">661,317</td>
<td align="right">1,306,107</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,170,897</td>
<td align="right">18,081,362</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">317,222</td>
<td align="right">625,170</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,115</td>
<td align="right">4,164</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">458,596</td>
<td align="right">902,622</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">19,328</td>
<td align="right">37,802</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,019,711</td>
<td align="right">31,108,077</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,798,970</td>
<td align="right">30,520,581</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">409,468</td>
<td align="right">789,774</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,035,665</td>
<td align="right">13,558,767</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">398,351</td>
<td align="right">767,340</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,752,412</td>
<td align="right">12,930,191</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,724,878</td>
<td align="right">22,407,261</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,429,941</td>
<td align="right">2,718,007</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,215,822</td>
<td align="right">2,310,858</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,763,056</td>
<td align="right">9,038,503</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,460,672</td>
<td align="right">4,649,643</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,336,094</td>
<td align="right">2,515,273</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,376,445</td>
<td align="right">4,424,201</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,760,024</td>
<td align="right">12,562,369</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,439,319</td>
<td align="right">4,532,840</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,215,505</td>
<td align="right">18,971,711</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,186</td>
<td align="right">11,429</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,991,828</td>
<td align="right">23,970,684</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,189,792</td>
<td align="right">2,192,034</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,039,746</td>
<td align="right">7,424,357</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,572,206</td>
<td align="right">2,887,023</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,404,263</td>
<td align="right">6,193,148</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,279,252</td>
<td align="right">34,797,997</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,509,111</td>
<td align="right">8,098,752</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,203,253</td>
<td align="right">11,137,144</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">46,471</td>
<td align="right">83,399</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,040,876</td>
<td align="right">16,111,707</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,687,505</td>
<td align="right">6,567,234</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,175,587</td>
<td align="right">5,649,273</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">75,142,359</td>
<td align="right">128,875,201</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">418,921</td>
<td align="right">710,052</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,453,031</td>
<td align="right">2,451,584</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,531,613</td>
<td align="right">4,247,615</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,409,876</td>
<td align="right">2,365,421</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,557,014</td>
<td align="right">4,284,398</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">308,097</td>
<td align="right">504,168</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">33,033,958</td>
<td align="right">53,832,455</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,666,503</td>
<td align="right">2,525,607</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,115,198</td>
<td align="right">13,617,257</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,397,966</td>
<td align="right">3,567,441</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">89,306</td>
<td align="right">48,640</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,102,784</td>
<td align="right">4,478,439</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">624,256</td>
<td align="right">895,566</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,839,805</td>
<td align="right">4,063,965</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,774,469</td>
<td align="right">3,933,093</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,855,203</td>
<td align="right">2,586,479</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">564,615</td>
<td align="right">758,856</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,432,620</td>
<td align="right">3,249,228</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">69,598</td>
<td align="right">86,982</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">75,718</td>
<td align="right">92,106</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,963,794</td>
<td align="right">2,313,171</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,119,304</td>
<td align="right">1,861,725</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">538,403</td>
<td align="right">481,194</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,592,734</td>
<td align="right">1,691,445</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">47</td>
<td align="right">48</td>
<td align="right">2.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,182,576</td>
<td align="right">99.5%</td>
<td align="right">36,374,960</td>
<td align="right">99.8%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,293</td>
<td align="right">0.0%</td>
<td align="right">12,565</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">88,255</td>
<td align="right">0.5%</td>
<td align="right">47,610</td>
<td align="right">0.1%</td>
<td align="right">-46.1%</td>
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
<td align="right">926</td>
<td align="right">80.0%</td>
<td align="right">1,053</td>
<td align="right">83.3%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">232</td>
<td align="right">20.0%</td>
<td align="right">211</td>
<td align="right">16.7%</td>
<td align="right">-9.1%</td>
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
<td align="right">210</td>
<td align="right">99.5%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
<td align="right">714,403</td>
<td align="right">100.0%</td>
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
<td align="right">45,839,545</td>
<td align="right">97.2%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">651,317</td>
<td align="right">2.8%</td>
<td align="right">1,303,082</td>
<td align="right">2.8%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">648,506</td>
<td align="right">2.8%</td>
<td align="right">1,287,942</td>
<td align="right">2.7%</td>
<td align="right">98.6%</td>
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
<td align="right">21,627</td>
<td align="right">100.0%</td>
<td align="right">33,956</td>
<td align="right">100.0%</td>
<td align="right">57.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,448,508</td>
<td align="right">68.6%</td>
<td align="right">14,901,180</td>
<td align="right">70.6%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,401,059</td>
<td align="right">31.3%</td>
<td align="right">6,189,219</td>
<td align="right">29.3%</td>
<td align="right">82.0%</td>
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
<td align="right">2,679</td>
<td align="right">83.6%</td>
<td align="right">3,404</td>
<td align="right">86.6%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">525</td>
<td align="right">16.4%</td>
<td align="right">525</td>
<td align="right">13.4%</td>
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
<td align="right">2,426</td>
<td align="right">90.6%</td>
<td align="right">3,087</td>
<td align="right">90.7%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">253</td>
<td align="right">9.4%</td>
<td align="right">317</td>
<td align="right">9.3%</td>
<td align="right">25.3%</td>
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
<td align="right">325,229</td>
<td align="right">8.4%</td>
<td align="right">650,861</td>
<td align="right">8.4%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
<td align="right">7,092,449</td>
<td align="right">91.1%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">18,738</td>
<td align="right">0.5%</td>
<td align="right">37,170</td>
<td align="right">0.5%</td>
<td align="right">98.4%</td>
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
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">12,580</td>
<td align="right">97.5%</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">275</td>
<td align="right">4.1%</td>
<td align="right">317</td>
<td align="right">2.5%</td>
<td align="right">15.3%</td>
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
<td align="right">106</td>
<td align="right">38.5%</td>
<td align="right">127</td>
<td align="right">40.1%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">190</td>
<td align="right">59.9%</td>
<td align="right">12.4%</td>
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
<td align="right">1,852,634</td>
<td align="right">73.0%</td>
<td align="right">2,583,697</td>
<td align="right">73.3%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">683,304</td>
<td align="right">26.9%</td>
<td align="right">936,942</td>
<td align="right">26.6%</td>
<td align="right">37.1%</td>
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
<td align="right">2,107</td>
<td align="right">82.0%</td>
<td align="right">2,320</td>
<td align="right">83.4%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">462</td>
<td align="right">18.0%</td>
<td align="right">462</td>
<td align="right">16.6%</td>
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
<td align="left">ascii string</td>
<td align="right">316</td>
<td align="right">15.0%</td>
<td align="right">359</td>
<td align="right">15.5%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">990</td>
<td align="right">47.0%</td>
<td align="right">1,116</td>
<td align="right">48.1%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">400</td>
<td align="right">19.0%</td>
<td align="right">444</td>
<td align="right">19.1%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">379</td>
<td align="right">18.0%</td>
<td align="right">379</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">1.0%</td>
<td align="right">22</td>
<td align="right">0.9%</td>
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
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">389,025</td>
<td align="right">389,025 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">376,740</td>
<td align="right">376,740 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
<td align="right">8,190</td>
<td align="right">8,190 / 0 !!</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">1,142,574</td>
<td align="right">1,142,574 / 0 !!</td>
<td align="right">100.0%</td>
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
<td align="right">253,498</td>
<td align="right">0.3%</td>
<td align="right">506,772</td>
<td align="right">0.3%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,901,969</td>
<td align="right">92.6%</td>
<td align="right">157,686,965</td>
<td align="right">93.0%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,323,171</td>
<td align="right">2.7%</td>
<td align="right">4,461,680</td>
<td align="right">2.6%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,007,693</td>
<td align="right">4.6%</td>
<td align="right">7,389,822</td>
<td align="right">4.4%</td>
<td align="right">84.4%</td>
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
<td align="right">57,215</td>
<td align="right">75.5%</td>
<td align="right">97,491</td>
<td align="right">82.2%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">18,571</td>
<td align="right">24.5%</td>
<td align="right">21,053</td>
<td align="right">17.8%</td>
<td align="right">13.4%</td>
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
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">592</td>
<td align="right">3.2%</td>
<td align="right">697</td>
<td align="right">3.3%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,643</td>
<td align="right">14.2%</td>
<td align="right">3,042</td>
<td align="right">14.4%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">14,996</td>
<td align="right">80.7%</td>
<td align="right">16,911</td>
<td align="right">80.3%</td>
<td align="right">12.8%</td>
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
<td align="right">13,791,237</td>
<td align="right">99.9%</td>
<td align="right">26,116,684</td>
<td align="right">99.9%</td>
<td align="right">89.4%</td>
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
<td align="right">16,355</td>
<td align="right">99.7%</td>
<td align="right">32,739</td>
<td align="right">99.9%</td>
<td align="right">100.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,284,591</td>
<td align="right">93.1%</td>
<td align="right">36,609,757</td>
<td align="right">93.2%</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,348,111</td>
<td align="right">6.9%</td>
<td align="right">2,665,584</td>
<td align="right">6.8%</td>
<td align="right">97.7%</td>
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
<td align="right">26,736</td>
<td align="right">100.0%</td>
<td align="right">51,583</td>
<td align="right">100.0%</td>
<td align="right">92.9%</td>
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
<td align="right">91,989</td>
<td align="right">99.7%</td>
<td align="right">184,149</td>
<td align="right">99.9%</td>
<td align="right">100.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,224,095</td>
<td align="right">90.1%</td>
<td align="right">36,240,893</td>
<td align="right">90.5%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">41,450</td>
<td align="right">0.2%</td>
<td align="right">78,315</td>
<td align="right">0.2%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,963,074</td>
<td align="right">9.7%</td>
<td align="right">3,699,050</td>
<td align="right">9.2%</td>
<td align="right">88.4%</td>
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
<td align="right">41,201</td>
<td align="right">99.0%</td>
<td align="right">73,997</td>
<td align="right">99.3%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">422</td>
<td align="right">1.0%</td>
<td align="right">485</td>
<td align="right">0.7%</td>
<td align="right">14.9%</td>
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
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">231</td>
<td align="right">47.6%</td>
<td align="right">10.0%</td>
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
<td align="right">2,073,448</td>
<td align="right">100.0%</td>
<td align="right">4,148,073</td>
<td align="right">100.0%</td>
<td align="right">100.1%</td>
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
<td align="right">6,621,670</td>
<td align="right">1.9%</td>
<td align="right">12,797,423</td>
<td align="right">2.1%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,033,971</td>
<td align="right">52.2%</td>
<td align="right">326,965,111</td>
<td align="right">52.7%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,538,015</td>
<td align="right">3.3%</td>
<td align="right">20,351,454</td>
<td align="right">3.3%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">148,777,150</td>
<td align="right">42.6%</td>
<td align="right">259,807,940</td>
<td align="right">41.9%</td>
<td align="right">74.6%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">6.6%</td>
<td align="right">1,429,155</td>
<td align="right">7.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">648,506</td>
<td align="right">6.0%</td>
<td align="right">1,287,942</td>
<td align="right">6.8%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">37,170</td>
<td align="right">0.2%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">41,450</td>
<td align="right">0.4%</td>
<td align="right">78,315</td>
<td align="right">0.4%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,007,693</td>
<td align="right">37.2%</td>
<td align="right">7,389,822</td>
<td align="right">38.8%</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,401,059</td>
<td align="right">31.6%</td>
<td align="right">6,189,219</td>
<td align="right">32.5%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">88,255</td>
<td align="right">0.8%</td>
<td align="right">47,610</td>
<td align="right">0.2%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,852,634</td>
<td align="right">17.2%</td>
<td align="right">2,583,697</td>
<td align="right">13.6%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">208,806</td>
<td align="right">3.2%</td>
<td align="right">418,900</td>
<td align="right">3.3%</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">324,298</td>
<td align="right">4.9%</td>
<td align="right">650,565</td>
<td align="right">5.1%</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">282,563</td>
<td align="right">4.3%</td>
<td align="right">565,310</td>
<td align="right">4.4%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">162,763</td>
<td align="right">2.5%</td>
<td align="right">325,579</td>
<td align="right">2.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">319,627</td>
<td align="right">4.8%</td>
<td align="right">638,542</td>
<td align="right">5.0%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,348,111</td>
<td align="right">20.4%</td>
<td align="right">2,665,584</td>
<td align="right">20.8%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,288,155</td>
<td align="right">19.5%</td>
<td align="right">2,512,198</td>
<td align="right">19.6%</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">856,804</td>
<td align="right">12.9%</td>
<td align="right">1,594,504</td>
<td align="right">12.5%</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">758,695</td>
<td align="right">11.5%</td>
<td align="right">1,404,267</td>
<td align="right">11.0%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">739,363</td>
<td align="right">11.2%</td>
<td align="right">1,359,529</td>
<td align="right">10.6%</td>
<td align="right">83.9%</td>
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
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">31,359,504</td>
<td align="right">87.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">45,045</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
<td align="right">35,753,907</td>
<td align="right">99.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">450,471</td>
<td align="right">1.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
<td align="right">2,752,155</td>
<td align="right">7.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
<td align="right">487,368</td>
<td align="right">1.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">12,354</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">37,204</td>
<td align="right"></td>
<td align="right">150,489</td>
<td align="right"></td>
<td align="right">304.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">509,894</td>
<td align="right"></td>
<td align="right">1,217,611</td>
<td align="right"></td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">475,680</td>
<td align="right"></td>
<td align="right">1,070,120</td>
<td align="right"></td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">62,370,980</td>
<td align="right">28.6%</td>
<td align="right">139,675,986</td>
<td align="right">31.9%</td>
<td align="right">123.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">63,315,617</td>
<td align="right">30.5%</td>
<td align="right">139,471,123</td>
<td align="right">33.4%</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">41,653,619</td>
<td align="right">19.1%</td>
<td align="right">87,568,282</td>
<td align="right">20.0%</td>
<td align="right">110.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">49,932,869</td>
<td align="right">24.0%</td>
<td align="right">103,457,422</td>
<td align="right">24.8%</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,330,919</td>
<td align="right"></td>
<td align="right">14,780,934</td>
<td align="right"></td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">14,541</td>
<td align="right">0.1%</td>
<td align="right">29,194</td>
<td align="right">0.1%</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,554,226</td>
<td align="right">40.0%</td>
<td align="right">15,117,028</td>
<td align="right">40.0%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,539,622</td>
<td align="right">39.9%</td>
<td align="right">15,087,708</td>
<td align="right">39.9%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">341,849</td>
<td align="right"></td>
<td align="right">683,865</td>
<td align="right"></td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,335,312</td>
<td align="right"></td>
<td align="right">22,675,148</td>
<td align="right"></td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,337,495</td>
<td align="right">60.0%</td>
<td align="right">22,674,818</td>
<td align="right">60.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">5,631,280</td>
<td align="right"></td>
<td align="right">11,190,217</td>
<td align="right"></td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,730,007</td>
<td align="right"></td>
<td align="right">27,072,384</td>
<td align="right"></td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">105,479,693</td>
<td align="right">48.4%</td>
<td align="right">197,745,366</td>
<td align="right">45.2%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">87,530,019</td>
<td align="right">42.1%</td>
<td align="right">163,797,502</td>
<td align="right">39.3%</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">8,369,063</td>
<td align="right">3.8%</td>
<td align="right">12,546,702</td>
<td align="right">2.9%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">7,011,330</td>
<td align="right">3.4%</td>
<td align="right">10,415,743</td>
<td align="right">2.5%</td>
<td align="right">48.6%</td>
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
<td align="right">320</td>
<td align="right">529,920</td>
<td align="right">4,206,903</td>
<td align="right">103,072</td>
<td align="right">596,496</td>
<td align="right">661</td>
<td align="right">1,115,712</td>
<td align="right">12,640,944</td>
<td align="right">773,345</td>
<td align="right">1,255,472</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">109</td>
<td align="right">20.4%</td>
<td align="right">427</td>
<td align="right">30.5%</td>
<td align="right">291.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,492,713</td>
<td align="right"></td>
<td align="right">5,226,433</td>
<td align="right"></td>
<td align="right">250.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">534</td>
<td align="right"></td>
<td align="right">1,401</td>
<td align="right"></td>
<td align="right">162.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">331,810,567</td>
<td align="right">22,228.7%</td>
<td align="right">839,609,911</td>
<td align="right">16,064.7%</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">339</td>
<td align="right">63.5%</td>
<td align="right">782</td>
<td align="right">55.8%</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">86</td>
<td align="right">16.1%</td>
<td align="right">171</td>
<td align="right">12.2%</td>
<td align="right">98.8%</td>
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
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">21 / 0 !!</td>
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

A potential trace is abandoned because it it too short.
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">42</td>
<td align="right">3.0%</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">275</td>
<td align="right">81.1%</td>
<td align="right">677</td>
<td align="right">86.6%</td>
<td align="right">146.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">339</td>
<td align="right"></td>
<td align="right">782</td>
<td align="right"></td>
<td align="right">130.7%</td>
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
<td align="right">617,097</td>
<td align="right">13.7%</td>
<td align="right">1,387,773</td>
<td align="right">14.6%</td>
<td align="right">124.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">94,696</td>
<td align="right">2.1%</td>
<td align="right">203,208</td>
<td align="right">2.1%</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,489,216</td>
<td align="right"></td>
<td align="right">9,502,720</td>
<td align="right"></td>
<td align="right">111.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">3,777,423</td>
<td align="right">84.1%</td>
<td align="right">7,911,739</td>
<td align="right">83.3%</td>
<td align="right">109.4%</td>
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
<td align="left">22</td>
<td align="right">8.0%</td>
<td align="left">107</td>
<td align="right">15.8%</td>
<td align="right">386.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">84</td>
<td align="right">30.5%</td>
<td align="left">233</td>
<td align="right">34.4%</td>
<td align="right">177.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">106</td>
<td align="right">38.5%</td>
<td align="left">211</td>
<td align="right">31.2%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">7.6%</td>
<td align="left">42</td>
<td align="right">6.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">15.3%</td>
<td align="left">84</td>
<td align="right">12.4%</td>
<td align="right">100.0%</td>
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
<td align="left"><= 32</td>
<td align="right">43</td>
<td align="right">12.7%</td>
<td align="right">190</td>
<td align="right">24.3%</td>
<td align="right">341.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">84</td>
<td align="right">24.8%</td>
<td align="right">191</td>
<td align="right">24.4%</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">190</td>
<td align="right">24.3%</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">5.4%</td>
<td align="right">42 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">147</td>
<td align="right">18.8%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">22</td>
<td align="right">2.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">22</td>
<td align="right">6.5%</td>
<td align="right">64</td>
<td align="right">8.2%</td>
<td align="right">190.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">170</td>
<td align="right">21.7%</td>
<td align="right">169.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">253</td>
<td align="right">32.4%</td>
<td align="right">138.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">6.2%</td>
<td align="right">63</td>
<td align="right">8.1%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">105</td>
<td align="right">13.4%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">22</td>
<td align="right">2.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left">_POP_ITER</td>
<td align="right">1,698</td>
<td align="right">191,394</td>
<td align="right">11,171.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,099</td>
<td align="right">155,715</td>
<td align="right">2,093.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,099</td>
<td align="right">126,420</td>
<td align="right">1,680.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">22,365</td>
<td align="right">398,223</td>
<td align="right">1,680.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,657</td>
<td align="right">150,231</td>
<td align="right">859.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,657</td>
<td align="right">150,231</td>
<td align="right">859.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">15,657</td>
<td align="right">150,231</td>
<td align="right">859.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">142,180</td>
<td align="right">554,988</td>
<td align="right">290.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">189,556</td>
<td align="right">708,961</td>
<td align="right">274.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,492,713</td>
<td align="right">5,226,433</td>
<td align="right">250.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,492,713</td>
<td align="right">5,226,433</td>
<td align="right">250.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">135,081</td>
<td align="right">451,521</td>
<td align="right">234.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">173,869</td>
<td align="right">557,243</td>
<td align="right">220.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">135,081</td>
<td align="right">428,568</td>
<td align="right">217.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">135,767</td>
<td align="right">429,101</td>
<td align="right">216.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">135,767</td>
<td align="right">414,422</td>
<td align="right">205.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">248,919</td>
<td align="right">742,561</td>
<td align="right">198.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">525,655</td>
<td align="right">1,559,266</td>
<td align="right">196.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">135,081</td>
<td align="right">399,273</td>
<td align="right">195.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">135,081</td>
<td align="right">399,273</td>
<td align="right">195.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">135,081</td>
<td align="right">399,273</td>
<td align="right">195.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">31,351</td>
<td align="right">92,442</td>
<td align="right">194.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,594,416</td>
<td align="right">10,331,847</td>
<td align="right">187.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,201,538</td>
<td align="right">9,114,770</td>
<td align="right">184.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">390,574</td>
<td align="right">1,111,714</td>
<td align="right">184.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">194,444</td>
<td align="right">547,323</td>
<td align="right">181.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">981,633</td>
<td align="right">2,753,406</td>
<td align="right">180.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">606,319</td>
<td align="right">1,668,055</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">606,319</td>
<td align="right">1,668,055</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">522,531</td>
<td align="right">1,433,565</td>
<td align="right">174.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,539,775</td>
<td align="right">4,202,249</td>
<td align="right">172.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">698,455</td>
<td align="right">1,892,314</td>
<td align="right">170.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">2,278,033</td>
<td align="right">6,141,429</td>
<td align="right">169.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">193,006</td>
<td align="right">514,227</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">514,227</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">514,227</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">193,006</td>
<td align="right">514,227</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">193,006</td>
<td align="right">514,227</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,447,309</td>
<td align="right">3,843,295</td>
<td align="right">165.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,708,510</td>
<td align="right">14,773,986</td>
<td align="right">158.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,656,089</td>
<td align="right">4,277,171</td>
<td align="right">158.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">3,721,468</td>
<td align="right">9,525,894</td>
<td align="right">156.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,039,582</td>
<td align="right">17,986,858</td>
<td align="right">155.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,988,182</td>
<td align="right">5,065,746</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,988,182</td>
<td align="right">5,065,746</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,988,182</td>
<td align="right">5,065,746</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,988,182</td>
<td align="right">5,065,746</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">2,255,668</td>
<td align="right">5,743,206</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,988,182</td>
<td align="right">5,056,254</td>
<td align="right">154.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,531,163</td>
<td align="right">6,414,406</td>
<td align="right">153.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,051,776</td>
<td align="right">10,261,349</td>
<td align="right">153.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,655,092</td>
<td align="right">4,187,858</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">64,378,571</td>
<td align="right">162,502,245</td>
<td align="right">152.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">734,852</td>
<td align="right">1,851,150</td>
<td align="right">151.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">5,544,555</td>
<td align="right">13,931,009</td>
<td align="right">151.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">62,828,119</td>
<td align="right">157,593,797</td>
<td align="right">150.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,938,671</td>
<td align="right">9,878,055</td>
<td align="right">150.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,853,101</td>
<td align="right">4,645,830</td>
<td align="right">150.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">3,104,441</td>
<td align="right">7,737,744</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,283,002</td>
<td align="right">3,181,256</td>
<td align="right">148.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,283,002</td>
<td align="right">3,180,666</td>
<td align="right">147.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,250,654</td>
<td align="right">3,097,815</td>
<td align="right">147.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">25,934,797</td>
<td align="right">64,135,615</td>
<td align="right">147.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,699,103</td>
<td align="right">9,128,952</td>
<td align="right">146.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">34,385,692</td>
<td align="right">84,804,732</td>
<td align="right">146.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,237,109</td>
<td align="right">22,633,230</td>
<td align="right">145.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,088,558</td>
<td align="right">2,664,627</td>
<td align="right">144.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,117,414</td>
<td align="right">2,733,033</td>
<td align="right">144.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,846,002</td>
<td align="right">4,510,758</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">10,517,504</td>
<td align="right">25,658,084</td>
<td align="right">144.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">791,406</td>
<td align="right">1,930,653</td>
<td align="right">144.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,692,004</td>
<td align="right">9,003,012</td>
<td align="right">143.9%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">3,692,004</td>
<td align="right">9,003,012</td>
<td align="right">143.9%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">3,692,004</td>
<td align="right">9,003,012</td>
<td align="right">143.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,846,002</td>
<td align="right">4,501,266</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">7,384,008</td>
<td align="right">18,003,783</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,692,004</td>
<td align="right">9,001,251</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">1,846,002</td>
<td align="right">4,499,985</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,101,703</td>
<td align="right">5,105,414</td>
<td align="right">142.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,092,541</td>
<td align="right">14,737,239</td>
<td align="right">141.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,039,981</td>
<td align="right">4,912,405</td>
<td align="right">140.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right"></td>
<td align="right">371,007</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right"></td>
<td align="right">371,007</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right"></td>
<td align="right">255,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">59,388</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">59,388</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">52,248</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">31,395</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">29,343</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">29,295</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">18,753</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">16,716</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">14,727</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right"></td>
<td align="right">14,679</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">9,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">9,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">9,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right"></td>
<td align="right">4,842</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">2,037</td>
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
Stats gathered on: 2025-06-29
