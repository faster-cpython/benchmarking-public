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
<td align="left">JUMP_BACKWARD</td>
<td align="right">6,359</td>
<td align="right">235,338</td>
<td align="right">3,600.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">362</td>
<td align="right">9,940</td>
<td align="right">2,645.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,186</td>
<td align="right">70,922</td>
<td align="right">2,126.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,783</td>
<td align="right">24,961</td>
<td align="right">1,299.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,732</td>
<td align="right">17,988</td>
<td align="right">938.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">840</td>
<td align="right">7,652</td>
<td align="right">811.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,046</td>
<td align="right">7,431</td>
<td align="right">610.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">312</td>
<td align="right">2,076</td>
<td align="right">565.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">316</td>
<td align="right">2,080</td>
<td align="right">558.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">328</td>
<td align="right">2,104</td>
<td align="right">541.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,176</td>
<td align="right">7,478</td>
<td align="right">535.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,505</td>
<td align="right">45,772</td>
<td align="right">438.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">33,212</td>
<td align="right">134,982</td>
<td align="right">306.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,781</td>
<td align="right">21,869</td>
<td align="right">278.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">21,758</td>
<td align="right">67,846</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">61,809</td>
<td align="right">149,875</td>
<td align="right">142.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,127</td>
<td align="right">22,912</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">7,040</td>
<td align="right">15,248</td>
<td align="right">116.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">48,913</td>
<td align="right">102,608</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">75,660</td>
<td align="right">149,479</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">18,133</td>
<td align="right">35,084</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">24,464</td>
<td align="right">45,460</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">63,557</td>
<td align="right">117,747</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">127,294</td>
<td align="right">235,396</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">46,399</td>
<td align="right">74,659</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">29,881</td>
<td align="right">47,962</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">842</td>
<td align="right">1,304</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,393</td>
<td align="right">38,178</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,908</td>
<td align="right">2,844</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">56,341</td>
<td align="right">82,267</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">29,360</td>
<td align="right">42,677</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,121</td>
<td align="right">1,583</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,557</td>
<td align="right">26,820</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">51,712</td>
<td align="right">70,196</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,369</td>
<td align="right">61,425</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">17,242</td>
<td align="right">22,156</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,002</td>
<td align="right">42,381</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">41,566</td>
<td align="right">53,337</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">19,070</td>
<td align="right">24,211</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">66,977</td>
<td align="right">84,816</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">19,618</td>
<td align="right">24,759</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">95,820</td>
<td align="right">120,872</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">378,498</td>
<td align="right">473,702</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">43,337</td>
<td align="right">54,005</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">9,479</td>
<td align="right">11,789</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">21,034</td>
<td align="right">25,667</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,526</td>
<td align="right">12,841</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,189</td>
<td align="right">23,288</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,304</td>
<td align="right">1,576</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">26,282</td>
<td align="right">31,639</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">20,971</td>
<td align="right">25,217</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">9,301</td>
<td align="right">11,142</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,670,199</td>
<td align="right">1,966,042</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">150,139</td>
<td align="right">174,710</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">110,663</td>
<td align="right">128,279</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">17,513</td>
<td align="right">14,769</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6,159</td>
<td align="right">7,083</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">15,508</td>
<td align="right">17,818</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">213,077</td>
<td align="right">242,744</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">770,485</td>
<td align="right">877,581</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">85,431</td>
<td align="right">97,162</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">803,168</td>
<td align="right">906,689</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">118,665</td>
<td align="right">133,869</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,701</td>
<td align="right">9,625</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,472</td>
<td align="right">11,444</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">10,140</td>
<td align="right">11,064</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">755,274</td>
<td align="right">815,607</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">15,598</td>
<td align="right">16,642</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">15,598</td>
<td align="right">16,642</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">7,927</td>
<td align="right">8,449</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">438</td>
<td align="right">459</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,428</td>
<td align="right">10,902</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">646,099</td>
<td align="right">675,367</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,110,437</td>
<td align="right">2,178,775</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,219,036</td>
<td align="right">20,761,083</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">129,401</td>
<td align="right">132,031</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">26,955</td>
<td align="right">27,444</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">281</td>
<td align="right">285</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">647,826</td>
<td align="right">655,786</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,966</td>
<td align="right">1,987</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,729</td>
<td align="right">8,809</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,657,556</td>
<td align="right">8,708,277</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">6,192</td>
<td align="right">6,216</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">27,654,456</td>
<td align="right">27,550,652</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">747,618</td>
<td align="right">749,730</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,532,247</td>
<td align="right">8,554,733</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,682</td>
<td align="right">5,694</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">47,896,638</td>
<td align="right">47,968,665</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">35,515,039</td>
<td align="right">35,561,539</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">13,066,253</td>
<td align="right">13,079,038</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,108</td>
<td align="right">17,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">69,272,702</td>
<td align="right">69,319,099</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">13,068,861</td>
<td align="right">13,070,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,397,902</td>
<td align="right">46,403,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,475,989</td>
<td align="right">8,476,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">47,617,794</td>
<td align="right">47,617,794</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">32,719,252</td>
<td align="right">32,719,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">8,446,852</td>
<td align="right">8,446,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">22,656</td>
<td align="right">22,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">18,684</td>
<td align="right">18,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">18,466</td>
<td align="right">18,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14,900</td>
<td align="right">14,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">11,142</td>
<td align="right">11,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">10,404</td>
<td align="right">10,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">8,596</td>
<td align="right">8,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">7,180</td>
<td align="right">7,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">5,388</td>
<td align="right">5,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">5,325</td>
<td align="right">5,325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,159</td>
<td align="right">5,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">4,608</td>
<td align="right">4,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,568</td>
<td align="right">2,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,847</td>
<td align="right">1,847</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,837</td>
<td align="right">1,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,837</td>
<td align="right">1,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,837</td>
<td align="right">1,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,726</td>
<td align="right">1,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,565</td>
<td align="right">1,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,544</td>
<td align="right">1,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,544</td>
<td align="right">1,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,532</td>
<td align="right">1,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,356</td>
<td align="right">1,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">373</td>
<td align="right">373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">272</td>
<td align="right">272</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">256</td>
<td align="right">256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">256</td>
<td align="right">256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">247</td>
<td align="right">247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224</td>
<td align="right">224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">132</td>
<td align="right">132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">56</td>
<td align="right">56</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">1,357</td>
<td align="right">0.0%</td>
<td align="right">24,401</td>
<td align="right">0.1%</td>
<td align="right">1,698.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">25,458,816</td>
<td align="right">100.0%</td>
<td align="right">25,458,816</td>
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
<td align="right">137</td>
<td align="right">100.0%</td>
<td align="right">271</td>
<td align="right">100.0%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">remainder</td>
<td align="right">49</td>
<td align="right">35.8%</td>
<td align="right">183</td>
<td align="right">67.5%</td>
<td align="right">273.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">88</td>
<td align="right">64.2%</td>
<td align="right">88</td>
<td align="right">32.5%</td>
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
<td align="right">16</td>
<td align="right">100.0%</td>
<td align="right">16</td>
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
<td align="right">16,985</td>
<td align="right">0.2%</td>
<td align="right">21,854</td>
<td align="right">0.2%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,219,186</td>
<td align="right">99.8%</td>
<td align="right">9,219,186</td>
<td align="right">99.8%</td>
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
<td align="right">227</td>
<td align="right">88.3%</td>
<td align="right">272</td>
<td align="right">90.1%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30</td>
<td align="right">11.7%</td>
<td align="right">30</td>
<td align="right">9.9%</td>
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
<td align="right">3</td>
<td align="right">1.3%</td>
<td align="right">47</td>
<td align="right">17.3%</td>
<td align="right">1,466.7%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">158</td>
<td align="right">69.6%</td>
<td align="right">159</td>
<td align="right">58.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">66</td>
<td align="right">29.1%</td>
<td align="right">66</td>
<td align="right">24.3%</td>
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
<td align="right">7,113</td>
<td align="right">0.0%</td>
<td align="right">8,324</td>
<td align="right">0.0%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">133,682,700</td>
<td align="right">100.0%</td>
<td align="right">133,681,499</td>
<td align="right">100.0%</td>
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
<td align="right">706</td>
<td align="right">0.0%</td>
<td align="right">706</td>
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
<td align="right">4,905</td>
<td align="right">100.0%</td>
<td align="right">4,927</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">48</td>
<td align="right">12.9%</td>
<td align="right">48</td>
<td align="right">12.9%</td>
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
<td align="right">1,408</td>
<td align="right">0.1%</td>
<td align="right">1,408</td>
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
<td align="right">1,468,099</td>
<td align="right">99.9%</td>
<td align="right">1,468,099</td>
<td align="right">99.9%</td>
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
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">63</td>
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
<td align="right">264</td>
<td align="right">60.1%</td>
<td align="right">264</td>
<td align="right">60.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">175</td>
<td align="right">39.9%</td>
<td align="right">175</td>
<td align="right">39.9%</td>
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
<td align="right">112</td>
<td align="right">64.0%</td>
<td align="right">112</td>
<td align="right">64.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">42</td>
<td align="right">24.0%</td>
<td align="right">42</td>
<td align="right">24.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">21</td>
<td align="right">12.0%</td>
<td align="right">21</td>
<td align="right">12.0%</td>
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
<td align="right">109,665</td>
<td align="right">1.2%</td>
<td align="right">127,053</td>
<td align="right">1.4%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,199,772</td>
<td align="right">98.8%</td>
<td align="right">9,199,772</td>
<td align="right">98.6%</td>
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
<td align="right">990</td>
<td align="right">100.0%</td>
<td align="right">1,218</td>
<td align="right">100.0%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">str</td>
<td align="right">790</td>
<td align="right">79.8%</td>
<td align="right">997</td>
<td align="right">81.9%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">88</td>
<td align="right">8.9%</td>
<td align="right">109</td>
<td align="right">8.9%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">112</td>
<td align="right">11.3%</td>
<td align="right">112</td>
<td align="right">9.2%</td>
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
<td align="right">61,290</td>
<td align="right">4.2%</td>
<td align="right">149,179</td>
<td align="right">8.9%</td>
<td align="right">143.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,405,315</td>
<td align="right">95.8%</td>
<td align="right">1,519,411</td>
<td align="right">91.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">256</td>
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
<td align="right">391</td>
<td align="right">75.3%</td>
<td align="right">568</td>
<td align="right">81.6%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">128</td>
<td align="right">24.7%</td>
<td align="right">128</td>
<td align="right">18.4%</td>
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
<td align="right">12</td>
<td align="right">3.1%</td>
<td align="right">96</td>
<td align="right">16.9%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">139</td>
<td align="right">35.5%</td>
<td align="right">314</td>
<td align="right">55.3%</td>
<td align="right">125.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">54.5%</td>
<td align="right">130</td>
<td align="right">22.9%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">23</td>
<td align="right">5.9%</td>
<td align="right">23</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">4</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right"></td>
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
<td align="right">2,106,252</td>
<td align="right">5.1%</td>
<td align="right">2,174,866</td>
<td align="right">5.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,360,871</td>
<td align="right">94.9%</td>
<td align="right">39,360,891</td>
<td align="right">94.7%</td>
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
<td align="right">7,521</td>
<td align="right">0.0%</td>
<td align="right">7,521</td>
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
<td align="right">1,808</td>
<td align="right">41.9%</td>
<td align="right">1,532</td>
<td align="right">37.9%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,505</td>
<td align="right">58.1%</td>
<td align="right">2,505</td>
<td align="right">62.1%</td>
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
<td align="right">1,113</td>
<td align="right">61.6%</td>
<td align="right">837</td>
<td align="right">54.6%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">480</td>
<td align="right">26.5%</td>
<td align="right">480</td>
<td align="right">31.3%</td>
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
<td align="right">8,785,152</td>
<td align="right">99.9%</td>
<td align="right">8,943,051</td>
<td align="right">99.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">953</td>
<td align="right">0.0%</td>
<td align="right">953</td>
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
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">17</td>
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
<td align="right">622</td>
<td align="right">0.0%</td>
<td align="right">622</td>
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
<td align="right">4,372</td>
<td align="right">100.0%</td>
<td align="right">4,372</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,296</td>
<td align="right">99.7%</td>
<td align="right">1,296</td>
<td align="right">99.7%</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">4</td>
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
<td align="right">14,850</td>
<td align="right">0.1%</td>
<td align="right">14,850</td>
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
<td align="right">13,079,038</td>
<td align="right">99.9%</td>
<td align="right">13,079,038</td>
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
<td align="right">2</td>
<td align="right">4.0%</td>
<td align="right">2</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48</td>
<td align="right">96.0%</td>
<td align="right">48</td>
<td align="right">96.0%</td>
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
<td align="right">48</td>
<td align="right">100.0%</td>
<td align="right">48</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">645,475</td>
<td align="right">7.1%</td>
<td align="right">674,669</td>
<td align="right">7.4%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,472,076</td>
<td align="right">92.9%</td>
<td align="right">8,472,076</td>
<td align="right">92.6%</td>
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
<td align="right">4,862</td>
<td align="right">0.1%</td>
<td align="right">4,862</td>
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
<td align="right">577</td>
<td align="right">89.5%</td>
<td align="right">651</td>
<td align="right">90.5%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68</td>
<td align="right">10.5%</td>
<td align="right">68</td>
<td align="right">9.5%</td>
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
<td align="right">289</td>
<td align="right">50.1%</td>
<td align="right">363</td>
<td align="right">55.8%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">131</td>
<td align="right">22.7%</td>
<td align="right">131</td>
<td align="right">20.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">112</td>
<td align="right">19.4%</td>
<td align="right">112</td>
<td align="right">17.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">45</td>
<td align="right">7.8%</td>
<td align="right">45</td>
<td align="right">6.9%</td>
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
<td align="right">133</td>
<td align="right">0.2%</td>
<td align="right">133</td>
<td align="right">0.2%</td>
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
<td align="right">87,828</td>
<td align="right">99.8%</td>
<td align="right">87,828</td>
<td align="right">99.8%</td>
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
<td align="right">5</td>
<td align="right">18.5%</td>
<td align="right">5</td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">22</td>
<td align="right">81.5%</td>
<td align="right">22</td>
<td align="right">81.5%</td>
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
<td align="right">22</td>
<td align="right">100.0%</td>
<td align="right">22</td>
<td align="right">100.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">29,246</td>
<td align="right">0.0%</td>
<td align="right">47,322</td>
<td align="right">0.1%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,063</td>
<td align="right">0.0%</td>
<td align="right">19,953</td>
<td align="right">0.0%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,977,950</td>
<td align="right">99.9%</td>
<td align="right">83,860,932</td>
<td align="right">99.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">856</td>
<td align="right">78.5%</td>
<td align="right">772</td>
<td align="right">76.3%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">235</td>
<td align="right">21.5%</td>
<td align="right">240</td>
<td align="right">23.7%</td>
<td align="right">2.1%</td>
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
<td align="right">139</td>
<td align="right">59.1%</td>
<td align="right">144</td>
<td align="right">60.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">96</td>
<td align="right">40.9%</td>
<td align="right">96</td>
<td align="right">40.0%</td>
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
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
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
<td align="right">14,498,316</td>
<td align="right">100.0%</td>
<td align="right">14,498,316</td>
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
<td align="right">192</td>
<td align="right">100.0%</td>
<td align="right">192</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">48,732</td>
<td align="right">0.0%</td>
<td align="right">41,772</td>
<td align="right">0.0%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,005,922</td>
<td align="right">0.8%</td>
<td align="right">3,255,383</td>
<td align="right">0.8%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">228,568,383</td>
<td align="right">57.4%</td>
<td align="right">230,217,592</td>
<td align="right">57.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">166,891,729</td>
<td align="right">41.9%</td>
<td align="right">167,841,474</td>
<td align="right">41.8%</td>
<td align="right">0.6%</td>
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
<td align="right">1,357</td>
<td align="right">0.0%</td>
<td align="right">24,401</td>
<td align="right">0.8%</td>
<td align="right">1,698.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">61,290</td>
<td align="right">2.1%</td>
<td align="right">149,179</td>
<td align="right">4.6%</td>
<td align="right">143.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">29,246</td>
<td align="right">1.0%</td>
<td align="right">47,322</td>
<td align="right">1.5%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">16,985</td>
<td align="right">0.6%</td>
<td align="right">21,854</td>
<td align="right">0.7%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">109,665</td>
<td align="right">3.7%</td>
<td align="right">127,053</td>
<td align="right">3.9%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">645,475</td>
<td align="right">21.6%</td>
<td align="right">674,669</td>
<td align="right">20.8%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,106,252</td>
<td align="right">70.5%</td>
<td align="right">2,174,866</td>
<td align="right">67.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14,850</td>
<td align="right">0.5%</td>
<td align="right">14,850</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,408</td>
<td align="right">0.0%</td>
<td align="right">1,408</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">953</td>
<td align="right">0.0%</td>
<td align="right">953</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">15,979</td>
<td align="right">32.6%</td>
<td align="right">11,063</td>
<td align="right">26.4%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">12,084</td>
<td align="right">24.7%</td>
<td align="right">8,890</td>
<td align="right">21.2%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">232</td>
<td align="right">0.5%</td>
<td align="right">171</td>
<td align="right">0.4%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">232</td>
<td align="right">0.5%</td>
<td align="right">171</td>
<td align="right">0.4%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,706</td>
<td align="right">13.7%</td>
<td align="right">7,917</td>
<td align="right">18.9%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">7,488</td>
<td align="right">15.3%</td>
<td align="right">7,488</td>
<td align="right">17.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,862</td>
<td align="right">9.9%</td>
<td align="right">4,862</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">566</td>
<td align="right">1.2%</td>
<td align="right">566</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">383</td>
<td align="right">0.8%</td>
<td align="right">383</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">256</td>
<td align="right">0.5%</td>
<td align="right">256</td>
<td align="right">0.6%</td>
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
<td align="right">2,515</td>
<td align="right">0.0%</td>
<td align="right">2,536</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">18,296,015</td>
<td align="right">20.7%</td>
<td align="right">18,296,036</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">47,618,476</td>
<td align="right">54.0%</td>
<td align="right">47,618,497</td>
<td align="right">54.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">47,618,476</td>
<td align="right">54.0%</td>
<td align="right">47,618,497</td>
<td align="right">54.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,632,612</td>
<td align="right">46.0%</td>
<td align="right">40,632,612</td>
<td align="right">46.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">29,322,461</td>
<td align="right">33.2%</td>
<td align="right">29,322,461</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">29,321,153</td>
<td align="right">33.2%</td>
<td align="right">29,321,153</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,304</td>
<td align="right">0.0%</td>
<td align="right">1,304</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">4,356</td>
<td align="right">0.0%</td>
<td align="right">4,356</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">11,546</td>
<td align="right">0.0%</td>
<td align="right">11,546</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">29,298,304</td>
<td align="right">33.2%</td>
<td align="right">29,298,304</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">55,508,108</td>
<td align="right">62.9%</td>
<td align="right">55,508,108</td>
<td align="right">62.9%</td>
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
<td align="right">6,479</td>
<td align="right"></td>
<td align="right">6,347</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">104,276</td>
<td align="right">0.0%</td>
<td align="right">102,540</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">55,481</td>
<td align="right"></td>
<td align="right">56,234</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">18,766,780</td>
<td align="right">0.9%</td>
<td align="right">18,898,941</td>
<td align="right">0.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">172,549,568</td>
<td align="right">8.2%</td>
<td align="right">173,428,435</td>
<td align="right">8.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">65,753,286</td>
<td align="right">2.6%</td>
<td align="right">66,052,058</td>
<td align="right">2.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">271,117,453</td>
<td align="right">10.6%</td>
<td align="right">272,234,237</td>
<td align="right">10.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,409,555,520</td>
<td align="right">66.6%</td>
<td align="right">1,407,096,283</td>
<td align="right">66.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,553,452,164</td>
<td align="right">61.0%</td>
<td align="right">1,550,750,625</td>
<td align="right">60.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,857</td>
<td align="right"></td>
<td align="right">57,773</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">65,945</td>
<td align="right">0.0%</td>
<td align="right">66,012</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">656,543,215</td>
<td align="right">25.8%</td>
<td align="right">656,126,815</td>
<td align="right">25.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">515,481,563</td>
<td align="right">24.4%</td>
<td align="right">515,388,184</td>
<td align="right">24.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">186,726,780</td>
<td align="right"></td>
<td align="right">186,723,085</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">185,674,570</td>
<td align="right">74.6%</td>
<td align="right">185,672,386</td>
<td align="right">74.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">46,021,950</td>
<td align="right"></td>
<td align="right">46,022,126</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">185,504,349</td>
<td align="right">74.5%</td>
<td align="right">185,503,834</td>
<td align="right">74.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">123,383,776</td>
<td align="right"></td>
<td align="right">123,383,658</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">63,230,573</td>
<td align="right">25.4%</td>
<td align="right">63,230,549</td>
<td align="right">25.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">63,232,684</td>
<td align="right"></td>
<td align="right">63,232,660</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">19,380</td>
<td align="right"></td>
<td align="right">19,380</td>
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
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">11,969</td>
<td align="right">25,100</td>
<td align="right">493,192,526</td>
<td align="right">11,969</td>
<td align="right">25,098</td>
<td align="right">493,221,795</td>
</tr>
<tr>
<td align="right">2</td>
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
<td align="right">93</td>
<td align="right">0.7%</td>
<td align="right">25</td>
<td align="right">0.2%</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">4,265</td>
<td align="right">32.3%</td>
<td align="right">2,039</td>
<td align="right">19.4%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">288</td>
<td align="right">2.2%</td>
<td align="right">202</td>
<td align="right">1.9%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">13,199</td>
<td align="right"></td>
<td align="right">10,530</td>
<td align="right"></td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">9,648</td>
<td align="right">73.1%</td>
<td align="right">8,906</td>
<td align="right">84.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">8,934</td>
<td align="right">67.7%</td>
<td align="right">8,491</td>
<td align="right">80.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">69,374,003</td>
<td align="right"></td>
<td align="right">67,914,203</td>
<td align="right"></td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,894,556,599</td>
<td align="right">4,172.4%</td>
<td align="right">2,885,276,150</td>
<td align="right">4,248.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">283</td>
<td align="right">2.7%</td>
<td align="right">283 / 0 !!</td>
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
<td align="right">4,265</td>
<td align="right"></td>
<td align="right">2,039</td>
<td align="right"></td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">4,265</td>
<td align="right">100.0%</td>
<td align="right">2,039</td>
<td align="right">100.0%</td>
<td align="right">-52.2%</td>
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
<td align="right">468</td>
<td align="right">11.0%</td>
<td align="right">188</td>
<td align="right">9.2%</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">579</td>
<td align="right">13.6%</td>
<td align="right">342</td>
<td align="right">16.8%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,273</td>
<td align="right">29.8%</td>
<td align="right">501</td>
<td align="right">24.6%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,110</td>
<td align="right">26.0%</td>
<td align="right">505</td>
<td align="right">24.8%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">571</td>
<td align="right">13.4%</td>
<td align="right">281</td>
<td align="right">13.8%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">264</td>
<td align="right">6.2%</td>
<td align="right">134</td>
<td align="right">6.6%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">88</td>
<td align="right">4.3%</td>
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
<td align="right">275</td>
<td align="right">6.4%</td>
<td align="right">82</td>
<td align="right">4.0%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">621</td>
<td align="right">14.6%</td>
<td align="right">318</td>
<td align="right">15.6%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">470</td>
<td align="right">11.0%</td>
<td align="right">303</td>
<td align="right">14.9%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,821</td>
<td align="right">42.7%</td>
<td align="right">771</td>
<td align="right">37.8%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">614</td>
<td align="right">14.4%</td>
<td align="right">213</td>
<td align="right">10.4%</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">355</td>
<td align="right">8.3%</td>
<td align="right">197</td>
<td align="right">9.7%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">109</td>
<td align="right">2.6%</td>
<td align="right">155</td>
<td align="right">7.6%</td>
<td align="right">42.2%</td>
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
<td align="left">_SWAP</td>
<td align="right">996</td>
<td align="right">24</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">328</td>
<td align="right">56</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">328</td>
<td align="right">56</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,770</td>
<td align="right">3,192</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">253</td>
<td align="right">105</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">44</td>
<td align="right">32</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">44</td>
<td align="right">32</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">44,768</td>
<td align="right">36,808</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">44,768</td>
<td align="right">36,808</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">44,768</td>
<td align="right">36,808</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,480,438</td>
<td align="right">1,338,737</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">85,484</td>
<td align="right">80,615</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">83,265</td>
<td align="right">79,019</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,385,444</td>
<td align="right">1,333,551</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">17,813,872</td>
<td align="right">17,157,455</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">133,466</td>
<td align="right">129,367</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,370,946</td>
<td align="right">1,333,551</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">126,623</td>
<td align="right">129,367</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">69,374,003</td>
<td align="right">67,914,203</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">67,988,306</td>
<td align="right">66,580,547</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">5,218,088</td>
<td align="right">5,116,318</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">5,218,088</td>
<td align="right">5,116,318</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">39,076,344</td>
<td align="right">38,339,725</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">88,231,102</td>
<td align="right">86,691,764</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,617,143</td>
<td align="right">4,549,407</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,617,143</td>
<td align="right">4,549,407</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,570,361</td>
<td align="right">4,503,837</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">756,259</td>
<td align="right">745,916</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">13,079,709</td>
<td align="right">13,255,679</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">49,815,837</td>
<td align="right">49,175,137</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">653,360</td>
<td align="right">646,097</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,233,876</td>
<td align="right">5,176,137</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">652,909</td>
<td align="right">646,097</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">98,749,924</td>
<td align="right">99,426,453</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,594,039</td>
<td align="right">4,563,260</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,424,300</td>
<td align="right">1,415,539</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">5,139,191</td>
<td align="right">5,109,997</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">17,462,316</td>
<td align="right">17,557,600</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,523,752</td>
<td align="right">4,500,708</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">10,631,279</td>
<td align="right">10,585,191</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">10,631,279</td>
<td align="right">10,585,191</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">18,857,099</td>
<td align="right">18,777,561</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">18,974,362</td>
<td align="right">18,897,201</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">16,708,052</td>
<td align="right">16,768,637</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">9,135,142</td>
<td align="right">9,104,046</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">24,467,782</td>
<td align="right">24,385,356</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">30,716,846</td>
<td align="right">30,622,819</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">81,932,195</td>
<td align="right">81,689,582</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">718,957</td>
<td align="right">716,845</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,185,501</td>
<td align="right">5,171,606</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">39,713,430</td>
<td align="right">39,609,909</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">9,126,510</td>
<td align="right">9,104,046</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">9,126,502</td>
<td align="right">9,104,046</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">10,004,939</td>
<td align="right">9,980,368</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,699,830</td>
<td align="right">30,626,011</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">38,367,463</td>
<td align="right">38,277,129</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">64,156,986</td>
<td align="right">64,008,362</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">8,509,999</td>
<td align="right">8,490,297</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">70,712,514</td>
<td align="right">70,550,777</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,471,965</td>
<td align="right">8,453,489</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">38,499,078</td>
<td align="right">38,416,276</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">9,890,322</td>
<td align="right">9,870,165</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">20,368,288</td>
<td align="right">20,327,772</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">21,557,198</td>
<td align="right">21,514,987</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">45,778,347</td>
<td align="right">45,690,458</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,571,332</td>
<td align="right">4,563,204</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">73,125,422</td>
<td align="right">73,003,807</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">72,993,521</td>
<td align="right">72,875,593</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">136,624,666</td>
<td align="right">136,842,932</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">8,503,614</td>
<td align="right">8,490,297</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">41,225,109</td>
<td align="right">41,163,889</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">17,588,918</td>
<td align="right">17,563,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">18,299,136</td>
<td align="right">18,273,210</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">17,689,510</td>
<td align="right">17,664,458</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">45,259,349</td>
<td align="right">45,199,251</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">41,331,355</td>
<td align="right">41,277,165</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">41,330,860</td>
<td align="right">41,277,165</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">286,746,342</td>
<td align="right">286,388,482</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">59,611,024</td>
<td align="right">59,537,260</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">56,693,833</td>
<td align="right">56,625,219</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">17,543,202</td>
<td align="right">17,522,206</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">13,064,060</td>
<td align="right">13,048,834</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">9,172,184</td>
<td align="right">9,161,516</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">14,358,389</td>
<td align="right">14,341,720</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">79,099</td>
<td align="right">79,019</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">95,411,921</td>
<td align="right">95,316,989</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">8,483,524</td>
<td align="right">8,475,396</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">30,001,758</td>
<td align="right">29,973,498</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">107,498,187</td>
<td align="right">107,397,883</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">9,192,712</td>
<td align="right">9,184,504</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,413,906</td>
<td align="right">1,412,862</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,413,906</td>
<td align="right">1,412,862</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">706,953</td>
<td align="right">706,431</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">9,109,997</td>
<td align="right">9,104,046</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">8,458,846</td>
<td align="right">8,453,489</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">9,109,554</td>
<td align="right">9,104,046</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">17,633,749</td>
<td align="right">17,623,087</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">29,918,193</td>
<td align="right">29,900,805</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">319,355,829</td>
<td align="right">319,516,153</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">13,064,640</td>
<td align="right">13,058,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,370,726</td>
<td align="right">25,358,995</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">34,396,160</td>
<td align="right">34,380,956</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">14,478,986</td>
<td align="right">14,473,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">8,460,093</td>
<td align="right">8,459,604</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">8,460,093</td>
<td align="right">8,459,604</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">69,002</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">16,951</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">16,056</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">16,056</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">12,797</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">12,785</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,785</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">12,785</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,785</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">12,785</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">6,385</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">4,613</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,613</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,704</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,315</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">2,310</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2,310</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">1,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,764</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,764</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">1,764</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">945</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">945</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">936</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">924</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">924</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">924</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">924</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">924</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">474</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">462</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">462</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">24</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">12</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">12</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">4</td>
<td align="right"></td>
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
<td align="right">42</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">42</td>
<td align="right"></td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-12
