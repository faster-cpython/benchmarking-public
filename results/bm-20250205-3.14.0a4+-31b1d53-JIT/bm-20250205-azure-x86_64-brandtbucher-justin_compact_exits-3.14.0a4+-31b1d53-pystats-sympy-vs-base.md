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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">18,675,014</td>
<td align="right">35,415,468</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">886,101</td>
<td align="right">1,678,685</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,552,963</td>
<td align="right">6,834,242</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,286,685</td>
<td align="right">22,705,640</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,201,978</td>
<td align="right">3,234,538</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,265,770</td>
<td align="right">11,892,780</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">68,955,186</td>
<td align="right">44,201,959</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,788,414</td>
<td align="right">2,408,608</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">24,436,121</td>
<td align="right">30,983,862</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,530,916</td>
<td align="right">42,412,912</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">13,399,985</td>
<td align="right">16,790,653</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,676,000</td>
<td align="right">3,306,381</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,393,988</td>
<td align="right">1,721,434</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,069,747</td>
<td align="right">2,552,965</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">5,049,160</td>
<td align="right">6,221,235</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,554,489</td>
<td align="right">75,139,117</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,172,460</td>
<td align="right">6,310,171</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,429,627</td>
<td align="right">4,165,168</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,009,286</td>
<td align="right">6,039,025</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,825,182</td>
<td align="right">3,390,728</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,879,764</td>
<td align="right">48,812,653</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">43,946,187</td>
<td align="right">50,395,011</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,720,916</td>
<td align="right">6,548,481</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,282,431</td>
<td align="right">17,400,814</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,439,128</td>
<td align="right">3,904,746</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,431,328</td>
<td align="right">3,886,692</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,441,932</td>
<td align="right">20,820,720</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,296,818</td>
<td align="right">18,398,809</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,521,819</td>
<td align="right">1,713,748</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,248,458</td>
<td align="right">33,543,026</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">26,537,795</td>
<td align="right">29,380,004</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">171,105,766</td>
<td align="right">189,074,696</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">40,062,584</td>
<td align="right">43,981,614</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,493,581</td>
<td align="right">16,987,722</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,877,445</td>
<td align="right">13,015,459</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,319,075</td>
<td align="right">25,363,943</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,956,257</td>
<td align="right">11,811,210</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,228,234</td>
<td align="right">6,713,566</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">60,520,764</td>
<td align="right">65,189,911</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">597,610,267</td>
<td align="right">640,186,237</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">203,171,632</td>
<td align="right">217,077,371</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">50,323,011</td>
<td align="right">53,751,520</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,221,545</td>
<td align="right">43,967,043</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,842,162</td>
<td align="right">150,023,596</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">15,255,369</td>
<td align="right">16,237,296</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">20,337,853</td>
<td align="right">21,623,349</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,488,810</td>
<td align="right">18,540,724</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,934,937</td>
<td align="right">21,115,304</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,823,641</td>
<td align="right">34,756,534</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,918,184</td>
<td align="right">59,138,665</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,267,836</td>
<td align="right">63,701,074</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,428,487</td>
<td align="right">45,637,205</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,039,517</td>
<td align="right">16,843,334</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,766,684</td>
<td align="right">31,171,720</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,938,449</td>
<td align="right">27,158,857</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">172,428,725</td>
<td align="right">180,457,558</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,719,469</td>
<td align="right">18,533,547</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">43,367,006</td>
<td align="right">45,306,603</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">104,337,352</td>
<td align="right">108,926,038</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,721,110</td>
<td align="right">36,127,540</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,107,086</td>
<td align="right">12,594,176</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,591,340</td>
<td align="right">19,327,059</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,018,908</td>
<td align="right">88,273,901</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">115,462,889</td>
<td align="right">119,687,164</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,050,122</td>
<td align="right">16,452,103</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">159,504,635</td>
<td align="right">163,377,513</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">46,180,919</td>
<td align="right">47,215,855</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">26,538,690</td>
<td align="right">27,116,383</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,609,919</td>
<td align="right">4,695,480</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">42,394,144</td>
<td align="right">43,093,904</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,718,567</td>
<td align="right">17,962,520</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,643,463</td>
<td align="right">6,724,296</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,740,553</td>
<td align="right">21,985,541</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,098,227</td>
<td align="right">21,237,330</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,939,129</td>
<td align="right">9,896,111</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,651,428</td>
<td align="right">17,703,220</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">919</td>
<td align="right">917</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,445</td>
<td align="right">1,442</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,971</td>
<td align="right">2,965</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,970</td>
<td align="right">10,952</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,801,746</td>
<td align="right">12,821,146</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,842,403</td>
<td align="right">97,946,802</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,077</td>
<td align="right">18,059</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,197</td>
<td align="right">24,177</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,016</td>
<td align="right">9,022</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">30,305,866</td>
<td align="right">30,319,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,016,770</td>
<td align="right">182,089,648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,667</td>
<td align="right">165,603</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,397</td>
<td align="right">1,221,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,634</td>
<td align="right">493,472</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,308</td>
<td align="right">40,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,950</td>
<td align="right">389,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,454</td>
<td align="right">655,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,454</td>
<td align="right">655,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,454</td>
<td align="right">655,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,684</td>
<td align="right">20,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,872</td>
<td align="right">745,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,853</td>
<td align="right">1,966,469</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,108</td>
<td align="right">1,287,858</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,025,459</td>
<td align="right">6,024,302</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,367</td>
<td align="right">746,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,459</td>
<td align="right">654,362</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,475</td>
<td align="right">654,378</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,591</td>
<td align="right">456,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,029</td>
<td align="right">17,027</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,758,922</td>
<td align="right">1,758,726</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,795</td>
<td align="right">4,497,318</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,356</td>
<td align="right">2,281,159</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,588,390</td>
<td align="right">2,588,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,669</td>
<td align="right">78,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,117</td>
<td align="right">83,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,548</td>
<td align="right">4,469,226</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,590,123</td>
<td align="right">6,589,698</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,517,293</td>
<td align="right">7,516,927</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,253</td>
<td align="right">3,728,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,456</td>
<td align="right">5,753,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,852</td>
<td align="right">171,844</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,587,592</td>
<td align="right">4,587,392</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,398</td>
<td align="right">141,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,434</td>
<td align="right">2,418,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,567,887</td>
<td align="right">15,567,334</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,490</td>
<td align="right">1,028,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,086</td>
<td align="right">1,029,122</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,913,653</td>
<td align="right">15,913,106</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,015</td>
<td align="right">6,622,789</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,808</td>
<td align="right">1,389,767</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,546</td>
<td align="right">427,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,323</td>
<td align="right">175,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,550,185</td>
<td align="right">3,550,119</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,133</td>
<td align="right">2,195,107</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,641</td>
<td align="right">147,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,308</td>
<td align="right">21,977,441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,927</td>
<td align="right">745,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,727</td>
<td align="right">4,181,711</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,624</td>
<td align="right">597,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,650</td>
<td align="right">942,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,916,863</td>
<td align="right">10,916,843</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,392</td>
<td align="right">6,744,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,460</td>
<td align="right">1,754,458</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,177</td>
<td align="right">1,323,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,531</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">26,515,813</td>
<td align="right">63.6%</td>
<td align="right">27,093,388</td>
<td align="right">64.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,707</td>
<td align="right">0.1%</td>
<td align="right">49,902</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,082,654</td>
<td align="right">36.2%</td>
<td align="right">15,082,043</td>
<td align="right">35.7%</td>
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
<td align="right">21,564</td>
<td align="right">90.5%</td>
<td align="right">21,683</td>
<td align="right">90.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,258</td>
<td align="right">9.5%</td>
<td align="right">2,257</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">2,226</td>
<td align="right">10.3%</td>
<td align="right">2,333</td>
<td align="right">10.8%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">3.3%</td>
<td align="right">737</td>
<td align="right">3.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">206</td>
<td align="right">1.0%</td>
<td align="right">212</td>
<td align="right">1.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">566</td>
<td align="right">2.6%</td>
<td align="right">569</td>
<td align="right">2.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,912</td>
<td align="right">18.1%</td>
<td align="right">3,896</td>
<td align="right">18.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,213</td>
<td align="right">5.6%</td>
<td align="right">1,209</td>
<td align="right">5.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">703</td>
<td align="right">3.3%</td>
<td align="right">701</td>
<td align="right">3.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,893</td>
<td align="right">13.4%</td>
<td align="right">2,896</td>
<td align="right">13.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,085</td>
<td align="right">5.0%</td>
<td align="right">1,086</td>
<td align="right">5.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">14.9%</td>
<td align="right">3,221</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">10.3%</td>
<td align="right">2,225</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,007</td>
<td align="right">4.7%</td>
<td align="right">1,007</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">4.6%</td>
<td align="right">982</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.7%</td>
<td align="right">363</td>
<td align="right">1.7%</td>
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
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.4%</td>
<td align="right">91</td>
<td align="right">0.4%</td>
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
<td align="right">8,259,762</td>
<td align="right">20.1%</td>
<td align="right">11,885,922</td>
<td align="right">26.6%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,749,742</td>
<td align="right">79.8%</td>
<td align="right">32,743,204</td>
<td align="right">73.3%</td>
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
<td align="right">10,757</td>
<td align="right">0.0%</td>
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
<td align="right">5,226</td>
<td align="right">84.2%</td>
<td align="right">6,076</td>
<td align="right">86.1%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">15.8%</td>
<td align="right">982</td>
<td align="right">13.9%</td>
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
<td align="right">3,687</td>
<td align="right">70.6%</td>
<td align="right">4,543</td>
<td align="right">74.8%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">277</td>
<td align="right">5.3%</td>
<td align="right">274</td>
<td align="right">4.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">691</td>
<td align="right">13.2%</td>
<td align="right">688</td>
<td align="right">11.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">422</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">148</td>
<td align="right">2.4%</td>
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
<td align="right">24,726,792</td>
<td align="right">7.7%</td>
<td align="right">24,814,395</td>
<td align="right">7.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">24,268,865</td>
<td align="right">7.6%</td>
<td align="right">24,354,787</td>
<td align="right">7.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">295,928,096</td>
<td align="right">92.3%</td>
<td align="right">295,965,073</td>
<td align="right">92.3%</td>
<td align="right">0.0%</td>
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
<td align="right">482,124</td>
<td align="right">100.0%</td>
<td align="right">483,785</td>
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
<td align="right">3,183</td>
<td align="right">74.9%</td>
<td align="right">3,183</td>
<td align="right">74.9%</td>
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
<td align="right">1,064</td>
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
<td align="right">25,900,949</td>
<td align="right">33.5%</td>
<td align="right">27,121,078</td>
<td align="right">34.5%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,024,441</td>
<td align="right">65.9%</td>
<td align="right">51,029,961</td>
<td align="right">64.9%</td>
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
<td align="right">409,641</td>
<td align="right">0.5%</td>
<td align="right">409,600</td>
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
<td align="right">36,330</td>
<td align="right">80.4%</td>
<td align="right">36,621</td>
<td align="right">80.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,843</td>
<td align="right">19.6%</td>
<td align="right">8,831</td>
<td align="right">19.4%</td>
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
<td align="left">bool</td>
<td align="right">399</td>
<td align="right">1.1%</td>
<td align="right">656</td>
<td align="right">1.8%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">118</td>
<td align="right">0.3%</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">139</td>
<td align="right">0.4%</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,405</td>
<td align="right">17.6%</td>
<td align="right">6,446</td>
<td align="right">17.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,153</td>
<td align="right">8.7%</td>
<td align="right">3,142</td>
<td align="right">8.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,258</td>
<td align="right">11.7%</td>
<td align="right">4,267</td>
<td align="right">11.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,105</td>
<td align="right">38.8%</td>
<td align="right">14,106</td>
<td align="right">38.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
<td align="right">7,480</td>
<td align="right">20.4%</td>
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
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.2%</td>
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
<td align="right">4,549,034</td>
<td align="right">16.2%</td>
<td align="right">6,829,749</td>
<td align="right">22.5%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,794</td>
<td align="right">83.8%</td>
<td align="right">23,499,843</td>
<td align="right">77.5%</td>
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
<td align="right">3,807</td>
<td align="right">96.9%</td>
<td align="right">4,371</td>
<td align="right">97.3%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.1%</td>
<td align="right">122</td>
<td align="right">2.7%</td>
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
<td align="right">1,898</td>
<td align="right">49.9%</td>
<td align="right">2,464</td>
<td align="right">56.4%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,473</td>
<td align="right">38.7%</td>
<td align="right">1,471</td>
<td align="right">33.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">7.9%</td>
<td align="right">299</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.6%</td>
<td align="right">137</td>
<td align="right">3.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">737,158</td>
<td align="right">1.1%</td>
<td align="right">1,123,881</td>
<td align="right">1.3%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,022,284</td>
<td align="right">48.3%</td>
<td align="right">40,519,662</td>
<td align="right">48.2%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33,479,929</td>
<td align="right">50.5%</td>
<td align="right">42,356,970</td>
<td align="right">50.4%</td>
<td align="right">26.5%</td>
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
<td align="right">14,538</td>
<td align="right">22.4%</td>
<td align="right">21,826</td>
<td align="right">28.3%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">50,284</td>
<td align="right">77.6%</td>
<td align="right">55,234</td>
<td align="right">71.7%</td>
<td align="right">9.8%</td>
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
<td align="right">2,879</td>
<td align="right">5.7%</td>
<td align="right">3,364</td>
<td align="right">6.1%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">41,369</td>
<td align="right">82.3%</td>
<td align="right">45,616</td>
<td align="right">82.6%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,709</td>
<td align="right">5.4%</td>
<td align="right">2,926</td>
<td align="right">5.3%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,334</td>
<td align="right">2.7%</td>
<td align="right">1,335</td>
<td align="right">2.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">758</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">557</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">382</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">43,146,124</td>
<td align="right">13.3%</td>
<td align="right">52,693,812</td>
<td align="right">16.0%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">60,207,410</td>
<td align="right">18.5%</td>
<td align="right">63,639,816</td>
<td align="right">19.4%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">221,676,220</td>
<td align="right">68.2%</td>
<td align="right">212,438,712</td>
<td align="right">64.6%</td>
<td align="right">-4.2%</td>
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
<td align="right">824,845</td>
<td align="right">94.8%</td>
<td align="right">1,004,955</td>
<td align="right">95.6%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,202</td>
<td align="right">5.2%</td>
<td align="right">46,082</td>
<td align="right">4.4%</td>
<td align="right">1.9%</td>
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
<td align="right">245</td>
<td align="right">0.5%</td>
<td align="right">362</td>
<td align="right">0.8%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,013</td>
<td align="right">6.7%</td>
<td align="right">3,198</td>
<td align="right">6.9%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,361</td>
<td align="right">5.2%</td>
<td align="right">2,478</td>
<td align="right">5.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,182</td>
<td align="right">46.9%</td>
<td align="right">21,627</td>
<td align="right">46.9%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,043</td>
<td align="right">8.9%</td>
<td align="right">4,062</td>
<td align="right">8.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,165</td>
<td align="right">7.0%</td>
<td align="right">3,161</td>
<td align="right">6.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,099</td>
<td align="right">6.9%</td>
<td align="right">3,102</td>
<td align="right">6.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
<td align="right">6,812</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
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
<td align="right">245,791,862</td>
<td align="right">100.0%</td>
<td align="right">252,517,468</td>
<td align="right">100.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,543</td>
<td align="right">0.0%</td>
<td align="right">4,534</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">13,582</td>
<td align="right">100.0%</td>
<td align="right">13,573</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">2,265,827</td>
<td align="right">100.0%</td>
<td align="right">2,265,829</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">731,656</td>
<td align="right">72.0%</td>
<td align="right">731,541</td>
<td align="right">72.0%</td>
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
<td align="right">1,577,712</td>
<td align="right">17.4%</td>
<td align="right">1,578,541</td>
<td align="right">17.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,326,659</td>
<td align="right">80.7%</td>
<td align="right">7,325,407</td>
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
<td align="right">174,007</td>
<td align="right">1.9%</td>
<td align="right">174,018</td>
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
<td align="left">Failure</td>
<td align="right">980</td>
<td align="right">3.2%</td>
<td align="right">973</td>
<td align="right">3.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,007</td>
<td align="right">96.8%</td>
<td align="right">30,031</td>
<td align="right">96.9%</td>
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
<td align="left">not managed dict</td>
<td align="right">300</td>
<td align="right">30.6%</td>
<td align="right">296</td>
<td align="right">30.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">52.9%</td>
<td align="right">518</td>
<td align="right">53.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.4%</td>
<td align="right">102</td>
<td align="right">10.5%</td>
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
<td align="right">884,388</td>
<td align="right">4.7%</td>
<td align="right">1,676,759</td>
<td align="right">8.6%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,741,465</td>
<td align="right">95.2%</td>
<td align="right">17,740,916</td>
<td align="right">91.4%</td>
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
<td align="right">1,137</td>
<td align="right">66.4%</td>
<td align="right">1,350</td>
<td align="right">70.1%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">33.6%</td>
<td align="right">576</td>
<td align="right">29.9%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,137</td>
<td align="right">100.0%</td>
<td align="right">1,350</td>
<td align="right">100.0%</td>
<td align="right">18.7%</td>
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
<td align="right">442,858</td>
<td align="right">0.3%</td>
<td align="right">501,471</td>
<td align="right">0.3%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,919,665</td>
<td align="right">6.1%</td>
<td align="right">9,875,458</td>
<td align="right">6.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,543,453</td>
<td align="right">93.7%</td>
<td align="right">153,521,718</td>
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
<td align="right">11,777</td>
<td align="right">43.2%</td>
<td align="right">12,984</td>
<td align="right">43.9%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,491</td>
<td align="right">56.8%</td>
<td align="right">16,574</td>
<td align="right">56.1%</td>
<td align="right">7.0%</td>
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
<td align="right">1,904</td>
<td align="right">16.2%</td>
<td align="right">2,289</td>
<td align="right">17.6%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,209</td>
<td align="right">52.7%</td>
<td align="right">7,014</td>
<td align="right">54.0%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,253</td>
<td align="right">10.6%</td>
<td align="right">1,269</td>
<td align="right">9.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">720</td>
<td align="right">6.1%</td>
<td align="right">721</td>
<td align="right">5.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">883</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">722</td>
<td align="right">6.1%</td>
<td align="right">722</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">84</td>
<td align="right">0.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,311</td>
<td align="right">0.0%</td>
<td align="right">6,332</td>
<td align="right">0.0%</td>
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
<td align="right">83,562,446</td>
<td align="right">100.0%</td>
<td align="right">83,676,223</td>
<td align="right">100.0%</td>
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
<td align="left">Failure</td>
<td align="right">313</td>
<td align="right">11.6%</td>
<td align="right">298</td>
<td align="right">11.1%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.4%</td>
<td align="right">2,392</td>
<td align="right">88.9%</td>
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
<td align="left">sequence</td>
<td align="right">270</td>
<td align="right">86.3%</td>
<td align="right">255</td>
<td align="right">85.6%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">13.7%</td>
<td align="right">43</td>
<td align="right">14.4%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">71,120,898</td>
<td align="right">1.9%</td>
<td align="right">81,203,281</td>
<td align="right">2.1%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">170,427,517</td>
<td align="right">4.6%</td>
<td align="right">191,198,676</td>
<td align="right">4.9%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,300,880,449</td>
<td align="right">35.4%</td>
<td align="right">1,399,007,060</td>
<td align="right">35.8%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,137,304,606</td>
<td align="right">58.1%</td>
<td align="right">2,238,838,452</td>
<td align="right">57.3%</td>
<td align="right">4.8%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">884,388</td>
<td align="right">0.5%</td>
<td align="right">1,676,759</td>
<td align="right">0.8%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,549,034</td>
<td align="right">2.3%</td>
<td align="right">6,829,749</td>
<td align="right">3.2%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,259,762</td>
<td align="right">4.2%</td>
<td align="right">11,885,922</td>
<td align="right">5.5%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,479,929</td>
<td align="right">17.2%</td>
<td align="right">42,356,970</td>
<td align="right">19.7%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,207,410</td>
<td align="right">31.0%</td>
<td align="right">63,639,816</td>
<td align="right">29.6%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,900,949</td>
<td align="right">13.3%</td>
<td align="right">27,121,078</td>
<td align="right">12.6%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">26,515,813</td>
<td align="right">13.6%</td>
<td align="right">27,093,388</td>
<td align="right">12.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,919,665</td>
<td align="right">5.1%</td>
<td align="right">9,875,458</td>
<td align="right">4.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,268,865</td>
<td align="right">12.5%</td>
<td align="right">24,354,787</td>
<td align="right">11.3%</td>
<td align="right">0.4%</td>
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
<td align="right">20,593,888</td>
<td align="right">29.0%</td>
<td align="right">28,934,187</td>
<td align="right">35.6%</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">518,451</td>
<td align="right">0.7%</td>
<td align="right">643,353</td>
<td align="right">0.8%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,807,910</td>
<td align="right">16.6%</td>
<td align="right">12,878,413</td>
<td align="right">15.9%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,167,629</td>
<td align="right">4.5%</td>
<td align="right">3,222,614</td>
<td align="right">4.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,159,228</td>
<td align="right">10.1%</td>
<td align="right">7,241,470</td>
<td align="right">8.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,113,087</td>
<td align="right">8.6%</td>
<td align="right">6,147,569</td>
<td align="right">7.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,299,792</td>
<td align="right">15.9%</td>
<td align="right">11,353,256</td>
<td align="right">14.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,576,933</td>
<td align="right">2.2%</td>
<td align="right">1,577,762</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,676</td>
<td align="right">7.2%</td>
<td align="right">5,102,450</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,580</td>
<td align="right">3.0%</td>
<td align="right">2,103,585</td>
<td align="right">2.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,374,098</td>
<td align="right">10.6%</td>
<td align="right">22,426,202</td>
<td align="right">10.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,337,876</td>
<td align="right">19.6%</td>
<td align="right">41,390,463</td>
<td align="right">19.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,996,819</td>
<td align="right">46.6%</td>
<td align="right">98,101,218</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,996,819</td>
<td align="right">46.6%</td>
<td align="right">98,101,218</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,621,936</td>
<td align="right">35.9%</td>
<td align="right">75,674,231</td>
<td align="right">35.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,622,721</td>
<td align="right">35.9%</td>
<td align="right">75,675,016</td>
<td align="right">35.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,826,347</td>
<td align="right">89.3%</td>
<td align="right">187,892,985</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,474</td>
<td align="right">0.5%</td>
<td align="right">950,267</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,436,817</td>
<td align="right">53.4%</td>
<td align="right">112,451,143</td>
<td align="right">53.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,830</td>
<td align="right">8.8%</td>
<td align="right">18,490,427</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,070</td>
<td align="right">4.4%</td>
<td align="right">9,332,111</td>
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
<td align="left">Method cache misses</td>
<td align="right">2,256,704</td>
<td align="right"></td>
<td align="right">2,582,305</td>
<td align="right"></td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,660,108,475</td>
<td align="right">34.1%</td>
<td align="right">1,489,609,774</td>
<td align="right">31.1%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,475,143</td>
<td align="right"></td>
<td align="right">3,825,342</td>
<td align="right"></td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,757,020,837</td>
<td align="right">30.6%</td>
<td align="right">1,592,361,390</td>
<td align="right">28.2%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">147,841,240</td>
<td align="right"></td>
<td align="right">157,063,247</td>
<td align="right"></td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,651,962,028</td>
<td align="right">33.9%</td>
<td align="right">1,727,894,960</td>
<td align="right">36.1%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">443,280,793</td>
<td align="right">9.1%</td>
<td align="right">459,748,856</td>
<td align="right">9.6%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,009,484,413</td>
<td align="right">35.0%</td>
<td align="right">2,079,599,391</td>
<td align="right">36.9%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,906</td>
<td align="right">0.0%</td>
<td align="right">9,178</td>
<td align="right">0.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">707,088,961</td>
<td align="right">12.3%</td>
<td align="right">727,943,975</td>
<td align="right">12.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,275,994,932</td>
<td align="right">22.2%</td>
<td align="right">1,240,650,372</td>
<td align="right">22.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,219,861</td>
<td align="right"></td>
<td align="right">1,244,302</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">763,983</td>
<td align="right">0.1%</td>
<td align="right">772,160</td>
<td align="right">0.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,118,800,547</td>
<td align="right">23.0%</td>
<td align="right">1,113,660,289</td>
<td align="right">23.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">264,841,186</td>
<td align="right"></td>
<td align="right">265,046,433</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">174,019,834</td>
<td align="right">33.8%</td>
<td align="right">174,003,545</td>
<td align="right">33.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,303</td>
<td align="right"></td>
<td align="right">866,226</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">339,793,623</td>
<td align="right">66.0%</td>
<td align="right">339,822,514</td>
<td align="right">66.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">339,828,267</td>
<td align="right"></td>
<td align="right">339,857,157</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">174,792,723</td>
<td align="right">34.0%</td>
<td align="right">174,784,883</td>
<td align="right">34.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">187,436,243</td>
<td align="right"></td>
<td align="right">187,432,618</td>
<td align="right"></td>
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
<td align="right">220</td>
<td align="right">1.3%</td>
<td align="right">540</td>
<td align="right">3.8%</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">10,349</td>
<td align="right">59.5%</td>
<td align="right">4,007</td>
<td align="right">28.1%</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">137,141,409</td>
<td align="right"></td>
<td align="right">57,235,197</td>
<td align="right"></td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">232</td>
<td align="right">1.3%</td>
<td align="right">119</td>
<td align="right">0.8%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">10,475</td>
<td align="right">60.2%</td>
<td align="right">5,619</td>
<td align="right">39.4%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,041</td>
<td align="right">40.5%</td>
<td align="right">10,237</td>
<td align="right">71.9%</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,901,804,253</td>
<td align="right">2,115.9%</td>
<td align="right">2,185,041,171</td>
<td align="right">3,817.7%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,390</td>
<td align="right"></td>
<td align="right">14,244</td>
<td align="right"></td>
<td align="right">-18.1%</td>
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
<td align="right">7,041</td>
<td align="right"></td>
<td align="right">10,237</td>
<td align="right"></td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6,953</td>
<td align="right">98.8%</td>
<td align="right">10,019</td>
<td align="right">97.9%</td>
<td align="right">44.1%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">57,081,856</td>
<td align="right">89.4%</td>
<td align="right">130,543,616</td>
<td align="right">99.6%</td>
<td align="right">128.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">7,196,816</td>
<td align="right">11.3%</td>
<td align="right">15,354,496</td>
<td align="right">11.7%</td>
<td align="right">113.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">41,817,991</td>
<td align="right">65.5%</td>
<td align="right">88,224,333</td>
<td align="right">67.3%</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">63,844,352</td>
<td align="right"></td>
<td align="right">131,051,520</td>
<td align="right"></td>
<td align="right">105.3%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">14,829,545</td>
<td align="right">23.2%</td>
<td align="right">27,472,691</td>
<td align="right">21.0%</td>
<td align="right">85.3%</td>
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
<td align="left">2,155</td>
<td align="right">31.0%</td>
<td align="left">1,811</td>
<td align="right">14.8%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">2,815</td>
<td align="right">40.5%</td>
<td align="left">6,265</td>
<td align="right">51.2%</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1,436</td>
<td align="right">20.7%</td>
<td align="left">3,077</td>
<td align="right">25.2%</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">526</td>
<td align="right">7.6%</td>
<td align="left">957</td>
<td align="right">7.8%</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">0.3%</td>
<td align="left">119</td>
<td align="right">1.0%</td>
<td align="right">466.7%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">3</td>
<td align="right">0.0%</td>
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
<td align="left"><= 8</td>
<td align="right">1,018</td>
<td align="right">14.5%</td>
<td align="right">447</td>
<td align="right">4.4%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,152</td>
<td align="right">16.4%</td>
<td align="right">1,478</td>
<td align="right">14.4%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,653</td>
<td align="right">37.7%</td>
<td align="right">5,412</td>
<td align="right">52.9%</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,399</td>
<td align="right">19.9%</td>
<td align="right">1,929</td>
<td align="right">18.8%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">798</td>
<td align="right">11.3%</td>
<td align="right">950</td>
<td align="right">9.3%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 4</td>
<td align="right">259</td>
<td align="right">3.7%</td>
<td align="right">102</td>
<td align="right">1.0%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">865</td>
<td align="right">12.3%</td>
<td align="right">501</td>
<td align="right">4.9%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,116</td>
<td align="right">15.9%</td>
<td align="right">1,322</td>
<td align="right">12.9%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,346</td>
<td align="right">47.5%</td>
<td align="right">6,220</td>
<td align="right">60.8%</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,179</td>
<td align="right">16.7%</td>
<td align="right">1,549</td>
<td align="right">15.1%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">167</td>
<td align="right">2.4%</td>
<td align="right">304</td>
<td align="right">3.0%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">607</td>
<td align="right">1,575</td>
<td align="right">159.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">97,410</td>
<td align="right">415</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">13,833,994</td>
<td align="right">404,737</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,382,787</td>
<td align="right">98,597</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">902,903</td>
<td align="right">99,157</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">651,738</td>
<td align="right">73,600</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,285,620</td>
<td align="right">147,200</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">559,105</td>
<td align="right">73,600</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">563,070</td>
<td align="right">97,275</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">159,560</td>
<td align="right">36,456</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,163,771</td>
<td align="right">975,486</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">628</td>
<td align="right">196</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">51,779,165</td>
<td align="right">16,489,871</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,190,266</td>
<td align="right">1,894,609</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">389,868</td>
<td align="right">144,794</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">123,027,377</td>
<td align="right">46,894,345</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,549,541</td>
<td align="right">10,383,815</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,357,901</td>
<td align="right">543,984</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">137,141,409</td>
<td align="right">57,235,197</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,010,709</td>
<td align="right">5,567,309</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,827,713</td>
<td align="right">795,205</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,451,926</td>
<td align="right">1,097,253</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,279,485</td>
<td align="right">1,120,001</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,753,453</td>
<td align="right">898,106</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,164,004</td>
<td align="right">1,110,972</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">1,698,859</td>
<td align="right">906,388</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">320,425</td>
<td align="right">173,568</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">48,796,472</td>
<td align="right">26,808,122</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">188,194</td>
<td align="right">106,742</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,420,528</td>
<td align="right">6,756,366</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,968,842</td>
<td align="right">8,517,421</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,362,154</td>
<td align="right">5,134,842</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">6,299,342</td>
<td align="right">3,914,395</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">28,041,206</td>
<td align="right">17,958,437</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">10,114,933</td>
<td align="right">6,654,046</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">179,080,046</td>
<td align="right">120,002,015</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,269,613</td>
<td align="right">867,348</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,269,613</td>
<td align="right">867,348</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">13,082,750</td>
<td align="right">9,291,779</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,399,577</td>
<td align="right">997,312</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,399,577</td>
<td align="right">997,312</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,844,489</td>
<td align="right">5,725,380</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">27,435,348</td>
<td align="right">20,029,838</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">14,074,185</td>
<td align="right">10,339,277</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,433,046</td>
<td align="right">3,289,324</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,033,923</td>
<td align="right">15,121,020</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,033,923</td>
<td align="right">15,121,020</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,441,637</td>
<td align="right">13,209,556</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,470,835</td>
<td align="right">4,959,755</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">23,094,273</td>
<td align="right">17,775,767</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">18,571,726</td>
<td align="right">14,340,193</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">116,939,900</td>
<td align="right">90,725,108</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">8,748,715</td>
<td align="right">6,808,339</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">8,219,426</td>
<td align="right">6,403,799</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">33,890,181</td>
<td align="right">26,497,994</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">33,071,298</td>
<td align="right">25,867,669</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,803,842</td>
<td align="right">3,764,903</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">8,802,472</td>
<td align="right">7,030,360</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,959,738</td>
<td align="right">4,781,743</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">5,959,738</td>
<td align="right">4,781,743</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">5,925,508</td>
<td align="right">4,781,743</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">17,924,097</td>
<td align="right">14,491,153</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">18,530,314</td>
<td align="right">14,998,043</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">8,912,130</td>
<td align="right">7,216,324</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">27,197,136</td>
<td align="right">22,061,245</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">48,293,393</td>
<td align="right">39,224,164</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">12,339,281</td>
<td align="right">10,198,709</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">12,745,371</td>
<td align="right">10,541,560</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">42,801,986</td>
<td align="right">35,416,394</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">17,968,438</td>
<td align="right">14,900,572</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,253,176</td>
<td align="right">33,434,308</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">370,456,815</td>
<td align="right">307,755,613</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">130,697,815</td>
<td align="right">108,596,475</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,701,207</td>
<td align="right">6,412,177</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,213,945</td>
<td align="right">9,347,425</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,104,246</td>
<td align="right">10,119,244</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">11,999,678</td>
<td align="right">10,071,355</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">8,537,740</td>
<td align="right">7,173,439</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">8,537,740</td>
<td align="right">7,173,439</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,537,112</td>
<td align="right">7,173,243</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,655,895</td>
<td align="right">3,914,395</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">316,405,847</td>
<td align="right">266,727,826</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,785,420</td>
<td align="right">4,043,353</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,152,002</td>
<td align="right">16,220,727</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,178,834</td>
<td align="right">33,345,476</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">28,163,711</td>
<td align="right">24,148,710</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">49,303,157</td>
<td align="right">42,315,320</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">64,621,632</td>
<td align="right">55,626,469</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">37,761,837</td>
<td align="right">32,567,150</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">43,626,558</td>
<td align="right">37,637,521</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">10,322,989</td>
<td align="right">8,923,441</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">58,007,289</td>
<td align="right">50,664,628</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">26,370,861</td>
<td align="right">23,116,853</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,039,432</td>
<td align="right">8,884,958</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,601,794</td>
<td align="right">11,221,747</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,449,216</td>
<td align="right">37,848,546</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,788,987</td>
<td align="right">6,176,088</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,747,522</td>
<td align="right">6,169,236</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">12,806,776</td>
<td align="right">11,847,049</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,887</td>
<td align="right">6,038,218</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,887</td>
<td align="right">6,038,218</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">11,817,420</td>
<td align="right">10,938,533</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,504,910</td>
<td align="right">6,049,161</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">6,909,379</td>
<td align="right">6,425,860</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">6,909,379</td>
<td align="right">6,425,860</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,559,570</td>
<td align="right">6,103,821</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,036,937</td>
<td align="right">7,494,848</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,701,229</td>
<td align="right">16,873,707</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,795,389</td>
<td align="right">15,075,332</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,191,778</td>
<td align="right">12,626,275</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,191,778</td>
<td align="right">12,626,275</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">41,938,637</td>
<td align="right">40,230,496</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,632,289</td>
<td align="right">5,493,026</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">28,820</td>
<td align="right">28,388</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">2,841,403</td>
<td align="right">2,826,784</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,512,339</td>
<td align="right">5,493,026</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,790</td>
<td align="right">2,513,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,677,677</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,363</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">245,074</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">174,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">144,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">73,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">52,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">39,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">24,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">24,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,228</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">5,166</td>
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
<td align="right">1,792</td>
<td align="right">1,902</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">768</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
