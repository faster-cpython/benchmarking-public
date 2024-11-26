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
<td align="right">17,415,326</td>
<td align="right">2,160.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">52,829</td>
<td align="right">339,309</td>
<td align="right">542.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,763</td>
<td align="right">389,282</td>
<td align="right">442.5%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">178,804</td>
<td align="right">568,939</td>
<td align="right">218.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,648</td>
<td align="right">186,535</td>
<td align="right">179.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">106,528</td>
<td align="right">293,124</td>
<td align="right">175.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,595</td>
<td align="right">8,941</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,347,333</td>
<td align="right">3,302,989</td>
<td align="right">145.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,498,073</td>
<td align="right">3,589,391</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">607,169</td>
<td align="right">1,389,682</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">539,432</td>
<td align="right">1,195,387</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">71,104</td>
<td align="right">147,634</td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,323,005</td>
<td align="right">12,490,134</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,808,389</td>
<td align="right">5,537,372</td>
<td align="right">97.2%</td>
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
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,314,881</td>
<td align="right">2,425,230</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,067,019</td>
<td align="right">14,845,386</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,779,393</td>
<td align="right">3,019,685</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,054,440</td>
<td align="right">1,765,571</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">237</td>
<td align="right">394</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">995,240</td>
<td align="right">1,605,086</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,805,111</td>
<td align="right">4,480,456</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,281,796</td>
<td align="right">2,024,186</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,290,605</td>
<td align="right">6,622,404</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,179,441</td>
<td align="right">12,488,646</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,196,337</td>
<td align="right">1,789,993</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,892,574</td>
<td align="right">4,289,947</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,122,738</td>
<td align="right">4,529,103</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,425,815</td>
<td align="right">50,715,318</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,537,171</td>
<td align="right">30,132,366</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,602,381</td>
<td align="right">2,229,644</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,521,897</td>
<td align="right">3,436,979</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,217,045</td>
<td align="right">2,840,618</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,457,631</td>
<td align="right">69,012,426</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,863,876</td>
<td align="right">28,616,102</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7,373</td>
<td align="right">9,212</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,679,299</td>
<td align="right">31,406,270</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,124,903</td>
<td align="right">1,363,326</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,203</td>
<td align="right">1,455</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,870,650</td>
<td align="right">4,676,797</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,342</td>
<td align="right">8,858</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">10,374,620</td>
<td align="right">12,512,004</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,685,736</td>
<td align="right">14,083,809</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80,708,246</td>
<td align="right">97,265,533</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,292,162</td>
<td align="right">17,056,810</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,262,813</td>
<td align="right">39,594,202</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,027,262</td>
<td align="right">28,443,303</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,923,568</td>
<td align="right">12,931,126</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,507,144</td>
<td align="right">19,518,872</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,204,172</td>
<td align="right">22,615,735</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,872,812</td>
<td align="right">52,644,896</td>
<td align="right">17.3%</td>
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
<td align="right">2,281,160</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">35,528,311</td>
<td align="right">41,549,976</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,667,487</td>
<td align="right">15,934,450</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,928,319</td>
<td align="right">36,043,279</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">32,752,476</td>
<td align="right">38,149,401</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">397,181</td>
<td align="right">461,696</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">473,147,955</td>
<td align="right">549,495,129</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">137,046,395</td>
<td align="right">158,967,124</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,321,493</td>
<td align="right">3,849,473</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,960,017</td>
<td align="right">4,586,491</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">158,370,328</td>
<td align="right">182,674,568</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,527,040</td>
<td align="right">17,792,538</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,975,360</td>
<td align="right">29,647,332</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">139,059,095</td>
<td align="right">158,623,072</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">9,688,544</td>
<td align="right">10,992,788</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,336,458</td>
<td align="right">18,500,913</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">5,311,333</td>
<td align="right">6,011,420</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,280</td>
<td align="right">20,684</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,186,655</td>
<td align="right">52,223,999</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">71,204,565</td>
<td align="right">80,431,311</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,289,409</td>
<td align="right">13,833,762</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,643,838</td>
<td align="right">20,954,327</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,451,521</td>
<td align="right">56,649,396</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">34,618,074</td>
<td align="right">38,769,857</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">34,907,880</td>
<td align="right">39,031,497</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,087,780</td>
<td align="right">152,136,148</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">529</td>
<td align="right">591</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,991,463</td>
<td align="right">4,438,527</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,634,778</td>
<td align="right">108,285,394</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">123,682</td>
<td align="right">136,922</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">8,503,993</td>
<td align="right">9,402,989</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,346,269</td>
<td align="right">125,190,488</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,558,021</td>
<td align="right">44,699,567</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,053,391</td>
<td align="right">42,398,970</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,307,282</td>
<td align="right">20,918,481</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">17,754,558</td>
<td align="right">19,234,873</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,603,370</td>
<td align="right">2,817,648</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,263,659</td>
<td align="right">6,744,349</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,621,458</td>
<td align="right">1,745,580</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,048,862</td>
<td align="right">17,190,304</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,950,393</td>
<td align="right">15,932,917</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,210,416</td>
<td align="right">6,594,990</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">74,105</td>
<td align="right">78,668</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,822,120</td>
<td align="right">17,827,517</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,607,752</td>
<td align="right">5,941,467</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,063,552</td>
<td align="right">2,186,198</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,741,576</td>
<td align="right">25,130,963</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,838,476</td>
<td align="right">5,104,983</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">468,031</td>
<td align="right">493,352</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,861,577</td>
<td align="right">4,055,427</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,749,059</td>
<td align="right">6,035,534</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25,660,891</td>
<td align="right">26,904,257</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">13,254,055</td>
<td align="right">13,888,998</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,246,413</td>
<td align="right">7,541,293</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">11,370,517</td>
<td align="right">11,832,556</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">43,042,437</td>
<td align="right">44,702,494</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,447,641</td>
<td align="right">20,155,466</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">622,558</td>
<td align="right">642,638</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,873,281</td>
<td align="right">17,372,453</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,057,439</td>
<td align="right">1,028,473</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,255,751</td>
<td align="right">1,287,649</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,583</td>
<td align="right">2,645</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,105,067</td>
<td align="right">11,335,243</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,837,932</td>
<td align="right">9,989,604</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,890</td>
<td align="right">9,006</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">39,809</td>
<td align="right">40,301</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">385,778</td>
<td align="right">389,878</td>
<td align="right">1.1%</td>
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
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,475,400</td>
<td align="right">10,555,379</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,082,852</td>
<td align="right">182,098,347</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,133</td>
<td align="right">172,034</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,663,951</td>
<td align="right">17,574,249</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,957</td>
<td align="right">2,968</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,726,908</td>
<td align="right">3,738,429</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,864</td>
<td align="right">175,315</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,443</td>
<td align="right">1,446</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,963,015</td>
<td align="right">1,966,313</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,002</td>
<td align="right">17,030</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,310</td>
<td align="right">165,553</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,321,668</td>
<td align="right">1,323,177</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,065</td>
<td align="right">18,084</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,171</td>
<td align="right">24,195</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,610,756</td>
<td align="right">97,701,607</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,462,310</td>
<td align="right">4,464,903</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,079</td>
<td align="right">83,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">654,996</td>
<td align="right">655,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">654,996</td>
<td align="right">655,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">654,996</td>
<td align="right">655,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,236</td>
<td align="right">1,244,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,898</td>
<td align="right">1,029,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,551</td>
<td align="right">642,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,892</td>
<td align="right">745,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,555</td>
<td align="right">427,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,608</td>
<td align="right">942,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,491</td>
<td align="right">21,977,179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,300</td>
<td align="right">746,295</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">25,110,718</td>
<td align="right">63.5%</td>
<td align="right">5.9%</td>
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
<td align="right">14,386,155</td>
<td align="right">36.4%</td>
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
<td align="right">18,975</td>
<td align="right">100.0%</td>
<td align="right">2.4%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,329</td>
<td align="right">12.6%</td>
<td align="right">2,493</td>
<td align="right">13.1%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">954</td>
<td align="right">5.1%</td>
<td align="right">1,011</td>
<td align="right">5.3%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">2,644</td>
<td align="right">14.3%</td>
<td align="right">2,801</td>
<td align="right">14.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">678</td>
<td align="right">3.7%</td>
<td align="right">696</td>
<td align="right">3.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">207</td>
<td align="right">1.1%</td>
<td align="right">212</td>
<td align="right">1.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">694</td>
<td align="right">3.7%</td>
<td align="right">705</td>
<td align="right">3.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">358</td>
<td align="right">1.9%</td>
<td align="right">363</td>
<td align="right">1.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">567</td>
<td align="right">3.1%</td>
<td align="right">571</td>
<td align="right">3.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,878</td>
<td align="right">15.5%</td>
<td align="right">2,895</td>
<td align="right">15.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,287</td>
<td align="right">6.9%</td>
<td align="right">1,291</td>
<td align="right">6.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,212</td>
<td align="right">6.5%</td>
<td align="right">1,209</td>
<td align="right">6.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">2,225</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.9%</td>
<td align="right">1,086</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.3%</td>
<td align="right">982</td>
<td align="right">5.2%</td>
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
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">91</td>
<td align="right">0.5%</td>
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
<td align="right">5,532,075</td>
<td align="right">14.4%</td>
<td align="right">97.3%</td>
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
<td align="right">10,754</td>
<td align="right">0.0%</td>
<td align="right">16.8%</td>
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
<td align="right">32,756,171</td>
<td align="right">85.5%</td>
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
<td align="right">3,860</td>
<td align="right">80.2%</td>
<td align="right">4,515</td>
<td align="right">82.1%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">950</td>
<td align="right">19.8%</td>
<td align="right">982</td>
<td align="right">17.9%</td>
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
<td align="left">out of range</td>
<td align="right">338</td>
<td align="right">8.8%</td>
<td align="right">422</td>
<td align="right">9.3%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,418</td>
<td align="right">62.6%</td>
<td align="right">2,981</td>
<td align="right">66.0%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">143</td>
<td align="right">3.7%</td>
<td align="right">148</td>
<td align="right">3.3%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">271</td>
<td align="right">7.0%</td>
<td align="right">273</td>
<td align="right">6.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">689</td>
<td align="right">17.8%</td>
<td align="right">690</td>
<td align="right">15.3%</td>
<td align="right">0.1%</td>
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
<td align="right">23,732,948</td>
<td align="right">7.4%</td>
<td align="right">2.1%</td>
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
<td align="right">8,444</td>
<td align="right">0.0%</td>
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
<td align="right">297,271,767</td>
<td align="right">92.7%</td>
<td align="right">296,932,697</td>
<td align="right">92.6%</td>
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
<td align="right">455,032</td>
<td align="right">100.0%</td>
<td align="right">464,456</td>
<td align="right">100.0%</td>
<td align="right">2.1%</td>
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
<td align="right">399</td>
<td align="right">9.4%</td>
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
<td align="right">409,659</td>
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
<td align="right">20,882,212</td>
<td align="right">28.9%</td>
<td align="right">8.4%</td>
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
<td align="right">51,026,271</td>
<td align="right">70.5%</td>
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
<td align="right">8,842</td>
<td align="right">20.1%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">33,475</td>
<td align="right">80.3%</td>
<td align="right">35,100</td>
<td align="right">79.9%</td>
<td align="right">4.9%</td>
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
<td align="right">224</td>
<td align="right">0.6%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">12,852</td>
<td align="right">38.4%</td>
<td align="right">14,109</td>
<td align="right">40.2%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,081</td>
<td align="right">15.2%</td>
<td align="right">5,352</td>
<td align="right">15.2%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">117</td>
<td align="right">0.3%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,217</td>
<td align="right">12.6%</td>
<td align="right">4,261</td>
<td align="right">12.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,129</td>
<td align="right">9.3%</td>
<td align="right">3,147</td>
<td align="right">9.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">22.3%</td>
<td align="right">7,480</td>
<td align="right">21.3%</td>
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
<td align="right">3,299,370</td>
<td align="right">12.3%</td>
<td align="right">145.5%</td>
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
<td align="right">23,499,630</td>
<td align="right">87.7%</td>
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
<td align="right">3,497</td>
<td align="right">100.0%</td>
<td align="right">9.9%</td>
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
<td align="left">other</td>
<td align="right">1,371</td>
<td align="right">43.1%</td>
<td align="right">1,589</td>
<td align="right">45.4%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,392</td>
<td align="right">43.7%</td>
<td align="right">1,472</td>
<td align="right">42.1%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">285</td>
<td align="right">9.0%</td>
<td align="right">299</td>
<td align="right">8.6%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">134</td>
<td align="right">4.2%</td>
<td align="right">137</td>
<td align="right">3.9%</td>
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
<td align="right">290,691</td>
<td align="right">0.5%</td>
<td align="right">232.1%</td>
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
<td align="right">28,796,061</td>
<td align="right">48.6%</td>
<td align="right">66.4%</td>
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
<td align="right">30,104,770</td>
<td align="right">50.8%</td>
<td align="right">39.9%</td>
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
<td align="right">6,117</td>
<td align="right">18.5%</td>
<td align="right">164.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,855</td>
<td align="right">85.7%</td>
<td align="right">26,896</td>
<td align="right">81.5%</td>
<td align="right">94.1%</td>
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
<td align="right">18,360</td>
<td align="right">68.3%</td>
<td align="right">185.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">422</td>
<td align="right">3.0%</td>
<td align="right">558</td>
<td align="right">2.1%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,111</td>
<td align="right">8.0%</td>
<td align="right">1,336</td>
<td align="right">5.0%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,136</td>
<td align="right">15.4%</td>
<td align="right">2,494</td>
<td align="right">9.3%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,412</td>
<td align="right">17.4%</td>
<td align="right">2,712</td>
<td align="right">10.1%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">693</td>
<td align="right">5.0%</td>
<td align="right">758</td>
<td align="right">2.8%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">350</td>
<td align="right">2.5%</td>
<td align="right">382</td>
<td align="right">1.4%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">239</td>
<td align="right">1.7%</td>
<td align="right">243</td>
<td align="right">0.9%</td>
<td align="right">1.7%</td>
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
<td align="right">36,540,704</td>
<td align="right">11.6%</td>
<td align="right">34.8%</td>
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
<td align="right">56,589,995</td>
<td align="right">17.9%</td>
<td align="right">12.3%</td>
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
<td align="right">222,903,177</td>
<td align="right">70.5%</td>
<td align="right">-2.6%</td>
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
<td align="right">702,371</td>
<td align="right">94.1%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,592</td>
<td align="right">7.5%</td>
<td align="right">44,213</td>
<td align="right">5.9%</td>
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
<td align="left">module attr not found</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">244</td>
<td align="right">0.6%</td>
<td align="right">294</td>
<td align="right">0.7%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,223</td>
<td align="right">14.6%</td>
<td align="right">6,735</td>
<td align="right">15.2%</td>
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
<td align="right">20,646</td>
<td align="right">46.7%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,847</td>
<td align="right">9.0%</td>
<td align="right">3,976</td>
<td align="right">9.0%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,007</td>
<td align="right">7.1%</td>
<td align="right">3,087</td>
<td align="right">7.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.5%</td>
<td align="right">2,410</td>
<td align="right">5.5%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,048</td>
<td align="right">7.2%</td>
<td align="right">3,107</td>
<td align="right">7.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,740</td>
<td align="right">6.4%</td>
<td align="right">2,781</td>
<td align="right">6.3%</td>
<td align="right">1.5%</td>
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
<td align="right">233,745,322</td>
<td align="right">100.0%</td>
<td align="right">12.0%</td>
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
<td align="right">4,537</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
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
<td align="right">13,595</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">2,265,780</td>
<td align="right">100.0%</td>
<td align="right">2,265,815</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">731,584</td>
<td align="right">72.0%</td>
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
<td align="right">1,577,045</td>
<td align="right">17.4%</td>
<td align="right">407.1%</td>
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
<td align="right">7,326,519</td>
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
<td align="right">174,005</td>
<td align="right">1.9%</td>
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
<td align="left">Success</td>
<td align="right">6,101</td>
<td align="right">86.4%</td>
<td align="right">30,007</td>
<td align="right">96.9%</td>
<td align="right">391.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">962</td>
<td align="right">13.6%</td>
<td align="right">975</td>
<td align="right">3.1%</td>
<td align="right">1.4%</td>
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
<td align="left">overridden</td>
<td align="right">157</td>
<td align="right">16.3%</td>
<td align="right">160</td>
<td align="right">16.4%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.8%</td>
<td align="right">518</td>
<td align="right">53.1%</td>
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
<td align="right">184,971</td>
<td align="right">1.0%</td>
<td align="right">184.1%</td>
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
<td align="right">17,740,867</td>
<td align="right">99.0%</td>
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
<td align="right">964</td>
<td align="right">62.6%</td>
<td align="right">988</td>
<td align="right">63.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">37.4%</td>
<td align="right">576</td>
<td align="right">36.8%</td>
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
<td align="right">964</td>
<td align="right">100.0%</td>
<td align="right">988</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="right">400,846</td>
<td align="right">0.2%</td>
<td align="right">17.2%</td>
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
<td align="right">9,970,394</td>
<td align="right">6.1%</td>
<td align="right">1.5%</td>
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
<td align="right">153,370,695</td>
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
<td align="right">11,597</td>
<td align="right">44.2%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,547</td>
<td align="right">58.6%</td>
<td align="right">14,659</td>
<td align="right">55.8%</td>
<td align="right">8.2%</td>
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
<td align="right">1,799</td>
<td align="right">15.5%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,817</td>
<td align="right">50.3%</td>
<td align="right">6,118</td>
<td align="right">52.8%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">651</td>
<td align="right">6.8%</td>
<td align="right">722</td>
<td align="right">6.2%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,239</td>
<td align="right">12.9%</td>
<td align="right">1,267</td>
<td align="right">10.9%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">711</td>
<td align="right">7.4%</td>
<td align="right">722</td>
<td align="right">6.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">9.2%</td>
<td align="right">883</td>
<td align="right">7.6%</td>
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
<td align="right">6,307</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
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
<td align="right">83,594,683</td>
<td align="right">100.0%</td>
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
<td align="right">293</td>
<td align="right">10.9%</td>
<td align="right">307</td>
<td align="right">11.4%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">89.1%</td>
<td align="right">2,392</td>
<td align="right">88.6%</td>
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
<td align="right">250</td>
<td align="right">85.3%</td>
<td align="right">264</td>
<td align="right">86.0%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.7%</td>
<td align="right">43</td>
<td align="right">14.0%</td>
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
<td align="right">62,983,257</td>
<td align="right">1.9%</td>
<td align="right">22.3%</td>
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
<td align="right">152,355,357</td>
<td align="right">4.5%</td>
<td align="right">17.6%</td>
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
<td align="right">1,170,875,873</td>
<td align="right">34.6%</td>
<td align="right">15.4%</td>
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
<td align="right">2,002,011,350</td>
<td align="right">59.1%</td>
<td align="right">11.2%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">65,108</td>
<td align="right">0.1%</td>
<td align="right">184,971</td>
<td align="right">0.1%</td>
<td align="right">184.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,344,029</td>
<td align="right">1.0%</td>
<td align="right">3,299,370</td>
<td align="right">2.2%</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,803,751</td>
<td align="right">2.2%</td>
<td align="right">5,532,075</td>
<td align="right">3.6%</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,522,593</td>
<td align="right">16.6%</td>
<td align="right">30,104,770</td>
<td align="right">19.8%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,394,591</td>
<td align="right">38.9%</td>
<td align="right">56,589,995</td>
<td align="right">37.2%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,272,623</td>
<td align="right">14.9%</td>
<td align="right">20,882,212</td>
<td align="right">13.7%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,721,770</td>
<td align="right">18.3%</td>
<td align="right">25,110,718</td>
<td align="right">16.5%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,820,744</td>
<td align="right">7.6%</td>
<td align="right">9,970,394</td>
<td align="right">6.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,567</td>
<td align="right">0.1%</td>
<td align="right">174,005</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
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
<td align="right">1,576,266</td>
<td align="right">2.5%</td>
<td align="right">408.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,656,273</td>
<td align="right">20.7%</td>
<td align="right">17,392,198</td>
<td align="right">27.6%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,428,808</td>
<td align="right">16.4%</td>
<td align="right">10,171,559</td>
<td align="right">16.1%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,678,149</td>
<td align="right">9.1%</td>
<td align="right">5,461,145</td>
<td align="right">8.7%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,684,686</td>
<td align="right">9.1%</td>
<td align="right">5,197,488</td>
<td align="right">8.3%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">373,727</td>
<td align="right">0.7%</td>
<td align="right">408,639</td>
<td align="right">0.6%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,944,529</td>
<td align="right">5.7%</td>
<td align="right">3,123,153</td>
<td align="right">5.0%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,313,787</td>
<td align="right">22.0%</td>
<td align="right">11,221,835</td>
<td align="right">17.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,560</td>
<td align="right">4.1%</td>
<td align="right">2,103,577</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,518</td>
<td align="right">9.9%</td>
<td align="right">5,102,530</td>
<td align="right">8.1%</td>
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
<td align="right">950,205</td>
<td align="right">0.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,414,980</td>
<td align="right">10.7%</td>
<td align="right">22,296,447</td>
<td align="right">10.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,083,691</td>
<td align="right">19.5%</td>
<td align="right">41,262,958</td>
<td align="right">19.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,378,553</td>
<td align="right">35.8%</td>
<td align="right">75,558,791</td>
<td align="right">35.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,379,338</td>
<td align="right">35.8%</td>
<td align="right">75,559,576</td>
<td align="right">35.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,759,716</td>
<td align="right">89.2%</td>
<td align="right">187,915,703</td>
<td align="right">89.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,794,318</td>
<td align="right">46.5%</td>
<td align="right">97,856,023</td>
<td align="right">46.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,794,318</td>
<td align="right">46.5%</td>
<td align="right">97,856,023</td>
<td align="right">46.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,625,333</td>
<td align="right">53.5%</td>
<td align="right">112,601,076</td>
<td align="right">53.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,471</td>
<td align="right">8.8%</td>
<td align="right">18,490,930</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,848</td>
<td align="right">4.4%</td>
<td align="right">9,332,056</td>
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
<td align="left">Mortal increfs</td>
<td align="right">2,073,594,707</td>
<td align="right">40.8%</td>
<td align="right">1,830,482,045</td>
<td align="right">36.7%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,135,809,193</td>
<td align="right">36.0%</td>
<td align="right">1,916,540,538</td>
<td align="right">32.9%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,403,097,135</td>
<td align="right">27.6%</td>
<td align="right">1,542,741,867</td>
<td align="right">30.9%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">387,688,953</td>
<td align="right">7.6%</td>
<td align="right">421,072,660</td>
<td align="right">8.4%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">632,705,858</td>
<td align="right">10.7%</td>
<td align="right">680,106,647</td>
<td align="right">11.7%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,013,535</td>
<td align="right"></td>
<td align="right">1,085,763</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,795,389,039</td>
<td align="right">30.2%</td>
<td align="right">1,911,200,231</td>
<td align="right">32.8%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,376,604,687</td>
<td align="right">23.2%</td>
<td align="right">1,311,791,155</td>
<td align="right">22.5%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">142,670,839</td>
<td align="right"></td>
<td align="right">147,985,348</td>
<td align="right"></td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">791,762</td>
<td align="right">0.2%</td>
<td align="right">774,124</td>
<td align="right">0.2%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,216,589,511</td>
<td align="right">23.9%</td>
<td align="right">1,195,728,660</td>
<td align="right">24.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,181,293</td>
<td align="right"></td>
<td align="right">3,233,457</td>
<td align="right"></td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,169,237</td>
<td align="right"></td>
<td align="right">2,149,123</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">261,911,713</td>
<td align="right"></td>
<td align="right">263,873,901</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">281,671,356</td>
<td align="right">54.7%</td>
<td align="right">281,729,205</td>
<td align="right">54.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,703,258</td>
<td align="right"></td>
<td align="right">281,761,096</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,056</td>
<td align="right"></td>
<td align="right">866,226</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,974,666</td>
<td align="right">45.3%</td>
<td align="right">232,941,678</td>
<td align="right">45.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,622,324</td>
<td align="right"></td>
<td align="right">245,588,032</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,174,295</td>
<td align="right">45.1%</td>
<td align="right">232,158,945</td>
<td align="right">45.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">18,988</td>
<td align="right">32.1%</td>
<td align="right">-67.8%</td>
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
<td align="right">412</td>
<td align="right">0.7%</td>
<td align="right">-62.0%</td>
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
<td align="right">59,239</td>
<td align="right"></td>
<td align="right">-51.2%</td>
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
<td align="right">711</td>
<td align="right">1.2%</td>
<td align="right">-47.3%</td>
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
<td align="right">37,183</td>
<td align="right">62.8%</td>
<td align="right">-37.3%</td>
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
<td align="right">40,251</td>
<td align="right">67.9%</td>
<td align="right">-35.6%</td>
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
<td align="right">199,556,138</td>
<td align="right"></td>
<td align="right">-30.1%</td>
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
<td align="right">3,313,726,218</td>
<td align="right">1,660.5%</td>
<td align="right">-23.3%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">58,961</td>
<td align="right"></td>
<td align="right">18,988</td>
<td align="right"></td>
<td align="right">-67.8%</td>
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
<td align="right">18,046</td>
<td align="right">95.0%</td>
<td align="right">-67.8%</td>
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
<td align="right">2,590</td>
<td align="right">13.6%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,679</td>
<td align="right">14.7%</td>
<td align="right">3,096</td>
<td align="right">16.3%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">23,696</td>
<td align="right">40.2%</td>
<td align="right">6,444</td>
<td align="right">33.9%</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">14,146</td>
<td align="right">24.0%</td>
<td align="right">4,030</td>
<td align="right">21.2%</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,412</td>
<td align="right">10.9%</td>
<td align="right">2,371</td>
<td align="right">12.5%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">746</td>
<td align="right">1.3%</td>
<td align="right">457</td>
<td align="right">2.4%</td>
<td align="right">-38.7%</td>
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
<td align="right">614</td>
<td align="right">3.2%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,956</td>
<td align="right">11.8%</td>
<td align="right">2,826</td>
<td align="right">14.9%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,624</td>
<td align="right">23.1%</td>
<td align="right">3,859</td>
<td align="right">20.3%</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,142</td>
<td align="right">37.6%</td>
<td align="right">6,378</td>
<td align="right">33.6%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,927</td>
<td align="right">18.5%</td>
<td align="right">3,969</td>
<td align="right">20.9%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,359</td>
<td align="right">2.3%</td>
<td align="right">379</td>
<td align="right">2.0%</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">35</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">-40.0%</td>
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
<td align="right">3,000</td>
<td align="right">1,969.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">145</td>
<td align="right">3,000</td>
<td align="right">1,969.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">145</td>
<td align="right">3,000</td>
<td align="right">1,969.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">30,690</td>
<td align="right">530</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">673,984</td>
<td align="right">19,213</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">654,264</td>
<td align="right">27,888</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,196,166</td>
<td align="right">104,874</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,036,151</td>
<td align="right">53,487</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">756,292</td>
<td align="right">45,381</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">132,992</td>
<td align="right">8,883</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">131,495</td>
<td align="right">8,883</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">236,060</td>
<td align="right">16,296</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,301,824</td>
<td align="right">191,713</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">203,629</td>
<td align="right">39,254</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">17,696</td>
<td align="right">4,473</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,472,982</td>
<td align="right">2,821,738</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">481,425</td>
<td align="right">165,331</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">619,501</td>
<td align="right">235,645</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,477,148</td>
<td align="right">564,786</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">319,942</td>
<td align="right">126,233</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,857,053</td>
<td align="right">1,526,364</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,791,511</td>
<td align="right">1,526,364</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,241,580</td>
<td align="right">2,231,180</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,284,888</td>
<td align="right">4,534,273</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">532,253</td>
<td align="right">235,526</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,388,176</td>
<td align="right">4,883,082</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">758,093</td>
<td align="right">361,212</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">11,505,283</td>
<td align="right">5,689,145</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,039,642</td>
<td align="right">19,983,668</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,475,601</td>
<td align="right">775,760</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,877,831</td>
<td align="right">2,069,119</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,239</td>
<td align="right">467,104</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,175,336</td>
<td align="right">647,926</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,450,239</td>
<td align="right">1,907,019</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,462,070</td>
<td align="right">3,052,839</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,384,212</td>
<td align="right">3,629,046</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,882,596</td>
<td align="right">2,246,888</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">3,850,818</td>
<td align="right">2,302,619</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">11,409,795</td>
<td align="right">6,994,328</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">491,081</td>
<td align="right">304,500</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">491,081</td>
<td align="right">304,500</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,027,854</td>
<td align="right">1,886,518</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,393,964</td>
<td align="right">6,484,092</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">3,473,926</td>
<td align="right">2,169,952</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,865,670</td>
<td align="right">23,275,158</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,703,884</td>
<td align="right">1,076,723</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">156,874,165</td>
<td align="right">99,378,556</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,066,103</td>
<td align="right">10,368,979</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">57,529,388</td>
<td align="right">37,297,472</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,426,907</td>
<td align="right">11,301,570</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,574,808</td>
<td align="right">10,224,250</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">980,496</td>
<td align="right">647,902</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,018,056</td>
<td align="right">4,011,090</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,188,149</td>
<td align="right">2,799,763</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,050,508</td>
<td align="right">12,079,629</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">106,215,616</td>
<td align="right">72,240,341</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">34,396,910</td>
<td align="right">23,758,635</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">259,193,754</td>
<td align="right">179,130,287</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,432,271</td>
<td align="right">17,718,307</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">53,789,556</td>
<td align="right">37,560,583</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">285,324,689</td>
<td align="right">199,556,138</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">913,514</td>
<td align="right">647,902</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,831,059</td>
<td align="right">5,590,956</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,033,429</td>
<td align="right">25,753,538</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,538,156</td>
<td align="right">1,830,468</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">317,413,875</td>
<td align="right">231,093,696</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,746,487</td>
<td align="right">2,004,384</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,972,258</td>
<td align="right">6,296,385</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,378,487</td>
<td align="right">15,016,396</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">10,429,956</td>
<td align="right">7,691,332</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">36,398,291</td>
<td align="right">26,896,117</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">36,299,446</td>
<td align="right">26,896,117</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">36,170,292</td>
<td align="right">26,820,148</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,059,212</td>
<td align="right">9,715,707</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,544,429</td>
<td align="right">8,619,963</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">21,043,728</td>
<td align="right">15,733,548</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">34,407,015</td>
<td align="right">25,739,006</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">47,110,021</td>
<td align="right">35,340,743</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">61,059,575</td>
<td align="right">46,185,735</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">10,064,436</td>
<td align="right">7,639,832</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">19,806,010</td>
<td align="right">15,081,296</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">77,318,038</td>
<td align="right">58,925,398</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">13,014,616</td>
<td align="right">9,988,971</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">13,014,616</td>
<td align="right">9,988,971</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">18,500,215</td>
<td align="right">14,212,187</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,798,012</td>
<td align="right">10,618,511</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">414,299</td>
<td align="right">323,951</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">4,204,796</td>
<td align="right">3,306,385</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">332,198</td>
<td align="right">261,706</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,864,185</td>
<td align="right">20,409,025</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">10,894,638</td>
<td align="right">8,604,884</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,484,381</td>
<td align="right">1,176,157</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,484,381</td>
<td align="right">1,176,157</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">31,171,876</td>
<td align="right">24,864,237</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">97,181,985</td>
<td align="right">77,596,028</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">402,959,615</td>
<td align="right">324,326,680</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">45,934,167</td>
<td align="right">37,005,108</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">18,819,649</td>
<td align="right">15,201,537</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,340,632</td>
<td align="right">9,969,758</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,030,103</td>
<td align="right">8,980,962</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">318,749,205</td>
<td align="right">261,024,902</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">440,648</td>
<td align="right">361,212</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">29,286,334</td>
<td align="right">24,100,167</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">7,867,509</td>
<td align="right">6,487,092</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">172,553,255</td>
<td align="right">142,651,456</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">40,029,155</td>
<td align="right">33,236,991</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">21,268,650</td>
<td align="right">17,691,469</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">8,975,249</td>
<td align="right">7,495,376</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">40,852,751</td>
<td align="right">34,156,752</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,255,642</td>
<td align="right">16,195,227</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">15,512,023</td>
<td align="right">13,058,396</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,210,583</td>
<td align="right">6,970,474</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">32,273,824</td>
<td align="right">27,423,245</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,793,414</td>
<td align="right">67,874,364</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">31,918,355</td>
<td align="right">27,333,549</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,285,534</td>
<td align="right">14,856,498</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">60,847,224</td>
<td align="right">52,347,682</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">45,647,478</td>
<td align="right">39,330,776</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">11,080,050</td>
<td align="right">9,549,160</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">48,832,887</td>
<td align="right">42,571,437</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">27,801,661</td>
<td align="right">24,238,786</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">37,699,964</td>
<td align="right">33,015,147</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">15,924,623</td>
<td align="right">14,093,372</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,358,492</td>
<td align="right">6,514,305</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,128,171</td>
<td align="right">43,644,066</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">7,208,671</td>
<td align="right">6,428,403</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,850,127</td>
<td align="right">5,252,246</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">87,642,357</td>
<td align="right">78,756,963</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,413,698</td>
<td align="right">13,187,544</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">11,984,853</td>
<td align="right">10,981,368</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,290,624</td>
<td align="right">25,977,948</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">20,617,238</td>
<td align="right">18,941,526</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,054,133</td>
<td align="right">21,242,220</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,983,632</td>
<td align="right">7,373,721</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,983,632</td>
<td align="right">7,373,721</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">46,243,066</td>
<td align="right">42,908,761</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,195,962</td>
<td align="right">13,199,259</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,943,145</td>
<td align="right">6,481,471</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,785,425</td>
<td align="right">17,613,075</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">7,399,249</td>
<td align="right">6,941,137</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,517,959</td>
<td align="right">2,398,260</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,544,355</td>
<td align="right">7,297,255</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,544,355</td>
<td align="right">7,297,255</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">32,089,186</td>
<td align="right">31,537,558</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,413,215</td>
<td align="right">13,199,259</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,514,501</td>
<td align="right">2,503,470</td>
<td align="right">-0.4%</td>
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
<td align="left">_STORE_ATTR</td>
<td align="right">637,202</td>
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
<td align="left">_TO_BOOL_STR</td>
<td align="right">286,480</td>
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
<td align="right">6,055</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,697</td>
<td align="right">4,134</td>
<td align="right">-38.3%</td>
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
