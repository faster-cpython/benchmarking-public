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
<td align="left">RESUME</td>
<td align="right">320</td>
<td align="right">6,720</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">169</td>
<td align="right">3,549</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">156</td>
<td align="right">3,276</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">150</td>
<td align="right">3,150</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">38</td>
<td align="right">798</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14</td>
<td align="right">294</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,552</td>
<td align="right">30,912</td>
<td align="right">1,891.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,942</td>
<td align="right">36,162</td>
<td align="right">1,762.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">42</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">253</td>
<td align="right">105</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,410</td>
<td align="right">1,134</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">10,283</td>
<td align="right">5,019</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">74,909</td>
<td align="right">36,729</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,698</td>
<td align="right">2,310</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">132,179</td>
<td align="right">64,995</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">142,661</td>
<td align="right">70,287</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">343,227</td>
<td align="right">169,155</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">136,760</td>
<td align="right">67,452</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">24,762</td>
<td align="right">12,222</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">137,588</td>
<td align="right">67,914</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">250,163</td>
<td align="right">123,543</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">19,937</td>
<td align="right">9,849</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">19,937</td>
<td align="right">9,849</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,191</td>
<td align="right">9,975</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,494,203</td>
<td align="right">1,232,217</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">645,614</td>
<td align="right">319,158</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">59,812</td>
<td align="right">29,568</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">100,958</td>
<td align="right">49,938</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">801,838</td>
<td align="right">396,942</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">347,709</td>
<td align="right">172,137</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">505,945</td>
<td align="right">250,509</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,738,440</td>
<td align="right">1,355,907</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">111,755</td>
<td align="right">55,335</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,637,346</td>
<td align="right">1,306,032</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">474,707</td>
<td align="right">235,095</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,158,774</td>
<td align="right">1,069,278</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">230,624</td>
<td align="right">114,240</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">205,225</td>
<td align="right">101,661</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">438,265</td>
<td align="right">217,161</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,558,462</td>
<td align="right">9,196,173</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,655,547</td>
<td align="right">7,758,387</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">7,714,192</td>
<td align="right">3,823,260</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">143,380</td>
<td align="right">71,064</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">73,214</td>
<td align="right">36,288</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,330,327</td>
<td align="right">1,650,789</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">27,620,535</td>
<td align="right">13,691,181</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">58,419</td>
<td align="right">28,959</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,237,596</td>
<td align="right">613,536</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,125,067</td>
<td align="right">2,045,022</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,279,633</td>
<td align="right">634,389</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">15,942,903</td>
<td align="right">7,904,337</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,175,430</td>
<td align="right">582,876</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">35,670,881</td>
<td align="right">17,688,699</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">358,899</td>
<td align="right">177,975</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">965,277</td>
<td align="right">478,674</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,044,525</td>
<td align="right">517,986</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">878,135</td>
<td align="right">435,477</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">35,521,477</td>
<td align="right">17,615,829</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,131,366</td>
<td align="right">4,528,482</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,903,415</td>
<td align="right">1,439,928</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,337,576</td>
<td align="right">3,639,090</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,120,377</td>
<td align="right">1,547,637</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">29,382,979</td>
<td align="right">14,573,307</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">57,011,668</td>
<td align="right">28,276,878</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,109,864</td>
<td align="right">5,014,422</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,718,284</td>
<td align="right">2,836,260</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,377,184</td>
<td align="right">683,088</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">3,819,264</td>
<td align="right">1,894,452</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,309,745</td>
<td align="right">1,145,697</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,444,243</td>
<td align="right">716,415</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">7,960,741</td>
<td align="right">3,949,029</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,402,961</td>
<td align="right">2,680,209</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,255,895</td>
<td align="right">2,607,255</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,773,549</td>
<td align="right">2,367,981</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,195,447</td>
<td align="right">1,585,143</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,001,645</td>
<td align="right">1,489,005</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,679,827</td>
<td align="right">1,329,363</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,665,476</td>
<td align="right">1,322,244</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">2,552,319</td>
<td align="right">1,266,111</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,850,263</td>
<td align="right">917,847</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,516,253</td>
<td align="right">752,157</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,221,994</td>
<td align="right">606,186</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">817,626</td>
<td align="right">405,594</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">817,626</td>
<td align="right">405,594</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">816,991</td>
<td align="right">405,279</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">763,905</td>
<td align="right">378,945</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">252,349</td>
<td align="right">125,181</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">231,267</td>
<td align="right">114,723</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">146,558</td>
<td align="right">72,702</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">105,283</td>
<td align="right">52,227</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">60,706</td>
<td align="right">30,114</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">60,706</td>
<td align="right">30,114</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">60,706</td>
<td align="right">30,114</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">48,133</td>
<td align="right">23,877</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">44,831</td>
<td align="right">22,239</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,224</td>
<td align="right">7,056</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,651</td>
<td align="right">819</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,524</td>
<td align="right">756</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">762</td>
<td align="right">378</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">127</td>
<td align="right">63</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">37,384,801</td>
<td align="right">18,545,247</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">20,480,212</td>
<td align="right">10,159,506</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,119,169</td>
<td align="right">5,515,839</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,534,631</td>
<td align="right">10,682,595</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,663,622</td>
<td align="right">4,793,796</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,544,623</td>
<td align="right">4,734,765</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,794,184</td>
<td align="right">3,370,374</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">105,541,915</td>
<td align="right">52,355,961</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,821,036</td>
<td align="right">5,864,040</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,863,583</td>
<td align="right">5,389,083</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,730,397</td>
<td align="right">13,756,239</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,351,595</td>
<td align="right">1,662,633</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,798,029</td>
<td align="right">14,285,985</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,201,737</td>
<td align="right">1,092,231</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,008,697</td>
<td align="right">996,471</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,391,148</td>
<td align="right">5,154,828</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,845,756</td>
<td align="right">915,642</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,660,016</td>
<td align="right">1,815,660</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,300,164</td>
<td align="right">644,994</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,287,972</td>
<td align="right">638,946</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,300,982</td>
<td align="right">6,598,494</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,015,176</td>
<td align="right">503,622</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">14,522,159</td>
<td align="right">7,204,449</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,525,146</td>
<td align="right">756,630</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">692,215</td>
<td align="right">343,413</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,391,988</td>
<td align="right">2,178,918</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">30,136</td>
<td align="right">14,952</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">252,033</td>
<td align="right">125,055</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">79,313</td>
<td align="right">39,375</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,800</td>
<td align="right">76,356</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,171,762</td>
<td align="right">1,574,769</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,215,826</td>
<td align="right">7,555,926</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,538,789</td>
<td align="right">2,254,476</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">45,023</td>
<td align="right">22,365</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">25,338</td>
<td align="right">12,600</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">309,735</td>
<td align="right">154,938</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">800,840</td>
<td align="right">402,150</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,913,071</td>
<td align="right">966,525</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">209,553</td>
<td align="right">106,176</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">191</td>
<td align="right">105</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">61,591</td>
<td align="right">33,915</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">499,739</td>
<td align="right">299,313</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,959</td>
<td align="right">7,686</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">123</td>
<td align="right"></td>
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
<td align="right">5,099</td>
<td align="right">0.1%</td>
<td align="right">2,499</td>
<td align="right">0.1%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,685,598</td>
<td align="right">98.2%</td>
<td align="right">1,826,874</td>
<td align="right">98.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,025</td>
<td align="right">1.6%</td>
<td align="right">31,584</td>
<td align="right">1.7%</td>
<td align="right">-48.2%</td>
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
<td align="right">167</td>
<td align="right">25.7%</td>
<td align="right">1,323</td>
<td align="right">55.8%</td>
<td align="right">692.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">484</td>
<td align="right">74.3%</td>
<td align="right">1,050</td>
<td align="right">44.2%</td>
<td align="right">116.9%</td>
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
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">2.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">48</td>
<td align="right">9.9%</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">206.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">49</td>
<td align="right">10.1%</td>
<td align="right">147</td>
<td align="right">14.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">72</td>
<td align="right">14.9%</td>
<td align="right">189</td>
<td align="right">18.0%</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">292</td>
<td align="right">60.3%</td>
<td align="right">525</td>
<td align="right">50.0%</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">22</td>
<td align="right">4.5%</td>
<td align="right">21</td>
<td align="right">2.0%</td>
<td align="right">-4.5%</td>
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
<td align="right">48,133</td>
<td align="right">100.0%</td>
<td align="right">23,877</td>
<td align="right">100.0%</td>
<td align="right">-50.4%</td>
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
<td align="right">540,530</td>
<td align="right">0.8%</td>
<td align="right">265,104</td>
<td align="right">0.8%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">67,629,464</td>
<td align="right">99.2%</td>
<td align="right">33,537,903</td>
<td align="right">99.1%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">531,218</td>
<td align="right">0.8%</td>
<td align="right">278,292</td>
<td align="right">0.8%</td>
<td align="right">-47.6%</td>
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
<td align="right">11,254</td>
<td align="right">100.0%</td>
<td align="right">22,974</td>
<td align="right">100.0%</td>
<td align="right">104.1%</td>
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
<td align="right">75</td>
<td align="right">50.0%</td>
<td align="right">1,575</td>
<td align="right">50.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">75</td>
<td align="right">100.0%</td>
<td align="right">1,575</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">853,654</td>
<td align="right">51.6%</td>
<td align="right">422,646</td>
<td align="right">51.2%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">799,378</td>
<td align="right">48.3%</td>
<td align="right">397,362</td>
<td align="right">48.2%</td>
<td align="right">-50.3%</td>
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
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">840</td>
<td align="right">17.5%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,422</td>
<td align="right">97.3%</td>
<td align="right">3,948</td>
<td align="right">82.5%</td>
<td align="right">177.6%</td>
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
<td align="right">80</td>
<td align="right">5.6%</td>
<td align="right">399</td>
<td align="right">10.1%</td>
<td align="right">398.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">50</td>
<td align="right">3.5%</td>
<td align="right">189</td>
<td align="right">4.8%</td>
<td align="right">278.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">49</td>
<td align="right">3.4%</td>
<td align="right">168</td>
<td align="right">4.3%</td>
<td align="right">242.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">494</td>
<td align="right">34.7%</td>
<td align="right">1,302</td>
<td align="right">33.0%</td>
<td align="right">163.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">659</td>
<td align="right">46.3%</td>
<td align="right">1,722</td>
<td align="right">43.6%</td>
<td align="right">161.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">46</td>
<td align="right">3.2%</td>
<td align="right">105</td>
<td align="right">2.7%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">44</td>
<td align="right">3.1%</td>
<td align="right">63</td>
<td align="right">1.6%</td>
<td align="right">43.2%</td>
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
<td align="right">26,914</td>
<td align="right">4.0%</td>
<td align="right">13,146</td>
<td align="right">4.0%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">428,474</td>
<td align="right">64.4%</td>
<td align="right">212,058</td>
<td align="right">64.0%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">209,075</td>
<td align="right">31.4%</td>
<td align="right">104,391</td>
<td align="right">31.5%</td>
<td align="right">-50.1%</td>
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
<td align="right">445</td>
<td align="right">45.2%</td>
<td align="right">1,092</td>
<td align="right">54.2%</td>
<td align="right">145.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">540</td>
<td align="right">54.8%</td>
<td align="right">924</td>
<td align="right">45.8%</td>
<td align="right">71.1%</td>
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
<td align="right">267</td>
<td align="right">60.0%</td>
<td align="right">819</td>
<td align="right">75.0%</td>
<td align="right">206.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">178</td>
<td align="right">40.0%</td>
<td align="right">273</td>
<td align="right">25.0%</td>
<td align="right">53.4%</td>
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
<td align="right">14,950,799</td>
<td align="right">49.6%</td>
<td align="right">7,414,785</td>
<td align="right">49.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,210,815</td>
<td align="right">50.4%</td>
<td align="right">7,547,337</td>
<td align="right">50.4%</td>
<td align="right">-50.4%</td>
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
<td align="right">87</td>
<td align="right">1.7%</td>
<td align="right">1,827</td>
<td align="right">21.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,924</td>
<td align="right">98.3%</td>
<td align="right">6,762</td>
<td align="right">78.7%</td>
<td align="right">37.3%</td>
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
<td align="left">ascii string</td>
<td align="right">50</td>
<td align="right">1.0%</td>
<td align="right">189</td>
<td align="right">2.8%</td>
<td align="right">278.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">144</td>
<td align="right">2.9%</td>
<td align="right">462</td>
<td align="right">6.8%</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">72</td>
<td align="right">1.5%</td>
<td align="right">231</td>
<td align="right">3.4%</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">146</td>
<td align="right">3.0%</td>
<td align="right">462</td>
<td align="right">6.8%</td>
<td align="right">216.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">285</td>
<td align="right">5.8%</td>
<td align="right">777</td>
<td align="right">11.5%</td>
<td align="right">172.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">186</td>
<td align="right">3.8%</td>
<td align="right">462</td>
<td align="right">6.8%</td>
<td align="right">148.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">183</td>
<td align="right">3.7%</td>
<td align="right">378</td>
<td align="right">5.6%</td>
<td align="right">106.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">90</td>
<td align="right">1.8%</td>
<td align="right">168</td>
<td align="right">2.5%</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">3,768</td>
<td align="right">76.5%</td>
<td align="right">3,633</td>
<td align="right">53.7%</td>
<td align="right">-3.6%</td>
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
<td align="right">4,453,255</td>
<td align="right">4,453,255 / 0 !!</td>
<td align="right">2,209,095</td>
<td align="right">2,209,095 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">222,250</td>
<td align="right">222,250 / 0 !!</td>
<td align="right">110,250</td>
<td align="right">110,250 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">33,274</td>
<td align="right">33,274 / 0 !!</td>
<td align="right">16,506</td>
<td align="right">16,506 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">31,496</td>
<td align="right">31,496 / 0 !!</td>
<td align="right">15,624</td>
<td align="right">15,624 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,559</td>
<td align="right">27,559 / 0 !!</td>
<td align="right">13,671</td>
<td align="right">13,671 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">19,558</td>
<td align="right">19,558 / 0 !!</td>
<td align="right">9,702</td>
<td align="right">9,702 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">14,351</td>
<td align="right">14,351 / 0 !!</td>
<td align="right">7,119</td>
<td align="right">7,119 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,286</td>
<td align="right">2,286 / 0 !!</td>
<td align="right">1,134</td>
<td align="right">1,134 / 0 !!</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,859,593</td>
<td align="right">4,859,593 / 0 !!</td>
<td align="right">2,410,695</td>
<td align="right">2,410,695 / 0 !!</td>
<td align="right">-50.4%</td>
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
<td align="right">349,955</td>
<td align="right">0.7%</td>
<td align="right">172,431</td>
<td align="right">0.7%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,084,550</td>
<td align="right">16.3%</td>
<td align="right">4,003,902</td>
<td align="right">16.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,019,255</td>
<td align="right">82.7%</td>
<td align="right">20,331,927</td>
<td align="right">82.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">493,655</td>
<td align="right">1.0%</td>
<td align="right">267,141</td>
<td align="right">1.1%</td>
<td align="right">-45.9%</td>
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
<td align="right">4,821</td>
<td align="right">3.0%</td>
<td align="right">9,429</td>
<td align="right">8.8%</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">153,606</td>
<td align="right">97.0%</td>
<td align="right">97,482</td>
<td align="right">91.2%</td>
<td align="right">-36.5%</td>
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
<td align="left">builtin class method</td>
<td align="right">47</td>
<td align="right">1.0%</td>
<td align="right">105</td>
<td align="right">1.1%</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">755</td>
<td align="right">15.7%</td>
<td align="right">1,512</td>
<td align="right">16.0%</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,906</td>
<td align="right">81.0%</td>
<td align="right">7,623</td>
<td align="right">80.8%</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">91</td>
<td align="right">1.9%</td>
<td align="right">168</td>
<td align="right">1.8%</td>
<td align="right">84.6%</td>
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
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right">15,456</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">84,631,991</td>
<td align="right">100.0%</td>
<td align="right">41,963,607</td>
<td align="right">99.9%</td>
<td align="right">-50.4%</td>
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
<td align="right">820</td>
<td align="right">100.0%</td>
<td align="right">15,540</td>
<td align="right">100.0%</td>
<td align="right">1,795.1%</td>
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
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">147</td>
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
<td align="right">3,819,264</td>
<td align="right">100.0%</td>
<td align="right">1,894,452</td>
<td align="right">100.0%</td>
<td align="right">-50.4%</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">147</td>
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
<td align="right">78</td>
<td align="right">0.0%</td>
<td align="right">1,638</td>
<td align="right">0.1%</td>
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
<td align="right">1,921,964</td>
<td align="right">55.5%</td>
<td align="right">944,853</td>
<td align="right">55.0%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,540,542</td>
<td align="right">44.5%</td>
<td align="right">770,931</td>
<td align="right">44.8%</td>
<td align="right">-50.0%</td>
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
<td align="right">29,344</td>
<td align="right">100.0%</td>
<td align="right">15,918</td>
<td align="right">100.0%</td>
<td align="right">-45.8%</td>
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
<td align="right">19</td>
<td align="right">0.0%</td>
<td align="right">399</td>
<td align="right">0.1%</td>
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
<td align="right">1,237,596</td>
<td align="right">100.0%</td>
<td align="right">613,536</td>
<td align="right">99.9%</td>
<td align="right">-50.4%</td>
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
<td align="right">100.0%</td>
<td align="right">399</td>
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
<td align="right">2,553,378</td>
<td align="right">5.9%</td>
<td align="right">1,258,614</td>
<td align="right">5.9%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,599,499</td>
<td align="right">89.6%</td>
<td align="right">19,143,180</td>
<td align="right">89.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,911,707</td>
<td align="right">4.4%</td>
<td align="right">956,949</td>
<td align="right">4.5%</td>
<td align="right">-49.9%</td>
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
<td align="right">928</td>
<td align="right">1.9%</td>
<td align="right">1,281</td>
<td align="right">3.9%</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">48,439</td>
<td align="right">98.1%</td>
<td align="right">31,647</td>
<td align="right">96.1%</td>
<td align="right">-34.7%</td>
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
<td align="right">26</td>
<td align="right">2.8%</td>
<td align="right">105</td>
<td align="right">8.2%</td>
<td align="right">303.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24</td>
<td align="right">2.6%</td>
<td align="right">63</td>
<td align="right">4.9%</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">272</td>
<td align="right">29.3%</td>
<td align="right">525</td>
<td align="right">41.0%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">264</td>
<td align="right">28.4%</td>
<td align="right">336</td>
<td align="right">26.2%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">342</td>
<td align="right">36.9%</td>
<td align="right">252</td>
<td align="right">19.7%</td>
<td align="right">-26.3%</td>
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
<td align="right">12,419,609</td>
<td align="right">99.9%</td>
<td align="right">6,160,119</td>
<td align="right">99.9%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,851</td>
<td align="right">0.1%</td>
<td align="right">6,699</td>
<td align="right">0.1%</td>
<td align="right">-43.5%</td>
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
<td align="right">60</td>
<td align="right">55.6%</td>
<td align="right">840</td>
<td align="right">85.1%</td>
<td align="right">1,300.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48</td>
<td align="right">44.4%</td>
<td align="right">147</td>
<td align="right">14.9%</td>
<td align="right">206.2%</td>
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
<td align="right">48</td>
<td align="right">100.0%</td>
<td align="right">147</td>
<td align="right">100.0%</td>
<td align="right">206.2%</td>
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
<td align="right">12,751,247</td>
<td align="right">1.7%</td>
<td align="right">6,318,710</td>
<td align="right">1.7%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">330,067,895</td>
<td align="right">43.6%</td>
<td align="right">163,661,611</td>
<td align="right">43.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">385,459,296</td>
<td align="right">50.9%</td>
<td align="right">191,228,247</td>
<td align="right">50.9%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">28,428,186</td>
<td align="right">3.8%</td>
<td align="right">14,263,956</td>
<td align="right">3.8%</td>
<td align="right">-49.8%</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right">15,456</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">48,133</td>
<td align="right">0.2%</td>
<td align="right">23,877</td>
<td align="right">0.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,210,815</td>
<td align="right">78.9%</td>
<td align="right">7,547,337</td>
<td align="right">78.4%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">799,378</td>
<td align="right">4.1%</td>
<td align="right">397,362</td>
<td align="right">4.1%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">209,075</td>
<td align="right">1.1%</td>
<td align="right">104,391</td>
<td align="right">1.1%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,911,707</td>
<td align="right">9.9%</td>
<td align="right">956,949</td>
<td align="right">9.9%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">61,025</td>
<td align="right">0.3%</td>
<td align="right">31,584</td>
<td align="right">0.3%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">531,218</td>
<td align="right">2.8%</td>
<td align="right">278,292</td>
<td align="right">2.9%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">493,655</td>
<td align="right">2.6%</td>
<td align="right">267,141</td>
<td align="right">2.8%</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,851</td>
<td align="right">0.1%</td>
<td align="right">6,699</td>
<td align="right">0.1%</td>
<td align="right">-43.5%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">294,242</td>
<td align="right">2.3%</td>
<td align="right">142,170</td>
<td align="right">2.2%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">511,053</td>
<td align="right">4.0%</td>
<td align="right">249,375</td>
<td align="right">3.9%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">239,655</td>
<td align="right">1.9%</td>
<td align="right">118,356</td>
<td align="right">1.9%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,209,232</td>
<td align="right">9.5%</td>
<td align="right">597,513</td>
<td align="right">9.5%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">38,841</td>
<td align="right">0.3%</td>
<td align="right">19,215</td>
<td align="right">0.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,788,251</td>
<td align="right">14.0%</td>
<td align="right">884,856</td>
<td align="right">14.0%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,845,308</td>
<td align="right">45.8%</td>
<td align="right">2,893,170</td>
<td align="right">45.8%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">209,887</td>
<td align="right">1.6%</td>
<td align="right">104,475</td>
<td align="right">1.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">977,374</td>
<td align="right">7.7%</td>
<td align="right">488,145</td>
<td align="right">7.7%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,540,542</td>
<td align="right">12.1%</td>
<td align="right">770,931</td>
<td align="right">12.2%</td>
<td align="right">-50.0%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">33,684,666</td>
<td align="right">88.1%</td>
<td align="right">16,706,991</td>
<td align="right">88.1%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">60,706</td>
<td align="right">0.2%</td>
<td align="right">30,114</td>
<td align="right">0.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">27,730,397</td>
<td align="right">72.5%</td>
<td align="right">13,756,239</td>
<td align="right">72.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">848,107</td>
<td align="right">2.2%</td>
<td align="right">420,735</td>
<td align="right">2.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">975,505</td>
<td align="right">2.6%</td>
<td align="right">484,281</td>
<td align="right">2.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">66,613</td>
<td align="right">0.2%</td>
<td align="right">33,075</td>
<td align="right">0.2%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,538,854</td>
<td align="right">11.9%</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,538,854</td>
<td align="right">11.9%</td>
<td align="right">2,254,539</td>
<td align="right">11.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,563,349</td>
<td align="right">9.3%</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,563,349</td>
<td align="right">9.3%</td>
<td align="right">1,770,258</td>
<td align="right">9.3%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,541,183</td>
<td align="right">6.6%</td>
<td align="right">1,263,066</td>
<td align="right">6.7%</td>
<td align="right">-50.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">13,009,639</td>
<td align="right">2.7%</td>
<td align="right">6,443,619</td>
<td align="right">2.7%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">7,024,002</td>
<td align="right">1.3%</td>
<td align="right">3,480,078</td>
<td align="right">1.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">185,405,751</td>
<td align="right">38.2%</td>
<td align="right">91,943,607</td>
<td align="right">38.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,239,920</td>
<td align="right">63.5%</td>
<td align="right">22,934,204</td>
<td align="right">63.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">48,983,919</td>
<td align="right"></td>
<td align="right">24,295,417</td>
<td align="right"></td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">59,817</td>
<td align="right">0.1%</td>
<td align="right">29,673</td>
<td align="right">0.1%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">127</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">120,523</td>
<td align="right"></td>
<td align="right">59,787</td>
<td align="right"></td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">233,460,569</td>
<td align="right">42.7%</td>
<td align="right">115,815,357</td>
<td align="right">42.7%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,236,238</td>
<td align="right"></td>
<td align="right">22,937,376</td>
<td align="right"></td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">26,582,976</td>
<td align="right">36.5%</td>
<td align="right">13,192,180</td>
<td align="right">36.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">26,523,032</td>
<td align="right">36.4%</td>
<td align="right">13,162,444</td>
<td align="right">36.4%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">28,764,885</td>
<td align="right"></td>
<td align="right">14,283,191</td>
<td align="right"></td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">117,379,740</td>
<td align="right">24.2%</td>
<td align="right">58,291,580</td>
<td align="right">24.2%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">186,887,309</td>
<td align="right">34.2%</td>
<td align="right">92,813,251</td>
<td align="right">34.2%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">169,284,487</td>
<td align="right">34.9%</td>
<td align="right">84,073,083</td>
<td align="right">34.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">119,130,434</td>
<td align="right">21.8%</td>
<td align="right">59,189,044</td>
<td align="right">21.8%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,921,163</td>
<td align="right"></td>
<td align="right">4,963,248</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">568,587</td>
<td align="right"></td>
<td align="right">299,904</td>
<td align="right"></td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">518,828</td>
<td align="right"></td>
<td align="right">274,572</td>
<td align="right"></td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">50,239</td>
<td align="right"></td>
<td align="right">27,896</td>
<td align="right"></td>
<td align="right">-44.5%</td>
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
<td align="right">128</td>
<td align="right">158,937</td>
<td align="right">1,397,115</td>
<td align="right">99,378</td>
<td align="right">187,095</td>
<td align="right">84</td>
<td align="right">96,117</td>
<td align="right">1,082,210</td>
<td align="right">41,997</td>
<td align="right">135,471</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-26
