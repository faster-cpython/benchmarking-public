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
<td align="right">770,461</td>
<td align="right">10,425,772</td>
<td align="right">1,253.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">52,829</td>
<td align="right">338,565</td>
<td align="right">540.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,763</td>
<td align="right">389,282</td>
<td align="right">442.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,595</td>
<td align="right">8,941</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">607,169</td>
<td align="right">1,389,659</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">178,804</td>
<td align="right">397,233</td>
<td align="right">122.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">539,432</td>
<td align="right">1,194,422</td>
<td align="right">121.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">71,104</td>
<td align="right">147,558</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">106,528</td>
<td align="right">211,718</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,347,333</td>
<td align="right">2,675,886</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">30,825</td>
<td align="right">1,679</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,729</td>
<td align="right">14,629</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,498,073</td>
<td align="right">2,732,928</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,314,881</td>
<td align="right">2,264,099</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,323,005</td>
<td align="right">10,572,981</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">237</td>
<td align="right">394</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,290,605</td>
<td align="right">6,622,436</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,067,019</td>
<td align="right">12,255,442</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,648</td>
<td align="right">100,792</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,805,111</td>
<td align="right">4,186,027</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,808,389</td>
<td align="right">4,136,843</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,779,393</td>
<td align="right">2,570,973</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,892,574</td>
<td align="right">4,088,635</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,179,441</td>
<td align="right">11,392,035</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,196,337</td>
<td align="right">1,622,967</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,054,440</td>
<td align="right">1,426,376</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">995,240</td>
<td align="right">1,336,471</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,281,796</td>
<td align="right">1,653,126</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,521,897</td>
<td align="right">3,177,201</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,863,876</td>
<td align="right">28,566,805</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7,373</td>
<td align="right">9,212</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,122,738</td>
<td align="right">3,840,769</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,425,815</td>
<td align="right">43,401,970</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,203</td>
<td align="right">1,455</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,537,171</td>
<td align="right">25,993,015</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,342</td>
<td align="right">8,858</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,679,299</td>
<td align="right">30,763,578</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,602,381</td>
<td align="right">1,911,952</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80,708,246</td>
<td align="right">96,140,169</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,190</td>
<td align="right">3,742</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,946,054</td>
<td align="right">2,281,105</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,124,903</td>
<td align="right">1,317,586</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">397,181</td>
<td align="right">461,688</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,457,631</td>
<td align="right">78,339,644</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,321,493</td>
<td align="right">3,796,455</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,667,487</td>
<td align="right">15,536,596</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,280</td>
<td align="right">20,678</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,507,144</td>
<td align="right">18,656,082</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,685,736</td>
<td align="right">13,188,263</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,923,568</td>
<td align="right">12,256,743</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">529</td>
<td align="right">591</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,204,172</td>
<td align="right">21,440,900</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">473,147,955</td>
<td align="right">528,049,501</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">139,059,095</td>
<td align="right">154,883,938</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">158,370,328</td>
<td align="right">175,626,052</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,217,045</td>
<td align="right">2,458,396</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">10,374,620</td>
<td align="right">11,494,266</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,027,262</td>
<td align="right">26,585,572</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,451,521</td>
<td align="right">55,790,892</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">71,204,565</td>
<td align="right">78,690,890</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">32,752,476</td>
<td align="right">36,129,713</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,643,838</td>
<td align="right">20,561,753</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">137,046,395</td>
<td align="right">151,106,101</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,960,017</td>
<td align="right">4,364,962</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,292,162</td>
<td align="right">15,692,009</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,087,780</td>
<td align="right">149,194,644</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,262,813</td>
<td align="right">36,407,665</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">5,311,333</td>
<td align="right">5,806,213</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,872,812</td>
<td align="right">49,045,815</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,975,360</td>
<td align="right">28,265,996</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">34,618,074</td>
<td align="right">37,614,640</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,928,319</td>
<td align="right">33,571,791</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,634,778</td>
<td align="right">105,945,393</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">35,528,311</td>
<td align="right">38,527,187</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,186,655</td>
<td align="right">50,024,369</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,336,458</td>
<td align="right">17,669,196</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">34,907,880</td>
<td align="right">37,642,655</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,263,659</td>
<td align="right">6,744,142</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,991,463</td>
<td align="right">4,291,087</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,527,040</td>
<td align="right">16,653,103</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">9,688,544</td>
<td align="right">10,354,662</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">74,105</td>
<td align="right">78,653</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,053,391</td>
<td align="right">41,433,933</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">8,503,993</td>
<td align="right">9,015,529</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,870,650</td>
<td align="right">4,102,483</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">17,754,558</td>
<td align="right">18,809,253</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,346,269</td>
<td align="right">119,879,579</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,558,021</td>
<td align="right">42,830,067</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">468,031</td>
<td align="right">493,514</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,289,409</td>
<td align="right">12,927,495</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,210,416</td>
<td align="right">6,525,330</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,607,752</td>
<td align="right">5,888,609</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,749,059</td>
<td align="right">6,035,360</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,822,120</td>
<td align="right">17,586,138</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,838,476</td>
<td align="right">5,052,122</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,048,862</td>
<td align="right">16,704,040</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,246,413</td>
<td align="right">7,541,203</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">11,370,517</td>
<td align="right">11,819,057</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,621,458</td>
<td align="right">1,684,025</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,950,393</td>
<td align="right">15,491,077</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,873,281</td>
<td align="right">17,474,962</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">62</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">622,558</td>
<td align="right">642,628</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25,660,891</td>
<td align="right">26,459,274</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">43,042,437</td>
<td align="right">44,371,978</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,063,552</td>
<td align="right">2,124,853</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,057,439</td>
<td align="right">1,028,357</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,255,751</td>
<td align="right">1,287,928</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,861,577</td>
<td align="right">3,958,564</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,741,576</td>
<td align="right">24,319,149</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,583</td>
<td align="right">2,645</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,447,641</td>
<td align="right">19,877,102</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">123,682</td>
<td align="right">126,223</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,837,932</td>
<td align="right">10,005,114</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,603,370</td>
<td align="right">2,644,178</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">13,254,055</td>
<td align="right">13,454,260</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,105,067</td>
<td align="right">11,256,051</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,307,282</td>
<td align="right">19,566,459</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">385,778</td>
<td align="right">389,902</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">39,809</td>
<td align="right">40,226</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">88,122</td>
<td align="right">89,010</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">176,758</td>
<td align="right">178,534</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">176,760</td>
<td align="right">178,536</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,957</td>
<td align="right">2,981</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,890</td>
<td align="right">8,961</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,065</td>
<td align="right">18,185</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,082,852</td>
<td align="right">182,115,519</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,133</td>
<td align="right">172,066</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,171</td>
<td align="right">24,271</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,475,400</td>
<td align="right">10,517,825</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,443</td>
<td align="right">1,447</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,663,951</td>
<td align="right">17,707,095</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,610,756</td>
<td align="right">97,823,390</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,310</td>
<td align="right">165,625</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,963,015</td>
<td align="right">1,966,236</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,321,668</td>
<td align="right">1,323,182</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,726,908</td>
<td align="right">3,730,896</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,864</td>
<td align="right">175,035</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,462,310</td>
<td align="right">4,465,066</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,002</td>
<td align="right">17,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,236</td>
<td align="right">1,244,521</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,079</td>
<td align="right">83,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">654,996</td>
<td align="right">655,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">654,996</td>
<td align="right">655,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">654,996</td>
<td align="right">655,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,551</td>
<td align="right">642,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,898</td>
<td align="right">1,028,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,892</td>
<td align="right">745,847</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,555</td>
<td align="right">427,530</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,300</td>
<td align="right">746,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,491</td>
<td align="right">21,976,744</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,608</td>
<td align="right">942,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">133,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
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
<td align="right">23,721,770</td>
<td align="right">62.2%</td>
<td align="right">24,299,055</td>
<td align="right">62.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,385,718</td>
<td align="right">37.7%</td>
<td align="right">14,384,696</td>
<td align="right">37.2%</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
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
<td align="right">18,536</td>
<td align="right">100.0%</td>
<td align="right">18,783</td>
<td align="right">100.0%</td>
<td align="right">1.3%</td>
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
<td align="left">add different types</td>
<td align="right">954</td>
<td align="right">5.1%</td>
<td align="right">1,006</td>
<td align="right">5.4%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,329</td>
<td align="right">12.6%</td>
<td align="right">2,455</td>
<td align="right">13.1%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">358</td>
<td align="right">1.9%</td>
<td align="right">346</td>
<td align="right">1.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">94</td>
<td align="right">0.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">678</td>
<td align="right">3.7%</td>
<td align="right">695</td>
<td align="right">3.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">694</td>
<td align="right">3.7%</td>
<td align="right">703</td>
<td align="right">3.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">2,644</td>
<td align="right">14.3%</td>
<td align="right">2,674</td>
<td align="right">14.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">207</td>
<td align="right">1.1%</td>
<td align="right">209</td>
<td align="right">1.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">567</td>
<td align="right">3.1%</td>
<td align="right">562</td>
<td align="right">3.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.3%</td>
<td align="right">989</td>
<td align="right">5.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,878</td>
<td align="right">15.5%</td>
<td align="right">2,891</td>
<td align="right">15.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,287</td>
<td align="right">6.9%</td>
<td align="right">1,292</td>
<td align="right">6.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,212</td>
<td align="right">6.5%</td>
<td align="right">1,210</td>
<td align="right">6.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.9%</td>
<td align="right">1,087</td>
<td align="right">5.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">2,225</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
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
<td align="right">7,342</td>
<td align="right">100.0%</td>
<td align="right">8,858</td>
<td align="right">100.0%</td>
<td align="right">20.6%</td>
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
<td align="right">2,803,751</td>
<td align="right">7.9%</td>
<td align="right">4,131,859</td>
<td align="right">11.2%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,205</td>
<td align="right">0.0%</td>
<td align="right">10,757</td>
<td align="right">0.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,730,918</td>
<td align="right">92.1%</td>
<td align="right">32,743,960</td>
<td align="right">88.8%</td>
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
<td align="right">3,860</td>
<td align="right">80.2%</td>
<td align="right">4,196</td>
<td align="right">80.9%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">950</td>
<td align="right">19.8%</td>
<td align="right">988</td>
<td align="right">19.1%</td>
<td align="right">4.0%</td>
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
<td align="right">338</td>
<td align="right">8.8%</td>
<td align="right">422</td>
<td align="right">10.1%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,418</td>
<td align="right">62.6%</td>
<td align="right">2,662</td>
<td align="right">63.4%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">143</td>
<td align="right">3.7%</td>
<td align="right">148</td>
<td align="right">3.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">689</td>
<td align="right">17.8%</td>
<td align="right">693</td>
<td align="right">16.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">271</td>
<td align="right">7.0%</td>
<td align="right">270</td>
<td align="right">6.4%</td>
<td align="right">-0.4%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,221</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,237,653</td>
<td align="right">7.2%</td>
<td align="right">23,624,050</td>
<td align="right">7.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,431</td>
<td align="right">0.0%</td>
<td align="right">8,487</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">297,271,767</td>
<td align="right">92.7%</td>
<td align="right">297,169,395</td>
<td align="right">92.6%</td>
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
<td align="right">455,032</td>
<td align="right">100.0%</td>
<td align="right">462,411</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
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
<td align="left">init not inline values</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
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
<td align="right">399</td>
<td align="right">9.4%</td>
<td align="right">401</td>
<td align="right">9.4%</td>
<td align="right">0.5%</td>
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
<td align="right">374,747</td>
<td align="right">0.5%</td>
<td align="right">409,685</td>
<td align="right">0.6%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,272,623</td>
<td align="right">27.3%</td>
<td align="right">19,530,540</td>
<td align="right">27.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,016,733</td>
<td align="right">72.2%</td>
<td align="right">51,025,183</td>
<td align="right">71.9%</td>
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
<td align="right">8,199</td>
<td align="right">19.7%</td>
<td align="right">8,845</td>
<td align="right">20.3%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">33,475</td>
<td align="right">80.3%</td>
<td align="right">34,747</td>
<td align="right">79.7%</td>
<td align="right">3.8%</td>
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
<td align="right">194</td>
<td align="right">0.6%</td>
<td align="right">169</td>
<td align="right">0.5%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">12,852</td>
<td align="right">38.4%</td>
<td align="right">14,105</td>
<td align="right">40.6%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,129</td>
<td align="right">9.3%</td>
<td align="right">3,164</td>
<td align="right">9.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,217</td>
<td align="right">12.6%</td>
<td align="right">4,238</td>
<td align="right">12.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,081</td>
<td align="right">15.2%</td>
<td align="right">5,069</td>
<td align="right">14.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">22.3%</td>
<td align="right">7,480</td>
<td align="right">21.5%</td>
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
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
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
<td align="right">1,344,029</td>
<td align="right">5.4%</td>
<td align="right">2,672,418</td>
<td align="right">10.2%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,465</td>
<td align="right">94.6%</td>
<td align="right">23,499,047</td>
<td align="right">89.8%</td>
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
<td align="right">3,182</td>
<td align="right">100.0%</td>
<td align="right">3,346</td>
<td align="right">100.0%</td>
<td align="right">5.2%</td>
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
<td align="left">tuple</td>
<td align="right">1,392</td>
<td align="right">43.7%</td>
<td align="right">1,472</td>
<td align="right">44.0%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">285</td>
<td align="right">9.0%</td>
<td align="right">299</td>
<td align="right">8.9%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,371</td>
<td align="right">43.1%</td>
<td align="right">1,438</td>
<td align="right">43.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">134</td>
<td align="right">4.2%</td>
<td align="right">137</td>
<td align="right">4.1%</td>
<td align="right">2.2%</td>
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
<td align="right">87,518</td>
<td align="right">0.2%</td>
<td align="right">203,286</td>
<td align="right">0.4%</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,301,746</td>
<td align="right">44.4%</td>
<td align="right">24,928,220</td>
<td align="right">48.8%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,522,593</td>
<td align="right">55.3%</td>
<td align="right">25,970,846</td>
<td align="right">50.8%</td>
<td align="right">20.7%</td>
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
<td align="right">2,311</td>
<td align="right">14.3%</td>
<td align="right">4,473</td>
<td align="right">17.3%</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,855</td>
<td align="right">85.7%</td>
<td align="right">21,452</td>
<td align="right">82.7%</td>
<td align="right">54.8%</td>
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
<td align="left">dict items</td>
<td align="right">6,439</td>
<td align="right">46.5%</td>
<td align="right">13,392</td>
<td align="right">62.4%</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">422</td>
<td align="right">3.0%</td>
<td align="right">558</td>
<td align="right">2.6%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,111</td>
<td align="right">8.0%</td>
<td align="right">1,335</td>
<td align="right">6.2%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">693</td>
<td align="right">5.0%</td>
<td align="right">758</td>
<td align="right">3.5%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">350</td>
<td align="right">2.5%</td>
<td align="right">382</td>
<td align="right">1.8%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,136</td>
<td align="right">15.4%</td>
<td align="right">2,297</td>
<td align="right">10.7%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">239</td>
<td align="right">1.7%</td>
<td align="right">243</td>
<td align="right">1.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,412</td>
<td align="right">17.4%</td>
<td align="right">2,434</td>
<td align="right">11.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.2%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.2%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right">27,099,571</td>
<td align="right">8.8%</td>
<td align="right">32,350,788</td>
<td align="right">10.3%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">50,394,591</td>
<td align="right">16.4%</td>
<td align="right">55,731,688</td>
<td align="right">17.7%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">228,932,251</td>
<td align="right">74.7%</td>
<td align="right">226,766,252</td>
<td align="right">72.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">523,360</td>
<td align="right">92.5%</td>
<td align="right">623,282</td>
<td align="right">93.4%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,592</td>
<td align="right">7.5%</td>
<td align="right">44,028</td>
<td align="right">6.6%</td>
<td align="right">3.4%</td>
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
<td align="left">module attr not found</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,223</td>
<td align="right">14.6%</td>
<td align="right">6,733</td>
<td align="right">15.3%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">142</td>
<td align="right">0.3%</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,960</td>
<td align="right">46.9%</td>
<td align="right">20,588</td>
<td align="right">46.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,007</td>
<td align="right">7.1%</td>
<td align="right">3,094</td>
<td align="right">7.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,847</td>
<td align="right">9.0%</td>
<td align="right">3,949</td>
<td align="right">9.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">244</td>
<td align="right">0.6%</td>
<td align="right">250</td>
<td align="right">0.6%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,048</td>
<td align="right">7.2%</td>
<td align="right">3,096</td>
<td align="right">7.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,740</td>
<td align="right">6.4%</td>
<td align="right">2,776</td>
<td align="right">6.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.5%</td>
<td align="right">2,366</td>
<td align="right">5.4%</td>
<td align="right">0.3%</td>
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
<td align="right">208,775,577</td>
<td align="right">100.0%</td>
<td align="right">229,256,648</td>
<td align="right">100.0%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,527</td>
<td align="right">0.0%</td>
<td align="right">4,594</td>
<td align="right">0.0%</td>
<td align="right">1.5%</td>
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
<td align="right">13,586</td>
<td align="right">100.0%</td>
<td align="right">13,639</td>
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
<td align="right">32</td>
<td align="right">0.0%</td>
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
<td align="right">2,265,780</td>
<td align="right">100.0%</td>
<td align="right">2,265,782</td>
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
<td align="right">731,589</td>
<td align="right">72.0%</td>
<td align="right">731,608</td>
<td align="right">72.0%</td>
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
<td align="right">310,975</td>
<td align="right">3.7%</td>
<td align="right">1,579,119</td>
<td align="right">17.4%</td>
<td align="right">407.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,930,941</td>
<td align="right">94.2%</td>
<td align="right">7,324,422</td>
<td align="right">80.7%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,567</td>
<td align="right">2.1%</td>
<td align="right">173,728</td>
<td align="right">1.9%</td>
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
<td align="right">6,101</td>
<td align="right">86.4%</td>
<td align="right">30,045</td>
<td align="right">96.9%</td>
<td align="right">392.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">962</td>
<td align="right">13.6%</td>
<td align="right">972</td>
<td align="right">3.1%</td>
<td align="right">1.0%</td>
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
<td align="right">284</td>
<td align="right">29.5%</td>
<td align="right">294</td>
<td align="right">30.2%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.8%</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">157</td>
<td align="right">16.3%</td>
<td align="right">157</td>
<td align="right">16.2%</td>
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
<td align="right">529</td>
<td align="right">100.0%</td>
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">11.7%</td>
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
<td align="right">65,108</td>
<td align="right">0.4%</td>
<td align="right">99,247</td>
<td align="right">0.6%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,994</td>
<td align="right">99.6%</td>
<td align="right">17,736,899</td>
<td align="right">99.4%</td>
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
<td align="right">576</td>
<td align="right">37.4%</td>
<td align="right">578</td>
<td align="right">37.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">964</td>
<td align="right">62.6%</td>
<td align="right">967</td>
<td align="right">62.6%</td>
<td align="right">0.3%</td>
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
<td align="right">964</td>
<td align="right">100.0%</td>
<td align="right">967</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">341,921</td>
<td align="right">0.2%</td>
<td align="right">386,420</td>
<td align="right">0.2%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,820,744</td>
<td align="right">6.0%</td>
<td align="right">9,985,976</td>
<td align="right">6.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">152,889,334</td>
<td align="right">93.8%</td>
<td align="right">153,410,356</td>
<td align="right">93.7%</td>
<td align="right">0.3%</td>
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
<td align="right">9,568</td>
<td align="right">41.4%</td>
<td align="right">11,505</td>
<td align="right">44.4%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,547</td>
<td align="right">58.6%</td>
<td align="right">14,406</td>
<td align="right">55.6%</td>
<td align="right">6.3%</td>
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
<td align="right">1,181</td>
<td align="right">12.3%</td>
<td align="right">1,816</td>
<td align="right">15.8%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,817</td>
<td align="right">50.3%</td>
<td align="right">6,022</td>
<td align="right">52.3%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">651</td>
<td align="right">6.8%</td>
<td align="right">724</td>
<td align="right">6.3%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,239</td>
<td align="right">12.9%</td>
<td align="right">1,262</td>
<td align="right">11.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">711</td>
<td align="right">7.4%</td>
<td align="right">712</td>
<td align="right">6.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">9.2%</td>
<td align="right">883</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.9%</td>
<td align="right">84</td>
<td align="right">0.7%</td>
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
<td align="right">6,205</td>
<td align="right">0.0%</td>
<td align="right">6,262</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,524,494</td>
<td align="right">100.0%</td>
<td align="right">83,730,147</td>
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
<td align="left">Failure</td>
<td align="right">293</td>
<td align="right">10.9%</td>
<td align="right">295</td>
<td align="right">10.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">89.1%</td>
<td align="right">2,404</td>
<td align="right">89.1%</td>
<td align="right">0.5%</td>
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
<td align="right">250</td>
<td align="right">85.3%</td>
<td align="right">252</td>
<td align="right">85.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.7%</td>
<td align="right">43</td>
<td align="right">14.6%</td>
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
<td align="right">51,482,582</td>
<td align="right">1.7%</td>
<td align="right">58,584,875</td>
<td align="right">1.8%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,014,344,387</td>
<td align="right">33.9%</td>
<td align="right">1,126,315,191</td>
<td align="right">34.5%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">129,603,312</td>
<td align="right">4.3%</td>
<td align="right">143,095,656</td>
<td align="right">4.4%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,800,897,806</td>
<td align="right">60.1%</td>
<td align="right">1,940,660,412</td>
<td align="right">59.4%</td>
<td align="right">7.8%</td>
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
<td align="right">1,344,029</td>
<td align="right">1.0%</td>
<td align="right">2,672,418</td>
<td align="right">1.9%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,108</td>
<td align="right">0.1%</td>
<td align="right">99,247</td>
<td align="right">0.1%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,803,751</td>
<td align="right">2.2%</td>
<td align="right">4,131,859</td>
<td align="right">2.9%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,522,593</td>
<td align="right">16.6%</td>
<td align="right">25,970,846</td>
<td align="right">18.2%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,394,591</td>
<td align="right">38.9%</td>
<td align="right">55,731,688</td>
<td align="right">39.0%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,721,770</td>
<td align="right">18.3%</td>
<td align="right">24,299,055</td>
<td align="right">17.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,820,744</td>
<td align="right">7.6%</td>
<td align="right">9,985,976</td>
<td align="right">7.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,272,623</td>
<td align="right">14.9%</td>
<td align="right">19,530,540</td>
<td align="right">13.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,567</td>
<td align="right">0.1%</td>
<td align="right">173,728</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">268,986</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">310,196</td>
<td align="right">0.6%</td>
<td align="right">1,578,340</td>
<td align="right">2.7%</td>
<td align="right">408.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,656,273</td>
<td align="right">20.7%</td>
<td align="right">14,088,454</td>
<td align="right">24.0%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,428,808</td>
<td align="right">16.4%</td>
<td align="right">9,820,262</td>
<td align="right">16.8%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">373,727</td>
<td align="right">0.7%</td>
<td align="right">408,665</td>
<td align="right">0.7%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,944,529</td>
<td align="right">5.7%</td>
<td align="right">3,128,765</td>
<td align="right">5.3%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,684,686</td>
<td align="right">9.1%</td>
<td align="right">4,953,352</td>
<td align="right">8.5%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,678,149</td>
<td align="right">9.1%</td>
<td align="right">4,921,682</td>
<td align="right">8.4%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,313,787</td>
<td align="right">22.0%</td>
<td align="right">11,357,232</td>
<td align="right">19.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,518</td>
<td align="right">9.9%</td>
<td align="right">5,102,561</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,560</td>
<td align="right">4.1%</td>
<td align="right">2,103,571</td>
<td align="right">3.6%</td>
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
<td align="right">1,008,403</td>
<td align="right">0.5%</td>
<td align="right">950,162</td>
<td align="right">0.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,083,691</td>
<td align="right">19.5%</td>
<td align="right">41,252,037</td>
<td align="right">19.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,378,553</td>
<td align="right">35.8%</td>
<td align="right">75,547,411</td>
<td align="right">35.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,379,338</td>
<td align="right">35.8%</td>
<td align="right">75,548,196</td>
<td align="right">35.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,794,318</td>
<td align="right">46.5%</td>
<td align="right">97,977,808</td>
<td align="right">46.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,794,318</td>
<td align="right">46.5%</td>
<td align="right">97,977,808</td>
<td align="right">46.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,759,716</td>
<td align="right">89.2%</td>
<td align="right">187,924,346</td>
<td align="right">89.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,414,980</td>
<td align="right">10.7%</td>
<td align="right">22,429,612</td>
<td align="right">10.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,625,333</td>
<td align="right">53.5%</td>
<td align="right">112,621,057</td>
<td align="right">53.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,471</td>
<td align="right">8.8%</td>
<td align="right">18,490,724</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,848</td>
<td align="right">4.4%</td>
<td align="right">9,331,927</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">1,013,535</td>
<td align="right"></td>
<td align="right">838,892</td>
<td align="right"></td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,181,293</td>
<td align="right"></td>
<td align="right">2,908,669</td>
<td align="right"></td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,073,594,707</td>
<td align="right">40.8%</td>
<td align="right">1,913,464,305</td>
<td align="right">38.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,135,809,193</td>
<td align="right">36.0%</td>
<td align="right">1,990,550,662</td>
<td align="right">34.0%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,403,097,135</td>
<td align="right">27.6%</td>
<td align="right">1,495,299,244</td>
<td align="right">29.8%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">387,688,953</td>
<td align="right">7.6%</td>
<td align="right">412,271,297</td>
<td align="right">8.2%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">632,705,858</td>
<td align="right">10.7%</td>
<td align="right">669,841,186</td>
<td align="right">11.4%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,169,237</td>
<td align="right"></td>
<td align="right">2,071,257</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,795,389,039</td>
<td align="right">30.2%</td>
<td align="right">1,872,702,537</td>
<td align="right">31.9%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,376,604,687</td>
<td align="right">23.2%</td>
<td align="right">1,329,245,060</td>
<td align="right">22.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">791,762</td>
<td align="right">0.2%</td>
<td align="right">771,056</td>
<td align="right">0.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">142,670,839</td>
<td align="right"></td>
<td align="right">144,701,568</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,216,589,511</td>
<td align="right">23.9%</td>
<td align="right">1,199,929,241</td>
<td align="right">23.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">261,911,713</td>
<td align="right"></td>
<td align="right">263,736,542</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,974,666</td>
<td align="right">45.3%</td>
<td align="right">232,912,460</td>
<td align="right">45.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,622,324</td>
<td align="right"></td>
<td align="right">245,559,877</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">281,671,356</td>
<td align="right">54.7%</td>
<td align="right">281,722,698</td>
<td align="right">54.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,703,258</td>
<td align="right"></td>
<td align="right">281,754,598</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,174,295</td>
<td align="right">45.1%</td>
<td align="right">232,132,795</td>
<td align="right">45.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,056</td>
<td align="right"></td>
<td align="right">866,156</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,609</td>
<td align="right">0.0%</td>
<td align="right">8,609</td>
<td align="right">0.0%</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">407</td>
<td align="right">0.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">99</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">58,961</td>
<td align="right">48.6%</td>
<td align="right">24,594</td>
<td align="right">33.9%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,085</td>
<td align="right">0.9%</td>
<td align="right">545</td>
<td align="right">0.8%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">121,435</td>
<td align="right"></td>
<td align="right">72,617</td>
<td align="right"></td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,348</td>
<td align="right">1.1%</td>
<td align="right">980</td>
<td align="right">1.3%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">59,337</td>
<td align="right">48.9%</td>
<td align="right">44,413</td>
<td align="right">61.2%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">62,474</td>
<td align="right">51.4%</td>
<td align="right">48,023</td>
<td align="right">66.1%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">285,324,689</td>
<td align="right"></td>
<td align="right">228,405,483</td>
<td align="right"></td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,318,504,498</td>
<td align="right">1,513.5%</td>
<td align="right">3,649,036,042</td>
<td align="right">1,597.6%</td>
<td align="right">-15.5%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">55,974</td>
<td align="right">94.9%</td>
<td align="right">23,302</td>
<td align="right">94.7%</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">58,961</td>
<td align="right"></td>
<td align="right">24,594</td>
<td align="right"></td>
<td align="right">-58.3%</td>
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
<td align="right">5,282</td>
<td align="right">9.0%</td>
<td align="right">3,124</td>
<td align="right">12.7%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,679</td>
<td align="right">14.7%</td>
<td align="right">4,150</td>
<td align="right">16.9%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">23,696</td>
<td align="right">40.2%</td>
<td align="right">8,011</td>
<td align="right">32.6%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">14,146</td>
<td align="right">24.0%</td>
<td align="right">5,259</td>
<td align="right">21.4%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,412</td>
<td align="right">10.9%</td>
<td align="right">3,357</td>
<td align="right">13.6%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">746</td>
<td align="right">1.3%</td>
<td align="right">693</td>
<td align="right">2.8%</td>
<td align="right">-7.1%</td>
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
<td align="right">931</td>
<td align="right">1.6%</td>
<td align="right">683</td>
<td align="right">2.8%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,956</td>
<td align="right">11.8%</td>
<td align="right">3,386</td>
<td align="right">13.8%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,624</td>
<td align="right">23.1%</td>
<td align="right">5,429</td>
<td align="right">22.1%</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,142</td>
<td align="right">37.6%</td>
<td align="right">7,819</td>
<td align="right">31.8%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,927</td>
<td align="right">18.5%</td>
<td align="right">5,350</td>
<td align="right">21.8%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,359</td>
<td align="right">2.3%</td>
<td align="right">507</td>
<td align="right">2.1%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">35</td>
<td align="right">0.1%</td>
<td align="right">128</td>
<td align="right">0.5%</td>
<td align="right">265.7%</td>
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
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">145</td>
<td align="right">4,266</td>
<td align="right">2,842.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">145</td>
<td align="right">4,266</td>
<td align="right">2,842.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">145</td>
<td align="right">4,266</td>
<td align="right">2,842.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">637,202</td>
<td align="right">222</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">286,480</td>
<td align="right">744</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">30,690</td>
<td align="right">744</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">673,984</td>
<td align="right">22,683</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">203,629</td>
<td align="right">45,559</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">481,425</td>
<td align="right">113,690</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,301,824</td>
<td align="right">352,727</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">654,264</td>
<td align="right">249,417</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">236,060</td>
<td align="right">97,249</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,196,166</td>
<td align="right">961,344</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,284,888</td>
<td align="right">4,583,239</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,472,982</td>
<td align="right">3,944,147</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,036,151</td>
<td align="right">491,379</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">619,501</td>
<td align="right">305,136</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,857,053</td>
<td align="right">1,924,144</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,791,511</td>
<td align="right">1,924,144</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">756,292</td>
<td align="right">384,825</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">758,093</td>
<td align="right">398,693</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">132,992</td>
<td align="right">70,418</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">131,495</td>
<td align="right">70,308</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,477,148</td>
<td align="right">824,609</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">11,505,283</td>
<td align="right">6,464,646</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,039,642</td>
<td align="right">21,504,713</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,241,580</td>
<td align="right">3,109,137</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,175,336</td>
<td align="right">700,746</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,388,176</td>
<td align="right">6,306,365</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,475,601</td>
<td align="right">980,882</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,066,103</td>
<td align="right">10,995,113</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">532,253</td>
<td align="right">365,126</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,393,964</td>
<td align="right">7,162,880</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,384,212</td>
<td align="right">4,410,499</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">319,942</td>
<td align="right">223,049</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,865,670</td>
<td align="right">25,717,789</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,462,070</td>
<td align="right">3,818,021</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,882,596</td>
<td align="right">2,738,881</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,574,808</td>
<td align="right">10,999,085</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">980,496</td>
<td align="right">700,736</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,877,831</td>
<td align="right">2,782,453</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,426,907</td>
<td align="right">12,891,602</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,239</td>
<td align="right">638,810</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">3,850,818</td>
<td align="right">2,904,260</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">57,529,388</td>
<td align="right">43,434,619</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">913,514</td>
<td align="right">700,736</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">156,874,165</td>
<td align="right">120,524,068</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">11,409,795</td>
<td align="right">8,849,704</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">36,170,292</td>
<td align="right">28,075,109</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,018,056</td>
<td align="right">4,685,177</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,033,429</td>
<td align="right">28,082,188</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">106,215,616</td>
<td align="right">83,232,953</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,027,854</td>
<td align="right">2,373,192</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">491,081</td>
<td align="right">385,896</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">491,081</td>
<td align="right">385,896</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,050,508</td>
<td align="right">14,263,918</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">259,193,754</td>
<td align="right">204,884,238</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,544,429</td>
<td align="right">9,208,815</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">285,324,689</td>
<td align="right">228,405,483</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">77,318,038</td>
<td align="right">62,192,718</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">61,059,575</td>
<td align="right">49,120,663</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">3,473,926</td>
<td align="right">2,807,944</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,450,239</td>
<td align="right">2,814,124</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,059,212</td>
<td align="right">10,680,089</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,703,884</td>
<td align="right">1,394,389</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,432,271</td>
<td align="right">20,842,656</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">19,806,010</td>
<td align="right">16,237,582</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">317,413,875</td>
<td align="right">260,448,775</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">18,500,215</td>
<td align="right">15,240,856</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">53,789,556</td>
<td align="right">44,449,259</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,538,156</td>
<td align="right">2,108,531</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">10,064,436</td>
<td align="right">8,399,395</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">36,398,291</td>
<td align="right">30,590,398</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">21,043,728</td>
<td align="right">17,719,118</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">45,934,167</td>
<td align="right">38,699,556</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">34,407,015</td>
<td align="right">28,991,250</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">36,299,446</td>
<td align="right">30,590,398</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,378,487</td>
<td align="right">17,189,579</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">414,299</td>
<td align="right">350,368</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">13,014,616</td>
<td align="right">11,041,250</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">13,014,616</td>
<td align="right">11,041,250</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">47,110,021</td>
<td align="right">40,194,277</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">17,696</td>
<td align="right">15,168</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,831,059</td>
<td align="right">6,718,513</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,798,012</td>
<td align="right">11,880,865</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,188,149</td>
<td align="right">3,611,968</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,746,487</td>
<td align="right">2,375,213</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">10,429,956</td>
<td align="right">9,047,488</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">402,959,615</td>
<td align="right">350,211,965</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">318,749,205</td>
<td align="right">278,530,675</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">4,204,796</td>
<td align="right">3,693,548</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">18,819,649</td>
<td align="right">16,578,247</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">8,975,249</td>
<td align="right">7,920,871</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">172,553,255</td>
<td align="right">152,376,756</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,030,103</td>
<td align="right">9,783,596</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">31,171,876</td>
<td align="right">27,670,974</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">97,181,985</td>
<td align="right">86,696,555</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,340,632</td>
<td align="right">11,018,567</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">40,029,155</td>
<td align="right">35,780,184</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">34,396,910</td>
<td align="right">30,781,151</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">21,268,650</td>
<td align="right">19,069,580</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">40,852,751</td>
<td align="right">36,770,382</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,793,414</td>
<td align="right">71,880,047</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">10,894,638</td>
<td align="right">9,829,851</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,210,583</td>
<td align="right">7,417,398</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">440,648</td>
<td align="right">398,693</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,864,185</td>
<td align="right">23,423,252</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">29,286,334</td>
<td align="right">26,656,789</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">7,867,509</td>
<td align="right">7,167,146</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">31,918,355</td>
<td align="right">29,101,060</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">45,647,478</td>
<td align="right">41,815,226</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,972,258</td>
<td align="right">5,372,505</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,285,534</td>
<td align="right">15,921,272</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,484,381</td>
<td align="right">1,368,142</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,484,381</td>
<td align="right">1,368,142</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">32,273,824</td>
<td align="right">29,795,156</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">27,801,661</td>
<td align="right">25,699,782</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">15,924,623</td>
<td align="right">14,739,441</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">37,699,964</td>
<td align="right">35,067,283</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,290,624</td>
<td align="right">26,366,864</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">60,847,224</td>
<td align="right">56,729,151</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">20,617,238</td>
<td align="right">19,235,387</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,128,171</td>
<td align="right">45,934,621</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">15,512,023</td>
<td align="right">14,503,918</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,943,145</td>
<td align="right">6,494,805</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">87,642,357</td>
<td align="right">82,320,694</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">48,832,887</td>
<td align="right">45,893,163</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,195,962</td>
<td align="right">13,372,810</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,255,642</td>
<td align="right">18,181,190</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,413,698</td>
<td align="right">13,631,546</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">11,984,853</td>
<td align="right">11,358,659</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">46,243,066</td>
<td align="right">44,221,150</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,983,632</td>
<td align="right">7,640,222</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,983,632</td>
<td align="right">7,640,222</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,358,492</td>
<td align="right">7,043,205</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,850,127</td>
<td align="right">5,626,359</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,785,425</td>
<td align="right">19,489,643</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">7,399,249</td>
<td align="right">7,139,631</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">332,198</td>
<td align="right">343,255</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">7,208,671</td>
<td align="right">6,994,501</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,054,133</td>
<td align="right">22,410,718</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,544,355</td>
<td align="right">7,374,525</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,544,355</td>
<td align="right">7,374,525</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">11,080,050</td>
<td align="right">10,922,190</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,517,959</td>
<td align="right">2,483,688</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,413,215</td>
<td align="right">13,372,486</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,514,501</td>
<td align="right">2,510,742</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">32,089,186</td>
<td align="right">32,043,292</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,670,311</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">885,079</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">782,327</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">480,509</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">334,946</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">334,946</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">317,519</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">294,586</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">294,429</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">286,002</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">286,002</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">76,586</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">64,476</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">58,024</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">31,665</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">24,690</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,001</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,001</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">5,346</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4,535</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">4,105</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">3,084</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,392</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,384</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,384</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,287</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">1,839</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,776</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,776</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,516</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,504</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">1,472</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">889</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">888</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">847</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">552</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">396</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">336</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">286</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">285</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">252</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">189</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">189</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">157</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">157</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">62</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">62</td>
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
<td align="right">11,067</td>
<td align="right">7,262</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,697</td>
<td align="right">5,544</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">364</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">279</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">64</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">4</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">4</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
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
