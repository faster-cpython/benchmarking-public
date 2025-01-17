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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">247,163</td>
<td align="right">6,625,113</td>
<td align="right">2,580.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">376,603</td>
<td align="right">614,405</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,840,009</td>
<td align="right">6,217,897</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,085,903</td>
<td align="right">1,957,744</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">774,237</td>
<td align="right">1,249,833</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,421,305</td>
<td align="right">2,293,220</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">910,554</td>
<td align="right">1,465,385</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,175,305</td>
<td align="right">1,888,700</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">261,798</td>
<td align="right">420,378</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,449,554</td>
<td align="right">2,321,469</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,332,737</td>
<td align="right">2,125,477</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,201,399</td>
<td align="right">1,914,794</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,350,055</td>
<td align="right">2,142,753</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">270,112</td>
<td align="right">428,692</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,487,375</td>
<td align="right">2,359,290</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">431,198</td>
<td align="right">672,218</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">567,866</td>
<td align="right">884,946</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">426,802</td>
<td align="right">664,656</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">284,944</td>
<td align="right">443,456</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">285,267</td>
<td align="right">443,779</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">145,129</td>
<td align="right">225,229</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">431,127</td>
<td align="right">668,994</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">152,572</td>
<td align="right">231,854</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">458,952</td>
<td align="right">696,732</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,841,910</td>
<td align="right">10,251,213</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,365,463</td>
<td align="right">9,536,301</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">161,161</td>
<td align="right">240,451</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">163,917</td>
<td align="right">243,284</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,820,888</td>
<td align="right">2,693,032</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">167,083</td>
<td align="right">246,368</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,868,721</td>
<td align="right">14,546,725</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,942,778</td>
<td align="right">19,046,429</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,919,288</td>
<td align="right">2,791,318</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,101,722</td>
<td align="right">17,413,604</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,175,472</td>
<td align="right">8,870,896</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,310,560</td>
<td align="right">1,865,391</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,823,109</td>
<td align="right">4,012,033</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,603,816</td>
<td align="right">5,110,805</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,832,184</td>
<td align="right">5,418,345</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,322,888</td>
<td align="right">4,670,796</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,371,664</td>
<td align="right">1,926,724</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,930,814</td>
<td align="right">5,516,234</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,222,074</td>
<td align="right">15,661,217</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,637,914</td>
<td align="right">3,668,516</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,244,003</td>
<td align="right">1,719,686</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,323,441</td>
<td align="right">3,196,055</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">73,054,138</td>
<td align="right">100,330,003</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,987,053</td>
<td align="right">4,096,498</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,420,593</td>
<td align="right">29,031,228</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,700,398</td>
<td align="right">3,651,979</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,328,469</td>
<td align="right">9,866,362</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">714,719</td>
<td align="right">952,563</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,406,175</td>
<td align="right">7,150,217</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,673,042</td>
<td align="right">18,034,296</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,417,328</td>
<td align="right">28,998,445</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">811,477</td>
<td align="right">1,049,274</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,950,599</td>
<td align="right">10,250,562</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">26,436,775</td>
<td align="right">34,047,392</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,119,959</td>
<td align="right">1,438,088</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">855,240</td>
<td align="right">1,093,037</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">288,762</td>
<td align="right">368,035</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,771,942</td>
<td align="right">6,043,239</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,229,116</td>
<td align="right">1,546,199</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,044,698</td>
<td align="right">21,328,213</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,038,692</td>
<td align="right">21,243,509</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,410,190</td>
<td align="right">9,074,905</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,060,677</td>
<td align="right">8,646,070</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,443,334</td>
<td align="right">1,760,418</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,051,720</td>
<td align="right">3,685,878</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,228,362</td>
<td align="right">3,862,475</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,516,926</td>
<td align="right">8,864,427</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,145,580</td>
<td align="right">1,304,144</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,433,277</td>
<td align="right">6,146,633</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">651,570</td>
<td align="right">730,962</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">13,405,098</td>
<td align="right">14,515,475</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,040,213</td>
<td align="right">1,119,504</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,030</td>
<td align="right">5,357</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,237,687</td>
<td align="right">3,396,251</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">471</td>
<td align="right">489</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,427</td>
<td align="right">13,755</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,650</td>
<td align="right">17,978</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,650</td>
<td align="right">17,978</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,603</td>
<td align="right">1,631</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,555</td>
<td align="right">4,587</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,218</td>
<td align="right">3,238</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">348</td>
<td align="right">350</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,641</td>
<td align="right">102,952</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,493</td>
<td align="right">605,127</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">448,608</td>
<td align="right">448,928</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,437</td>
<td align="right">97,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,048</td>
<td align="right">34,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,020</td>
<td align="right">191,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,137</td>
<td align="right">35,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,870</td>
<td align="right">928,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,658</td>
<td align="right">81,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,690</td>
<td align="right">857,682</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,665</td>
<td align="right">940,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,712</td>
<td align="right">1,818,707</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,724,481</td>
<td align="right">4,724,481</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,264</td>
<td align="right">856,264</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,686</td>
<td align="right">462,686</td>
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
<td align="right">87,314</td>
<td align="right">87,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">84,725</td>
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
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">44,014</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">29,563</td>
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
<td align="right">13,887</td>
<td align="right">13,887</td>
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
<td align="left">BINARY_SUBSCR_GETITEM</td>
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
<td align="right">1,654,018</td>
<td align="right">24.0%</td>
<td align="right">8,243,904</td>
<td align="right">78.7%</td>
<td align="right">398.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,930</td>
<td align="right">2.4%</td>
<td align="right">271,207</td>
<td align="right">2.6%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,083,278</td>
<td align="right">73.6%</td>
<td align="right">1,956,306</td>
<td align="right">18.7%</td>
<td align="right">-61.5%</td>
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
<td align="right">3,232</td>
<td align="right">56.3%</td>
<td align="right">5,251</td>
<td align="right">80.1%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,507</td>
<td align="right">43.7%</td>
<td align="right">1,302</td>
<td align="right">19.9%</td>
<td align="right">-48.1%</td>
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
<td align="right">688</td>
<td align="right">27.4%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,215</td>
<td align="right">48.5%</td>
<td align="right">712</td>
<td align="right">54.7%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">294</td>
<td align="right">11.7%</td>
<td align="right">293</td>
<td align="right">22.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">7.5%</td>
<td align="right">187</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">4.3%</td>
<td align="right">109</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">14</td>
<td align="right">0.6%</td>
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
<td align="right">13,887</td>
<td align="right">100.0%</td>
<td align="right">13,887</td>
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
<td align="right">468,492</td>
<td align="right">51.1%</td>
<td align="right">627,072</td>
<td align="right">58.3%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">448,233</td>
<td align="right">48.9%</td>
<td align="right">448,560</td>
<td align="right">41.7%</td>
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
<td align="right">257</td>
<td align="right">68.5%</td>
<td align="right">250</td>
<td align="right">67.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">31.5%</td>
<td align="right">118</td>
<td align="right">32.1%</td>
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
<td align="right">256</td>
<td align="right">99.6%</td>
<td align="right">249</td>
<td align="right">99.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">18,352,957</td>
<td align="right">100.0%</td>
<td align="right">25,648,759</td>
<td align="right">100.0%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,183</td>
<td align="right">0.0%</td>
<td align="right">1,226</td>
<td align="right">0.0%</td>
<td align="right">3.6%</td>
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
<td align="right">3,373</td>
<td align="right">100.0%</td>
<td align="right">3,362</td>
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
<td align="right">127,145</td>
<td align="right">3.0%</td>
<td align="right">206,348</td>
<td align="right">3.8%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">428,108</td>
<td align="right">10.3%</td>
<td align="right">667,563</td>
<td align="right">12.3%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,613,495</td>
<td align="right">86.6%</td>
<td align="right">4,565,164</td>
<td align="right">83.9%</td>
<td align="right">26.3%</td>
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
<td align="right">2,657</td>
<td align="right">48.6%</td>
<td align="right">4,155</td>
<td align="right">48.7%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,815</td>
<td align="right">51.4%</td>
<td align="right">4,376</td>
<td align="right">51.3%</td>
<td align="right">55.5%</td>
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
<td align="right">2,521</td>
<td align="right">89.6%</td>
<td align="right">4,083</td>
<td align="right">93.3%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">153</td>
<td align="right">5.4%</td>
<td align="right">152</td>
<td align="right">3.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">3.4%</td>
<td align="right">96</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">1.6%</td>
<td align="right">44</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">1,310,975</td>
<td align="right">100.0%</td>
<td align="right">1,865,806</td>
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
<td align="right">12,512,917</td>
<td align="right">93.0%</td>
<td align="right">14,415,499</td>
<td align="right">93.9%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">940,122</td>
<td align="right">7.0%</td>
<td align="right">940,122</td>
<td align="right">6.1%</td>
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
<td align="right">10.1%</td>
<td align="right">50</td>
<td align="right">9.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">89.9%</td>
<td align="right">488</td>
<td align="right">90.7%</td>
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
<td align="right">6,830,900</td>
<td align="right">17.2%</td>
<td align="right">10,239,361</td>
<td align="right">19.0%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,526,101</td>
<td align="right">81.8%</td>
<td align="right">43,391,569</td>
<td align="right">80.3%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">388,557</td>
<td align="right">1.0%</td>
<td align="right">389,408</td>
<td align="right">0.7%</td>
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
<td align="left">Failure</td>
<td align="right">6,465</td>
<td align="right">35.8%</td>
<td align="right">7,328</td>
<td align="right">38.7%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,587</td>
<td align="right">64.2%</td>
<td align="right">11,597</td>
<td align="right">61.3%</td>
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
<td align="right">1,471</td>
<td align="right">22.8%</td>
<td align="right">1,924</td>
<td align="right">26.3%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">768</td>
<td align="right">11.9%</td>
<td align="right">884</td>
<td align="right">12.1%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,492</td>
<td align="right">23.1%</td>
<td align="right">1,563</td>
<td align="right">21.3%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">10.5%</td>
<td align="right">682</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.1%</td>
<td align="right">460</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.1%</td>
<td align="right">68</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">19,117,941</td>
<td align="right">100.0%</td>
<td align="right">27,917,016</td>
<td align="right">100.0%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">830</td>
<td align="right">0.0%</td>
<td align="right">852</td>
<td align="right">0.0%</td>
<td align="right">2.7%</td>
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
<td align="right">309</td>
<td align="right">0.0%</td>
<td align="right">309</td>
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
<td align="right">2,397</td>
<td align="right">100.0%</td>
<td align="right">2,395</td>
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
<td align="right">1,445,105</td>
<td align="right">100.0%</td>
<td align="right">2,317,020</td>
<td align="right">100.0%</td>
<td align="right">60.3%</td>
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
<td align="right">3,800,284</td>
<td align="right">94.5%</td>
<td align="right">5,385,704</td>
<td align="right">96.0%</td>
<td align="right">41.7%</td>
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
<td align="right">2.0%</td>
<td align="right">79,937</td>
<td align="right">1.4%</td>
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
<td align="right">3.5%</td>
<td align="right">140,400</td>
<td align="right">2.5%</td>
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
<td align="right">3,614</td>
<td align="right">82.9%</td>
<td align="right">3,615</td>
<td align="right">83.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.1%</td>
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
<td align="right">734</td>
<td align="right">98.8%</td>
<td align="right">883</td>
<td align="right">118.8%</td>
<td align="right">20.3%</td>
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
<td align="right">1,371,664</td>
<td align="right">98.5%</td>
<td align="right">1,926,724</td>
<td align="right">98.9%</td>
<td align="right">40.5%</td>
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
<td align="right">1.5%</td>
<td align="right">21,264</td>
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
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
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
<td align="right">8,430,992</td>
<td align="right">92.8%</td>
<td align="right">12,791,471</td>
<td align="right">94.6%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">650,221</td>
<td align="right">7.2%</td>
<td align="right">729,605</td>
<td align="right">5.4%</td>
<td align="right">12.2%</td>
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
<td align="right">888</td>
<td align="right">65.8%</td>
<td align="right">901</td>
<td align="right">66.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">461</td>
<td align="right">34.2%</td>
<td align="right">456</td>
<td align="right">33.6%</td>
<td align="right">-1.1%</td>
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
<td align="right">327</td>
<td align="right">36.8%</td>
<td align="right">351</td>
<td align="right">39.0%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">152</td>
<td align="right">17.1%</td>
<td align="right">141</td>
<td align="right">15.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.1%</td>
<td align="right">232</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.5%</td>
<td align="right">111</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">7.3%</td>
<td align="right">65</td>
<td align="right">7.2%</td>
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
<td align="right">2,003,270</td>
<td align="right">100.0%</td>
<td align="right">2,161,826</td>
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
<td align="right">158,259,612</td>
<td align="right">37.1%</td>
<td align="right">218,924,517</td>
<td align="right">38.8%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">252,510,335</td>
<td align="right">59.3%</td>
<td align="right">329,895,864</td>
<td align="right">58.4%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">822,165</td>
<td align="right">0.2%</td>
<td align="right">1,008,496</td>
<td align="right">0.2%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,525,362</td>
<td align="right">3.4%</td>
<td align="right">15,127,287</td>
<td align="right">2.7%</td>
<td align="right">4.1%</td>
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
<td align="right">5,083,278</td>
<td align="right">35.1%</td>
<td align="right">1,956,306</td>
<td align="right">13.0%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">428,108</td>
<td align="right">3.0%</td>
<td align="right">667,563</td>
<td align="right">4.4%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,830,900</td>
<td align="right">47.1%</td>
<td align="right">10,239,361</td>
<td align="right">67.8%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">650,221</td>
<td align="right">4.5%</td>
<td align="right">729,605</td>
<td align="right">4.8%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,183</td>
<td align="right">0.0%</td>
<td align="right">1,226</td>
<td align="right">0.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">448,233</td>
<td align="right">3.1%</td>
<td align="right">448,560</td>
<td align="right">3.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,122</td>
<td align="right">6.5%</td>
<td align="right">940,122</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.6%</td>
<td align="right">79,937</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right">13,887</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">82,429</td>
<td align="right">10.0%</td>
<td align="right">135,658</td>
<td align="right">13.5%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">82,501</td>
<td align="right">10.0%</td>
<td align="right">135,549</td>
<td align="right">13.4%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">127,144</td>
<td align="right">15.5%</td>
<td align="right">206,347</td>
<td align="right">20.5%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">318,905</td>
<td align="right">38.8%</td>
<td align="right">319,748</td>
<td align="right">31.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,592</td>
<td align="right">7.2%</td>
<td align="right">59,600</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">17.1%</td>
<td align="right">140,400</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.2%</td>
<td align="right">9,895</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.0%</td>
<td align="right">398</td>
<td align="right">0.0%</td>
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
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
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
<td align="right">392,486</td>
<td align="right">1.5%</td>
<td align="right">550,988</td>
<td align="right">1.6%</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">21,424,826</td>
<td align="right">81.0%</td>
<td align="right">29,035,461</td>
<td align="right">85.2%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,928,801</td>
<td align="right">71.6%</td>
<td align="right">25,191,935</td>
<td align="right">74.0%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,093,846</td>
<td align="right">26.8%</td>
<td align="right">8,441,347</td>
<td align="right">24.8%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,093,905</td>
<td align="right">26.8%</td>
<td align="right">8,441,406</td>
<td align="right">24.8%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,521,284</td>
<td align="right">28.4%</td>
<td align="right">8,868,785</td>
<td align="right">26.0%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,521,284</td>
<td align="right">28.4%</td>
<td align="right">8,868,785</td>
<td align="right">26.0%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,665</td>
<td align="right">0.1%</td>
<td align="right">17,993</td>
<td align="right">0.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.6%</td>
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
<td align="right">1.7%</td>
<td align="right">456,471</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.7%</td>
<td align="right">441,509</td>
<td align="right">1.3%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">12,012</td>
<td align="right"></td>
<td align="right">27,322</td>
<td align="right"></td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,844</td>
<td align="right"></td>
<td align="right">77,333</td>
<td align="right"></td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">25,074</td>
<td align="right"></td>
<td align="right">50,271</td>
<td align="right"></td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,183,732</td>
<td align="right"></td>
<td align="right">1,817,900</td>
<td align="right"></td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">8,326,480</td>
<td align="right"></td>
<td align="right">12,504,311</td>
<td align="right"></td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">64,598,114</td>
<td align="right">21.3%</td>
<td align="right">89,569,530</td>
<td align="right">21.9%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">43,147,777</td>
<td align="right">12.0%</td>
<td align="right">59,437,327</td>
<td align="right">12.3%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">34,928,153</td>
<td align="right">11.5%</td>
<td align="right">48,043,217</td>
<td align="right">11.8%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">83,595,270</td>
<td align="right">23.3%</td>
<td align="right">114,753,314</td>
<td align="right">23.8%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">48,781,291</td>
<td align="right">16.1%</td>
<td align="right">66,345,996</td>
<td align="right">16.2%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,048,564</td>
<td align="right"></td>
<td align="right">21,495,981</td>
<td align="right"></td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,047,116</td>
<td align="right">51.0%</td>
<td align="right">21,494,020</td>
<td align="right">52.7%</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">173,298,489</td>
<td align="right">48.4%</td>
<td align="right">230,808,085</td>
<td align="right">47.9%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">154,462,712</td>
<td align="right">51.0%</td>
<td align="right">204,335,101</td>
<td align="right">50.0%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,416,645</td>
<td align="right"></td>
<td align="right">12,413,443</td>
<td align="right"></td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">58,347,059</td>
<td align="right">16.3%</td>
<td align="right">76,572,706</td>
<td align="right">15.9%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,413,531</td>
<td align="right"></td>
<td align="right">20,849,672</td>
<td align="right"></td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,309,987</td>
<td align="right">48.6%</td>
<td align="right">19,191,741</td>
<td align="right">47.0%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,431,069</td>
<td align="right">49.0%</td>
<td align="right">19,312,825</td>
<td align="right">47.3%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,535</td>
<td align="right">0.1%</td>
<td align="right">43,536</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,547</td>
<td align="right">0.2%</td>
<td align="right">77,548</td>
<td align="right">0.2%</td>
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
<td align="right">11,144</td>
<td align="right">774</td>
<td align="right">794</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">11,144</td>
<td align="right">774</td>
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
Stats gathered on: 2025-01-17
