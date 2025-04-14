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
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">87,034</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,599</td>
<td align="right">168,813</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">423,192</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,637</td>
<td align="right">115,812</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,439,595</td>
<td align="right">1,871,412</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,609,089</td>
<td align="right">1,988,828</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,143,477</td>
<td align="right">719,384</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,255,303</td>
<td align="right">809,053</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,895,901</td>
<td align="right">1,990,278</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,516,985</td>
<td align="right">13,455,607</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,550,497</td>
<td align="right">2,659,781</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,847,140</td>
<td align="right">1,393,253</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,321,989</td>
<td align="right">16,214,600</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,080,902</td>
<td align="right">2,529,741</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,020,764</td>
<td align="right">1,596,671</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">27,862,211</td>
<td align="right">22,535,786</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,302,681</td>
<td align="right">10,052,780</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">96,894</td>
<td align="right">89,862</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,833,286</td>
<td align="right">11,990,868</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">368,557</td>
<td align="right">392,694</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">754,477</td>
<td align="right">710,288</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,293,782</td>
<td align="right">1,223,417</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">538,463</td>
<td align="right">509,280</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,110,704</td>
<td align="right">1,050,792</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,097,947</td>
<td align="right">1,039,560</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">369,170</td>
<td align="right">350,450</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">393,118</td>
<td align="right">373,295</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">919,733</td>
<td align="right">873,377</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">393,441</td>
<td align="right">373,618</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,848,002</td>
<td align="right">3,656,734</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">377,484</td>
<td align="right">358,764</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">783,419</td>
<td align="right">744,870</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,051</td>
<td align="right">4,803</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">5,138,231</td>
<td align="right">4,888,346</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">197,117</td>
<td align="right">187,680</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">587,840</td>
<td align="right">559,718</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,492,726</td>
<td align="right">1,421,864</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">592,181</td>
<td align="right">564,104</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">619,932</td>
<td align="right">590,719</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,520,975</td>
<td align="right">1,450,113</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,558,796</td>
<td align="right">1,487,934</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,685,030</td>
<td align="right">7,339,555</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,274,376</td>
<td align="right">1,217,243</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,172,240</td>
<td align="right">1,120,496</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,978,161</td>
<td align="right">2,847,432</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">214,847</td>
<td align="right">205,487</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,429,676</td>
<td align="right">1,367,526</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,399,494</td>
<td align="right">1,339,300</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,627,417</td>
<td align="right">6,342,546</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,608,916</td>
<td align="right">4,412,491</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">220,763</td>
<td align="right">211,379</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">68,388,670</td>
<td align="right">65,491,312</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,224,786</td>
<td align="right">9,792,326</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">766,439</td>
<td align="right">734,141</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,276,238</td>
<td align="right">10,803,113</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,375,443</td>
<td align="right">5,161,311</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">216,783</td>
<td align="right">208,511</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,119,543</td>
<td align="right">12,624,007</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,803,945</td>
<td align="right">2,698,222</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,816,432</td>
<td align="right">2,711,733</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,101,711</td>
<td align="right">3,949,373</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,911,175</td>
<td align="right">14,369,387</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,566,506</td>
<td align="right">1,509,748</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,150,272</td>
<td align="right">6,892,794</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,490,611</td>
<td align="right">24,601,141</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,441,957</td>
<td align="right">6,221,321</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,674,356</td>
<td align="right">3,549,055</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">766,270</td>
<td align="right">740,467</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,865,134</td>
<td align="right">1,805,776</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,702,206</td>
<td align="right">3,587,103</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">973,331</td>
<td align="right">944,124</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,667,408</td>
<td align="right">2,590,232</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">104</td>
<td align="right">107</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,017,084</td>
<td align="right">987,882</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,334,722</td>
<td align="right">1,296,457</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,889,642</td>
<td align="right">5,722,040</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">341,669</td>
<td align="right">332,259</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,764,349</td>
<td align="right">6,596,600</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,612,539</td>
<td align="right">2,549,041</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">204,935</td>
<td align="right">200,791</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">595,739</td>
<td align="right">583,896</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,434,001</td>
<td align="right">8,268,960</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,448</td>
<td align="right">13,200</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,671</td>
<td align="right">17,423</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,671</td>
<td align="right">17,423</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">682,092</td>
<td align="right">672,735</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">343</td>
<td align="right">346</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,630,977</td>
<td align="right">4,592,663</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,686</td>
<td align="right">453,081</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,613</td>
<td align="right">1,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,387</td>
<td align="right">102,097</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">108,851</td>
<td align="right">108,598</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,548</td>
<td align="right">4,539</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,397</td>
<td align="right">97,313</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,427</td>
<td align="right">46,406</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,577</td>
<td align="right">16,571</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,212</td>
<td align="right">3,213</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,045</td>
<td align="right">34,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,132</td>
<td align="right">35,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,841</td>
<td align="right">928,778</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,017</td>
<td align="right">191,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,706</td>
<td align="right">1,818,682</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,672</td>
<td align="right">426,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">105,142</td>
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
<td align="right">86,432</td>
<td align="right">86,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">84,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,659</td>
<td align="right">81,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">77,368</td>
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
<td align="right">67,589</td>
<td align="right">67,589</td>
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
<td align="right">59,119</td>
<td align="right">59,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,866</td>
<td align="right">55,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,862</td>
<td align="right">55,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,904</td>
<td align="right">42,904</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,559</td>
<td align="right">29,559</td>
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
<td align="right">21,938</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,469</td>
<td align="right">21,469</td>
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
<td align="right">17,858</td>
<td align="right">17,858</td>
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
<td align="right">14,143</td>
<td align="right">14,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286</td>
<td align="right">10,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,870</td>
<td align="right">9,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">8,491</td>
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
<td align="right">806</td>
<td align="right">806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">543</td>
<td align="right">543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">485</td>
<td align="right">485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">267</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">154</td>
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
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
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
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE_KNOWN</td>
<td align="right"></td>
<td align="right">90,510</td>
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
<td align="right">14,752</td>
<td align="right">0.1%</td>
<td align="right">22,556</td>
<td align="right">0.2%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,820,152</td>
<td align="right">98.8%</td>
<td align="right">9,356,012</td>
<td align="right">98.6%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">107,900</td>
<td align="right">1.1%</td>
<td align="right">107,656</td>
<td align="right">1.1%</td>
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
<td align="right">542</td>
<td align="right">44.0%</td>
<td align="right">691</td>
<td align="right">50.3%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">691</td>
<td align="right">56.0%</td>
<td align="right">682</td>
<td align="right">49.7%</td>
<td align="right">-1.3%</td>
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
<td align="right">142</td>
<td align="right">20.5%</td>
<td align="right">134</td>
<td align="right">19.6%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">293</td>
<td align="right">42.4%</td>
<td align="right">292</td>
<td align="right">42.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">27.1%</td>
<td align="right">187</td>
<td align="right">27.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">9.6%</td>
<td align="right">66</td>
<td align="right">9.7%</td>
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
<tr>
<td align="left">subscr list slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">14,143</td>
<td align="right">100.0%</td>
<td align="right">14,143</td>
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
<td align="right">23,307,986</td>
<td align="right">100.0%</td>
<td align="right">22,420,571</td>
<td align="right">100.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,994</td>
<td align="right">0.0%</td>
<td align="right">2,004</td>
<td align="right">0.0%</td>
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
<td align="right">795</td>
<td align="right">0.0%</td>
<td align="right">795</td>
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
<td align="right">3,349</td>
<td align="right">100.0%</td>
<td align="right">3,330</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">15,347</td>
<td align="right">0.3%</td>
<td align="right">21,218</td>
<td align="right">0.4%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">753,327</td>
<td align="right">15.0%</td>
<td align="right">709,012</td>
<td align="right">14.5%</td>
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
<td align="right">4,261,069</td>
<td align="right">84.7%</td>
<td align="right">4,143,102</td>
<td align="right">85.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">545</td>
<td align="right">38.1%</td>
<td align="right">654</td>
<td align="right">39.2%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">884</td>
<td align="right">61.9%</td>
<td align="right">1,013</td>
<td align="right">60.8%</td>
<td align="right">14.6%</td>
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
<td align="right">591</td>
<td align="right">66.9%</td>
<td align="right">721</td>
<td align="right">71.2%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">152</td>
<td align="right">17.2%</td>
<td align="right">151</td>
<td align="right">14.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">10.9%</td>
<td align="right">96</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">44</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
<td align="right">1,688,790</td>
<td align="right">100.0%</td>
<td align="right">1,620,478</td>
<td align="right">100.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">270</td>
<td align="right">0.0%</td>
<td align="right">270</td>
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
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">82.7%</td>
<td align="right">43</td>
<td align="right">82.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">939,093</td>
<td align="right">7.3%</td>
<td align="right">115,483</td>
<td align="right">1.6%</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,872,870</td>
<td align="right">92.7%</td>
<td align="right">7,224,302</td>
<td align="right">98.4%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">232</td>
<td align="right">0.0%</td>
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
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">89.7%</td>
<td align="right">276</td>
<td align="right">83.4%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">56</td>
<td align="right">10.3%</td>
<td align="right">55</td>
<td align="right">16.6%</td>
<td align="right">-1.8%</td>
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
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">7,673,914</td>
<td align="right">16.3%</td>
<td align="right">7,328,393</td>
<td align="right">16.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,888,254</td>
<td align="right">82.8%</td>
<td align="right">37,640,887</td>
<td align="right">83.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">387,785</td>
<td align="right">0.8%</td>
<td align="right">382,807</td>
<td align="right">0.8%</td>
<td align="right">-1.3%</td>
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
<td align="left">Failure</td>
<td align="right">6,604</td>
<td align="right">36.4%</td>
<td align="right">6,676</td>
<td align="right">36.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,529</td>
<td align="right">63.6%</td>
<td align="right">11,425</td>
<td align="right">63.1%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">844</td>
<td align="right">12.8%</td>
<td align="right">880</td>
<td align="right">13.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,576</td>
<td align="right">23.9%</td>
<td align="right">1,587</td>
<td align="right">23.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,343</td>
<td align="right">20.3%</td>
<td align="right">1,350</td>
<td align="right">20.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">10.3%</td>
<td align="right">681</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">460</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.1%</td>
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
<td align="right">19,561,257</td>
<td align="right">100.0%</td>
<td align="right">18,845,085</td>
<td align="right">100.0%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">834</td>
<td align="right">0.0%</td>
<td align="right">843</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
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
<td align="right">243</td>
<td align="right">0.0%</td>
<td align="right">243</td>
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
<td align="right">2,384</td>
<td align="right">100.0%</td>
<td align="right">2,376</td>
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
<td align="right">2,038,456</td>
<td align="right">100.0%</td>
<td align="right">1,931,580</td>
<td align="right">100.0%</td>
<td align="right">-5.2%</td>
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
<td align="right">4,877,964</td>
<td align="right">95.6%</td>
<td align="right">4,685,144</td>
<td align="right">95.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,937</td>
<td align="right">1.6%</td>
<td align="right">79,937</td>
<td align="right">1.6%</td>
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
<td align="right">140,400</td>
<td align="right">2.8%</td>
<td align="right">140,400</td>
<td align="right">2.9%</td>
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
<td align="right">3,615</td>
<td align="right">83.0%</td>
<td align="right">3,615</td>
<td align="right">83.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.0%</td>
<td align="right">743</td>
<td align="right">17.0%</td>
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
<td align="right">798</td>
<td align="right">107.4%</td>
<td align="right">814</td>
<td align="right">109.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">344</td>
<td align="right">46.3%</td>
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
<td align="right">10</td>
<td align="right">1.3%</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
<td align="right">1,749,782</td>
<td align="right">98.8%</td>
<td align="right">1,686,033</td>
<td align="right">98.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,264</td>
<td align="right">1.2%</td>
<td align="right">21,264</td>
<td align="right">1.2%</td>
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
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.2%</td>
<td align="right">187</td>
<td align="right">91.2%</td>
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
<td align="right">11,393,136</td>
<td align="right">95.0%</td>
<td align="right">10,854,391</td>
<td align="right">94.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">594,418</td>
<td align="right">5.0%</td>
<td align="right">582,582</td>
<td align="right">5.1%</td>
<td align="right">-2.0%</td>
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
<td align="left">Success</td>
<td align="right">462</td>
<td align="right">35.0%</td>
<td align="right">458</td>
<td align="right">34.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">859</td>
<td align="right">65.0%</td>
<td align="right">856</td>
<td align="right">65.1%</td>
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
<td align="left">sequence</td>
<td align="right">145</td>
<td align="right">16.9%</td>
<td align="right">131</td>
<td align="right">15.3%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">304</td>
<td align="right">35.4%</td>
<td align="right">315</td>
<td align="right">36.8%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">27.0%</td>
<td align="right">232</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.9%</td>
<td align="right">111</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">2,110,612</td>
<td align="right">100.0%</td>
<td align="right">2,091,829</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">171,393,767</td>
<td align="right">41.0%</td>
<td align="right">142,031,192</td>
<td align="right">39.6%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">236,166,929</td>
<td align="right">56.5%</td>
<td align="right">206,564,329</td>
<td align="right">57.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">10,209,487</td>
<td align="right">2.4%</td>
<td align="right">9,407,086</td>
<td align="right">2.6%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">559,352</td>
<td align="right">0.1%</td>
<td align="right">568,510</td>
<td align="right">0.2%</td>
<td align="right">1.6%</td>
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
<td align="right">939,093</td>
<td align="right">9.2%</td>
<td align="right">115,483</td>
<td align="right">1.2%</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">753,327</td>
<td align="right">7.4%</td>
<td align="right">709,012</td>
<td align="right">7.6%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,673,914</td>
<td align="right">75.3%</td>
<td align="right">7,328,393</td>
<td align="right">78.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">594,418</td>
<td align="right">5.8%</td>
<td align="right">582,582</td>
<td align="right">6.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,994</td>
<td align="right">0.0%</td>
<td align="right">2,004</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">107,900</td>
<td align="right">1.1%</td>
<td align="right">107,656</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.8%</td>
<td align="right">79,937</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
<td align="right">14,143</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">834</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">422,986</td>
<td align="right">4.5%</td>
<td align="right"></td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">7,477</td>
<td align="right">1.3%</td>
<td align="right">11,444</td>
<td align="right">2.0%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">7,275</td>
<td align="right">1.3%</td>
<td align="right">11,112</td>
<td align="right">2.0%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">15,346</td>
<td align="right">2.7%</td>
<td align="right">21,217</td>
<td align="right">3.7%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">318,367</td>
<td align="right">56.9%</td>
<td align="right">313,387</td>
<td align="right">55.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,386</td>
<td align="right">10.6%</td>
<td align="right">59,388</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">25.1%</td>
<td align="right">140,400</td>
<td align="right">24.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.8%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
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
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">232</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">500,674</td>
<td align="right">1.6%</td>
<td align="right">480,843</td>
<td align="right">1.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">26,598,430</td>
<td align="right">84.1%</td>
<td align="right">25,660,940</td>
<td align="right">83.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,185,330</td>
<td align="right">73.3%</td>
<td align="right">22,412,881</td>
<td align="right">73.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,010,921</td>
<td align="right">25.3%</td>
<td align="right">7,845,650</td>
<td align="right">25.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,010,980</td>
<td align="right">25.3%</td>
<td align="right">7,845,709</td>
<td align="right">25.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,438,359</td>
<td align="right">26.7%</td>
<td align="right">8,273,318</td>
<td align="right">27.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,438,359</td>
<td align="right">26.7%</td>
<td align="right">8,273,318</td>
<td align="right">27.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,686</td>
<td align="right">0.1%</td>
<td align="right">17,438</td>
<td align="right">0.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.4%</td>
<td align="right">427,609</td>
<td align="right">1.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">17</td>
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
<td align="right">1.4%</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.4%</td>
<td align="right">441,509</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">66,995</td>
<td align="right"></td>
<td align="right">36,257</td>
<td align="right"></td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">131,244</td>
<td align="right"></td>
<td align="right">78,057</td>
<td align="right"></td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">64,533</td>
<td align="right"></td>
<td align="right">42,104</td>
<td align="right"></td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">95,804,402</td>
<td align="right">21.4%</td>
<td align="right">112,011,602</td>
<td align="right">25.2%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">98,102,056</td>
<td align="right">26.3%</td>
<td align="right">112,309,994</td>
<td align="right">30.3%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">83,274,913</td>
<td align="right">18.6%</td>
<td align="right">73,103,759</td>
<td align="right">16.5%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">62,832,772</td>
<td align="right">16.9%</td>
<td align="right">56,809,532</td>
<td align="right">15.4%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">191,251,284</td>
<td align="right">42.7%</td>
<td align="right">176,069,181</td>
<td align="right">39.7%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">155,018,941</td>
<td align="right">41.6%</td>
<td align="right">142,844,130</td>
<td align="right">38.6%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">78,087,538</td>
<td align="right">17.4%</td>
<td align="right">82,789,450</td>
<td align="right">18.6%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,614,804</td>
<td align="right"></td>
<td align="right">1,537,676</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">11,141,875</td>
<td align="right"></td>
<td align="right">10,654,291</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,344,187</td>
<td align="right">59.2%</td>
<td align="right">21,585,906</td>
<td align="right">59.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,345,831</td>
<td align="right"></td>
<td align="right">21,588,171</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,413,310</td>
<td align="right"></td>
<td align="right">11,067,110</td>
<td align="right"></td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">56,513,974</td>
<td align="right">15.2%</td>
<td align="right">58,097,934</td>
<td align="right">15.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,727,325</td>
<td align="right"></td>
<td align="right">16,284,627</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,246,952</td>
<td align="right">40.4%</td>
<td align="right">14,872,106</td>
<td align="right">40.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,368,135</td>
<td align="right">40.8%</td>
<td align="right">14,993,334</td>
<td align="right">41.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,600</td>
<td align="right">0.2%</td>
<td align="right">77,640</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,583</td>
<td align="right">0.1%</td>
<td align="right">43,588</td>
<td align="right">0.1%</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,918,115</td>
<td align="right"></td>
<td align="right">12,711,385</td>
<td align="right"></td>
<td align="right">335.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,327</td>
<td align="right">41.8%</td>
<td align="right">191</td>
<td align="right">24.4%</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,547</td>
<td align="right">48.8%</td>
<td align="right">300</td>
<td align="right">38.3%</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,173</td>
<td align="right"></td>
<td align="right">783</td>
<td align="right"></td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">232,605,900</td>
<td align="right">7,971.1%</td>
<td align="right">390,727,608</td>
<td align="right">3,073.8%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">13</td>
<td align="right">1.7%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">87</td>
<td align="right">2.7%</td>
<td align="right">80</td>
<td align="right">10.2%</td>
<td align="right">-8.0%</td>
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
<td align="right">6.7%</td>
<td align="right">212</td>
<td align="right">27.1%</td>
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
<td align="right">87</td>
<td align="right"></td>
<td align="right">80</td>
<td align="right"></td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">87</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">-8.0%</td>
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
<td align="right">208,608</td>
<td align="right">9.3%</td>
<td align="right">185,659</td>
<td align="right">8.2%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">1,712,288</td>
<td align="right">76.4%</td>
<td align="right">1,747,645</td>
<td align="right">77.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">319,616</td>
<td align="right">14.3%</td>
<td align="right">323,592</td>
<td align="right">14.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,240,512</td>
<td align="right"></td>
<td align="right">2,256,896</td>
<td align="right"></td>
<td align="right">0.7%</td>
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
<td align="left">16</td>
<td align="right">18.4%</td>
<td align="left">11</td>
<td align="right">13.8%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">25.3%</td>
<td align="left">23</td>
<td align="right">28.7%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">33</td>
<td align="right">37.9%</td>
<td align="left">20</td>
<td align="right">25.0%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">16</td>
<td align="right">18.4%</td>
<td align="left">23</td>
<td align="right">28.7%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">3</td>
<td align="right">3.8%</td>
<td align="right"></td>
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
<td align="right">16</td>
<td align="right">18.4%</td>
<td align="right">13</td>
<td align="right">16.2%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">25.3%</td>
<td align="right">23</td>
<td align="right">28.7%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">17</td>
<td align="right">19.5%</td>
<td align="right">10</td>
<td align="right">12.5%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">17</td>
<td align="right">19.5%</td>
<td align="right">11</td>
<td align="right">13.8%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">15</td>
<td align="right">17.2%</td>
<td align="right">22</td>
<td align="right">27.5%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">1.2%</td>
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
<td align="left"><= 32</td>
<td align="right">37</td>
<td align="right">42.5%</td>
<td align="right">32</td>
<td align="right">40.0%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">2</td>
<td align="right">2.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">17</td>
<td align="right">19.5%</td>
<td align="right">10</td>
<td align="right">12.5%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">32</td>
<td align="right">36.8%</td>
<td align="right">33</td>
<td align="right">41.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">1.2%</td>
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
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">2.5%</td>
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
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,029</td>
<td align="right">824,639</td>
<td align="right">80,039.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">109,354</td>
<td align="right">922,377</td>
<td align="right">743.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">631,385</td>
<td align="right">4,740,116</td>
<td align="right">650.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">841,073</td>
<td align="right">4,958,059</td>
<td align="right">489.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">109,455</td>
<td align="right">514,786</td>
<td align="right">370.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,751,963</td>
<td align="right">12,153,235</td>
<td align="right">341.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,918,115</td>
<td align="right">12,711,385</td>
<td align="right">335.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,533,378</td>
<td align="right">5,999,059</td>
<td align="right">291.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,492,550</td>
<td align="right">13,277,420</td>
<td align="right">280.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">166,152</td>
<td align="right">558,150</td>
<td align="right">235.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,102,811</td>
<td align="right">6,983,420</td>
<td align="right">232.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,932,074</td>
<td align="right">6,350,672</td>
<td align="right">228.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,932,074</td>
<td align="right">6,350,672</td>
<td align="right">228.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,148,308</td>
<td align="right">20,053,637</td>
<td align="right">226.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">441,495</td>
<td align="right">1,223,148</td>
<td align="right">177.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,604,504</td>
<td align="right">20,859,748</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,748,156</td>
<td align="right">8,137,090</td>
<td align="right">117.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,748,156</td>
<td align="right">8,137,090</td>
<td align="right">117.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">691,998</td>
<td align="right">1,493,010</td>
<td align="right">115.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">403,567</td>
<td align="right">811,253</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">4,371,327</td>
<td align="right">8,713,578</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,730,786</td>
<td align="right">53,667,074</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">615,470</td>
<td align="right">977,432</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">691,116</td>
<td align="right">1,084,442</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">27,058,669</td>
<td align="right">32,323,281</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,539,876</td>
<td align="right">2,945,213</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,380,484</td>
<td align="right">2,713,785</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">838,231</td>
<td align="right">763,474</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">441,495</td>
<td align="right">407,776</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,064,068</td>
<td align="right">1,908,963</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">963,425</td>
<td align="right">893,692</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,485,357</td>
<td align="right">1,379,609</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">521,930</td>
<td align="right">485,916</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">2,501,580</td>
<td align="right">2,337,072</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">2,335,430</td>
<td align="right">2,186,609</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,610,619</td>
<td align="right">1,509,877</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,882,338</td>
<td align="right">7,287,309</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,071,135</td>
<td align="right">1,953,383</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,893,043</td>
<td align="right">1,787,295</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">740,739</td>
<td align="right">700,021</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,172,468</td>
<td align="right">2,055,960</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,285,827</td>
<td align="right">2,163,370</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,285,827</td>
<td align="right">2,163,370</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,815,889</td>
<td align="right">1,721,775</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,371,113</td>
<td align="right">1,301,379</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,629,087</td>
<td align="right">3,807,291</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,476,341</td>
<td align="right">1,404,258</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,748,156</td>
<td align="right">3,570,380</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,059,750</td>
<td align="right">7,385,613</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,059,750</td>
<td align="right">7,385,613</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,300,729</td>
<td align="right">2,194,981</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,625,438</td>
<td align="right">5,878,113</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,226,226</td>
<td align="right">3,084,464</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">905,681</td>
<td align="right">865,905</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,103,586</td>
<td align="right">1,055,566</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">392,784</td>
<td align="right">376,075</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,015,048</td>
<td align="right">972,929</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,202,394</td>
<td align="right">4,993,622</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">925,497</td>
<td align="right">889,483</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,209,598</td>
<td align="right">4,052,138</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,317,356</td>
<td align="right">1,273,975</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,376,368</td>
<td align="right">2,301,984</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,904,431</td>
<td align="right">1,845,363</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,904,431</td>
<td align="right">1,845,363</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,780,494</td>
<td align="right">8,561,915</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">109,455</td>
<td align="right">107,100</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">109,455</td>
<td align="right">107,100</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">109,354</td>
<td align="right">107,005</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,931,666</td>
<td align="right">1,890,803</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">577,542</td>
<td align="right">565,537</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,374,023</td>
<td align="right">1,348,914</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">574,435</td>
<td align="right">566,035</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">577,671</td>
<td align="right">569,271</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,578</td>
<td align="right">403,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">627,377</td>
<td align="right">622,673</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,148,536</td>
<td align="right">1,141,483</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">517,141</td>
<td align="right">514,786</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">517,141</td>
<td align="right">514,786</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">521,172</td>
<td align="right">518,829</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,214,950</td>
<td align="right">1,218,555</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,135,427</td>
<td align="right">2,133,078</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
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
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
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
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
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
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN</td>
<td align="right"></td>
<td align="right">4,566,710</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_FUNCTION</td>
<td align="right"></td>
<td align="right">4,566,710</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_OFFSET</td>
<td align="right"></td>
<td align="right">4,566,710</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">4,566,710</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_YIELD_VALUE_FUNCTION</td>
<td align="right"></td>
<td align="right">4,554,786</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_YIELD_VALUE_OFFSET</td>
<td align="right"></td>
<td align="right">4,554,786</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">4,554,786</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">407,686</td>
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
Stats gathered on: 2025-02-18
