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
<td align="right">387,626</td>
<td align="right">248,574</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">796,252</td>
<td align="right">518,143</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">806,437</td>
<td align="right">528,515</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">269,364</td>
<td align="right">176,678</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,856,939</td>
<td align="right">1,880,716</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">460,764</td>
<td align="right">304,909</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,094,939</td>
<td align="right">724,710</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,950,076</td>
<td align="right">2,630,701</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,049,661</td>
<td align="right">703,231</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,123,188</td>
<td align="right">752,959</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">997,229</td>
<td align="right">668,604</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">569,413</td>
<td align="right">384,584</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">726,612</td>
<td align="right">491,098</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,079,217</td>
<td align="right">732,972</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,161,009</td>
<td align="right">790,780</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">438,089</td>
<td align="right">299,050</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">292,184</td>
<td align="right">199,475</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">292,507</td>
<td align="right">199,798</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">969,095</td>
<td align="right">669,434</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,506,454</td>
<td align="right">1,049,297</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">469,066</td>
<td align="right">329,988</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">646,856</td>
<td align="right">461,456</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">164,944</td>
<td align="right">118,601</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,030,400</td>
<td align="right">1,464,526</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">167,994</td>
<td align="right">121,689</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,422,240</td>
<td align="right">1,035,211</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">170,838</td>
<td align="right">124,489</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,362,692</td>
<td align="right">3,187,721</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,358,656</td>
<td align="right">5,381,881</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,014,312</td>
<td align="right">5,153,803</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,738,272</td>
<td align="right">7,169,605</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,958,094</td>
<td align="right">3,652,549</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">98,831</td>
<td align="right">73,480</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,562,368</td>
<td align="right">2,651,139</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,116,317</td>
<td align="right">3,827,651</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,692,100</td>
<td align="right">1,274,681</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,164,927</td>
<td align="right">6,963,588</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,769,834</td>
<td align="right">1,346,399</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">300,853</td>
<td align="right">230,277</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,097,594</td>
<td align="right">3,145,051</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,270,347</td>
<td align="right">3,322,835</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,668,097</td>
<td align="right">2,084,390</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,279,654</td>
<td align="right">1,001,360</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">99,824</td>
<td align="right">78,617</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">53,753,513</td>
<td align="right">42,346,474</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,979,829</td>
<td align="right">2,361,741</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,727,953</td>
<td align="right">2,184,534</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,575,649</td>
<td align="right">16,586,794</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,627,159</td>
<td align="right">9,385,619</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,627,788</td>
<td align="right">2,134,587</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,190,232</td>
<td align="right">14,849,894</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,046,697</td>
<td align="right">3,306,684</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,977,204</td>
<td align="right">1,627,358</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,560,295</td>
<td align="right">10,359,074</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,287,162</td>
<td align="right">10,198,374</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">822,472</td>
<td align="right">683,414</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,265,842</td>
<td align="right">1,895,030</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">866,932</td>
<td align="right">727,883</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,095,836</td>
<td align="right">925,412</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">925,944</td>
<td align="right">786,155</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">160,638</td>
<td align="right">136,448</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,995,570</td>
<td align="right">14,450,750</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,165,982</td>
<td align="right">1,850,386</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">181,232</td>
<td align="right">155,972</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,963,885</td>
<td align="right">5,171,980</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">564,408</td>
<td align="right">489,746</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">687,835</td>
<td align="right">616,153</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,579,617</td>
<td align="right">6,791,592</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">65,383</td>
<td align="right">59,512</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">778,211</td>
<td align="right">712,594</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">218,600</td>
<td align="right">200,367</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,438,308</td>
<td align="right">3,174,333</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,913,676</td>
<td align="right">7,328,677</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,047</td>
<td align="right">4,780</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,565,122</td>
<td align="right">1,493,440</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">558,270</td>
<td align="right">540,063</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">371,822</td>
<td align="right">362,660</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,444</td>
<td align="right">13,177</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,667</td>
<td align="right">17,400</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,667</td>
<td align="right">17,400</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,896</td>
<td align="right">4,837</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">347</td>
<td align="right">351</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,234</td>
<td align="right">3,203</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,824</td>
<td align="right">40,553</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">476</td>
<td align="right">478</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,596</td>
<td align="right">102,319</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,072</td>
<td align="right">200,548</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,476</td>
<td align="right">21,470</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,313</td>
<td align="right">97,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,048</td>
<td align="right">34,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,406</td>
<td align="right">46,401</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,134</td>
<td align="right">35,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,370</td>
<td align="right">81,364</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,873</td>
<td align="right">452,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,020</td>
<td align="right">191,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">907,791</td>
<td align="right">907,777</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,684</td>
<td align="right">1,818,678</td>
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
<td align="right">168,813</td>
<td align="right">168,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,813</td>
<td align="right">115,813</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">87,032</td>
<td align="right">87,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,432</td>
<td align="right">86,432</td>
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
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
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
<td align="right">59,119</td>
<td align="right">59,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,611</td>
<td align="right">55,611</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,607</td>
<td align="right">55,607</td>
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
<td align="left">CALL_TUPLE_1</td>
<td align="right">14,867</td>
<td align="right">14,867</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">953</td>
<td align="right">953</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,945,972</td>
<td align="right">71.8%</td>
<td align="right">2,627,174</td>
<td align="right">65.3%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,750</td>
<td align="right">0.5%</td>
<td align="right">25,852</td>
<td align="right">0.6%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,517,431</td>
<td align="right">27.6%</td>
<td align="right">1,365,120</td>
<td align="right">33.9%</td>
<td align="right">-10.0%</td>
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
<td align="right">3,995</td>
<td align="right">85.5%</td>
<td align="right">3,419</td>
<td align="right">85.1%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">677</td>
<td align="right">14.5%</td>
<td align="right">599</td>
<td align="right">14.9%</td>
<td align="right">-11.5%</td>
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
<td align="right">567</td>
<td align="right">14.2%</td>
<td align="right">445</td>
<td align="right">13.0%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,052</td>
<td align="right">26.3%</td>
<td align="right">836</td>
<td align="right">24.5%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,957</td>
<td align="right">49.0%</td>
<td align="right">1,722</td>
<td align="right">50.4%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">296</td>
<td align="right">7.4%</td>
<td align="right">293</td>
<td align="right">8.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">2.7%</td>
<td align="right">109</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">14</td>
<td align="right">0.4%</td>
<td align="right">14</td>
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
<td align="right">476,058</td>
<td align="right">92.1%</td>
<td align="right">383,372</td>
<td align="right">90.4%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,564</td>
<td align="right">7.8%</td>
<td align="right">40,297</td>
<td align="right">9.5%</td>
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
<td align="left">Failure</td>
<td align="right">142</td>
<td align="right">54.6%</td>
<td align="right">138</td>
<td align="right">53.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">45.4%</td>
<td align="right">118</td>
<td align="right">46.1%</td>
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
<td align="right">141</td>
<td align="right">99.3%</td>
<td align="right">137</td>
<td align="right">99.3%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">0.7%</td>
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
<td align="right">18,650,844</td>
<td align="right">100.0%</td>
<td align="right">14,384,115</td>
<td align="right">100.0%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,463</td>
<td align="right">0.0%</td>
<td align="right">1,448</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">3,531</td>
<td align="right">98.8%</td>
<td align="right">3,487</td>
<td align="right">98.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">1.2%</td>
<td align="right">43</td>
<td align="right">1.2%</td>
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
<td align="left">out of versions</td>
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">459,180</td>
<td align="right">11.0%</td>
<td align="right">303,590</td>
<td align="right">8.8%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">43,416</td>
<td align="right">1.0%</td>
<td align="right">34,436</td>
<td align="right">1.0%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,657,220</td>
<td align="right">87.9%</td>
<td align="right">3,100,399</td>
<td align="right">90.1%</td>
<td align="right">-15.2%</td>
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
<td align="right">1,316</td>
<td align="right">55.0%</td>
<td align="right">1,054</td>
<td align="right">53.8%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,078</td>
<td align="right">45.0%</td>
<td align="right">904</td>
<td align="right">46.2%</td>
<td align="right">-16.1%</td>
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
<td align="right">1,068</td>
<td align="right">81.2%</td>
<td align="right">809</td>
<td align="right">76.8%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">107</td>
<td align="right">8.1%</td>
<td align="right">104</td>
<td align="right">9.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">7.3%</td>
<td align="right">96</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">3.3%</td>
<td align="right">44</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,336,616</td>
<td align="right">100.0%</td>
<td align="right">1,012,121</td>
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
<td align="right">6,254,478</td>
<td align="right">98.2%</td>
<td align="right">5,843,259</td>
<td align="right">98.1%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">115,483</td>
<td align="right">1.8%</td>
<td align="right">115,483</td>
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
<td align="right">54</td>
<td align="right">16.4%</td>
<td align="right">54</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">276</td>
<td align="right">83.6%</td>
<td align="right">276</td>
<td align="right">83.6%</td>
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
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="right">5,105,928</td>
<td align="right">13.3%</td>
<td align="right">3,817,691</td>
<td align="right">12.5%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,897,599</td>
<td align="right">85.7%</td>
<td align="right">26,443,962</td>
<td align="right">86.3%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">354,181</td>
<td align="right">0.9%</td>
<td align="right">353,733</td>
<td align="right">1.2%</td>
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
<td align="right">5,631</td>
<td align="right">33.5%</td>
<td align="right">5,287</td>
<td align="right">32.3%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,196</td>
<td align="right">66.5%</td>
<td align="right">11,097</td>
<td align="right">67.7%</td>
<td align="right">-0.9%</td>
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
<td align="right">1,389</td>
<td align="right">24.7%</td>
<td align="right">1,159</td>
<td align="right">21.9%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">820</td>
<td align="right">14.6%</td>
<td align="right">768</td>
<td align="right">14.5%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,419</td>
<td align="right">25.2%</td>
<td align="right">1,403</td>
<td align="right">26.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">683</td>
<td align="right">12.1%</td>
<td align="right">681</td>
<td align="right">12.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">8.2%</td>
<td align="right">460</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.3%</td>
<td align="right">71</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.2%</td>
<td align="right">68</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.8%</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">14,008,310</td>
<td align="right">100.0%</td>
<td align="right">10,492,131</td>
<td align="right">100.0%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">832</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">2,403</td>
<td align="right">100.0%</td>
<td align="right">2,380</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">1,485,521</td>
<td align="right">100.0%</td>
<td align="right">975,626</td>
<td align="right">100.0%</td>
<td align="right">-34.3%</td>
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
<td align="right">3,874,155</td>
<td align="right">94.6%</td>
<td align="right">2,947,158</td>
<td align="right">93.0%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,687</td>
<td align="right">1.9%</td>
<td align="right">79,684</td>
<td align="right">2.5%</td>
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
<td align="right">140,654</td>
<td align="right">3.4%</td>
<td align="right">140,654</td>
<td align="right">4.4%</td>
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
<td align="right">3,620</td>
<td align="right">83.8%</td>
<td align="right">3,617</td>
<td align="right">83.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">699</td>
<td align="right">16.2%</td>
<td align="right">699</td>
<td align="right">16.2%</td>
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
<td align="right">49.2%</td>
<td align="right">344</td>
<td align="right">49.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">29.5%</td>
<td align="right">206</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">139</td>
<td align="right">19.9%</td>
<td align="right">139</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.4%</td>
<td align="right">10</td>
<td align="right">1.4%</td>
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
<td align="right">1,401,913</td>
<td align="right">98.5%</td>
<td align="right">1,077,064</td>
<td align="right">98.0%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,268</td>
<td align="right">1.5%</td>
<td align="right">21,265</td>
<td align="right">1.9%</td>
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
<td align="right">21</td>
<td align="right">10.1%</td>
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">89.9%</td>
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
<td align="right">8,604,473</td>
<td align="right">97.9%</td>
<td align="right">6,055,086</td>
<td align="right">97.5%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180,011</td>
<td align="right">2.0%</td>
<td align="right">154,767</td>
<td align="right">2.5%</td>
<td align="right">-14.0%</td>
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
<td align="right">760</td>
<td align="right">62.2%</td>
<td align="right">749</td>
<td align="right">62.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">461</td>
<td align="right">37.8%</td>
<td align="right">456</td>
<td align="right">37.8%</td>
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
<td align="right">319</td>
<td align="right">42.0%</td>
<td align="right">305</td>
<td align="right">40.7%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">138</td>
<td align="right">18.2%</td>
<td align="right">141</td>
<td align="right">18.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">126</td>
<td align="right">16.6%</td>
<td align="right">126</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">14.6%</td>
<td align="right">111</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">8.6%</td>
<td align="right">65</td>
<td align="right">8.7%</td>
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
<td align="right">2,010,743</td>
<td align="right">100.0%</td>
<td align="right">1,918,042</td>
<td align="right">100.0%</td>
<td align="right">-4.6%</td>
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
<td align="right">9,990,611</td>
<td align="right">3.3%</td>
<td align="right">7,201,082</td>
<td align="right">3.0%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">107,823,952</td>
<td align="right">35.6%</td>
<td align="right">84,744,310</td>
<td align="right">34.9%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">184,496,953</td>
<td align="right">60.9%</td>
<td align="right">150,434,870</td>
<td align="right">61.9%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">569,188</td>
<td align="right">0.2%</td>
<td align="right">555,877</td>
<td align="right">0.2%</td>
<td align="right">-2.3%</td>
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
<td align="right">459,180</td>
<td align="right">4.6%</td>
<td align="right">303,590</td>
<td align="right">4.2%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,945,972</td>
<td align="right">39.6%</td>
<td align="right">2,627,174</td>
<td align="right">36.6%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,105,928</td>
<td align="right">51.2%</td>
<td align="right">3,817,691</td>
<td align="right">53.2%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">180,011</td>
<td align="right">1.8%</td>
<td align="right">154,767</td>
<td align="right">2.2%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,463</td>
<td align="right">0.0%</td>
<td align="right">1,448</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,564</td>
<td align="right">0.4%</td>
<td align="right">40,297</td>
<td align="right">0.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,268</td>
<td align="right">0.2%</td>
<td align="right">21,265</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,687</td>
<td align="right">0.8%</td>
<td align="right">79,684</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,483</td>
<td align="right">1.2%</td>
<td align="right">115,483</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right">13,887</td>
<td align="right">0.2%</td>
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
<td align="right">43,415</td>
<td align="right">7.6%</td>
<td align="right">34,435</td>
<td align="right">6.2%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">29,750</td>
<td align="right">5.2%</td>
<td align="right">25,852</td>
<td align="right">4.7%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">294,630</td>
<td align="right">51.8%</td>
<td align="right">294,184</td>
<td align="right">52.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,491</td>
<td align="right">8.7%</td>
<td align="right">49,489</td>
<td align="right">8.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">24.7%</td>
<td align="right">140,654</td>
<td align="right">25.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.8%</td>
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
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">153</td>
<td align="right">0.0%</td>
<td align="right">153</td>
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
<td align="right">399,731</td>
<td align="right">1.5%</td>
<td align="right">307,001</td>
<td align="right">1.4%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">21,748,430</td>
<td align="right">81.2%</td>
<td align="right">17,298,246</td>
<td align="right">77.5%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">19,189,969</td>
<td align="right">71.7%</td>
<td align="right">15,527,810</td>
<td align="right">69.6%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,156,537</td>
<td align="right">26.7%</td>
<td align="right">6,368,512</td>
<td align="right">28.5%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,156,596</td>
<td align="right">26.7%</td>
<td align="right">6,368,571</td>
<td align="right">28.5%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,583,975</td>
<td align="right">28.3%</td>
<td align="right">6,795,950</td>
<td align="right">30.4%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,583,975</td>
<td align="right">28.3%</td>
<td align="right">6,795,950</td>
<td align="right">30.4%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,682</td>
<td align="right">0.1%</td>
<td align="right">17,415</td>
<td align="right">0.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.6%</td>
<td align="right">427,379</td>
<td align="right">1.9%</td>
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
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.6%</td>
<td align="right">441,509</td>
<td align="right">2.0%</td>
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
<td align="left">Method cache misses</td>
<td align="right">35,424</td>
<td align="right"></td>
<td align="right">54,594</td>
<td align="right"></td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,213,282</td>
<td align="right"></td>
<td align="right">842,482</td>
<td align="right"></td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,455,971</td>
<td align="right"></td>
<td align="right">5,350,006</td>
<td align="right"></td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">60,745,022</td>
<td align="right">15.3%</td>
<td align="right">46,468,174</td>
<td align="right">14.4%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">47,053,576</td>
<td align="right">14.3%</td>
<td align="right">36,201,379</td>
<td align="right">13.5%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">15,274,462</td>
<td align="right">49.3%</td>
<td align="right">12,088,636</td>
<td align="right">47.3%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">15,277,248</td>
<td align="right"></td>
<td align="right">12,091,455</td>
<td align="right"></td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">50,467,720</td>
<td align="right">15.3%</td>
<td align="right">40,443,404</td>
<td align="right">15.1%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">152,551,418</td>
<td align="right">38.5%</td>
<td align="right">122,483,120</td>
<td align="right">37.9%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">119,530,996</td>
<td align="right">36.2%</td>
<td align="right">96,888,754</td>
<td align="right">36.1%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">75,235,753</td>
<td align="right">19.0%</td>
<td align="right">61,555,278</td>
<td align="right">19.1%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,851,197</td>
<td align="right"></td>
<td align="right">8,078,872</td>
<td align="right"></td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">178,962</td>
<td align="right"></td>
<td align="right">209,013</td>
<td align="right"></td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">112,808,288</td>
<td align="right">34.2%</td>
<td align="right">94,686,534</td>
<td align="right">35.3%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,724,962</td>
<td align="right"></td>
<td align="right">14,128,170</td>
<td align="right"></td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,597,211</td>
<td align="right">50.3%</td>
<td align="right">13,324,907</td>
<td align="right">52.2%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,718,516</td>
<td align="right">50.7%</td>
<td align="right">13,446,159</td>
<td align="right">52.7%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">108,085,954</td>
<td align="right">27.3%</td>
<td align="right">92,534,734</td>
<td align="right">28.6%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">143,838</td>
<td align="right"></td>
<td align="right">154,732</td>
<td align="right"></td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,730</td>
<td align="right">0.3%</td>
<td align="right">77,684</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,575</td>
<td align="right">0.1%</td>
<td align="right">43,568</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">640</td>
<td align="right">0.1%</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">30</td>
<td align="right">1.5%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">23</td>
<td align="right">1.2%</td>
<td align="right">17</td>
<td align="right">0.9%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">255</td>
<td align="right">13.1%</td>
<td align="right">193</td>
<td align="right">10.7%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">317,318,262</td>
<td align="right">1,649.3%</td>
<td align="right">274,414,173</td>
<td align="right">1,510.3%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,940</td>
<td align="right"></td>
<td align="right">1,811</td>
<td align="right"></td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">19,239,322</td>
<td align="right"></td>
<td align="right">18,169,299</td>
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
<td align="right">1,639</td>
<td align="right">84.5%</td>
<td align="right">1,559</td>
<td align="right">86.1%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,655</td>
<td align="right">85.3%</td>
<td align="right">1,598</td>
<td align="right">88.2%</td>
<td align="right">-3.4%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">255</td>
<td align="right"></td>
<td align="right">193</td>
<td align="right"></td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">255</td>
<td align="right">100.0%</td>
<td align="right">193</td>
<td align="right">100.0%</td>
<td align="right">-24.3%</td>
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
<td align="right">52</td>
<td align="right">20.4%</td>
<td align="right">42</td>
<td align="right">21.8%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">11</td>
<td align="right">4.3%</td>
<td align="right">9</td>
<td align="right">4.7%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50</td>
<td align="right">19.6%</td>
<td align="right">40</td>
<td align="right">20.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">44</td>
<td align="right">17.3%</td>
<td align="right">40</td>
<td align="right">20.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">50</td>
<td align="right">19.6%</td>
<td align="right">25</td>
<td align="right">13.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">16</td>
<td align="right">6.3%</td>
<td align="right">12</td>
<td align="right">6.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">32</td>
<td align="right">12.5%</td>
<td align="right">25</td>
<td align="right">13.0%</td>
<td align="right">-21.9%</td>
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
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">61</td>
<td align="right">23.9%</td>
<td align="right">49</td>
<td align="right">25.4%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">8.6%</td>
<td align="right">22</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">72</td>
<td align="right">28.2%</td>
<td align="right">58</td>
<td align="right">30.1%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">8.6%</td>
<td align="right">13</td>
<td align="right">6.7%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">45</td>
<td align="right">17.6%</td>
<td align="right">25</td>
<td align="right">13.0%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">32</td>
<td align="right">12.5%</td>
<td align="right">25</td>
<td align="right">13.0%</td>
<td align="right">-21.9%</td>
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
<td align="left">_COMPARE_OP_INT</td>
<td align="right">490,633</td>
<td align="right">286,765</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">833,666</td>
<td align="right">489,463</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">281,822</td>
<td align="right">166,986</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">281,835</td>
<td align="right">166,997</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">281,835</td>
<td align="right">166,997</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">340,534</td>
<td align="right">202,233</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">290,605</td>
<td align="right">173,359</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">39,184</td>
<td align="right">23,434</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">177,854</td>
<td align="right">106,375</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">177,854</td>
<td align="right">106,375</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">161,531</td>
<td align="right">97,160</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,168,548</td>
<td align="right">707,219</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,150,401</td>
<td align="right">702,625</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,571,710</td>
<td align="right">960,387</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">862,647</td>
<td align="right">528,495</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,278,200</td>
<td align="right">787,723</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">405,966</td>
<td align="right">250,551</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">686,370</td>
<td align="right">423,852</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">122,259</td>
<td align="right">75,704</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">366,782</td>
<td align="right">227,116</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">73,886</td>
<td align="right">45,764</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">73,886</td>
<td align="right">45,764</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,093,138</td>
<td align="right">678,685</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">481,838</td>
<td align="right">300,161</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">237,315</td>
<td align="right">148,749</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">57,493</td>
<td align="right">36,496</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">57,538</td>
<td align="right">36,536</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,045,053</td>
<td align="right">2,014,712</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,361,848</td>
<td align="right">1,594,266</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,361,848</td>
<td align="right">1,594,266</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,124,533</td>
<td align="right">1,445,517</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,734,561</td>
<td align="right">2,589,384</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,904,005</td>
<td align="right">2,714,922</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,562,913</td>
<td align="right">2,501,609</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,638,875</td>
<td align="right">1,153,460</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,029,583</td>
<td align="right">4,281,455</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,085,957</td>
<td align="right">2,195,282</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,611,309</td>
<td align="right">1,149,412</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,679,991</td>
<td align="right">1,944,731</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,245,085</td>
<td align="right">907,871</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,247,046</td>
<td align="right">918,655</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">44,168</td>
<td align="right">33,156</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">133,287</td>
<td align="right">100,261</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,048,018</td>
<td align="right">788,656</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,003,903</td>
<td align="right">755,940</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,201,224</td>
<td align="right">1,665,563</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">55</td>
<td align="right">68</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,736,968</td>
<td align="right">1,359,334</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,703,350</td>
<td align="right">2,132,494</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,299,981</td>
<td align="right">6,629,908</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,640,109</td>
<td align="right">1,310,420</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">816,251</td>
<td align="right">652,432</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">815,168</td>
<td align="right">654,860</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,050,435</td>
<td align="right">5,686,748</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">752,343</td>
<td align="right">614,039</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">19,750,866</td>
<td align="right">16,997,492</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">8,301,271</td>
<td align="right">7,156,094</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">27,654,556</td>
<td align="right">23,911,420</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,499,870</td>
<td align="right">2,171,401</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">5,912,955</td>
<td align="right">5,171,706</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">5,912,955</td>
<td align="right">5,171,706</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,179,863</td>
<td align="right">1,034,495</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,397,082</td>
<td align="right">7,377,746</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">597,510</td>
<td align="right">527,377</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,170,647</td>
<td align="right">1,035,508</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,081,115</td>
<td align="right">6,391,683</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,065,746</td>
<td align="right">5,479,407</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,065,746</td>
<td align="right">5,479,407</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,103,369</td>
<td align="right">1,902,785</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,069,962</td>
<td align="right">974,271</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">526,528</td>
<td align="right">479,955</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">529,764</td>
<td align="right">483,191</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,066,808</td>
<td align="right">975,678</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,027,786</td>
<td align="right">1,874,586</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,526,913</td>
<td align="right">2,337,176</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">504,433</td>
<td align="right">467,670</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">504,433</td>
<td align="right">467,670</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,475,087</td>
<td align="right">2,296,346</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,475,087</td>
<td align="right">2,296,346</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">13,983,049</td>
<td align="right">13,027,849</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">995,194</td>
<td align="right">927,625</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">17,332,251</td>
<td align="right">16,187,294</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">7,868,556</td>
<td align="right">7,395,295</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">485,722</td>
<td align="right">457,592</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">485,722</td>
<td align="right">457,592</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">19,765,850</td>
<td align="right">18,649,254</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">19,239,322</td>
<td align="right">18,169,299</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,390,230</td>
<td align="right">1,323,088</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">465,249</td>
<td align="right">444,235</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">469,368</td>
<td align="right">448,354</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">469,260</td>
<td align="right">448,272</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,675,413</td>
<td align="right">4,471,376</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,018,946</td>
<td align="right">4,830,203</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">442,571</td>
<td align="right">426,803</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">442,571</td>
<td align="right">426,803</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,256,218</td>
<td align="right">5,141,382</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,280,551</td>
<td align="right">1,259,554</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,525,399</td>
<td align="right">5,445,905</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,488,015</td>
<td align="right">2,467,018</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,387</td>
<td align="right">403,369</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,387</td>
<td align="right">403,369</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,387</td>
<td align="right">403,369</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,566,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">824,639</td>
<td align="right">824,639</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
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
Stats gathered on: 2024-12-13
