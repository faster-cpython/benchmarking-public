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
<td align="right">785,569</td>
<td align="right">541,105</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,592,162</td>
<td align="right">1,103,234</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">534,316</td>
<td align="right">371,378</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,605,999</td>
<td align="right">1,117,914</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,081,391</td>
<td align="right">753,066</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,155,368</td>
<td align="right">1,505,907</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">542,630</td>
<td align="right">379,692</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,183,618</td>
<td align="right">1,534,157</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,099,398</td>
<td align="right">775,869</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,113,100</td>
<td align="right">787,164</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">835,563</td>
<td align="right">591,158</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,520,477</td>
<td align="right">3,906,042</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,221,439</td>
<td align="right">1,571,978</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">557,651</td>
<td align="right">394,655</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">557,974</td>
<td align="right">394,978</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">839,907</td>
<td align="right">595,501</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">279,588</td>
<td align="right">198,274</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">7,327,892</td>
<td align="right">5,238,894</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">867,043</td>
<td align="right">622,579</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,991,166</td>
<td align="right">1,431,172</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,020,795</td>
<td align="right">1,459,687</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">297,420</td>
<td align="right">215,951</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">299,961</td>
<td align="right">218,550</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,783,207</td>
<td align="right">1,303,978</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">303,331</td>
<td align="right">221,862</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,805,029</td>
<td align="right">1,325,779</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,080,386</td>
<td align="right">8,162,341</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,243,414</td>
<td align="right">1,655,461</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,611,588</td>
<td align="right">7,099,458</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,257,324</td>
<td align="right">4,627,703</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,939,724</td>
<td align="right">11,126,415</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,181,637</td>
<td align="right">13,643,785</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,553,602</td>
<td align="right">3,422,099</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,268,630</td>
<td align="right">953,978</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,922,982</td>
<td align="right">3,711,190</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,656,009</td>
<td align="right">12,605,372</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,427,169</td>
<td align="right">4,125,554</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,513,567</td>
<td align="right">6,483,838</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,061,664</td>
<td align="right">1,572,825</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,071,165</td>
<td align="right">1,583,368</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,436,647</td>
<td align="right">1,875,945</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95,977,066</td>
<td align="right">74,281,323</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,262,795</td>
<td align="right">12,616,061</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,004,978</td>
<td align="right">6,212,481</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,485,591</td>
<td align="right">25,991,776</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,637,927</td>
<td align="right">2,827,409</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,287,423</td>
<td align="right">8,013,648</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,129,700</td>
<td align="right">3,235,435</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,734,740</td>
<td align="right">2,929,226</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,366,077</td>
<td align="right">2,642,311</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,582,259</td>
<td align="right">16,185,845</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,584,985</td>
<td align="right">1,259,053</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,220,432</td>
<td align="right">975,968</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,665,494</td>
<td align="right">1,339,711</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,264,184</td>
<td align="right">1,019,714</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,345,301</td>
<td align="right">2,701,440</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">424,234</td>
<td align="right">342,769</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">35,785,650</td>
<td align="right">29,203,921</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,743,207</td>
<td align="right">16,179,229</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,172,576</td>
<td align="right">22,340,079</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,057,918</td>
<td align="right">18,990,551</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,718,906</td>
<td align="right">7,192,472</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,041,245</td>
<td align="right">4,159,782</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">939,398</td>
<td align="right">780,912</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,142,138</td>
<td align="right">3,490,274</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,509,134</td>
<td align="right">7,215,923</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,834,388</td>
<td align="right">8,449,102</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,134,956</td>
<td align="right">3,568,961</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,391,234</td>
<td align="right">6,680,468</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">106</td>
<td align="right">115</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,176,478</td>
<td align="right">1,095,003</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,278,451</td>
<td align="right">5,882,661</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,234,016</td>
<td align="right">1,156,994</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">104,870</td>
<td align="right">109,301</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">12,290,364</td>
<td align="right">11,896,708</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,518,989</td>
<td align="right">2,441,967</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">380,684</td>
<td align="right">390,317</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">603,834</td>
<td align="right">607,978</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,570</td>
<td align="right">4,600</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">342</td>
<td align="right">340</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,215</td>
<td align="right">5,245</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,624</td>
<td align="right">1,631</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,613</td>
<td align="right">13,642</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">486</td>
<td align="right">485</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">8,349</td>
<td align="right">8,334</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,836</td>
<td align="right">17,865</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,836</td>
<td align="right">17,865</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,234</td>
<td align="right">3,232</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">205,265</td>
<td align="right">205,364</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,554</td>
<td align="right">102,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,662</td>
<td align="right">81,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,685</td>
<td align="right">456,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,811</td>
<td align="right">516,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,044</td>
<td align="right">34,042</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,405</td>
<td align="right">97,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,143</td>
<td align="right">35,142</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,016</td>
<td align="right">191,014</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,631</td>
<td align="right">939,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">454,115</td>
<td align="right">454,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,846</td>
<td align="right">928,847</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,599</td>
<td align="right">4,723,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,702</td>
<td align="right">1,818,702</td>
<td align="right">0.0%</td>
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
<td align="right">84,727</td>
<td align="right">84,727</td>
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
<td align="right">59,120</td>
<td align="right">59,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,867</td>
<td align="right">55,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,863</td>
<td align="right">55,863</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,381</td>
<td align="right">10,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,287</td>
<td align="right">10,287</td>
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
<td align="right">14,231,190</td>
<td align="right">96.4%</td>
<td align="right">10,235,214</td>
<td align="right">95.0%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,675</td>
<td align="right">0.1%</td>
<td align="right">21,940</td>
<td align="right">0.2%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">515,748</td>
<td align="right">3.5%</td>
<td align="right">515,779</td>
<td align="right">4.8%</td>
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
<td align="right">617</td>
<td align="right">43.4%</td>
<td align="right">684</td>
<td align="right">45.9%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">804</td>
<td align="right">56.6%</td>
<td align="right">806</td>
<td align="right">54.1%</td>
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
<td align="left">subscr</td>
<td align="right">255</td>
<td align="right">31.7%</td>
<td align="right">258</td>
<td align="right">32.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">293</td>
<td align="right">36.4%</td>
<td align="right">292</td>
<td align="right">36.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.3%</td>
<td align="right">187</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
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
<td align="right">30,893,420</td>
<td align="right">100.0%</td>
<td align="right">23,397,370</td>
<td align="right">100.0%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,012</td>
<td align="right">0.0%</td>
<td align="right">2,030</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
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
<td align="right">3,353</td>
<td align="right">100.0%</td>
<td align="right">3,365</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,080,079</td>
<td align="right">17.0%</td>
<td align="right">751,788</td>
<td align="right">14.9%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,249,528</td>
<td align="right">82.7%</td>
<td align="right">4,271,703</td>
<td align="right">84.7%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,343</td>
<td align="right">0.3%</td>
<td align="right">20,747</td>
<td align="right">0.4%</td>
<td align="right">13.1%</td>
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
<td align="right">604</td>
<td align="right">36.6%</td>
<td align="right">644</td>
<td align="right">38.8%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,046</td>
<td align="right">63.4%</td>
<td align="right">1,015</td>
<td align="right">61.2%</td>
<td align="right">-3.0%</td>
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
<td align="right">755</td>
<td align="right">72.2%</td>
<td align="right">725</td>
<td align="right">71.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">152</td>
<td align="right">14.5%</td>
<td align="right">151</td>
<td align="right">14.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">9.1%</td>
<td align="right">95</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.2%</td>
<td align="right">44</td>
<td align="right">4.3%</td>
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
<td align="right">2,265,262</td>
<td align="right">100.0%</td>
<td align="right">1,694,836</td>
<td align="right">100.0%</td>
<td align="right">-25.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,902,741</td>
<td align="right">93.2%</td>
<td align="right">11,947,569</td>
<td align="right">92.7%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">939,093</td>
<td align="right">6.8%</td>
<td align="right">939,093</td>
<td align="right">7.3%</td>
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
<td align="right">53</td>
<td align="right">9.8%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.7%</td>
<td align="right">488</td>
<td align="right">90.2%</td>
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
<td align="right">11,068,366</td>
<td align="right">18.1%</td>
<td align="right">8,150,940</td>
<td align="right">17.3%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">49,701,077</td>
<td align="right">81.3%</td>
<td align="right">38,667,482</td>
<td align="right">81.9%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">388,388</td>
<td align="right">0.6%</td>
<td align="right">388,291</td>
<td align="right">0.8%</td>
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
<td align="right">7,513</td>
<td align="right">39.5%</td>
<td align="right">6,862</td>
<td align="right">37.2%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,530</td>
<td align="right">60.5%</td>
<td align="right">11,581</td>
<td align="right">62.8%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">2,008</td>
<td align="right">26.7%</td>
<td align="right">1,656</td>
<td align="right">24.1%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">923</td>
<td align="right">12.3%</td>
<td align="right">871</td>
<td align="right">12.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,454</td>
<td align="right">19.4%</td>
<td align="right">1,442</td>
<td align="right">21.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">9.1%</td>
<td align="right">684</td>
<td align="right">10.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.1%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">0.9%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">0.9%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.6%</td>
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
<td align="right">26,694,934</td>
<td align="right">100.0%</td>
<td align="right">20,127,353</td>
<td align="right">100.0%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">848</td>
<td align="right">0.0%</td>
<td align="right">853</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
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
<td align="right">2,392</td>
<td align="right">100.0%</td>
<td align="right">2,385</td>
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
<td align="right">2,944,624</td>
<td align="right">100.0%</td>
<td align="right">2,048,266</td>
<td align="right">100.0%</td>
<td align="right">-30.4%</td>
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
<td align="right">6,526,884</td>
<td align="right">96.7%</td>
<td align="right">4,897,221</td>
<td align="right">95.7%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,939</td>
<td align="right">1.2%</td>
<td align="right">79,942</td>
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
<td align="right">2.1%</td>
<td align="right">140,400</td>
<td align="right">2.7%</td>
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
<td align="right">3,616</td>
<td align="right">83.0%</td>
<td align="right">3,620</td>
<td align="right">83.0%</td>
<td align="right">0.1%</td>
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
<td align="right">996</td>
<td align="right">134.1%</td>
<td align="right">838</td>
<td align="right">112.8%</td>
<td align="right">-15.9%</td>
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
<td align="right">2,326,316</td>
<td align="right">99.1%</td>
<td align="right">1,756,220</td>
<td align="right">98.8%</td>
<td align="right">-24.5%</td>
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
<td align="right">0.9%</td>
<td align="right">21,267</td>
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
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">21</td>
<td align="right">10.1%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">187</td>
<td align="right">89.9%</td>
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
<td align="right">15,927,425</td>
<td align="right">96.3%</td>
<td align="right">11,445,343</td>
<td align="right">95.0%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">602,498</td>
<td align="right">3.6%</td>
<td align="right">606,642</td>
<td align="right">5.0%</td>
<td align="right">0.7%</td>
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
<td align="right">456</td>
<td align="right">34.1%</td>
<td align="right">457</td>
<td align="right">34.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">880</td>
<td align="right">65.9%</td>
<td align="right">879</td>
<td align="right">65.8%</td>
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
<td align="left">sequence</td>
<td align="right">153</td>
<td align="right">17.4%</td>
<td align="right">146</td>
<td align="right">16.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">318</td>
<td align="right">36.1%</td>
<td align="right">324</td>
<td align="right">36.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.4%</td>
<td align="right">232</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.6%</td>
<td align="right">111</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">44</td>
<td align="right">5.0%</td>
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
<td align="right">2,275,764</td>
<td align="right">100.0%</td>
<td align="right">2,112,829</td>
<td align="right">100.0%</td>
<td align="right">-7.2%</td>
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
<td align="right">14,347,852</td>
<td align="right">2.6%</td>
<td align="right">11,105,708</td>
<td align="right">2.5%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">230,770,122</td>
<td align="right">41.2%</td>
<td align="right">184,021,214</td>
<td align="right">41.1%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">314,967,185</td>
<td align="right">56.2%</td>
<td align="right">252,110,542</td>
<td align="right">56.3%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">566,904</td>
<td align="right">0.1%</td>
<td align="right">572,472</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
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
<td align="right">1,080,079</td>
<td align="right">7.5%</td>
<td align="right">751,788</td>
<td align="right">6.8%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,068,366</td>
<td align="right">77.3%</td>
<td align="right">8,150,940</td>
<td align="right">73.5%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,012</td>
<td align="right">0.0%</td>
<td align="right">2,030</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">602,498</td>
<td align="right">4.2%</td>
<td align="right">606,642</td>
<td align="right">5.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">848</td>
<td align="right">0.0%</td>
<td align="right">853</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">21,267</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,748</td>
<td align="right">3.6%</td>
<td align="right">515,779</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,939</td>
<td align="right">0.6%</td>
<td align="right">79,942</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,093</td>
<td align="right">6.6%</td>
<td align="right">939,093</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
<td align="right">14,143</td>
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
<td align="right">9,165</td>
<td align="right">1.6%</td>
<td align="right">10,858</td>
<td align="right">1.9%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">9,510</td>
<td align="right">1.7%</td>
<td align="right">11,082</td>
<td align="right">1.9%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,342</td>
<td align="right">3.2%</td>
<td align="right">20,746</td>
<td align="right">3.6%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">318,971</td>
<td align="right">56.3%</td>
<td align="right">318,873</td>
<td align="right">55.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,372</td>
<td align="right">10.5%</td>
<td align="right">59,373</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">24.8%</td>
<td align="right">140,400</td>
<td align="right">24.5%</td>
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
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">276</td>
<td align="right">0.0%</td>
<td align="right">276</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">162</td>
<td align="right">0.0%</td>
<td align="right">162</td>
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
<td align="right">665,211</td>
<td align="right">1.7%</td>
<td align="right">502,215</td>
<td align="right">1.6%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">34,510,428</td>
<td align="right">87.3%</td>
<td align="right">26,687,417</td>
<td align="right">84.2%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">29,696,940</td>
<td align="right">75.1%</td>
<td align="right">23,259,215</td>
<td align="right">73.3%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">9,411,308</td>
<td align="right">23.8%</td>
<td align="right">8,026,022</td>
<td align="right">25.3%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">9,411,367</td>
<td align="right">23.8%</td>
<td align="right">8,026,081</td>
<td align="right">25.3%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,838,746</td>
<td align="right">24.9%</td>
<td align="right">8,453,460</td>
<td align="right">26.7%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,838,746</td>
<td align="right">24.9%</td>
<td align="right">8,453,460</td>
<td align="right">26.7%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,851</td>
<td align="right">0.0%</td>
<td align="right">17,880</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.1%</td>
<td align="right">427,379</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
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
<td align="right">1.2%</td>
<td align="right">456,471</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.1%</td>
<td align="right">441,509</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">57,299</td>
<td align="right"></td>
<td align="right">13,061</td>
<td align="right"></td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">151,283</td>
<td align="right"></td>
<td align="right">39,898</td>
<td align="right"></td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">94,260</td>
<td align="right"></td>
<td align="right">27,112</td>
<td align="right"></td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,274,167</td>
<td align="right"></td>
<td align="right">1,622,303</td>
<td align="right"></td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">15,483,049</td>
<td align="right"></td>
<td align="right">11,230,721</td>
<td align="right"></td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,252,472</td>
<td align="right">0.3%</td>
<td align="right">926,581</td>
<td align="right">0.3%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">116,683,303</td>
<td align="right">28.9%</td>
<td align="right">88,622,959</td>
<td align="right">28.2%</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">73,892,717</td>
<td align="right">16.7%</td>
<td align="right">56,442,133</td>
<td align="right">16.3%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">70,203,322</td>
<td align="right">17.4%</td>
<td align="right">54,072,944</td>
<td align="right">17.2%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,014,124</td>
<td align="right">2.0%</td>
<td align="right">6,222,574</td>
<td align="right">2.0%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,777,100</td>
<td align="right">60.8%</td>
<td align="right">22,422,562</td>
<td align="right">59.3%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,778,704</td>
<td align="right"></td>
<td align="right">22,424,332</td>
<td align="right"></td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">115,394,120</td>
<td align="right">26.1%</td>
<td align="right">90,062,162</td>
<td align="right">26.1%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">252,080,814</td>
<td align="right">57.0%</td>
<td align="right">197,939,026</td>
<td align="right">57.3%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">14,551,595</td>
<td align="right"></td>
<td align="right">11,499,363</td>
<td align="right"></td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">208,281,717</td>
<td align="right">51.7%</td>
<td align="right">165,341,285</td>
<td align="right">52.6%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">20,516,789</td>
<td align="right"></td>
<td align="right">16,768,573</td>
<td align="right"></td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">18,459,097</td>
<td align="right">39.0%</td>
<td align="right">15,281,416</td>
<td align="right">40.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">18,580,282</td>
<td align="right">39.2%</td>
<td align="right">15,402,613</td>
<td align="right">40.7%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,600</td>
<td align="right">0.2%</td>
<td align="right">77,613</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,585</td>
<td align="right">0.1%</td>
<td align="right">43,584</td>
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
<td align="right">9,539</td>
<td align="right">696</td>
<td align="right">639</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">9,539</td>
<td align="right">696</td>
<td align="right">639</td>
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
<td align="right">3,533,075</td>
<td align="right"></td>
<td align="right">2,447,252</td>
<td align="right"></td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">241,396,281</td>
<td align="right">6,832.5%</td>
<td align="right">172,017,214</td>
<td align="right">7,029.0%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,662</td>
<td align="right">48.7%</td>
<td align="right">1,538</td>
<td align="right">48.5%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,547</td>
<td align="right">45.4%</td>
<td align="right">1,433</td>
<td align="right">45.2%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,410</td>
<td align="right"></td>
<td align="right">3,170</td>
<td align="right"></td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">95</td>
<td align="right">2.8%</td>
<td align="right">93</td>
<td align="right">2.9%</td>
<td align="right">-2.1%</td>
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
<td align="right">106</td>
<td align="right">3.1%</td>
<td align="right">106</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
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
<td align="right">12</td>
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
<td align="right">93</td>
<td align="right"></td>
<td align="right">-2.1%</td>
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
<td align="right">93</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">269,984</td>
<td align="right">10.4%</td>
<td align="right">285,730</td>
<td align="right">11.2%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">2,279,872</td>
<td align="right">87.7%</td>
<td align="right">2,220,142</td>
<td align="right">86.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">51,104</td>
<td align="right">2.0%</td>
<td align="right">50,032</td>
<td align="right">2.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,600,960</td>
<td align="right"></td>
<td align="right">2,555,904</td>
<td align="right"></td>
<td align="right">-1.7%</td>
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
<td align="left">17</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">23.2%</td>
<td align="left">22</td>
<td align="right">23.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">36</td>
<td align="right">37.9%</td>
<td align="left">33</td>
<td align="right">35.5%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">20</td>
<td align="right">21.1%</td>
<td align="left">21</td>
<td align="right">22.6%</td>
<td align="right">5.0%</td>
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
<td align="right">17</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">23.2%</td>
<td align="right">22</td>
<td align="right">23.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">18</td>
<td align="right">19.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">15</td>
<td align="right">16.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">21.1%</td>
<td align="right">21</td>
<td align="right">22.6%</td>
<td align="right">5.0%</td>
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
<td align="right">38</td>
<td align="right">40.0%</td>
<td align="right">38</td>
<td align="right">40.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">18</td>
<td align="right">19.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">38</td>
<td align="right">40.0%</td>
<td align="right">36</td>
<td align="right">38.7%</td>
<td align="right">-5.3%</td>
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
<td align="right">765,456</td>
<td align="right">1,976,871</td>
<td align="right">158.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,971,259</td>
<td align="right">518,559</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,205,803</td>
<td align="right">518,559</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">183,955</td>
<td align="right">98,056</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">183,955</td>
<td align="right">98,056</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">184,066</td>
<td align="right">98,152</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">184,066</td>
<td align="right">98,152</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">184,066</td>
<td align="right">98,152</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">184,066</td>
<td align="right">98,152</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">184,066</td>
<td align="right">98,152</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">368,903</td>
<td align="right">197,090</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">439,217</td>
<td align="right">271,004</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">440,099</td>
<td align="right">271,886</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">674,887</td>
<td align="right">421,194</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">674,887</td>
<td align="right">421,194</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,133,477</td>
<td align="right">714,767</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">930,038</td>
<td align="right">594,046</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,624,295</td>
<td align="right">1,037,806</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">3,523,208</td>
<td align="right">2,271,120</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">3,768,757</td>
<td align="right">2,432,774</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,828,975</td>
<td align="right">1,827,372</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,828,975</td>
<td align="right">1,827,372</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">949,522</td>
<td align="right">616,711</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,676,101</td>
<td align="right">1,090,024</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,440,347</td>
<td align="right">939,753</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,440,343</td>
<td align="right">939,753</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,881,220</td>
<td align="right">1,880,885</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,881,220</td>
<td align="right">1,880,885</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,409,235</td>
<td align="right">1,579,030</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,806,890</td>
<td align="right">5,138,586</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">736,461</td>
<td align="right">484,780</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">245,553</td>
<td align="right">161,654</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,205,803</td>
<td align="right">1,458,312</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,205,803</td>
<td align="right">1,458,312</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,714,975</td>
<td align="right">1,135,267</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,460,950</td>
<td align="right">1,631,164</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">746,063</td>
<td align="right">495,978</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,736,715</td>
<td align="right">2,495,430</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,736,715</td>
<td align="right">2,495,430</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,736,715</td>
<td align="right">2,495,430</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,747,696</td>
<td align="right">3,175,631</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,798,285</td>
<td align="right">2,559,016</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,020,604</td>
<td align="right">691,408</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">255,151</td>
<td align="right">172,852</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">765,456</td>
<td align="right">518,559</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">5,085,702</td>
<td align="right">3,511,579</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,533,075</td>
<td align="right">2,447,252</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,287,522</td>
<td align="right">2,285,598</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">15,510,603</td>
<td align="right">10,826,140</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,048,693</td>
<td align="right">2,132,959</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,330,831</td>
<td align="right">1,662,425</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,188,687</td>
<td align="right">3,020,523</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,126,777</td>
<td align="right">1,547,069</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,803,379</td>
<td align="right">22,459,551</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,034,031</td>
<td align="right">2,955,745</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">964,663</td>
<td align="right">706,951</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,884,561</td>
<td align="right">1,381,207</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,277,902</td>
<td align="right">941,449</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,777,802</td>
<td align="right">3,525,995</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,817,571</td>
<td align="right">18,389,379</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,329,617</td>
<td align="right">993,583</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,695,628</td>
<td align="right">5,863,991</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,404,299</td>
<td align="right">1,070,319</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,404,299</td>
<td align="right">1,070,319</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,341,307</td>
<td align="right">4,838,653</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,074,466</td>
<td align="right">820,731</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,913,151</td>
<td align="right">1,491,176</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,145,642</td>
<td align="right">895,515</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,520,937</td>
<td align="right">3,766,402</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,520,937</td>
<td align="right">3,766,402</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">765,456</td>
<td align="right">887,619</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">595,780</td>
<td align="right">509,873</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">655,612</td>
<td align="right">573,271</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">658,848</td>
<td align="right">576,507</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,210,028</td>
<td align="right">2,124,129</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,614,477</td>
<td align="right">2,528,578</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,343,623</td>
<td align="right">4,238,272</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,579</td>
<td align="right">399,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,236,975</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">623,172</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,579</td>
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
<td align="right">107</td>
<td align="right">107</td>
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
Stats gathered on: 2025-03-29
