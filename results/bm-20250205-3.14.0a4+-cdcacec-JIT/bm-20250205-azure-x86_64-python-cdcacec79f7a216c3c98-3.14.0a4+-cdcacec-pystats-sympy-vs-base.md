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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">123,981,687</td>
<td align="right">2,418,434</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,016,950</td>
<td align="right">2,825,182</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,978,554</td>
<td align="right">2,069,747</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,421,970</td>
<td align="right">5,720,916</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,353,480</td>
<td align="right">4,552,963</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,500,890</td>
<td align="right">15,286,685</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,098</td>
<td align="right">886,101</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,989,937</td>
<td align="right">3,431,328</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,532,266</td>
<td align="right">33,530,916</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,089,413</td>
<td align="right">3,429,627</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">18,498,758</td>
<td align="right">8,265,770</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,012,726</td>
<td align="right">5,049,160</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,101,740</td>
<td align="right">5,172,460</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,624,007</td>
<td align="right">17,488,810</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,023,974</td>
<td align="right">41,879,764</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,532,407</td>
<td align="right">43,946,187</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">50,013,995</td>
<td align="right">26,537,795</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,411,394</td>
<td align="right">5,009,286</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">30,485,816</td>
<td align="right">16,296,818</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,325,035</td>
<td align="right">1,788,414</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,029,655</td>
<td align="right">2,201,978</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,134,150</td>
<td align="right">15,255,369</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,241,859</td>
<td align="right">3,728,253</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">77,962,952</td>
<td align="right">50,323,011</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">23,933,917</td>
<td align="right">15,493,581</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,631,963</td>
<td align="right">12,107,086</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,126,113</td>
<td align="right">15,282,431</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">36,549,258</td>
<td align="right">24,436,121</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,313,978</td>
<td align="right">12,801,746</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">198,345,480</td>
<td align="right">140,842,162</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">280,971,260</td>
<td align="right">203,171,632</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,837,120</td>
<td align="right">32,823,641</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,269,784</td>
<td align="right">13,399,985</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,098,752</td>
<td align="right">29,766,684</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,744,744</td>
<td align="right">18,441,932</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,097,983</td>
<td align="right">85,018,908</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,046,797</td>
<td align="right">40,062,584</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,299</td>
<td align="right">1,521,819</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">25,930,514</td>
<td align="right">19,934,937</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">78,194,883</td>
<td align="right">60,267,836</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,813,998</td>
<td align="right">41,221,545</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">758,710,130</td>
<td align="right">597,610,267</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,204</td>
<td align="right">21,098,227</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">23,379,640</td>
<td align="right">18,591,340</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,306,363</td>
<td align="right">2,676,000</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,551,958</td>
<td align="right">61,554,489</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">211,618,925</td>
<td align="right">172,428,725</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,114,430</td>
<td align="right">43,367,006</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,946,623</td>
<td align="right">60,520,764</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,423,855</td>
<td align="right">25,938,449</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,437,503</td>
<td align="right">30,248,458</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,228,074</td>
<td align="right">171,105,766</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,704</td>
<td align="right">3,439,128</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,297,694</td>
<td align="right">42,394,144</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">134,034,936</td>
<td align="right">115,462,889</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,709,374</td>
<td align="right">10,956,257</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">64,292,420</td>
<td align="right">55,918,184</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,231,318</td>
<td align="right">23,319,075</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,810,204</td>
<td align="right">159,504,635</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,162,754</td>
<td align="right">11,877,445</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">115,540,793</td>
<td align="right">104,337,352</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,146,000</td>
<td align="right">30,305,866</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,178</td>
<td align="right">6,228,234</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,382</td>
<td align="right">16,050,122</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,076,786</td>
<td align="right">17,719,469</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,638,987</td>
<td align="right">43,428,487</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,695,754</td>
<td align="right">20,337,853</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">37,022,676</td>
<td align="right">34,721,110</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,942,143</td>
<td align="right">16,039,517</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,694,300</td>
<td align="right">3,550,185</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">62</td>
<td align="right">60</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,006</td>
<td align="right">1,758,922</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,830,510</td>
<td align="right">6,643,463</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,189,925</td>
<td align="right">26,538,690</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,713,530</td>
<td align="right">4,609,919</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">46,989,024</td>
<td align="right">46,180,919</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,929</td>
<td align="right">9,939,129</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,756</td>
<td align="right">456,591</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,542</td>
<td align="right">21,740,553</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,740,714</td>
<td align="right">15,567,887</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,616,814</td>
<td align="right">2,588,390</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,501,425</td>
<td align="right">17,651,428</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,204</td>
<td align="right">18,077</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,614,378</td>
<td align="right">4,587,592</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,985,936</td>
<td align="right">15,913,653</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,982</td>
<td align="right">2,971</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,282</td>
<td align="right">24,197</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,234</td>
<td align="right">7,517,293</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,756,161</td>
<td align="right">17,718,567</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,002</td>
<td align="right">17,029</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,447</td>
<td align="right">1,445</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">920</td>
<td align="right">919</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,749,767</td>
<td align="right">97,842,403</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,545</td>
<td align="right">165,667</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,223,246</td>
<td align="right">1,222,397</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,311</td>
<td align="right">493,634</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,963</td>
<td align="right">10,970</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,563</td>
<td align="right">147,641</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,290</td>
<td align="right">40,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,287,615</td>
<td align="right">1,288,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,231</td>
<td align="right">655,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,231</td>
<td align="right">655,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,231</td>
<td align="right">655,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,062,096</td>
<td align="right">182,016,770</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,708</td>
<td align="right">744,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,024,327</td>
<td align="right">6,025,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,883</td>
<td align="right">389,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,881</td>
<td align="right">171,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,261</td>
<td align="right">6,590,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,253</td>
<td align="right">6,623,015</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,752,812</td>
<td align="right">5,753,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,386</td>
<td align="right">654,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,402</td>
<td align="right">654,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,017</td>
<td align="right">9,016</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,311</td>
<td align="right">4,497,795</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,075</td>
<td align="right">4,469,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,663</td>
<td align="right">1,389,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,682</td>
<td align="right">20,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,667</td>
<td align="right">1,966,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,300</td>
<td align="right">746,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,111</td>
<td align="right">83,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,877</td>
<td align="right">745,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,210</td>
<td align="right">2,281,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,665</td>
<td align="right">78,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,317</td>
<td align="right">175,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,916,494</td>
<td align="right">10,916,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,457</td>
<td align="right">1,028,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,053</td>
<td align="right">1,029,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,623</td>
<td align="right">4,181,727</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,194</td>
<td align="right">1,323,177</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,638</td>
<td align="right">942,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,147</td>
<td align="right">21,977,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,549</td>
<td align="right">427,546</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,119</td>
<td align="right">2,195,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,353</td>
<td align="right">6,744,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,627</td>
<td align="right">597,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,463</td>
<td align="right">1,754,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,529</td>
<td align="right">1,244,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">389,282</td>
<td align="right">389,282</td>
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
<td align="right">339,309</td>
<td align="right">339,309</td>
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
<td align="right">178,536</td>
<td align="right">178,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,398</td>
<td align="right">141,398</td>
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
<td align="right">89,010</td>
<td align="right">89,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">14,629</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">8,858</td>
<td align="right">8,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">3,742</td>
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
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">1,455</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">68,955,186</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">18,675,014</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">1,393,988</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,166,846</td>
<td align="right">64.2%</td>
<td align="right">26,515,813</td>
<td align="right">63.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,953</td>
<td align="right">0.1%</td>
<td align="right">49,707</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,080,906</td>
<td align="right">35.6%</td>
<td align="right">15,082,654</td>
<td align="right">36.2%</td>
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
<td align="right">2,310</td>
<td align="right">9.6%</td>
<td align="right">2,258</td>
<td align="right">9.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,719</td>
<td align="right">90.4%</td>
<td align="right">21,564</td>
<td align="right">90.5%</td>
<td align="right">-0.7%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,353</td>
<td align="right">10.8%</td>
<td align="right">2,226</td>
<td align="right">10.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">94</td>
<td align="right">0.4%</td>
<td align="right">91</td>
<td align="right">0.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">738</td>
<td align="right">3.4%</td>
<td align="right">716</td>
<td align="right">3.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">206</td>
<td align="right">1.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">995</td>
<td align="right">4.6%</td>
<td align="right">1,007</td>
<td align="right">4.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">367</td>
<td align="right">1.7%</td>
<td align="right">363</td>
<td align="right">1.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">989</td>
<td align="right">4.6%</td>
<td align="right">982</td>
<td align="right">4.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,906</td>
<td align="right">13.4%</td>
<td align="right">2,893</td>
<td align="right">13.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,896</td>
<td align="right">17.9%</td>
<td align="right">3,912</td>
<td align="right">18.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">568</td>
<td align="right">2.6%</td>
<td align="right">566</td>
<td align="right">2.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">702</td>
<td align="right">3.2%</td>
<td align="right">703</td>
<td align="right">3.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.0%</td>
<td align="right">1,085</td>
<td align="right">5.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">14.8%</td>
<td align="right">3,221</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">10.2%</td>
<td align="right">2,225</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,213</td>
<td align="right">5.6%</td>
<td align="right">1,213</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.7%</td>
<td align="right">155</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">8,858</td>
<td align="right">100.0%</td>
<td align="right">8,858</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">18,490,281</td>
<td align="right">36.1%</td>
<td align="right">8,259,762</td>
<td align="right">20.1%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,752,185</td>
<td align="right">63.9%</td>
<td align="right">32,749,742</td>
<td align="right">79.8%</td>
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
<td align="right">10,759</td>
<td align="right">0.0%</td>
<td align="right">10,759</td>
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
<td align="right">7,689</td>
<td align="right">88.6%</td>
<td align="right">5,226</td>
<td align="right">84.2%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">988</td>
<td align="right">11.4%</td>
<td align="right">982</td>
<td align="right">15.8%</td>
<td align="right">-0.6%</td>
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
<td align="right">6,150</td>
<td align="right">80.0%</td>
<td align="right">3,687</td>
<td align="right">70.6%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">276</td>
<td align="right">3.6%</td>
<td align="right">277</td>
<td align="right">5.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">692</td>
<td align="right">9.0%</td>
<td align="right">691</td>
<td align="right">13.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">5.5%</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">1.9%</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">24,609,528</td>
<td align="right">7.7%</td>
<td align="right">24,726,792</td>
<td align="right">7.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">24,153,846</td>
<td align="right">7.5%</td>
<td align="right">24,268,865</td>
<td align="right">7.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">295,958,579</td>
<td align="right">92.3%</td>
<td align="right">295,928,096</td>
<td align="right">92.3%</td>
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
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
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
<td align="right">479,964</td>
<td align="right">100.0%</td>
<td align="right">482,124</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">3,185</td>
<td align="right">74.9%</td>
<td align="right">3,183</td>
<td align="right">74.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,067</td>
<td align="right">100.0%</td>
<td align="right">1,067</td>
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
<td align="right">30,385,272</td>
<td align="right">37.1%</td>
<td align="right">25,900,949</td>
<td align="right">33.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,033,096</td>
<td align="right">62.3%</td>
<td align="right">51,024,441</td>
<td align="right">65.9%</td>
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
<td align="right">409,699</td>
<td align="right">0.5%</td>
<td align="right">409,641</td>
<td align="right">0.5%</td>
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
<td align="left">Failure</td>
<td align="right">37,414</td>
<td align="right">80.9%</td>
<td align="right">36,330</td>
<td align="right">80.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,842</td>
<td align="right">19.1%</td>
<td align="right">8,843</td>
<td align="right">19.6%</td>
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
<td align="left">bool</td>
<td align="right">1,442</td>
<td align="right">3.9%</td>
<td align="right">399</td>
<td align="right">1.1%</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">139</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">117</td>
<td align="right">0.3%</td>
<td align="right">118</td>
<td align="right">0.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,459</td>
<td align="right">17.3%</td>
<td align="right">6,405</td>
<td align="right">17.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,149</td>
<td align="right">8.4%</td>
<td align="right">3,153</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,256</td>
<td align="right">11.4%</td>
<td align="right">4,258</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,101</td>
<td align="right">37.7%</td>
<td align="right">14,105</td>
<td align="right">38.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
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
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
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
<td align="right">17,346,429</td>
<td align="right">42.5%</td>
<td align="right">4,549,034</td>
<td align="right">16.2%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,615</td>
<td align="right">57.5%</td>
<td align="right">23,499,794</td>
<td align="right">83.8%</td>
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
<td align="right">6,929</td>
<td align="right">98.3%</td>
<td align="right">3,807</td>
<td align="right">96.9%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">1.7%</td>
<td align="right">122</td>
<td align="right">3.1%</td>
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
<td align="right">5,023</td>
<td align="right">72.5%</td>
<td align="right">1,898</td>
<td align="right">49.9%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,470</td>
<td align="right">21.2%</td>
<td align="right">1,473</td>
<td align="right">38.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">299</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">2.0%</td>
<td align="right">137</td>
<td align="right">3.6%</td>
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
<td align="right">83,532,079</td>
<td align="right">50.2%</td>
<td align="right">32,022,284</td>
<td align="right">48.3%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,472,290</td>
<td align="right">49.0%</td>
<td align="right">33,479,929</td>
<td align="right">50.5%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,229,078</td>
<td align="right">0.7%</td>
<td align="right">737,158</td>
<td align="right">1.1%</td>
<td align="right">-40.0%</td>
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
<td align="right">23,819</td>
<td align="right">28.7%</td>
<td align="right">14,538</td>
<td align="right">22.4%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,261</td>
<td align="right">71.3%</td>
<td align="right">50,284</td>
<td align="right">77.6%</td>
<td align="right">-15.1%</td>
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
<td align="right">6,299</td>
<td align="right">10.6%</td>
<td align="right">2,879</td>
<td align="right">5.7%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,200</td>
<td align="right">7.1%</td>
<td align="right">2,709</td>
<td align="right">5.4%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">45,434</td>
<td align="right">76.7%</td>
<td align="right">41,369</td>
<td align="right">82.3%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,334</td>
<td align="right">2.3%</td>
<td align="right">1,334</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.3%</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
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
<td align="right">78,130,071</td>
<td align="right">22.8%</td>
<td align="right">60,207,410</td>
<td align="right">18.5%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,298,121</td>
<td align="right">15.5%</td>
<td align="right">43,146,124</td>
<td align="right">13.3%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">211,616,707</td>
<td align="right">61.7%</td>
<td align="right">221,676,220</td>
<td align="right">68.2%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">18,588</td>
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
<td align="right">1,016,429</td>
<td align="right">95.3%</td>
<td align="right">824,845</td>
<td align="right">94.8%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">49,596</td>
<td align="right">4.7%</td>
<td align="right">45,202</td>
<td align="right">5.2%</td>
<td align="right">-8.9%</td>
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
<td align="left">builtin class method</td>
<td align="right">568</td>
<td align="right">1.1%</td>
<td align="right">245</td>
<td align="right">0.5%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,564</td>
<td align="right">9.2%</td>
<td align="right">3,013</td>
<td align="right">6.7%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,355</td>
<td align="right">8.8%</td>
<td align="right">3,165</td>
<td align="right">7.0%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,684</td>
<td align="right">5.4%</td>
<td align="right">2,361</td>
<td align="right">5.2%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,090</td>
<td align="right">14.3%</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,891</td>
<td align="right">44.1%</td>
<td align="right">21,182</td>
<td align="right">46.9%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,058</td>
<td align="right">8.2%</td>
<td align="right">4,043</td>
<td align="right">8.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,106</td>
<td align="right">6.3%</td>
<td align="right">3,099</td>
<td align="right">6.9%</td>
<td align="right">-0.2%</td>
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
<tr>
<td align="left">module attr not found</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">291,906,893</td>
<td align="right">100.0%</td>
<td align="right">245,791,862</td>
<td align="right">100.0%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,599</td>
<td align="right">0.0%</td>
<td align="right">4,543</td>
<td align="right">0.0%</td>
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
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,294</td>
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
<td align="right">13,653</td>
<td align="right">100.0%</td>
<td align="right">13,582</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,832</td>
<td align="right">100.0%</td>
<td align="right">2,265,827</td>
<td align="right">100.0%</td>
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
<td align="right">731,589</td>
<td align="right">72.0%</td>
<td align="right">731,656</td>
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
<td align="right">1,573,252</td>
<td align="right">17.3%</td>
<td align="right">1,577,712</td>
<td align="right">17.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,330,211</td>
<td align="right">80.7%</td>
<td align="right">7,326,659</td>
<td align="right">80.7%</td>
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
<td align="right">173,999</td>
<td align="right">1.9%</td>
<td align="right">174,007</td>
<td align="right">1.9%</td>
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
<td align="right">29,931</td>
<td align="right">96.8%</td>
<td align="right">30,007</td>
<td align="right">96.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">982</td>
<td align="right">3.2%</td>
<td align="right">980</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
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
<td align="right">304</td>
<td align="right">31.0%</td>
<td align="right">300</td>
<td align="right">30.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">52.7%</td>
<td align="right">518</td>
<td align="right">52.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.4%</td>
<td align="right">102</td>
<td align="right">10.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,582,977</td>
<td align="right">12.7%</td>
<td align="right">884,388</td>
<td align="right">4.7%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,399</td>
<td align="right">87.3%</td>
<td align="right">17,741,465</td>
<td align="right">95.2%</td>
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
<td align="right">1,543</td>
<td align="right">72.7%</td>
<td align="right">1,137</td>
<td align="right">66.4%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">578</td>
<td align="right">27.3%</td>
<td align="right">576</td>
<td align="right">33.6%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,543</td>
<td align="right">100.0%</td>
<td align="right">1,137</td>
<td align="right">100.0%</td>
<td align="right">-26.3%</td>
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
<td align="right">596,744</td>
<td align="right">0.4%</td>
<td align="right">442,858</td>
<td align="right">0.3%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,755,972</td>
<td align="right">6.0%</td>
<td align="right">9,919,665</td>
<td align="right">6.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,554,370</td>
<td align="right">93.7%</td>
<td align="right">153,543,453</td>
<td align="right">93.7%</td>
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
<td align="left">Failure</td>
<td align="right">14,291</td>
<td align="right">43.7%</td>
<td align="right">11,777</td>
<td align="right">43.2%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,381</td>
<td align="right">56.3%</td>
<td align="right">15,491</td>
<td align="right">56.8%</td>
<td align="right">-15.7%</td>
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
<td align="right">2,600</td>
<td align="right">18.2%</td>
<td align="right">1,904</td>
<td align="right">16.2%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,010</td>
<td align="right">56.0%</td>
<td align="right">6,209</td>
<td align="right">52.7%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,267</td>
<td align="right">8.9%</td>
<td align="right">1,253</td>
<td align="right">10.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">724</td>
<td align="right">5.1%</td>
<td align="right">720</td>
<td align="right">6.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">721</td>
<td align="right">5.0%</td>
<td align="right">722</td>
<td align="right">6.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
<td align="right">0.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,452,987</td>
<td align="right">100.0%</td>
<td align="right">83,562,446</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,308</td>
<td align="right">0.0%</td>
<td align="right">6,311</td>
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
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">313</td>
<td align="right">11.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,404</td>
<td align="right">88.7%</td>
<td align="right">2,392</td>
<td align="right">88.4%</td>
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
<td align="left">sequence</td>
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">270</td>
<td align="right">86.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">43</td>
<td align="right">13.7%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">266,064,068</td>
<td align="right">5.6%</td>
<td align="right">170,427,517</td>
<td align="right">4.6%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,746,289,462</td>
<td align="right">37.0%</td>
<td align="right">1,300,880,449</td>
<td align="right">35.4%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,627,934,266</td>
<td align="right">55.7%</td>
<td align="right">2,137,304,606</td>
<td align="right">58.1%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">81,796,964</td>
<td align="right">1.7%</td>
<td align="right">71,120,898</td>
<td align="right">1.9%</td>
<td align="right">-13.1%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">17,346,429</td>
<td align="right">6.0%</td>
<td align="right">4,549,034</td>
<td align="right">2.3%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,582,977</td>
<td align="right">0.9%</td>
<td align="right">884,388</td>
<td align="right">0.5%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,472,290</td>
<td align="right">28.1%</td>
<td align="right">33,479,929</td>
<td align="right">17.2%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">18,490,281</td>
<td align="right">6.4%</td>
<td align="right">8,259,762</td>
<td align="right">4.2%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">78,130,071</td>
<td align="right">26.9%</td>
<td align="right">60,207,410</td>
<td align="right">31.0%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,385,272</td>
<td align="right">10.5%</td>
<td align="right">25,900,949</td>
<td align="right">13.3%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,166,846</td>
<td align="right">9.4%</td>
<td align="right">26,515,813</td>
<td align="right">13.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,972</td>
<td align="right">3.4%</td>
<td align="right">9,919,665</td>
<td align="right">5.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,153,846</td>
<td align="right">8.3%</td>
<td align="right">24,268,865</td>
<td align="right">12.5%</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,014,753</td>
<td align="right">35.5%</td>
<td align="right">20,593,888</td>
<td align="right">29.0%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">633,306</td>
<td align="right">0.8%</td>
<td align="right">518,451</td>
<td align="right">0.7%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,349,768</td>
<td align="right">16.3%</td>
<td align="right">11,807,910</td>
<td align="right">16.6%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,604</td>
<td align="right">8.9%</td>
<td align="right">7,159,228</td>
<td align="right">10.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,147,408</td>
<td align="right">13.6%</td>
<td align="right">11,299,792</td>
<td align="right">15.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,202,658</td>
<td align="right">3.9%</td>
<td align="right">3,167,629</td>
<td align="right">4.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,148,321</td>
<td align="right">7.5%</td>
<td align="right">6,113,087</td>
<td align="right">8.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,572,473</td>
<td align="right">1.9%</td>
<td align="right">1,576,933</td>
<td align="right">2.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,539</td>
<td align="right">6.2%</td>
<td align="right">5,102,676</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,581</td>
<td align="right">2.6%</td>
<td align="right">2,103,580</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,223,604</td>
<td align="right">10.6%</td>
<td align="right">22,374,098</td>
<td align="right">10.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,396,258</td>
<td align="right">19.7%</td>
<td align="right">41,337,876</td>
<td align="right">19.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,904,187</td>
<td align="right">46.5%</td>
<td align="right">97,996,819</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,904,187</td>
<td align="right">46.5%</td>
<td align="right">97,996,819</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,679,798</td>
<td align="right">36.0%</td>
<td align="right">75,621,936</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,680,583</td>
<td align="right">36.0%</td>
<td align="right">75,622,721</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,876,073</td>
<td align="right">89.3%</td>
<td align="right">187,826,347</td>
<td align="right">89.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,274</td>
<td align="right">0.5%</td>
<td align="right">950,474</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,428,609</td>
<td align="right">53.5%</td>
<td align="right">112,436,817</td>
<td align="right">53.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,422</td>
<td align="right">8.8%</td>
<td align="right">18,490,830</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,039</td>
<td align="right">4.4%</td>
<td align="right">9,332,070</td>
<td align="right">4.4%</td>
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
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="left">Mortal increfs</td>
<td align="right">1,120,826,976</td>
<td align="right">23.9%</td>
<td align="right">1,660,108,475</td>
<td align="right">34.1%</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,244,855,712</td>
<td align="right">22.7%</td>
<td align="right">1,757,020,837</td>
<td align="right">30.6%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">578,592,809</td>
<td align="right">12.3%</td>
<td align="right">443,280,793</td>
<td align="right">9.1%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,079,471,746</td>
<td align="right">19.7%</td>
<td align="right">1,275,994,932</td>
<td align="right">22.2%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,993,993,668</td>
<td align="right">42.5%</td>
<td align="right">1,651,962,028</td>
<td align="right">33.9%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">843,319,222</td>
<td align="right">15.4%</td>
<td align="right">707,088,961</td>
<td align="right">12.3%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,324,421,013</td>
<td align="right">42.3%</td>
<td align="right">2,009,484,413</td>
<td align="right">35.0%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">995,873,408</td>
<td align="right">21.2%</td>
<td align="right">1,118,800,547</td>
<td align="right">23.0%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">157,877,530</td>
<td align="right"></td>
<td align="right">147,841,240</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,370,366</td>
<td align="right"></td>
<td align="right">2,256,704</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,561,917</td>
<td align="right"></td>
<td align="right">3,475,143</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,192,854</td>
<td align="right"></td>
<td align="right">1,219,861</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,803</td>
<td align="right">0.0%</td>
<td align="right">8,906</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">760,063</td>
<td align="right">0.1%</td>
<td align="right">763,983</td>
<td align="right">0.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">265,022,786</td>
<td align="right"></td>
<td align="right">264,841,186</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,217</td>
<td align="right"></td>
<td align="right">866,303</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">174,032,001</td>
<td align="right">33.8%</td>
<td align="right">174,019,834</td>
<td align="right">33.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">187,445,011</td>
<td align="right"></td>
<td align="right">187,436,243</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">174,800,867</td>
<td align="right">34.0%</td>
<td align="right">174,792,723</td>
<td align="right">34.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">339,840,374</td>
<td align="right"></td>
<td align="right">339,828,267</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">339,805,726</td>
<td align="right">66.0%</td>
<td align="right">339,793,623</td>
<td align="right">66.0%</td>
<td align="right">-0.0%</td>
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
Stats gathered on: 2025-02-06
