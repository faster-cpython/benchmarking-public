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
<td align="right">737,770</td>
<td align="right">7,063,687</td>
<td align="right">857.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">52,828</td>
<td align="right">338,565</td>
<td align="right">540.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,764</td>
<td align="right">378,215</td>
<td align="right">427.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,595</td>
<td align="right">8,941</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">607,170</td>
<td align="right">1,389,666</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">539,732</td>
<td align="right">1,192,640</td>
<td align="right">121.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">71,110</td>
<td align="right">147,584</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">30,826</td>
<td align="right">1,679</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,729</td>
<td align="right">13,963</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">175,015</td>
<td align="right">311,123</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,346,830</td>
<td align="right">2,358,961</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">105,916</td>
<td align="right">179,097</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">237</td>
<td align="right">394</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,276,562</td>
<td align="right">9,710,199</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,288,584</td>
<td align="right">6,622,327</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,498,806</td>
<td align="right">2,310,610</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,893,110</td>
<td align="right">3,984,446</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,314,750</td>
<td align="right">1,809,844</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,053,808</td>
<td align="right">10,976,354</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,780,166</td>
<td align="right">2,352,246</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,159,251</td>
<td align="right">10,333,786</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,802,319</td>
<td align="right">3,509,534</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7,373</td>
<td align="right">9,212</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,196,578</td>
<td align="right">1,486,847</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,860,744</td>
<td align="right">28,062,328</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">123,583</td>
<td align="right">95,486</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,203</td>
<td align="right">1,455</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,802,952</td>
<td align="right">3,385,079</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">995,242</td>
<td align="right">1,200,062</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,520,033</td>
<td align="right">3,038,135</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,055,105</td>
<td align="right">1,263,974</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,342</td>
<td align="right">8,778</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,781,524</td>
<td align="right">30,435,800</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80,696,760</td>
<td align="right">94,891,258</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,190</td>
<td align="right">3,742</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,946,296</td>
<td align="right">2,281,083</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,281,897</td>
<td align="right">1,495,197</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,122,081</td>
<td align="right">3,641,380</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,406,516</td>
<td align="right">41,153,400</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,316</td>
<td align="right">20,690</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,566,177</td>
<td align="right">24,214,196</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,315,807</td>
<td align="right">3,721,682</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">529</td>
<td align="right">591</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,666,011</td>
<td align="right">15,250,611</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,654,614</td>
<td align="right">81,916,182</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,125,045</td>
<td align="right">1,254,815</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,505,803</td>
<td align="right">18,385,614</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,727,301</td>
<td align="right">12,967,762</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,600,778</td>
<td align="right">1,769,048</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">397,283</td>
<td align="right">435,696</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">473,129,449</td>
<td align="right">516,819,096</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">138,950,683</td>
<td align="right">151,263,463</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,634,877</td>
<td align="right">20,256,001</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,091,463</td>
<td align="right">147,751,869</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">158,262,085</td>
<td align="right">171,399,325</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">137,180,163</td>
<td align="right">148,528,148</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">34,553,170</td>
<td align="right">37,250,131</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,976,958</td>
<td align="right">28,001,571</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,895,695</td>
<td align="right">11,732,449</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,408,239</td>
<td align="right">54,174,705</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">71,172,221</td>
<td align="right">76,479,384</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">32,794,986</td>
<td align="right">35,171,259</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,541,289</td>
<td align="right">104,259,448</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">10,360,971</td>
<td align="right">11,055,480</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,719</td>
<td align="right">71,151</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,832,632</td>
<td align="right">47,754,902</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,204,712</td>
<td align="right">20,453,201</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,022,823</td>
<td align="right">25,565,608</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">5,305,436</td>
<td align="right">5,643,272</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">74,158</td>
<td align="right">78,667</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,960,090</td>
<td align="right">4,199,261</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,331,175</td>
<td align="right">17,299,520</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,938,918</td>
<td align="right">32,741,495</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">8,504,916</td>
<td align="right">8,989,130</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,991,323</td>
<td align="right">4,216,130</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,218,471</td>
<td align="right">2,339,476</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">17,740,232</td>
<td align="right">18,706,448</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,290,760</td>
<td align="right">15,062,945</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">468,382</td>
<td align="right">493,385</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,299,831</td>
<td align="right">35,073,328</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,206,682</td>
<td align="right">48,665,833</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,263,415</td>
<td align="right">6,594,090</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">34,897,738</td>
<td align="right">36,667,217</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,749,850</td>
<td align="right">6,035,485</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">35,566,421</td>
<td align="right">37,273,985</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,060,087</td>
<td align="right">40,875,139</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,539,876</td>
<td align="right">42,408,534</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,211,422</td>
<td align="right">6,493,104</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,821,749</td>
<td align="right">17,500,617</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,528,042</td>
<td align="right">16,137,106</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,352,055</td>
<td align="right">117,763,827</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">9,685,776</td>
<td align="right">10,061,941</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,602,739</td>
<td align="right">5,813,789</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">11,371,356</td>
<td align="right">11,798,295</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,006,240</td>
<td align="right">17,627,380</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">622,656</td>
<td align="right">642,618</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,247,162</td>
<td align="right">7,478,431</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,291,100</td>
<td align="right">12,670,225</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,833,313</td>
<td align="right">4,977,318</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,856,311</td>
<td align="right">3,963,988</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,057,794</td>
<td align="right">1,028,454</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,583</td>
<td align="right">2,645</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,034,786</td>
<td align="right">16,416,334</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,621,464</td>
<td align="right">1,654,833</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,949,976</td>
<td align="right">15,253,836</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">43,276,533</td>
<td align="right">44,142,162</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25,647,062</td>
<td align="right">26,147,927</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,256,335</td>
<td align="right">1,278,640</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,736,740</td>
<td align="right">24,135,008</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">61</td>
<td align="right">60</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,063,683</td>
<td align="right">2,095,596</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,439,933</td>
<td align="right">19,701,089</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,108</td>
<td align="right">8,995</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,308,906</td>
<td align="right">19,523,908</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,990</td>
<td align="right">2,958</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">385,745</td>
<td align="right">389,854</td>
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
<td align="left">TO_BOOL</td>
<td align="right">9,838,541</td>
<td align="right">9,936,672</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,874,510</td>
<td align="right">3,912,902</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,000</td>
<td align="right">40,264</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,097,073</td>
<td align="right">11,165,450</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,148</td>
<td align="right">18,046</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,603,532</td>
<td align="right">2,617,911</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">13,249,013</td>
<td align="right">13,320,728</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,132</td>
<td align="right">172,033</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,193,994</td>
<td align="right">182,116,141</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,794,692</td>
<td align="right">17,864,739</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,251</td>
<td align="right">24,165</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,442</td>
<td align="right">1,447</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,476,178</td>
<td align="right">10,498,515</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,746,037</td>
<td align="right">97,936,759</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,963,368</td>
<td align="right">1,966,277</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,321,678</td>
<td align="right">1,323,085</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,446</td>
<td align="right">165,567</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,149</td>
<td align="right">83,107</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,466,952</td>
<td align="right">4,469,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,726,848</td>
<td align="right">3,728,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,253</td>
<td align="right">1,244,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,252</td>
<td align="right">1,029,059</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,012</td>
<td align="right">17,010</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,415</td>
<td align="right">655,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,415</td>
<td align="right">655,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,415</td>
<td align="right">655,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,649</td>
<td align="right">642,602</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,679</td>
<td align="right">942,621</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,571</td>
<td align="right">427,547</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,952</td>
<td align="right">745,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,978</td>
<td align="right">21,977,095</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,252</td>
<td align="right">746,271</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,017</td>
<td align="right">175,018</td>
<td align="right">0.0%</td>
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
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="right">23,716,839</td>
<td align="right">62.2%</td>
<td align="right">24,115,005</td>
<td align="right">62.6%</td>
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
<td align="right">14,387,058</td>
<td align="right">37.7%</td>
<td align="right">14,386,304</td>
<td align="right">37.3%</td>
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
<td align="right">18,597</td>
<td align="right">100.0%</td>
<td align="right">18,734</td>
<td align="right">100.0%</td>
<td align="right">0.7%</td>
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
<td align="left">floor divide</td>
<td align="right">362</td>
<td align="right">1.9%</td>
<td align="right">342</td>
<td align="right">1.8%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">976</td>
<td align="right">5.2%</td>
<td align="right">1,009</td>
<td align="right">5.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,323</td>
<td align="right">12.5%</td>
<td align="right">2,396</td>
<td align="right">12.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">677</td>
<td align="right">3.6%</td>
<td align="right">695</td>
<td align="right">3.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583</td>
<td align="right">3.1%</td>
<td align="right">570</td>
<td align="right">3.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">2,644</td>
<td align="right">14.2%</td>
<td align="right">2,691</td>
<td align="right">14.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">214</td>
<td align="right">1.2%</td>
<td align="right">211</td>
<td align="right">1.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">92</td>
<td align="right">0.5%</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">989</td>
<td align="right">5.3%</td>
<td align="right">982</td>
<td align="right">5.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">190</td>
<td align="right">1.0%</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,877</td>
<td align="right">15.5%</td>
<td align="right">2,892</td>
<td align="right">15.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,213</td>
<td align="right">6.5%</td>
<td align="right">1,208</td>
<td align="right">6.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">698</td>
<td align="right">3.8%</td>
<td align="right">700</td>
<td align="right">3.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">2,225</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,292</td>
<td align="right">6.9%</td>
<td align="right">1,292</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.8%</td>
<td align="right">1,086</td>
<td align="right">5.8%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">8,778</td>
<td align="right">100.0%</td>
<td align="right">19.6%</td>
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
<td align="right">2,797,663</td>
<td align="right">7.9%</td>
<td align="right">3,504,673</td>
<td align="right">9.7%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">10,753</td>
<td align="right">0.0%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,764,892</td>
<td align="right">92.1%</td>
<td align="right">32,769,582</td>
<td align="right">90.3%</td>
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
<td align="right">3,873</td>
<td align="right">80.2%</td>
<td align="right">4,079</td>
<td align="right">80.6%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">955</td>
<td align="right">19.8%</td>
<td align="right">982</td>
<td align="right">19.4%</td>
<td align="right">2.8%</td>
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
<td align="right">8.7%</td>
<td align="right">422</td>
<td align="right">10.3%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,427</td>
<td align="right">62.7%</td>
<td align="right">2,542</td>
<td align="right">62.3%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">271</td>
<td align="right">7.0%</td>
<td align="right">276</td>
<td align="right">6.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">146</td>
<td align="right">3.8%</td>
<td align="right">148</td>
<td align="right">3.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">690</td>
<td align="right">17.8%</td>
<td align="right">690</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
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
<td align="right">10,315</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,370,345</td>
<td align="right">7.3%</td>
<td align="right">23,713,164</td>
<td align="right">7.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,506</td>
<td align="right">0.0%</td>
<td align="right">8,430</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">297,454,078</td>
<td align="right">92.7%</td>
<td align="right">297,297,059</td>
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
<td align="right">457,541</td>
<td align="right">100.0%</td>
<td align="right">464,080</td>
<td align="right">100.0%</td>
<td align="right">1.4%</td>
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
<td align="right">401</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.4%</td>
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
<td align="right">374,462</td>
<td align="right">0.5%</td>
<td align="right">392,031</td>
<td align="right">0.6%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,274,216</td>
<td align="right">27.3%</td>
<td align="right">19,488,435</td>
<td align="right">27.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,022,615</td>
<td align="right">72.2%</td>
<td align="right">51,032,942</td>
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
<td align="right">8,196</td>
<td align="right">19.7%</td>
<td align="right">8,496</td>
<td align="right">19.8%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">33,504</td>
<td align="right">80.3%</td>
<td align="right">34,335</td>
<td align="right">80.2%</td>
<td align="right">2.5%</td>
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
<td align="right">198</td>
<td align="right">0.6%</td>
<td align="right">169</td>
<td align="right">0.5%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">12,844</td>
<td align="right">38.3%</td>
<td align="right">13,627</td>
<td align="right">39.7%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,100</td>
<td align="right">9.3%</td>
<td align="right">3,141</td>
<td align="right">9.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,096</td>
<td align="right">15.2%</td>
<td align="right">5,143</td>
<td align="right">15.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,263</td>
<td align="right">12.7%</td>
<td align="right">4,252</td>
<td align="right">12.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">22.3%</td>
<td align="right">7,480</td>
<td align="right">21.8%</td>
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
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">115</td>
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
<td align="right">1,343,532</td>
<td align="right">5.4%</td>
<td align="right">2,355,584</td>
<td align="right">9.1%</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,870</td>
<td align="right">94.6%</td>
<td align="right">23,499,559</td>
<td align="right">90.9%</td>
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
<td align="right">3,176</td>
<td align="right">100.0%</td>
<td align="right">3,255</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="right">1,396</td>
<td align="right">44.0%</td>
<td align="right">1,473</td>
<td align="right">45.3%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">285</td>
<td align="right">9.0%</td>
<td align="right">299</td>
<td align="right">9.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">134</td>
<td align="right">4.2%</td>
<td align="right">137</td>
<td align="right">4.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,361</td>
<td align="right">42.9%</td>
<td align="right">1,346</td>
<td align="right">41.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">90,190</td>
<td align="right">0.2%</td>
<td align="right">145,257</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,265,702</td>
<td align="right">44.4%</td>
<td align="right">22,512,529</td>
<td align="right">48.0%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,551,521</td>
<td align="right">55.4%</td>
<td align="right">24,195,668</td>
<td align="right">51.6%</td>
<td align="right">12.3%</td>
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
<td align="right">2,364</td>
<td align="right">14.5%</td>
<td align="right">3,368</td>
<td align="right">15.9%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,932</td>
<td align="right">85.5%</td>
<td align="right">17,823</td>
<td align="right">84.1%</td>
<td align="right">27.9%</td>
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
<td align="right">6,494</td>
<td align="right">46.6%</td>
<td align="right">9,930</td>
<td align="right">55.7%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">422</td>
<td align="right">3.0%</td>
<td align="right">557</td>
<td align="right">3.1%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,115</td>
<td align="right">8.0%</td>
<td align="right">1,311</td>
<td align="right">7.4%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">693</td>
<td align="right">5.0%</td>
<td align="right">758</td>
<td align="right">4.3%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">350</td>
<td align="right">2.5%</td>
<td align="right">382</td>
<td align="right">2.1%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,136</td>
<td align="right">15.3%</td>
<td align="right">2,247</td>
<td align="right">12.6%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,430</td>
<td align="right">17.4%</td>
<td align="right">2,342</td>
<td align="right">13.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">239</td>
<td align="right">1.7%</td>
<td align="right">243</td>
<td align="right">1.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.2%</td>
<td align="right">29</td>
<td align="right">0.2%</td>
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
<td align="right">27,061,611</td>
<td align="right">8.8%</td>
<td align="right">30,622,152</td>
<td align="right">9.7%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">50,351,214</td>
<td align="right">16.4%</td>
<td align="right">54,116,007</td>
<td align="right">17.2%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">229,220,071</td>
<td align="right">74.7%</td>
<td align="right">229,289,892</td>
<td align="right">73.0%</td>
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
<td align="right">522,656</td>
<td align="right">92.5%</td>
<td align="right">590,574</td>
<td align="right">93.1%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,669</td>
<td align="right">7.5%</td>
<td align="right">43,526</td>
<td align="right">6.9%</td>
<td align="right">2.0%</td>
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
<td align="right">208</td>
<td align="right">0.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,223</td>
<td align="right">14.6%</td>
<td align="right">6,543</td>
<td align="right">15.0%</td>
<td align="right">5.1%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">3,018</td>
<td align="right">7.1%</td>
<td align="right">3,087</td>
<td align="right">7.1%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,983</td>
<td align="right">46.8%</td>
<td align="right">20,383</td>
<td align="right">46.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.5%</td>
<td align="right">2,324</td>
<td align="right">5.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,737</td>
<td align="right">6.4%</td>
<td align="right">2,777</td>
<td align="right">6.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,879</td>
<td align="right">9.1%</td>
<td align="right">3,931</td>
<td align="right">9.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,062</td>
<td align="right">7.2%</td>
<td align="right">3,097</td>
<td align="right">7.1%</td>
<td align="right">1.1%</td>
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
<td align="right">208,746,767</td>
<td align="right">100.0%</td>
<td align="right">225,668,460</td>
<td align="right">100.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,612</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">-2.0%</td>
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
<td align="right">13,584</td>
<td align="right">100.0%</td>
<td align="right">13,574</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,861</td>
<td align="right">100.0%</td>
<td align="right">2,265,786</td>
<td align="right">100.0%</td>
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
<td align="right">731,541</td>
<td align="right">72.0%</td>
<td align="right">731,560</td>
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
<td align="right">309,064</td>
<td align="right">3.7%</td>
<td align="right">1,577,337</td>
<td align="right">17.4%</td>
<td align="right">410.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,927,697</td>
<td align="right">94.2%</td>
<td align="right">7,326,073</td>
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
<td align="right">173,713</td>
<td align="right">2.1%</td>
<td align="right">173,705</td>
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
<td align="right">6,068</td>
<td align="right">86.2%</td>
<td align="right">30,016</td>
<td align="right">96.8%</td>
<td align="right">394.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">969</td>
<td align="right">13.8%</td>
<td align="right">978</td>
<td align="right">3.2%</td>
<td align="right">0.9%</td>
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
<td align="left">overridden</td>
<td align="right">154</td>
<td align="right">15.9%</td>
<td align="right">161</td>
<td align="right">16.5%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">294</td>
<td align="right">30.3%</td>
<td align="right">296</td>
<td align="right">30.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.5%</td>
<td align="right">518</td>
<td align="right">53.0%</td>
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
<td align="right">65,185</td>
<td align="right">0.4%</td>
<td align="right">69,616</td>
<td align="right">0.4%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,579</td>
<td align="right">99.6%</td>
<td align="right">17,740,932</td>
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
<td align="left">Failure</td>
<td align="right">958</td>
<td align="right">62.5%</td>
<td align="right">959</td>
<td align="right">62.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">37.5%</td>
<td align="right">576</td>
<td align="right">37.5%</td>
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
<td align="right">958</td>
<td align="right">100.0%</td>
<td align="right">959</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">342,122</td>
<td align="right">0.2%</td>
<td align="right">379,450</td>
<td align="right">0.2%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,821,309</td>
<td align="right">6.0%</td>
<td align="right">9,917,617</td>
<td align="right">6.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">152,917,418</td>
<td align="right">93.8%</td>
<td align="right">153,357,449</td>
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
<td align="right">9,592</td>
<td align="right">41.4%</td>
<td align="right">11,442</td>
<td align="right">44.5%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,568</td>
<td align="right">58.6%</td>
<td align="right">14,252</td>
<td align="right">55.5%</td>
<td align="right">5.0%</td>
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
<td align="right">1,189</td>
<td align="right">12.4%</td>
<td align="right">1,813</td>
<td align="right">15.8%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,815</td>
<td align="right">50.2%</td>
<td align="right">5,967</td>
<td align="right">52.1%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">648</td>
<td align="right">6.8%</td>
<td align="right">721</td>
<td align="right">6.3%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">723</td>
<td align="right">7.5%</td>
<td align="right">718</td>
<td align="right">6.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,248</td>
<td align="right">13.0%</td>
<td align="right">1,254</td>
<td align="right">11.0%</td>
<td align="right">0.5%</td>
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
<td align="right">6,411</td>
<td align="right">0.0%</td>
<td align="right">6,300</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,771,789</td>
<td align="right">100.0%</td>
<td align="right">83,920,627</td>
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
<td align="right">297</td>
<td align="right">11.0%</td>
<td align="right">303</td>
<td align="right">11.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,400</td>
<td align="right">89.0%</td>
<td align="right">2,392</td>
<td align="right">88.8%</td>
<td align="right">-0.3%</td>
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
<td align="right">254</td>
<td align="right">85.5%</td>
<td align="right">260</td>
<td align="right">85.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.5%</td>
<td align="right">43</td>
<td align="right">14.2%</td>
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
<td align="right">51,578,031</td>
<td align="right">1.7%</td>
<td align="right">56,860,908</td>
<td align="right">1.8%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,014,258,470</td>
<td align="right">33.8%</td>
<td align="right">1,103,589,460</td>
<td align="right">34.4%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">129,580,465</td>
<td align="right">4.3%</td>
<td align="right">138,431,331</td>
<td align="right">4.3%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,801,488,907</td>
<td align="right">60.1%</td>
<td align="right">1,907,063,405</td>
<td align="right">59.5%</td>
<td align="right">5.9%</td>
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
<td align="right">1,343,532</td>
<td align="right">1.0%</td>
<td align="right">2,355,584</td>
<td align="right">1.7%</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,797,663</td>
<td align="right">2.2%</td>
<td align="right">3,504,673</td>
<td align="right">2.5%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,551,521</td>
<td align="right">16.7%</td>
<td align="right">24,195,668</td>
<td align="right">17.5%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,351,214</td>
<td align="right">38.9%</td>
<td align="right">54,116,007</td>
<td align="right">39.1%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,185</td>
<td align="right">0.1%</td>
<td align="right">69,616</td>
<td align="right">0.1%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,716,839</td>
<td align="right">18.3%</td>
<td align="right">24,115,005</td>
<td align="right">17.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,274,216</td>
<td align="right">14.9%</td>
<td align="right">19,488,435</td>
<td align="right">14.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,821,309</td>
<td align="right">7.6%</td>
<td align="right">9,917,617</td>
<td align="right">7.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,713</td>
<td align="right">0.1%</td>
<td align="right">173,705</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">308,285</td>
<td align="right">0.6%</td>
<td align="right">1,576,558</td>
<td align="right">2.8%</td>
<td align="right">411.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,653,708</td>
<td align="right">20.7%</td>
<td align="right">12,757,583</td>
<td align="right">22.4%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,391,933</td>
<td align="right">16.3%</td>
<td align="right">9,512,031</td>
<td align="right">16.7%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">373,442</td>
<td align="right">0.7%</td>
<td align="right">391,011</td>
<td align="right">0.7%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,677,973</td>
<td align="right">9.1%</td>
<td align="right">4,888,343</td>
<td align="right">8.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,945,594</td>
<td align="right">5.7%</td>
<td align="right">3,072,967</td>
<td align="right">5.4%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,685,022</td>
<td align="right">9.1%</td>
<td align="right">4,881,986</td>
<td align="right">8.6%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,446,201</td>
<td align="right">22.2%</td>
<td align="right">11,517,861</td>
<td align="right">20.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,595</td>
<td align="right">4.1%</td>
<td align="right">2,103,582</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,458</td>
<td align="right">9.9%</td>
<td align="right">5,102,486</td>
<td align="right">9.0%</td>
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
<td align="right">1,008,657</td>
<td align="right">0.5%</td>
<td align="right">950,386</td>
<td align="right">0.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,085,060</td>
<td align="right">19.5%</td>
<td align="right">41,207,287</td>
<td align="right">19.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,546,987</td>
<td align="right">10.7%</td>
<td align="right">22,587,408</td>
<td align="right">10.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,929,604</td>
<td align="right">46.5%</td>
<td align="right">98,091,175</td>
<td align="right">46.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,929,604</td>
<td align="right">46.5%</td>
<td align="right">98,091,175</td>
<td align="right">46.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,381,832</td>
<td align="right">35.8%</td>
<td align="right">75,502,982</td>
<td align="right">35.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,382,617</td>
<td align="right">35.8%</td>
<td align="right">75,503,767</td>
<td align="right">35.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,751,847</td>
<td align="right">53.5%</td>
<td align="right">112,687,276</td>
<td align="right">53.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,889,628</td>
<td align="right">89.2%</td>
<td align="right">187,946,148</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,491,306</td>
<td align="right">8.8%</td>
<td align="right">18,490,772</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,243</td>
<td align="right">4.4%</td>
<td align="right">9,332,030</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">876,158</td>
<td align="right"></td>
<td align="right">1,109,455</td>
<td align="right"></td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,282,997</td>
<td align="right"></td>
<td align="right">3,663,499</td>
<td align="right"></td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,408,404</td>
<td align="right"></td>
<td align="right">2,555,324</td>
<td align="right"></td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,077,470,519</td>
<td align="right">40.8%</td>
<td align="right">1,951,127,648</td>
<td align="right">38.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,139,083,215</td>
<td align="right">36.0%</td>
<td align="right">2,026,434,944</td>
<td align="right">34.5%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">387,998,441</td>
<td align="right">7.6%</td>
<td align="right">408,228,851</td>
<td align="right">8.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,403,204,887</td>
<td align="right">27.6%</td>
<td align="right">1,472,298,975</td>
<td align="right">29.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">633,401,520</td>
<td align="right">10.7%</td>
<td align="right">664,210,614</td>
<td align="right">11.3%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,796,300,913</td>
<td align="right">30.2%</td>
<td align="right">1,851,585,062</td>
<td align="right">31.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,378,539,696</td>
<td align="right">23.2%</td>
<td align="right">1,337,870,792</td>
<td align="right">22.8%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">801,928</td>
<td align="right">0.2%</td>
<td align="right">786,034</td>
<td align="right">0.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,218,261,992</td>
<td align="right">23.9%</td>
<td align="right">1,203,359,076</td>
<td align="right">23.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">262,313,332</td>
<td align="right"></td>
<td align="right">263,351,890</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">142,401,507</td>
<td align="right"></td>
<td align="right">141,926,413</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">233,116,712</td>
<td align="right">45.3%</td>
<td align="right">233,000,388</td>
<td align="right">45.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,764,554</td>
<td align="right"></td>
<td align="right">245,647,689</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,305,909</td>
<td align="right">45.1%</td>
<td align="right">232,205,476</td>
<td align="right">45.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,875</td>
<td align="right">0.0%</td>
<td align="right">8,878</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,330</td>
<td align="right"></td>
<td align="right">866,194</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">281,740,002</td>
<td align="right">54.7%</td>
<td align="right">281,748,718</td>
<td align="right">54.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,771,895</td>
<td align="right"></td>
<td align="right">281,780,609</td>
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
<td align="right">92</td>
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
<td align="right">58,499</td>
<td align="right">48.4%</td>
<td align="right">28,299</td>
<td align="right">35.1%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,097</td>
<td align="right">0.9%</td>
<td align="right">551</td>
<td align="right">0.7%</td>
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
<td align="right">120,851</td>
<td align="right"></td>
<td align="right">80,638</td>
<td align="right"></td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,336</td>
<td align="right">1.1%</td>
<td align="right">990</td>
<td align="right">1.2%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">59,228</td>
<td align="right">49.0%</td>
<td align="right">48,804</td>
<td align="right">60.5%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">286,205,481</td>
<td align="right"></td>
<td align="right">238,571,585</td>
<td align="right"></td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">62,352</td>
<td align="right">51.6%</td>
<td align="right">52,339</td>
<td align="right">64.9%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,330,044,406</td>
<td align="right">1,512.9%</td>
<td align="right">3,806,107,092</td>
<td align="right">1,595.4%</td>
<td align="right">-12.1%</td>
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
<td align="right">58,499</td>
<td align="right"></td>
<td align="right">28,299</td>
<td align="right"></td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">55,606</td>
<td align="right">95.1%</td>
<td align="right">27,114</td>
<td align="right">95.8%</td>
<td align="right">-51.2%</td>
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
<td align="right">5,265</td>
<td align="right">9.0%</td>
<td align="right">3,505</td>
<td align="right">12.4%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,563</td>
<td align="right">14.6%</td>
<td align="right">5,213</td>
<td align="right">18.4%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">23,569</td>
<td align="right">40.3%</td>
<td align="right">9,525</td>
<td align="right">33.7%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">14,037</td>
<td align="right">24.0%</td>
<td align="right">5,953</td>
<td align="right">21.0%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,337</td>
<td align="right">10.8%</td>
<td align="right">3,420</td>
<td align="right">12.1%</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">728</td>
<td align="right">1.2%</td>
<td align="right">683</td>
<td align="right">2.4%</td>
<td align="right">-6.2%</td>
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
<td align="right">918</td>
<td align="right">1.6%</td>
<td align="right">658</td>
<td align="right">2.3%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,894</td>
<td align="right">11.8%</td>
<td align="right">4,379</td>
<td align="right">15.5%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,504</td>
<td align="right">23.1%</td>
<td align="right">6,414</td>
<td align="right">22.7%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,069</td>
<td align="right">37.7%</td>
<td align="right">9,235</td>
<td align="right">32.6%</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,820</td>
<td align="right">18.5%</td>
<td align="right">5,679</td>
<td align="right">20.1%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,368</td>
<td align="right">2.3%</td>
<td align="right">606</td>
<td align="right">2.1%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">33</td>
<td align="right">0.1%</td>
<td align="right">143</td>
<td align="right">0.5%</td>
<td align="right">333.3%</td>
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
<td align="right">10</td>
<td align="right">630</td>
<td align="right">6,200.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">10</td>
<td align="right">630</td>
<td align="right">6,200.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">10</td>
<td align="right">630</td>
<td align="right">6,200.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">3,084</td>
<td align="right">15,080</td>
<td align="right">389.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">17,830</td>
<td align="right">45,916</td>
<td align="right">157.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">644,075</td>
<td align="right">271</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">286,481</td>
<td align="right">744</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">317,518</td>
<td align="right">11,067</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">673,423</td>
<td align="right">25,977</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,516</td>
<td align="right">80</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,504</td>
<td align="right">80</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right">666</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">294,613</td>
<td align="right">62,748</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">294,456</td>
<td align="right">62,748</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">31,665</td>
<td align="right">9,072</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">481,347</td>
<td align="right">150,357</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">64,514</td>
<td align="right">25,998</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">186,733</td>
<td align="right">285,119</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,286,962</td>
<td align="right">5,083,716</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,398,641</td>
<td align="right">4,477,263</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">236,300</td>
<td align="right">127,866</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">620,254</td>
<td align="right">337,552</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">481,525</td>
<td align="right">262,252</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">758,526</td>
<td align="right">429,187</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,859,950</td>
<td align="right">2,210,125</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,794,158</td>
<td align="right">2,210,125</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,151,400</td>
<td align="right">22,848,235</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">11,535,185</td>
<td align="right">6,950,461</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,302,488</td>
<td align="right">807,123</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,195,577</td>
<td align="right">1,383,649</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">654,292</td>
<td align="right">415,093</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">30,625</td>
<td align="right">19,471</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,247,024</td>
<td align="right">3,369,564</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,480,165</td>
<td align="right">963,663</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,181,973</td>
<td align="right">775,612</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,401,879</td>
<td align="right">4,265,323</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">325,458</td>
<td align="right">217,640</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,036,151</td>
<td align="right">732,658</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,344,048</td>
<td align="right">7,362,547</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,086,993</td>
<td align="right">11,502,645</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">756,281</td>
<td align="right">547,037</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,444,746</td>
<td align="right">12,772,266</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,194,062</td>
<td align="right">874,531</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,568,926</td>
<td align="right">11,573,645</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,440,202</td>
<td align="right">7,763,406</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,908,544</td>
<td align="right">27,461,164</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">132,988</td>
<td align="right">99,605</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">131,495</td>
<td align="right">99,488</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,481,898</td>
<td align="right">1,143,856</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">987,738</td>
<td align="right">775,590</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,473,444</td>
<td align="right">4,313,697</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,882,949</td>
<td align="right">3,109,362</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">36,204,134</td>
<td align="right">29,026,447</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">534,305</td>
<td align="right">429,583</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">157,310,386</td>
<td align="right">128,131,492</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">57,928,728</td>
<td align="right">47,290,766</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">106,508,922</td>
<td align="right">86,988,302</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">259,898,180</td>
<td align="right">213,794,551</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,152,678</td>
<td align="right">29,789,203</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">78,451,179</td>
<td align="right">65,001,442</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">286,205,481</td>
<td align="right">238,571,585</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">861,028</td>
<td align="right">724,920</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">920,480</td>
<td align="right">775,590</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">61,090,211</td>
<td align="right">51,551,247</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,884,279</td>
<td align="right">3,302,760</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">491,713</td>
<td align="right">418,518</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">491,713</td>
<td align="right">418,518</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">318,073,583</td>
<td align="right">271,380,432</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">3,865,610</td>
<td align="right">3,313,687</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,969,109</td>
<td align="right">5,670,423</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,056,376</td>
<td align="right">11,239,390</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,047,308</td>
<td align="right">5,209,797</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,561,163</td>
<td align="right">9,982,323</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,487,067</td>
<td align="right">22,031,516</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">53,958,340</td>
<td align="right">46,652,437</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">11,415,198</td>
<td align="right">9,871,952</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,112,254</td>
<td align="right">15,667,344</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">13,187,035</td>
<td align="right">11,420,584</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">13,187,035</td>
<td align="right">11,420,584</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,042,705</td>
<td align="right">2,660,903</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">36,525,084</td>
<td align="right">31,992,874</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">36,426,218</td>
<td align="right">31,992,874</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">18,527,424</td>
<td align="right">16,277,227</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">19,800,831</td>
<td align="right">17,402,774</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">4,204,823</td>
<td align="right">3,720,089</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">46,016,827</td>
<td align="right">40,768,377</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">21,095,305</td>
<td align="right">18,719,492</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">10,059,761</td>
<td align="right">8,929,594</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">21,370,764</td>
<td align="right">18,975,252</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,450,381</td>
<td align="right">3,070,720</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,552,209</td>
<td align="right">18,303,213</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">3,477,095</td>
<td align="right">3,100,657</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">47,469,496</td>
<td align="right">42,338,162</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">34,406,220</td>
<td align="right">30,696,941</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">8,990,449</td>
<td align="right">8,023,759</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">18,877,608</td>
<td align="right">16,867,218</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,546,311</td>
<td align="right">2,284,849</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">404,708,267</td>
<td align="right">363,896,893</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,705,684</td>
<td align="right">1,537,333</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">319,710,993</td>
<td align="right">289,231,977</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,194,780</td>
<td align="right">3,795,557</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,513,612</td>
<td align="right">11,394,607</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">173,136,895</td>
<td align="right">157,799,657</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,791,226</td>
<td align="right">12,608,273</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,746,989</td>
<td align="right">2,533,315</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">420,309</td>
<td align="right">387,795</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,862,899</td>
<td align="right">7,259,670</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,909,505</td>
<td align="right">73,832,342</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">40,059,651</td>
<td align="right">37,028,535</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">10,933,464</td>
<td align="right">10,107,175</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,032,959</td>
<td align="right">10,204,616</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">10,465,852</td>
<td align="right">9,698,201</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">30,094,075</td>
<td align="right">27,985,553</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,210,365</td>
<td align="right">7,638,000</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">97,490,945</td>
<td align="right">90,894,183</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,952,868</td>
<td align="right">20,233,800</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">40,892,180</td>
<td align="right">38,170,424</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">7,901,933</td>
<td align="right">7,387,898</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">31,941,303</td>
<td align="right">29,917,506</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,943,089</td>
<td align="right">6,515,728</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">16,008,971</td>
<td align="right">15,055,455</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,305,147</td>
<td align="right">26,682,106</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,196,581</td>
<td align="right">13,399,192</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">28,291,506</td>
<td align="right">26,724,398</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,301,700</td>
<td align="right">16,353,823</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,040,376</td>
<td align="right">24,629,697</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">441,082</td>
<td align="right">418,120</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">34,444,012</td>
<td align="right">32,687,091</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">45,681,938</td>
<td align="right">43,496,389</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">37,752,944</td>
<td align="right">36,035,002</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">27,816,289</td>
<td align="right">26,585,987</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">11,994,590</td>
<td align="right">11,467,343</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">88,023,701</td>
<td align="right">84,190,730</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,235,655</td>
<td align="right">47,176,905</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">61,058,745</td>
<td align="right">58,751,183</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">15,711,729</td>
<td align="right">15,129,312</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,431,956</td>
<td align="right">13,951,470</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">49,042,545</td>
<td align="right">47,418,185</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,484,367</td>
<td align="right">1,437,871</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,484,367</td>
<td align="right">1,437,871</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">31,868,102</td>
<td align="right">32,808,847</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">20,619,749</td>
<td align="right">20,037,001</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">46,338,441</td>
<td align="right">45,133,836</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,983,424</td>
<td align="right">7,778,775</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,983,424</td>
<td align="right">7,778,775</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,655,923</td>
<td align="right">19,219,659</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">7,399,041</td>
<td align="right">7,246,080</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,435,090</td>
<td align="right">7,285,108</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">332,365</td>
<td align="right">325,744</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,881,962</td>
<td align="right">5,766,479</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">11,164,228</td>
<td align="right">10,977,861</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">31,519,466</td>
<td align="right">31,054,322</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,552,449</td>
<td align="right">7,468,927</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,552,449</td>
<td align="right">7,468,927</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,095,657</td>
<td align="right">22,854,384</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">7,238,387</td>
<td align="right">7,205,362</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,517,946</td>
<td align="right">2,513,410</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,413,449</td>
<td align="right">13,398,895</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,515,365</td>
<td align="right">2,513,934</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,666,981</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">871,373</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">782,715</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">334,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">334,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">286,003</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">286,003</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">76,607</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">58,049</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">24,689</td>
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
<td align="right">4,090</td>
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
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">1,325</td>
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
<td align="left">SEND</td>
<td align="right">278</td>
<td align="right">42</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">64</td>
<td align="right">42</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">10,956</td>
<td align="right">7,812</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,697</td>
<td align="right">5,573</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">364</td>
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
Stats gathered on: 2024-11-14
