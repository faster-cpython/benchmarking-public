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
<td align="right">27,265,819</td>
<td align="right">165,301</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,765,273</td>
<td align="right">2,397,120</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,863,016</td>
<td align="right">3,524,562</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,087,068</td>
<td align="right">514,944</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,356,451</td>
<td align="right">1,149,161</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">9,255,698</td>
<td align="right">4,528,444</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">235,361</td>
<td align="right">351,167</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,295,651</td>
<td align="right">660,485</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,540,747</td>
<td align="right">4,893,089</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,304,955</td>
<td align="right">712,018</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,573,836</td>
<td align="right">5,776,022</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,870,442</td>
<td align="right">1,685,979</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,002,066</td>
<td align="right">9,502,197</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">11,361,464</td>
<td align="right">7,108,944</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,368,375</td>
<td align="right">3,541,084</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,238,847</td>
<td align="right">849,921</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,810,959</td>
<td align="right">4,039,972</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,408,364</td>
<td align="right">2,498,906</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">11,822,274</td>
<td align="right">8,874,112</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,690,423</td>
<td align="right">2,812,030</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">912,147</td>
<td align="right">705,012</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,725,895</td>
<td align="right">2,110,994</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">534,680</td>
<td align="right">650,486</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,823,201</td>
<td align="right">2,213,095</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,798,682</td>
<td align="right">1,424,474</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,698,565</td>
<td align="right">3,780,181</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20,496,718</td>
<td align="right">16,591,335</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,037,852</td>
<td align="right">2,477,965</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,152,028</td>
<td align="right">6,701,963</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,190,434</td>
<td align="right">985,414</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">797,809</td>
<td align="right">669,016</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">36,518,965</td>
<td align="right">31,341,928</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,801,262</td>
<td align="right">4,122,690</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,307,745</td>
<td align="right">1,984,727</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">49,280,897</td>
<td align="right">42,671,893</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">199,491,695</td>
<td align="right">173,082,288</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,792,194</td>
<td align="right">1,562,382</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,642,195</td>
<td align="right">7,567,629</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,416,976</td>
<td align="right">3,005,960</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">33,166,710</td>
<td align="right">29,229,951</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,197,886</td>
<td align="right">1,939,288</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,191,267</td>
<td align="right">1,943,763</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,075,050</td>
<td align="right">8,099,627</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">47,748,858</td>
<td align="right">42,639,877</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">20,374,996</td>
<td align="right">18,202,567</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">217,568</td>
<td align="right">196,211</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">29,424,692</td>
<td align="right">26,546,154</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,189,441</td>
<td align="right">1,074,224</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,930,189</td>
<td align="right">15,390,406</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">32,494,160</td>
<td align="right">29,593,689</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,898,743</td>
<td align="right">3,572,580</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,840,859</td>
<td align="right">2,613,762</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">57,792,922</td>
<td align="right">53,240,971</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,272,405</td>
<td align="right">3,980,085</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">984,400</td>
<td align="right">920,372</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">15,707,665</td>
<td align="right">14,769,425</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,117,862</td>
<td align="right">1,993,228</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">35,479,204</td>
<td align="right">33,438,056</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">473,899</td>
<td align="right">446,662</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,943,615</td>
<td align="right">5,615,256</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">25,750,647</td>
<td align="right">24,593,394</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,058,630</td>
<td align="right">2,922,749</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">465,888</td>
<td align="right">445,980</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,181,536</td>
<td align="right">1,133,583</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,503,016</td>
<td align="right">13,927,575</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,703,878</td>
<td align="right">1,640,836</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,950,610</td>
<td align="right">10,566,038</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,844,340</td>
<td align="right">4,675,374</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">15,119,939</td>
<td align="right">14,594,240</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,259,119</td>
<td align="right">7,998,433</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,799,178</td>
<td align="right">3,687,268</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,581,484</td>
<td align="right">6,393,177</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">47,181,320</td>
<td align="right">45,936,197</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">10,347,853</td>
<td align="right">10,122,559</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,506,026</td>
<td align="right">9,313,660</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,022,117</td>
<td align="right">1,986,270</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,186,088</td>
<td align="right">10,022,808</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,591,045</td>
<td align="right">25,246,746</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,875,989</td>
<td align="right">2,847,436</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,979,237</td>
<td align="right">8,901,479</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,817,970</td>
<td align="right">26,601,435</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,540,309</td>
<td align="right">4,513,699</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,714,613</td>
<td align="right">46,466,741</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">965,143</td>
<td align="right">962,431</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,068,694</td>
<td align="right">1,066,510</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">85,470</td>
<td align="right">85,417</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84,797</td>
<td align="right">84,775</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,699,635</td>
<td align="right">4,700,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,351,587</td>
<td align="right">11,350,339</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">259,122</td>
<td align="right">259,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">50,232</td>
<td align="right">50,229</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,793,345</td>
<td align="right">6,792,967</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,574,612</td>
<td align="right">2,574,606</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,711,001</td>
<td align="right">11,711,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,224,787</td>
<td align="right">11,224,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,153,384</td>
<td align="right">8,153,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,938,705</td>
<td align="right">6,938,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,494,809</td>
<td align="right">6,494,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,643,820</td>
<td align="right">5,643,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,334,162</td>
<td align="right">5,334,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,327,419</td>
<td align="right">4,327,419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,858,349</td>
<td align="right">2,858,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,664,639</td>
<td align="right">2,664,639</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,946,594</td>
<td align="right">1,946,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,806,104</td>
<td align="right">1,806,104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,800,525</td>
<td align="right">1,800,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,746,789</td>
<td align="right">1,746,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,623,486</td>
<td align="right">1,623,486</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,548,306</td>
<td align="right">1,548,306</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,501,275</td>
<td align="right">1,501,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,392,417</td>
<td align="right">1,392,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,047,297</td>
<td align="right">1,047,297</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,000,580</td>
<td align="right">1,000,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">974,194</td>
<td align="right">974,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">823,880</td>
<td align="right">823,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">822,997</td>
<td align="right">822,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">820,983</td>
<td align="right">820,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">690,951</td>
<td align="right">690,951</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">663,194</td>
<td align="right">663,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">615,988</td>
<td align="right">615,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">615,988</td>
<td align="right">615,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">576,407</td>
<td align="right">576,407</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">555,786</td>
<td align="right">555,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">438,760</td>
<td align="right">438,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,660</td>
<td align="right">353,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">307,447</td>
<td align="right">307,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">296,894</td>
<td align="right">296,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">281,347</td>
<td align="right">281,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,928</td>
<td align="right">280,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,967</td>
<td align="right">255,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">231,966</td>
<td align="right">231,966</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">165,666</td>
<td align="right">165,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,618</td>
<td align="right">165,618</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,159</td>
<td align="right">163,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">137,192</td>
<td align="right">137,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,577</td>
<td align="right">122,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,790</td>
<td align="right">108,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,238</td>
<td align="right">98,238</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84,394</td>
<td align="right">84,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">82,705</td>
<td align="right">82,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,255</td>
<td align="right">76,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">64,045</td>
<td align="right">64,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">56,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,559</td>
<td align="right">55,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">44,647</td>
<td align="right">44,647</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">43,011</td>
<td align="right">43,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,532</td>
<td align="right">31,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">27,323</td>
<td align="right">27,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">25,187</td>
<td align="right">25,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">23,353</td>
<td align="right">23,353</td>
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
<td align="right">17,957</td>
<td align="right">17,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">10,991</td>
<td align="right">10,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,665</td>
<td align="right">5,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">5,557</td>
<td align="right">5,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,036</td>
<td align="right">3,036</td>
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
<td align="right">2,426</td>
<td align="right">2,426</td>
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
<td align="right">1,132</td>
<td align="right">1,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,107</td>
<td align="right">1,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,081</td>
<td align="right">1,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">967</td>
<td align="right">967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">953</td>
<td align="right">953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">777</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">589</td>
<td align="right">589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">226</td>
<td align="right">226</td>
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
<td align="right">34</td>
<td align="right">34</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">11,684,429</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">11,476,703</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">111,604</td>
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
<td align="right">1,302,202</td>
<td align="right">17.6%</td>
<td align="right">709,414</td>
<td align="right">10.4%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,095,477</td>
<td align="right">82.4%</td>
<td align="right">6,095,477</td>
<td align="right">89.5%</td>
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
<td align="right">25</td>
<td align="right">0.0%</td>
<td align="right">25</td>
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
<td align="right">2,221</td>
<td align="right">80.7%</td>
<td align="right">2,072</td>
<td align="right">79.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">532</td>
<td align="right">19.3%</td>
<td align="right">532</td>
<td align="right">20.4%</td>
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
<td align="left">add different types</td>
<td align="right">309</td>
<td align="right">13.9%</td>
<td align="right">160</td>
<td align="right">7.7%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">998</td>
<td align="right">44.9%</td>
<td align="right">998</td>
<td align="right">48.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">230</td>
<td align="right">10.4%</td>
<td align="right">230</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">211</td>
<td align="right">9.5%</td>
<td align="right">211</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">152</td>
<td align="right">6.8%</td>
<td align="right">152</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">117</td>
<td align="right">5.3%</td>
<td align="right">117</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">3.0%</td>
<td align="right">66</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">51</td>
<td align="right">2.3%</td>
<td align="right">51</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">1.6%</td>
<td align="right">36</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
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
<td align="right">473,899</td>
<td align="right">100.0%</td>
<td align="right">446,662</td>
<td align="right">100.0%</td>
<td align="right">-5.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,306</td>
<td align="right">1.2%</td>
<td align="right">62,806</td>
<td align="right">0.5%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,182,974</td>
<td align="right">15.5%</td>
<td align="right">1,936,483</td>
<td align="right">14.2%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,688,849</td>
<td align="right">83.2%</td>
<td align="right">11,659,947</td>
<td align="right">85.3%</td>
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
<td align="right">4,517</td>
<td align="right">39.7%</td>
<td align="right">2,599</td>
<td align="right">30.7%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,865</td>
<td align="right">60.3%</td>
<td align="right">5,854</td>
<td align="right">69.3%</td>
<td align="right">-14.7%</td>
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
<td align="right">3,624</td>
<td align="right">52.8%</td>
<td align="right">2,690</td>
<td align="right">46.0%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">732</td>
<td align="right">10.7%</td>
<td align="right">690</td>
<td align="right">11.8%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">815</td>
<td align="right">11.9%</td>
<td align="right">780</td>
<td align="right">13.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">845</td>
<td align="right">12.3%</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">782</td>
<td align="right">11.4%</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
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
<td align="right">8,127,473</td>
<td align="right">11.9%</td>
<td align="right">7,776,542</td>
<td align="right">11.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,981,697</td>
<td align="right">11.7%</td>
<td align="right">7,637,387</td>
<td align="right">11.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,153,962</td>
<td align="right">88.1%</td>
<td align="right">60,574,272</td>
<td align="right">88.6%</td>
<td align="right">0.7%</td>
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
<td align="right">173,099</td>
<td align="right">100.0%</td>
<td align="right">166,478</td>
<td align="right">100.0%</td>
<td align="right">-3.8%</td>
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
<td align="right">562,890</td>
<td align="right">97.8%</td>
<td align="right">562,890</td>
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
<td align="right">573,137</td>
<td align="right">99.6%</td>
<td align="right">573,137</td>
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
<td align="right">12,673</td>
<td align="right">100.0%</td>
<td align="right">12,673</td>
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
<td align="right">1,064,644</td>
<td align="right">5.8%</td>
<td align="right">1,062,460</td>
<td align="right">5.8%</td>
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
<td align="right">17,224,659</td>
<td align="right">94.1%</td>
<td align="right">17,224,656</td>
<td align="right">94.2%</td>
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
<td align="right">3,372</td>
<td align="right">0.0%</td>
<td align="right">3,372</td>
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
<td align="right">1,535</td>
<td align="right">37.3%</td>
<td align="right">1,535</td>
<td align="right">37.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,582</td>
<td align="right">62.7%</td>
<td align="right">2,582</td>
<td align="right">62.7%</td>
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
<td align="left">different types</td>
<td align="right">1,108</td>
<td align="right">42.9%</td>
<td align="right">1,108</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">679</td>
<td align="right">26.3%</td>
<td align="right">679</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">243</td>
<td align="right">9.4%</td>
<td align="right">243</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">193</td>
<td align="right">7.5%</td>
<td align="right">193</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">153</td>
<td align="right">5.9%</td>
<td align="right">153</td>
<td align="right">5.9%</td>
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
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
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
<td align="right">3,401,181</td>
<td align="right">45.0%</td>
<td align="right">2,491,958</td>
<td align="right">37.5%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,117,919</td>
<td align="right">54.5%</td>
<td align="right">4,117,919</td>
<td align="right">62.0%</td>
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
<td align="right">6,467</td>
<td align="right">84.1%</td>
<td align="right">6,232</td>
<td align="right">83.6%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,227</td>
<td align="right">15.9%</td>
<td align="right">1,227</td>
<td align="right">16.4%</td>
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
<td align="right">657</td>
<td align="right">10.2%</td>
<td align="right">529</td>
<td align="right">8.5%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,304</td>
<td align="right">20.2%</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,293</td>
<td align="right">50.9%</td>
<td align="right">3,249</td>
<td align="right">52.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,213</td>
<td align="right">18.8%</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
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
<td align="right">5,800,778</td>
<td align="right">16.0%</td>
<td align="right">4,030,216</td>
<td align="right">14.7%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,219,176</td>
<td align="right">83.3%</td>
<td align="right">23,111,710</td>
<td align="right">84.4%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">226,677</td>
<td align="right">0.6%</td>
<td align="right">223,164</td>
<td align="right">0.8%</td>
<td align="right">-1.5%</td>
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
<td align="right">9,049</td>
<td align="right">62.6%</td>
<td align="right">8,624</td>
<td align="right">61.8%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,406</td>
<td align="right">37.4%</td>
<td align="right">5,322</td>
<td align="right">38.2%</td>
<td align="right">-1.6%</td>
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
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,486</td>
<td align="right">16.4%</td>
<td align="right">1,189</td>
<td align="right">13.8%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,452</td>
<td align="right">16.0%</td>
<td align="right">1,409</td>
<td align="right">16.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,264</td>
<td align="right">47.1%</td>
<td align="right">4,243</td>
<td align="right">49.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">604</td>
<td align="right">6.7%</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.4%</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">276</td>
<td align="right">3.1%</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">253</td>
<td align="right">2.8%</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">140</td>
<td align="right">1.5%</td>
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
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">33,984,872</td>
<td align="right">26.4%</td>
<td align="right">31,582,719</td>
<td align="right">25.3%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,362,797</td>
<td align="right">11.1%</td>
<td align="right">13,795,234</td>
<td align="right">11.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">80,458,749</td>
<td align="right">62.4%</td>
<td align="right">79,481,977</td>
<td align="right">63.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">207,251</td>
<td align="right">0.2%</td>
<td align="right">207,251</td>
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
<td align="right">78,245</td>
<td align="right">10.6%</td>
<td align="right">70,367</td>
<td align="right">10.3%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">659,201</td>
<td align="right">89.4%</td>
<td align="right">613,936</td>
<td align="right">89.7%</td>
<td align="right">-6.9%</td>
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
<td align="right">392</td>
<td align="right">0.6%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,694</td>
<td align="right">4.7%</td>
<td align="right">3,652</td>
<td align="right">5.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,888</td>
<td align="right">5.0%</td>
<td align="right">3,888</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,533</td>
<td align="right">2.0%</td>
<td align="right">1,533</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,279</td>
<td align="right">1.6%</td>
<td align="right">1,279</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">989</td>
<td align="right">1.3%</td>
<td align="right">989</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">1.1%</td>
<td align="right">836</td>
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
<td align="right">204</td>
<td align="right">0.3%</td>
<td align="right">204</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">127</td>
<td align="right">0.2%</td>
<td align="right">127</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">61,909,114</td>
<td align="right">99.9%</td>
<td align="right">56,130,105</td>
<td align="right">99.9%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,292</td>
<td align="right">0.0%</td>
<td align="right">5,292</td>
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
<td align="right">9,738</td>
<td align="right">0.0%</td>
<td align="right">9,738</td>
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
<td align="right">18,196</td>
<td align="right">100.0%</td>
<td align="right">18,196</td>
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
<td align="right">138</td>
<td align="right">0.0%</td>
<td align="right">138</td>
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
<td align="right">721,404</td>
<td align="right">99.9%</td>
<td align="right">721,404</td>
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
<td align="right">451</td>
<td align="right">100.0%</td>
<td align="right">451</td>
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
<td align="right">6,491,865</td>
<td align="right">54.9%</td>
<td align="right">6,491,865</td>
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
<td align="right">5,334,162</td>
<td align="right">45.1%</td>
<td align="right">5,334,162</td>
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
<td align="right">2,841</td>
<td align="right">96.5%</td>
<td align="right">2,841</td>
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
<td align="right">2,058</td>
<td align="right">72.4%</td>
<td align="right">2,058</td>
<td align="right">72.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">25.8%</td>
<td align="right">732</td>
<td align="right">25.8%</td>
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
<td align="right">1,384,799</td>
<td align="right">9.9%</td>
<td align="right">1,384,799</td>
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
<td align="right">10,795,343</td>
<td align="right">77.1%</td>
<td align="right">10,795,343</td>
<td align="right">77.1%</td>
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
<td align="right">1,806,150</td>
<td align="right">12.9%</td>
<td align="right">1,806,150</td>
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
<td align="right">38,385</td>
<td align="right">92.2%</td>
<td align="right">38,385</td>
<td align="right">92.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,246</td>
<td align="right">7.8%</td>
<td align="right">3,246</td>
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
<td align="right">63,502</td>
<td align="right">1,956.3%</td>
<td align="right">55,730</td>
<td align="right">1,716.9%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">606</td>
<td align="right">18.7%</td>
<td align="right">606</td>
<td align="right">18.7%</td>
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
<td align="right">8.7%</td>
<td align="right">283</td>
<td align="right">8.7%</td>
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
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">105</td>
<td align="right">3.2%</td>
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
<td align="right">39</td>
<td align="right">1.2%</td>
<td align="right">39</td>
<td align="right">1.2%</td>
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
<td align="right">84,024</td>
<td align="right">3.1%</td>
<td align="right">84,002</td>
<td align="right">3.1%</td>
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
<td align="right">2,588,343</td>
<td align="right">96.8%</td>
<td align="right">2,588,343</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,023,001</td>
<td align="right">9.3%</td>
<td align="right">3,033,503</td>
<td align="right">7.1%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,847,763</td>
<td align="right">89.4%</td>
<td align="right">38,987,815</td>
<td align="right">91.5%</td>
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
<td align="right">560,621</td>
<td align="right">1.3%</td>
<td align="right">560,621</td>
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
<td align="right">82,928</td>
<td align="right">90.8%</td>
<td align="right">64,253</td>
<td align="right">88.5%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,389</td>
<td align="right">9.2%</td>
<td align="right">8,389</td>
<td align="right">11.5%</td>
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
<td align="right">5,854</td>
<td align="right">69.8%</td>
<td align="right">5,854</td>
<td align="right">69.8%</td>
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
<td align="right">7.9%</td>
<td align="right">665</td>
<td align="right">7.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,237,670</td>
<td align="right">13.4%</td>
<td align="right">848,870</td>
<td align="right">9.6%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,974,755</td>
<td align="right">86.6%</td>
<td align="right">7,973,972</td>
<td align="right">90.4%</td>
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
<td align="right">372</td>
<td align="right">31.6%</td>
<td align="right">246</td>
<td align="right">23.4%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">805</td>
<td align="right">68.4%</td>
<td align="right">805</td>
<td align="right">76.6%</td>
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
<td align="right">348</td>
<td align="right">93.5%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">6.5%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">491,507,803</td>
<td align="right">40.1%</td>
<td align="right">426,543,933</td>
<td align="right">39.0%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">38,602,147</td>
<td align="right">3.1%</td>
<td align="right">34,087,451</td>
<td align="right">3.1%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">648,035,303</td>
<td align="right">52.8%</td>
<td align="right">586,805,642</td>
<td align="right">53.7%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">48,944,812</td>
<td align="right">4.0%</td>
<td align="right">45,098,393</td>
<td align="right">4.1%</td>
<td align="right">-7.9%</td>
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
<td align="right">1,302,202</td>
<td align="right">2.8%</td>
<td align="right">709,414</td>
<td align="right">1.7%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,237,670</td>
<td align="right">2.6%</td>
<td align="right">848,870</td>
<td align="right">2.0%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,800,778</td>
<td align="right">12.4%</td>
<td align="right">4,030,216</td>
<td align="right">9.6%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,401,181</td>
<td align="right">7.3%</td>
<td align="right">2,491,958</td>
<td align="right">5.9%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,182,974</td>
<td align="right">4.7%</td>
<td align="right">1,936,483</td>
<td align="right">4.6%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,981,697</td>
<td align="right">17.0%</td>
<td align="right">7,637,387</td>
<td align="right">18.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,362,797</td>
<td align="right">30.6%</td>
<td align="right">13,795,234</td>
<td align="right">32.8%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,064,644</td>
<td align="right">2.3%</td>
<td align="right">1,062,460</td>
<td align="right">2.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,491,865</td>
<td align="right">13.8%</td>
<td align="right">6,491,865</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,384,799</td>
<td align="right">3.0%</td>
<td align="right">1,384,799</td>
<td align="right">3.3%</td>
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
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">7,828,574</td>
<td align="right">16.0%</td>
<td align="right">6,028,664</td>
<td align="right">13.4%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,381,900</td>
<td align="right">6.9%</td>
<td align="right">2,621,065</td>
<td align="right">5.8%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,613,045</td>
<td align="right">3.3%</td>
<td align="right">1,256,283</td>
<td align="right">2.8%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,028,672</td>
<td align="right">2.1%</td>
<td align="right">924,727</td>
<td align="right">2.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,706,511</td>
<td align="right">11.7%</td>
<td align="right">5,301,574</td>
<td align="right">11.8%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,383,776</td>
<td align="right">11.0%</td>
<td align="right">5,721,705</td>
<td align="right">12.7%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,233,558</td>
<td align="right">6.6%</td>
<td align="right">3,140,557</td>
<td align="right">7.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,121,377</td>
<td align="right">32.9%</td>
<td align="right">16,121,193</td>
<td align="right">35.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,806,067</td>
<td align="right">3.7%</td>
<td align="right">1,806,067</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">532,453</td>
<td align="right">1.1%</td>
<td align="right">532,453</td>
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
<td align="left">Frame objects created</td>
<td align="right">874,191</td>
<td align="right">1.3%</td>
<td align="right">1,104,699</td>
<td align="right">1.6%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,250,682</td>
<td align="right">7.6%</td>
<td align="right">5,365,243</td>
<td align="right">7.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,573,687</td>
<td align="right">16.7%</td>
<td align="right">11,688,245</td>
<td align="right">16.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,573,687</td>
<td align="right">16.7%</td>
<td align="right">11,688,245</td>
<td align="right">16.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,622,433</td>
<td align="right">83.3%</td>
<td align="right">57,623,675</td>
<td align="right">83.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">388,603</td>
<td align="right">0.6%</td>
<td align="right">388,600</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,321,900</td>
<td align="right">9.1%</td>
<td align="right">6,321,897</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,323,005</td>
<td align="right">9.1%</td>
<td align="right">6,323,002</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">48,095,890</td>
<td align="right">69.5%</td>
<td align="right">48,095,884</td>
<td align="right">69.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
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
<td align="right">453,539</td>
<td align="right">0.7%</td>
<td align="right">453,539</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,162,144</td>
<td align="right">1.7%</td>
<td align="right">1,162,144</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">245,446,491</td>
<td align="right">21.0%</td>
<td align="right">322,173,379</td>
<td align="right">26.5%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">270,121,368</td>
<td align="right">25.8%</td>
<td align="right">349,133,371</td>
<td align="right">32.4%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">149,384,310</td>
<td align="right">12.8%</td>
<td align="right">182,831,594</td>
<td align="right">15.0%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,771,489</td>
<td align="right"></td>
<td align="right">1,475,101</td>
<td align="right"></td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,020,849</td>
<td align="right"></td>
<td align="right">1,727,439</td>
<td align="right"></td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">200,408,140</td>
<td align="right">17.2%</td>
<td align="right">178,422,977</td>
<td align="right">14.7%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">133,584,463</td>
<td align="right">12.8%</td>
<td align="right">120,864,552</td>
<td align="right">11.2%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">466,665,530</td>
<td align="right">44.6%</td>
<td align="right">423,510,923</td>
<td align="right">39.2%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">572,108,807</td>
<td align="right">49.0%</td>
<td align="right">531,704,248</td>
<td align="right">43.8%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">175,244,118</td>
<td align="right">16.8%</td>
<td align="right">185,553,918</td>
<td align="right">17.2%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">251,566</td>
<td align="right"></td>
<td align="right">254,421</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">46,805,830</td>
<td align="right"></td>
<td align="right">47,269,168</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">47,857,707</td>
<td align="right">50.3%</td>
<td align="right">48,319,833</td>
<td align="right">50.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">48,208,482</td>
<td align="right">50.7%</td>
<td align="right">48,672,665</td>
<td align="right">50.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">312,048</td>
<td align="right">0.3%</td>
<td align="right">314,021</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">54,956,679</td>
<td align="right"></td>
<td align="right">54,692,031</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">29,139,978</td>
<td align="right"></td>
<td align="right">29,035,793</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,727</td>
<td align="right">0.0%</td>
<td align="right">38,811</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,858,339</td>
<td align="right">49.3%</td>
<td align="right">46,858,668</td>
<td align="right">49.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,883,809</td>
<td align="right"></td>
<td align="right">46,884,138</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,112,093</td>
<td align="right"></td>
<td align="right">1,112,093</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">99,256</td>
<td align="right">8.9%</td>
<td align="right">99,256</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">5,007</td>
<td align="right">0.5%</td>
<td align="right">5,007</td>
<td align="right">0.5%</td>
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
<td align="right">1,327</td>
<td align="right">27,060</td>
<td align="right">70,845,782</td>
<td align="right">11,097,434</td>
<td align="right">1,947,812</td>
<td align="right">1,327</td>
<td align="right">27,060</td>
<td align="right">70,847,075</td>
<td align="right">11,097,823</td>
<td align="right">1,950,653</td>
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
Stats gathered on: 2025-02-06
