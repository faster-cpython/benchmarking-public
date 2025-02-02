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
<td align="left">JUMP_BACKWARD</td>
<td align="right">43,931</td>
<td align="right">95,676</td>
<td align="right">117.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,396</td>
<td align="right">7,976</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">332,597</td>
<td align="right">566,246</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">683,432</td>
<td align="right">1,155,225</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">686,174</td>
<td align="right">1,153,494</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,319,593</td>
<td align="right">3,877,900</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">232,666</td>
<td align="right">388,450</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">353,722</td>
<td align="right">590,290</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">935,936</td>
<td align="right">1,559,164</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">711,924</td>
<td align="right">1,182,323</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,099,198</td>
<td align="right">5,125,807</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">964,173</td>
<td align="right">1,587,403</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">483,018</td>
<td align="right">794,689</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">745,248</td>
<td align="right">1,212,886</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">373,645</td>
<td align="right">607,411</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">251,349</td>
<td align="right">408,506</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">251,411</td>
<td align="right">408,568</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,001,986</td>
<td align="right">1,625,216</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">770,375</td>
<td align="right">1,248,878</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">753,997</td>
<td align="right">1,221,833</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">503,168</td>
<td align="right">815,132</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,681</td>
<td align="right">34,944</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">382,918</td>
<td align="right">616,645</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">644,680</td>
<td align="right">1,036,364</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">133,234</td>
<td align="right">213,955</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,063,420</td>
<td align="right">1,694,024</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">554,932</td>
<td align="right">871,687</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">142,399</td>
<td align="right">221,691</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,589,600</td>
<td align="right">2,451,064</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,203,416</td>
<td align="right">6,402,573</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,201,291</td>
<td align="right">4,864,240</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,311,219</td>
<td align="right">12,570,501</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,014,003</td>
<td align="right">9,089,257</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">152,473</td>
<td align="right">230,386</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,091</td>
<td align="right">33,283</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,482,874</td>
<td align="right">8,236,417</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,478,597</td>
<td align="right">2,203,401</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,327,426</td>
<td align="right">1,970,008</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,097,081</td>
<td align="right">4,583,117</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,502</td>
<td align="right">12,562</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">173,048</td>
<td align="right">254,446</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,246,525</td>
<td align="right">6,200,611</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,500,805</td>
<td align="right">10,897,272</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,337,651</td>
<td align="right">4,752,799</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,085,161</td>
<td align="right">2,960,621</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,588,112</td>
<td align="right">5,087,923</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,166,206</td>
<td align="right">1,632,096</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">44,394,471</td>
<td align="right">61,590,953</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,349,152</td>
<td align="right">3,230,958</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,022,526</td>
<td align="right">2,748,471</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,260,673</td>
<td align="right">3,066,495</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,330,831</td>
<td align="right">24,758,549</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,580,297</td>
<td align="right">12,854,052</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">756,672</td>
<td align="right">1,009,665</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,731</td>
<td align="right">11,636</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">8,731</td>
<td align="right">11,636</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,400,657</td>
<td align="right">20,456,235</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,743,621</td>
<td align="right">2,301,026</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">767,408</td>
<td align="right">1,001,078</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">10,496,664</td>
<td align="right">13,687,702</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,110,784</td>
<td align="right">2,734,526</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,052,292</td>
<td align="right">3,929,842</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,043,324</td>
<td align="right">12,916,577</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15</td>
<td align="right">19</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,818,073</td>
<td align="right">2,294,752</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">914,707</td>
<td align="right">1,154,326</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,728</td>
<td align="right">15,923</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,323,563</td>
<td align="right">17,817,106</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,495,064</td>
<td align="right">6,748,769</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">716,430</td>
<td align="right">877,832</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,142</td>
<td align="right">11,020</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">39,010</td>
<td align="right">46,750</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">433,885</td>
<td align="right">515,822</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,266,812</td>
<td align="right">8,590,857</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,997,851</td>
<td align="right">3,436,343</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,015</td>
<td align="right">29,779</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,189,720</td>
<td align="right">9,327,319</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">589,942</td>
<td align="right">671,563</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66,670</td>
<td align="right">75,625</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,702</td>
<td align="right">32,060</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">146,973</td>
<td align="right">163,490</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">26,276</td>
<td align="right">29,181</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">139</td>
<td align="right">150</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,856</td>
<td align="right">5,190</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,455,185</td>
<td align="right">1,537,514</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">184,847</td>
<td align="right">192,944</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">93</td>
<td align="right">97</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,277</td>
<td align="right">155,439</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">94,468</td>
<td align="right">98,186</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">89,341</td>
<td align="right">92,770</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">50,952</td>
<td align="right">52,588</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,254</td>
<td align="right">13,590</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">92</td>
<td align="right">94</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,477</td>
<td align="right">17,813</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,477</td>
<td align="right">17,813</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">368</td>
<td align="right">375</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">456</td>
<td align="right">463</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,625</td>
<td align="right">37,186</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,966</td>
<td align="right">38,462</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,447</td>
<td align="right">4,492</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,692</td>
<td align="right">20,894</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">892,609</td>
<td align="right">901,220</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">443,602</td>
<td align="right">447,642</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">489,421</td>
<td align="right">493,819</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,127</td>
<td align="right">3,154</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">29,925</td>
<td align="right">30,082</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">300,203</td>
<td align="right">300,681</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,184</td>
<td align="right">9,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,467</td>
<td align="right">21,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,831</td>
<td align="right">12,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,864</td>
<td align="right">43,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,032</td>
<td align="right">34,035</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,693</td>
<td align="right">84,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,547</td>
<td align="right">29,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,041</td>
<td align="right">81,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,873</td>
<td align="right">42,875</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,107</td>
<td align="right">105,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,651</td>
<td align="right">1,818,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,067,766</td>
<td align="right">5,067,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">105,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">77,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">67,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">55,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,466</td>
<td align="right">55,466</td>
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
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
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
<td align="right">12,855</td>
<td align="right">12,855</td>
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
<td align="right">9,101</td>
<td align="right">9,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">8,485</td>
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
<td align="right">742</td>
<td align="right">742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">191</td>
<td align="right">191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">179</td>
<td align="right">179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">152</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">146</td>
<td align="right">146</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
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
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14</td>
<td align="right">14</td>
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
<td align="left">BINARY_SUBSCR_GETITEM</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,097,336</td>
<td align="right">68.8%</td>
<td align="right">5,123,355</td>
<td align="right">73.8%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,400,559</td>
<td align="right">31.1%</td>
<td align="right">1,820,676</td>
<td align="right">26.2%</td>
<td align="right">30.0%</td>
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
<td align="right">141</td>
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
<td align="right">1,746</td>
<td align="right">100.0%</td>
<td align="right">2,335</td>
<td align="right">100.0%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">or</td>
<td align="right">463</td>
<td align="right">26.5%</td>
<td align="right">681</td>
<td align="right">29.2%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">800</td>
<td align="right">45.8%</td>
<td align="right">1,156</td>
<td align="right">49.5%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">191</td>
<td align="right">10.9%</td>
<td align="right">202</td>
<td align="right">8.7%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">205</td>
<td align="right">11.7%</td>
<td align="right">209</td>
<td align="right">9.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">5.0%</td>
<td align="right">87</td>
<td align="right">3.7%</td>
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
<td align="right">12,855</td>
<td align="right">100.0%</td>
<td align="right">12,855</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

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
<td align="right">439,186</td>
<td align="right">92.3%</td>
<td align="right">594,970</td>
<td align="right">94.1%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,330</td>
<td align="right">7.6%</td>
<td align="right">36,902</td>
<td align="right">5.8%</td>
<td align="right">1.6%</td>
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
<td align="right">178</td>
<td align="right">60.3%</td>
<td align="right">167</td>
<td align="right">58.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">39.7%</td>
<td align="right">117</td>
<td align="right">41.2%</td>
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
<td align="left">buffer int</td>
<td align="right">177</td>
<td align="right">99.4%</td>
<td align="right">166</td>
<td align="right">99.4%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.6%</td>
<td align="right">1</td>
<td align="right">0.6%</td>
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
<td align="right">16,946,847</td>
<td align="right">100.0%</td>
<td align="right">24,116,164</td>
<td align="right">100.0%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,155</td>
<td align="right">0.0%</td>
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
<td align="right">516</td>
<td align="right">0.0%</td>
<td align="right">510</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">3,447</td>
<td align="right">100.0%</td>
<td align="right">3,475</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">41</td>
<td align="right">22.9%</td>
<td align="right">41</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
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
<td align="right">372,972</td>
<td align="right">9.8%</td>
<td align="right">606,660</td>
<td align="right">12.2%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,430,395</td>
<td align="right">90.1%</td>
<td align="right">4,365,794</td>
<td align="right">87.7%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,277</td>
<td align="right">0.1%</td>
<td align="right">4,390</td>
<td align="right">0.1%</td>
<td align="right">2.6%</td>
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
<td align="right">407</td>
<td align="right">55.0%</td>
<td align="right">482</td>
<td align="right">58.6%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">333</td>
<td align="right">45.0%</td>
<td align="right">341</td>
<td align="right">41.4%</td>
<td align="right">2.4%</td>
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
<td align="right">209</td>
<td align="right">51.4%</td>
<td align="right">280</td>
<td align="right">58.1%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">103</td>
<td align="right">25.3%</td>
<td align="right">107</td>
<td align="right">22.2%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">23.3%</td>
<td align="right">95</td>
<td align="right">19.7%</td>
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
<td align="right">1,207,881</td>
<td align="right">100.0%</td>
<td align="right">1,753,057</td>
<td align="right">100.0%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
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
<td align="right">21,788</td>
<td align="right">0.4%</td>
<td align="right">32,987</td>
<td align="right">0.6%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,454,940</td>
<td align="right">99.6%</td>
<td align="right">5,948,584</td>
<td align="right">99.4%</td>
<td align="right">9.0%</td>
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
<td align="right">47</td>
<td align="right">15.5%</td>
<td align="right">51</td>
<td align="right">17.2%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">256</td>
<td align="right">84.5%</td>
<td align="right">245</td>
<td align="right">82.8%</td>
<td align="right">-4.3%</td>
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
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">75</td>
<td align="right">30.6%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">33</td>
<td align="right">13.5%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">72</td>
<td align="right">28.1%</td>
<td align="right">54</td>
<td align="right">22.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">70</td>
<td align="right">28.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">7</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">4,236,781</td>
<td align="right">12.2%</td>
<td align="right">6,190,235</td>
<td align="right">13.0%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,222,127</td>
<td align="right">86.8%</td>
<td align="right">41,076,475</td>
<td align="right">86.3%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">333,964</td>
<td align="right">1.0%</td>
<td align="right">340,460</td>
<td align="right">0.7%</td>
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
<td align="right">5,097</td>
<td align="right">32.4%</td>
<td align="right">5,659</td>
<td align="right">34.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,658</td>
<td align="right">67.6%</td>
<td align="right">10,899</td>
<td align="right">65.8%</td>
<td align="right">2.3%</td>
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
<td align="right">1,108</td>
<td align="right">21.7%</td>
<td align="right">1,512</td>
<td align="right">26.7%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">665</td>
<td align="right">13.0%</td>
<td align="right">731</td>
<td align="right">12.9%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,346</td>
<td align="right">26.4%</td>
<td align="right">1,353</td>
<td align="right">23.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">13.4%</td>
<td align="right">681</td>
<td align="right">12.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.0%</td>
<td align="right">460</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.4%</td>
<td align="right">71</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.3%</td>
<td align="right">68</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">45</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">11,899,057</td>
<td align="right">100.0%</td>
<td align="right">17,658,150</td>
<td align="right">100.0%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">794</td>
<td align="right">0.0%</td>
<td align="right">805</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
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
<td align="right">274</td>
<td align="right">0.0%</td>
<td align="right">274</td>
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
<td align="right">2,342</td>
<td align="right">100.0%</td>
<td align="right">2,358</td>
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
<td align="right">1,283,715</td>
<td align="right">100.0%</td>
<td align="right">2,140,454</td>
<td align="right">100.0%</td>
<td align="right">66.7%</td>
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
<td align="right">3,506,071</td>
<td align="right">94.1%</td>
<td align="right">5,063,884</td>
<td align="right">95.8%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,406</td>
<td align="right">2.1%</td>
<td align="right">79,408</td>
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
<td align="right">140,654</td>
<td align="right">3.8%</td>
<td align="right">140,654</td>
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
<td align="right">3,615</td>
<td align="right">84.6%</td>
<td align="right">3,617</td>
<td align="right">84.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">656</td>
<td align="right">15.4%</td>
<td align="right">656</td>
<td align="right">15.4%</td>
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
<td align="left">property</td>
<td align="right">344</td>
<td align="right">52.4%</td>
<td align="right">344</td>
<td align="right">52.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">163</td>
<td align="right">24.8%</td>
<td align="right">163</td>
<td align="right">24.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">139</td>
<td align="right">21.2%</td>
<td align="right">139</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.5%</td>
<td align="right">10</td>
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
<td align="right">1,274,199</td>
<td align="right">98.3%</td>
<td align="right">1,817,926</td>
<td align="right">98.8%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,262</td>
<td align="right">1.6%</td>
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
<td align="right">20</td>
<td align="right">9.7%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.2%</td>
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
<td align="right">7,546,553</td>
<td align="right">99.1%</td>
<td align="right">11,850,891</td>
<td align="right">99.4%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">65,695</td>
<td align="right">0.9%</td>
<td align="right">74,602</td>
<td align="right">0.6%</td>
<td align="right">13.6%</td>
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
<td align="right">533</td>
<td align="right">54.7%</td>
<td align="right">573</td>
<td align="right">56.0%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">442</td>
<td align="right">45.3%</td>
<td align="right">450</td>
<td align="right">44.0%</td>
<td align="right">1.8%</td>
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
<td align="right">118</td>
<td align="right">22.1%</td>
<td align="right">143</td>
<td align="right">25.0%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">174</td>
<td align="right">32.6%</td>
<td align="right">195</td>
<td align="right">34.0%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">130</td>
<td align="right">24.4%</td>
<td align="right">124</td>
<td align="right">21.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">12.8%</td>
<td align="right">68</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">43</td>
<td align="right">8.1%</td>
<td align="right">43</td>
<td align="right">7.5%</td>
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
<td align="right">1,973,452</td>
<td align="right">100.0%</td>
<td align="right">2,129,302</td>
<td align="right">100.0%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">36</td>
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
<td align="right">110</td>
<td align="right">100.0%</td>
<td align="right">110</td>
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
<td align="right">7,968,098</td>
<td align="right">3.1%</td>
<td align="right">12,203,347</td>
<td align="right">3.5%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">88,350,286</td>
<td align="right">34.8%</td>
<td align="right">123,392,477</td>
<td align="right">35.7%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">157,404,072</td>
<td align="right">61.9%</td>
<td align="right">209,288,896</td>
<td align="right">60.6%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">479,787</td>
<td align="right">0.2%</td>
<td align="right">486,537</td>
<td align="right">0.1%</td>
<td align="right">1.4%</td>
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
<td align="right">3,097,336</td>
<td align="right">39.0%</td>
<td align="right">5,123,355</td>
<td align="right">42.1%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">372,972</td>
<td align="right">4.7%</td>
<td align="right">606,660</td>
<td align="right">5.0%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,788</td>
<td align="right">0.3%</td>
<td align="right">32,987</td>
<td align="right">0.3%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,236,781</td>
<td align="right">53.3%</td>
<td align="right">6,190,235</td>
<td align="right">50.8%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">65,695</td>
<td align="right">0.8%</td>
<td align="right">74,602</td>
<td align="right">0.6%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,330</td>
<td align="right">0.5%</td>
<td align="right">36,902</td>
<td align="right">0.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,155</td>
<td align="right">0.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,262</td>
<td align="right">0.3%</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,406</td>
<td align="right">1.0%</td>
<td align="right">79,408</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.2%</td>
<td align="right">12,855</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,276</td>
<td align="right">0.9%</td>
<td align="right">4,389</td>
<td align="right">0.9%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">274,375</td>
<td align="right">57.2%</td>
<td align="right">280,924</td>
<td align="right">57.7%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,539</td>
<td align="right">10.3%</td>
<td align="right">49,486</td>
<td align="right">10.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">140,654</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
<td align="right">9,895</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">141</td>
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
<td align="right">362,909</td>
<td align="right">1.5%</td>
<td align="right">518,652</td>
<td align="right">1.6%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,977,659</td>
<td align="right">79.9%</td>
<td align="right">27,459,348</td>
<td align="right">84.5%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">17,731,622</td>
<td align="right">70.9%</td>
<td align="right">23,889,266</td>
<td align="right">73.5%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,844,257</td>
<td align="right">27.4%</td>
<td align="right">8,168,302</td>
<td align="right">25.1%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,844,313</td>
<td align="right">27.4%</td>
<td align="right">8,168,358</td>
<td align="right">25.1%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,271,170</td>
<td align="right">29.1%</td>
<td align="right">8,595,215</td>
<td align="right">26.5%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,271,170</td>
<td align="right">29.1%</td>
<td align="right">8,595,215</td>
<td align="right">26.5%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,488</td>
<td align="right">0.1%</td>
<td align="right">17,824</td>
<td align="right">0.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.7%</td>
<td align="right">426,857</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.8%</td>
<td align="right">456,471</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">1.8%</td>
<td align="right">441,507</td>
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
<td align="left">Inline values</td>
<td align="right">1,066,340</td>
<td align="right"></td>
<td align="right">1,689,466</td>
<td align="right"></td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">94,661</td>
<td align="right"></td>
<td align="right">41,209</td>
<td align="right"></td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">6,547,991</td>
<td align="right"></td>
<td align="right">10,113,656</td>
<td align="right"></td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,229,964</td>
<td align="right">13.8%</td>
<td align="right">73,789,558</td>
<td align="right">14.9%</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">39,456,382</td>
<td align="right">12.8%</td>
<td align="right">56,278,368</td>
<td align="right">13.7%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,062,954</td>
<td align="right">48.7%</td>
<td align="right">19,253,343</td>
<td align="right">50.8%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,065,752</td>
<td align="right"></td>
<td align="right">19,256,054</td>
<td align="right"></td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">49,320,430</td>
<td align="right">16.1%</td>
<td align="right">67,470,416</td>
<td align="right">16.4%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">135,125,459</td>
<td align="right">36.5%</td>
<td align="right">183,482,608</td>
<td align="right">37.1%</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">103,021,379</td>
<td align="right">33.5%</td>
<td align="right">138,180,468</td>
<td align="right">33.6%</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">74,194,445</td>
<td align="right">20.0%</td>
<td align="right">98,747,698</td>
<td align="right">20.0%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,248,421</td>
<td align="right"></td>
<td align="right">12,200,213</td>
<td align="right"></td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">143,025</td>
<td align="right"></td>
<td align="right">97,528</td>
<td align="right"></td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">115,354,699</td>
<td align="right">37.6%</td>
<td align="right">149,248,400</td>
<td align="right">36.3%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,690,081</td>
<td align="right"></td>
<td align="right">20,052,563</td>
<td align="right"></td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">109,669,899</td>
<td align="right">29.6%</td>
<td align="right">138,360,465</td>
<td align="right">28.0%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">14,688,443</td>
<td align="right">50.9%</td>
<td align="right">18,507,176</td>
<td align="right">48.9%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">14,809,804</td>
<td align="right">51.3%</td>
<td align="right">18,628,715</td>
<td align="right">49.2%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">48,648</td>
<td align="right"></td>
<td align="right">56,602</td>
<td align="right"></td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,828</td>
<td align="right">0.3%</td>
<td align="right">77,994</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,533</td>
<td align="right">0.2%</td>
<td align="right">43,545</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.1%</td>
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
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
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
</tr>
<tr>
<td align="right">1</td>
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
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">17</td>
<td align="right">0.4%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">360</td>
<td align="right">9.9%</td>
<td align="right">770</td>
<td align="right">17.2%</td>
<td align="right">113.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">351,586,730</td>
<td align="right">1,692.1%</td>
<td align="right">441,915,012</td>
<td align="right">1,925.2%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,627</td>
<td align="right"></td>
<td align="right">4,488</td>
<td align="right"></td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,083</td>
<td align="right">85.0%</td>
<td align="right">3,742</td>
<td align="right">83.4%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">205</td>
<td align="right">5.7%</td>
<td align="right">236</td>
<td align="right">5.3%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,062</td>
<td align="right">84.4%</td>
<td align="right">3,482</td>
<td align="right">77.6%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">20,777,825</td>
<td align="right"></td>
<td align="right">22,954,275</td>
<td align="right"></td>
<td align="right">10.5%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">356</td>
<td align="right">98.9%</td>
<td align="right">770</td>
<td align="right">100.0%</td>
<td align="right">116.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">360</td>
<td align="right"></td>
<td align="right">770</td>
<td align="right"></td>
<td align="right">113.9%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">4</td>
<td align="right">1.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
</tbody>
</table>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">101</td>
<td align="right">28.1%</td>
<td align="right">213</td>
<td align="right">27.7%</td>
<td align="right">110.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">6.1%</td>
<td align="right">64</td>
<td align="right">8.3%</td>
<td align="right">190.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">65</td>
<td align="right">18.1%</td>
<td align="right">197</td>
<td align="right">25.6%</td>
<td align="right">203.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">116</td>
<td align="right">32.2%</td>
<td align="right">110</td>
<td align="right">14.3%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24</td>
<td align="right">6.7%</td>
<td align="right">146</td>
<td align="right">19.0%</td>
<td align="right">508.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">31</td>
<td align="right">8.6%</td>
<td align="right">36</td>
<td align="right">4.7%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">300.0%</td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">9</td>
<td align="right">2.5%</td>
<td align="right">44</td>
<td align="right">5.7%</td>
<td align="right">388.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">108</td>
<td align="right">30.0%</td>
<td align="right">230</td>
<td align="right">29.9%</td>
<td align="right">113.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">29</td>
<td align="right">8.1%</td>
<td align="right">46</td>
<td align="right">6.0%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">93</td>
<td align="right">25.8%</td>
<td align="right">220</td>
<td align="right">28.6%</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">76</td>
<td align="right">21.1%</td>
<td align="right">117</td>
<td align="right">15.2%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">38</td>
<td align="right">10.6%</td>
<td align="right">74</td>
<td align="right">9.6%</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">39</td>
<td align="right">5.1%</td>
<td align="right">1,200.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60,911</td>
<td align="right">615,920</td>
<td align="right">911.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,077</td>
<td align="right">62</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">323,979</td>
<td align="right">557,490</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">323,979</td>
<td align="right">557,490</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">107,993</td>
<td align="right">185,830</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">323,981</td>
<td align="right">557,490</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">323,981</td>
<td align="right">557,490</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">323,985</td>
<td align="right">557,490</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,080,118</td>
<td align="right">1,858,343</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">540,153</td>
<td align="right">929,193</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">324,167</td>
<td align="right">557,533</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,031</td>
<td align="right">185,788</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">432,265</td>
<td align="right">743,361</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">108,092</td>
<td align="right">185,867</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,192,278</td>
<td align="right">2,045,631</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,088,242</td>
<td align="right">1,860,929</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">439,942</td>
<td align="right">745,915</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,221,350</td>
<td align="right">2,067,589</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">336,237</td>
<td align="right">566,367</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,023,405</td>
<td align="right">1,715,561</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">112,010</td>
<td align="right">187,171</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">228,250</td>
<td align="right">380,839</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">11,921</td>
<td align="right">4,181</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">234,860</td>
<td align="right">386,697</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">590,950</td>
<td align="right">971,895</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,642,595</td>
<td align="right">2,696,566</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">964,241</td>
<td align="right">1,566,404</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,736,812</td>
<td align="right">2,795,772</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">240,629</td>
<td align="right">386,403</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">365,241</td>
<td align="right">585,655</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">365,241</td>
<td align="right">585,655</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,341</td>
<td align="right">5,797</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,597,954</td>
<td align="right">5,724,456</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,870,831</td>
<td align="right">4,558,771</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,870,831</td>
<td align="right">4,558,771</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">122,508</td>
<td align="right">194,285</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,546,664</td>
<td align="right">4,001,238</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">513,737</td>
<td align="right">799,828</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,079,130</td>
<td align="right">3,232,524</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,847,178</td>
<td align="right">2,848,932</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,350,082</td>
<td align="right">6,706,385</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,009,694</td>
<td align="right">6,137,267</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,851,248</td>
<td align="right">7,408,647</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,495,957</td>
<td align="right">5,337,439</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">3,045</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">3,045</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,385</td>
<td align="right">3,045</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">3,045</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">3,045</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">6,385</td>
<td align="right">3,045</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,641,929</td>
<td align="right">5,543,808</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,430,613</td>
<td align="right">9,746,382</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,518,816</td>
<td align="right">2,291,541</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,160</td>
<td align="right">218,213</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,421,396</td>
<td align="right">2,108,875</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,455,960</td>
<td align="right">2,135,659</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,504,625</td>
<td align="right">3,562,388</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,110,873</td>
<td align="right">1,565,646</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">952,148</td>
<td align="right">1,337,039</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">9,965,350</td>
<td align="right">13,835,440</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,806,710</td>
<td align="right">2,503,326</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,961,153</td>
<td align="right">4,097,375</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,812,899</td>
<td align="right">2,505,953</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">44,035</td>
<td align="right">27,521</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,598,284</td>
<td align="right">11,797,505</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">862,213</td>
<td align="right">1,164,606</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,151</td>
<td align="right">2,751</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,151</td>
<td align="right">2,751</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">4,151</td>
<td align="right">2,751</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,151</td>
<td align="right">2,751</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,151</td>
<td align="right">2,751</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,384,235</td>
<td align="right">1,766,261</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">811,367</td>
<td align="right">1,034,160</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">967,818</td>
<td align="right">1,230,413</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,030,921</td>
<td align="right">8,914,284</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,047,696</td>
<td align="right">8,930,796</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">8,995,322</td>
<td align="right">11,347,565</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,299,348</td>
<td align="right">26,478,714</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">29,802,217</td>
<td align="right">37,044,567</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,536,097</td>
<td align="right">3,147,030</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,272,080</td>
<td align="right">1,576,184</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">655,039</td>
<td align="right">805,049</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">655,045</td>
<td align="right">805,049</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,775,484</td>
<td align="right">10,770,278</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,341,658</td>
<td align="right">1,638,638</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">8,564</td>
<td align="right">6,686</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">8,564</td>
<td align="right">6,686</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,382,229</td>
<td align="right">10,145,539</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,510,690</td>
<td align="right">3,034,025</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,332,224</td>
<td align="right">7,489,441</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,332,224</td>
<td align="right">7,489,441</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,859,852</td>
<td align="right">3,376,492</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,746,235</td>
<td align="right">2,044,799</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">16,379</td>
<td align="right">13,613</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,280,192</td>
<td align="right">1,491,417</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">523,797</td>
<td align="right">601,319</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">526,251</td>
<td align="right">600,458</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">524,352</td>
<td align="right">597,735</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">536,209</td>
<td align="right">609,699</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,058,738</td>
<td align="right">1,203,814</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">536,268</td>
<td align="right">609,751</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">540,543</td>
<td align="right">612,320</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">540,543</td>
<td align="right">612,320</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,363,612</td>
<td align="right">17,314,576</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">564,021</td>
<td align="right">634,810</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">18,499,393</td>
<td align="right">20,719,241</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,244,251</td>
<td align="right">9,227,136</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">59</td>
<td align="right">52</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59</td>
<td align="right">52</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,299,474</td>
<td align="right">2,562,120</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,639,504</td>
<td align="right">2,935,869</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,639,504</td>
<td align="right">2,935,869</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">601,123</td>
<td align="right">665,384</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">21,378,948</td>
<td align="right">23,619,659</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">20,777,825</td>
<td align="right">22,954,275</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,290,943</td>
<td align="right">5,749,946</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,775,150</td>
<td align="right">5,157,955</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">191</td>
<td align="right">180</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,990,964</td>
<td align="right">6,290,572</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,366,327</td>
<td align="right">1,432,012</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">60,907</td>
<td align="right">58,002</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60,907</td>
<td align="right">58,002</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">60,907</td>
<td align="right">58,002</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">61,094</td>
<td align="right">58,182</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">189</td>
<td align="right">180</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,397,366</td>
<td align="right">5,623,109</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,649,521</td>
<td align="right">2,712,966</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">418,255</td>
<td align="right">410,867</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">16,775</td>
<td align="right">16,512</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,847</td>
<td align="right">16,590</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">415,913</td>
<td align="right">410,471</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">918,323</td>
<td align="right">907,124</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">411,762</td>
<td align="right">407,720</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">422,270</td>
<td align="right">418,690</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">829,765</td>
<td align="right">824,573</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">411,718</td>
<td align="right">410,082</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,645,240</td>
<td align="right">4,641,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">411,776</td>
<td align="right">411,488</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">823,550</td>
<td align="right">822,976</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">411,730</td>
<td align="right">411,488</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">819,293</td>
<td align="right">818,819</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">411,726</td>
<td align="right">411,488</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">21</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">6</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">186,031</td>
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
<td align="right">156</td>
<td align="right">155</td>
<td align="right">-0.6%</td>
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
Stats gathered on: 2024-11-11
