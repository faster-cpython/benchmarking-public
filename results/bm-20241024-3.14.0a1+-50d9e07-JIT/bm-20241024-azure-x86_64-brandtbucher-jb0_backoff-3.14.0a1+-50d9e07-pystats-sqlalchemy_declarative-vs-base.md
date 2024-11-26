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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,305,741</td>
<td align="right">11,998,657</td>
<td align="right">263.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">14,768</td>
<td align="right">43,989</td>
<td align="right">197.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,224,000</td>
<td align="right">42</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">18,120</td>
<td align="right">1</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">828,600</td>
<td align="right">63</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">181,114</td>
<td align="right">60</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,781</td>
<td align="right">21</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">303,040</td>
<td align="right">8,163</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">13,022,424</td>
<td align="right">618,443</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">708,480</td>
<td align="right">55,806</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">66,900</td>
<td align="right">6,180</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">66,900</td>
<td align="right">6,180</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,366,801</td>
<td align="right">129,251</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,949,827</td>
<td align="right">754,523</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">718,980</td>
<td align="right">94,624</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,605,560</td>
<td align="right">264,615</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,571,299</td>
<td align="right">1,103,020</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,363,960</td>
<td align="right">231,307</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,786,200</td>
<td align="right">306,242</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,585,204</td>
<td align="right">273,040</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,564,020</td>
<td align="right">270,130</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,267,921</td>
<td align="right">231,128</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,254,320</td>
<td align="right">232,833</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,719,381</td>
<td align="right">742,742</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,964,043</td>
<td align="right">437,985</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,099,680</td>
<td align="right">246,548</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">170,880</td>
<td align="right">39,783</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,592,880</td>
<td align="right">377,714</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">835,795</td>
<td align="right">198,501</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">243,500</td>
<td align="right">57,847</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">30,120</td>
<td align="right">7,560</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,134,186</td>
<td align="right">287,559</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">46,741</td>
<td align="right">12,000</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,640,540</td>
<td align="right">690,321</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,435,022</td>
<td align="right">377,246</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,805,743</td>
<td align="right">501,772</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">160,700</td>
<td align="right">45,923</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,015,509</td>
<td align="right">585,284</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,392,900</td>
<td align="right">418,037</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,777,745</td>
<td align="right">3,691,645</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">181,320</td>
<td align="right">58,022</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,455,520</td>
<td align="right">466,136</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,626,051</td>
<td align="right">1,831,068</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">454,040</td>
<td align="right">149,486</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">14,800,422</td>
<td align="right">4,963,584</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,300,160</td>
<td align="right">477,141</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">162,120</td>
<td align="right">60,182</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,150,670</td>
<td align="right">1,605,695</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,894,672</td>
<td align="right">764,801</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,704,428</td>
<td align="right">1,132,990</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,400,798</td>
<td align="right">2,874,452</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,683,809</td>
<td align="right">2,160,831</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">90,240</td>
<td align="right">42,121</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">71,804,958</td>
<td align="right">34,016,165</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">7,615,600</td>
<td align="right">3,610,965</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">424,640</td>
<td align="right">206,984</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,735,140</td>
<td align="right">856,108</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">182,820</td>
<td align="right">90,242</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,214,834</td>
<td align="right">603,418</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">71,440</td>
<td align="right">35,640</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,000</td>
<td align="right">12,000</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">96,240</td>
<td align="right">48,121</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">297,260</td>
<td align="right">149,162</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">297,660</td>
<td align="right">158,766</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">120,920</td>
<td align="right">64,580</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,447,651</td>
<td align="right">790,396</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,220</td>
<td align="right">95,420</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">479,740</td>
<td align="right">263,124</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">96,660</td>
<td align="right">54,301</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,348,120</td>
<td align="right">9,250,511</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,876,836</td>
<td align="right">5,028,559</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,005,506</td>
<td align="right">2,338,552</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">71,460</td>
<td align="right">41,880</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">422,162</td>
<td align="right">255,442</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,221,827</td>
<td align="right">1,352,008</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">168,240</td>
<td align="right">106,022</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">179,640</td>
<td align="right">114,182</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">331,320</td>
<td align="right">214,861</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">24,000</td>
<td align="right">15,780</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">147,196</td>
<td align="right">97,917</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,240</td>
<td align="right">24,120</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">18,240</td>
<td align="right">12,240</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,919,456</td>
<td align="right">3,327,033</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,003,100</td>
<td align="right">3,411,168</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,667,194</td>
<td align="right">4,855,400</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,732,834</td>
<td align="right">1,264,404</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,313,997</td>
<td align="right">1,698,569</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,850,464</td>
<td align="right">11,151,534</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,310,208</td>
<td align="right">1,754,330</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">329,441</td>
<td align="right">253,862</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">30,160</td>
<td align="right">24,160</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,547,443</td>
<td align="right">8,550,337</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,744,837</td>
<td align="right">3,918,333</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,926,060</td>
<td align="right">1,598,161</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">72,240</td>
<td align="right">60,240</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">222,958</td>
<td align="right">189,192</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">115,080</td>
<td align="right">98,402</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">62,140</td>
<td align="right">70,232</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">100,140</td>
<td align="right">88,141</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">254,160</td>
<td align="right">224,341</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">49,696</td>
<td align="right">43,977</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">6,892,500</td>
<td align="right">6,172,581</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,424,180</td>
<td align="right">1,277,181</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">708,602</td>
<td align="right">642,361</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">978,083</td>
<td align="right">892,023</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,073,940</td>
<td align="right">1,011,123</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">13,202,932</td>
<td align="right">12,825,717</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,187,942</td>
<td align="right">8,107,081</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">12,240</td>
<td align="right">12,120</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">702,120</td>
<td align="right">708,359</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">182,543</td>
<td align="right">181,941</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,762,980</td>
<td align="right">4,756,621</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">366,120</td>
<td align="right">366,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">270,000</td>
<td align="right">270,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">241,920</td>
<td align="right">241,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">45,900</td>
<td align="right">45,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">30,120</td>
<td align="right">30,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">24,180</td>
<td align="right">24,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">24,120</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">24,000</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,000</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,000</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">24,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">18,000</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,600</td>
<td align="right">12,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,080</td>
<td align="right">12,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,000</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">12,000</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">12,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">12,000</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">10,621</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">420,802</td>
<td align="right">80.2%</td>
<td align="right">254,482</td>
<td align="right">71.1%</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">102,480</td>
<td align="right">19.5%</td>
<td align="right">102,480</td>
<td align="right">28.6%</td>
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
<td align="right">1,320</td>
<td align="right">97.1%</td>
<td align="right">920</td>
<td align="right">95.8%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">2.9%</td>
<td align="right">40</td>
<td align="right">4.2%</td>
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
<td align="left">remainder</td>
<td align="right">80</td>
<td align="right">6.1%</td>
<td align="right">40</td>
<td align="right">4.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">3.0%</td>
<td align="right">20</td>
<td align="right">2.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">180</td>
<td align="right">13.6%</td>
<td align="right">100</td>
<td align="right">10.9%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">500</td>
<td align="right">37.9%</td>
<td align="right">300</td>
<td align="right">32.6%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">160</td>
<td align="right">12.1%</td>
<td align="right">100</td>
<td align="right">10.9%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">24.2%</td>
<td align="right">320</td>
<td align="right">34.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">40</td>
<td align="right">3.0%</td>
<td align="right">40</td>
<td align="right">4.3%</td>
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
<td align="right">328,021</td>
<td align="right">4.8%</td>
<td align="right">252,722</td>
<td align="right">3.8%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,441,660</td>
<td align="right">95.1%</td>
<td align="right">6,441,660</td>
<td align="right">96.2%</td>
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
<td align="right">1,300</td>
<td align="right">91.5%</td>
<td align="right">1,020</td>
<td align="right">89.5%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">8.5%</td>
<td align="right">120</td>
<td align="right">10.5%</td>
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
<td align="right">1,100</td>
<td align="right">84.6%</td>
<td align="right">900</td>
<td align="right">88.2%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">80</td>
<td align="right">6.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">80</td>
<td align="right">6.2%</td>
<td align="right">80</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">40</td>
<td align="right">3.9%</td>
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
<td align="right">360,101</td>
<td align="right">2.3%</td>
<td align="right">292,441</td>
<td align="right">1.9%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,251,819</td>
<td align="right">97.6%</td>
<td align="right">15,296,319</td>
<td align="right">98.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,120</td>
<td align="right">0.1%</td>
<td align="right">12,120</td>
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
<td align="right">7,460</td>
<td align="right">98.2%</td>
<td align="right">6,220</td>
<td align="right">97.8%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">140</td>
<td align="right">1.8%</td>
<td align="right">140</td>
<td align="right">2.2%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">12,000</td>
<td align="right">60.2%</td>
<td align="right">12,000</td>
<td align="right">60.2%</td>
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
<td align="right">7,840</td>
<td align="right">39.4%</td>
<td align="right">7,840</td>
<td align="right">39.4%</td>
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
<td align="right">120,480</td>
<td align="right">45.4%</td>
<td align="right">64,260</td>
<td align="right">30.7%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">144,480</td>
<td align="right">54.4%</td>
<td align="right">144,480</td>
<td align="right">69.1%</td>
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
<td align="right">440</td>
<td align="right">100.0%</td>
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">-27.3%</td>
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
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">18.2%</td>
<td align="right">40</td>
<td align="right">12.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">200</td>
<td align="right">45.5%</td>
<td align="right">160</td>
<td align="right">50.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">80</td>
<td align="right">18.2%</td>
<td align="right">80</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">9.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">9.1%</td>
<td align="right">40</td>
<td align="right">12.5%</td>
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
<td align="right">1,365,721</td>
<td align="right">37.7%</td>
<td align="right">128,651</td>
<td align="right">5.4%</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,253,522</td>
<td align="right">62.1%</td>
<td align="right">2,253,327</td>
<td align="right">94.3%</td>
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
<td align="right">6,000</td>
<td align="right">0.2%</td>
<td align="right">6,000</td>
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
<td align="right">1,080</td>
<td align="right">90.0%</td>
<td align="right">600</td>
<td align="right">83.3%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">10.0%</td>
<td align="right">120</td>
<td align="right">16.7%</td>
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
<td align="right">520</td>
<td align="right">48.1%</td>
<td align="right">220</td>
<td align="right">36.7%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">520</td>
<td align="right">48.1%</td>
<td align="right">340</td>
<td align="right">56.7%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">40</td>
<td align="right">3.7%</td>
<td align="right">40</td>
<td align="right">6.7%</td>
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
<td align="right">1,453,140</td>
<td align="right">43.4%</td>
<td align="right">464,536</td>
<td align="right">27.3%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,885,254</td>
<td align="right">56.3%</td>
<td align="right">1,225,479</td>
<td align="right">72.1%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,480</td>
<td align="right">0.3%</td>
<td align="right">8,480</td>
<td align="right">0.5%</td>
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
<td align="right">2,300</td>
<td align="right">90.6%</td>
<td align="right">1,520</td>
<td align="right">86.4%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">9.4%</td>
<td align="right">240</td>
<td align="right">13.6%</td>
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
<td align="right">140</td>
<td align="right">6.1%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">260</td>
<td align="right">11.3%</td>
<td align="right">120</td>
<td align="right">7.9%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">80</td>
<td align="right">3.5%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">200</td>
<td align="right">8.7%</td>
<td align="right">120</td>
<td align="right">7.9%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">120</td>
<td align="right">5.2%</td>
<td align="right">80</td>
<td align="right">5.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,200</td>
<td align="right">52.2%</td>
<td align="right">840</td>
<td align="right">55.3%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">220</td>
<td align="right">9.6%</td>
<td align="right">200</td>
<td align="right">13.2%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
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
<td align="right">6,381,764</td>
<td align="right">14.6%</td>
<td align="right">2,862,412</td>
<td align="right">7.3%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,088,128</td>
<td align="right">7.0%</td>
<td align="right">2,906,640</td>
<td align="right">7.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,327,737</td>
<td align="right">78.3%</td>
<td align="right">33,535,316</td>
<td align="right">85.3%</td>
<td align="right">-2.3%</td>
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
<td align="right">13,922</td>
<td align="right">17.9%</td>
<td align="right">9,980</td>
<td align="right">14.8%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,998</td>
<td align="right">82.1%</td>
<td align="right">57,480</td>
<td align="right">85.2%</td>
<td align="right">-10.2%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">540</td>
<td align="right">3.9%</td>
<td align="right">60</td>
<td align="right">0.6%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">140</td>
<td align="right">1.0%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">120</td>
<td align="right">1.2%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,300</td>
<td align="right">9.3%</td>
<td align="right">820</td>
<td align="right">8.2%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">520</td>
<td align="right">3.7%</td>
<td align="right">340</td>
<td align="right">3.4%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">7,362</td>
<td align="right">52.9%</td>
<td align="right">5,220</td>
<td align="right">52.3%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,320</td>
<td align="right">9.5%</td>
<td align="right">960</td>
<td align="right">9.6%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,160</td>
<td align="right">15.5%</td>
<td align="right">2,120</td>
<td align="right">21.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">10,633,636</td>
<td align="right">100.0%</td>
<td align="right">3,083,471</td>
<td align="right">100.0%</td>
<td align="right">-71.0%</td>
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
<td align="right">260</td>
<td align="right">100.0%</td>
<td align="right">260</td>
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
<td align="right">12,240</td>
<td align="right">100.0%</td>
<td align="right">12,240</td>
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
<td align="right">7,611,180</td>
<td align="right">52.0%</td>
<td align="right">3,608,405</td>
<td align="right">34.0%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">358,900</td>
<td align="right">2.5%</td>
<td align="right">236,707</td>
<td align="right">2.2%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,659,380</td>
<td align="right">45.5%</td>
<td align="right">6,760,054</td>
<td align="right">63.7%</td>
<td align="right">1.5%</td>
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
<td align="right">4,420</td>
<td align="right">39.4%</td>
<td align="right">2,560</td>
<td align="right">35.9%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,800</td>
<td align="right">60.6%</td>
<td align="right">4,580</td>
<td align="right">64.1%</td>
<td align="right">-32.6%</td>
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
<td align="left">split dict</td>
<td align="right">120</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">1.6%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,180</td>
<td align="right">71.9%</td>
<td align="right">1,880</td>
<td align="right">73.4%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">480</td>
<td align="right">10.9%</td>
<td align="right">360</td>
<td align="right">14.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">160</td>
<td align="right">3.6%</td>
<td align="right">120</td>
<td align="right">4.7%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">320</td>
<td align="right">7.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">2.7%</td>
<td align="right">120</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">40</td>
<td align="right">0.9%</td>
<td align="right">40</td>
<td align="right">1.6%</td>
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
<td align="right">28,621</td>
<td align="right">1.2%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,263,380</td>
<td align="right">98.7%</td>
<td align="right">2,263,380</td>
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
<td align="left">Failure</td>
<td align="right">140</td>
<td align="right">87.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
<td align="right">100</td>
<td align="right">71.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">40</td>
<td align="right">28.6%</td>
<td align="right"></td>
<td align="right"></td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,726,988</td>
<td align="right">9.6%</td>
<td align="right">1,259,744</td>
<td align="right">7.3%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">137,183</td>
<td align="right">0.8%</td>
<td align="right">125,843</td>
<td align="right">0.7%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,050,382</td>
<td align="right">89.6%</td>
<td align="right">15,959,882</td>
<td align="right">92.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">5,766</td>
<td align="right">67.9%</td>
<td align="right">4,580</td>
<td align="right">64.9%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,725</td>
<td align="right">32.1%</td>
<td align="right">2,480</td>
<td align="right">35.1%</td>
<td align="right">-9.0%</td>
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
<td align="left">dict</td>
<td align="right">600</td>
<td align="right">10.4%</td>
<td align="right">300</td>
<td align="right">6.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">620</td>
<td align="right">10.8%</td>
<td align="right">340</td>
<td align="right">7.4%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">180</td>
<td align="right">3.1%</td>
<td align="right">140</td>
<td align="right">3.1%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,600</td>
<td align="right">27.7%</td>
<td align="right">1,260</td>
<td align="right">27.5%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,280</td>
<td align="right">22.2%</td>
<td align="right">1,040</td>
<td align="right">22.7%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">563</td>
<td align="right">9.8%</td>
<td align="right">660</td>
<td align="right">14.4%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">923</td>
<td align="right">16.0%</td>
<td align="right">840</td>
<td align="right">18.3%</td>
<td align="right">-9.0%</td>
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
<td align="right">24,120</td>
<td align="right">0.6%</td>
<td align="right">24,120</td>
<td align="right">0.6%</td>
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
<td align="right">4,329,060</td>
<td align="right">99.4%</td>
<td align="right">4,329,060</td>
<td align="right">99.4%</td>
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
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">103,443,686</td>
<td align="right">30.9%</td>
<td align="right">37,741,168</td>
<td align="right">20.7%</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">19,521,977</td>
<td align="right">5.8%</td>
<td align="right">8,968,233</td>
<td align="right">4.9%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">208,372,672</td>
<td align="right">62.1%</td>
<td align="right">131,875,709</td>
<td align="right">72.4%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">3,966,641</td>
<td align="right">1.2%</td>
<td align="right">3,584,114</td>
<td align="right">2.0%</td>
<td align="right">-9.6%</td>
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
<td align="right">1,365,721</td>
<td align="right">7.0%</td>
<td align="right">128,651</td>
<td align="right">1.4%</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,453,140</td>
<td align="right">7.5%</td>
<td align="right">464,536</td>
<td align="right">5.2%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,381,764</td>
<td align="right">32.8%</td>
<td align="right">2,862,412</td>
<td align="right">32.0%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">7,611,180</td>
<td align="right">39.1%</td>
<td align="right">3,608,405</td>
<td align="right">40.3%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">120,480</td>
<td align="right">0.6%</td>
<td align="right">64,260</td>
<td align="right">0.7%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">420,802</td>
<td align="right">2.2%</td>
<td align="right">254,482</td>
<td align="right">2.8%</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,726,988</td>
<td align="right">8.9%</td>
<td align="right">1,259,744</td>
<td align="right">14.1%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">328,021</td>
<td align="right">1.7%</td>
<td align="right">252,722</td>
<td align="right">2.8%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,621</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">24,120</td>
<td align="right">0.1%</td>
<td align="right">24,120</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">12,120</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">216,060</td>
<td align="right">5.4%</td>
<td align="right">109,800</td>
<td align="right">3.1%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">126,401</td>
<td align="right">3.2%</td>
<td align="right">85,080</td>
<td align="right">2.4%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">306,300</td>
<td align="right">7.7%</td>
<td align="right">223,987</td>
<td align="right">6.2%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">51,740</td>
<td align="right">1.3%</td>
<td align="right">40,083</td>
<td align="right">1.1%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">119,648</td>
<td align="right">3.0%</td>
<td align="right">112,880</td>
<td align="right">3.1%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">534,160</td>
<td align="right">13.5%</td>
<td align="right">521,280</td>
<td align="right">14.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,245,320</td>
<td align="right">31.4%</td>
<td align="right">1,217,580</td>
<td align="right">34.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">869,460</td>
<td align="right">21.9%</td>
<td align="right">865,140</td>
<td align="right">24.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">178,220</td>
<td align="right">4.5%</td>
<td align="right">178,220</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">52,600</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">36,400</td>
<td align="right">1.0%</td>
<td align="right"></td>
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
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,438,800</td>
<td align="right">28.9%</td>
<td align="right">4,432,441</td>
<td align="right">28.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,438,800</td>
<td align="right">28.9%</td>
<td align="right">4,432,441</td>
<td align="right">28.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,763,040</td>
<td align="right">31.1%</td>
<td align="right">4,756,681</td>
<td align="right">31.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,763,040</td>
<td align="right">31.1%</td>
<td align="right">4,756,681</td>
<td align="right">31.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">10,570,620</td>
<td align="right">68.9%</td>
<td align="right">10,576,979</td>
<td align="right">69.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">15,147,540</td>
<td align="right">98.8%</td>
<td align="right">15,153,779</td>
<td align="right">98.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">432,480</td>
<td align="right">2.8%</td>
<td align="right">432,360</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">324,240</td>
<td align="right">2.1%</td>
<td align="right">324,240</td>
<td align="right">2.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">1,284,480</td>
<td align="right">8.4%</td>
<td align="right">1,284,480</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">72,660</td>
<td align="right">0.5%</td>
<td align="right">72,660</td>
<td align="right">0.5%</td>
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
<td align="right">36,000</td>
<td align="right">0.2%</td>
<td align="right">36,000</td>
<td align="right">0.2%</td>
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
<td align="right">157,889,092</td>
<td align="right">34.4%</td>
<td align="right">244,725,289</td>
<td align="right">52.0%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">159,182,527</td>
<td align="right">33.4%</td>
<td align="right">234,516,939</td>
<td align="right">46.3%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">58,424,652</td>
<td align="right">12.7%</td>
<td align="right">33,995,206</td>
<td align="right">7.2%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">158,681,943</td>
<td align="right">34.6%</td>
<td align="right">93,396,651</td>
<td align="right">19.9%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">41,522,809</td>
<td align="right">8.7%</td>
<td align="right">26,267,864</td>
<td align="right">5.2%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">81,741,615</td>
<td align="right">17.1%</td>
<td align="right">105,588,248</td>
<td align="right">20.8%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">194,463,895</td>
<td align="right">40.8%</td>
<td align="right">140,679,838</td>
<td align="right">27.7%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">83,417,742</td>
<td align="right">18.2%</td>
<td align="right">98,249,999</td>
<td align="right">20.9%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">245,409</td>
<td align="right"></td>
<td align="right">205,852</td>
<td align="right"></td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">104,117</td>
<td align="right">0.3%</td>
<td align="right">116,131</td>
<td align="right">0.3%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">826,644</td>
<td align="right"></td>
<td align="right">760,250</td>
<td align="right"></td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">581,235</td>
<td align="right"></td>
<td align="right">554,398</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">12,400</td>
<td align="right">0.0%</td>
<td align="right">12,535</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">18,924,029</td>
<td align="right"></td>
<td align="right">18,719,007</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,897,836</td>
<td align="right"></td>
<td align="right">8,917,312</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">22,325,120</td>
<td align="right">56.1%</td>
<td align="right">22,315,343</td>
<td align="right">56.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,380,000</td>
<td align="right">43.6%</td>
<td align="right">17,373,927</td>
<td align="right">43.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,403,880</td>
<td align="right"></td>
<td align="right">17,398,087</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">24,121,707</td>
<td align="right"></td>
<td align="right">24,126,119</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">22,441,637</td>
<td align="right">56.4%</td>
<td align="right">22,444,009</td>
<td align="right">56.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,622,520</td>
<td align="right"></td>
<td align="right">1,622,520</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">696,720</td>
<td align="right">42.9%</td>
<td align="right">696,720</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">24,120</td>
<td align="right">1.5%</td>
<td align="right">24,120</td>
<td align="right">1.5%</td>
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
<td align="right">20</td>
<td align="right">1,440</td>
<td align="right">140,094</td>
<td align="right">40</td>
<td align="right">2,160</td>
<td align="right">314,560</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,640</td>
<td align="right">21.6%</td>
<td align="right">19,361</td>
<td align="right">39.0%</td>
<td align="right">431.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,760</td>
<td align="right">40.1%</td>
<td align="right">30,012</td>
<td align="right">60.4%</td>
<td align="right">344.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">280</td>
<td align="right">1.7%</td>
<td align="right">926</td>
<td align="right">1.9%</td>
<td align="right">230.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">16,877</td>
<td align="right"></td>
<td align="right">49,696</td>
<td align="right"></td>
<td align="right">194.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">13,197</td>
<td align="right">78.2%</td>
<td align="right">30,275</td>
<td align="right">60.9%</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">253,427,635</td>
<td align="right">2,195.4%</td>
<td align="right">580,732,001</td>
<td align="right">2,259.1%</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">11,543,396</td>
<td align="right"></td>
<td align="right">25,705,947</td>
<td align="right"></td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">543</td>
<td align="right">3.2%</td>
<td align="right">612</td>
<td align="right">1.2%</td>
<td align="right">12.7%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">13,057</td>
<td align="right">98.9%</td>
<td align="right">29,995</td>
<td align="right">99.1%</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">13,197</td>
<td align="right"></td>
<td align="right">30,275</td>
<td align="right"></td>
<td align="right">129.4%</td>
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
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60 / 0 !!</td>
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
<td align="right">768</td>
<td align="right">2.5%</td>
<td align="right">768 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,760</td>
<td align="right">20.9%</td>
<td align="right">3,981</td>
<td align="right">13.1%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,120</td>
<td align="right">16.1%</td>
<td align="right">4,260</td>
<td align="right">14.1%</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,297</td>
<td align="right">25.0%</td>
<td align="right">8,397</td>
<td align="right">27.7%</td>
<td align="right">154.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,999</td>
<td align="right">22.7%</td>
<td align="right">7,351</td>
<td align="right">24.3%</td>
<td align="right">145.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">961</td>
<td align="right">7.3%</td>
<td align="right">3,878</td>
<td align="right">12.8%</td>
<td align="right">303.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">920</td>
<td align="right">7.0%</td>
<td align="right">1,340</td>
<td align="right">4.4%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">300</td>
<td align="right">1.0%</td>
<td align="right">114.3%</td>
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
<td align="right">1,860</td>
<td align="right">14.1%</td>
<td align="right">3,269</td>
<td align="right">10.8%</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,100</td>
<td align="right">15.9%</td>
<td align="right">3,020</td>
<td align="right">10.0%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,460</td>
<td align="right">11.1%</td>
<td align="right">5,321</td>
<td align="right">17.6%</td>
<td align="right">264.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,596</td>
<td align="right">27.2%</td>
<td align="right">9,002</td>
<td align="right">29.7%</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,701</td>
<td align="right">20.5%</td>
<td align="right">6,375</td>
<td align="right">21.1%</td>
<td align="right">136.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">920</td>
<td align="right">7.0%</td>
<td align="right">2,248</td>
<td align="right">7.4%</td>
<td align="right">144.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">420</td>
<td align="right">3.2%</td>
<td align="right">640</td>
<td align="right">2.1%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right"></td>
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
<td align="left">_STORE_ATTR</td>
<td align="right">91,080</td>
<td align="right">4,113,154</td>
<td align="right">4,416.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">61,600</td>
<td align="right">2,446,166</td>
<td align="right">3,871.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">24,000</td>
<td align="right">852,537</td>
<td align="right">3,452.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">92,939</td>
<td align="right">3,183,135</td>
<td align="right">3,325.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,939</td>
<td align="right">3,048,819</td>
<td align="right">3,180.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">30,600</td>
<td align="right">883,732</td>
<td align="right">2,788.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">48,040</td>
<td align="right">1,069,527</td>
<td align="right">2,126.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">6,000</td>
<td align="right">129,298</td>
<td align="right">2,055.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">16,380</td>
<td align="right">343,979</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">468,158</td>
<td align="right">9,743,459</td>
<td align="right">1,981.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">576,098</td>
<td align="right">10,628,433</td>
<td align="right">1,744.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">49,098</td>
<td align="right">856,117</td>
<td align="right">1,643.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">97,080</td>
<td align="right">1,690,752</td>
<td align="right">1,641.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">397,118</td>
<td align="right">5,828,864</td>
<td align="right">1,367.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">128,360</td>
<td align="right">1,876,971</td>
<td align="right">1,362.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">612,700</td>
<td align="right">8,749,536</td>
<td align="right">1,328.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">66,180</td>
<td align="right">895,098</td>
<td align="right">1,252.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">194,066</td>
<td align="right">2,216,226</td>
<td align="right">1,042.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">104,540</td>
<td align="right">1,090,371</td>
<td align="right">943.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,344,584</td>
<td align="right">13,934,227</td>
<td align="right">936.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">92,580</td>
<td align="right">914,335</td>
<td align="right">887.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">12,000</td>
<td align="right">113,938</td>
<td align="right">849.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">12,000</td>
<td align="right">113,938</td>
<td align="right">849.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">11,960</td>
<td align="right">109,078</td>
<td align="right">812.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">174,761</td>
<td align="right">1,411,636</td>
<td align="right">707.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">107,940</td>
<td align="right">824,615</td>
<td align="right">664.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">32,860</td>
<td align="right">250,377</td>
<td align="right">662.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">549,657</td>
<td align="right">4,121,588</td>
<td align="right">649.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">28,780</td>
<td align="right">214,433</td>
<td align="right">645.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">169,138</td>
<td align="right">1,226,914</td>
<td align="right">625.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">3,967,123</td>
<td align="right">28,648,344</td>
<td align="right">622.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">214,920</td>
<td align="right">1,430,086</td>
<td align="right">565.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">16,380</td>
<td align="right">108,958</td>
<td align="right">565.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,225,586</td>
<td align="right">20,939,084</td>
<td align="right">549.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">27,300</td>
<td align="right">174,239</td>
<td align="right">538.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">80,600</td>
<td align="right">510,315</td>
<td align="right">533.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">144,978</td>
<td align="right">904,325</td>
<td align="right">523.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">2,640,431</td>
<td align="right">16,269,191</td>
<td align="right">516.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">42,620</td>
<td align="right">253,595</td>
<td align="right">495.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">62,260</td>
<td align="right">366,814</td>
<td align="right">489.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">124,420</td>
<td align="right">705,109</td>
<td align="right">466.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">124,420</td>
<td align="right">705,109</td>
<td align="right">466.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">25,600</td>
<td align="right">140,377</td>
<td align="right">448.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">48,380</td>
<td align="right">264,996</td>
<td align="right">447.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">33,280</td>
<td align="right">181,378</td>
<td align="right">445.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">137,412</td>
<td align="right">730,181</td>
<td align="right">431.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">313,120</td>
<td align="right">1,433,279</td>
<td align="right">357.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">186,825</td>
<td align="right">839,555</td>
<td align="right">349.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">844,435</td>
<td align="right">3,418,025</td>
<td align="right">304.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,682,133</td>
<td align="right">6,568,097</td>
<td align="right">290.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">45,480</td>
<td align="right">176,577</td>
<td align="right">288.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">385,740</td>
<td align="right">1,476,444</td>
<td align="right">282.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">336,099</td>
<td align="right">1,264,493</td>
<td align="right">276.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">34,400</td>
<td align="right">118,379</td>
<td align="right">244.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,548,444</td>
<td align="right">8,586,153</td>
<td align="right">236.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">29,140</td>
<td align="right">97,460</td>
<td align="right">234.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,400</td>
<td align="right">94,520</td>
<td align="right">232.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">633,700</td>
<td align="right">1,974,645</td>
<td align="right">211.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">24,120</td>
<td align="right">72,239</td>
<td align="right">199.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">24,120</td>
<td align="right">72,239</td>
<td align="right">199.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">689,336</td>
<td align="right">2,001,500</td>
<td align="right">190.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">74,880</td>
<td align="right">213,774</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,148,869</td>
<td align="right">5,943,852</td>
<td align="right">176.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,148,869</td>
<td align="right">5,943,852</td>
<td align="right">176.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,766,484</td>
<td align="right">4,739,976</td>
<td align="right">168.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,144,735</td>
<td align="right">3,038,589</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">102,398</td>
<td align="right">268,718</td>
<td align="right">162.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,456,644</td>
<td align="right">3,725,203</td>
<td align="right">155.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,415,225</td>
<td align="right">3,600,743</td>
<td align="right">154.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">8,220</td>
<td align="right">20,219</td>
<td align="right">146.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">67,619</td>
<td align="right">162,479</td>
<td align="right">140.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,190,990</td>
<td align="right">7,620,714</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">734,937</td>
<td align="right">1,705,130</td>
<td align="right">132.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">11,543,396</td>
<td align="right">25,705,947</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,406,984</td>
<td align="right">3,077,387</td>
<td align="right">118.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">733,614</td>
<td align="right">1,580,241</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">11,020,244</td>
<td align="right">23,475,322</td>
<td align="right">113.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,523,057</td>
<td align="right">5,164,344</td>
<td align="right">104.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,904,231</td>
<td align="right">3,847,969</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">24,490,400</td>
<td align="right">49,123,093</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,590,792</td>
<td align="right">3,162,230</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,718,335</td>
<td align="right">41,045,934</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,315,924</td>
<td align="right">2,596,214</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">80,038</td>
<td align="right">156,198</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,194,988</td>
<td align="right">2,324,759</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">15,204,636</td>
<td align="right">29,303,276</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">165,439</td>
<td align="right">317,978</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,435,131</td>
<td align="right">2,682,986</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,211,946</td>
<td align="right">2,262,495</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">37,620</td>
<td align="right">69,656</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">6,905,857</td>
<td align="right">12,777,273</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">43,499</td>
<td align="right">78,240</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,876,440</td>
<td align="right">3,356,398</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,478,090</td>
<td align="right">6,023,065</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">853,643</td>
<td align="right">1,469,071</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,283,940</td>
<td align="right">2,177,654</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">43,499</td>
<td align="right">72,119</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,976,880</td>
<td align="right">3,270,770</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,842,000</td>
<td align="right">2,973,893</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,843,451</td>
<td align="right">4,583,570</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,323,119</td>
<td align="right">2,033,452</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">963,398</td>
<td align="right">1,465,590</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,744,111</td>
<td align="right">4,174,336</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">36,000</td>
<td align="right">52,678</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,839,264</td>
<td align="right">20,244,557</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,757,654</td>
<td align="right">5,424,608</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">6,481,826</td>
<td align="right">9,332,946</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">2,301,102</td>
<td align="right">3,289,511</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,681,219</td>
<td align="right">2,393,959</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">438,538</td>
<td align="right">253,020</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,346,838</td>
<td align="right">3,186,470</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">772,392</td>
<td align="right">1,046,217</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">18,000</td>
<td align="right">24,000</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">18,000</td>
<td align="right">24,000</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">17,940</td>
<td align="right">23,880</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">198,660</td>
<td align="right">264,118</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">142,640</td>
<td align="right">184,999</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,790,192</td>
<td align="right">2,249,636</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">43,499</td>
<td align="right">54,120</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,796,378</td>
<td align="right">7,205,425</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,252,575</td>
<td align="right">4,002,995</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,160,349</td>
<td align="right">3,817,604</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,840,774</td>
<td align="right">12,874,797</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">229,220</td>
<td align="right">271,579</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">229,220</td>
<td align="right">271,579</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">642,118</td>
<td align="right">755,959</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">489,179</td>
<td align="right">564,478</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,199,666</td>
<td align="right">1,380,720</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,399,666</td>
<td align="right">5,026,603</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,753,528</td>
<td align="right">3,130,743</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,373,709</td>
<td align="right">1,552,350</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">309,840</td>
<td align="right">339,659</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,992,006</td>
<td align="right">8,603,422</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,998,006</td>
<td align="right">8,609,422</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">76,424</td>
<td align="right">82,143</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">120,000</td>
<td align="right">128,220</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">782,864</td>
<td align="right">832,143</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">885,702</td>
<td align="right">915,087</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,661,240</td>
<td align="right">3,597,329</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">1,282,340</td>
<td align="right">1,274,248</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">593,617</td>
<td align="right">594,219</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">30,000</td>
<td align="right">30,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">8,220</td>
<td align="right">8,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">8,220</td>
<td align="right">8,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">1,950,219</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">1,223,958</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">652,554</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">652,554</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">186,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">122,459</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">116,459</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">95,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">95,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">95,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">84,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">72,119</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">72,119</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">62,218</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">60,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">60,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">56,999</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">56,999</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">56,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">36,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">30,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">24,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">24,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">22,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">22,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">18,119</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">16,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">12,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">12,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right"></td>
<td align="right">6,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">6,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">120</td>
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
<td align="right">360</td>
<td align="right">1,340</td>
<td align="right">272.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">420</td>
<td align="right">1,080</td>
<td align="right">157.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
