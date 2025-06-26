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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">1,270</td>
<td align="right">2,016.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">187,761</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,150</td>
<td align="right">87,150</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">200</td>
<td align="right">4,200</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">2,793</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">2,667</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">2,142</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">1,932</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">21</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">21</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">996</td>
<td align="right">20,789</td>
<td align="right">1,987.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">184,485</td>
<td align="right">1,902.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">6,993</td>
<td align="right">1,674.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,965</td>
<td align="right">50,216</td>
<td align="right">1,593.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,109</td>
<td align="right">89,524</td>
<td align="right">1,159.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,798</td>
<td align="right">273,229</td>
<td align="right">1,048.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,067</td>
<td align="right">191,758</td>
<td align="right">961.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,443</td>
<td align="right">13,460</td>
<td align="right">832.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,688</td>
<td align="right">164,993</td>
<td align="right">697.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,037</td>
<td align="right">90,471</td>
<td align="right">651.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,550</td>
<td align="right">25,599</td>
<td align="right">361.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,038</td>
<td align="right">40,142</td>
<td align="right">344.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">2,103</td>
<td align="right">255.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">2,940</td>
<td align="right">178.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">79,551</td>
<td align="right">214,776</td>
<td align="right">170.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">494,972</td>
<td align="right">1,233,917</td>
<td align="right">149.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,349</td>
<td align="right">386,574</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">5,466</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">202,050</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">41,233</td>
<td align="right">58,664</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">378,841</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,329,745</td>
<td align="right">4,553,867</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,009</td>
<td align="right">120,324</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,534</td>
<td align="right">241,236</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,532</td>
<td align="right">241,194</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,570</td>
<td align="right">2,987,337</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,318</td>
<td align="right">7,867,332</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,035,197</td>
<td align="right">5,228,819</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">341,720</td>
<td align="right">440,463</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,678</td>
<td align="right">5,096,141</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,996</td>
<td align="right">945,883</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,773</td>
<td align="right">1,737,386</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,537</td>
<td align="right">743,837</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">388,827</td>
<td align="right">464,739</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">360</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,220,468</td>
<td align="right">1,455,456</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,132</td>
<td align="right">98,296</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">427,533</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,895</td>
<td align="right">444,324</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,312</td>
<td align="right">848,593</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,376</td>
<td align="right">743,360</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,376</td>
<td align="right">743,360</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,376</td>
<td align="right">743,360</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,512</td>
<td align="right">736,791</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,496</td>
<td align="right">736,447</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,559</td>
<td align="right">2,257,519</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,314</td>
<td align="right">1,477,445</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,090</td>
<td align="right">2,021,185</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,835</td>
<td align="right">7,361,192</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,857</td>
<td align="right">7,261,242</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,978,534</td>
<td align="right">9,882,023</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">231</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,282</td>
<td align="right">6,276,650</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,709</td>
<td align="right">4,886,147</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,920,900</td>
<td align="right">11,855,532</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,831,328</td>
<td align="right">7,400,224</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,873,705</td>
<td align="right">11,740,387</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,350</td>
<td align="right">7,254,689</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">15,684</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,052</td>
<td align="right">184,070</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,824</td>
<td align="right">493,958</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,355</td>
<td align="right">2,763,059</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,438,272</td>
<td align="right">10,050,592</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,644</td>
<td align="right">2,136,320</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,709,286</td>
<td align="right">13,400,650</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,147,026</td>
<td align="right">34,858,865</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,030,050</td>
<td align="right">1,082,497</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,159</td>
<td align="right">1,080,679</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,601,799</td>
<td align="right">187,317,812</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,992,015</td>
<td align="right">10,469,618</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">15,009,202</td>
<td align="right">15,707,120</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">149,428,538</td>
<td align="right">156,324,068</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,610,040</td>
<td align="right">12,117,879</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,531</td>
<td align="right">1,825,632</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">46,445,089</td>
<td align="right">48,244,959</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,383,294</td>
<td align="right">18,029,046</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,002,664</td>
<td align="right">11,411,007</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,115,136</td>
<td align="right">54,046,132</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,299,427</td>
<td align="right">51,124,102</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60,584,325</td>
<td align="right">62,814,070</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,231,595</td>
<td align="right">27,193,025</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,485,034</td>
<td align="right">50,215,542</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,369,298</td>
<td align="right">24,200,562</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,691</td>
<td align="right">770,532</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,516</td>
<td align="right">7,796,126</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,736,994</td>
<td align="right">81,367,416</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,832,568</td>
<td align="right">187,832,493</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,178,208</td>
<td align="right">205,587,706</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,091,651</td>
<td align="right">11,437,299</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,994,843</td>
<td align="right">3,087,664</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,833,248</td>
<td align="right">54,468,342</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,697,677</td>
<td align="right">22,342,996</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,100,073</td>
<td align="right">116,459,285</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,200</td>
<td align="right">4,598,587</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">679,047,670</td>
<td align="right">698,573,885</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,681,141</td>
<td align="right">18,179,941</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,733,003</td>
<td align="right">47,012,523</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,915,513</td>
<td align="right">8,129,495</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,387</td>
<td align="right">17,917,843</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,079,219</td>
<td align="right">8,294,740</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,816</td>
<td align="right">10,025,728</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">232,557,229</td>
<td align="right">238,451,416</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">149,944,406</td>
<td align="right">153,637,299</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,253,480</td>
<td align="right">54,554,557</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,951,442</td>
<td align="right">82,905,459</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,440,571</td>
<td align="right">36,278,762</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,768</td>
<td align="right">22,500,423</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,735,130</td>
<td align="right">25,307,594</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,100,875</td>
<td align="right">40,990,664</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">135,220,711</td>
<td align="right">138,211,812</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">192,472,089</td>
<td align="right">196,607,396</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,971,805</td>
<td align="right">6,096,686</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,630,485</td>
<td align="right">37,378,132</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,621,556</td>
<td align="right">36,333,198</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,130,701</td>
<td align="right">23,586,264</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,158,054</td>
<td align="right">27,692,407</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,616,684</td>
<td align="right">2,668,053</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">273,566,749</td>
<td align="right">278,900,836</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">45,118,069</td>
<td align="right">45,966,233</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,319</td>
<td align="right">6,913,792</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">44,466,576</td>
<td align="right">45,276,769</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,985,877</td>
<td align="right">16,258,382</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,163,868</td>
<td align="right">13,385,702</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,653</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">47,033,888</td>
<td align="right">47,751,872</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,950,879</td>
<td align="right">73,036,476</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,427,672</td>
<td align="right">12,593,940</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,945,639</td>
<td align="right">17,171,378</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,401</td>
<td align="right">143,116</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,555</td>
<td align="right">22,225,256</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,612,955</td>
<td align="right">4,664,417</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,938,573</td>
<td align="right">18,134,523</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,671</td>
<td align="right">932,374</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,539</td>
<td align="right">431,891</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,384,545</td>
<td align="right">73,072,400</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,800,140</td>
<td align="right">71,457,571</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,444,609</td>
<td align="right">30,716,987</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,574,000</td>
<td align="right">76,214,154</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,826,843</td>
<td align="right">45,188,894</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,630,342</td>
<td align="right">18,777,666</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,028,007</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,577</td>
<td align="right">166,808</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,742,007</td>
<td align="right">82,344,091</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,314,187</td>
<td align="right">18,443,332</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,483</td>
<td align="right">26,905,990</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,077,112</td>
<td align="right">18,968,935</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,741,142</td>
<td align="right">15,654,885</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,709</td>
<td align="right">4,203,754</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,017,016</td>
<td align="right">15,938,334</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,422,076</td>
<td align="right">23,309,758</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,537</td>
<td align="right">1,249,621</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,412,203</td>
<td align="right">46,228,640</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,082,233</td>
<td align="right">19,139,655</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,232,577</td>
<td align="right">82,008,930</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,287,751</td>
<td align="right">1,291,034</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,742,529</td>
<td align="right">83,569,375</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,601,775</td>
<td align="right">18,566,065</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,199,392</td>
<td align="right">2,195,562</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,242,033</td>
<td align="right">6,245,951</td>
<td align="right">0.1%</td>
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
<td align="right">396,470</td>
<td align="right">0.3%</td>
<td align="right">435,791</td>
<td align="right">0.4%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">70,867,616</td>
<td align="right">60.6%</td>
<td align="right">74,053,593</td>
<td align="right">60.9%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,701,810</td>
<td align="right">39.1%</td>
<td align="right">46,929,449</td>
<td align="right">38.6%</td>
<td align="right">2.7%</td>
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
<td align="right">9,560</td>
<td align="right">24.7%</td>
<td align="right">24,355</td>
<td align="right">26.8%</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">29,068</td>
<td align="right">75.3%</td>
<td align="right">66,674</td>
<td align="right">73.2%</td>
<td align="right">129.4%</td>
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
<td align="left">subscr array</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">3,822</td>
<td align="right">5.7%</td>
<td align="right">805.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.2%</td>
<td align="right">1,269</td>
<td align="right">1.9%</td>
<td align="right">249.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">625</td>
<td align="right">2.2%</td>
<td align="right">2,067</td>
<td align="right">3.1%</td>
<td align="right">230.7%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">738</td>
<td align="right">2.5%</td>
<td align="right">2,415</td>
<td align="right">3.6%</td>
<td align="right">227.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,901</td>
<td align="right">10.0%</td>
<td align="right">9,431</td>
<td align="right">14.1%</td>
<td align="right">225.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,209</td>
<td align="right">4.2%</td>
<td align="right">3,741</td>
<td align="right">5.6%</td>
<td align="right">209.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">705</td>
<td align="right">2.4%</td>
<td align="right">2,152</td>
<td align="right">3.2%</td>
<td align="right">205.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">2,968</td>
<td align="right">4.5%</td>
<td align="right">202.2%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,764</td>
<td align="right">6.1%</td>
<td align="right">4,868</td>
<td align="right">7.3%</td>
<td align="right">176.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,353</td>
<td align="right">8.1%</td>
<td align="right">6,159</td>
<td align="right">9.2%</td>
<td align="right">161.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">204</td>
<td align="right">0.3%</td>
<td align="right">124.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">3.7%</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">116.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">566</td>
<td align="right">1.9%</td>
<td align="right">1,178</td>
<td align="right">1.8%</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">6,261</td>
<td align="right">9.4%</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,003</td>
<td align="right">3.5%</td>
<td align="right">1,924</td>
<td align="right">2.9%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">294</td>
<td align="right">0.4%</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,561</td>
<td align="right">15.7%</td>
<td align="right">7,960</td>
<td align="right">11.9%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">0.7%</td>
<td align="right">358</td>
<td align="right">0.5%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,884</td>
<td align="right">13.4%</td>
<td align="right">4,047</td>
<td align="right">6.1%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">7</td>
<td align="right">0.0%</td>
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
<td align="right">12,037</td>
<td align="right">100.0%</td>
<td align="right">90,471</td>
<td align="right">100.0%</td>
<td align="right">651.6%</td>
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
<td align="right">276,364,092</td>
<td align="right">88.3%</td>
<td align="right">285,988,796</td>
<td align="right">88.6%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,819,364</td>
<td align="right">11.4%</td>
<td align="right">36,169,944</td>
<td align="right">11.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">36,499,509</td>
<td align="right">11.7%</td>
<td align="right">36,685,825</td>
<td align="right">11.4%</td>
<td align="right">0.5%</td>
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
<td align="right">703,943</td>
<td align="right">100.0%</td>
<td align="right">789,110</td>
<td align="right">100.0%</td>
<td align="right">12.1%</td>
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
<td align="right">11,360</td>
<td align="right">69.1%</td>
<td align="right">256.9%</td>
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
<td align="right">2,988</td>
<td align="right">18.2%</td>
<td align="right">6.5%</td>
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
<td align="right">1,065</td>
<td align="right">100.0%</td>
<td align="right">5,088</td>
<td align="right">100.0%</td>
<td align="right">377.7%</td>
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
<td align="right">412,636</td>
<td align="right">0.5%</td>
<td align="right">448,830</td>
<td align="right">0.5%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,036,678</td>
<td align="right">62.3%</td>
<td align="right">52,829,257</td>
<td align="right">62.9%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,405,903</td>
<td align="right">37.1%</td>
<td align="right">30,643,037</td>
<td align="right">36.5%</td>
<td align="right">0.8%</td>
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
<td align="right">8,890</td>
<td align="right">19.1%</td>
<td align="right">18,219</td>
<td align="right">22.1%</td>
<td align="right">104.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,545</td>
<td align="right">80.9%</td>
<td align="right">64,040</td>
<td align="right">77.9%</td>
<td align="right">70.6%</td>
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
<td align="right">3,155</td>
<td align="right">8.4%</td>
<td align="right">10,000</td>
<td align="right">15.6%</td>
<td align="right">217.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,254</td>
<td align="right">11.3%</td>
<td align="right">12,102</td>
<td align="right">18.9%</td>
<td align="right">184.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">231</td>
<td align="right">0.4%</td>
<td align="right">153.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">139.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">315</td>
<td align="right">0.5%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,474</td>
<td align="right">17.2%</td>
<td align="right">14,405</td>
<td align="right">22.5%</td>
<td align="right">122.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">291</td>
<td align="right">0.5%</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">63</td>
<td align="right">0.1%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,455</td>
<td align="right">3.9%</td>
<td align="right">1,787</td>
<td align="right">2.8%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,204</td>
<td align="right">37.8%</td>
<td align="right">16,131</td>
<td align="right">25.2%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">19.9%</td>
<td align="right">8,442</td>
<td align="right">13.2%</td>
<td align="right">12.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">924</td>
<td align="right">0.0%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,376,186</td>
<td align="right">42.5%</td>
<td align="right">18,013,437</td>
<td align="right">43.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,500,607</td>
<td align="right">57.5%</td>
<td align="right">23,523,610</td>
<td align="right">56.6%</td>
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
<td align="left">Success</td>
<td align="right">125</td>
<td align="right">1.8%</td>
<td align="right">1,365</td>
<td align="right">8.7%</td>
<td align="right">992.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,983</td>
<td align="right">98.2%</td>
<td align="right">14,244</td>
<td align="right">91.3%</td>
<td align="right">104.0%</td>
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
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">1,197</td>
<td align="right">8.4%</td>
<td align="right">300.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,469</td>
<td align="right">21.0%</td>
<td align="right">5,527</td>
<td align="right">38.8%</td>
<td align="right">276.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">2.6%</td>
<td align="right">357</td>
<td align="right">2.5%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,033</td>
<td align="right">72.1%</td>
<td align="right">7,163</td>
<td align="right">50.3%</td>
<td align="right">42.3%</td>
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
<td align="right">102,441,255</td>
<td align="right">55.2%</td>
<td align="right">105,703,750</td>
<td align="right">55.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,600</td>
<td align="right">0.7%</td>
<td align="right">1,225,877</td>
<td align="right">0.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,680,001</td>
<td align="right">44.0%</td>
<td align="right">82,245,184</td>
<td align="right">43.5%</td>
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
<td align="left">Success</td>
<td align="right">24,531</td>
<td align="right">28.6%</td>
<td align="right">37,127</td>
<td align="right">30.5%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,212</td>
<td align="right">71.4%</td>
<td align="right">84,791</td>
<td align="right">69.5%</td>
<td align="right">38.5%</td>
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
<td align="right">64</td>
<td align="right">0.1%</td>
<td align="right">1,344</td>
<td align="right">1.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">479.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">2,773</td>
<td align="right">3.3%</td>
<td align="right">397.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">1,618</td>
<td align="right">1.9%</td>
<td align="right">323.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">903</td>
<td align="right">1.1%</td>
<td align="right">271.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">194</td>
<td align="right">0.3%</td>
<td align="right">714</td>
<td align="right">0.8%</td>
<td align="right">268.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.1%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,359</td>
<td align="right">2.2%</td>
<td align="right">4,306</td>
<td align="right">5.1%</td>
<td align="right">216.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.2%</td>
<td align="right">1,828</td>
<td align="right">2.2%</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,200</td>
<td align="right">6.9%</td>
<td align="right">6,637</td>
<td align="right">7.8%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">47,042</td>
<td align="right">76.9%</td>
<td align="right">56,931</td>
<td align="right">67.1%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,359</td>
<td align="right">10.4%</td>
<td align="right">7,485</td>
<td align="right">8.8%</td>
<td align="right">17.7%</td>
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
<td align="left">string</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
<td align="right">4,119</td>
<td align="right">4,119 / 0 !!</td>
<td align="right">829.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">157,971</td>
<td align="right">157,971 / 0 !!</td>
<td align="right">166,060</td>
<td align="right">166,060 / 0 !!</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,488</td>
<td align="right">70,488 / 0 !!</td>
<td align="right">72,803</td>
<td align="right">72,803 / 0 !!</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,716,222</td>
<td align="right">8,716,222 / 0 !!</td>
<td align="right">8,946,720</td>
<td align="right">8,946,720 / 0 !!</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,171,643</td>
<td align="right">7,171,643 / 0 !!</td>
<td align="right">7,357,731</td>
<td align="right">7,357,731 / 0 !!</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">6,174</td>
<td align="right">6,174 / 0 !!</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,236,550</td>
<td align="right">12,236,550 / 0 !!</td>
<td align="right">12,462,094</td>
<td align="right">12,462,094 / 0 !!</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,619</td>
<td align="right">9,440,619 / 0 !!</td>
<td align="right">9,563,506</td>
<td align="right">9,563,506 / 0 !!</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,233,924</td>
<td align="right">9,233,924 / 0 !!</td>
<td align="right">9,172,665</td>
<td align="right">9,172,665 / 0 !!</td>
<td align="right">-0.7%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">223,160,442</td>
<td align="right">64.3%</td>
<td align="right">228,943,373</td>
<td align="right">64.7%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">70,737,224</td>
<td align="right">20.4%</td>
<td align="right">71,231,132</td>
<td align="right">20.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,244,512</td>
<td align="right">15.3%</td>
<td align="right">53,446,448</td>
<td align="right">15.1%</td>
<td align="right">0.4%</td>
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
<td align="right">47,748</td>
<td align="right">4.5%</td>
<td align="right">127,546</td>
<td align="right">10.4%</td>
<td align="right">167.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,015,399</td>
<td align="right">95.5%</td>
<td align="right">1,095,112</td>
<td align="right">89.6%</td>
<td align="right">7.9%</td>
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
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">588</td>
<td align="right">0.5%</td>
<td align="right">297.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,067</td>
<td align="right">8.5%</td>
<td align="right">12,359</td>
<td align="right">9.7%</td>
<td align="right">203.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,099</td>
<td align="right">6.5%</td>
<td align="right">8,886</td>
<td align="right">7.0%</td>
<td align="right">186.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,868</td>
<td align="right">45.8%</td>
<td align="right">61,744</td>
<td align="right">48.4%</td>
<td align="right">182.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,741</td>
<td align="right">5.7%</td>
<td align="right">7,570</td>
<td align="right">5.9%</td>
<td align="right">176.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,353</td>
<td align="right">9.1%</td>
<td align="right">10,736</td>
<td align="right">8.4%</td>
<td align="right">146.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">106</td>
<td align="right">0.1%</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">566</td>
<td align="right">1.2%</td>
<td align="right">1,218</td>
<td align="right">1.0%</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,093</td>
<td align="right">14.9%</td>
<td align="right">15,150</td>
<td align="right">11.9%</td>
<td align="right">113.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,684</td>
<td align="right">5.6%</td>
<td align="right">4,706</td>
<td align="right">3.7%</td>
<td align="right">75.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,535</td>
<td align="right">0.0%</td>
<td align="right">95,058</td>
<td align="right">0.0%</td>
<td align="right">1,996.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,299</td>
<td align="right">0.0%</td>
<td align="right">21,399</td>
<td align="right">0.0%</td>
<td align="right">1,547.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">291,700,573</td>
<td align="right">100.0%</td>
<td align="right">303,755,698</td>
<td align="right">99.9%</td>
<td align="right">4.1%</td>
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
<td align="right">96,910</td>
<td align="right">100.0%</td>
<td align="right">613.5%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">2,033.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,985</td>
<td align="right">100.0%</td>
<td align="right">2,409,819</td>
<td align="right">99.9%</td>
<td align="right">6.3%</td>
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
<td align="right">630</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
<td align="right">27,421</td>
<td align="right">2.2%</td>
<td align="right">86.4%</td>
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
<td align="right">375,973</td>
<td align="right">30.6%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">731,601</td>
<td align="right">72.0%</td>
<td align="right">821,172</td>
<td align="right">66.9%</td>
<td align="right">12.2%</td>
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
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">2,805</td>
<td align="right">83.1%</td>
<td align="right">153.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">569</td>
<td align="right">16.9%</td>
<td align="right">107.7%</td>
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
<td align="right">2,805</td>
<td align="right">100.0%</td>
<td align="right">153.2%</td>
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
<td align="right">174,041</td>
<td align="right">1.9%</td>
<td align="right">377,545</td>
<td align="right">3.5%</td>
<td align="right">116.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,327,652</td>
<td align="right">80.7%</td>
<td align="right">8,525,905</td>
<td align="right">79.4%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,576,753</td>
<td align="right">17.4%</td>
<td align="right">1,822,624</td>
<td align="right">17.0%</td>
<td align="right">15.6%</td>
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
<td align="right">972</td>
<td align="right">3.1%</td>
<td align="right">3,653</td>
<td align="right">8.4%</td>
<td align="right">275.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,007</td>
<td align="right">96.9%</td>
<td align="right">39,685</td>
<td align="right">91.6%</td>
<td align="right">32.3%</td>
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
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">1.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">296</td>
<td align="right">30.5%</td>
<td align="right">1,406</td>
<td align="right">38.5%</td>
<td align="right">375.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">462</td>
<td align="right">12.6%</td>
<td align="right">352.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">1,953</td>
<td align="right">53.5%</td>
<td align="right">277.0%</td>
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
<td align="right">2,103</td>
<td align="right">100.0%</td>
<td align="right">255.8%</td>
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
<td align="right">2,583,236</td>
<td align="right">12.7%</td>
<td align="right">2,756,687</td>
<td align="right">13.2%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,408</td>
<td align="right">87.3%</td>
<td align="right">18,084,014</td>
<td align="right">86.7%</td>
<td align="right">1.9%</td>
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
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">2,862</td>
<td align="right">44.9%</td>
<td align="right">396.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,543</td>
<td align="right">72.8%</td>
<td align="right">3,510</td>
<td align="right">55.1%</td>
<td align="right">127.5%</td>
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
<td align="right">3,510</td>
<td align="right">100.0%</td>
<td align="right">127.5%</td>
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
<td align="right">623,465</td>
<td align="right">0.3%</td>
<td align="right">668,596</td>
<td align="right">0.4%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,481,194</td>
<td align="right">94.2%</td>
<td align="right">173,524,946</td>
<td align="right">94.2%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,755,773</td>
<td align="right">5.4%</td>
<td align="right">9,941,259</td>
<td align="right">5.4%</td>
<td align="right">1.9%</td>
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
<td align="right">18,964</td>
<td align="right">57.0%</td>
<td align="right">68,734</td>
<td align="right">71.7%</td>
<td align="right">262.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,286</td>
<td align="right">43.0%</td>
<td align="right">27,195</td>
<td align="right">28.3%</td>
<td align="right">90.4%</td>
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
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">3,339</td>
<td align="right">12.3%</td>
<td align="right">278.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">723</td>
<td align="right">5.1%</td>
<td align="right">2,352</td>
<td align="right">8.6%</td>
<td align="right">225.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,263</td>
<td align="right">8.8%</td>
<td align="right">3,363</td>
<td align="right">12.4%</td>
<td align="right">166.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">721</td>
<td align="right">5.0%</td>
<td align="right">1,394</td>
<td align="right">5.1%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,997</td>
<td align="right">56.0%</td>
<td align="right">13,548</td>
<td align="right">49.8%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,613</td>
<td align="right">18.3%</td>
<td align="right">3,073</td>
<td align="right">11.3%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
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
<td align="right">6,348</td>
<td align="right">0.0%</td>
<td align="right">27,413</td>
<td align="right">0.0%</td>
<td align="right">331.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,661,729</td>
<td align="right">100.0%</td>
<td align="right">83,443,080</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">2,391</td>
<td align="right">88.9%</td>
<td align="right">11,975</td>
<td align="right">94.1%</td>
<td align="right">400.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">299</td>
<td align="right">11.1%</td>
<td align="right">754</td>
<td align="right">5.9%</td>
<td align="right">152.2%</td>
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
<td align="right">256</td>
<td align="right">85.6%</td>
<td align="right">691</td>
<td align="right">91.6%</td>
<td align="right">169.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.4%</td>
<td align="right">63</td>
<td align="right">8.4%</td>
<td align="right">46.5%</td>
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
<td align="right">1,642,471,176</td>
<td align="right">34.2%</td>
<td align="right">1,694,208,994</td>
<td align="right">34.4%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,756,660,654</td>
<td align="right">57.4%</td>
<td align="right">2,831,638,278</td>
<td align="right">57.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">306,010,591</td>
<td align="right">6.4%</td>
<td align="right">311,478,725</td>
<td align="right">6.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">94,035,780</td>
<td align="right">2.0%</td>
<td align="right">94,786,723</td>
<td align="right">1.9%</td>
<td align="right">0.8%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">174,041</td>
<td align="right">0.1%</td>
<td align="right">377,545</td>
<td align="right">0.1%</td>
<td align="right">116.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
<td align="right">375,973</td>
<td align="right">0.1%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,236</td>
<td align="right">0.9%</td>
<td align="right">2,756,687</td>
<td align="right">0.9%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,376,186</td>
<td align="right">5.9%</td>
<td align="right">18,013,437</td>
<td align="right">6.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,701,810</td>
<td align="right">15.5%</td>
<td align="right">46,929,449</td>
<td align="right">15.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,773</td>
<td align="right">3.3%</td>
<td align="right">9,941,259</td>
<td align="right">3.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,819,364</td>
<td align="right">12.2%</td>
<td align="right">36,169,944</td>
<td align="right">12.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,405,903</td>
<td align="right">10.3%</td>
<td align="right">30,643,037</td>
<td align="right">10.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,737,224</td>
<td align="right">24.0%</td>
<td align="right">71,231,132</td>
<td align="right">23.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,680,001</td>
<td align="right">27.7%</td>
<td align="right">82,245,184</td>
<td align="right">27.5%</td>
<td align="right">0.7%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,575,974</td>
<td align="right">1.7%</td>
<td align="right">1,821,838</td>
<td align="right">1.9%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,204,185</td>
<td align="right">3.4%</td>
<td align="right">3,288,841</td>
<td align="right">3.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,702,810</td>
<td align="right">12.4%</td>
<td align="right">11,908,825</td>
<td align="right">12.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,330,381</td>
<td align="right">12.0%</td>
<td align="right">11,167,014</td>
<td align="right">11.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,566</td>
<td align="right">5.4%</td>
<td align="right">5,167,179</td>
<td align="right">5.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,289,672</td>
<td align="right">14.1%</td>
<td align="right">13,379,071</td>
<td align="right">14.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,150,788</td>
<td align="right">6.5%</td>
<td align="right">6,179,361</td>
<td align="right">6.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,022,244</td>
<td align="right">30.9%</td>
<td align="right">28,957,854</td>
<td align="right">30.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,479</td>
<td align="right">7.8%</td>
<td align="right">7,304,074</td>
<td align="right">7.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,582</td>
<td align="right">2.2%</td>
<td align="right">2,105,489</td>
<td align="right">2.2%</td>
<td align="right">0.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">416</td>
<td align="right">0.0%</td>
<td align="right">8,736</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">624.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,946</td>
<td align="right">1.6%</td>
<td align="right">4,046,570</td>
<td align="right">1.9%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,354</td>
<td align="right">0.5%</td>
<td align="right">1,047,603</td>
<td align="right">0.5%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,891,409</td>
<td align="right">37.5%</td>
<td align="right">81,531,738</td>
<td align="right">37.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,891,409</td>
<td align="right">37.5%</td>
<td align="right">81,531,738</td>
<td align="right">37.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,636,187</td>
<td align="right">89.2%</td>
<td align="right">193,792,415</td>
<td align="right">89.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,381,415</td>
<td align="right">62.5%</td>
<td align="right">135,543,483</td>
<td align="right">62.4%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,422,463</td>
<td align="right">35.9%</td>
<td align="right">77,485,168</td>
<td align="right">35.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,421,678</td>
<td align="right">35.9%</td>
<td align="right">77,477,650</td>
<td align="right">35.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,737</td>
<td align="right">8.8%</td>
<td align="right">18,917,842</td>
<td align="right">8.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,137,433</td>
<td align="right">19.6%</td>
<td align="right">42,032,329</td>
<td align="right">19.4%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,149</td>
<td align="right">4.4%</td>
<td align="right">9,359,272</td>
<td align="right">4.3%</td>
<td align="right">0.3%</td>
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
<td align="right">8,931</td>
<td align="right">0.0%</td>
<td align="right">23,463</td>
<td align="right">0.0%</td>
<td align="right">162.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,352,090</td>
<td align="right"></td>
<td align="right">3,858,283</td>
<td align="right"></td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,753,828</td>
<td align="right"></td>
<td align="right">5,467,541</td>
<td align="right"></td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,373</td>
<td align="right"></td>
<td align="right">1,186,736</td>
<td align="right"></td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,403,312</td>
<td align="right"></td>
<td align="right">1,612,703</td>
<td align="right"></td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">760,111</td>
<td align="right">0.2%</td>
<td align="right">857,215</td>
<td align="right">0.2%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">79,078,912</td>
<td align="right">2.3%</td>
<td align="right">83,382,536</td>
<td align="right">2.4%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,054,003</td>
<td align="right">26.8%</td>
<td align="right">135,568,912</td>
<td align="right">27.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,284,961</td>
<td align="right">26.6%</td>
<td align="right">134,688,234</td>
<td align="right">27.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,360,798</td>
<td align="right">1.3%</td>
<td align="right">53,749,459</td>
<td align="right">1.3%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">970,291,526</td>
<td align="right">28.3%</td>
<td align="right">1,004,596,242</td>
<td align="right">28.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,100,015,765</td>
<td align="right">32.0%</td>
<td align="right">1,136,862,501</td>
<td align="right">32.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,203,867,984</td>
<td align="right">30.8%</td>
<td align="right">1,241,498,424</td>
<td align="right">30.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,708,921</td>
<td align="right"></td>
<td align="right">146,078,318</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,803,859</td>
<td align="right"></td>
<td align="right">255,533,701</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,055,627,798</td>
<td align="right">27.0%</td>
<td align="right">1,083,684,844</td>
<td align="right">27.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">352,530,335</td>
<td align="right"></td>
<td align="right">361,648,085</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">352,495,146</td>
<td align="right">73.2%</td>
<td align="right">361,394,613</td>
<td align="right">72.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">150,452,763</td>
<td align="right"></td>
<td align="right">154,210,129</td>
<td align="right"></td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,283,213,812</td>
<td align="right">37.4%</td>
<td align="right">1,314,401,543</td>
<td align="right">37.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,600,782,275</td>
<td align="right">40.9%</td>
<td align="right">1,639,608,034</td>
<td align="right">40.8%</td>
<td align="right">2.4%</td>
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
Stats gathered on: 2025-06-26
