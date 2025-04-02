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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,248,271</td>
<td align="right">1,892,060</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,517,397</td>
<td align="right">2,165,383</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,164,359</td>
<td align="right">4,451,598</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,819,686</td>
<td align="right">2,461,512</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,631,340</td>
<td align="right">4,004,960</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,538,819</td>
<td align="right">7,821,985</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,687,095</td>
<td align="right">4,328,468</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,276,341</td>
<td align="right">13,917,415</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">20,080,393</td>
<td align="right">19,714,711</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">44,268,464</td>
<td align="right">43,561,691</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">30,117,006</td>
<td align="right">29,758,956</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,561,495</td>
<td align="right">31,217,870</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">57,592,401</td>
<td align="right">57,233,362</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">75,739</td>
<td align="right">76,126</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180,472,517</td>
<td align="right">179,779,208</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,018,862</td>
<td align="right">2,025,023</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,477,371</td>
<td align="right">2,483,531</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,644,638</td>
<td align="right">3,650,818</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,595,278</td>
<td align="right">2,599,373</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,648,358</td>
<td align="right">4,654,685</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,548</td>
<td align="right">108,695</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,149,841</td>
<td align="right">3,153,936</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">777</td>
<td align="right">778</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,792,976</td>
<td align="right">9,781,836</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,747,084</td>
<td align="right">3,751,178</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">110,793</td>
<td align="right">110,901</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,691,698</td>
<td align="right">18,708,441</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,517,662</td>
<td align="right">5,522,322</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,297,782</td>
<td align="right">9,304,475</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,546,657</td>
<td align="right">1,547,493</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">27,445,027</td>
<td align="right">27,458,788</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,744,806</td>
<td align="right">1,745,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,671,985</td>
<td align="right">18,679,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">15,107,903</td>
<td align="right">15,112,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,802,775</td>
<td align="right">1,803,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,978,184</td>
<td align="right">1,978,574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,791,200</td>
<td align="right">1,791,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">982,278</td>
<td align="right">982,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">31,869,234</td>
<td align="right">31,873,857</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">44,898,485</td>
<td align="right">44,903,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">27,197,415</td>
<td align="right">27,194,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,247,975</td>
<td align="right">4,247,547</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,792,566</td>
<td align="right">8,793,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,293,645</td>
<td align="right">2,293,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">49,952</td>
<td align="right">49,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,835,516</td>
<td align="right">2,835,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,055,551</td>
<td align="right">2,055,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,956,794</td>
<td align="right">6,957,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,005,814</td>
<td align="right">10,006,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,789,364</td>
<td align="right">3,789,225</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,026,373</td>
<td align="right">9,026,685</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,134,735</td>
<td align="right">8,135,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,669,940</td>
<td align="right">4,670,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">25,016,780</td>
<td align="right">25,017,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">920,809</td>
<td align="right">920,827</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,082,170</td>
<td align="right">1,082,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">48,436,810</td>
<td align="right">48,437,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,669,662</td>
<td align="right">36,670,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,143,757</td>
<td align="right">1,143,775</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,217,659</td>
<td align="right">15,217,845</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">15,053,362</td>
<td align="right">15,053,503</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,570,745</td>
<td align="right">46,571,084</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">576,321</td>
<td align="right">576,318</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,028,232</td>
<td align="right">1,028,228</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,973,986</td>
<td align="right">6,974,006</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,685,424</td>
<td align="right">1,685,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,208,196</td>
<td align="right">8,208,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">3,508,336</td>
<td align="right">3,508,333</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,044,579</td>
<td align="right">8,044,576</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,894,129</td>
<td align="right">3,894,128</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,554,410</td>
<td align="right">25,554,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">14,604,086</td>
<td align="right">14,604,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,308,191</td>
<td align="right">12,308,191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,705,869</td>
<td align="right">11,705,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,218,938</td>
<td align="right">11,218,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,761,953</td>
<td align="right">9,761,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,258,001</td>
<td align="right">8,258,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,393</td>
<td align="right">8,152,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,908,101</td>
<td align="right">6,908,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,498,261</td>
<td align="right">6,498,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,493,276</td>
<td align="right">6,493,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,627,234</td>
<td align="right">5,627,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">5,420,227</td>
<td align="right">5,420,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,333,854</td>
<td align="right">5,333,854</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,527,567</td>
<td align="right">4,527,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,302,363</td>
<td align="right">4,302,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,194,793</td>
<td align="right">4,194,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,860,446</td>
<td align="right">3,860,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,689,635</td>
<td align="right">3,689,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,039,928</td>
<td align="right">3,039,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,872,405</td>
<td align="right">2,872,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,846,283</td>
<td align="right">2,846,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,659,733</td>
<td align="right">2,659,733</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,570,980</td>
<td align="right">2,570,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,007,838</td>
<td align="right">2,007,838</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,941,617</td>
<td align="right">1,941,617</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,619,814</td>
<td align="right">1,619,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,499,315</td>
<td align="right">1,499,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,423,642</td>
<td align="right">1,423,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,389,094</td>
<td align="right">1,389,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,376,670</td>
<td align="right">1,376,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,173,131</td>
<td align="right">1,173,131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,148,836</td>
<td align="right">1,148,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,029,144</td>
<td align="right">1,029,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">970,072</td>
<td align="right">970,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">960,838</td>
<td align="right">960,838</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">849,919</td>
<td align="right">849,919</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">822,277</td>
<td align="right">822,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">821,162</td>
<td align="right">821,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">819,393</td>
<td align="right">819,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">704,913</td>
<td align="right">704,913</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">688,955</td>
<td align="right">688,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">668,847</td>
<td align="right">668,847</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">660,924</td>
<td align="right">660,924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">660,299</td>
<td align="right">660,299</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">614,479</td>
<td align="right">614,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">614,479</td>
<td align="right">614,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">553,448</td>
<td align="right">553,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">532,430</td>
<td align="right">532,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">514,661</td>
<td align="right">514,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">504,700</td>
<td align="right">504,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">445,800</td>
<td align="right">445,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">438,341</td>
<td align="right">438,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">352,790</td>
<td align="right">352,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">307,447</td>
<td align="right">307,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">294,882</td>
<td align="right">294,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">285,410</td>
<td align="right">285,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,755</td>
<td align="right">280,755</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,337</td>
<td align="right">280,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">259,109</td>
<td align="right">259,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">256,480</td>
<td align="right">256,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,540</td>
<td align="right">255,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">231,672</td>
<td align="right">231,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">195,188</td>
<td align="right">195,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,257</td>
<td align="right">165,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">165,127</td>
<td align="right">165,127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">164,900</td>
<td align="right">164,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">161,605</td>
<td align="right">161,605</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">133,856</td>
<td align="right">133,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,383</td>
<td align="right">122,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,113</td>
<td align="right">98,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84,791</td>
<td align="right">84,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84,256</td>
<td align="right">84,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">82,484</td>
<td align="right">82,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">68,785</td>
<td align="right">68,785</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">64,175</td>
<td align="right">64,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,548</td>
<td align="right">56,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,041</td>
<td align="right">55,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,588</td>
<td align="right">47,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">44,577</td>
<td align="right">44,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">42,891</td>
<td align="right">42,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,995</td>
<td align="right">26,995</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">25,194</td>
<td align="right">25,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">23,338</td>
<td align="right">23,338</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,679</td>
<td align="right">19,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,968</td>
<td align="right">18,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,267</td>
<td align="right">18,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">13,979</td>
<td align="right">13,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,054</td>
<td align="right">11,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,637</td>
<td align="right">5,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">5,607</td>
<td align="right">5,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,031</td>
<td align="right">3,031</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,949</td>
<td align="right">2,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,414</td>
<td align="right">2,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,305</td>
<td align="right">1,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,133</td>
<td align="right">1,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,107</td>
<td align="right">1,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,035</td>
<td align="right">1,035</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,025</td>
<td align="right">1,025</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">956</td>
<td align="right">956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">587</td>
<td align="right">587</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">223</td>
<td align="right">223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">214</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
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
<td align="right">62,822</td>
<td align="right">0.2%</td>
<td align="right">63,053</td>
<td align="right">0.2%</td>
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
<td align="right">22,899,878</td>
<td align="right">88.7%</td>
<td align="right">22,899,643</td>
<td align="right">88.7%</td>
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
<td align="right">2,836,593</td>
<td align="right">11.0%</td>
<td align="right">2,836,593</td>
<td align="right">11.0%</td>
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
<td align="right">3,130</td>
<td align="right">28.8%</td>
<td align="right">3,135</td>
<td align="right">28.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,733</td>
<td align="right">71.2%</td>
<td align="right">7,733</td>
<td align="right">71.2%</td>
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
<td align="left">out of range</td>
<td align="right">2,690</td>
<td align="right">34.8%</td>
<td align="right">2,690</td>
<td align="right">34.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">1,581</td>
<td align="right">20.4%</td>
<td align="right">1,581</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">998</td>
<td align="right">12.9%</td>
<td align="right">998</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">721</td>
<td align="right">9.3%</td>
<td align="right">721</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">616</td>
<td align="right">8.0%</td>
<td align="right">616</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">230</td>
<td align="right">3.0%</td>
<td align="right">230</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">211</td>
<td align="right">2.7%</td>
<td align="right">211</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">179</td>
<td align="right">2.3%</td>
<td align="right">179</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">152</td>
<td align="right">2.0%</td>
<td align="right">152</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">117</td>
<td align="right">1.5%</td>
<td align="right">117</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.9%</td>
<td align="right">66</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">51</td>
<td align="right">0.7%</td>
<td align="right">51</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">0.5%</td>
<td align="right">36</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.1%</td>
<td align="right">10</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">504,700</td>
<td align="right">100.0%</td>
<td align="right">504,700</td>
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
<td align="right">59,167,968</td>
<td align="right">88.4%</td>
<td align="right">59,166,830</td>
<td align="right">88.4%</td>
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
<td align="right">7,765,418</td>
<td align="right">11.6%</td>
<td align="right">7,765,283</td>
<td align="right">11.6%</td>
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
<td align="right">7,626,390</td>
<td align="right">11.4%</td>
<td align="right">7,626,258</td>
<td align="right">11.4%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">166,023</td>
<td align="right">100.0%</td>
<td align="right">166,020</td>
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
<td align="left">init not simple</td>
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">0.0%</td>
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
<td align="right">562,864</td>
<td align="right">97.8%</td>
<td align="right">562,864</td>
<td align="right">97.8%</td>
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
<td align="right">573,094</td>
<td align="right">99.6%</td>
<td align="right">573,094</td>
<td align="right">99.6%</td>
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
<td align="right">12,644</td>
<td align="right">100.0%</td>
<td align="right">12,644</td>
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
<td align="right">1,024,158</td>
<td align="right">5.6%</td>
<td align="right">1,024,155</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,181,783</td>
<td align="right">94.3%</td>
<td align="right">17,181,783</td>
<td align="right">94.3%</td>
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
<td align="right">3,375</td>
<td align="right">0.0%</td>
<td align="right">3,375</td>
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
<td align="right">2,606</td>
<td align="right">62.9%</td>
<td align="right">2,605</td>
<td align="right">62.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,535</td>
<td align="right">37.1%</td>
<td align="right">1,535</td>
<td align="right">37.1%</td>
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
<td align="right">244</td>
<td align="right">9.4%</td>
<td align="right">243</td>
<td align="right">9.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,108</td>
<td align="right">42.5%</td>
<td align="right">1,108</td>
<td align="right">42.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">717</td>
<td align="right">27.5%</td>
<td align="right">717</td>
<td align="right">27.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">174</td>
<td align="right">6.7%</td>
<td align="right">174</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">156</td>
<td align="right">6.0%</td>
<td align="right">156</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.8%</td>
<td align="right">48</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">17</td>
<td align="right">0.7%</td>
<td align="right">17</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,470,451</td>
<td align="right">37.4%</td>
<td align="right">2,476,610</td>
<td align="right">37.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,109,872</td>
<td align="right">62.1%</td>
<td align="right">4,109,872</td>
<td align="right">62.1%</td>
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
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,561</td>
<td align="right">0.4%</td>
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
<td align="right">6,207</td>
<td align="right">83.5%</td>
<td align="right">6,208</td>
<td align="right">83.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,224</td>
<td align="right">16.5%</td>
<td align="right">1,224</td>
<td align="right">16.5%</td>
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
<td align="right">3,246</td>
<td align="right">52.3%</td>
<td align="right">3,247</td>
<td align="right">52.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,241</td>
<td align="right">20.0%</td>
<td align="right">1,241</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,192</td>
<td align="right">19.2%</td>
<td align="right">1,192</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">528</td>
<td align="right">8.5%</td>
<td align="right">528</td>
<td align="right">8.5%</td>
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
<td align="right">4,677,042</td>
<td align="right">14.6%</td>
<td align="right">4,318,501</td>
<td align="right">13.7%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,025,890</td>
<td align="right">84.6%</td>
<td align="right">27,018,845</td>
<td align="right">85.6%</td>
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
<td align="right">225,559</td>
<td align="right">0.7%</td>
<td align="right">225,559</td>
<td align="right">0.7%</td>
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
<td align="right">8,774</td>
<td align="right">61.3%</td>
<td align="right">8,688</td>
<td align="right">61.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,531</td>
<td align="right">38.7%</td>
<td align="right">5,531</td>
<td align="right">38.9%</td>
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
<td align="right">161</td>
<td align="right">1.8%</td>
<td align="right">75</td>
<td align="right">0.9%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,264</td>
<td align="right">48.6%</td>
<td align="right">4,264</td>
<td align="right">49.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,410</td>
<td align="right">16.1%</td>
<td align="right">1,410</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,273</td>
<td align="right">14.5%</td>
<td align="right">1,273</td>
<td align="right">14.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">604</td>
<td align="right">6.9%</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">255</td>
<td align="right">2.9%</td>
<td align="right">255</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
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
<td align="right">14,141,775</td>
<td align="right">11.3%</td>
<td align="right">13,782,933</td>
<td align="right">11.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,041,393</td>
<td align="right">62.9%</td>
<td align="right">79,054,240</td>
<td align="right">63.1%</td>
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
<td align="right">32,324,993</td>
<td align="right">25.7%</td>
<td align="right">32,324,752</td>
<td align="right">25.8%</td>
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
<td align="right">199,734</td>
<td align="right">0.2%</td>
<td align="right">199,734</td>
<td align="right">0.2%</td>
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
<td align="right">72,825</td>
<td align="right">10.4%</td>
<td align="right">72,741</td>
<td align="right">10.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">627,970</td>
<td align="right">89.6%</td>
<td align="right">627,966</td>
<td align="right">89.6%</td>
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
<td align="left">class method obj</td>
<td align="right">456</td>
<td align="right">0.6%</td>
<td align="right">370</td>
<td align="right">0.5%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,307</td>
<td align="right">5.9%</td>
<td align="right">4,307</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,615</td>
<td align="right">5.0%</td>
<td align="right">3,615</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,533</td>
<td align="right">2.1%</td>
<td align="right">1,533</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,188</td>
<td align="right">1.6%</td>
<td align="right">1,188</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">968</td>
<td align="right">1.3%</td>
<td align="right">968</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">837</td>
<td align="right">1.1%</td>
<td align="right">837</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.3%</td>
<td align="right">235</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">224</td>
<td align="right">0.3%</td>
<td align="right">224</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">208</td>
<td align="right">0.3%</td>
<td align="right">208</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">155</td>
<td align="right">0.2%</td>
<td align="right">155</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">102</td>
<td align="right">0.1%</td>
<td align="right">102</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
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
<td align="right">57,553,547</td>
<td align="right">99.9%</td>
<td align="right">57,208,385</td>
<td align="right">99.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,284</td>
<td align="right">0.0%</td>
<td align="right">5,284</td>
<td align="right">0.0%</td>
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
<td align="right">508</td>
<td align="right">0.0%</td>
<td align="right">508</td>
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
<td align="right">9,359</td>
<td align="right">0.0%</td>
<td align="right">9,359</td>
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
<td align="right">18,184</td>
<td align="right">100.0%</td>
<td align="right">18,184</td>
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
<td align="right">137</td>
<td align="right">0.0%</td>
<td align="right">137</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">718,705</td>
<td align="right">99.9%</td>
<td align="right">718,705</td>
<td align="right">99.9%</td>
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
<td align="right">450</td>
<td align="right">100.0%</td>
<td align="right">450</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,490,313</td>
<td align="right">54.9%</td>
<td align="right">6,490,313</td>
<td align="right">54.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,333,854</td>
<td align="right">45.1%</td>
<td align="right">5,333,854</td>
<td align="right">45.1%</td>
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
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,860</td>
<td align="right">96.5%</td>
<td align="right">2,860</td>
<td align="right">96.5%</td>
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
<td align="right">2,057</td>
<td align="right">71.9%</td>
<td align="right">2,057</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,381,494</td>
<td align="right">9.9%</td>
<td align="right">1,381,494</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,761,931</td>
<td align="right">77.2%</td>
<td align="right">10,761,931</td>
<td align="right">77.2%</td>
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
<td align="right">1,792,372</td>
<td align="right">12.9%</td>
<td align="right">1,792,372</td>
<td align="right">12.9%</td>
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
<td align="right">38,129</td>
<td align="right">92.2%</td>
<td align="right">38,129</td>
<td align="right">92.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,228</td>
<td align="right">7.8%</td>
<td align="right">3,228</td>
<td align="right">7.8%</td>
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
<td align="right">57,755</td>
<td align="right">1,789.2%</td>
<td align="right">57,757</td>
<td align="right">1,789.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,397</td>
<td align="right">43.3%</td>
<td align="right">1,397</td>
<td align="right">43.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">606</td>
<td align="right">18.8%</td>
<td align="right">606</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">283</td>
<td align="right">8.8%</td>
<td align="right">283</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">106</td>
<td align="right">3.3%</td>
<td align="right">106</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">50</td>
<td align="right">1.5%</td>
<td align="right">50</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">18</td>
<td align="right">0.6%</td>
<td align="right">18</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">84,018</td>
<td align="right">3.1%</td>
<td align="right">84,018</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,586,100</td>
<td align="right">96.8%</td>
<td align="right">2,586,100</td>
<td align="right">96.8%</td>
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
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430</td>
<td align="right">55.6%</td>
<td align="right">430</td>
<td align="right">55.6%</td>
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
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">8</td>
<td align="right">1.9%</td>
<td align="right">8</td>
<td align="right">1.9%</td>
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
<td align="right">41,136,257</td>
<td align="right">91.7%</td>
<td align="right">41,142,644</td>
<td align="right">91.7%</td>
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
<td align="right">560,398</td>
<td align="right">1.2%</td>
<td align="right">560,395</td>
<td align="right">1.2%</td>
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
<td align="right">3,162,958</td>
<td align="right">7.0%</td>
<td align="right">3,162,967</td>
<td align="right">7.0%</td>
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
<td align="right">66,920</td>
<td align="right">88.9%</td>
<td align="right">66,920</td>
<td align="right">88.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,362</td>
<td align="right">11.1%</td>
<td align="right">8,362</td>
<td align="right">11.1%</td>
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
<td align="left">set</td>
<td align="right">5,827</td>
<td align="right">69.7%</td>
<td align="right">5,827</td>
<td align="right">69.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">764</td>
<td align="right">9.1%</td>
<td align="right">764</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">8.0%</td>
<td align="right">665</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">564</td>
<td align="right">6.7%</td>
<td align="right">564</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">3.9%</td>
<td align="right">325</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
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
<td align="right">7,938,602</td>
<td align="right">90.3%</td>
<td align="right">7,945,002</td>
<td align="right">90.3%</td>
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
<td align="right">848,869</td>
<td align="right">9.7%</td>
<td align="right">848,869</td>
<td align="right">9.7%</td>
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
<td align="right">804</td>
<td align="right">76.6%</td>
<td align="right">804</td>
<td align="right">76.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">246</td>
<td align="right">23.4%</td>
<td align="right">246</td>
<td align="right">23.4%</td>
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
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">24</td>
<td align="right">9.8%</td>
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
<td align="right">35,266,782</td>
<td align="right">3.1%</td>
<td align="right">34,555,382</td>
<td align="right">3.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">604,195,973</td>
<td align="right">53.0%</td>
<td align="right">601,078,864</td>
<td align="right">53.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">455,132,599</td>
<td align="right">39.9%</td>
<td align="right">453,389,073</td>
<td align="right">39.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">45,947,210</td>
<td align="right">4.0%</td>
<td align="right">45,947,094</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">4,677,042</td>
<td align="right">10.8%</td>
<td align="right">4,318,501</td>
<td align="right">10.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,141,775</td>
<td align="right">32.7%</td>
<td align="right">13,782,933</td>
<td align="right">32.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,470,451</td>
<td align="right">5.7%</td>
<td align="right">2,476,610</td>
<td align="right">5.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,626,390</td>
<td align="right">17.6%</td>
<td align="right">7,626,258</td>
<td align="right">17.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,024,158</td>
<td align="right">2.4%</td>
<td align="right">1,024,155</td>
<td align="right">2.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,490,313</td>
<td align="right">15.0%</td>
<td align="right">6,490,313</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,836,593</td>
<td align="right">6.6%</td>
<td align="right">2,836,593</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,381,494</td>
<td align="right">3.2%</td>
<td align="right">1,381,494</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">848,869</td>
<td align="right">2.0%</td>
<td align="right">848,869</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">562,864</td>
<td align="right">1.3%</td>
<td align="right">562,864</td>
<td align="right">1.3%</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,177,220</td>
<td align="right">2.6%</td>
<td align="right">1,179,340</td>
<td align="right">2.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,772,374</td>
<td align="right">12.6%</td>
<td align="right">5,770,119</td>
<td align="right">12.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,226,594</td>
<td align="right">7.0%</td>
<td align="right">3,226,418</td>
<td align="right">7.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,405,264</td>
<td align="right">11.8%</td>
<td align="right">5,405,219</td>
<td align="right">11.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">6,486,334</td>
<td align="right">14.1%</td>
<td align="right">6,486,281</td>
<td align="right">14.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,722,522</td>
<td align="right">5.9%</td>
<td align="right">2,722,521</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,116,107</td>
<td align="right">35.1%</td>
<td align="right">16,116,107</td>
<td align="right">35.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,792,289</td>
<td align="right">3.9%</td>
<td align="right">1,792,289</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,025,268</td>
<td align="right">2.2%</td>
<td align="right">1,025,268</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">534,913</td>
<td align="right">1.2%</td>
<td align="right">534,913</td>
<td align="right">1.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">372,423</td>
<td align="right">0.5%</td>
<td align="right">372,420</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,267,680</td>
<td align="right">9.1%</td>
<td align="right">6,267,677</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,268,786</td>
<td align="right">9.1%</td>
<td align="right">6,268,783</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,265,953</td>
<td align="right">12.0%</td>
<td align="right">8,265,950</td>
<td align="right">12.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,265,953</td>
<td align="right">12.0%</td>
<td align="right">8,265,950</td>
<td align="right">12.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,973,629</td>
<td align="right">69.5%</td>
<td align="right">47,973,623</td>
<td align="right">69.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">60,799,158</td>
<td align="right">88.0%</td>
<td align="right">60,799,155</td>
<td align="right">88.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,997,167</td>
<td align="right">2.9%</td>
<td align="right">1,997,167</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">452,136</td>
<td align="right">0.7%</td>
<td align="right">452,136</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,154,264</td>
<td align="right">1.7%</td>
<td align="right">1,154,264</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">56</td>
<td align="right">0.0%</td>
<td align="right">56</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">872,128</td>
<td align="right">1.3%</td>
<td align="right">872,128</td>
<td align="right">1.3%</td>
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
<td align="right">1,611,321</td>
<td align="right"></td>
<td align="right">1,684,173</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,886,201</td>
<td align="right"></td>
<td align="right">1,952,788</td>
<td align="right"></td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">39,474,019</td>
<td align="right">4.1%</td>
<td align="right">38,484,686</td>
<td align="right">4.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">276,817</td>
<td align="right"></td>
<td align="right">270,706</td>
<td align="right"></td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,837,221</td>
<td align="right">49.3%</td>
<td align="right">46,135,595</td>
<td align="right">48.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,862,840</td>
<td align="right"></td>
<td align="right">46,161,214</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">319,206,723</td>
<td align="right">32.9%</td>
<td align="right">323,918,484</td>
<td align="right">33.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">432,582,442</td>
<td align="right">44.6%</td>
<td align="right">427,652,925</td>
<td align="right">44.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">296,325,669</td>
<td align="right">29.4%</td>
<td align="right">298,545,591</td>
<td align="right">29.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">536,218,813</td>
<td align="right">53.2%</td>
<td align="right">533,079,590</td>
<td align="right">52.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">148,198,706</td>
<td align="right">14.7%</td>
<td align="right">148,643,659</td>
<td align="right">14.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">178,619,875</td>
<td align="right">18.4%</td>
<td align="right">178,257,554</td>
<td align="right">18.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">54,503,922</td>
<td align="right"></td>
<td align="right">54,430,694</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,757</td>
<td align="right">0.0%</td>
<td align="right">38,736</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">46,807,865</td>
<td align="right"></td>
<td align="right">46,820,864</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">313,159</td>
<td align="right">0.3%</td>
<td align="right">313,227</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">29,082,659</td>
<td align="right"></td>
<td align="right">29,088,764</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">47,829,515</td>
<td align="right">50.3%</td>
<td align="right">47,836,006</td>
<td align="right">50.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">48,181,431</td>
<td align="right">50.7%</td>
<td align="right">48,187,969</td>
<td align="right">51.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">27,134,781</td>
<td align="right">2.7%</td>
<td align="right">27,134,778</td>
<td align="right">2.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,107,983</td>
<td align="right"></td>
<td align="right">1,107,983</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">98,542</td>
<td align="right">8.9%</td>
<td align="right">98,542</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">4,942</td>
<td align="right">0.4%</td>
<td align="right">4,942</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">1,322</td>
<td align="right">26,495</td>
<td align="right">70,859,344</td>
<td align="right">10,757,906</td>
<td align="right">2,117,774</td>
<td align="right">1,322</td>
<td align="right">26,495</td>
<td align="right">70,851,225</td>
<td align="right">10,759,918</td>
<td align="right">2,115,970</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">120</td>
<td align="right">2.6%</td>
<td align="right">206</td>
<td align="right">4.4%</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">744</td>
<td align="right">16.0%</td>
<td align="right">616</td>
<td align="right">13.2%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">287,799,025</td>
<td align="right">2,334.7%</td>
<td align="right">301,712,889</td>
<td align="right">2,372.9%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,189</td>
<td align="right">25.5%</td>
<td align="right">1,236</td>
<td align="right">26.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">12,326,889</td>
<td align="right"></td>
<td align="right">12,714,914</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,604</td>
<td align="right">55.9%</td>
<td align="right">2,601</td>
<td align="right">55.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,657</td>
<td align="right"></td>
<td align="right">4,659</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">43</td>
<td align="right">0.9%</td>
<td align="right">43</td>
<td align="right">0.9%</td>
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
<td align="right">1,167</td>
<td align="right">98.1%</td>
<td align="right">1,214</td>
<td align="right">98.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,189</td>
<td align="right"></td>
<td align="right">1,236</td>
<td align="right"></td>
<td align="right">4.0%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">341,040</td>
<td align="right">2.1%</td>
<td align="right">546,112</td>
<td align="right">3.3%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,596,036</td>
<td align="right">16.2%</td>
<td align="right">2,266,006</td>
<td align="right">13.6%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">13,053,708</td>
<td align="right">81.6%</td>
<td align="right">13,829,930</td>
<td align="right">83.1%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">12,660,736</td>
<td align="right">79.2%</td>
<td align="right">13,250,560</td>
<td align="right">79.6%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">15,990,784</td>
<td align="right"></td>
<td align="right">16,642,048</td>
<td align="right"></td>
<td align="right">4.1%</td>
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
<td align="left">8</td>
<td align="right">0.7%</td>
<td align="left">8</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">522</td>
<td align="right">44.7%</td>
<td align="left">542</td>
<td align="right">44.6%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">446</td>
<td align="right">38.2%</td>
<td align="left">494</td>
<td align="right">40.7%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">189</td>
<td align="right">16.2%</td>
<td align="left">148</td>
<td align="right">12.2%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">2</td>
<td align="right">0.2%</td>
<td align="left">22</td>
<td align="right">1.8%</td>
<td align="right">1,000.0%</td>
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
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8</td>
<td align="right">0.7%</td>
<td align="right">8</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">497</td>
<td align="right">41.8%</td>
<td align="right">520</td>
<td align="right">42.1%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">364</td>
<td align="right">30.6%</td>
<td align="right">388</td>
<td align="right">31.4%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">191</td>
<td align="right">16.1%</td>
<td align="right">212</td>
<td align="right">17.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">128</td>
<td align="right">10.8%</td>
<td align="right">107</td>
<td align="right">8.7%</td>
<td align="right">-16.4%</td>
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
<td align="left"><= 8</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51</td>
<td align="right">4.3%</td>
<td align="right">72</td>
<td align="right">5.8%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">498</td>
<td align="right">41.9%</td>
<td align="right">500</td>
<td align="right">40.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">425</td>
<td align="right">35.7%</td>
<td align="right">470</td>
<td align="right">38.0%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">169</td>
<td align="right">14.2%</td>
<td align="right">148</td>
<td align="right">12.0%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22</td>
<td align="right">1.9%</td>
<td align="right">22</td>
<td align="right">1.8%</td>
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
<td align="left">_COPY_FREE_VARS</td>
<td align="right">303</td>
<td align="right">358,477</td>
<td align="right">118,209.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">117,568</td>
<td align="right">3,584,905</td>
<td align="right">2,949.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">76,833</td>
<td align="right">793,667</td>
<td align="right">933.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">55,268</td>
<td align="right">415,201</td>
<td align="right">651.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">58,424</td>
<td align="right">417,511</td>
<td align="right">614.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">76,166</td>
<td align="right">435,409</td>
<td align="right">471.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">76,166</td>
<td align="right">435,409</td>
<td align="right">471.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">76,166</td>
<td align="right">435,409</td>
<td align="right">471.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">76,166</td>
<td align="right">435,409</td>
<td align="right">471.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">458,904</td>
<td align="right">813,085</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">519</td>
<td align="right">132</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">519</td>
<td align="right">132</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">489,074</td>
<td align="right">842,845</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">315</td>
<td align="right">168</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,050,895</td>
<td align="right">1,405,923</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,123,182</td>
<td align="right">1,481,723</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,321,286</td>
<td align="right">1,680,130</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,867,375</td>
<td align="right">2,263,227</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,735,110</td>
<td align="right">2,087,429</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,791,553</td>
<td align="right">2,117,766</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,233,155</td>
<td align="right">2,590,705</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,228,463</td>
<td align="right">6,935,403</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,189,057</td>
<td align="right">3,547,471</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,812,753</td>
<td align="right">4,165,647</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,063,516</td>
<td align="right">4,422,018</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,779,431</td>
<td align="right">5,137,761</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,183,585</td>
<td align="right">13,908,916</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,720</td>
<td align="right">2,856</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,327,100</td>
<td align="right">7,680,618</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,928</td>
<td align="right">3,066</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,888</td>
<td align="right">3,024</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,750,696</td>
<td align="right">8,108,688</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">11,977,868</td>
<td align="right">12,365,585</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">12,326,889</td>
<td align="right">12,714,914</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">17,338</td>
<td align="right">17,766</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,928,607</td>
<td align="right">25,523,237</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">17,399,634</td>
<td align="right">17,786,170</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">24,027,348</td>
<td align="right">24,488,641</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">20,427</td>
<td align="right">20,040</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">218,190</td>
<td align="right">214,095</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">218,190</td>
<td align="right">214,095</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">244,083</td>
<td align="right">239,988</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">37,267,136</td>
<td align="right">37,890,968</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">260,238</td>
<td align="right">256,143</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">23,241</td>
<td align="right">22,896</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">679,284</td>
<td align="right">669,904</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">419,179</td>
<td align="right">414,519</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">565,550</td>
<td align="right">561,269</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">664,768</td>
<td align="right">660,674</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">38,385</td>
<td align="right">38,244</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,558,510</td>
<td align="right">2,550,320</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">135,435</td>
<td align="right">135,045</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,151,793</td>
<td align="right">6,169,330</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,151,793</td>
<td align="right">6,169,330</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,014,943</td>
<td align="right">1,017,654</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,408,377</td>
<td align="right">1,405,022</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,838,137</td>
<td align="right">1,834,782</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">192,249</td>
<td align="right">191,956</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,795,643</td>
<td align="right">5,787,039</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,678,970</td>
<td align="right">3,674,344</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">294,487</td>
<td align="right">294,126</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">608,913</td>
<td align="right">608,184</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,649,189</td>
<td align="right">3,644,864</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">587,067</td>
<td align="right">586,446</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">349,021</td>
<td align="right">349,329</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">169,113</td>
<td align="right">168,966</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">139,265</td>
<td align="right">139,171</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">901,098</td>
<td align="right">900,570</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">355,182</td>
<td align="right">355,364</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,338,653</td>
<td align="right">7,340,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,072,745</td>
<td align="right">5,071,256</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">63,151</td>
<td align="right">63,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,193,467</td>
<td align="right">1,193,152</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">926,013</td>
<td align="right">926,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,424,058</td>
<td align="right">2,423,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">72,170</td>
<td align="right">72,152</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">631,491</td>
<td align="right">631,344</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">5,566,620</td>
<td align="right">5,565,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,058,432</td>
<td align="right">1,058,285</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,689,083</td>
<td align="right">3,688,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,677,667</td>
<td align="right">1,677,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,182,320</td>
<td align="right">4,182,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,899,860</td>
<td align="right">2,899,713</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,123,980</td>
<td align="right">2,123,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">825,745</td>
<td align="right">825,727</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,858,937</td>
<td align="right">1,858,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">925,447</td>
<td align="right">925,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,391,765</td>
<td align="right">2,391,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,228,070</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,728,232</td>
<td align="right">1,728,232</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,336,896</td>
<td align="right">1,336,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,290</td>
<td align="right">1,207,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,184,463</td>
<td align="right">1,184,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">828,345</td>
<td align="right">828,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">713,522</td>
<td align="right">713,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">635,166</td>
<td align="right">635,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">572,124</td>
<td align="right">572,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">433,326</td>
<td align="right">433,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">374,208</td>
<td align="right">374,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">207,135</td>
<td align="right">207,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">139,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">131,791</td>
<td align="right">131,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,793</td>
<td align="right">128,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">63,042</td>
<td align="right">63,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">63,042</td>
<td align="right">63,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">33,075</td>
<td align="right">33,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">32,524</td>
<td align="right">32,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">31,164</td>
<td align="right">31,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">27,237</td>
<td align="right">27,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">21,000</td>
<td align="right">21,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">19,908</td>
<td align="right">19,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">16,262</td>
<td align="right">16,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">10,500</td>
<td align="right">10,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">10,332</td>
<td align="right">10,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">836</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">836</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">462</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">368</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">315</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">303</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">274</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">168</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">94</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">13</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">13</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">241</td>
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
<td align="left">CALL</td>
<td align="right">120</td>
<td align="right">121</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right"></td>
<td align="right">149</td>
<td align="right"></td>
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
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-04-02
