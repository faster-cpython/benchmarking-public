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
<td align="left">NOT_TAKEN</td>
<td align="right">91,371</td>
<td align="right">472,282</td>
<td align="right">416.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">845,187</td>
<td align="right">34,062</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">243,768</td>
<td align="right">110,943</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,397,214</td>
<td align="right">655,977</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">885,339</td>
<td align="right">452,046</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">642,747</td>
<td align="right">340,662</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,393,328</td>
<td align="right">1,283,843</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">465,927</td>
<td align="right">260,484</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,789,956</td>
<td align="right">1,017,807</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">737,562</td>
<td align="right">443,520</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">878,031</td>
<td align="right">549,415</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,723,540</td>
<td align="right">4,315,142</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,592,444</td>
<td align="right">11,516,475</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7,901,013</td>
<td align="right">5,290,842</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,441,209</td>
<td align="right">978,900</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,811,746</td>
<td align="right">2,599,344</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">700,791</td>
<td align="right">498,260</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,735,427</td>
<td align="right">4,128,599</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,708,808</td>
<td align="right">4,155,123</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">828,723</td>
<td align="right">609,684</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,204,637</td>
<td align="right">6,054,867</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">29,869,277</td>
<td align="right">23,027,661</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,852,129</td>
<td align="right">14,592,275</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">13,231,650</td>
<td align="right">10,356,637</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,287,693</td>
<td align="right">3,411,795</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3,285,093</td>
<td align="right">2,653,854</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">144,270</td>
<td align="right">116,823</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">490,308</td>
<td align="right">411,516</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,781,193</td>
<td align="right">1,498,192</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,843,001</td>
<td align="right">2,395,071</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,962,319</td>
<td align="right">4,187,839</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">254,352</td>
<td align="right">218,196</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">383,859</td>
<td align="right">333,774</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,180,430</td>
<td align="right">1,900,639</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">29,985,499</td>
<td align="right">26,259,829</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,357,955</td>
<td align="right">4,748,630</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,602,330</td>
<td align="right">29,372,140</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,791,800</td>
<td align="right">3,423,145</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">83,347,034</td>
<td align="right">76,030,972</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,443,094</td>
<td align="right">4,802,974</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,963,835</td>
<td align="right">2,724,576</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,790,632</td>
<td align="right">8,105,282</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">65,113,507</td>
<td align="right">60,476,761</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,203,312</td>
<td align="right">7,625,563</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,275,639</td>
<td align="right">6,763,945</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,698,181</td>
<td align="right">5,317,606</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">8,586,708</td>
<td align="right">9,145,497</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">5,985</td>
<td align="right">5,607</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">66,048,041</td>
<td align="right">61,896,914</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">15,297,910</td>
<td align="right">14,369,598</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,611,203</td>
<td align="right">2,453,157</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">96,236,951</td>
<td align="right">90,580,464</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,000,037</td>
<td align="right">14,142,479</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">7,051,664</td>
<td align="right">6,671,399</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">27,294,771</td>
<td align="right">25,938,063</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">28,140</td>
<td align="right">26,775</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">81,606</td>
<td align="right">85,323</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">52,500</td>
<td align="right">50,295</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">26,826,426</td>
<td align="right">25,715,150</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,267,153</td>
<td align="right">4,438,896</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,115,481</td>
<td align="right">61,624,158</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">348,987,322</td>
<td align="right">335,746,287</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">70,328,752</td>
<td align="right">67,763,570</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">80,094</td>
<td align="right">77,238</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">33,791,801</td>
<td align="right">32,661,326</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,345,918</td>
<td align="right">15,843,115</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">79,674</td>
<td align="right">77,238</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,997,659</td>
<td align="right">9,706,669</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,837,457</td>
<td align="right">2,762,739</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,288,845</td>
<td align="right">2,233,345</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">23,148,150</td>
<td align="right">22,591,182</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,003,312</td>
<td align="right">31,237,382</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,324,859</td>
<td align="right">2,269,728</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,846,754</td>
<td align="right">8,637,426</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">15,091,012</td>
<td align="right">14,736,511</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,111,126</td>
<td align="right">4,024,291</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,944,598</td>
<td align="right">3,865,449</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,671,735</td>
<td align="right">67,354,357</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,853,166</td>
<td align="right">4,760,313</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">138,957</td>
<td align="right">136,353</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,541,984</td>
<td align="right">5,451,201</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">101,609,965</td>
<td align="right">99,958,784</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,914,790</td>
<td align="right">12,747,630</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,483,304</td>
<td align="right">32,069,919</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,605,833</td>
<td align="right">52,924,094</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,433,564</td>
<td align="right">2,405,004</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,974,151</td>
<td align="right">12,829,608</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,273,755</td>
<td align="right">1,259,769</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,061,755</td>
<td align="right">50,512,706</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">32,928,339</td>
<td align="right">32,632,643</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">7,542,001</td>
<td align="right">7,475,179</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">20,559,626</td>
<td align="right">20,384,864</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">985,008</td>
<td align="right">978,654</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">504,147</td>
<td align="right">501,543</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">42,158,250</td>
<td align="right">41,981,580</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">98,928,580</td>
<td align="right">98,543,784</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">195,615</td>
<td align="right">194,901</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">111,381,914</td>
<td align="right">110,984,603</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,564,982</td>
<td align="right">2,557,086</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,347,927</td>
<td align="right">1,343,895</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,828,198</td>
<td align="right">6,818,875</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,325,394</td>
<td align="right">1,323,945</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">25,268,754</td>
<td align="right">25,245,171</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,687,201</td>
<td align="right">3,685,395</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">422,310</td>
<td align="right">422,226</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">451,731</td>
<td align="right">451,689</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,049</td>
<td align="right">164,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,323,628</td>
<td align="right">3,323,544</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,415,437</td>
<td align="right">4,415,395</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,065,514</td>
<td align="right">6,065,535</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">16,454,046</td>
<td align="right">16,454,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">27,380,459</td>
<td align="right">27,380,429</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">20,406,326</td>
<td align="right">20,406,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,414,905</td>
<td align="right">13,414,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,650,841</td>
<td align="right">12,650,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,627,031</td>
<td align="right">8,627,031</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,512,224</td>
<td align="right">8,512,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,496,726</td>
<td align="right">8,496,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,779,952</td>
<td align="right">7,779,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,825,651</td>
<td align="right">6,825,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,727,621</td>
<td align="right">6,727,621</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,334,247</td>
<td align="right">6,334,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,622,309</td>
<td align="right">5,622,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,476,359</td>
<td align="right">5,476,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,663,302</td>
<td align="right">4,663,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,203,969</td>
<td align="right">4,203,969</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,036,263</td>
<td align="right">4,036,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,366,086</td>
<td align="right">3,366,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,327,913</td>
<td align="right">2,327,913</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,993,614</td>
<td align="right">1,993,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,693,692</td>
<td align="right">1,693,692</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,480,248</td>
<td align="right">1,480,248</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,427,202</td>
<td align="right">1,427,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,320,606</td>
<td align="right">1,320,606</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,280,790</td>
<td align="right">1,280,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,236,585</td>
<td align="right">1,236,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,231,967</td>
<td align="right">1,231,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,195,194</td>
<td align="right">1,195,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,195,194</td>
<td align="right">1,195,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">902,538</td>
<td align="right">902,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">735,859</td>
<td align="right">735,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">536,256</td>
<td align="right">536,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">532,434</td>
<td align="right">532,434</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">455,448</td>
<td align="right">455,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">452,928</td>
<td align="right">452,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">333,543</td>
<td align="right">333,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">326,823</td>
<td align="right">326,823</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">285,327</td>
<td align="right">285,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">245,763</td>
<td align="right">245,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">241,731</td>
<td align="right">241,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">212,394</td>
<td align="right">212,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">209,244</td>
<td align="right">209,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">203,574</td>
<td align="right">203,574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">128,205</td>
<td align="right">128,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">127,596</td>
<td align="right">127,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">120,267</td>
<td align="right">120,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">110,460</td>
<td align="right">110,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">74,319</td>
<td align="right">74,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,135</td>
<td align="right">72,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,373</td>
<td align="right">65,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60,816</td>
<td align="right">60,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">56,952</td>
<td align="right">56,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">30,156</td>
<td align="right">30,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21,294</td>
<td align="right">21,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">20,706</td>
<td align="right">20,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,475</td>
<td align="right">20,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,207</td>
<td align="right">18,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">14,049</td>
<td align="right">14,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,881</td>
<td align="right">13,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,395</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,972</td>
<td align="right">6,972</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,502</td>
<td align="right">5,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,242</td>
<td align="right">4,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,011</td>
<td align="right">4,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,465</td>
<td align="right">3,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,638</td>
<td align="right">1,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,239</td>
<td align="right">1,239</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">609</td>
<td align="right">609</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">94,420</td>
<td align="right">0.3%</td>
<td align="right">49,900</td>
<td align="right">0.1%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,928,425</td>
<td align="right">14.0%</td>
<td align="right">4,155,793</td>
<td align="right">12.5%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,105,291</td>
<td align="right">85.6%</td>
<td align="right">29,095,143</td>
<td align="right">87.3%</td>
<td align="right">-3.4%</td>
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
<td align="right">20,601</td>
<td align="right">57.8%</td>
<td align="right">18,753</td>
<td align="right">57.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,015</td>
<td align="right">42.2%</td>
<td align="right">14,175</td>
<td align="right">43.0%</td>
<td align="right">-5.6%</td>
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
<td align="left">floor divide</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">5,229</td>
<td align="right">25.4%</td>
<td align="right">3,885</td>
<td align="right">20.7%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">756</td>
<td align="right">3.7%</td>
<td align="right">651</td>
<td align="right">3.5%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">588</td>
<td align="right">2.9%</td>
<td align="right">525</td>
<td align="right">2.8%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,289</td>
<td align="right">11.1%</td>
<td align="right">2,121</td>
<td align="right">11.3%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">777</td>
<td align="right">3.8%</td>
<td align="right">735</td>
<td align="right">3.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,360</td>
<td align="right">16.3%</td>
<td align="right">3,297</td>
<td align="right">17.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">2,961</td>
<td align="right">14.4%</td>
<td align="right">2,940</td>
<td align="right">15.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">2,310</td>
<td align="right">11.2%</td>
<td align="right">2,310</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">336</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">336</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">210</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">210</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">147</td>
<td align="right">0.7%</td>
<td align="right">147</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">105</td>
<td align="right">0.5%</td>
<td align="right">105</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
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
<td align="right">737,562</td>
<td align="right">100.0%</td>
<td align="right">443,520</td>
<td align="right">100.0%</td>
<td align="right">-39.9%</td>
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
<td align="right">113,970,194</td>
<td align="right">89.8%</td>
<td align="right">113,671,691</td>
<td align="right">89.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,678,515</td>
<td align="right">10.0%</td>
<td align="right">12,670,075</td>
<td align="right">10.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,580,803</td>
<td align="right">9.9%</td>
<td align="right">12,572,509</td>
<td align="right">9.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
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
<td align="right">339,443</td>
<td align="right">100.0%</td>
<td align="right">339,297</td>
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
<td align="right">483</td>
<td align="right">483 / 0 !!</td>
<td align="right">483</td>
<td align="right">483 / 0 !!</td>
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
<td align="right">636,615</td>
<td align="right">96.7%</td>
<td align="right">636,615</td>
<td align="right">96.7%</td>
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
<td align="right">637,287</td>
<td align="right">96.8%</td>
<td align="right">637,287</td>
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
<td align="right">21,966</td>
<td align="right">100.0%</td>
<td align="right">21,966</td>
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
<td align="right">4,830,339</td>
<td align="right">11.5%</td>
<td align="right">4,737,528</td>
<td align="right">11.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,037,211</td>
<td align="right">88.4%</td>
<td align="right">37,037,214</td>
<td align="right">88.5%</td>
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
<td align="right">29,400</td>
<td align="right">0.1%</td>
<td align="right">29,400</td>
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
<td align="left">Failure</td>
<td align="right">11,088</td>
<td align="right">47.4%</td>
<td align="right">11,046</td>
<td align="right">47.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,285</td>
<td align="right">52.6%</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
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
<td align="right">3,654</td>
<td align="right">33.0%</td>
<td align="right">3,633</td>
<td align="right">32.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,305</td>
<td align="right">38.8%</td>
<td align="right">4,284</td>
<td align="right">38.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">903</td>
<td align="right">8.1%</td>
<td align="right">903</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">840</td>
<td align="right">7.6%</td>
<td align="right">840</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">420</td>
<td align="right">3.8%</td>
<td align="right">420</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">378</td>
<td align="right">3.4%</td>
<td align="right">378</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">210</td>
<td align="right">1.9%</td>
<td align="right">210</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
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
<td align="right">3,789,099</td>
<td align="right">33.5%</td>
<td align="right">2,577,168</td>
<td align="right">25.5%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,476,082</td>
<td align="right">66.1%</td>
<td align="right">7,476,082</td>
<td align="right">74.0%</td>
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
<td align="right">26,439</td>
<td align="right">0.2%</td>
<td align="right">26,439</td>
<td align="right">0.3%</td>
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
<td align="right">18,279</td>
<td align="right">79.0%</td>
<td align="right">17,808</td>
<td align="right">78.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,851</td>
<td align="right">21.0%</td>
<td align="right">4,851</td>
<td align="right">21.4%</td>
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
<td align="right">8,178</td>
<td align="right">44.7%</td>
<td align="right">7,938</td>
<td align="right">44.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">12.3%</td>
<td align="right">2,184</td>
<td align="right">12.3%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">4,116</td>
<td align="right">22.5%</td>
<td align="right">4,011</td>
<td align="right">22.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,738</td>
<td align="right">20.4%</td>
<td align="right">3,675</td>
<td align="right">20.6%</td>
<td align="right">-1.7%</td>
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
<td align="right">233,310</td>
<td align="right">0.5%</td>
<td align="right">152,838</td>
<td align="right">0.4%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,671,176</td>
<td align="right">11.4%</td>
<td align="right">4,121,922</td>
<td align="right">9.6%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,742,104</td>
<td align="right">88.0%</td>
<td align="right">38,779,572</td>
<td align="right">90.0%</td>
<td align="right">-11.3%</td>
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
<td align="right">22,470</td>
<td align="right">53.5%</td>
<td align="right">18,060</td>
<td align="right">50.1%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19,530</td>
<td align="right">46.5%</td>
<td align="right">17,997</td>
<td align="right">49.9%</td>
<td align="right">-7.8%</td>
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
<td align="left">seq iter</td>
<td align="right">378</td>
<td align="right">1.7%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,174</td>
<td align="right">27.5%</td>
<td align="right">3,024</td>
<td align="right">16.7%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">189</td>
<td align="right">0.8%</td>
<td align="right">126</td>
<td align="right">0.7%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,704</td>
<td align="right">20.9%</td>
<td align="right">4,116</td>
<td align="right">22.8%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,851</td>
<td align="right">21.6%</td>
<td align="right">4,620</td>
<td align="right">25.6%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,155</td>
<td align="right">5.1%</td>
<td align="right">1,134</td>
<td align="right">6.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,953</td>
<td align="right">8.7%</td>
<td align="right">1,932</td>
<td align="right">10.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">924</td>
<td align="right">4.1%</td>
<td align="right">924</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">525</td>
<td align="right">2.3%</td>
<td align="right">525</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">231</td>
<td align="right">1.0%</td>
<td align="right">231</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.7%</td>
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
<td align="left">list</td>
<td align="right">9,144,784</td>
<td align="right">9,144,784 / 0 !!</td>
<td align="right">9,144,784</td>
<td align="right">9,144,784 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">5,551,224</td>
<td align="right">5,551,224 / 0 !!</td>
<td align="right">5,551,224</td>
<td align="right">5,551,224 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,654,355</td>
<td align="right">3,654,355 / 0 !!</td>
<td align="right">3,654,355</td>
<td align="right">3,654,355 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">858,081</td>
<td align="right">858,081 / 0 !!</td>
<td align="right">858,081</td>
<td align="right">858,081 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">728,616</td>
<td align="right">728,616 / 0 !!</td>
<td align="right">728,616</td>
<td align="right">728,616 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">363,510</td>
<td align="right">363,510 / 0 !!</td>
<td align="right">363,510</td>
<td align="right">363,510 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">243,705</td>
<td align="right">243,705 / 0 !!</td>
<td align="right">243,705</td>
<td align="right">243,705 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,713</td>
<td align="right">13,713 / 0 !!</td>
<td align="right">13,713</td>
<td align="right">13,713 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">6,804</td>
<td align="right">6,804 / 0 !!</td>
<td align="right">6,804</td>
<td align="right">6,804 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">163,181,658</td>
<td align="right">67.5%</td>
<td align="right">159,485,494</td>
<td align="right">67.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,991,652</td>
<td align="right">13.2%</td>
<td align="right">31,578,771</td>
<td align="right">13.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">46,027,253</td>
<td align="right">19.0%</td>
<td align="right">46,041,593</td>
<td align="right">19.4%</td>
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
<td align="right">341,082</td>
<td align="right">0.1%</td>
<td align="right">341,082</td>
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
<td align="left">Failure</td>
<td align="right">186,627</td>
<td align="right">15.9%</td>
<td align="right">186,186</td>
<td align="right">15.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">986,580</td>
<td align="right">84.1%</td>
<td align="right">986,748</td>
<td align="right">84.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">567</td>
<td align="right">0.3%</td>
<td align="right">588</td>
<td align="right">0.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">15,603</td>
<td align="right">8.4%</td>
<td align="right">15,456</td>
<td align="right">8.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">18,942</td>
<td align="right">10.1%</td>
<td align="right">18,921</td>
<td align="right">10.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,063</td>
<td align="right">11.3%</td>
<td align="right">21,084</td>
<td align="right">11.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,536</td>
<td align="right">2.4%</td>
<td align="right">4,536</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,591</td>
<td align="right">1.9%</td>
<td align="right">3,591</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">1,869</td>
<td align="right">1.0%</td>
<td align="right">1,869</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,806</td>
<td align="right">1.0%</td>
<td align="right">1,806</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,092</td>
<td align="right">0.6%</td>
<td align="right">1,092</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">840</td>
<td align="right">0.5%</td>
<td align="right">840</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">756</td>
<td align="right">0.4%</td>
<td align="right">756</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">609</td>
<td align="right">0.3%</td>
<td align="right">609</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">129,188,038</td>
<td align="right">99.8%</td>
<td align="right">122,059,969</td>
<td align="right">99.8%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,509</td>
<td align="right">0.1%</td>
<td align="right">103,509</td>
<td align="right">0.1%</td>
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
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">1,134</td>
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
<td align="right">40,950</td>
<td align="right">0.0%</td>
<td align="right">40,950</td>
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
<td align="right">100,611</td>
<td align="right">100.0%</td>
<td align="right">100,611</td>
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
<td align="right">2,121</td>
<td align="right">0.1%</td>
<td align="right">2,121</td>
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
<td align="right">3,578,480</td>
<td align="right">99.9%</td>
<td align="right">3,578,480</td>
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
<td align="right">2,121</td>
<td align="right">100.0%</td>
<td align="right">2,121</td>
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
<td align="right">6,815,823</td>
<td align="right">55.4%</td>
<td align="right">6,815,823</td>
<td align="right">55.4%</td>
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
<td align="right">5,476,359</td>
<td align="right">44.5%</td>
<td align="right">5,476,359</td>
<td align="right">44.5%</td>
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
<td align="right">903</td>
<td align="right">9.2%</td>
<td align="right">903</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,925</td>
<td align="right">90.8%</td>
<td align="right">8,925</td>
<td align="right">90.8%</td>
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
<td align="right">6,594</td>
<td align="right">73.9%</td>
<td align="right">6,594</td>
<td align="right">73.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,121</td>
<td align="right">23.8%</td>
<td align="right">2,121</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">210</td>
<td align="right">2.4%</td>
<td align="right">210</td>
<td align="right">2.4%</td>
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
<td align="right">3,657,801</td>
<td align="right">8.1%</td>
<td align="right">3,656,016</td>
<td align="right">8.1%</td>
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
<td align="right">27,752,511</td>
<td align="right">61.5%</td>
<td align="right">27,752,511</td>
<td align="right">61.5%</td>
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
<td align="right">13,706,259</td>
<td align="right">30.4%</td>
<td align="right">13,706,259</td>
<td align="right">30.4%</td>
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
<td align="right">16,422</td>
<td align="right">5.7%</td>
<td align="right">16,401</td>
<td align="right">5.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">271,173</td>
<td align="right">94.3%</td>
<td align="right">271,173</td>
<td align="right">94.3%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">189</td>
<td align="right">1.2%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111,321</td>
<td align="right">677.9%</td>
<td align="right">111,006</td>
<td align="right">676.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">7,539</td>
<td align="right">45.9%</td>
<td align="right">7,539</td>
<td align="right">46.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,360</td>
<td align="right">20.5%</td>
<td align="right">3,360</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">1,869</td>
<td align="right">11.4%</td>
<td align="right">1,869</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,092</td>
<td align="right">6.6%</td>
<td align="right">1,092</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">630</td>
<td align="right">3.8%</td>
<td align="right">630</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">609</td>
<td align="right">3.7%</td>
<td align="right">609</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">441</td>
<td align="right">2.7%</td>
<td align="right">441</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">168</td>
<td align="right">1.0%</td>
<td align="right">168</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
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
<td align="right">609</td>
<td align="right">100.0%</td>
<td align="right">609</td>
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
<td align="right">239,757</td>
<td align="right">6.2%</td>
<td align="right">107,058</td>
<td align="right">2.9%</td>
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
<td align="right">3,629,325</td>
<td align="right">93.7%</td>
<td align="right">3,629,325</td>
<td align="right">97.0%</td>
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
<td align="right">1,890</td>
<td align="right">47.1%</td>
<td align="right">1,764</td>
<td align="right">45.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,121</td>
<td align="right">52.9%</td>
<td align="right">2,121</td>
<td align="right">54.6%</td>
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
<td align="left">bytearray int</td>
<td align="right">441</td>
<td align="right">23.3%</td>
<td align="right">315</td>
<td align="right">17.9%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">819</td>
<td align="right">43.3%</td>
<td align="right">819</td>
<td align="right">46.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">252</td>
<td align="right">13.3%</td>
<td align="right">252</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">147</td>
<td align="right">7.8%</td>
<td align="right">147</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">126</td>
<td align="right">6.7%</td>
<td align="right">126</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">105</td>
<td align="right">5.6%</td>
<td align="right">105</td>
<td align="right">6.0%</td>
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
<td align="right">7,038,969</td>
<td align="right">6.7%</td>
<td align="right">7,714,602</td>
<td align="right">7.4%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">96,754,772</td>
<td align="right">92.3%</td>
<td align="right">95,830,214</td>
<td align="right">91.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">919,068</td>
<td align="right">0.9%</td>
<td align="right">912,840</td>
<td align="right">0.9%</td>
<td align="right">-0.7%</td>
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
<td align="right">180,726</td>
<td align="right">91.5%</td>
<td align="right">193,473</td>
<td align="right">92.1%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,695</td>
<td align="right">8.5%</td>
<td align="right">16,590</td>
<td align="right">7.9%</td>
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
<td align="right">1,113</td>
<td align="right">6.7%</td>
<td align="right">1,029</td>
<td align="right">6.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,218</td>
<td align="right">7.3%</td>
<td align="right">1,197</td>
<td align="right">7.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,626</td>
<td align="right">63.6%</td>
<td align="right">10,626</td>
<td align="right">64.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,617</td>
<td align="right">9.7%</td>
<td align="right">1,617</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,008</td>
<td align="right">6.0%</td>
<td align="right">1,008</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">756</td>
<td align="right">4.5%</td>
<td align="right">756</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">147</td>
<td align="right">0.9%</td>
<td align="right">147</td>
<td align="right">0.9%</td>
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
<td align="right">839,874</td>
<td align="right">3.2%</td>
<td align="right">29,127</td>
<td align="right">0.1%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">25,423,305</td>
<td align="right">96.8%</td>
<td align="right">25,426,407</td>
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
<td align="left">Failure</td>
<td align="right">903</td>
<td align="right">17.0%</td>
<td align="right">525</td>
<td align="right">10.6%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,410</td>
<td align="right">83.0%</td>
<td align="right">4,410</td>
<td align="right">89.4%</td>
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
<td align="right">819</td>
<td align="right">90.7%</td>
<td align="right">441</td>
<td align="right">84.0%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">84</td>
<td align="right">9.3%</td>
<td align="right">84</td>
<td align="right">16.0%</td>
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
<td align="right">86,174,796</td>
<td align="right">3.9%</td>
<td align="right">80,707,077</td>
<td align="right">3.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">796,192,171</td>
<td align="right">35.9%</td>
<td align="right">751,838,640</td>
<td align="right">35.4%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,257,626,913</td>
<td align="right">56.6%</td>
<td align="right">1,210,216,207</td>
<td align="right">57.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">80,515,741</td>
<td align="right">3.6%</td>
<td align="right">81,072,625</td>
<td align="right">3.8%</td>
<td align="right">0.7%</td>
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
<td align="right">3,789,099</td>
<td align="right">4.9%</td>
<td align="right">2,577,168</td>
<td align="right">3.6%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,671,176</td>
<td align="right">7.3%</td>
<td align="right">4,121,922</td>
<td align="right">5.7%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,928,425</td>
<td align="right">6.3%</td>
<td align="right">4,155,793</td>
<td align="right">5.7%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,830,339</td>
<td align="right">6.2%</td>
<td align="right">4,737,528</td>
<td align="right">6.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">31,991,652</td>
<td align="right">41.1%</td>
<td align="right">31,578,771</td>
<td align="right">43.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">919,068</td>
<td align="right">1.2%</td>
<td align="right">912,840</td>
<td align="right">1.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,580,803</td>
<td align="right">16.2%</td>
<td align="right">12,572,509</td>
<td align="right">17.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,657,801</td>
<td align="right">4.7%</td>
<td align="right">3,656,016</td>
<td align="right">5.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,815,823</td>
<td align="right">8.8%</td>
<td align="right">6,815,823</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">839,874</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">636,615</td>
<td align="right">0.9%</td>
<td align="right"></td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">906,885</td>
<td align="right">1.1%</td>
<td align="right">1,100,820</td>
<td align="right">1.4%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,021,572</td>
<td align="right">2.5%</td>
<td align="right">2,317,666</td>
<td align="right">2.9%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,898,648</td>
<td align="right">7.3%</td>
<td align="right">6,382,026</td>
<td align="right">7.9%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,976,975</td>
<td align="right">11.1%</td>
<td align="right">8,713,622</td>
<td align="right">10.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,568,773</td>
<td align="right">11.9%</td>
<td align="right">9,820,671</td>
<td align="right">12.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">9,068,010</td>
<td align="right">11.3%</td>
<td align="right">8,831,268</td>
<td align="right">10.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,664,899</td>
<td align="right">4.6%</td>
<td align="right">3,663,786</td>
<td align="right">4.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">18,348,939</td>
<td align="right">22.8%</td>
<td align="right">18,348,939</td>
<td align="right">22.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,706,217</td>
<td align="right">17.0%</td>
<td align="right">13,706,217</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">5,267,178</td>
<td align="right">6.5%</td>
<td align="right">5,267,178</td>
<td align="right">6.5%</td>
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
<td align="right">561,604</td>
<td align="right">0.5%</td>
<td align="right">561,616</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">2,973,600</td>
<td align="right">2.4%</td>
<td align="right">2,973,558</td>
<td align="right">2.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">27,746,615</td>
<td align="right">22.3%</td>
<td align="right">27,746,585</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">27,746,615</td>
<td align="right">22.3%</td>
<td align="right">27,746,585</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">96,657,756</td>
<td align="right">77.7%</td>
<td align="right">96,657,810</td>
<td align="right">77.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">24,758,945</td>
<td align="right">19.9%</td>
<td align="right">24,758,957</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">24,773,015</td>
<td align="right">19.9%</td>
<td align="right">24,773,027</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">100,761,019</td>
<td align="right">81.0%</td>
<td align="right">100,761,043</td>
<td align="right">81.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">682,689</td>
<td align="right">0.5%</td>
<td align="right">682,689</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">4,325,471</td>
<td align="right">3.5%</td>
<td align="right">4,325,471</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">1,449</td>
<td align="right">0.0%</td>
<td align="right">1,449</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,677,753</td>
<td align="right">1.3%</td>
<td align="right">1,677,753</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">756,762</td>
<td align="right"></td>
<td align="right">665,848</td>
<td align="right"></td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,595,432</td>
<td align="right"></td>
<td align="right">3,334,277</td>
<td align="right"></td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,867,950</td>
<td align="right"></td>
<td align="right">2,697,116</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">496,670,884</td>
<td align="right">31.8%</td>
<td align="right">515,416,755</td>
<td align="right">33.0%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">694,152,852</td>
<td align="right">44.4%</td>
<td align="right">674,013,156</td>
<td align="right">43.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">554,046,766</td>
<td align="right">35.5%</td>
<td align="right">540,481,427</td>
<td align="right">34.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">518,662,561</td>
<td align="right">33.2%</td>
<td align="right">530,834,188</td>
<td align="right">34.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,695,591</td>
<td align="right">2.3%</td>
<td align="right">35,120,104</td>
<td align="right">2.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,628,242</td>
<td align="right">4.5%</td>
<td align="right">68,541,131</td>
<td align="right">4.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">489,237</td>
<td align="right">0.3%</td>
<td align="right">495,978</td>
<td align="right">0.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">419,363,602</td>
<td align="right">26.9%</td>
<td align="right">421,334,475</td>
<td align="right">27.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">54,778,777</td>
<td align="right"></td>
<td align="right">54,865,830</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">227,094</td>
<td align="right">0.1%</td>
<td align="right">227,451</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">336,019,468</td>
<td align="right">21.5%</td>
<td align="right">336,528,512</td>
<td align="right">21.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">113,034,445</td>
<td align="right"></td>
<td align="right">112,878,714</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">99,120,543</td>
<td align="right">56.9%</td>
<td align="right">99,130,081</td>
<td align="right">56.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">86,977,019</td>
<td align="right"></td>
<td align="right">86,982,721</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">98,404,212</td>
<td align="right">56.5%</td>
<td align="right">98,406,652</td>
<td align="right">56.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">75,006,556</td>
<td align="right">43.1%</td>
<td align="right">75,007,462</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">75,047,046</td>
<td align="right"></td>
<td align="right">75,047,952</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,978,259</td>
<td align="right"></td>
<td align="right">3,978,259</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">366,114</td>
<td align="right">9.2%</td>
<td align="right">366,114</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">37,632</td>
<td align="right">0.9%</td>
<td align="right">37,632</td>
<td align="right">0.9%</td>
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
<td align="right">4,872</td>
<td align="right">65,289</td>
<td align="right">156,856,510</td>
<td align="right">19,087,999</td>
<td align="right">7,331,976</td>
<td align="right">4,893</td>
<td align="right">65,436</td>
<td align="right">197,647,599</td>
<td align="right">27,589,073</td>
<td align="right">7,317,814</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">168</td>
<td align="right">1.8%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,470</td>
<td align="right">22.8%</td>
<td align="right">9,219</td>
<td align="right">27.4%</td>
<td align="right">527.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">3,696</td>
<td align="right">57.3%</td>
<td align="right">20,916</td>
<td align="right">62.3%</td>
<td align="right">465.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">6,447</td>
<td align="right"></td>
<td align="right">33,600</td>
<td align="right"></td>
<td align="right">421.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">42</td>
<td align="right">0.7%</td>
<td align="right">147</td>
<td align="right">0.4%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">924</td>
<td align="right">14.3%</td>
<td align="right">3,066</td>
<td align="right">9.1%</td>
<td align="right">231.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">850,682,448</td>
<td align="right">3,369.6%</td>
<td align="right">1,059,952,533</td>
<td align="right">4,252.4%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">357</td>
<td align="right">5.5%</td>
<td align="right">399</td>
<td align="right">1.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">25,245,654</td>
<td align="right"></td>
<td align="right">24,925,872</td>
<td align="right"></td>
<td align="right">-1.3%</td>
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
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">315</td>
<td align="right">0.9%</td>
<td align="right">315 / 0 !!</td>
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
<td align="right">1,470</td>
<td align="right"></td>
<td align="right">9,219</td>
<td align="right"></td>
<td align="right">527.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,449</td>
<td align="right">98.6%</td>
<td align="right">8,568</td>
<td align="right">92.9%</td>
<td align="right">491.3%</td>
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
<td align="right">3,100,797</td>
<td align="right">21.7%</td>
<td align="right">19,778,598</td>
<td align="right">21.9%</td>
<td align="right">537.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">14,278,656</td>
<td align="right"></td>
<td align="right">90,316,800</td>
<td align="right"></td>
<td align="right">532.5%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">10,864,539</td>
<td align="right">76.1%</td>
<td align="right">68,604,186</td>
<td align="right">76.0%</td>
<td align="right">531.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">313,320</td>
<td align="right">2.2%</td>
<td align="right">1,934,016</td>
<td align="right">2.1%</td>
<td align="right">517.3%</td>
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
<td align="right">86,016</td>
<td align="right">0.1%</td>
<td align="right">86,016 / 0 !!</td>
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
<td align="left">357</td>
<td align="right">24.6%</td>
<td align="left">819</td>
<td align="right">9.6%</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">693</td>
<td align="right">47.8%</td>
<td align="left">4,557</td>
<td align="right">53.2%</td>
<td align="right">557.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">273</td>
<td align="right">18.8%</td>
<td align="left">2,562</td>
<td align="right">29.9%</td>
<td align="right">838.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">105</td>
<td align="right">7.2%</td>
<td align="left">609</td>
<td align="right">7.1%</td>
<td align="right">480.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">1.4%</td>
<td align="left">21</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 16</td>
<td align="right">147</td>
<td align="right">10.0%</td>
<td align="right">126</td>
<td align="right">1.4%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">378</td>
<td align="right">25.7%</td>
<td align="right">1,596</td>
<td align="right">17.3%</td>
<td align="right">322.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">525</td>
<td align="right">35.7%</td>
<td align="right">4,347</td>
<td align="right">47.2%</td>
<td align="right">728.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">294</td>
<td align="right">20.0%</td>
<td align="right">2,478</td>
<td align="right">26.9%</td>
<td align="right">742.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">105</td>
<td align="right">7.1%</td>
<td align="right">588</td>
<td align="right">6.4%</td>
<td align="right">460.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right"></td>
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
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">252</td>
<td align="right">17.1%</td>
<td align="right">294</td>
<td align="right">3.2%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">672</td>
<td align="right">45.7%</td>
<td align="right">4,389</td>
<td align="right">47.6%</td>
<td align="right">553.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">315</td>
<td align="right">21.4%</td>
<td align="right">2,940</td>
<td align="right">31.9%</td>
<td align="right">833.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">10.0%</td>
<td align="right">840</td>
<td align="right">9.1%</td>
<td align="right">471.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">0.2%</td>
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
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,793</td>
<td align="right">407,069</td>
<td align="right">14,474.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,628</td>
<td align="right">390,448</td>
<td align="right">6,837.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">5,628</td>
<td align="right">309,251</td>
<td align="right">5,394.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,788</td>
<td align="right">237,686</td>
<td align="right">4,864.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,810</td>
<td align="right">462,126</td>
<td align="right">3,507.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">5,229</td>
<td align="right">179,991</td>
<td align="right">3,342.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">5,628</td>
<td align="right">172,040</td>
<td align="right">2,956.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">19,866</td>
<td align="right">417,201</td>
<td align="right">2,000.1%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">19,866</td>
<td align="right">417,201</td>
<td align="right">2,000.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,866</td>
<td align="right">417,201</td>
<td align="right">2,000.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">19,866</td>
<td align="right">417,201</td>
<td align="right">2,000.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">14,238</td>
<td align="right">296,961</td>
<td align="right">1,985.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,405</td>
<td align="right">96,789</td>
<td align="right">1,411.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">5,628</td>
<td align="right">83,538</td>
<td align="right">1,384.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">19,866</td>
<td align="right">286,335</td>
<td align="right">1,341.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,033</td>
<td align="right">170,079</td>
<td align="right">1,313.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">29,316</td>
<td align="right">383,817</td>
<td align="right">1,209.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">29,316</td>
<td align="right">371,931</td>
<td align="right">1,168.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">31,836</td>
<td align="right">311,627</td>
<td align="right">878.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">33,642</td>
<td align="right">327,684</td>
<td align="right">874.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">85,029</td>
<td align="right">818,736</td>
<td align="right">862.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">31,836</td>
<td align="right">296,772</td>
<td align="right">832.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">31,836</td>
<td align="right">252,324</td>
<td align="right">692.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">78,624</td>
<td align="right">590,318</td>
<td align="right">650.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">16,002</td>
<td align="right">111,279</td>
<td align="right">595.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">106,302</td>
<td align="right">737,541</td>
<td align="right">593.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">69,930</td>
<td align="right">438,585</td>
<td align="right">527.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,672</td>
<td align="right">392,288</td>
<td align="right">516.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">20,307</td>
<td align="right">113,127</td>
<td align="right">457.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">31,836</td>
<td align="right">174,888</td>
<td align="right">449.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">383,376</td>
<td align="right">1,885,512</td>
<td align="right">391.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">1,527,036</td>
<td align="right">6,626,173</td>
<td align="right">333.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">171,339</td>
<td align="right">714,792</td>
<td align="right">317.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">168,861</td>
<td align="right">665,847</td>
<td align="right">294.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">10,164</td>
<td align="right">37,611</td>
<td align="right">270.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">449,883</td>
<td align="right">1,580,370</td>
<td align="right">251.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,628,760</td>
<td align="right">5,503,185</td>
<td align="right">237.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">119,175</td>
<td align="right">394,377</td>
<td align="right">230.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">576,576</td>
<td align="right">1,897,980</td>
<td align="right">229.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,174,509</td>
<td align="right">3,784,683</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">252,756</td>
<td align="right">811,251</td>
<td align="right">221.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">383,145</td>
<td align="right">1,226,740</td>
<td align="right">220.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">588,483</td>
<td align="right">1,866,291</td>
<td align="right">217.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">1,193,472</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">368,361</td>
<td align="right">1,140,510</td>
<td align="right">209.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">689,346</td>
<td align="right">2,046,054</td>
<td align="right">196.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">126,378</td>
<td align="right">366,015</td>
<td align="right">189.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">126,378</td>
<td align="right">365,637</td>
<td align="right">189.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">689,136</td>
<td align="right">1,967,485</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">277,704</td>
<td align="right">776,178</td>
<td align="right">179.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">277,704</td>
<td align="right">775,401</td>
<td align="right">179.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">391,608</td>
<td align="right">1,076,961</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,592,889</td>
<td align="right">12,600,820</td>
<td align="right">174.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,101,764</td>
<td align="right">5,748,129</td>
<td align="right">173.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">625,674</td>
<td align="right">1,707,272</td>
<td align="right">172.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">697,620</td>
<td align="right">1,891,184</td>
<td align="right">171.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">3,507</td>
<td align="right">169.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">840,609</td>
<td align="right">2,237,184</td>
<td align="right">166.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">238,014</td>
<td align="right">618,279</td>
<td align="right">159.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,067,304</td>
<td align="right">2,737,812</td>
<td align="right">156.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,044,518</td>
<td align="right">4,974,132</td>
<td align="right">143.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,020,411</td>
<td align="right">2,385,789</td>
<td align="right">133.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">194,481</td>
<td align="right">453,702</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">923,202</td>
<td align="right">2,138,208</td>
<td align="right">131.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,461,557</td>
<td align="right">5,675,782</td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,501,122</td>
<td align="right">3,441,711</td>
<td align="right">129.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">805,770</td>
<td align="right">1,822,083</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,695,540</td>
<td align="right">3,828,578</td>
<td align="right">125.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,853,712</td>
<td align="right">3,850,888</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">2,834,391</td>
<td align="right">5,829,138</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,116,003</td>
<td align="right">2,225,488</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,155,399</td>
<td align="right">8,904</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">829,836</td>
<td align="right">1,591,061</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,076,145</td>
<td align="right">2,035,854</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,305,024</td>
<td align="right">2,402,048</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">729,267</td>
<td align="right">1,338,595</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">61,110</td>
<td align="right">111,195</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">61,110</td>
<td align="right">111,195</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">758,247</td>
<td align="right">1,363,476</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">584,850</td>
<td align="right">1,018,143</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right">200,949</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right">200,949</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,624,055</td>
<td align="right">4,445,187</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,187,445</td>
<td align="right">1,979,460</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">5,628</td>
<td align="right">1,911</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,137,864</td>
<td align="right">1,879,101</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,499,190</td>
<td align="right">2,466,648</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">553,014</td>
<td align="right">855,099</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,238</td>
<td align="right">21,714</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">894,348</td>
<td align="right">428,921</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,424,850</td>
<td align="right">2,104,494</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,608,919</td>
<td align="right">25,428,686</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">138,089,112</td>
<td align="right">175,988,242</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">163,067,688</td>
<td align="right">200,692,342</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">43,496,019</td>
<td align="right">52,633,885</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">21,800,520</td>
<td align="right">26,038,138</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,679,349</td>
<td align="right">2,005,647</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">18,136,419</td>
<td align="right">21,657,441</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">21,800,520</td>
<td align="right">26,020,729</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">20,601,063</td>
<td align="right">23,787,106</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">21,119,763</td>
<td align="right">24,194,539</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">14,898,114</td>
<td align="right">13,492,814</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">16,208,220</td>
<td align="right">17,630,641</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">19,553,688</td>
<td align="right">21,163,618</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">19,553,688</td>
<td align="right">21,163,618</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">19,359,354</td>
<td align="right">20,862,727</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,115,628</td>
<td align="right">20,529,414</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">43,382,073</td>
<td align="right">46,583,313</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">38,259,480</td>
<td align="right">40,686,179</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,578,358</td>
<td align="right">25,991,873</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">19,149,480</td>
<td align="right">19,848,005</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,105,607</td>
<td align="right">2,177,307</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">24,476,907</td>
<td align="right">25,165,519</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,416,981</td>
<td align="right">16,789,803</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">25,245,654</td>
<td align="right">24,925,872</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">24,351,306</td>
<td align="right">24,496,468</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">374,887</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">299,874</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">295,696</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">295,696</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">295,696</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">209,328</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">205,443</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">205,443</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">203,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">180,345</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">178,581</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">176,670</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">166,908</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">146,097</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">132,699</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">86,835</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right"></td>
<td align="right">85,743</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">79,149</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">78,792</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">74,718</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">70,581</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">66,822</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">55,890</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">55,503</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">55,503</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">55,146</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">51,975</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right"></td>
<td align="right">43,617</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">36,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">36,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">32,193</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">28,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right"></td>
<td align="right">18,774</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">16,611</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right"></td>
<td align="right">14,742</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">13,986</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">12,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">7,896</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right"></td>
<td align="right">4,809</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">4,725</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">4,053</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">2,856</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">2,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">2,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">2,436</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">1,785</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">1,449</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">1,365</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">714</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">483</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">378</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">252</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">42</td>
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
<td align="right">357</td>
<td align="right">462</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right"></td>
<td align="right">21</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">21</td>
<td align="right">147</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">21</td>
<td align="right">147</td>
<td align="right">600.0%</td>
</tr>
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
<td align="right">252</td>
<td align="right">252</td>
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
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-07-02
