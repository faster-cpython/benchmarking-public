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
<td align="left">COMPARE_OP</td>
<td align="right">724,450</td>
<td align="right">798,939</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">520,119</td>
<td align="right">571,538</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,061,266</td>
<td align="right">1,164,091</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">357,553</td>
<td align="right">391,807</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,075,785</td>
<td align="right">1,176,687</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">365,866</td>
<td align="right">400,120</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">759,264</td>
<td align="right">827,794</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,450,198</td>
<td align="right">1,581,080</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">380,580</td>
<td align="right">414,872</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">570,421</td>
<td align="right">621,776</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">380,900</td>
<td align="right">415,192</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">574,761</td>
<td align="right">626,137</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">191,303</td>
<td align="right">208,266</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,478,444</td>
<td align="right">1,609,326</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,138,186</td>
<td align="right">1,238,363</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,773,805</td>
<td align="right">4,104,990</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,516,261</td>
<td align="right">1,647,143</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">601,568</td>
<td align="right">652,952</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">5,031,476</td>
<td align="right">5,456,309</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">748,050</td>
<td align="right">810,399</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,270,132</td>
<td align="right">1,375,878</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">209,028</td>
<td align="right">226,155</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">211,903</td>
<td align="right">229,006</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,541,061</td>
<td align="right">8,144,679</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">214,959</td>
<td align="right">232,078</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,449,143</td>
<td align="right">6,958,778</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,932,091</td>
<td align="right">3,162,407</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,405,568</td>
<td align="right">1,515,874</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,376,969</td>
<td align="right">1,484,839</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,957,025</td>
<td align="right">10,734,787</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,555,574</td>
<td align="right">4,898,401</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,040,492</td>
<td align="right">11,864,805</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,010,219</td>
<td align="right">2,159,452</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">912,461</td>
<td align="right">979,815</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,255,907</td>
<td align="right">1,347,706</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,350,101</td>
<td align="right">11,103,962</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,243,857</td>
<td align="right">5,620,857</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,878,541</td>
<td align="right">13,787,323</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">62,276,156</td>
<td align="right">66,531,551</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,531,231</td>
<td align="right">1,633,975</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,014,113</td>
<td align="right">4,283,234</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,754,847</td>
<td align="right">2,937,648</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,020,480</td>
<td align="right">7,480,820</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,309,971</td>
<td align="right">6,719,681</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,608,352</td>
<td align="right">3,839,364</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,590,086</td>
<td align="right">15,519,773</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,835,967</td>
<td align="right">1,952,752</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,750,728</td>
<td align="right">2,925,177</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">24,937,089</td>
<td align="right">26,506,298</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">393,330</td>
<td align="right">369,114</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,652,121</td>
<td align="right">13,382,587</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,849,974</td>
<td align="right">3,011,648</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,231,152</td>
<td align="right">1,299,685</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">954,987</td>
<td align="right">1,006,398</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,311,580</td>
<td align="right">1,380,233</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,619,116</td>
<td align="right">2,756,166</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,830,313</td>
<td align="right">1,925,999</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">998,707</td>
<td align="right">1,050,120</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,816,861</td>
<td align="right">6,115,168</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">335,862</td>
<td align="right">352,965</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,623,578</td>
<td align="right">2,753,454</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">27,410,034</td>
<td align="right">28,764,657</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,682,558</td>
<td align="right">3,862,664</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">760,238</td>
<td align="right">796,960</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,225,150</td>
<td align="right">19,079,389</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,067,102</td>
<td align="right">22,035,382</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,682,828</td>
<td align="right">6,957,995</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">103</td>
<td align="right">107</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">460</td>
<td align="right">477</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,346,972</td>
<td align="right">8,638,250</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,513,090</td>
<td align="right">3,635,536</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,886,768</td>
<td align="right">5,032,538</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">676,286</td>
<td align="right">693,404</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">102,445</td>
<td align="right">104,953</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,609,377</td>
<td align="right">6,729,032</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">348</td>
<td align="right">354</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,143,227</td>
<td align="right">1,162,838</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,574</td>
<td align="right">1,601</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,644,985</td>
<td align="right">4,714,967</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,504</td>
<td align="right">4,562</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,197</td>
<td align="right">3,234</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,071</td>
<td align="right">5,126</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">734,189</td>
<td align="right">741,702</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,020,512</td>
<td align="right">2,040,123</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,447,176</td>
<td align="right">11,507,526</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">600,612</td>
<td align="right">603,718</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,469</td>
<td align="right">13,524</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,692</td>
<td align="right">17,747</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,692</td>
<td align="right">17,747</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">204,831</td>
<td align="right">205,074</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,567</td>
<td align="right">16,578</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">108,871</td>
<td align="right">108,932</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,428</td>
<td align="right">97,376</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,540</td>
<td align="right">456,702</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,042</td>
<td align="right">34,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,424</td>
<td align="right">102,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,433</td>
<td align="right">46,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,121</td>
<td align="right">35,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,015</td>
<td align="right">191,025</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,850</td>
<td align="right">928,812</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,673</td>
<td align="right">81,671</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,707</td>
<td align="right">1,818,699</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,626</td>
<td align="right">939,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,280</td>
<td align="right">5,068,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,575</td>
<td align="right">4,723,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,671</td>
<td align="right">426,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,140</td>
<td align="right">105,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,431</td>
<td align="right">86,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,720</td>
<td align="right">84,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,356</td>
<td align="right">77,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,588</td>
<td align="right">67,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,116</td>
<td align="right">59,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,863</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,859</td>
<td align="right">55,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,010</td>
<td align="right">44,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,252</td>
<td align="right">31,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,557</td>
<td align="right">29,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,908</td>
<td align="right">21,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,809</td>
<td align="right">17,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">14,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,837</td>
<td align="right">12,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,380</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,488</td>
<td align="right">8,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">784</td>
<td align="right">784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">504</td>
<td align="right">504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">491</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">391</td>
<td align="right">391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">207</td>
<td align="right">207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">181</td>
<td align="right">181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">27</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
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
<td align="right">22,882</td>
<td align="right">0.2%</td>
<td align="right">14,634</td>
<td align="right">0.1%</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,891,766</td>
<td align="right">98.7%</td>
<td align="right">10,739,354</td>
<td align="right">98.9%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">107,913</td>
<td align="right">1.1%</td>
<td align="right">107,977</td>
<td align="right">1.0%</td>
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
<td align="right">699</td>
<td align="right">50.1%</td>
<td align="right">539</td>
<td align="right">43.7%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">697</td>
<td align="right">49.9%</td>
<td align="right">695</td>
<td align="right">56.3%</td>
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
<td align="left">subscr deque</td>
<td align="right">91</td>
<td align="right">13.1%</td>
<td align="right">86</td>
<td align="right">12.4%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">293</td>
<td align="right">42.0%</td>
<td align="right">296</td>
<td align="right">42.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">26.8%</td>
<td align="right">187</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">9.5%</td>
<td align="right">66</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">58</td>
<td align="right">8.3%</td>
<td align="right">58</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
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
<td align="right">14,139</td>
<td align="right">100.0%</td>
<td align="right">14,139</td>
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
<td align="right">22,754,959</td>
<td align="right">100.0%</td>
<td align="right">24,331,314</td>
<td align="right">100.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,947</td>
<td align="right">0.0%</td>
<td align="right">1,992</td>
<td align="right">0.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">790</td>
<td align="right">0.0%</td>
<td align="right">790</td>
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
<td align="right">3,347</td>
<td align="right">100.0%</td>
<td align="right">3,360</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">42</td>
<td align="right">23.2%</td>
<td align="right">42</td>
<td align="right">23.2%</td>
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
<td align="right">139</td>
<td align="right">100.0%</td>
<td align="right">139</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,491</td>
<td align="right">0.4%</td>
<td align="right">15,317</td>
<td align="right">0.3%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">723,155</td>
<td align="right">14.7%</td>
<td align="right">797,764</td>
<td align="right">15.3%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,187,303</td>
<td align="right">84.9%</td>
<td align="right">4,392,960</td>
<td align="right">84.4%</td>
<td align="right">4.9%</td>
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
<td align="right">658</td>
<td align="right">38.9%</td>
<td align="right">547</td>
<td align="right">37.6%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,035</td>
<td align="right">61.1%</td>
<td align="right">908</td>
<td align="right">62.4%</td>
<td align="right">-12.3%</td>
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
<td align="left">float long</td>
<td align="right">744</td>
<td align="right">71.9%</td>
<td align="right">614</td>
<td align="right">67.6%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">152</td>
<td align="right">14.7%</td>
<td align="right">155</td>
<td align="right">17.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">9.2%</td>
<td align="right">95</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.3%</td>
<td align="right">44</td>
<td align="right">4.8%</td>
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
<td align="right">1,645,797</td>
<td align="right">100.0%</td>
<td align="right">1,765,735</td>
<td align="right">100.0%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">264</td>
<td align="right">0.0%</td>
<td align="right">264</td>
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
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">84.3%</td>
<td align="right">43</td>
<td align="right">84.3%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,855,689</td>
<td align="right">92.7%</td>
<td align="right">12,026,720</td>
<td align="right">92.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">939,088</td>
<td align="right">7.3%</td>
<td align="right">939,088</td>
<td align="right">7.2%</td>
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
<td align="right">50</td>
<td align="right">9.3%</td>
<td align="right">49</td>
<td align="right">9.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.7%</td>
<td align="right">488</td>
<td align="right">90.9%</td>
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
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="left">list</td>
<td align="right">2,219,851</td>
<td align="right">2,219,851 / 0 !!</td>
<td align="right">2,391,158</td>
<td align="right">2,391,158 / 0 !!</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">992,909</td>
<td align="right">992,909 / 0 !!</td>
<td align="right">1,044,277</td>
<td align="right">1,044,277 / 0 !!</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
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
<td align="right">7,529,668</td>
<td align="right">16.3%</td>
<td align="right">8,133,261</td>
<td align="right">16.6%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,217,355</td>
<td align="right">82.8%</td>
<td align="right">40,438,576</td>
<td align="right">82.6%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,576</td>
<td align="right">0.9%</td>
<td align="right">398,365</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">11,727</td>
<td align="right">63.1%</td>
<td align="right">11,761</td>
<td align="right">63.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,868</td>
<td align="right">36.9%</td>
<td align="right">6,880</td>
<td align="right">36.9%</td>
<td align="right">0.2%</td>
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
<td align="right">859</td>
<td align="right">12.5%</td>
<td align="right">831</td>
<td align="right">12.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,618</td>
<td align="right">23.6%</td>
<td align="right">1,642</td>
<td align="right">23.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,516</td>
<td align="right">22.1%</td>
<td align="right">1,507</td>
<td align="right">21.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">9.9%</td>
<td align="right">681</td>
<td align="right">9.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
<td align="right">19,188,274</td>
<td align="right">100.0%</td>
<td align="right">20,506,766</td>
<td align="right">100.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">818</td>
<td align="right">0.0%</td>
<td align="right">847</td>
<td align="right">0.0%</td>
<td align="right">3.5%</td>
</tr>
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
<td align="right">9</td>
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
<td align="right">238</td>
<td align="right">0.0%</td>
<td align="right">238</td>
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
<td align="right">2,385</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,971,358</td>
<td align="right">100.0%</td>
<td align="right">2,159,829</td>
<td align="right">100.0%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">4,805,297</td>
<td align="right">95.2%</td>
<td align="right">5,147,963</td>
<td align="right">95.5%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,941</td>
<td align="right">1.6%</td>
<td align="right">79,940</td>
<td align="right">1.5%</td>
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
<td align="right">160,377</td>
<td align="right">3.2%</td>
<td align="right">160,377</td>
<td align="right">3.0%</td>
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
<td align="right">3,992</td>
<td align="right">84.3%</td>
<td align="right">3,991</td>
<td align="right">84.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">744</td>
<td align="right">15.7%</td>
<td align="right">744</td>
<td align="right">15.7%</td>
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
<td align="right">827</td>
<td align="right">111.2%</td>
<td align="right">847</td>
<td align="right">113.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">11</td>
<td align="right">1.5%</td>
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
<td align="right">1,707,536</td>
<td align="right">98.8%</td>
<td align="right">1,826,910</td>
<td align="right">98.8%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,263</td>
<td align="right">1.2%</td>
<td align="right">21,262</td>
<td align="right">1.2%</td>
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
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.2%</td>
<td align="right">187</td>
<td align="right">91.7%</td>
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
<td align="left">py simple</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">11,081,822</td>
<td align="right">94.9%</td>
<td align="right">12,025,347</td>
<td align="right">95.2%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">599,272</td>
<td align="right">5.1%</td>
<td align="right">602,393</td>
<td align="right">4.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">882</td>
<td align="right">65.8%</td>
<td align="right">865</td>
<td align="right">65.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">458</td>
<td align="right">34.2%</td>
<td align="right">460</td>
<td align="right">34.7%</td>
<td align="right">0.4%</td>
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
<td align="left">mapping</td>
<td align="right">322</td>
<td align="right">36.5%</td>
<td align="right">309</td>
<td align="right">35.7%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">151</td>
<td align="right">17.1%</td>
<td align="right">147</td>
<td align="right">17.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.3%</td>
<td align="right">232</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.6%</td>
<td align="right">111</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.5%</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">2,099,007</td>
<td align="right">100.0%</td>
<td align="right">2,133,222</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,890,288</td>
<td align="right">3.1%</td>
<td align="right">13,733,326</td>
<td align="right">3.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">168,684,326</td>
<td align="right">41.0%</td>
<td align="right">178,220,260</td>
<td align="right">41.0%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">229,563,123</td>
<td align="right">55.8%</td>
<td align="right">242,263,152</td>
<td align="right">55.7%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">603,387</td>
<td align="right">0.1%</td>
<td align="right">589,749</td>
<td align="right">0.1%</td>
<td align="right">-2.3%</td>
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
<td align="right">723,155</td>
<td align="right">7.2%</td>
<td align="right">797,764</td>
<td align="right">7.5%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,529,668</td>
<td align="right">75.2%</td>
<td align="right">8,133,261</td>
<td align="right">76.0%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">818</td>
<td align="right">0.0%</td>
<td align="right">847</td>
<td align="right">0.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,947</td>
<td align="right">0.0%</td>
<td align="right">1,992</td>
<td align="right">0.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">599,272</td>
<td align="right">6.0%</td>
<td align="right">602,393</td>
<td align="right">5.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">107,913</td>
<td align="right">1.1%</td>
<td align="right">107,977</td>
<td align="right">1.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,263</td>
<td align="right">0.2%</td>
<td align="right">21,262</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,941</td>
<td align="right">0.8%</td>
<td align="right">79,940</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,088</td>
<td align="right">9.4%</td>
<td align="right">939,088</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
<td align="right">14,139</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">11,294</td>
<td align="right">1.9%</td>
<td align="right">7,134</td>
<td align="right">1.2%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">11,588</td>
<td align="right">1.9%</td>
<td align="right">7,500</td>
<td align="right">1.3%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">21,490</td>
<td align="right">3.6%</td>
<td align="right">15,316</td>
<td align="right">2.6%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">337,824</td>
<td align="right">56.0%</td>
<td align="right">338,611</td>
<td align="right">57.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,708</td>
<td align="right">8.2%</td>
<td align="right">49,710</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">26.6%</td>
<td align="right">160,377</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.6%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">397</td>
<td align="right">0.1%</td>
<td align="right">397</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">152</td>
<td align="right">0.0%</td>
<td align="right">152</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">483,905</td>
<td align="right">1.6%</td>
<td align="right">518,179</td>
<td align="right">1.6%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">26,012,140</td>
<td align="right">83.8%</td>
<td align="right">27,658,137</td>
<td align="right">84.6%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">22,686,068</td>
<td align="right">73.1%</td>
<td align="right">24,040,787</td>
<td align="right">73.6%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,923,897</td>
<td align="right">25.5%</td>
<td align="right">8,215,175</td>
<td align="right">25.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,923,955</td>
<td align="right">25.5%</td>
<td align="right">8,215,233</td>
<td align="right">25.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,351,330</td>
<td align="right">26.9%</td>
<td align="right">8,642,608</td>
<td align="right">26.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,351,330</td>
<td align="right">26.9%</td>
<td align="right">8,642,608</td>
<td align="right">26.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,706</td>
<td align="right">0.1%</td>
<td align="right">17,761</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.4%</td>
<td align="right">427,375</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">456,471</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.4%</td>
<td align="right">441,508</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">118,293</td>
<td align="right"></td>
<td align="right">206,672</td>
<td align="right"></td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">266,921</td>
<td align="right"></td>
<td align="right">360,123</td>
<td align="right"></td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,566,508</td>
<td align="right"></td>
<td align="right">1,703,574</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">10,844,740</td>
<td align="right"></td>
<td align="right">11,665,257</td>
<td align="right"></td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">909,745</td>
<td align="right">0.3%</td>
<td align="right">978,460</td>
<td align="right">0.3%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,697,416</td>
<td align="right">2.3%</td>
<td align="right">6,071,893</td>
<td align="right">2.4%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">51,068,569</td>
<td align="right">21.0%</td>
<td align="right">54,407,198</td>
<td align="right">21.3%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">25,066,514</td>
<td align="right"></td>
<td align="right">26,593,251</td>
<td align="right"></td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">25,064,749</td>
<td align="right">66.2%</td>
<td align="right">26,591,211</td>
<td align="right">66.6%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,671,202</td>
<td align="right"></td>
<td align="right">11,317,445</td>
<td align="right"></td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">84,469,924</td>
<td align="right">34.7%</td>
<td align="right">88,934,627</td>
<td align="right">34.9%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">84,552,652</td>
<td align="right">30.5%</td>
<td align="right">88,829,376</td>
<td align="right">30.7%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,096,886</td>
<td align="right"></td>
<td align="right">14,763,820</td>
<td align="right"></td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,658,337</td>
<td align="right">33.4%</td>
<td align="right">13,205,690</td>
<td align="right">33.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,779,529</td>
<td align="right">33.8%</td>
<td align="right">13,326,880</td>
<td align="right">33.4%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">136,284,285</td>
<td align="right">49.1%</td>
<td align="right">141,816,046</td>
<td align="right">49.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">102,220,231</td>
<td align="right">42.0%</td>
<td align="right">105,712,914</td>
<td align="right">41.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">148,881</td>
<td align="right"></td>
<td align="right">153,700</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,667,593</td>
<td align="right">20.1%</td>
<td align="right">57,268,154</td>
<td align="right">19.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,584</td>
<td align="right">0.1%</td>
<td align="right">43,582</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,608</td>
<td align="right">0.2%</td>
<td align="right">77,608</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">280</td>
<td align="right">11,537</td>
<td align="right">737</td>
<td align="right">794</td>
<td align="right">1</td>
<td align="right">280</td>
<td align="right">11,537</td>
<td align="right">737</td>
<td align="right">794</td>
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
<td align="right">14</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">86</td>
<td align="right">2.7%</td>
<td align="right">95</td>
<td align="right">3.0%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,775,502</td>
<td align="right"></td>
<td align="right">3,042,738</td>
<td align="right"></td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">248,329,023</td>
<td align="right">8,947.2%</td>
<td align="right">265,645,349</td>
<td align="right">8,730.5%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,311</td>
<td align="right">41.9%</td>
<td align="right">1,351</td>
<td align="right">42.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,132</td>
<td align="right"></td>
<td align="right">3,217</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,523</td>
<td align="right">48.6%</td>
<td align="right">1,559</td>
<td align="right">48.5%</td>
<td align="right">2.4%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">212</td>
<td align="right">6.8%</td>
<td align="right">212</td>
<td align="right">6.6%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">86</td>
<td align="right"></td>
<td align="right">95</td>
<td align="right"></td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">86</td>
<td align="right">100.0%</td>
<td align="right">95</td>
<td align="right">100.0%</td>
<td align="right">10.5%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">2,341,617</td>
<td align="right">90.3%</td>
<td align="right">2,105,687</td>
<td align="right">89.7%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,592,768</td>
<td align="right"></td>
<td align="right">2,347,008</td>
<td align="right"></td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">52,192</td>
<td align="right">2.0%</td>
<td align="right">50,000</td>
<td align="right">2.1%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">198,959</td>
<td align="right">7.7%</td>
<td align="right">191,321</td>
<td align="right">8.2%</td>
<td align="right">-3.8%</td>
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
<td align="left"><= 8,192</td>
<td align="left">12</td>
<td align="right">14.0%</td>
<td align="left">18</td>
<td align="right">18.9%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">25.6%</td>
<td align="left">23</td>
<td align="right">24.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">26</td>
<td align="right">30.2%</td>
<td align="left">36</td>
<td align="right">37.9%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">26</td>
<td align="right">30.2%</td>
<td align="left">18</td>
<td align="right">18.9%</td>
<td align="right">-30.8%</td>
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
<td align="right">12</td>
<td align="right">14.0%</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21</td>
<td align="right">24.4%</td>
<td align="right">21</td>
<td align="right">22.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2</td>
<td align="right">2.3%</td>
<td align="right">2</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">25</td>
<td align="right">29.1%</td>
<td align="right">36</td>
<td align="right">37.9%</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">26</td>
<td align="right">30.2%</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">-30.8%</td>
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
<td align="left"><= 32</td>
<td align="right">12</td>
<td align="right">14.0%</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">25.6%</td>
<td align="right">22</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13</td>
<td align="right">15.1%</td>
<td align="right">19</td>
<td align="right">20.0%</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">25</td>
<td align="right">29.1%</td>
<td align="right">26</td>
<td align="right">27.4%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">14</td>
<td align="right">16.3%</td>
<td align="right">10</td>
<td align="right">10.5%</td>
<td align="right">-28.6%</td>
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
<td align="left">_DEOPT</td>
<td align="right">153,929</td>
<td align="right">177,109</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">405,688</td>
<td align="right">466,689</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">405,688</td>
<td align="right">466,689</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">98,003</td>
<td align="right">112,609</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">98,003</td>
<td align="right">112,609</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">98,094</td>
<td align="right">112,711</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">98,094</td>
<td align="right">112,711</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">98,094</td>
<td align="right">112,711</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">781,129</td>
<td align="right">893,092</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">767,568</td>
<td align="right">876,989</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">571,471</td>
<td align="right">651,669</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">361,880</td>
<td align="right">410,300</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,805,703</td>
<td align="right">2,045,775</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,805,703</td>
<td align="right">2,045,775</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">903,048</td>
<td align="right">1,021,638</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">2,345,769</td>
<td align="right">2,646,541</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">2,191,845</td>
<td align="right">2,469,432</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,400,413</td>
<td align="right">1,576,587</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">693,457</td>
<td align="right">780,269</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,953,677</td>
<td align="right">2,196,012</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">595,454</td>
<td align="right">667,660</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,522,383</td>
<td align="right">1,705,178</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,160,503</td>
<td align="right">1,294,878</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">166,665</td>
<td align="right">185,862</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,458,205</td>
<td align="right">3,830,324</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,169,979</td>
<td align="right">2,394,573</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,169,979</td>
<td align="right">2,394,573</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,068,111</td>
<td align="right">2,277,931</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">6,549,346</td>
<td align="right">7,209,793</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,456,732</td>
<td align="right">1,602,510</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,808,099</td>
<td align="right">1,984,273</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,775,502</td>
<td align="right">3,042,738</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,404,607</td>
<td align="right">1,537,805</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">3,695,769</td>
<td align="right">4,044,551</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,621,573</td>
<td align="right">2,865,629</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,310,739</td>
<td align="right">1,429,324</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,341,887</td>
<td align="right">3,628,159</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">971,191</td>
<td align="right">1,051,228</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,406,503</td>
<td align="right">1,521,685</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,018,134</td>
<td align="right">2,182,918</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,614,072</td>
<td align="right">3,905,424</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">3,614,072</td>
<td align="right">3,905,424</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,614,072</td>
<td align="right">3,905,424</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,614,072</td>
<td align="right">3,905,424</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,742,540</td>
<td align="right">1,881,674</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,215,785</td>
<td align="right">2,391,959</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">805,408</td>
<td align="right">866,248</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,116,712</td>
<td align="right">3,350,475</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">817,493</td>
<td align="right">878,494</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,070,818</td>
<td align="right">1,147,606</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">43,215,086</td>
<td align="right">46,279,589</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,040,457</td>
<td align="right">5,396,020</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">38,312,099</td>
<td align="right">40,894,962</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">900,927</td>
<td align="right">958,516</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,087,846</td>
<td align="right">4,344,798</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">701,786</td>
<td align="right">745,615</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,957,937</td>
<td align="right">6,320,105</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,315,861</td>
<td align="right">2,445,658</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,477,378</td>
<td align="right">5,767,070</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,284,709</td>
<td align="right">1,350,289</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,335,069</td>
<td align="right">1,402,525</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">671,563</td>
<td align="right">705,377</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,876,600</td>
<td align="right">1,971,082</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">603,783</td>
<td align="right">633,006</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,859,558</td>
<td align="right">1,948,323</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,859,558</td>
<td align="right">1,948,323</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">7,804,782</td>
<td align="right">8,114,372</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,684,429</td>
<td align="right">1,749,848</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">569,350</td>
<td align="right">588,547</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">569,350</td>
<td align="right">588,547</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">566,385</td>
<td align="right">585,421</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">569,621</td>
<td align="right">588,657</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">569,621</td>
<td align="right">588,657</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">505,780</td>
<td align="right">520,397</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">505,780</td>
<td align="right">520,397</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">505,780</td>
<td align="right">520,397</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">505,689</td>
<td align="right">520,295</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">509,820</td>
<td align="right">524,438</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,964,412</td>
<td align="right">7,143,039</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,964,412</td>
<td align="right">7,143,039</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">909,347</td>
<td align="right">923,964</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">913,466</td>
<td align="right">928,086</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,124,076</td>
<td align="right">2,138,682</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,528,525</td>
<td align="right">2,543,131</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,720</td>
<td align="right">399,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,215,092</td>
<td align="right">1,214,931</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INSERT_NULL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">812,135</td>
<td align="right">812,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
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
<td align="right">214</td>
<td align="right">214</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-03
