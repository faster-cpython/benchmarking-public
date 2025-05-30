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
<td align="right">592,490</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,592,162</td>
<td align="right">1,206,000</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">534,316</td>
<td align="right">405,278</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,605,999</td>
<td align="right">1,219,204</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,155,368</td>
<td align="right">1,638,346</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,081,391</td>
<td align="right">823,611</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">542,630</td>
<td align="right">413,592</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,183,618</td>
<td align="right">1,666,596</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,520,477</td>
<td align="right">4,215,342</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,099,398</td>
<td align="right">839,978</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,221,439</td>
<td align="right">1,704,417</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">7,327,892</td>
<td align="right">5,623,531</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">835,563</td>
<td align="right">641,998</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,113,100</td>
<td align="right">855,483</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">279,588</td>
<td align="right">215,081</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">557,651</td>
<td align="right">429,091</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">839,907</td>
<td align="right">646,339</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">557,974</td>
<td align="right">429,414</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,991,166</td>
<td align="right">1,534,307</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,020,795</td>
<td align="right">1,563,582</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">867,043</td>
<td align="right">673,934</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,805,029</td>
<td align="right">1,405,527</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,783,207</td>
<td align="right">1,389,863</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">297,420</td>
<td align="right">232,901</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">299,961</td>
<td align="right">234,997</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,268,630</td>
<td align="right">996,501</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">303,331</td>
<td align="right">238,819</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,080,386</td>
<td align="right">8,748,109</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,611,588</td>
<td align="right">7,603,907</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,257,324</td>
<td align="right">4,969,309</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,243,414</td>
<td align="right">1,786,423</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,939,724</td>
<td align="right">11,898,674</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,553,602</td>
<td align="right">3,645,710</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,181,637</td>
<td align="right">14,559,210</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,922,982</td>
<td align="right">3,956,819</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,656,009</td>
<td align="right">13,414,161</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,427,169</td>
<td align="right">4,390,919</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,513,567</td>
<td align="right">6,897,011</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,061,664</td>
<td align="right">1,674,768</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,071,165</td>
<td align="right">1,684,877</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,436,647</td>
<td align="right">1,985,642</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95,977,066</td>
<td align="right">78,611,975</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,262,795</td>
<td align="right">13,341,593</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,637,927</td>
<td align="right">2,985,446</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,004,978</td>
<td align="right">6,587,456</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,485,591</td>
<td align="right">27,556,480</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,287,423</td>
<td align="right">8,482,792</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,734,740</td>
<td align="right">3,083,966</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,366,077</td>
<td align="right">2,785,290</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,129,700</td>
<td align="right">3,419,067</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,582,259</td>
<td align="right">17,094,902</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,584,985</td>
<td align="right">1,327,383</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,220,432</td>
<td align="right">1,027,360</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,665,494</td>
<td align="right">1,406,736</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,345,301</td>
<td align="right">2,829,889</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,264,184</td>
<td align="right">1,071,119</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">424,234</td>
<td align="right">359,720</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">35,785,650</td>
<td align="right">30,553,049</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,743,207</td>
<td align="right">16,891,087</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">939,398</td>
<td align="right">804,015</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,172,576</td>
<td align="right">23,265,646</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,041,245</td>
<td align="right">4,317,317</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,718,906</td>
<td align="right">7,480,112</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,057,918</td>
<td align="right">19,827,294</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,142,138</td>
<td align="right">3,626,948</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,509,134</td>
<td align="right">7,464,801</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,834,388</td>
<td align="right">8,740,121</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,134,956</td>
<td align="right">3,678,113</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,391,234</td>
<td align="right">6,791,554</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">106</td>
<td align="right">113</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">104,870</td>
<td align="right">98,508</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,234,016</td>
<td align="right">1,163,146</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,176,478</td>
<td align="right">1,111,950</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,278,451</td>
<td align="right">5,950,723</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,215</td>
<td align="right">4,977</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">486</td>
<td align="right">501</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,518,989</td>
<td align="right">2,448,119</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">12,290,364</td>
<td align="right">11,954,590</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">342</td>
<td align="right">349</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,613</td>
<td align="right">13,374</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,836</td>
<td align="right">17,597</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,836</td>
<td align="right">17,597</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,570</td>
<td align="right">4,625</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">603,834</td>
<td align="right">596,734</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,624</td>
<td align="right">1,643</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,234</td>
<td align="right">3,243</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">205,265</td>
<td align="right">204,771</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,554</td>
<td align="right">102,308</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">8,349</td>
<td align="right">8,334</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">380,684</td>
<td align="right">380,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,811</td>
<td align="right">516,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,044</td>
<td align="right">34,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,143</td>
<td align="right">35,134</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,405</td>
<td align="right">97,389</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,662</td>
<td align="right">81,668</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,016</td>
<td align="right">191,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,846</td>
<td align="right">928,834</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,685</td>
<td align="right">456,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">454,115</td>
<td align="right">454,111</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,702</td>
<td align="right">1,818,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,631</td>
<td align="right">939,633</td>
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
<td align="right">11,076,020</td>
<td align="right">95.4%</td>
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
<td align="right">18,675</td>
<td align="right">0.1%</td>
<td align="right">18,853</td>
<td align="right">0.2%</td>
<td align="right">1.0%</td>
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
<td align="right">515,524</td>
<td align="right">4.4%</td>
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
<td align="right">617</td>
<td align="right">43.4%</td>
<td align="right">623</td>
<td align="right">43.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">804</td>
<td align="right">56.6%</td>
<td align="right">800</td>
<td align="right">56.2%</td>
<td align="right">-0.5%</td>
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
<td align="right">248</td>
<td align="right">31.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">293</td>
<td align="right">36.4%</td>
<td align="right">296</td>
<td align="right">37.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.3%</td>
<td align="right">187</td>
<td align="right">23.4%</td>
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
<td align="right">24,965,322</td>
<td align="right">100.0%</td>
<td align="right">-19.2%</td>
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
<td align="right">2,048</td>
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
<td align="right">3,372</td>
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
<td align="right">822,369</td>
<td align="right">15.5%</td>
<td align="right">-23.9%</td>
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
<td align="right">4,476,903</td>
<td align="right">84.2%</td>
<td align="right">-14.7%</td>
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
<td align="right">18,465</td>
<td align="right">0.3%</td>
<td align="right">0.7%</td>
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
<td align="right">1,046</td>
<td align="right">63.4%</td>
<td align="right">977</td>
<td align="right">61.8%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">604</td>
<td align="right">36.6%</td>
<td align="right">605</td>
<td align="right">38.2%</td>
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
<td align="left">float long</td>
<td align="right">755</td>
<td align="right">72.2%</td>
<td align="right">683</td>
<td align="right">69.9%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">152</td>
<td align="right">14.5%</td>
<td align="right">155</td>
<td align="right">15.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">9.1%</td>
<td align="right">95</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.2%</td>
<td align="right">44</td>
<td align="right">4.5%</td>
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
<td align="right">1,814,781</td>
<td align="right">100.0%</td>
<td align="right">-19.9%</td>
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
<td align="right">12,109,493</td>
<td align="right">92.8%</td>
<td align="right">-6.1%</td>
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
<td align="right">52</td>
<td align="right">9.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.7%</td>
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
<td align="right">11,068,366</td>
<td align="right">18.1%</td>
<td align="right">8,736,652</td>
<td align="right">17.5%</td>
<td align="right">-21.1%</td>
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
<td align="right">40,814,449</td>
<td align="right">81.7%</td>
<td align="right">-17.9%</td>
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
<td align="right">387,041</td>
<td align="right">0.8%</td>
<td align="right">-0.3%</td>
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
<td align="right">6,907</td>
<td align="right">37.4%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,530</td>
<td align="right">60.5%</td>
<td align="right">11,569</td>
<td align="right">62.6%</td>
<td align="right">0.3%</td>
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
<td align="right">1,686</td>
<td align="right">24.4%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">923</td>
<td align="right">12.3%</td>
<td align="right">855</td>
<td align="right">12.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,454</td>
<td align="right">19.4%</td>
<td align="right">1,434</td>
<td align="right">20.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">9.1%</td>
<td align="right">681</td>
<td align="right">9.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">21,455,951</td>
<td align="right">100.0%</td>
<td align="right">-19.6%</td>
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
<td align="right">858</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
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
<td align="right">2,391</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">2,236,541</td>
<td align="right">100.0%</td>
<td align="right">-24.0%</td>
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
<td align="right">5,238,871</td>
<td align="right">95.9%</td>
<td align="right">-19.7%</td>
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
<td align="right">1.5%</td>
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
<td align="right">2.6%</td>
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
<td align="right">3,619</td>
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
<td align="right">869</td>
<td align="right">117.0%</td>
<td align="right">-12.8%</td>
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
<td align="right">1,876,340</td>
<td align="right">98.9%</td>
<td align="right">-19.3%</td>
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
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">20</td>
<td align="right">9.7%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">187</td>
<td align="right">90.3%</td>
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
<td align="right">12,382,993</td>
<td align="right">95.4%</td>
<td align="right">-22.3%</td>
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
<td align="right">595,409</td>
<td align="right">4.6%</td>
<td align="right">-1.2%</td>
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
<td align="right">880</td>
<td align="right">65.9%</td>
<td align="right">866</td>
<td align="right">65.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">456</td>
<td align="right">34.1%</td>
<td align="right">459</td>
<td align="right">34.6%</td>
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
<td align="left">sequence</td>
<td align="right">153</td>
<td align="right">17.4%</td>
<td align="right">145</td>
<td align="right">16.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">318</td>
<td align="right">36.1%</td>
<td align="right">312</td>
<td align="right">36.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.4%</td>
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
<td align="right">2,275,764</td>
<td align="right">100.0%</td>
<td align="right">2,146,714</td>
<td align="right">100.0%</td>
<td align="right">-5.7%</td>
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
<td align="right">11,750,548</td>
<td align="right">2.5%</td>
<td align="right">-18.1%</td>
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
<td align="right">193,366,740</td>
<td align="right">41.1%</td>
<td align="right">-16.2%</td>
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
<td align="right">264,675,598</td>
<td align="right">56.3%</td>
<td align="right">-16.0%</td>
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
<td align="right">565,856</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
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
<td align="right">822,369</td>
<td align="right">7.0%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,068,366</td>
<td align="right">77.3%</td>
<td align="right">8,736,652</td>
<td align="right">74.5%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,012</td>
<td align="right">0.0%</td>
<td align="right">2,048</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">848</td>
<td align="right">0.0%</td>
<td align="right">858</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">602,498</td>
<td align="right">4.2%</td>
<td align="right">595,409</td>
<td align="right">5.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,748</td>
<td align="right">3.6%</td>
<td align="right">515,524</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">8.0%</td>
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
<td align="right">9,261</td>
<td align="right">1.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">9,510</td>
<td align="right">1.7%</td>
<td align="right">9,592</td>
<td align="right">1.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,342</td>
<td align="right">3.2%</td>
<td align="right">18,464</td>
<td align="right">3.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">318,971</td>
<td align="right">56.3%</td>
<td align="right">317,619</td>
<td align="right">56.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,372</td>
<td align="right">10.5%</td>
<td align="right">59,377</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">24.8%</td>
<td align="right">140,400</td>
<td align="right">24.8%</td>
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
<td align="right">536,629</td>
<td align="right">1.6%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">34,510,428</td>
<td align="right">87.3%</td>
<td align="right">28,326,565</td>
<td align="right">84.9%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">29,696,940</td>
<td align="right">75.1%</td>
<td align="right">24,607,344</td>
<td align="right">73.8%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">9,411,308</td>
<td align="right">23.8%</td>
<td align="right">8,317,041</td>
<td align="right">24.9%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">9,411,367</td>
<td align="right">23.8%</td>
<td align="right">8,317,100</td>
<td align="right">24.9%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,838,746</td>
<td align="right">24.9%</td>
<td align="right">8,744,479</td>
<td align="right">26.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,838,746</td>
<td align="right">24.9%</td>
<td align="right">8,744,479</td>
<td align="right">26.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,851</td>
<td align="right">0.0%</td>
<td align="right">17,612</td>
<td align="right">0.1%</td>
<td align="right">-1.3%</td>
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
<td align="right">1.3%</td>
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
<td align="right">94,260</td>
<td align="right"></td>
<td align="right">29,438</td>
<td align="right"></td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">151,283</td>
<td align="right"></td>
<td align="right">49,472</td>
<td align="right"></td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">57,299</td>
<td align="right"></td>
<td align="right">20,311</td>
<td align="right"></td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,274,167</td>
<td align="right"></td>
<td align="right">1,758,963</td>
<td align="right"></td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">15,483,049</td>
<td align="right"></td>
<td align="right">12,133,671</td>
<td align="right"></td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,252,472</td>
<td align="right">0.3%</td>
<td align="right">994,877</td>
<td align="right">0.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">116,683,303</td>
<td align="right">28.9%</td>
<td align="right">94,853,836</td>
<td align="right">28.5%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">73,892,717</td>
<td align="right">16.7%</td>
<td align="right">60,092,851</td>
<td align="right">16.4%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">70,203,322</td>
<td align="right">17.4%</td>
<td align="right">57,443,431</td>
<td align="right">17.3%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,014,124</td>
<td align="right">2.0%</td>
<td align="right">6,597,847</td>
<td align="right">2.0%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,777,100</td>
<td align="right">60.8%</td>
<td align="right">23,750,574</td>
<td align="right">59.6%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,778,704</td>
<td align="right"></td>
<td align="right">23,752,451</td>
<td align="right"></td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">115,394,120</td>
<td align="right">26.1%</td>
<td align="right">95,644,277</td>
<td align="right">26.1%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">252,080,814</td>
<td align="right">57.0%</td>
<td align="right">209,049,121</td>
<td align="right">57.2%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">14,551,595</td>
<td align="right"></td>
<td align="right">12,142,250</td>
<td align="right"></td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">208,281,717</td>
<td align="right">51.7%</td>
<td align="right">174,028,402</td>
<td align="right">52.3%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">20,516,789</td>
<td align="right"></td>
<td align="right">17,556,007</td>
<td align="right"></td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">18,459,097</td>
<td align="right">39.0%</td>
<td align="right">15,949,498</td>
<td align="right">40.1%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">18,580,282</td>
<td align="right">39.2%</td>
<td align="right">16,070,698</td>
<td align="right">40.4%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,600</td>
<td align="right">0.2%</td>
<td align="right">77,617</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,585</td>
<td align="right">0.1%</td>
<td align="right">43,583</td>
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
<td align="right">2,714,746</td>
<td align="right"></td>
<td align="right">-23.2%</td>
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
<td align="right">188,713,165</td>
<td align="right">6,951.4%</td>
<td align="right">-21.8%</td>
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
<td align="right">85</td>
<td align="right">2.6%</td>
<td align="right">-10.5%</td>
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
<td align="right">0.3%</td>
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
<td align="right">1,547</td>
<td align="right">45.4%</td>
<td align="right">1,458</td>
<td align="right">45.3%</td>
<td align="right">-5.8%</td>
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
<td align="right">3,218</td>
<td align="right"></td>
<td align="right">-5.6%</td>
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
<td align="right">1,569</td>
<td align="right">48.8%</td>
<td align="right">-5.6%</td>
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
<td align="right">85</td>
<td align="right"></td>
<td align="right">-10.5%</td>
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
<td align="right">85</td>
<td align="right">100.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">2,279,872</td>
<td align="right">87.7%</td>
<td align="right">2,038,271</td>
<td align="right">87.0%</td>
<td align="right">-10.6%</td>
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
<td align="right">45,968</td>
<td align="right">2.0%</td>
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
<td align="right">2,600,960</td>
<td align="right"></td>
<td align="right">2,342,912</td>
<td align="right"></td>
<td align="right">-9.9%</td>
</tr>
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
<td align="right">258,673</td>
<td align="right">11.0%</td>
<td align="right">-4.2%</td>
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
<td align="left">14</td>
<td align="right">16.5%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">23.2%</td>
<td align="left">22</td>
<td align="right">25.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">36</td>
<td align="right">37.9%</td>
<td align="left">30</td>
<td align="right">35.3%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">20</td>
<td align="right">21.1%</td>
<td align="left">19</td>
<td align="right">22.4%</td>
<td align="right">-5.0%</td>
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
<td align="right">14</td>
<td align="right">16.5%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">23.2%</td>
<td align="right">22</td>
<td align="right">25.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">15</td>
<td align="right">17.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">15</td>
<td align="right">17.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">21.1%</td>
<td align="right">19</td>
<td align="right">22.4%</td>
<td align="right">-5.0%</td>
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
<td align="right">35</td>
<td align="right">41.2%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">1</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18</td>
<td align="right">18.9%</td>
<td align="right">15</td>
<td align="right">17.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">38</td>
<td align="right">40.0%</td>
<td align="right">34</td>
<td align="right">40.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">2,211,042</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,971,259</td>
<td align="right">574,395</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,205,803</td>
<td align="right">574,395</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">765,456</td>
<td align="right">1,017,542</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">183,955</td>
<td align="right">125,794</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">183,955</td>
<td align="right">125,794</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">184,066</td>
<td align="right">125,890</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">184,066</td>
<td align="right">125,890</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">184,066</td>
<td align="right">125,890</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">184,066</td>
<td align="right">125,890</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">184,066</td>
<td align="right">125,890</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">368,903</td>
<td align="right">252,566</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">439,217</td>
<td align="right">317,353</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">674,887</td>
<td align="right">487,854</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">674,887</td>
<td align="right">487,854</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">440,099</td>
<td align="right">318,235</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,133,477</td>
<td align="right">826,079</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">930,038</td>
<td align="right">679,317</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,624,295</td>
<td align="right">1,188,037</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">3,523,208</td>
<td align="right">2,588,488</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">3,768,757</td>
<td align="right">2,769,580</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,828,975</td>
<td align="right">2,079,794</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,828,975</td>
<td align="right">2,079,794</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,676,101</td>
<td align="right">1,232,817</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">736,461</td>
<td align="right">543,129</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,440,343</td>
<td align="right">1,062,249</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,440,347</td>
<td align="right">1,062,252</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">245,553</td>
<td align="right">181,095</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">949,522</td>
<td align="right">700,285</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,881,220</td>
<td align="right">2,128,089</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,881,220</td>
<td align="right">2,128,089</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,806,890</td>
<td align="right">5,774,203</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,409,235</td>
<td align="right">1,783,400</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">746,063</td>
<td align="right">553,500</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,205,803</td>
<td align="right">1,636,647</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,205,803</td>
<td align="right">1,636,647</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,460,950</td>
<td align="right">1,828,107</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,714,975</td>
<td align="right">1,274,674</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,736,715</td>
<td align="right">2,785,437</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,736,715</td>
<td align="right">2,785,437</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,736,715</td>
<td align="right">2,785,437</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,747,696</td>
<td align="right">3,540,898</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,798,285</td>
<td align="right">2,840,709</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,020,604</td>
<td align="right">765,852</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">255,151</td>
<td align="right">191,463</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">765,456</td>
<td align="right">574,395</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">5,085,702</td>
<td align="right">3,885,201</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,533,075</td>
<td align="right">2,714,746</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,287,522</td>
<td align="right">2,533,651</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,048,693</td>
<td align="right">2,357,673</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">15,510,603</td>
<td align="right">12,019,514</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,330,831</td>
<td align="right">1,823,848</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,188,687</td>
<td align="right">3,306,672</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,126,777</td>
<td align="right">1,686,473</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,884,561</td>
<td align="right">1,497,926</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,034,031</td>
<td align="right">3,209,340</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,803,379</td>
<td align="right">24,513,838</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,777,802</td>
<td align="right">3,836,082</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,817,571</td>
<td align="right">19,979,185</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,277,902</td>
<td align="right">1,034,191</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,329,617</td>
<td align="right">1,078,898</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,404,299</td>
<td align="right">1,147,279</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,404,299</td>
<td align="right">1,147,279</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">964,663</td>
<td align="right">790,165</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,695,628</td>
<td align="right">6,313,614</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,341,307</td>
<td align="right">5,209,298</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,074,466</td>
<td align="right">887,435</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,145,642</td>
<td align="right">953,081</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,913,151</td>
<td align="right">1,604,273</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,520,937</td>
<td align="right">3,955,819</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,520,937</td>
<td align="right">3,955,819</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">595,780</td>
<td align="right">537,622</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">655,612</td>
<td align="right">591,926</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">658,848</td>
<td align="right">595,162</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,343,623</td>
<td align="right">4,650,802</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,210,028</td>
<td align="right">2,151,867</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,614,477</td>
<td align="right">2,556,316</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,579</td>
<td align="right">399,581</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-03-19
