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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">564,744</td>
<td align="right">483,815</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,150,502</td>
<td align="right">988,652</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">387,117</td>
<td align="right">333,087</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,164,062</td>
<td align="right">1,002,645</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,565,505</td>
<td align="right">1,350,975</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">785,710</td>
<td align="right">678,323</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">395,430</td>
<td align="right">341,400</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,070,675</td>
<td align="right">3,519,628</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,593,751</td>
<td align="right">1,379,221</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">5,421,536</td>
<td align="right">4,692,995</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">803,964</td>
<td align="right">697,370</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,480,221</td>
<td align="right">1,284,052</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">818,668</td>
<td align="right">710,712</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">614,739</td>
<td align="right">533,710</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">206,030</td>
<td align="right">178,927</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,631,568</td>
<td align="right">1,417,038</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">410,423</td>
<td align="right">356,509</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">410,743</td>
<td align="right">356,829</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,225,782</td>
<td align="right">1,065,256</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">619,101</td>
<td align="right">538,058</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,509,962</td>
<td align="right">1,312,354</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,367,102</td>
<td align="right">1,190,667</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,345,254</td>
<td align="right">1,174,382</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">646,176</td>
<td align="right">565,235</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">977,273</td>
<td align="right">855,668</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,140,620</td>
<td align="right">2,754,234</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,902,999</td>
<td align="right">6,059,552</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,077,932</td>
<td align="right">7,091,622</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">223,810</td>
<td align="right">196,795</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">226,401</td>
<td align="right">199,296</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,644,660</td>
<td align="right">9,370,792</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">229,733</td>
<td align="right">202,724</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,774,370</td>
<td align="right">10,413,394</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,948,047</td>
<td align="right">1,731,118</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,852,744</td>
<td align="right">4,313,071</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,689,297</td>
<td align="right">12,176,759</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,008,714</td>
<td align="right">9,798,893</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,570,268</td>
<td align="right">4,976,477</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,822,762</td>
<td align="right">3,416,469</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">66,062,899</td>
<td align="right">59,042,460</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,430,026</td>
<td align="right">6,672,594</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,247,701</td>
<td align="right">3,815,104</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,915,196</td>
<td align="right">2,618,858</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,670,183</td>
<td align="right">5,999,460</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,620,033</td>
<td align="right">1,458,007</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,926,201</td>
<td align="right">1,734,882</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,903,385</td>
<td align="right">2,624,978</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,397,319</td>
<td align="right">13,930,129</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">26,299,417</td>
<td align="right">23,817,015</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,998,700</td>
<td align="right">2,720,055</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,133,239</td>
<td align="right">1,939,835</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,303,872</td>
<td align="right">12,099,863</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,748,099</td>
<td align="right">2,504,982</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,095,815</td>
<td align="right">5,567,788</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,290,545</td>
<td align="right">1,182,609</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,849,852</td>
<td align="right">3,537,572</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">999,604</td>
<td align="right">918,681</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,737,886</td>
<td align="right">2,522,026</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,370,601</td>
<td align="right">1,262,694</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,043,318</td>
<td align="right">962,410</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">794,204</td>
<td align="right">732,705</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">350,623</td>
<td align="right">323,623</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">28,599,773</td>
<td align="right">26,408,968</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,957,258</td>
<td align="right">20,290,803</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,969,219</td>
<td align="right">17,613,447</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">106,897</td>
<td align="right">99,389</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,927,187</td>
<td align="right">6,481,319</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,042,736</td>
<td align="right">4,745,778</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,621,695</td>
<td align="right">3,425,350</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,599,754</td>
<td align="right">8,141,113</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">105</td>
<td align="right">110</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">691,061</td>
<td align="right">664,044</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,735,760</td>
<td align="right">6,478,605</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,717,998</td>
<td align="right">4,573,999</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">747,539</td>
<td align="right">725,020</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,162,441</td>
<td align="right">1,127,931</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">348</td>
<td align="right">356</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">475</td>
<td align="right">484</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,039,726</td>
<td align="right">2,005,216</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">605,493</td>
<td align="right">597,119</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,594</td>
<td align="right">1,615</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,513,184</td>
<td align="right">11,373,548</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,546</td>
<td align="right">4,601</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,049</td>
<td align="right">5,084</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,217</td>
<td align="right">3,237</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">385,477</td>
<td align="right">383,165</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,447</td>
<td align="right">13,482</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,670</td>
<td align="right">17,705</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,670</td>
<td align="right">17,705</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,374</td>
<td align="right">102,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">204,962</td>
<td align="right">205,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">108,840</td>
<td align="right">108,884</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,372</td>
<td align="right">97,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,573</td>
<td align="right">16,568</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,045</td>
<td align="right">34,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,419</td>
<td align="right">46,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,018</td>
<td align="right">191,028</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,469</td>
<td align="right">21,468</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,808</td>
<td align="right">928,829</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,745</td>
<td align="right">456,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,674</td>
<td align="right">81,673</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,699</td>
<td align="right">1,818,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,627</td>
<td align="right">939,628</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,128</td>
<td align="right">35,128</td>
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
<td align="right">10,622,428</td>
<td align="right">98.8%</td>
<td align="right">9,301,139</td>
<td align="right">98.6%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,319</td>
<td align="right">0.2%</td>
<td align="right">19,509</td>
<td align="right">0.2%</td>
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
<td align="right">107,895</td>
<td align="right">1.0%</td>
<td align="right">107,940</td>
<td align="right">1.1%</td>
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
<td align="right">651</td>
<td align="right">48.8%</td>
<td align="right">633</td>
<td align="right">48.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">684</td>
<td align="right">51.2%</td>
<td align="right">684</td>
<td align="right">51.9%</td>
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
<td align="left">remainder</td>
<td align="right">294</td>
<td align="right">43.0%</td>
<td align="right">294</td>
<td align="right">43.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">27.3%</td>
<td align="right">187</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">76</td>
<td align="right">11.1%</td>
<td align="right">76</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">9.6%</td>
<td align="right">66</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">58</td>
<td align="right">8.5%</td>
<td align="right">58</td>
<td align="right">8.5%</td>
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
<td align="right">24,120,013</td>
<td align="right">100.0%</td>
<td align="right">21,637,583</td>
<td align="right">100.0%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,977</td>
<td align="right">0.0%</td>
<td align="right">2,013</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">787</td>
<td align="right">0.0%</td>
<td align="right">787</td>
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
<td align="right">3,356</td>
<td align="right">100.0%</td>
<td align="right">3,375</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">784,439</td>
<td align="right">15.2%</td>
<td align="right">677,097</td>
<td align="right">14.3%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,365,778</td>
<td align="right">84.4%</td>
<td align="right">4,042,217</td>
<td align="right">85.3%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,571</td>
<td align="right">0.4%</td>
<td align="right">18,982</td>
<td align="right">0.4%</td>
<td align="right">-3.0%</td>
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
<td align="right">1,006</td>
<td align="right">61.6%</td>
<td align="right">962</td>
<td align="right">61.0%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">627</td>
<td align="right">38.4%</td>
<td align="right">614</td>
<td align="right">39.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">714</td>
<td align="right">71.0%</td>
<td align="right">670</td>
<td align="right">69.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">153</td>
<td align="right">15.2%</td>
<td align="right">153</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">9.4%</td>
<td align="right">95</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.4%</td>
<td align="right">44</td>
<td align="right">4.6%</td>
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
<td align="right">1,749,950</td>
<td align="right">100.0%</td>
<td align="right">1,561,113</td>
<td align="right">100.0%</td>
<td align="right">-10.8%</td>
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
<td align="right">12,026,412</td>
<td align="right">92.8%</td>
<td align="right">11,688,214</td>
<td align="right">92.6%</td>
<td align="right">-2.8%</td>
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
<td align="right">7.2%</td>
<td align="right">939,088</td>
<td align="right">7.4%</td>
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
<td align="right">51</td>
<td align="right">9.5%</td>
<td align="right">52</td>
<td align="right">9.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.5%</td>
<td align="right">488</td>
<td align="right">90.4%</td>
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
<td align="right">8,066,475</td>
<td align="right">16.6%</td>
<td align="right">7,080,417</td>
<td align="right">16.2%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,152,695</td>
<td align="right">82.6%</td>
<td align="right">36,284,945</td>
<td align="right">82.9%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,937</td>
<td align="right">0.8%</td>
<td align="right">397,041</td>
<td align="right">0.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">6,923</td>
<td align="right">37.1%</td>
<td align="right">6,653</td>
<td align="right">36.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,752</td>
<td align="right">62.9%</td>
<td align="right">11,769</td>
<td align="right">63.9%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,651</td>
<td align="right">23.8%</td>
<td align="right">1,517</td>
<td align="right">22.8%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">855</td>
<td align="right">12.4%</td>
<td align="right">807</td>
<td align="right">12.1%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,513</td>
<td align="right">21.9%</td>
<td align="right">1,505</td>
<td align="right">22.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">9.9%</td>
<td align="right">684</td>
<td align="right">10.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.6%</td>
<td align="right">460</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.0%</td>
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
<td align="right">20,359,242</td>
<td align="right">100.0%</td>
<td align="right">18,175,981</td>
<td align="right">100.0%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">833</td>
<td align="right">0.0%</td>
<td align="right">849</td>
<td align="right">0.0%</td>
<td align="right">1.9%</td>
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
<td align="right">2,390</td>
<td align="right">100.0%</td>
<td align="right">2,394</td>
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
<td align="right">2,134,904</td>
<td align="right">100.0%</td>
<td align="right">1,838,131</td>
<td align="right">100.0%</td>
<td align="right">-13.9%</td>
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
<td align="right">5,102,262</td>
<td align="right">95.5%</td>
<td align="right">4,562,582</td>
<td align="right">95.0%</td>
<td align="right">-10.6%</td>
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
<td align="right">1.5%</td>
<td align="right">79,941</td>
<td align="right">1.7%</td>
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
<td align="right">160,377</td>
<td align="right">3.0%</td>
<td align="right">160,377</td>
<td align="right">3.3%</td>
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
<td align="right">3,993</td>
<td align="right">84.3%</td>
<td align="right">3,992</td>
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
<td align="right">848</td>
<td align="right">114.0%</td>
<td align="right">791</td>
<td align="right">106.3%</td>
<td align="right">-6.7%</td>
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
<td align="right">1,811,213</td>
<td align="right">98.8%</td>
<td align="right">1,623,274</td>
<td align="right">98.7%</td>
<td align="right">-10.4%</td>
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
<td align="right">21,263</td>
<td align="right">1.3%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
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
<td align="right">11,899,036</td>
<td align="right">95.2%</td>
<td align="right">10,412,994</td>
<td align="right">94.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">604,175</td>
<td align="right">4.8%</td>
<td align="right">595,811</td>
<td align="right">5.4%</td>
<td align="right">-1.4%</td>
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
<td align="right">858</td>
<td align="right">65.1%</td>
<td align="right">847</td>
<td align="right">64.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">34.9%</td>
<td align="right">461</td>
<td align="right">35.2%</td>
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
<td align="left">sequence</td>
<td align="right">131</td>
<td align="right">15.3%</td>
<td align="right">125</td>
<td align="right">14.8%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">318</td>
<td align="right">37.1%</td>
<td align="right">313</td>
<td align="right">37.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">27.0%</td>
<td align="right">232</td>
<td align="right">27.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.9%</td>
<td align="right">111</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">44</td>
<td align="right">5.2%</td>
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
<td align="right">2,128,529</td>
<td align="right">100.0%</td>
<td align="right">2,074,523</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">10,643,360</td>
<td align="right">2.5%</td>
<td align="right">9,541,407</td>
<td align="right">2.4%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">177,172,058</td>
<td align="right">41.0%</td>
<td align="right">161,446,274</td>
<td align="right">40.9%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">243,901,488</td>
<td align="right">56.4%</td>
<td align="right">222,673,588</td>
<td align="right">56.5%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">599,259</td>
<td align="right">0.1%</td>
<td align="right">596,966</td>
<td align="right">0.2%</td>
<td align="right">-0.4%</td>
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
<td align="right">784,439</td>
<td align="right">7.4%</td>
<td align="right">677,097</td>
<td align="right">7.1%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,066,475</td>
<td align="right">76.0%</td>
<td align="right">7,080,417</td>
<td align="right">74.4%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">833</td>
<td align="right">0.0%</td>
<td align="right">849</td>
<td align="right">0.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,977</td>
<td align="right">0.0%</td>
<td align="right">2,013</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">604,175</td>
<td align="right">5.7%</td>
<td align="right">595,811</td>
<td align="right">6.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">107,895</td>
<td align="right">1.0%</td>
<td align="right">107,940</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,088</td>
<td align="right">8.8%</td>
<td align="right">939,088</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,941</td>
<td align="right">0.8%</td>
<td align="right">79,941</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,263</td>
<td align="right">0.2%</td>
<td align="right">21,263</td>
<td align="right">0.2%</td>
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
<td align="right">10,003</td>
<td align="right">1.7%</td>
<td align="right">9,554</td>
<td align="right">1.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">10,316</td>
<td align="right">1.7%</td>
<td align="right">9,955</td>
<td align="right">1.7%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">19,570</td>
<td align="right">3.3%</td>
<td align="right">18,981</td>
<td align="right">3.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">338,190</td>
<td align="right">56.4%</td>
<td align="right">337,288</td>
<td align="right">56.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,703</td>
<td align="right">8.3%</td>
<td align="right">49,709</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">26.8%</td>
<td align="right">160,377</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
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
<td align="right">513,748</td>
<td align="right">1.6%</td>
<td align="right">459,816</td>
<td align="right">1.5%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">27,438,792</td>
<td align="right">84.5%</td>
<td align="right">24,846,738</td>
<td align="right">83.2%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,859,938</td>
<td align="right">73.5%</td>
<td align="right">21,726,525</td>
<td align="right">72.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,176,679</td>
<td align="right">25.2%</td>
<td align="right">7,718,038</td>
<td align="right">25.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,176,737</td>
<td align="right">25.2%</td>
<td align="right">7,718,096</td>
<td align="right">25.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,604,112</td>
<td align="right">26.5%</td>
<td align="right">8,145,471</td>
<td align="right">27.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,604,112</td>
<td align="right">26.5%</td>
<td align="right">8,145,471</td>
<td align="right">27.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,684</td>
<td align="right">0.1%</td>
<td align="right">17,719</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.3%</td>
<td align="right">427,375</td>
<td align="right">1.4%</td>
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
<td align="right">1.4%</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.4%</td>
<td align="right">441,508</td>
<td align="right">1.5%</td>
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
<td align="left">Method cache collisions</td>
<td align="right">45,831</td>
<td align="right"></td>
<td align="right">66,383</td>
<td align="right"></td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,685,294</td>
<td align="right"></td>
<td align="right">1,469,422</td>
<td align="right"></td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">11,570,958</td>
<td align="right"></td>
<td align="right">10,127,682</td>
<td align="right"></td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">969,350</td>
<td align="right">0.3%</td>
<td align="right">861,438</td>
<td align="right">0.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,632,480</td>
<td align="right"></td>
<td align="right">8,596,813</td>
<td align="right"></td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">6,023,078</td>
<td align="right">2.3%</td>
<td align="right">5,430,881</td>
<td align="right">2.3%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">60,501,851</td>
<td align="right">20.5%</td>
<td align="right">54,811,688</td>
<td align="right">20.3%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">55,547,831</td>
<td align="right">21.4%</td>
<td align="right">50,482,995</td>
<td align="right">21.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,386,194</td>
<td align="right">66.6%</td>
<td align="right">23,982,937</td>
<td align="right">65.9%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,389,020</td>
<td align="right"></td>
<td align="right">23,985,620</td>
<td align="right"></td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">90,573,682</td>
<td align="right">34.9%</td>
<td align="right">82,654,781</td>
<td align="right">34.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">142,896,583</td>
<td align="right">48.5%</td>
<td align="right">130,816,882</td>
<td align="right">48.6%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">90,487,457</td>
<td align="right">30.7%</td>
<td align="right">82,863,720</td>
<td align="right">30.8%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">107,059,445</td>
<td align="right">41.3%</td>
<td align="right">98,189,626</td>
<td align="right">41.5%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,675,470</td>
<td align="right"></td>
<td align="right">13,624,515</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">180,161</td>
<td align="right"></td>
<td align="right">192,473</td>
<td align="right"></td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,134,290</td>
<td align="right">33.1%</td>
<td align="right">12,272,078</td>
<td align="right">33.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,255,482</td>
<td align="right">33.4%</td>
<td align="right">12,393,292</td>
<td align="right">34.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,752,365</td>
<td align="right"></td>
<td align="right">1,762,798</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,605</td>
<td align="right">0.2%</td>
<td align="right">77,632</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,587</td>
<td align="right">0.1%</td>
<td align="right">43,582</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">212</td>
<td align="right">10,306</td>
<td align="right">758</td>
<td align="right">711</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">10,306</td>
<td align="right">758</td>
<td align="right">711</td>
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
<td align="right">95</td>
<td align="right">3.0%</td>
<td align="right">84</td>
<td align="right">2.7%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,978,234</td>
<td align="right"></td>
<td align="right">2,643,231</td>
<td align="right"></td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">258,034,680</td>
<td align="right">8,664.0%</td>
<td align="right">234,272,967</td>
<td align="right">8,863.1%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">12</td>
<td align="right">0.4%</td>
<td align="right">11</td>
<td align="right">0.4%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,341</td>
<td align="right">42.0%</td>
<td align="right">1,301</td>
<td align="right">41.8%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,194</td>
<td align="right"></td>
<td align="right">3,109</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,546</td>
<td align="right">48.4%</td>
<td align="right">1,512</td>
<td align="right">48.6%</td>
<td align="right">-2.2%</td>
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
<td align="right">6.6%</td>
<td align="right">212</td>
<td align="right">6.8%</td>
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
<td align="right">95</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">95</td>
<td align="right">100.0%</td>
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">-11.6%</td>
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
<td align="right">2,347,602</td>
<td align="right">89.4%</td>
<td align="right">2,105,733</td>
<td align="right">88.9%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">53,104</td>
<td align="right">2.0%</td>
<td align="right">47,824</td>
<td align="right">2.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,625,536</td>
<td align="right"></td>
<td align="right">2,367,488</td>
<td align="right"></td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">224,830</td>
<td align="right">8.6%</td>
<td align="right">213,931</td>
<td align="right">9.0%</td>
<td align="right">-4.8%</td>
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
<td align="left">17</td>
<td align="right">17.9%</td>
<td align="left">13</td>
<td align="right">15.5%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">23.2%</td>
<td align="left">22</td>
<td align="right">26.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">34</td>
<td align="right">35.8%</td>
<td align="left">28</td>
<td align="right">33.3%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">22</td>
<td align="right">23.2%</td>
<td align="left">21</td>
<td align="right">25.0%</td>
<td align="right">-4.5%</td>
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
<td align="right">17</td>
<td align="right">17.9%</td>
<td align="right">13</td>
<td align="right">15.5%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21</td>
<td align="right">22.1%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2</td>
<td align="right">2.1%</td>
<td align="right">2</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">33</td>
<td align="right">34.7%</td>
<td align="right">27</td>
<td align="right">32.1%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">22</td>
<td align="right">23.2%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
<td align="right">-4.5%</td>
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
<td align="right">17</td>
<td align="right">17.9%</td>
<td align="right">13</td>
<td align="right">15.5%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">23.2%</td>
<td align="right">22</td>
<td align="right">26.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">14</td>
<td align="right">16.7%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">26</td>
<td align="right">27.4%</td>
<td align="right">24</td>
<td align="right">28.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">12</td>
<td align="right">12.6%</td>
<td align="right">11</td>
<td align="right">13.1%</td>
<td align="right">-8.3%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">545,599</td>
<td align="right">2,175,101</td>
<td align="right">298.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,356,201</td>
<td align="right">871,042</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,305,367</td>
<td align="right">1,274,609</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">108,319</td>
<td align="right">88,820</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,319</td>
<td align="right">88,820</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">108,416</td>
<td align="right">88,912</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">108,416</td>
<td align="right">88,912</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">108,416</td>
<td align="right">88,912</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">848,229</td>
<td align="right">709,527</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">449,630</td>
<td align="right">377,344</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">449,630</td>
<td align="right">377,344</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">762,334</td>
<td align="right">641,088</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">631,494</td>
<td align="right">531,795</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">2,411,455</td>
<td align="right">2,033,938</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">2,582,183</td>
<td align="right">2,178,263</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">654,015</td>
<td align="right">552,268</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,990,909</td>
<td align="right">1,681,289</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,990,909</td>
<td align="right">1,681,289</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">995,229</td>
<td align="right">840,700</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">170,729</td>
<td align="right">144,328</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,671,661</td>
<td align="right">1,413,346</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,540,829</td>
<td align="right">1,304,059</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,148,817</td>
<td align="right">1,822,894</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">545,599</td>
<td align="right">463,356</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,273,062</td>
<td align="right">1,081,163</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">182,746</td>
<td align="right">155,333</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,760,139</td>
<td align="right">3,250,231</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,347,114</td>
<td align="right">2,043,928</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,347,114</td>
<td align="right">2,043,928</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,234,722</td>
<td align="right">1,951,022</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,948,515</td>
<td align="right">1,711,745</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">3,980,701</td>
<td align="right">3,497,199</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">7,057,558</td>
<td align="right">6,219,329</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,334,453</td>
<td align="right">5,960,379</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,507,108</td>
<td align="right">1,333,084</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,566,455</td>
<td align="right">1,386,552</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,978,234</td>
<td align="right">2,643,231</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,402,916</td>
<td align="right">1,248,389</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,807,505</td>
<td align="right">2,498,903</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,502,989</td>
<td align="right">1,338,511</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,850,966</td>
<td align="right">3,449,710</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,850,966</td>
<td align="right">3,449,710</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,850,966</td>
<td align="right">3,449,710</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,560,495</td>
<td align="right">3,198,072</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,143,718</td>
<td align="right">1,936,383</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,031,009</td>
<td align="right">931,303</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,135,142</td>
<td align="right">1,025,490</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">45,592,265</td>
<td align="right">41,575,590</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">949,166</td>
<td align="right">866,923</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,843,391</td>
<td align="right">1,685,012</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">849,145</td>
<td align="right">776,852</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">40,314,173</td>
<td align="right">36,924,099</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">861,435</td>
<td align="right">789,149</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,293,308</td>
<td align="right">3,947,881</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">732,740</td>
<td align="right">674,238</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,422,665</td>
<td align="right">2,238,679</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,235,435</td>
<td align="right">5,772,270</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,387,664</td>
<td align="right">1,293,828</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,703,599</td>
<td align="right">5,320,197</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">697,966</td>
<td align="right">651,049</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">624,421</td>
<td align="right">585,418</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,946,529</td>
<td align="right">1,827,317</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,334,409</td>
<td align="right">1,254,205</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,926,062</td>
<td align="right">1,819,455</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,926,062</td>
<td align="right">1,819,455</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">8,056,535</td>
<td align="right">7,627,826</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">582,261</td>
<td align="right">554,841</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">585,497</td>
<td align="right">558,077</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">585,497</td>
<td align="right">558,077</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">585,431</td>
<td align="right">558,018</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">585,431</td>
<td align="right">558,018</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,733,924</td>
<td align="right">1,653,713</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">516,102</td>
<td align="right">496,598</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">516,102</td>
<td align="right">496,598</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">516,102</td>
<td align="right">496,598</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">516,005</td>
<td align="right">496,506</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">520,143</td>
<td align="right">500,648</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,099,309</td>
<td align="right">6,872,456</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,099,309</td>
<td align="right">6,872,456</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">919,669</td>
<td align="right">900,165</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">923,790</td>
<td align="right">904,288</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,134,392</td>
<td align="right">2,114,893</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,538,841</td>
<td align="right">2,519,342</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,515</td>
<td align="right">399,508</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,515</td>
<td align="right">399,508</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,515</td>
<td align="right">399,508</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,515</td>
<td align="right">399,508</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,515</td>
<td align="right">399,508</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,214,887</td>
<td align="right">1,214,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">864,448</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,515</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">398,599</td>
<td align="right"></td>
<td align="right"></td>
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
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">332,183</td>
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
Stats gathered on: 2025-04-25
