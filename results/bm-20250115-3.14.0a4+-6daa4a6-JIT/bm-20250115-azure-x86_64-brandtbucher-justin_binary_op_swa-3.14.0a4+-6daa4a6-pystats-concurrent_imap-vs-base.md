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
<td align="right">601,795</td>
<td align="right">662,430</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,662,272</td>
<td align="right">1,827,425</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,233,518</td>
<td align="right">1,355,915</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">851,192</td>
<td align="right">935,500</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,224,591</td>
<td align="right">1,345,851</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">412,128</td>
<td align="right">452,572</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,690,521</td>
<td align="right">1,855,674</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,256,808</td>
<td align="right">4,665,083</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,728,342</td>
<td align="right">1,893,495</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,303,116</td>
<td align="right">1,424,992</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">652,241</td>
<td align="right">712,883</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">434,969</td>
<td align="right">475,384</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">435,292</td>
<td align="right">475,707</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,738,232</td>
<td align="right">6,263,609</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">683,225</td>
<td align="right">743,845</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">932,410</td>
<td align="right">1,013,255</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">236,326</td>
<td align="right">256,548</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">239,365</td>
<td align="right">259,614</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">688,984</td>
<td align="right">746,584</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">242,219</td>
<td align="right">262,434</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,406,471</td>
<td align="right">1,523,720</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,428,953</td>
<td align="right">1,546,717</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,622,831</td>
<td align="right">10,412,379</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,567,661</td>
<td align="right">14,678,824</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,753,163</td>
<td align="right">2,975,583</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,459,789</td>
<td align="right">1,576,967</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">990,564</td>
<td align="right">1,069,711</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,391,658</td>
<td align="right">2,579,778</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,920,902</td>
<td align="right">5,307,381</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,015,326</td>
<td align="right">2,172,973</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,327,827</td>
<td align="right">7,897,959</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,277,349</td>
<td align="right">1,375,933</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,471,483</td>
<td align="right">8,046,866</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,314,175</td>
<td align="right">12,185,370</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,388,453</td>
<td align="right">10,102,316</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,769,523</td>
<td align="right">6,196,976</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,718,928</td>
<td align="right">1,843,446</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,750,612</td>
<td align="right">1,876,570</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,546,725</td>
<td align="right">5,942,163</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,936,774</td>
<td align="right">3,145,317</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,254,143</td>
<td align="right">2,414,085</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,382,834</td>
<td align="right">5,752,142</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">66,109,166</td>
<td align="right">70,539,524</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,360,215</td>
<td align="right">3,584,643</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,979,687</td>
<td align="right">27,641,147</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">343,355</td>
<td align="right">364,152</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,833,386</td>
<td align="right">14,663,432</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,727,350</td>
<td align="right">3,946,817</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,036,640</td>
<td align="right">1,097,268</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,164,808</td>
<td align="right">14,980,240</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,581,504</td>
<td align="right">23,880,211</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,836,948</td>
<td align="right">2,998,624</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,468,014</td>
<td align="right">2,606,891</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,080,401</td>
<td align="right">1,141,032</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,002,293</td>
<td align="right">12,640,610</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,696,678</td>
<td align="right">3,875,160</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,313,172</td>
<td align="right">1,376,171</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">50,365</td>
<td align="right">52,766</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,710,881</td>
<td align="right">4,925,967</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,085,753</td>
<td align="right">7,406,273</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,799,628</td>
<td align="right">20,681,644</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,021,460</td>
<td align="right">1,062,668</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,792,960</td>
<td align="right">9,136,520</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,674,137</td>
<td align="right">8,982,092</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,365,867</td>
<td align="right">3,467,058</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">619,674</td>
<td align="right">637,573</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">89,926</td>
<td align="right">87,343</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">750,298</td>
<td align="right">767,930</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">700,668</td>
<td align="right">715,299</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">697,339</td>
<td align="right">706,102</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">172,602</td>
<td align="right">170,519</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,627,585</td>
<td align="right">1,645,217</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">370,236</td>
<td align="right">373,940</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,310</td>
<td align="right">5,270</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">348</td>
<td align="right">350</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">131,755</td>
<td align="right">132,358</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">482</td>
<td align="right">480</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">78,144</td>
<td align="right">78,464</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,622</td>
<td align="right">1,617</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,708</td>
<td align="right">13,667</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,931</td>
<td align="right">17,890</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,931</td>
<td align="right">17,890</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,545</td>
<td align="right">4,550</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">41,097</td>
<td align="right">41,053</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,865</td>
<td align="right">102,801</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,618</td>
<td align="right">201,502</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,325</td>
<td align="right">97,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">20,725</td>
<td align="right">20,715</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,218</td>
<td align="right">3,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,409</td>
<td align="right">46,397</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,470</td>
<td align="right">21,467</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">204,130</td>
<td align="right">204,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">543,797</td>
<td align="right">543,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,050</td>
<td align="right">34,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,787</td>
<td align="right">928,750</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,660</td>
<td align="right">81,657</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,139</td>
<td align="right">35,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,889</td>
<td align="right">452,877</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">168,815</td>
<td align="right">168,819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,022</td>
<td align="right">191,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,812</td>
<td align="right">115,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,683</td>
<td align="right">1,818,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
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
<td align="right">55,866</td>
<td align="right">55,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,862</td>
<td align="right">55,862</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">21,938</td>
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
<td align="right">5,734,367</td>
<td align="right">76.7%</td>
<td align="right">6,259,508</td>
<td align="right">77.5%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,763</td>
<td align="right">0.3%</td>
<td align="right">21,315</td>
<td align="right">0.3%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,715,885</td>
<td align="right">23.0%</td>
<td align="right">1,792,992</td>
<td align="right">22.2%</td>
<td align="right">4.5%</td>
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
<td align="right">3,754</td>
<td align="right">88.5%</td>
<td align="right">3,991</td>
<td align="right">88.6%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">487</td>
<td align="right">11.5%</td>
<td align="right">516</td>
<td align="right">11.4%</td>
<td align="right">6.0%</td>
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
<td align="right">716</td>
<td align="right">19.1%</td>
<td align="right">776</td>
<td align="right">19.4%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,264</td>
<td align="right">33.7%</td>
<td align="right">1,363</td>
<td align="right">34.2%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,360</td>
<td align="right">36.2%</td>
<td align="right">1,436</td>
<td align="right">36.0%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">291</td>
<td align="right">7.8%</td>
<td align="right">293</td>
<td align="right">7.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">2.9%</td>
<td align="right">109</td>
<td align="right">2.7%</td>
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
<td align="right">618,822</td>
<td align="right">93.8%</td>
<td align="right">659,266</td>
<td align="right">94.1%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,827</td>
<td align="right">6.2%</td>
<td align="right">40,787</td>
<td align="right">5.8%</td>
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
<td align="left">Failure</td>
<td align="right">152</td>
<td align="right">56.3%</td>
<td align="right">148</td>
<td align="right">55.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">43.7%</td>
<td align="right">118</td>
<td align="right">44.4%</td>
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
<td align="right">151</td>
<td align="right">99.3%</td>
<td align="right">147</td>
<td align="right">99.3%</td>
<td align="right">-2.6%</td>
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
<td align="right">25,263,115</td>
<td align="right">100.0%</td>
<td align="right">27,122,068</td>
<td align="right">100.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,209</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">3,337</td>
<td align="right">100.0%</td>
<td align="right">3,351</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">687,630</td>
<td align="right">13.2%</td>
<td align="right">745,193</td>
<td align="right">13.5%</td>
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
<td align="right">4,499,796</td>
<td align="right">86.3%</td>
<td align="right">4,756,777</td>
<td align="right">86.0%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,226</td>
<td align="right">0.5%</td>
<td align="right">28,721</td>
<td align="right">0.5%</td>
<td align="right">1.8%</td>
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
<td align="right">1,088</td>
<td align="right">58.0%</td>
<td align="right">1,124</td>
<td align="right">58.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">789</td>
<td align="right">42.0%</td>
<td align="right">798</td>
<td align="right">41.5%</td>
<td align="right">1.1%</td>
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
<td align="right">797</td>
<td align="right">73.3%</td>
<td align="right">831</td>
<td align="right">73.9%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">150</td>
<td align="right">13.8%</td>
<td align="right">152</td>
<td align="right">13.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">8.8%</td>
<td align="right">96</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.0%</td>
<td align="right">44</td>
<td align="right">3.9%</td>
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
<td align="right">1,836,331</td>
<td align="right">100.0%</td>
<td align="right">1,977,791</td>
<td align="right">100.0%</td>
<td align="right">7.7%</td>
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
<td align="right">6,553,967</td>
<td align="right">98.3%</td>
<td align="right">6,680,528</td>
<td align="right">98.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">115,484</td>
<td align="right">1.7%</td>
<td align="right">115,486</td>
<td align="right">1.7%</td>
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
<td align="right">52</td>
<td align="right">15.9%</td>
<td align="right">51</td>
<td align="right">15.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">276</td>
<td align="right">84.1%</td>
<td align="right">276</td>
<td align="right">84.4%</td>
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
<td align="right">7,460,437</td>
<td align="right">15.2%</td>
<td align="right">8,035,614</td>
<td align="right">15.4%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,255,064</td>
<td align="right">84.0%</td>
<td align="right">43,908,624</td>
<td align="right">83.9%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">384,894</td>
<td align="right">0.8%</td>
<td align="right">385,342</td>
<td align="right">0.7%</td>
<td align="right">0.1%</td>
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
<td align="right">6,545</td>
<td align="right">36.3%</td>
<td align="right">6,747</td>
<td align="right">37.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,487</td>
<td align="right">63.7%</td>
<td align="right">11,502</td>
<td align="right">63.0%</td>
<td align="right">0.1%</td>
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
<td align="right">1,670</td>
<td align="right">25.5%</td>
<td align="right">1,780</td>
<td align="right">26.4%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">792</td>
<td align="right">12.1%</td>
<td align="right">810</td>
<td align="right">12.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,313</td>
<td align="right">20.1%</td>
<td align="right">1,318</td>
<td align="right">19.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">10.4%</td>
<td align="right">681</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">460</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
<td align="right">19,114,077</td>
<td align="right">100.0%</td>
<td align="right">20,620,678</td>
<td align="right">100.0%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">845</td>
<td align="right">0.0%</td>
<td align="right">838</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">2,382</td>
<td align="right">100.0%</td>
<td align="right">2,390</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">2,270,790</td>
<td align="right">100.0%</td>
<td align="right">2,493,095</td>
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
<td align="right">5,301,929</td>
<td align="right">96.0%</td>
<td align="right">5,706,155</td>
<td align="right">96.3%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,937</td>
<td align="right">1.4%</td>
<td align="right">79,936</td>
<td align="right">1.3%</td>
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
<td align="right">140,400</td>
<td align="right">2.5%</td>
<td align="right">140,400</td>
<td align="right">2.4%</td>
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
<td align="right">3,616</td>
<td align="right">83.0%</td>
<td align="right">3,614</td>
<td align="right">82.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.0%</td>
<td align="right">743</td>
<td align="right">17.1%</td>
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
<td align="right">708</td>
<td align="right">95.3%</td>
<td align="right">754</td>
<td align="right">101.5%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
<td align="right">1,901,588</td>
<td align="right">98.9%</td>
<td align="right">2,042,514</td>
<td align="right">99.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,264</td>
<td align="right">1.1%</td>
<td align="right">21,263</td>
<td align="right">1.0%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
<td align="right">187</td>
<td align="right">91.7%</td>
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
<td align="right">12,552,608</td>
<td align="right">98.6%</td>
<td align="right">13,665,234</td>
<td align="right">98.8%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">171,399</td>
<td align="right">1.3%</td>
<td align="right">169,314</td>
<td align="right">1.2%</td>
<td align="right">-1.2%</td>
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
<td align="right">747</td>
<td align="right">62.1%</td>
<td align="right">749</td>
<td align="right">62.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">456</td>
<td align="right">37.9%</td>
<td align="right">456</td>
<td align="right">37.8%</td>
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
<td align="left">mapping</td>
<td align="right">301</td>
<td align="right">40.3%</td>
<td align="right">304</td>
<td align="right">40.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">143</td>
<td align="right">19.1%</td>
<td align="right">142</td>
<td align="right">19.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">126</td>
<td align="right">16.9%</td>
<td align="right">126</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">14.9%</td>
<td align="right">111</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">8.7%</td>
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
<td align="right">2,153,516</td>
<td align="right">100.0%</td>
<td align="right">2,193,924</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="right">14,353,712</td>
<td align="right">3.8%</td>
<td align="right">15,509,946</td>
<td align="right">3.9%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">134,439,437</td>
<td align="right">36.1%</td>
<td align="right">143,420,029</td>
<td align="right">36.2%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">223,553,308</td>
<td align="right">59.9%</td>
<td align="right">236,814,563</td>
<td align="right">59.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">574,473</td>
<td align="right">0.2%</td>
<td align="right">576,977</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
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
<td align="right">5,734,367</td>
<td align="right">40.0%</td>
<td align="right">6,259,508</td>
<td align="right">40.4%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">687,630</td>
<td align="right">4.8%</td>
<td align="right">745,193</td>
<td align="right">4.8%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,460,437</td>
<td align="right">52.1%</td>
<td align="right">8,035,614</td>
<td align="right">51.9%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">171,399</td>
<td align="right">1.2%</td>
<td align="right">169,314</td>
<td align="right">1.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,209</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,827</td>
<td align="right">0.3%</td>
<td align="right">40,787</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">21,263</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,484</td>
<td align="right">0.8%</td>
<td align="right">115,486</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.6%</td>
<td align="right">79,936</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">19,763</td>
<td align="right">3.4%</td>
<td align="right">21,315</td>
<td align="right">3.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">28,225</td>
<td align="right">4.9%</td>
<td align="right">28,720</td>
<td align="right">5.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">315,254</td>
<td align="right">54.9%</td>
<td align="right">315,685</td>
<td align="right">54.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,580</td>
<td align="right">10.4%</td>
<td align="right">59,597</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">24.4%</td>
<td align="right">140,400</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
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
<td align="right">542,506</td>
<td align="right">1.6%</td>
<td align="right">582,916</td>
<td align="right">1.6%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">28,624,041</td>
<td align="right">85.1%</td>
<td align="right">30,565,121</td>
<td align="right">85.9%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">24,851,982</td>
<td align="right">73.9%</td>
<td align="right">26,449,502</td>
<td align="right">74.3%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,369,880</td>
<td align="right">24.9%</td>
<td align="right">8,713,440</td>
<td align="right">24.5%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,369,939</td>
<td align="right">24.9%</td>
<td align="right">8,713,499</td>
<td align="right">24.5%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,797,318</td>
<td align="right">26.1%</td>
<td align="right">9,140,878</td>
<td align="right">25.7%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,797,318</td>
<td align="right">26.1%</td>
<td align="right">9,140,878</td>
<td align="right">25.7%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,946</td>
<td align="right">0.1%</td>
<td align="right">17,905</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.3%</td>
<td align="right">427,379</td>
<td align="right">1.2%</td>
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
<td align="right">1.4%</td>
<td align="right">456,471</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.3%</td>
<td align="right">441,509</td>
<td align="right">1.2%</td>
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
<td align="left">Inline values</td>
<td align="right">1,784,390</td>
<td align="right"></td>
<td align="right">1,946,080</td>
<td align="right"></td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">12,293,894</td>
<td align="right"></td>
<td align="right">13,366,461</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">78,624,706</td>
<td align="right">15.4%</td>
<td align="right">84,445,705</td>
<td align="right">15.6%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">59,408,386</td>
<td align="right">14.0%</td>
<td align="right">63,750,998</td>
<td align="right">14.1%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">71,044,394</td>
<td align="right">16.7%</td>
<td align="right">75,951,558</td>
<td align="right">16.8%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">21,221,797</td>
<td align="right">52.6%</td>
<td align="right">22,601,042</td>
<td align="right">52.9%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,223,677</td>
<td align="right"></td>
<td align="right">22,602,867</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">193,968,332</td>
<td align="right">37.9%</td>
<td align="right">206,449,610</td>
<td align="right">38.1%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">12,269,967</td>
<td align="right"></td>
<td align="right">13,038,450</td>
<td align="right"></td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">146,669,379</td>
<td align="right">34.5%</td>
<td align="right">155,649,857</td>
<td align="right">34.4%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">148,435,345</td>
<td align="right">34.9%</td>
<td align="right">157,494,865</td>
<td align="right">34.8%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">137,416,933</td>
<td align="right">26.8%</td>
<td align="right">145,081,356</td>
<td align="right">26.8%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">20,619,090</td>
<td align="right"></td>
<td align="right">21,749,697</td>
<td align="right"></td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">18,990,520</td>
<td align="right">47.1%</td>
<td align="right">19,979,660</td>
<td align="right">46.8%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">19,111,792</td>
<td align="right">47.4%</td>
<td align="right">20,100,911</td>
<td align="right">47.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,964</td>
<td align="right"></td>
<td align="right">10,444</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">101,887,697</td>
<td align="right">19.9%</td>
<td align="right">105,326,953</td>
<td align="right">19.5%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">43,632</td>
<td align="right"></td>
<td align="right">42,365</td>
<td align="right"></td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">32,904</td>
<td align="right"></td>
<td align="right">32,139</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,674</td>
<td align="right">0.2%</td>
<td align="right">77,643</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,598</td>
<td align="right">0.1%</td>
<td align="right">43,608</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">11,144</td>
<td align="right">774</td>
<td align="right">794</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">11,144</td>
<td align="right">774</td>
<td align="right">794</td>
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
<td align="right">70</td>
<td align="right">3.3%</td>
<td align="right">82</td>
<td align="right">3.7%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">452,562,065</td>
<td align="right">2,162.1%</td>
<td align="right">485,529,544</td>
<td align="right">2,247.8%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">15</td>
<td align="right">0.7%</td>
<td align="right">14</td>
<td align="right">0.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,707</td>
<td align="right">79.7%</td>
<td align="right">1,776</td>
<td align="right">80.0%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">247</td>
<td align="right">11.5%</td>
<td align="right">256</td>
<td align="right">11.5%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,143</td>
<td align="right"></td>
<td align="right">2,219</td>
<td align="right"></td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">20,931,585</td>
<td align="right"></td>
<td align="right">21,599,871</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,826</td>
<td align="right">85.2%</td>
<td align="right">1,881</td>
<td align="right">84.8%</td>
<td align="right">3.0%</td>
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
<td align="right">247</td>
<td align="right"></td>
<td align="right">256</td>
<td align="right"></td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">247</td>
<td align="right">100.0%</td>
<td align="right">256</td>
<td align="right">100.0%</td>
<td align="right">3.6%</td>
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
<td align="right">67</td>
<td align="right">27.1%</td>
<td align="right">73</td>
<td align="right">28.5%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">15</td>
<td align="right">6.1%</td>
<td align="right">17</td>
<td align="right">6.6%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24</td>
<td align="right">9.7%</td>
<td align="right">21</td>
<td align="right">8.2%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">44</td>
<td align="right">17.8%</td>
<td align="right">45</td>
<td align="right">17.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">48</td>
<td align="right">19.4%</td>
<td align="right">48</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">27</td>
<td align="right">10.9%</td>
<td align="right">29</td>
<td align="right">11.3%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">22</td>
<td align="right">8.9%</td>
<td align="right">23</td>
<td align="right">9.0%</td>
<td align="right">4.5%</td>
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
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">80</td>
<td align="right">32.4%</td>
<td align="right">88</td>
<td align="right">34.4%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">67</td>
<td align="right">27.1%</td>
<td align="right">65</td>
<td align="right">25.4%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">23</td>
<td align="right">9.3%</td>
<td align="right">27</td>
<td align="right">10.5%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">52</td>
<td align="right">21.1%</td>
<td align="right">36</td>
<td align="right">14.1%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">23</td>
<td align="right">9.3%</td>
<td align="right">38</td>
<td align="right">14.8%</td>
<td align="right">65.2%</td>
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
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">33,211</td>
<td align="right">48,897</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">100,458</td>
<td align="right">147,529</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">137,783</td>
<td align="right">160,576</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">108,182</td>
<td align="right">125,916</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">56</td>
<td align="right">65</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">470,558</td>
<td align="right">535,189</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">623,908</td>
<td align="right">708,852</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">320,431</td>
<td align="right">363,154</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,296,028</td>
<td align="right">1,461,665</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">159,737</td>
<td align="right">179,926</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">159,737</td>
<td align="right">179,926</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,308,125</td>
<td align="right">8,140,030</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">860,371</td>
<td align="right">963,104</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">673,325</td>
<td align="right">753,404</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">342,298</td>
<td align="right">382,422</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">342,298</td>
<td align="right">382,422</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">524,859</td>
<td align="right">584,918</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">524,868</td>
<td align="right">584,926</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">524,868</td>
<td align="right">584,926</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,570,157</td>
<td align="right">1,749,686</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,598,196</td>
<td align="right">2,892,011</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">4,065,271</td>
<td align="right">4,511,317</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,065,271</td>
<td align="right">4,511,317</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,807,381</td>
<td align="right">3,112,945</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,815,881</td>
<td align="right">3,120,632</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,834,899</td>
<td align="right">2,032,884</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,002,128</td>
<td align="right">2,218,047</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,594,713</td>
<td align="right">3,976,128</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,752,322</td>
<td align="right">1,938,007</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,640,121</td>
<td align="right">2,919,741</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,096,452</td>
<td align="right">2,308,032</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,054,856</td>
<td align="right">2,260,815</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">584,718</td>
<td align="right">641,870</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">4,321,873</td>
<td align="right">4,743,666</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">6,527,918</td>
<td align="right">7,141,807</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,962,729</td>
<td align="right">2,144,949</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,003,059</td>
<td align="right">6,556,889</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">5,418,341</td>
<td align="right">5,915,019</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,472,716</td>
<td align="right">1,604,745</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">5,461,236</td>
<td align="right">5,947,823</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,648,758</td>
<td align="right">8,313,165</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,998,712</td>
<td align="right">10,854,909</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,287,812</td>
<td align="right">3,569,029</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,222,188</td>
<td align="right">1,326,195</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">10,601,369</td>
<td align="right">11,450,872</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">843,958</td>
<td align="right">909,728</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,412,961</td>
<td align="right">3,678,302</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,881,317</td>
<td align="right">4,180,117</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,368,431</td>
<td align="right">2,550,104</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">13,913,618</td>
<td align="right">14,954,028</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,085,133</td>
<td align="right">1,165,211</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,455,917</td>
<td align="right">2,631,374</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,132,126</td>
<td align="right">1,210,152</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,096,468</td>
<td align="right">1,171,353</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,693,683</td>
<td align="right">1,806,423</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,599,015</td>
<td align="right">1,704,144</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,393,546</td>
<td align="right">1,482,109</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,279,214</td>
<td align="right">2,423,761</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">653,739</td>
<td align="right">694,260</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">653,739</td>
<td align="right">694,260</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,476,524</td>
<td align="right">1,560,218</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">37,998,413</td>
<td align="right">40,134,561</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">48,741,123</td>
<td align="right">51,458,372</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">11,094,628</td>
<td align="right">11,708,517</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">152,505</td>
<td align="right">160,666</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,101,902</td>
<td align="right">3,259,181</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,014,561</td>
<td align="right">9,447,547</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,014,561</td>
<td align="right">9,447,547</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,308,766</td>
<td align="right">1,370,793</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">10,771,238</td>
<td align="right">11,269,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,122,321</td>
<td align="right">3,266,243</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,675,505</td>
<td align="right">1,750,859</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">545,556</td>
<td align="right">568,344</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">15,765,878</td>
<td align="right">16,422,248</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">549,534</td>
<td align="right">572,328</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">549,675</td>
<td align="right">572,463</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,236,498</td>
<td align="right">7,534,986</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,236,498</td>
<td align="right">7,534,986</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,839,960</td>
<td align="right">16,448,178</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,148,147</td>
<td align="right">1,189,985</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">571,585</td>
<td align="right">591,769</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">571,585</td>
<td align="right">591,769</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">511,557</td>
<td align="right">529,304</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">511,557</td>
<td align="right">529,304</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">511,557</td>
<td align="right">529,304</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,399,472</td>
<td align="right">2,476,359</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,399,472</td>
<td align="right">2,476,359</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">20,931,585</td>
<td align="right">21,599,871</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">21,530,747</td>
<td align="right">22,218,096</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">598,472</td>
<td align="right">617,522</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">599,162</td>
<td align="right">618,225</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">602,398</td>
<td align="right">621,461</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,303,732</td>
<td align="right">19,898,785</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,742,767</td>
<td align="right">2,823,392</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,516,680</td>
<td align="right">5,641,759</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,052,248</td>
<td align="right">5,152,121</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,051,472</td>
<td align="right">5,140,026</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,360,841</td>
<td align="right">1,383,634</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,091,569</td>
<td align="right">5,151,628</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,568,305</td>
<td align="right">2,591,098</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,375</td>
<td align="right">403,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,375</td>
<td align="right">403,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,375</td>
<td align="right">403,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">824,638</td>
<td align="right">824,636</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,566,710</td>
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
<td align="left">_GUARD_BOTH_INT</td>
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
<tr>
<td align="left">_POP_UNDER</td>
<td align="right"></td>
<td align="right">2,748,777</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_INT</td>
<td align="right"></td>
<td align="right">2,411,663</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_IMMORTAL</td>
<td align="right"></td>
<td align="right">1,872,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">1,262,683</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right"></td>
<td align="right">374,531</td>
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
<td align="right">214</td>
<td align="right">214</td>
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
Stats gathered on: 2025-01-16
