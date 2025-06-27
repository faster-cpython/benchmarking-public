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
<td align="right">1,264</td>
<td align="right">2,006.7%</td>
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
<td align="right">995</td>
<td align="right">20,740</td>
<td align="right">1,984.4%</td>
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
<td align="right">2,960</td>
<td align="right">50,153</td>
<td align="right">1,594.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,112</td>
<td align="right">89,537</td>
<td align="right">1,159.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,801</td>
<td align="right">272,916</td>
<td align="right">1,046.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,079</td>
<td align="right">191,350</td>
<td align="right">958.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,442</td>
<td align="right">13,448</td>
<td align="right">832.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,690</td>
<td align="right">165,001</td>
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
<td align="right">9,017</td>
<td align="right">40,123</td>
<td align="right">345.0%</td>
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
<td align="right">79,547</td>
<td align="right">214,794</td>
<td align="right">170.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,282</td>
<td align="right">1,234,376</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,329</td>
<td align="right">386,623</td>
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
<td align="right">41,195</td>
<td align="right">58,750</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">378,841</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,329,566</td>
<td align="right">4,554,026</td>
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
<td align="right">2,281,587</td>
<td align="right">2,987,282</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,179</td>
<td align="right">7,867,411</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,035,113</td>
<td align="right">5,229,016</td>
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
<td align="right">4,002,056</td>
<td align="right">5,096,966</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,983</td>
<td align="right">945,892</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,860</td>
<td align="right">1,737,637</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,535</td>
<td align="right">743,833</td>
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
<td align="right">1,221,655</td>
<td align="right">1,454,614</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,122</td>
<td align="right">98,324</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">427,533</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,914</td>
<td align="right">444,249</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,331</td>
<td align="right">848,518</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,254</td>
<td align="right">743,498</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,254</td>
<td align="right">743,498</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,254</td>
<td align="right">743,498</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,525</td>
<td align="right">736,750</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,509</td>
<td align="right">736,406</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,736</td>
<td align="right">2,257,733</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,311</td>
<td align="right">1,477,400</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,575</td>
<td align="right">2,021,667</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,274</td>
<td align="right">7,362,296</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,590,402</td>
<td align="right">7,262,308</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,978,714</td>
<td align="right">9,882,032</td>
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
<td align="right">5,753,692</td>
<td align="right">6,277,544</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,670</td>
<td align="right">4,886,181</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,921,196</td>
<td align="right">11,856,190</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,832,084</td>
<td align="right">7,401,737</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,873,681</td>
<td align="right">11,740,342</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,424</td>
<td align="right">7,254,593</td>
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
<td align="right">171,994</td>
<td align="right">184,114</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,713</td>
<td align="right">494,033</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,162</td>
<td align="right">2,763,176</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,601,708</td>
<td align="right">19,787,234</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,688</td>
<td align="right">2,136,615</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,666,594</td>
<td align="right">18,679,210</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,479,957</td>
<td align="right">10,005,203</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,709,189</td>
<td align="right">13,400,755</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,147,603</td>
<td align="right">34,859,645</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,030,006</td>
<td align="right">1,082,615</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,115</td>
<td align="right">1,080,797</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,611,401</td>
<td align="right">187,333,965</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,992,964</td>
<td align="right">10,470,370</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">15,008,603</td>
<td align="right">15,700,880</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">149,489,014</td>
<td align="right">156,308,061</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,618,105</td>
<td align="right">12,129,578</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60,624,108</td>
<td align="right">63,278,446</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,525</td>
<td align="right">1,825,642</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,928,962</td>
<td align="right">18,643,221</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">46,453,916</td>
<td align="right">48,258,450</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,010,652</td>
<td align="right">11,422,814</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,115,430</td>
<td align="right">54,047,305</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,302,528</td>
<td align="right">51,127,890</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,231,648</td>
<td align="right">27,193,941</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,377,872</td>
<td align="right">24,212,604</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,494,797</td>
<td align="right">50,196,820</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,207,400</td>
<td align="right">206,045,847</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">745,333</td>
<td align="right">770,509</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,660</td>
<td align="right">7,796,351</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,737,066</td>
<td align="right">81,369,327</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,876,335</td>
<td align="right">187,791,215</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,279,901</td>
<td align="right">55,007,666</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,424,546</td>
<td align="right">17,982,699</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,647,347</td>
<td align="right">36,780,434</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,099,672</td>
<td align="right">11,448,984</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,562</td>
<td align="right">3,088,428</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">45,111,718</td>
<td align="right">46,478,126</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">679,101,554</td>
<td align="right">699,532,737</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,068,372</td>
<td align="right">19,639,784</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,696,031</td>
<td align="right">22,343,470</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,103,750</td>
<td align="right">116,465,593</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,883,802</td>
<td align="right">54,435,925</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,617</td>
<td align="right">4,598,935</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">135,221,924</td>
<td align="right">139,127,581</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">149,939,588</td>
<td align="right">154,151,967</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,923,543</td>
<td align="right">8,141,245</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,087,290</td>
<td align="right">8,306,411</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,603</td>
<td align="right">17,918,151</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">232,636,946</td>
<td align="right">238,871,300</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,778,034</td>
<td align="right">10,025,799</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,961,023</td>
<td align="right">82,919,937</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,825,616</td>
<td align="right">46,918,237</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,440,589</td>
<td align="right">36,278,863</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,686</td>
<td align="right">22,500,318</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,743,040</td>
<td align="right">25,319,493</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,094,883</td>
<td align="right">40,984,031</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,145,252</td>
<td align="right">27,686,349</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,976,687</td>
<td align="right">6,095,616</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,631,651</td>
<td align="right">37,356,259</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,616,864</td>
<td align="right">2,668,442</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,130,949</td>
<td align="right">23,586,054</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">192,653,091</td>
<td align="right">196,431,306</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">273,578,812</td>
<td align="right">278,915,251</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,322</td>
<td align="right">6,913,783</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">44,480,299</td>
<td align="right">45,289,114</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,986,244</td>
<td align="right">16,258,370</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,163,868</td>
<td align="right">13,385,646</td>
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
<td align="right">47,046,882</td>
<td align="right">47,763,385</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,957,582</td>
<td align="right">73,036,731</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,436,023</td>
<td align="right">12,606,335</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,945,589</td>
<td align="right">17,171,921</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,781,489</td>
<td align="right">82,813,444</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,403</td>
<td align="right">143,113</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,503</td>
<td align="right">22,225,747</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,612,997</td>
<td align="right">4,664,344</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,646</td>
<td align="right">932,398</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,549</td>
<td align="right">431,889</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,394,323</td>
<td align="right">73,087,839</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,800,412</td>
<td align="right">71,458,844</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,574,092</td>
<td align="right">76,217,523</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,844,903</td>
<td align="right">45,199,177</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,630,321</td>
<td align="right">18,777,359</td>
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
<td align="right">165,703</td>
<td align="right">166,978</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,314,253</td>
<td align="right">18,443,559</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,643</td>
<td align="right">26,906,216</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,492,968</td>
<td align="right">30,673,403</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,077,896</td>
<td align="right">18,969,661</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,742,740</td>
<td align="right">15,656,891</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,712</td>
<td align="right">4,203,852</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,016,994</td>
<td align="right">15,938,388</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,422,217</td>
<td align="right">23,310,085</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,531</td>
<td align="right">1,249,631</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,412,479</td>
<td align="right">46,227,886</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,774,244</td>
<td align="right">84,014,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,257</td>
<td align="right">1,291,711</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,263,410</td>
<td align="right">82,452,558</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,200,037</td>
<td align="right">2,195,978</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,242,121</td>
<td align="right">6,246,478</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">163,668,931</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">437,301</td>
<td align="right">0.4%</td>
<td align="right">475,578</td>
<td align="right">0.4%</td>
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
<td align="right">70,887,922</td>
<td align="right">60.5%</td>
<td align="right">74,080,262</td>
<td align="right">61.0%</td>
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
<td align="right">45,794,386</td>
<td align="right">39.1%</td>
<td align="right">46,835,425</td>
<td align="right">38.6%</td>
<td align="right">2.3%</td>
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
<td align="right">10,349</td>
<td align="right">26.2%</td>
<td align="right">24,868</td>
<td align="right">27.2%</td>
<td align="right">140.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">29,103</td>
<td align="right">73.8%</td>
<td align="right">66,606</td>
<td align="right">72.8%</td>
<td align="right">128.9%</td>
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
<td align="right">1,253</td>
<td align="right">1.9%</td>
<td align="right">245.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">625</td>
<td align="right">2.1%</td>
<td align="right">2,063</td>
<td align="right">3.1%</td>
<td align="right">230.1%</td>
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
<td align="right">2,894</td>
<td align="right">9.9%</td>
<td align="right">9,426</td>
<td align="right">14.2%</td>
<td align="right">225.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,213</td>
<td align="right">4.2%</td>
<td align="right">3,736</td>
<td align="right">5.6%</td>
<td align="right">208.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">705</td>
<td align="right">2.4%</td>
<td align="right">2,157</td>
<td align="right">3.2%</td>
<td align="right">206.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">2,940</td>
<td align="right">4.4%</td>
<td align="right">199.4%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,757</td>
<td align="right">6.0%</td>
<td align="right">4,874</td>
<td align="right">7.3%</td>
<td align="right">177.4%</td>
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
<td align="left">true divide different types</td>
<td align="right">1,085</td>
<td align="right">3.7%</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">117.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">196</td>
<td align="right">0.3%</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">571</td>
<td align="right">2.0%</td>
<td align="right">1,177</td>
<td align="right">1.8%</td>
<td align="right">106.1%</td>
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
<td align="right">1,006</td>
<td align="right">3.5%</td>
<td align="right">1,927</td>
<td align="right">2.9%</td>
<td align="right">91.6%</td>
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
<td align="right">4,591</td>
<td align="right">15.8%</td>
<td align="right">7,953</td>
<td align="right">11.9%</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">212</td>
<td align="right">0.7%</td>
<td align="right">359</td>
<td align="right">0.5%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.6%</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,893</td>
<td align="right">13.4%</td>
<td align="right">4,042</td>
<td align="right">6.1%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3</td>
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
<td align="right">276,421,676</td>
<td align="right">88.3%</td>
<td align="right">285,958,727</td>
<td align="right">88.4%</td>
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
<td align="right">35,805,337</td>
<td align="right">11.4%</td>
<td align="right">36,663,809</td>
<td align="right">11.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">36,485,212</td>
<td align="right">11.7%</td>
<td align="right">37,189,383</td>
<td align="right">11.5%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">37,189,383</td>
<td align="right">11.5%</td>
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
<td align="left">Success</td>
<td align="right">703,676</td>
<td align="right">100.0%</td>
<td align="right">798,490</td>
<td align="right">100.0%</td>
<td align="right">13.5%</td>
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
<td align="right">11,352</td>
<td align="right">69.1%</td>
<td align="right">256.6%</td>
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
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,988</td>
<td align="right">18.2%</td>
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
<td align="left">Success</td>
<td align="right">1,064</td>
<td align="right">100.0%</td>
<td align="right">5,084</td>
<td align="right">100.0%</td>
<td align="right">377.8%</td>
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
<td align="right">409,662</td>
<td align="right">0.5%</td>
<td align="right">447,872</td>
<td align="right">0.5%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,033,966</td>
<td align="right">62.3%</td>
<td align="right">52,824,238</td>
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
<td align="right">30,454,353</td>
<td align="right">37.2%</td>
<td align="right">30,599,507</td>
<td align="right">36.5%</td>
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
<td align="right">8,833</td>
<td align="right">19.1%</td>
<td align="right">18,189</td>
<td align="right">22.1%</td>
<td align="right">105.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,455</td>
<td align="right">80.9%</td>
<td align="right">63,998</td>
<td align="right">77.9%</td>
<td align="right">70.9%</td>
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
<td align="right">3,151</td>
<td align="right">8.4%</td>
<td align="right">10,000</td>
<td align="right">15.6%</td>
<td align="right">217.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,256</td>
<td align="right">11.4%</td>
<td align="right">12,053</td>
<td align="right">18.8%</td>
<td align="right">183.2%</td>
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
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">137.4%</td>
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
<td align="right">6,469</td>
<td align="right">17.3%</td>
<td align="right">14,458</td>
<td align="right">22.6%</td>
<td align="right">123.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">292</td>
<td align="right">0.5%</td>
<td align="right">116.3%</td>
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
<td align="right">1,466</td>
<td align="right">3.9%</td>
<td align="right">1,783</td>
<td align="right">2.8%</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,110</td>
<td align="right">37.7%</td>
<td align="right">16,088</td>
<td align="right">25.1%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
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
<td align="right">17,417,428</td>
<td align="right">42.6%</td>
<td align="right">17,967,108</td>
<td align="right">43.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,500,744</td>
<td align="right">57.4%</td>
<td align="right">23,523,955</td>
<td align="right">56.7%</td>
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
<td align="right">8.8%</td>
<td align="right">992.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,993</td>
<td align="right">98.2%</td>
<td align="right">14,226</td>
<td align="right">91.2%</td>
<td align="right">103.4%</td>
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
<td align="right">1,473</td>
<td align="right">21.1%</td>
<td align="right">5,526</td>
<td align="right">38.8%</td>
<td align="right">275.2%</td>
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
<td align="right">5,039</td>
<td align="right">72.1%</td>
<td align="right">7,146</td>
<td align="right">50.2%</td>
<td align="right">41.8%</td>
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
<td align="right">102,430,338</td>
<td align="right">55.2%</td>
<td align="right">106,193,556</td>
<td align="right">55.8%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,256,797</td>
<td align="right">0.7%</td>
<td align="right">1,211,429</td>
<td align="right">0.6%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,719,513</td>
<td align="right">44.1%</td>
<td align="right">82,714,486</td>
<td align="right">43.5%</td>
<td align="right">1.2%</td>
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
<td align="right">24,415</td>
<td align="right">28.5%</td>
<td align="right">36,823</td>
<td align="right">30.3%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,185</td>
<td align="right">71.5%</td>
<td align="right">84,872</td>
<td align="right">69.7%</td>
<td align="right">38.7%</td>
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
<td align="right">1,361</td>
<td align="right">2.2%</td>
<td align="right">4,307</td>
<td align="right">5.1%</td>
<td align="right">216.5%</td>
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
<td align="right">47,016</td>
<td align="right">76.8%</td>
<td align="right">56,893</td>
<td align="right">67.0%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,356</td>
<td align="right">10.4%</td>
<td align="right">7,603</td>
<td align="right">9.0%</td>
<td align="right">19.6%</td>
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
<td align="right">157,957</td>
<td align="right">157,957 / 0 !!</td>
<td align="right">166,106</td>
<td align="right">166,106 / 0 !!</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,456</td>
<td align="right">70,456 / 0 !!</td>
<td align="right">72,796</td>
<td align="right">72,796 / 0 !!</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,716,141</td>
<td align="right">8,716,141 / 0 !!</td>
<td align="right">8,947,217</td>
<td align="right">8,947,217 / 0 !!</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,184,609</td>
<td align="right">7,184,609 / 0 !!</td>
<td align="right">7,368,690</td>
<td align="right">7,368,690 / 0 !!</td>
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
<td align="right">12,236,601</td>
<td align="right">12,236,601 / 0 !!</td>
<td align="right">12,461,900</td>
<td align="right">12,461,900 / 0 !!</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,727</td>
<td align="right">9,440,727 / 0 !!</td>
<td align="right">9,563,739</td>
<td align="right">9,563,739 / 0 !!</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,233,920</td>
<td align="right">9,233,920 / 0 !!</td>
<td align="right">9,172,644</td>
<td align="right">9,172,644 / 0 !!</td>
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
<td align="right">223,192,612</td>
<td align="right">64.3%</td>
<td align="right">229,390,523</td>
<td align="right">64.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">70,737,453</td>
<td align="right">20.4%</td>
<td align="right">71,232,478</td>
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
<td align="right">53,244,981</td>
<td align="right">15.3%</td>
<td align="right">53,449,879</td>
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
<td align="right">47,756</td>
<td align="right">4.5%</td>
<td align="right">127,514</td>
<td align="right">10.4%</td>
<td align="right">167.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,015,458</td>
<td align="right">95.5%</td>
<td align="right">1,095,112</td>
<td align="right">89.6%</td>
<td align="right">7.8%</td>
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
<td align="right">12,349</td>
<td align="right">9.7%</td>
<td align="right">203.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,101</td>
<td align="right">6.5%</td>
<td align="right">8,883</td>
<td align="right">7.0%</td>
<td align="right">186.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,874</td>
<td align="right">45.8%</td>
<td align="right">61,727</td>
<td align="right">48.4%</td>
<td align="right">182.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,740</td>
<td align="right">5.7%</td>
<td align="right">7,569</td>
<td align="right">5.9%</td>
<td align="right">176.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,355</td>
<td align="right">9.1%</td>
<td align="right">10,736</td>
<td align="right">8.4%</td>
<td align="right">146.5%</td>
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
<td align="right">4,549</td>
<td align="right">0.0%</td>
<td align="right">94,816</td>
<td align="right">0.0%</td>
<td align="right">1,984.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,303</td>
<td align="right">0.0%</td>
<td align="right">21,399</td>
<td align="right">0.0%</td>
<td align="right">1,542.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">291,713,848</td>
<td align="right">100.0%</td>
<td align="right">303,778,159</td>
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
<td align="right">96,744</td>
<td align="right">100.0%</td>
<td align="right">612.3%</td>
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
<td align="right">634</td>
<td align="right">0.0%</td>
<td align="right">2,013.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,957</td>
<td align="right">100.0%</td>
<td align="right">2,409,798</td>
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
<td align="right">731,620</td>
<td align="right">72.0%</td>
<td align="right">821,097</td>
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
<td align="right">174,018</td>
<td align="right">1.9%</td>
<td align="right">377,594</td>
<td align="right">3.5%</td>
<td align="right">117.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,329,139</td>
<td align="right">80.7%</td>
<td align="right">8,527,724</td>
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
<td align="right">1,575,722</td>
<td align="right">17.4%</td>
<td align="right">1,821,854</td>
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
<td align="right">975</td>
<td align="right">3.2%</td>
<td align="right">3,653</td>
<td align="right">8.4%</td>
<td align="right">274.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">29,976</td>
<td align="right">96.8%</td>
<td align="right">39,658</td>
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
<td align="right">300</td>
<td align="right">30.8%</td>
<td align="right">1,406</td>
<td align="right">38.5%</td>
<td align="right">368.7%</td>
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
<td align="right">53.1%</td>
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
<td align="right">2,583,043</td>
<td align="right">12.7%</td>
<td align="right">2,756,808</td>
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
<td align="right">17,740,769</td>
<td align="right">87.3%</td>
<td align="right">18,084,012</td>
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
<td align="right">2,858</td>
<td align="right">44.9%</td>
<td align="right">396.2%</td>
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
<td align="right">623,266</td>
<td align="right">0.3%</td>
<td align="right">668,840</td>
<td align="right">0.4%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,478,326</td>
<td align="right">94.2%</td>
<td align="right">174,041,916</td>
<td align="right">94.2%</td>
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
<td align="right">9,755,980</td>
<td align="right">5.4%</td>
<td align="right">9,941,407</td>
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
<td align="right">18,979</td>
<td align="right">57.1%</td>
<td align="right">68,659</td>
<td align="right">71.6%</td>
<td align="right">261.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,277</td>
<td align="right">42.9%</td>
<td align="right">27,191</td>
<td align="right">28.4%</td>
<td align="right">90.5%</td>
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
<td align="right">722</td>
<td align="right">5.1%</td>
<td align="right">2,352</td>
<td align="right">8.6%</td>
<td align="right">225.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,262</td>
<td align="right">8.8%</td>
<td align="right">3,367</td>
<td align="right">12.4%</td>
<td align="right">166.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">719</td>
<td align="right">5.0%</td>
<td align="right">1,396</td>
<td align="right">5.1%</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,952</td>
<td align="right">55.7%</td>
<td align="right">13,535</td>
<td align="right">49.8%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,653</td>
<td align="right">18.6%</td>
<td align="right">3,076</td>
<td align="right">11.3%</td>
<td align="right">15.9%</td>
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
<td align="right">6,331</td>
<td align="right">0.0%</td>
<td align="right">27,433</td>
<td align="right">0.0%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,693,070</td>
<td align="right">100.0%</td>
<td align="right">83,887,382</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">89.0%</td>
<td align="right">11,935</td>
<td align="right">94.1%</td>
<td align="right">399.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">295</td>
<td align="right">11.0%</td>
<td align="right">755</td>
<td align="right">5.9%</td>
<td align="right">155.9%</td>
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
<td align="right">252</td>
<td align="right">85.4%</td>
<td align="right">692</td>
<td align="right">91.7%</td>
<td align="right">174.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.6%</td>
<td align="right">63</td>
<td align="right">8.3%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,757,336,883</td>
<td align="right">57.4%</td>
<td align="right">3,000,154,603</td>
<td align="right">58.8%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,642,592,989</td>
<td align="right">34.2%</td>
<td align="right">1,697,446,720</td>
<td align="right">33.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">306,245,561</td>
<td align="right">6.4%</td>
<td align="right">311,776,126</td>
<td align="right">6.1%</td>
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
<td align="right">94,052,780</td>
<td align="right">2.0%</td>
<td align="right">95,317,567</td>
<td align="right">1.9%</td>
<td align="right">1.3%</td>
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
<td align="right">174,018</td>
<td align="right">0.1%</td>
<td align="right">377,594</td>
<td align="right">0.1%</td>
<td align="right">117.0%</td>
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
<td align="right">2,583,043</td>
<td align="right">0.9%</td>
<td align="right">2,756,808</td>
<td align="right">0.9%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,417,428</td>
<td align="right">5.9%</td>
<td align="right">17,967,108</td>
<td align="right">6.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,805,337</td>
<td align="right">12.1%</td>
<td align="right">36,663,809</td>
<td align="right">12.2%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,794,386</td>
<td align="right">15.5%</td>
<td align="right">46,835,425</td>
<td align="right">15.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,980</td>
<td align="right">3.3%</td>
<td align="right">9,941,407</td>
<td align="right">3.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,719,513</td>
<td align="right">27.7%</td>
<td align="right">82,714,486</td>
<td align="right">27.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">70,737,453</td>
<td align="right">24.0%</td>
<td align="right">71,232,478</td>
<td align="right">23.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,454,353</td>
<td align="right">10.3%</td>
<td align="right">30,599,507</td>
<td align="right">10.2%</td>
<td align="right">0.5%</td>
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
<td align="right">1,574,943</td>
<td align="right">1.7%</td>
<td align="right">1,821,068</td>
<td align="right">1.9%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,315,646</td>
<td align="right">12.0%</td>
<td align="right">11,676,112</td>
<td align="right">12.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,202,729</td>
<td align="right">3.4%</td>
<td align="right">3,289,816</td>
<td align="right">3.5%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,702,207</td>
<td align="right">12.4%</td>
<td align="right">11,902,585</td>
<td align="right">12.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,605</td>
<td align="right">5.4%</td>
<td align="right">5,167,058</td>
<td align="right">5.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,290,600</td>
<td align="right">14.1%</td>
<td align="right">13,378,050</td>
<td align="right">14.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,151,650</td>
<td align="right">6.5%</td>
<td align="right">6,180,076</td>
<td align="right">6.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,022,760</td>
<td align="right">30.9%</td>
<td align="right">28,963,522</td>
<td align="right">30.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,248</td>
<td align="right">7.8%</td>
<td align="right">7,302,537</td>
<td align="right">7.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,586</td>
<td align="right">2.2%</td>
<td align="right">2,105,488</td>
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
<td align="right">3,468,951</td>
<td align="right">1.6%</td>
<td align="right">4,046,597</td>
<td align="right">1.9%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,257</td>
<td align="right">0.5%</td>
<td align="right">1,047,648</td>
<td align="right">0.5%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,418,551</td>
<td align="right">62.5%</td>
<td align="right">136,011,345</td>
<td align="right">62.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,891,481</td>
<td align="right">37.5%</td>
<td align="right">81,533,639</td>
<td align="right">37.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,891,481</td>
<td align="right">37.5%</td>
<td align="right">81,533,639</td>
<td align="right">37.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,687,245</td>
<td align="right">89.2%</td>
<td align="right">193,762,056</td>
<td align="right">89.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,422,530</td>
<td align="right">35.9%</td>
<td align="right">77,487,042</td>
<td align="right">35.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,421,745</td>
<td align="right">35.9%</td>
<td align="right">77,479,524</td>
<td align="right">35.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,755</td>
<td align="right">8.8%</td>
<td align="right">18,917,856</td>
<td align="right">8.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,137,420</td>
<td align="right">19.6%</td>
<td align="right">42,033,877</td>
<td align="right">19.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,104</td>
<td align="right">4.4%</td>
<td align="right">9,359,393</td>
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
<td align="right">2,211,065</td>
<td align="right"></td>
<td align="right">4,197,394</td>
<td align="right"></td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,819,716</td>
<td align="right"></td>
<td align="right">5,709,260</td>
<td align="right"></td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,372</td>
<td align="right"></td>
<td align="right">1,186,762</td>
<td align="right"></td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">761,571</td>
<td align="right">0.2%</td>
<td align="right">851,779</td>
<td align="right">0.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,610,356</td>
<td align="right"></td>
<td align="right">1,515,561</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">79,096,380</td>
<td align="right">2.3%</td>
<td align="right">83,407,923</td>
<td align="right">2.4%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,083,960</td>
<td align="right">26.8%</td>
<td align="right">135,597,935</td>
<td align="right">27.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,313,458</td>
<td align="right">26.6%</td>
<td align="right">134,722,693</td>
<td align="right">27.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,429,546</td>
<td align="right">1.3%</td>
<td align="right">53,739,867</td>
<td align="right">1.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">970,667,044</td>
<td align="right">28.3%</td>
<td align="right">1,005,501,965</td>
<td align="right">28.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,100,224,780</td>
<td align="right">32.0%</td>
<td align="right">1,137,303,053</td>
<td align="right">32.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,204,063,378</td>
<td align="right">30.8%</td>
<td align="right">1,241,511,686</td>
<td align="right">30.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,738,825</td>
<td align="right"></td>
<td align="right">146,109,951</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,639,588</td>
<td align="right"></td>
<td align="right">255,591,234</td>
<td align="right"></td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,055,955,684</td>
<td align="right">27.0%</td>
<td align="right">1,084,327,189</td>
<td align="right">27.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">352,553,964</td>
<td align="right"></td>
<td align="right">361,659,585</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,601,072,071</td>
<td align="right">40.9%</td>
<td align="right">1,641,502,319</td>
<td align="right">40.8%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,283,438,215</td>
<td align="right">37.4%</td>
<td align="right">1,315,818,705</td>
<td align="right">37.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">352,518,772</td>
<td align="right">73.2%</td>
<td align="right">361,406,108</td>
<td align="right">72.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">150,595,221</td>
<td align="right"></td>
<td align="right">153,876,478</td>
<td align="right"></td>
<td align="right">2.2%</td>
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
Stats gathered on: 2025-06-27
