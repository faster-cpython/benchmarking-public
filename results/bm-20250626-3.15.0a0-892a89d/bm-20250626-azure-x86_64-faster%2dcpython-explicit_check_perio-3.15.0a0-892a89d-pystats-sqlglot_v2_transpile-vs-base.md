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
<td align="left">RESUME</td>
<td align="right">181</td>
<td align="right">3,801</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">107</td>
<td align="right">2,247</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">86</td>
<td align="right">1,806</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">48</td>
<td align="right">1,008</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">536</td>
<td align="right">9,576</td>
<td align="right">1,686.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,116</td>
<td align="right">18,816</td>
<td align="right">1,586.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">462</td>
<td align="right">1,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">69</td>
<td align="right">48</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">75,553</td>
<td align="right">83,399</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,156</td>
<td align="right">24,609</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,155</td>
<td align="right">4,071</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,158</td>
<td align="right">4,074</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,158</td>
<td align="right">4,074</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,228</td>
<td align="right">4,143</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">25,020</td>
<td align="right">24,555</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,317</td>
<td align="right">8,169</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">54,062</td>
<td align="right">53,130</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">519,839</td>
<td align="right">511,119</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">29,111</td>
<td align="right">28,623</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">11,243</td>
<td align="right">11,429</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">49,906</td>
<td align="right">49,098</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">83,177</td>
<td align="right">81,837</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">241,284</td>
<td align="right">237,411</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">187,149</td>
<td align="right">184,149</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">33,271</td>
<td align="right">32,739</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,367,182</td>
<td align="right">3,313,366</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,534,767</td>
<td align="right">1,510,269</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">266,169</td>
<td align="right">261,933</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">116,449</td>
<td align="right">114,597</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">16,349,752</td>
<td align="right">16,092,413</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,933,355</td>
<td align="right">18,636,350</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,147,867</td>
<td align="right">1,129,863</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">640,477</td>
<td align="right">630,441</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">935,297</td>
<td align="right">920,672</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,106,015</td>
<td align="right">16,839,540</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">873,382</td>
<td align="right">859,782</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,503,003</td>
<td align="right">2,464,045</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,314,233</td>
<td align="right">1,293,789</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,867,376</td>
<td align="right">1,838,340</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">34,985,371</td>
<td align="right">34,441,461</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">153,882</td>
<td align="right">151,494</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">8,896,272</td>
<td align="right">8,758,373</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">11,889,709</td>
<td align="right">11,705,548</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,146,178</td>
<td align="right">35,586,327</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,243,535</td>
<td align="right">1,224,279</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,181,690</td>
<td align="right">3,132,429</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">644,642</td>
<td align="right">634,662</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,301,761</td>
<td align="right">1,281,609</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,622,943</td>
<td align="right">5,535,915</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">15,400,785</td>
<td align="right">15,162,552</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,456,933</td>
<td align="right">9,310,647</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,297,647</td>
<td align="right">10,138,443</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,767,807</td>
<td align="right">1,740,483</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,564,937</td>
<td align="right">6,463,493</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">640,484</td>
<td align="right">630,588</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,341,087</td>
<td align="right">9,196,803</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,096,677</td>
<td align="right">4,033,476</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,614,164</td>
<td align="right">3,558,408</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">573,941</td>
<td align="right">565,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">573,941</td>
<td align="right">565,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">573,941</td>
<td align="right">565,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,845,488</td>
<td align="right">2,801,622</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">119,817,544</td>
<td align="right">117,970,750</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">13,820,343</td>
<td align="right">13,607,391</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">39,890,423</td>
<td align="right">39,275,775</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">7,136,837</td>
<td align="right">7,026,873</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">13,271,361</td>
<td align="right">13,066,977</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,634,965</td>
<td align="right">3,579,009</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">11,491,314</td>
<td align="right">11,314,422</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">36,312,718</td>
<td align="right">35,753,907</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,138,281</td>
<td align="right">12,936,105</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,443,728</td>
<td align="right">12,252,240</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">1,429,155</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,409,901</td>
<td align="right">1,388,205</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">952,411</td>
<td align="right">937,755</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">632,168</td>
<td align="right">622,440</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">557,306</td>
<td align="right">548,730</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">457,490</td>
<td align="right">450,450</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">407,582</td>
<td align="right">401,310</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">203,791</td>
<td align="right">200,655</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">141,406</td>
<td align="right">139,230</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">120,611</td>
<td align="right">118,755</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">45,749</td>
<td align="right">45,045</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">45,749</td>
<td align="right">45,045</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">45,749</td>
<td align="right">45,045</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">33,272</td>
<td align="right">32,760</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">29,113</td>
<td align="right">28,665</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,954</td>
<td align="right">24,570</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,954</td>
<td align="right">24,570</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">12,477</td>
<td align="right">12,285</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">8,318</td>
<td align="right">8,190</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">4,159</td>
<td align="right">4,095</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4,159</td>
<td align="right">4,095</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,159</td>
<td align="right">4,095</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,159</td>
<td align="right">4,095</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">54,458,016</td>
<td align="right">53,619,999</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">24,176,337</td>
<td align="right">23,804,304</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">241,713,952</td>
<td align="right">237,994,383</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">11,483,069</td>
<td align="right">11,306,364</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,926,312</td>
<td align="right">12,727,398</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,703,899</td>
<td align="right">4,631,514</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,184,024</td>
<td align="right">4,119,639</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">16,112,246</td>
<td align="right">15,864,306</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,990,391</td>
<td align="right">2,944,374</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,548,246</td>
<td align="right">5,462,868</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">27,978,433</td>
<td align="right">27,547,893</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,551,377</td>
<td align="right">1,527,504</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,420,678</td>
<td align="right">2,383,428</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,262,636</td>
<td align="right">2,227,818</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">931,686</td>
<td align="right">917,349</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">831,870</td>
<td align="right">819,069</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">711,259</td>
<td align="right">700,314</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,343,497</td>
<td align="right">1,322,823</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,508,367</td>
<td align="right">2,469,768</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">341,108</td>
<td align="right">335,859</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">470,107</td>
<td align="right">462,873</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">195,543</td>
<td align="right">192,534</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,773</td>
<td align="right">69,684</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">66,614</td>
<td align="right">65,589</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,819,774</td>
<td align="right">25,422,492</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,342</td>
<td align="right">32,829</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">20,865</td>
<td align="right">20,544</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">12,547</td>
<td align="right">12,354</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,242,133</td>
<td align="right">11,069,256</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,229</td>
<td align="right">4,164</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,299,717</td>
<td align="right">1,279,817</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,500,058</td>
<td align="right">4,431,210</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,591,875</td>
<td align="right">10,431,146</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,518,331</td>
<td align="right">9,374,583</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,893,430</td>
<td align="right">6,789,754</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,334,636</td>
<td align="right">8,218,665</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">570,025</td>
<td align="right">562,995</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,730,287</td>
<td align="right">10,605,744</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,558</td>
<td align="right">37,802</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,142</td>
<td align="right">49,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">20,648,703</td>
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
<td align="right">12,782</td>
<td align="right">0.0%</td>
<td align="right">12,565</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,944,352</td>
<td align="right">98.4%</td>
<td align="right">36,374,960</td>
<td align="right">98.4%</td>
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
<td align="right">569,825</td>
<td align="right">1.5%</td>
<td align="right">561,837</td>
<td align="right">1.5%</td>
<td align="right">-1.4%</td>
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
<td align="right">297</td>
<td align="right">67.8%</td>
<td align="right">1,053</td>
<td align="right">75.6%</td>
<td align="right">254.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">141</td>
<td align="right">32.2%</td>
<td align="right">339</td>
<td align="right">24.4%</td>
<td align="right">140.4%</td>
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
<td align="right">140</td>
<td align="right">99.3%</td>
<td align="right">338</td>
<td align="right">99.7%</td>
<td align="right">141.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">1,451,491</td>
<td align="right">100.0%</td>
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">46,563,866</td>
<td align="right">97.2%</td>
<td align="right">45,839,545</td>
<td align="right">97.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,323,282</td>
<td align="right">2.8%</td>
<td align="right">1,303,082</td>
<td align="right">2.8%</td>
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
<td align="right">1,298,756</td>
<td align="right">2.7%</td>
<td align="right">1,287,942</td>
<td align="right">2.7%</td>
<td align="right">-0.8%</td>
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
<td align="right">1,303,082</td>
<td align="right">2.8%</td>
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
<td align="right">25,642</td>
<td align="right">100.0%</td>
<td align="right">33,956</td>
<td align="right">100.0%</td>
<td align="right">32.4%</td>
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
<td align="right">43</td>
<td align="right">50.0%</td>
<td align="right">903</td>
<td align="right">50.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">903</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">15,134,576</td>
<td align="right">61.4%</td>
<td align="right">14,901,180</td>
<td align="right">61.4%</td>
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
<td align="right">9,515,817</td>
<td align="right">38.6%</td>
<td align="right">9,369,885</td>
<td align="right">38.6%</td>
<td align="right">-1.5%</td>
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
<td align="right">25</td>
<td align="right">1.0%</td>
<td align="right">525</td>
<td align="right">11.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,489</td>
<td align="right">99.0%</td>
<td align="right">4,173</td>
<td align="right">88.8%</td>
<td align="right">67.7%</td>
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
<td align="right">138</td>
<td align="right">5.5%</td>
<td align="right">317</td>
<td align="right">7.6%</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">2,351</td>
<td align="right">94.5%</td>
<td align="right">3,856</td>
<td align="right">92.4%</td>
<td align="right">64.0%</td>
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
<td align="right">661,297</td>
<td align="right">8.4%</td>
<td align="right">650,861</td>
<td align="right">8.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,203,357</td>
<td align="right">91.2%</td>
<td align="right">7,092,449</td>
<td align="right">91.1%</td>
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
<td align="right">37,446</td>
<td align="right">0.5%</td>
<td align="right">37,170</td>
<td align="right">0.5%</td>
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
<td align="right">97</td>
<td align="right">0.8%</td>
<td align="right">317</td>
<td align="right">2.5%</td>
<td align="right">226.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,492</td>
<td align="right">99.2%</td>
<td align="right">12,580</td>
<td align="right">97.5%</td>
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
<td align="left">list</td>
<td align="right">50</td>
<td align="right">51.5%</td>
<td align="right">190</td>
<td align="right">59.9%</td>
<td align="right">280.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">47</td>
<td align="right">48.5%</td>
<td align="right">127</td>
<td align="right">40.1%</td>
<td align="right">170.2%</td>
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
<td align="right">1,389,154</td>
<td align="right">16.8%</td>
<td align="right">1,367,337</td>
<td align="right">16.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,891,555</td>
<td align="right">83.2%</td>
<td align="right">6,785,946</td>
<td align="right">83.2%</td>
<td align="right">-1.5%</td>
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
<td align="right">22</td>
<td align="right">1.2%</td>
<td align="right">462</td>
<td align="right">12.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,853</td>
<td align="right">98.8%</td>
<td align="right">3,346</td>
<td align="right">87.9%</td>
<td align="right">80.6%</td>
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
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">22</td>
<td align="right">0.7%</td>
<td align="right">1,000.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">189</td>
<td align="right">10.2%</td>
<td align="right">507</td>
<td align="right">15.2%</td>
<td align="right">168.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">340</td>
<td align="right">18.3%</td>
<td align="right">635</td>
<td align="right">19.0%</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">945</td>
<td align="right">51.0%</td>
<td align="right">1,631</td>
<td align="right">48.7%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">377</td>
<td align="right">20.3%</td>
<td align="right">551</td>
<td align="right">16.5%</td>
<td align="right">46.2%</td>
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
<td align="right">1,018,955</td>
<td align="right">1,018,955 / 0 !!</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">395,105</td>
<td align="right">395,105 / 0 !!</td>
<td align="right">389,025</td>
<td align="right">389,025 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">382,628</td>
<td align="right">382,628 / 0 !!</td>
<td align="right">376,740</td>
<td align="right">376,740 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">12,477</td>
<td align="right">12,477 / 0 !!</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,477</td>
<td align="right">12,477 / 0 !!</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8,318</td>
<td align="right">8,318 / 0 !!</td>
<td align="right">8,190</td>
<td align="right">8,190 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160,431</td>
<td align="right">1,160,431 / 0 !!</td>
<td align="right">1,142,574</td>
<td align="right">1,142,574 / 0 !!</td>
<td align="right">-1.5%</td>
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
<td align="right">4,804,158</td>
<td align="right">2.6%</td>
<td align="right">4,726,218</td>
<td align="right">2.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">172,468,282</td>
<td align="right">91.7%</td>
<td align="right">169,805,208</td>
<td align="right">91.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">514,342</td>
<td align="right">0.3%</td>
<td align="right">506,772</td>
<td align="right">0.3%</td>
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
<td align="right">10,722,613</td>
<td align="right">5.7%</td>
<td align="right">10,570,440</td>
<td align="right">5.7%</td>
<td align="right">-1.4%</td>
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
<td align="right">6,852</td>
<td align="right">7.0%</td>
<td align="right">21,822</td>
<td align="right">17.6%</td>
<td align="right">218.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">91,485</td>
<td align="right">93.0%</td>
<td align="right">102,489</td>
<td align="right">82.4%</td>
<td align="right">12.0%</td>
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
<td align="right">926</td>
<td align="right">13.5%</td>
<td align="right">3,042</td>
<td align="right">13.9%</td>
<td align="right">228.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">5,526</td>
<td align="right">80.6%</td>
<td align="right">17,680</td>
<td align="right">81.0%</td>
<td align="right">219.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">237</td>
<td align="right">3.5%</td>
<td align="right">697</td>
<td align="right">3.2%</td>
<td align="right">194.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">47</td>
<td align="right">0.7%</td>
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">170.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">47</td>
<td align="right">0.7%</td>
<td align="right">127</td>
<td align="right">0.6%</td>
<td align="right">170.2%</td>
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
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
<td align="right">0.0%</td>
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
<td align="right">32,506,588</td>
<td align="right">100.0%</td>
<td align="right">31,997,640</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">312</td>
<td align="right">100.0%</td>
<td align="right">4,872</td>
<td align="right">100.0%</td>
<td align="right">1,461.5%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">33,271</td>
<td align="right">100.0%</td>
<td align="right">32,739</td>
<td align="right">99.9%</td>
<td align="right">-1.6%</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">945</td>
<td align="right">0.0%</td>
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
<td align="right">37,166,033</td>
<td align="right">93.2%</td>
<td align="right">36,586,227</td>
<td align="right">93.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,724,390</td>
<td align="right">6.8%</td>
<td align="right">2,689,548</td>
<td align="right">6.8%</td>
<td align="right">-1.3%</td>
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
<td align="right">51,469</td>
<td align="right">100.0%</td>
<td align="right">52,017</td>
<td align="right">100.0%</td>
<td align="right">1.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
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
<td align="right">187,149</td>
<td align="right">100.0%</td>
<td align="right">184,149</td>
<td align="right">99.9%</td>
<td align="right">-1.6%</td>
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
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,148</td>
<td align="right">0.2%</td>
<td align="right">78,315</td>
<td align="right">0.2%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,282,084</td>
<td align="right">10.2%</td>
<td align="right">4,211,011</td>
<td align="right">10.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,680,008</td>
<td align="right">89.6%</td>
<td align="right">37,101,068</td>
<td align="right">89.6%</td>
<td align="right">-1.5%</td>
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
<td align="right">166</td>
<td align="right">0.2%</td>
<td align="right">485</td>
<td align="right">0.6%</td>
<td align="right">192.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">80,918</td>
<td align="right">99.8%</td>
<td align="right">83,652</td>
<td align="right">99.4%</td>
<td align="right">3.4%</td>
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
<td align="right">72</td>
<td align="right">43.4%</td>
<td align="right">231</td>
<td align="right">47.6%</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">28.3%</td>
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">170.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">47</td>
<td align="right">28.3%</td>
<td align="right">127</td>
<td align="right">26.2%</td>
<td align="right">170.2%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">231</td>
<td align="right">0.0%</td>
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
<td align="right">4,213,126</td>
<td align="right">100.0%</td>
<td align="right">4,148,073</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">645.2%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">523,113,098</td>
<td align="right">51.0%</td>
<td align="right">535,729,368</td>
<td align="right">52.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">456,157,690</td>
<td align="right">44.5%</td>
<td align="right">449,097,220</td>
<td align="right">43.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">13,808,401</td>
<td align="right">1.3%</td>
<td align="right">13,597,910</td>
<td align="right">1.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">32,268,967</td>
<td align="right">3.1%</td>
<td align="right">31,861,007</td>
<td align="right">3.1%</td>
<td align="right">-1.3%</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">75,148</td>
<td align="right">0.2%</td>
<td align="right">78,315</td>
<td align="right">0.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">4.7%</td>
<td align="right">1,429,155</td>
<td align="right">4.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,515,817</td>
<td align="right">31.1%</td>
<td align="right">9,369,885</td>
<td align="right">31.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,891,555</td>
<td align="right">22.5%</td>
<td align="right">6,785,946</td>
<td align="right">22.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,722,613</td>
<td align="right">35.1%</td>
<td align="right">10,570,440</td>
<td align="right">35.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">569,825</td>
<td align="right">1.9%</td>
<td align="right">561,837</td>
<td align="right">1.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,298,756</td>
<td align="right">4.2%</td>
<td align="right">1,287,942</td>
<td align="right">4.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,446</td>
<td align="right">0.1%</td>
<td align="right">37,170</td>
<td align="right">0.1%</td>
<td align="right">-0.7%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,699,213</td>
<td align="right">19.5%</td>
<td align="right">2,654,077</td>
<td align="right">19.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,687,522</td>
<td align="right">12.2%</td>
<td align="right">1,660,314</td>
<td align="right">12.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">425,751</td>
<td align="right">3.1%</td>
<td align="right">418,900</td>
<td align="right">3.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,506,213</td>
<td align="right">10.9%</td>
<td align="right">1,482,188</td>
<td align="right">10.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">648,890</td>
<td align="right">4.7%</td>
<td align="right">638,542</td>
<td align="right">4.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,879,425</td>
<td align="right">13.6%</td>
<td align="right">1,849,726</td>
<td align="right">13.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">660,981</td>
<td align="right">4.8%</td>
<td align="right">650,565</td>
<td align="right">4.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">574,149</td>
<td align="right">4.2%</td>
<td align="right">565,310</td>
<td align="right">4.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">330,667</td>
<td align="right">2.4%</td>
<td align="right">325,579</td>
<td align="right">2.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,724,390</td>
<td align="right">19.7%</td>
<td align="right">2,689,548</td>
<td align="right">19.8%</td>
<td align="right">-1.3%</td>
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
<td align="right">31,850,022</td>
<td align="right">87.6%</td>
<td align="right">31,359,504</td>
<td align="right">87.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">36,312,718</td>
<td align="right">99.9%</td>
<td align="right">35,753,907</td>
<td align="right">99.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">45,749</td>
<td align="right">0.1%</td>
<td align="right">45,045</td>
<td align="right">0.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">12,547</td>
<td align="right">0.0%</td>
<td align="right">12,354</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">457,491</td>
<td align="right">1.3%</td>
<td align="right">450,471</td>
<td align="right">1.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,005,204</td>
<td align="right">11.0%</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,005,204</td>
<td align="right">11.0%</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,500,128</td>
<td align="right">12.4%</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,500,128</td>
<td align="right">12.4%</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,794,863</td>
<td align="right">7.7%</td>
<td align="right">2,752,155</td>
<td align="right">7.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">494,924</td>
<td align="right">1.4%</td>
<td align="right">487,368</td>
<td align="right">1.4%</td>
<td align="right">-1.5%</td>
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
<td align="left">Method cache misses</td>
<td align="right">1,143,663</td>
<td align="right"></td>
<td align="right">906,524</td>
<td align="right"></td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,205,518</td>
<td align="right"></td>
<td align="right">972,669</td>
<td align="right"></td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">62,222</td>
<td align="right"></td>
<td align="right">69,674</td>
<td align="right"></td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">64,895,060</td>
<td align="right">14.6%</td>
<td align="right">63,744,808</td>
<td align="right">14.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">69,577,832</td>
<td align="right">15.7%</td>
<td align="right">68,360,126</td>
<td align="right">15.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">85,366,301</td>
<td align="right">20.3%</td>
<td align="right">83,873,260</td>
<td align="right">20.3%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">75,085,987</td>
<td align="right">17.9%</td>
<td align="right">73,778,965</td>
<td align="right">17.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,456,670</td>
<td align="right"></td>
<td align="right">11,271,160</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,016,561</td>
<td align="right"></td>
<td align="right">14,780,785</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">30,519,270</td>
<td align="right">7.3%</td>
<td align="right">30,042,456</td>
<td align="right">7.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,911,604</td>
<td align="right">8.1%</td>
<td align="right">35,355,607</td>
<td align="right">8.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,324,851</td>
<td align="right">39.9%</td>
<td align="right">15,088,001</td>
<td align="right">39.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,353,964</td>
<td align="right">40.0%</td>
<td align="right">15,116,666</td>
<td align="right">40.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">228,653,082</td>
<td align="right">54.5%</td>
<td align="right">225,120,244</td>
<td align="right">54.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">273,517,947</td>
<td align="right">61.6%</td>
<td align="right">269,306,967</td>
<td align="right">61.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,113</td>
<td align="right">0.1%</td>
<td align="right">28,665</td>
<td align="right">0.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">694,553</td>
<td align="right"></td>
<td align="right">683,865</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">23,027,442</td>
<td align="right">60.0%</td>
<td align="right">22,674,396</td>
<td align="right">60.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,024,300</td>
<td align="right"></td>
<td align="right">22,674,786</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">27,672,183</td>
<td align="right"></td>
<td align="right">27,524,646</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">651</td>
<td align="right">1,120,341</td>
<td align="right">12,427,893</td>
<td align="right">768,413</td>
<td align="right">1,242,484</td>
<td align="right">661</td>
<td align="right">1,115,397</td>
<td align="right">12,635,960</td>
<td align="right">774,339</td>
<td align="right">1,253,283</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-27
