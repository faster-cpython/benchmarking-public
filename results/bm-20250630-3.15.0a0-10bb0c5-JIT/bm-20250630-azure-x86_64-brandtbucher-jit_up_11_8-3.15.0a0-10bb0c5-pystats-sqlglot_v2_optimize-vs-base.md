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
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">361,032</td>
<td align="right">128,961</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">602,070</td>
<td align="right">240,870</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">599,676</td>
<td align="right">366,807</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,260,985</td>
<td align="right">2,281,965</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">599,424</td>
<td align="right">424,641</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">376,950</td>
<td align="right">274,407</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">125,181</td>
<td align="right">96,474</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">282,009</td>
<td align="right">219,513</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,368,107</td>
<td align="right">1,868,013</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,296,351</td>
<td align="right">1,041,075</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,541,397</td>
<td align="right">3,759,756</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">790,965</td>
<td align="right">656,901</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">577,164</td>
<td align="right">488,775</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,393,958</td>
<td align="right">2,092,923</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,199,058</td>
<td align="right">1,049,454</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">5,725,230</td>
<td align="right">5,105,709</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,958,796</td>
<td align="right">1,765,134</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,569,198</td>
<td align="right">6,838,881</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">106,176</td>
<td align="right">96,117</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,509,582</td>
<td align="right">4,107,285</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,071,437</td>
<td align="right">4,639,971</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,624,894</td>
<td align="right">3,327,240</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">44,848,251</td>
<td align="right">41,172,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,452,190</td>
<td align="right">3,177,657</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,189,787</td>
<td align="right">10,337,439</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,022,361</td>
<td align="right">3,734,052</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,953,607</td>
<td align="right">3,679,074</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">14,295,645</td>
<td align="right">13,315,869</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,106,626</td>
<td align="right">11,285,358</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">935,067</td>
<td align="right">872,571</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,861,077</td>
<td align="right">7,371,126</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,752,765</td>
<td align="right">1,648,857</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">11,427,570</td>
<td align="right">10,753,428</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,796,578</td>
<td align="right">14,881,860</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,633,647</td>
<td align="right">7,241,451</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">21,872,592</td>
<td align="right">20,869,464</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,231,310</td>
<td align="right">5,010,033</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,100,904</td>
<td align="right">1,058,652</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,401,155</td>
<td align="right">8,089,368</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,607,842</td>
<td align="right">3,494,568</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">852,642</td>
<td align="right">826,119</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,071,426</td>
<td align="right">15,587,187</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,193,385</td>
<td align="right">4,070,241</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,593,479</td>
<td align="right">2,531,718</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">503,622</td>
<td align="right">492,513</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,382,272</td>
<td align="right">12,115,593</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,475,308</td>
<td align="right">6,340,992</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,145,922</td>
<td align="right">7,042,581</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,329,363</td>
<td align="right">1,312,857</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">71,064</td>
<td align="right">70,266</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,680,209</td>
<td align="right">2,655,450</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">177,975</td>
<td align="right">176,379</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,232,217</td>
<td align="right">1,222,158</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">217,161</td>
<td align="right">215,565</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">114,240</td>
<td align="right">113,442</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">250,509</td>
<td align="right">248,913</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">39,375</td>
<td align="right">39,144</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">966,525</td>
<td align="right">961,632</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,649,697</td>
<td align="right">1,642,641</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,367,981</td>
<td align="right">2,359,182</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">72,702</td>
<td align="right">72,471</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">299,313</td>
<td align="right">298,389</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">396,942</td>
<td align="right">396,144</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">402,150</td>
<td align="right">401,457</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">582,876</td>
<td align="right">582,078</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,091,118</td>
<td align="right">1,092,231</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,069,278</td>
<td align="right">1,068,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,574,769</td>
<td align="right">1,574,076</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,045,022</td>
<td align="right">2,044,224</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">644,994</td>
<td align="right">644,763</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">917,847</td>
<td align="right">917,616</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,949,029</td>
<td align="right">3,949,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,836,260</td>
<td align="right">2,836,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,254,476</td>
<td align="right">2,254,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,894,452</td>
<td align="right">1,894,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,547,637</td>
<td align="right">1,547,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,489,005</td>
<td align="right">1,489,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,439,928</td>
<td align="right">1,439,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,355,907</td>
<td align="right">1,355,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,266,111</td>
<td align="right">1,266,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,145,697</td>
<td align="right">1,145,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">752,157</td>
<td align="right">752,157</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">716,415</td>
<td align="right">716,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">683,088</td>
<td align="right">683,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">606,186</td>
<td align="right">606,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">478,674</td>
<td align="right">478,674</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">405,594</td>
<td align="right">405,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">405,594</td>
<td align="right">405,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">405,279</td>
<td align="right">405,279</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">378,945</td>
<td align="right">378,945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">319,158</td>
<td align="right">319,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">235,095</td>
<td align="right">235,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">172,137</td>
<td align="right">172,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">169,155</td>
<td align="right">169,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">154,938</td>
<td align="right">154,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">125,181</td>
<td align="right">125,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">125,055</td>
<td align="right">125,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,543</td>
<td align="right">123,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">114,723</td>
<td align="right">114,723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">101,661</td>
<td align="right">101,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">76,356</td>
<td align="right">76,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">70,287</td>
<td align="right">70,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">67,914</td>
<td align="right">67,914</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">67,452</td>
<td align="right">67,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">64,995</td>
<td align="right">64,995</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">55,335</td>
<td align="right">55,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">52,227</td>
<td align="right">52,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">49,938</td>
<td align="right">49,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">36,729</td>
<td align="right">36,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">36,288</td>
<td align="right">36,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,162</td>
<td align="right">36,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">33,915</td>
<td align="right">33,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">30,912</td>
<td align="right">30,912</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">30,114</td>
<td align="right">30,114</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">30,114</td>
<td align="right">30,114</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">30,114</td>
<td align="right">30,114</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">29,568</td>
<td align="right">29,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,959</td>
<td align="right">28,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,877</td>
<td align="right">23,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">22,365</td>
<td align="right">22,365</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">22,239</td>
<td align="right">22,239</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">14,952</td>
<td align="right">14,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">12,600</td>
<td align="right">12,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">12,222</td>
<td align="right">12,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">9,975</td>
<td align="right">9,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">9,849</td>
<td align="right">9,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">9,849</td>
<td align="right">9,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">7,686</td>
<td align="right">7,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,056</td>
<td align="right">7,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">6,720</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">5,019</td>
<td align="right">5,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,549</td>
<td align="right">3,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,276</td>
<td align="right">3,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">3,150</td>
<td align="right">3,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,310</td>
<td align="right">2,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,134</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">819</td>
<td align="right">819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">798</td>
<td align="right">798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">756</td>
<td align="right">756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">294</td>
<td align="right">294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">31,584</td>
<td align="right">1.7%</td>
<td align="right">31,584</td>
<td align="right">1.7%</td>
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
<td align="right">1,826,874</td>
<td align="right">98.0%</td>
<td align="right">1,826,874</td>
<td align="right">98.0%</td>
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
<td align="right">2,499</td>
<td align="right">0.1%</td>
<td align="right">2,499</td>
<td align="right">0.1%</td>
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
<td align="right">1,323</td>
<td align="right">55.8%</td>
<td align="right">1,323</td>
<td align="right">55.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,050</td>
<td align="right">44.2%</td>
<td align="right">1,050</td>
<td align="right">44.2%</td>
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
<td align="left">add other</td>
<td align="right">525</td>
<td align="right">50.0%</td>
<td align="right">525</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">189</td>
<td align="right">18.0%</td>
<td align="right">189</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">2.0%</td>
<td align="right">21</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">21</td>
<td align="right">2.0%</td>
<td align="right">21</td>
<td align="right">2.0%</td>
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
<td align="right">23,877</td>
<td align="right">100.0%</td>
<td align="right">23,877</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">260,652</td>
<td align="right">0.8%</td>
<td align="right">255,087</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">273,924</td>
<td align="right">0.8%</td>
<td align="right">268,464</td>
<td align="right">0.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,542,271</td>
<td align="right">99.1%</td>
<td align="right">33,547,731</td>
<td align="right">99.1%</td>
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
<td align="right">22,890</td>
<td align="right">100.0%</td>
<td align="right">22,785</td>
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
<td align="right">1,575</td>
<td align="right">50.0%</td>
<td align="right">1,575</td>
<td align="right">50.0%</td>
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
<td align="right">1,575</td>
<td align="right">100.0%</td>
<td align="right">1,575</td>
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
<td align="right">397,362</td>
<td align="right">48.2%</td>
<td align="right">396,669</td>
<td align="right">48.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">422,646</td>
<td align="right">51.2%</td>
<td align="right">422,646</td>
<td align="right">51.3%</td>
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
<td align="right">840</td>
<td align="right">17.5%</td>
<td align="right">840</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,948</td>
<td align="right">82.5%</td>
<td align="right">3,948</td>
<td align="right">82.5%</td>
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
<td align="left">baseobject</td>
<td align="right">1,722</td>
<td align="right">43.6%</td>
<td align="right">1,722</td>
<td align="right">43.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,302</td>
<td align="right">33.0%</td>
<td align="right">1,302</td>
<td align="right">33.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">399</td>
<td align="right">10.1%</td>
<td align="right">399</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">189</td>
<td align="right">4.8%</td>
<td align="right">189</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">168</td>
<td align="right">4.3%</td>
<td align="right">168</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">105</td>
<td align="right">2.7%</td>
<td align="right">105</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">63</td>
<td align="right">1.6%</td>
<td align="right">63</td>
<td align="right">1.6%</td>
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
<td align="right">104,391</td>
<td align="right">31.5%</td>
<td align="right">94,332</td>
<td align="right">29.4%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">212,058</td>
<td align="right">64.0%</td>
<td align="right">212,058</td>
<td align="right">66.0%</td>
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
<td align="right">13,146</td>
<td align="right">4.0%</td>
<td align="right">13,146</td>
<td align="right">4.1%</td>
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
<td align="right">924</td>
<td align="right">45.8%</td>
<td align="right">924</td>
<td align="right">45.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,092</td>
<td align="right">54.2%</td>
<td align="right">1,092</td>
<td align="right">54.2%</td>
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
<td align="right">819</td>
<td align="right">75.0%</td>
<td align="right">819</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">273</td>
<td align="right">25.0%</td>
<td align="right">273</td>
<td align="right">25.0%</td>
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
<td align="right">5,254,410</td>
<td align="right">53.8%</td>
<td align="right">4,754,316</td>
<td align="right">53.7%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,501,749</td>
<td align="right">46.1%</td>
<td align="right">4,099,557</td>
<td align="right">46.3%</td>
<td align="right">-8.9%</td>
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
<td align="right">6,006</td>
<td align="right">76.7%</td>
<td align="right">5,901</td>
<td align="right">76.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,827</td>
<td align="right">23.3%</td>
<td align="right">1,827</td>
<td align="right">23.6%</td>
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
<td align="left">itertools</td>
<td align="right">462</td>
<td align="right">7.7%</td>
<td align="right">420</td>
<td align="right">7.1%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,877</td>
<td align="right">47.9%</td>
<td align="right">2,814</td>
<td align="right">47.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">777</td>
<td align="right">12.9%</td>
<td align="right">777</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">462</td>
<td align="right">7.7%</td>
<td align="right">462</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">462</td>
<td align="right">7.7%</td>
<td align="right">462</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">378</td>
<td align="right">6.3%</td>
<td align="right">378</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">231</td>
<td align="right">3.8%</td>
<td align="right">231</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">189</td>
<td align="right">3.1%</td>
<td align="right">189</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">168</td>
<td align="right">2.8%</td>
<td align="right">168</td>
<td align="right">2.8%</td>
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
<td align="left">other</td>
<td align="right">2,410,695</td>
<td align="right">2,410,695 / 0 !!</td>
<td align="right">2,410,695</td>
<td align="right">2,410,695 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,209,095</td>
<td align="right">2,209,095 / 0 !!</td>
<td align="right">2,209,095</td>
<td align="right">2,209,095 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">110,250</td>
<td align="right">110,250 / 0 !!</td>
<td align="right">110,250</td>
<td align="right">110,250 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">16,506</td>
<td align="right">16,506 / 0 !!</td>
<td align="right">16,506</td>
<td align="right">16,506 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">15,624</td>
<td align="right">15,624 / 0 !!</td>
<td align="right">15,624</td>
<td align="right">15,624 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">13,671</td>
<td align="right">13,671 / 0 !!</td>
<td align="right">13,671</td>
<td align="right">13,671 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,702</td>
<td align="right">9,702 / 0 !!</td>
<td align="right">9,702</td>
<td align="right">9,702 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,119</td>
<td align="right">7,119 / 0 !!</td>
<td align="right">7,119</td>
<td align="right">7,119 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,134</td>
<td align="right">1,134 / 0 !!</td>
<td align="right">1,134</td>
<td align="right">1,134 / 0 !!</td>
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
<td align="right">3,970,470</td>
<td align="right">16.2%</td>
<td align="right">3,468,045</td>
<td align="right">14.8%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,282,829</td>
<td align="right">82.6%</td>
<td align="right">19,734,981</td>
<td align="right">84.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">267,141</td>
<td align="right">1.1%</td>
<td align="right">266,217</td>
<td align="right">1.1%</td>
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
<td align="right">172,431</td>
<td align="right">0.7%</td>
<td align="right">172,431</td>
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
<td align="left">Success</td>
<td align="right">96,873</td>
<td align="right">91.1%</td>
<td align="right">87,381</td>
<td align="right">90.3%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,429</td>
<td align="right">8.9%</td>
<td align="right">9,429</td>
<td align="right">9.7%</td>
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
<td align="left">mutable class</td>
<td align="right">7,623</td>
<td align="right">80.8%</td>
<td align="right">7,623</td>
<td align="right">80.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,512</td>
<td align="right">16.0%</td>
<td align="right">1,512</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">168</td>
<td align="right">1.8%</td>
<td align="right">168</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">105</td>
<td align="right">1.1%</td>
<td align="right">105</td>
<td align="right">1.1%</td>
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
<td align="right">33,613,881</td>
<td align="right">99.9%</td>
<td align="right">31,832,451</td>
<td align="right">99.9%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,456</td>
<td align="right">0.0%</td>
<td align="right">15,456</td>
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
<td align="right">4,452</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">15,540</td>
<td align="right">100.0%</td>
<td align="right">15,540</td>
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
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">147</td>
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
<td align="right">1,894,452</td>
<td align="right">100.0%</td>
<td align="right">1,894,452</td>
<td align="right">100.0%</td>
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
<td align="right">147</td>
<td align="right">100.0%</td>
<td align="right">147</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">770,931</td>
<td align="right">44.8%</td>
<td align="right">769,839</td>
<td align="right">44.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">944,853</td>
<td align="right">55.0%</td>
<td align="right">945,903</td>
<td align="right">55.0%</td>
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
<td align="right">1,638</td>
<td align="right">0.1%</td>
<td align="right">1,638</td>
<td align="right">0.1%</td>
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
<td align="right">15,918</td>
<td align="right">100.0%</td>
<td align="right">15,876</td>
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
<td align="right">399</td>
<td align="right">0.1%</td>
<td align="right">399</td>
<td align="right">0.1%</td>
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
<td align="right">613,536</td>
<td align="right">99.9%</td>
<td align="right">613,536</td>
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
<td align="right">399</td>
<td align="right">100.0%</td>
<td align="right">399</td>
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
<td align="right">15,983,667</td>
<td align="right">87.8%</td>
<td align="right">15,239,301</td>
<td align="right">87.3%</td>
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
<td align="right">956,949</td>
<td align="right">5.3%</td>
<td align="right">952,056</td>
<td align="right">5.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,258,614</td>
<td align="right">6.9%</td>
<td align="right">1,258,614</td>
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
<td align="right">31,647</td>
<td align="right">96.1%</td>
<td align="right">31,647</td>
<td align="right">96.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,281</td>
<td align="right">3.9%</td>
<td align="right">1,281</td>
<td align="right">3.9%</td>
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
<td align="right">525</td>
<td align="right">41.0%</td>
<td align="right">525</td>
<td align="right">41.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">336</td>
<td align="right">26.2%</td>
<td align="right">336</td>
<td align="right">26.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">252</td>
<td align="right">19.7%</td>
<td align="right">252</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">105</td>
<td align="right">8.2%</td>
<td align="right">105</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">63</td>
<td align="right">4.9%</td>
<td align="right">63</td>
<td align="right">4.9%</td>
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
<td align="right">6,699</td>
<td align="right">0.1%</td>
<td align="right">6,699</td>
<td align="right">0.1%</td>
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
<td align="right">6,160,119</td>
<td align="right">99.9%</td>
<td align="right">6,160,119</td>
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
<td align="right">840</td>
<td align="right">85.1%</td>
<td align="right">840</td>
<td align="right">85.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">147</td>
<td align="right">14.9%</td>
<td align="right">147</td>
<td align="right">14.9%</td>
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
<td align="right">147</td>
<td align="right">100.0%</td>
<td align="right">147</td>
<td align="right">100.0%</td>
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
<td align="right">6,280,785</td>
<td align="right">1.9%</td>
<td align="right">5,771,745</td>
<td align="right">1.9%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">10,446,177</td>
<td align="right">3.2%</td>
<td align="right">9,739,002</td>
<td align="right">3.2%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">171,516,177</td>
<td align="right">52.9%</td>
<td align="right">160,928,586</td>
<td align="right">52.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">136,256,505</td>
<td align="right">42.0%</td>
<td align="right">128,201,115</td>
<td align="right">42.1%</td>
<td align="right">-5.9%</td>
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
<td align="right">104,391</td>
<td align="right">1.6%</td>
<td align="right">94,332</td>
<td align="right">1.5%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,501,749</td>
<td align="right">68.4%</td>
<td align="right">4,099,557</td>
<td align="right">66.6%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">273,924</td>
<td align="right">4.2%</td>
<td align="right">268,464</td>
<td align="right">4.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">956,949</td>
<td align="right">14.5%</td>
<td align="right">952,056</td>
<td align="right">15.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">267,141</td>
<td align="right">4.1%</td>
<td align="right">266,217</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">397,362</td>
<td align="right">6.0%</td>
<td align="right">396,669</td>
<td align="right">6.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">31,584</td>
<td align="right">0.5%</td>
<td align="right">31,584</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,877</td>
<td align="right">0.4%</td>
<td align="right">23,877</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,456</td>
<td align="right">0.2%</td>
<td align="right">15,456</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">6,699</td>
<td align="right">0.1%</td>
<td align="right">6,699</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">484,113</td>
<td align="right">7.7%</td>
<td align="right">345,597</td>
<td align="right">6.0%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,863,770</td>
<td align="right">45.6%</td>
<td align="right">2,499,861</td>
<td align="right">43.3%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">137,718</td>
<td align="right">2.2%</td>
<td align="right">132,153</td>
<td align="right">2.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">770,931</td>
<td align="right">12.3%</td>
<td align="right">769,839</td>
<td align="right">13.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">884,856</td>
<td align="right">14.1%</td>
<td align="right">884,856</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">597,513</td>
<td align="right">9.5%</td>
<td align="right">597,513</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">249,375</td>
<td align="right">4.0%</td>
<td align="right">249,375</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">118,356</td>
<td align="right">1.9%</td>
<td align="right">118,356</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">104,475</td>
<td align="right">1.7%</td>
<td align="right">104,475</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">19,215</td>
<td align="right">0.3%</td>
<td align="right">19,215</td>
<td align="right">0.3%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">16,706,991</td>
<td align="right">88.1%</td>
<td align="right">16,706,991</td>
<td align="right">88.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">484,281</td>
<td align="right">2.6%</td>
<td align="right">484,281</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">420,735</td>
<td align="right">2.2%</td>
<td align="right">420,735</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">33,075</td>
<td align="right">0.2%</td>
<td align="right">33,075</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,263,066</td>
<td align="right">6.7%</td>
<td align="right">1,263,066</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">30,114</td>
<td align="right">0.2%</td>
<td align="right">30,114</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">13,756,239</td>
<td align="right">72.5%</td>
<td align="right">13,756,239</td>
<td align="right">72.5%</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">18,967</td>
<td align="right"></td>
<td align="right">14,593</td>
<td align="right"></td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,585,748</td>
<td align="right">2.3%</td>
<td align="right">4,939,809</td>
<td align="right">2.0%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">84,212,142</td>
<td align="right">34.5%</td>
<td align="right">78,806,721</td>
<td align="right">32.5%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">108,509,814</td>
<td align="right">39.6%</td>
<td align="right">103,503,015</td>
<td align="right">38.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">95,013,843</td>
<td align="right">39.0%</td>
<td align="right">99,178,329</td>
<td align="right">40.9%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">287,018</td>
<td align="right"></td>
<td align="right">276,231</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">103,331,500</td>
<td align="right">37.7%</td>
<td align="right">107,091,845</td>
<td align="right">39.3%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">270,350</td>
<td align="right"></td>
<td align="right">264,112</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,988</td>
<td align="right">0.1%</td>
<td align="right">30,408</td>
<td align="right">0.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,934,122</td>
<td align="right"></td>
<td align="right">4,882,337</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">59,106,610</td>
<td align="right">24.2%</td>
<td align="right">59,698,126</td>
<td align="right">24.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">3,479,511</td>
<td align="right">1.3%</td>
<td align="right">3,474,051</td>
<td align="right">1.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">58,612,690</td>
<td align="right">21.4%</td>
<td align="right">58,563,090</td>
<td align="right">21.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,285,953</td>
<td align="right"></td>
<td align="right">14,282,473</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">24,304,346</td>
<td align="right"></td>
<td align="right">24,308,720</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,162,611</td>
<td align="right">36.4%</td>
<td align="right">13,161,939</td>
<td align="right">36.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,934,163</td>
<td align="right">63.5%</td>
<td align="right">22,934,961</td>
<td align="right">63.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,937,145</td>
<td align="right"></td>
<td align="right">22,937,838</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,192,725</td>
<td align="right">36.5%</td>
<td align="right">13,192,725</td>
<td align="right">36.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">59,787</td>
<td align="right"></td>
<td align="right">59,787</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">84</td>
<td align="right">97,734</td>
<td align="right">1,084,986</td>
<td align="right">43,764</td>
<td align="right">135,618</td>
<td align="right">84</td>
<td align="right">95,991</td>
<td align="right">1,033,592</td>
<td align="right">53,559</td>
<td align="right">124,857</td>
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
<td align="right">21</td>
<td align="right">1.3%</td>
<td align="right">105</td>
<td align="right">3.4%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">1.3%</td>
<td align="right">84</td>
<td align="right">2.7%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">462</td>
<td align="right">27.8%</td>
<td align="right">1,239</td>
<td align="right">39.6%</td>
<td align="right">168.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">63</td>
<td align="right">3.8%</td>
<td align="right">126</td>
<td align="right">4.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,659</td>
<td align="right"></td>
<td align="right">3,129</td>
<td align="right"></td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">735</td>
<td align="right">44.3%</td>
<td align="right">1,386</td>
<td align="right">44.3%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,693,521</td>
<td align="right"></td>
<td align="right">7,049,280</td>
<td align="right"></td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">135,862,755</td>
<td align="right">2,894.7%</td>
<td align="right">185,443,587</td>
<td align="right">2,630.7%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">462</td>
<td align="right">27.8%</td>
<td align="right">504</td>
<td align="right">16.1%</td>
<td align="right">9.1%</td>
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

A potential trace is abandoned because it is too short.
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
<td align="right">462</td>
<td align="right"></td>
<td align="right">1,239</td>
<td align="right"></td>
<td align="right">168.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">462</td>
<td align="right">100.0%</td>
<td align="right">1,239</td>
<td align="right">100.0%</td>
<td align="right">168.2%</td>
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
<td align="right">3,687,747</td>
<td align="right">76.6%</td>
<td align="right">12,830,496</td>
<td align="right">81.5%</td>
<td align="right">247.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,816,896</td>
<td align="right"></td>
<td align="right">15,740,928</td>
<td align="right"></td>
<td align="right">226.8%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">94,080</td>
<td align="right">2.0%</td>
<td align="right">306,768</td>
<td align="right">1.9%</td>
<td align="right">226.1%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,035,069</td>
<td align="right">21.5%</td>
<td align="right">2,603,664</td>
<td align="right">16.5%</td>
<td align="right">151.5%</td>
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
<td align="right">258,048</td>
<td align="right">1.6%</td>
<td align="right">258,048 / 0 !!</td>
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
<td align="left">168</td>
<td align="right">36.4%</td>
<td align="left">441</td>
<td align="right">35.6%</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">189</td>
<td align="right">40.9%</td>
<td align="left">399</td>
<td align="right">32.2%</td>
<td align="right">111.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">42</td>
<td align="right">9.1%</td>
<td align="left">105</td>
<td align="right">8.5%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">42</td>
<td align="right">9.1%</td>
<td align="left">189</td>
<td align="right">15.3%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">4.5%</td>
<td align="left">105</td>
<td align="right">8.5%</td>
<td align="right">400.0%</td>
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
<td align="right">84</td>
<td align="right">18.2%</td>
<td align="right">168</td>
<td align="right">13.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21</td>
<td align="right">4.5%</td>
<td align="right">105</td>
<td align="right">8.5%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">63</td>
<td align="right">13.6%</td>
<td align="right">168</td>
<td align="right">13.6%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">168</td>
<td align="right">36.4%</td>
<td align="right">336</td>
<td align="right">27.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">9.1%</td>
<td align="right">105</td>
<td align="right">8.5%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">13.6%</td>
<td align="right">147</td>
<td align="right">11.9%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">4.5%</td>
<td align="right">210</td>
<td align="right">16.9%</td>
<td align="right">900.0%</td>
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
<td align="right">84</td>
<td align="right">18.2%</td>
<td align="right">189</td>
<td align="right">15.3%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">63</td>
<td align="right">13.6%</td>
<td align="right">168</td>
<td align="right">13.6%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">147</td>
<td align="right">31.8%</td>
<td align="right">294</td>
<td align="right">23.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">84</td>
<td align="right">18.2%</td>
<td align="right">210</td>
<td align="right">16.9%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">63</td>
<td align="right">13.6%</td>
<td align="right">189</td>
<td align="right">15.3%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">189</td>
<td align="right">15.3%</td>
<td align="right">189 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">4.5%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">11,466</td>
<td align="right">372,666</td>
<td align="right">3,150.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">11,466</td>
<td align="right">372,666</td>
<td align="right">3,150.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">9,618</td>
<td align="right">280,392</td>
<td align="right">2,815.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">9,618</td>
<td align="right">256,389</td>
<td align="right">2,565.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">9,618</td>
<td align="right">134,841</td>
<td align="right">1,302.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">9,618</td>
<td align="right">134,841</td>
<td align="right">1,302.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,092</td>
<td align="right">8,106</td>
<td align="right">642.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">68,145</td>
<td align="right">433,524</td>
<td align="right">536.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">34,965</td>
<td align="right">209,748</td>
<td align="right">499.9%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">13,776</td>
<td align="right">75,537</td>
<td align="right">448.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">42,714</td>
<td align="right">207,984</td>
<td align="right">386.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">31,248</td>
<td align="right">144,522</td>
<td align="right">362.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">66,213</td>
<td align="right">218,253</td>
<td align="right">229.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">72,303</td>
<td align="right">235,704</td>
<td align="right">226.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">564,564</td>
<td align="right">1,782,144</td>
<td align="right">215.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">250,446</td>
<td align="right">756,483</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">110,712</td>
<td align="right">312,921</td>
<td align="right">182.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">58,527</td>
<td align="right">161,070</td>
<td align="right">175.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">62,895</td>
<td align="right">166,803</td>
<td align="right">165.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">411,894</td>
<td align="right">1,042,419</td>
<td align="right">153.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">160,671</td>
<td align="right">406,140</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">156,954</td>
<td align="right">389,025</td>
<td align="right">147.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">61,782</td>
<td align="right">150,171</td>
<td align="right">143.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">191,919</td>
<td align="right">466,116</td>
<td align="right">142.9%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">34,965</td>
<td align="right">77,091</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">34,965</td>
<td align="right">77,091</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">621,159</td>
<td align="right">1,368,507</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">136,962</td>
<td align="right">300,006</td>
<td align="right">119.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">124,677</td>
<td align="right">258,741</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">309,267</td>
<td align="right">634,200</td>
<td align="right">105.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">343,308</td>
<td align="right">698,187</td>
<td align="right">103.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">61,404</td>
<td align="right">123,900</td>
<td align="right">101.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">61,404</td>
<td align="right">123,900</td>
<td align="right">101.8%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">847,686</td>
<td align="right">1,629,327</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">255,381</td>
<td align="right">487,242</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">236,229</td>
<td align="right">362,460</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,693,521</td>
<td align="right">7,049,280</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,693,521</td>
<td align="right">7,049,280</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">5,439,798</td>
<td align="right">7,951,020</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,626,891</td>
<td align="right">2,357,901</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,626,891</td>
<td align="right">2,357,901</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,626,891</td>
<td align="right">2,357,901</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,747,452</td>
<td align="right">2,509,773</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,084,923</td>
<td align="right">1,523,424</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">2,848,776</td>
<td align="right">3,937,185</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">771,435</td>
<td align="right">1,059,744</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">184,590</td>
<td align="right">252,882</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">451,941</td>
<td align="right">614,229</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">446,565</td>
<td align="right">604,359</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">632,730</td>
<td align="right">854,007</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,859,570</td>
<td align="right">3,859,485</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">26,142,438</td>
<td align="right">34,967,940</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,186,017</td>
<td align="right">1,586,025</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">388,794</td>
<td align="right">509,607</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">976,416</td>
<td align="right">1,277,451</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,317,624</td>
<td align="right">1,723,701</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">19,694,829</td>
<td align="right">25,722,354</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,617,273</td>
<td align="right">2,101,512</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,122,425</td>
<td align="right">6,561,849</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">339,024</td>
<td align="right">432,075</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,893,063</td>
<td align="right">6,121,290</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,826,621</td>
<td align="right">3,526,719</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">776,748</td>
<td align="right">964,551</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,160,375</td>
<td align="right">2,660,469</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,160,375</td>
<td align="right">2,660,469</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">778,722</td>
<td align="right">958,188</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">798,420</td>
<td align="right">971,649</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,145,737</td>
<td align="right">3,819,879</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,690,791</td>
<td align="right">5,672,793</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">746,277</td>
<td align="right">901,740</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,507,441</td>
<td align="right">4,217,430</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,480,311</td>
<td align="right">1,770,825</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,373,967</td>
<td align="right">1,640,646</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,562,232</td>
<td align="right">1,836,765</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,562,232</td>
<td align="right">1,830,885</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">210,336</td>
<td align="right">241,899</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,369,977</td>
<td align="right">1,571,493</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">192,024</td>
<td align="right">218,610</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,045,588</td>
<td align="right">3,447,780</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">795,207</td>
<td align="right">898,128</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">216,930</td>
<td align="right">197,925</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">216,930</td>
<td align="right">197,925</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">416,703</td>
<td align="right">383,733</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">561,729</td>
<td align="right">603,981</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">640,731</td>
<td align="right">678,972</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">311,934</td>
<td align="right">330,435</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">746,046</td>
<td align="right">773,493</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">732,501</td>
<td align="right">759,024</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">746,046</td>
<td align="right">767,613</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">184,464</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,113</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">446,166</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">24,759</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">16,506</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">15,519</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right"></td>
<td align="right">10,059</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">8,799</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">5,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">4,893</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right"></td>
<td align="right">3,990</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">3,192</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right">1,596</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">1,596</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">1,596</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">1,596</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">693</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">462</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">231</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">231</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">231</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">231</td>
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
<td align="right"></td>
<td align="right">42</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-01
