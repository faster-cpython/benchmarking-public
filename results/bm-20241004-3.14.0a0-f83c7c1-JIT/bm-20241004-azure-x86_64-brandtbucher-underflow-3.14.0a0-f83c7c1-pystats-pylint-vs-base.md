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
<td align="left">END_FOR</td>
<td align="right">6,291,860</td>
<td align="right">1,348,081</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">453,840</td>
<td align="right">121,032</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,321,023</td>
<td align="right">1,879,709</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,883,640</td>
<td align="right">1,882,351</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,810,100</td>
<td align="right">1,137,651</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,980</td>
<td align="right">3,480</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,010,160</td>
<td align="right">527,879</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">6,865,263</td>
<td align="right">3,675,229</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">10,647,000</td>
<td align="right">6,611,095</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,399,180</td>
<td align="right">2,134,697</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">25,748,612</td>
<td align="right">17,008,872</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,012,557</td>
<td align="right">1,343,113</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">3,079,520</td>
<td align="right">2,104,547</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">659,200</td>
<td align="right">452,023</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,599,500</td>
<td align="right">1,113,499</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,560</td>
<td align="right">9,500</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,920,242</td>
<td align="right">2,104,017</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">39,324,260</td>
<td align="right">28,755,214</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,451,960</td>
<td align="right">1,070,882</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,361,845</td>
<td align="right">2,483,071</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,562,100</td>
<td align="right">12,262,876</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">62,217,760</td>
<td align="right">47,392,604</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">74,622,334</td>
<td align="right">56,849,356</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">37,452,646</td>
<td align="right">28,724,708</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">96,260</td>
<td align="right">73,971</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">609,540</td>
<td align="right">472,180</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,780,052</td>
<td align="right">1,422,248</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">61,159,902</td>
<td align="right">48,960,005</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,846,840</td>
<td align="right">2,287,141</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,033,272</td>
<td align="right">4,068,533</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,444,597</td>
<td align="right">39,573,974</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,542,305</td>
<td align="right">2,137,524</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,849,903</td>
<td align="right">3,255,410</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,577,540</td>
<td align="right">2,187,371</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">395,980</td>
<td align="right">336,736</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">62,571,332</td>
<td align="right">53,411,270</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,862,620</td>
<td align="right">2,463,260</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">54,558,553</td>
<td align="right">46,969,487</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">109,660</td>
<td align="right">94,700</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,383,840</td>
<td align="right">2,928,125</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,016,220</td>
<td align="right">881,619</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,983,525</td>
<td align="right">1,727,861</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,580,455</td>
<td align="right">12,807,733</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">7,140,203</td>
<td align="right">6,285,554</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286,063</td>
<td align="right">9,080,298</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">322,361,500</td>
<td align="right">285,633,597</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">77,558,514</td>
<td align="right">68,958,917</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">738,180</td>
<td align="right">658,668</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,213,920</td>
<td align="right">1,979,227</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">61,888,146</td>
<td align="right">55,463,869</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,370,842</td>
<td align="right">2,126,783</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">29,034,041</td>
<td align="right">26,047,972</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,075,022</td>
<td align="right">5,452,439</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">20,206,021</td>
<td align="right">18,236,618</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,107,693</td>
<td align="right">1,906,422</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,887,521</td>
<td align="right">5,339,205</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,422,362</td>
<td align="right">1,290,095</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">569,500</td>
<td align="right">516,737</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,641,020</td>
<td align="right">2,401,900</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">33,602,213</td>
<td align="right">30,601,038</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,212,560</td>
<td align="right">2,937,191</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,898,691</td>
<td align="right">2,652,285</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,368,223</td>
<td align="right">10,437,029</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,982,190</td>
<td align="right">6,412,427</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,629,918</td>
<td align="right">6,115,705</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">15,932,049</td>
<td align="right">14,725,253</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">80,413,556</td>
<td align="right">74,329,356</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,878,851</td>
<td align="right">8,227,276</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,360,380</td>
<td align="right">9,655,652</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">87,340</td>
<td align="right">81,463</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,539,400</td>
<td align="right">1,436,536</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">27,439,835</td>
<td align="right">25,631,629</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">26,120,315</td>
<td align="right">24,422,834</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,388,672</td>
<td align="right">3,173,739</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,404,842</td>
<td align="right">2,256,622</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,015,549</td>
<td align="right">3,770,526</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">123,480</td>
<td align="right">130,976</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">69,477,914</td>
<td align="right">65,328,560</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,348,383</td>
<td align="right">2,208,855</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">46,598,435</td>
<td align="right">44,022,397</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,717,915</td>
<td align="right">9,199,995</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">17,556,266</td>
<td align="right">16,621,180</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,169,810</td>
<td align="right">4,902,247</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">23,260</td>
<td align="right">22,073</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">49,247</td>
<td align="right">46,748</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,227,380</td>
<td align="right">3,064,516</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">173,200</td>
<td align="right">164,708</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">25,700</td>
<td align="right">26,960</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">69,600</td>
<td align="right">66,230</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,807,300</td>
<td align="right">2,680,541</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,531,240</td>
<td align="right">6,242,861</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">29,514,222</td>
<td align="right">28,212,978</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">96,516,500</td>
<td align="right">92,278,107</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">521,492</td>
<td align="right">498,989</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,802,359</td>
<td align="right">6,519,177</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">43,244,177</td>
<td align="right">41,478,749</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,589,348</td>
<td align="right">3,445,335</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,944,981</td>
<td align="right">4,768,726</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,453,601</td>
<td align="right">4,306,046</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">6,222,740</td>
<td align="right">6,017,685</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,284,380</td>
<td align="right">1,242,117</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">572,460</td>
<td align="right">555,402</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,548,580</td>
<td align="right">31,607,832</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">26,515,445</td>
<td align="right">25,764,276</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">15,529,460</td>
<td align="right">15,090,162</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">138,220</td>
<td align="right">141,658</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,163,503</td>
<td align="right">9,930,429</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">61,100</td>
<td align="right">59,717</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,874,819</td>
<td align="right">1,834,888</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,377,341</td>
<td align="right">1,406,398</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">334,460</td>
<td align="right">340,940</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">459,820</td>
<td align="right">451,161</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,243,503</td>
<td align="right">1,221,331</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,500,200</td>
<td align="right">5,406,962</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,041,658</td>
<td align="right">4,108,407</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">870,660</td>
<td align="right">856,319</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">383,980</td>
<td align="right">378,317</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,193,781</td>
<td align="right">1,178,651</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">125,920</td>
<td align="right">124,359</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">827,680</td>
<td align="right">819,033</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">760,720</td>
<td align="right">753,053</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,301,570</td>
<td align="right">3,279,549</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,450,600</td>
<td align="right">1,443,173</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">105,420</td>
<td align="right">104,920</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,540</td>
<td align="right">108,040</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">343,180</td>
<td align="right">341,620</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,027,619</td>
<td align="right">4,012,830</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">841,920</td>
<td align="right">844,852</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">325,760</td>
<td align="right">326,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">538,780</td>
<td align="right">540,600</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">539,880</td>
<td align="right">541,700</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">408,520</td>
<td align="right">407,240</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,360,340</td>
<td align="right">1,356,275</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">9,300</td>
<td align="right">9,319</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6,004,583</td>
<td align="right">6,016,783</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">6,968,747</td>
<td align="right">6,960,953</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">84,403</td>
<td align="right">84,328</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">924,083</td>
<td align="right">924,718</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,740</td>
<td align="right">11,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,312,647</td>
<td align="right">37,310,012</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,529,700</td>
<td align="right">8,529,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,550,840</td>
<td align="right">3,550,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,876,740</td>
<td align="right">1,876,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,764,560</td>
<td align="right">1,764,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,519,100</td>
<td align="right">1,519,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,361,720</td>
<td align="right">1,361,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,015,700</td>
<td align="right">1,015,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">270,720</td>
<td align="right">270,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">266,280</td>
<td align="right">266,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">240,940</td>
<td align="right">240,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">199,420</td>
<td align="right">199,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">195,520</td>
<td align="right">195,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">154,480</td>
<td align="right">154,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">149,900</td>
<td align="right">149,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,340</td>
<td align="right">91,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">66,580</td>
<td align="right">66,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60,480</td>
<td align="right">60,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">35,980</td>
<td align="right">35,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">25,820</td>
<td align="right">25,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20,600</td>
<td align="right">20,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,580</td>
<td align="right">13,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,720</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,940</td>
<td align="right">5,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">4,720</td>
<td align="right">4,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,580</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,560</td>
<td align="right">4,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,220</td>
<td align="right">4,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,420</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">740</td>
<td align="right">740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
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
<td align="right">858,260</td>
<td align="right">9.2%</td>
<td align="right">843,899</td>
<td align="right">9.1%</td>
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
<td align="right">8,449,880</td>
<td align="right">90.7%</td>
<td align="right">8,449,880</td>
<td align="right">90.8%</td>
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
<td align="right">9,160</td>
<td align="right">73.9%</td>
<td align="right">9,180</td>
<td align="right">73.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,240</td>
<td align="right">26.1%</td>
<td align="right">3,240</td>
<td align="right">26.1%</td>
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
<td align="left">and int</td>
<td align="right">1,440</td>
<td align="right">15.7%</td>
<td align="right">1,460</td>
<td align="right">15.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,420</td>
<td align="right">37.3%</td>
<td align="right">3,420</td>
<td align="right">37.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">880</td>
<td align="right">9.6%</td>
<td align="right">880</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">720</td>
<td align="right">7.9%</td>
<td align="right">720</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">620</td>
<td align="right">6.8%</td>
<td align="right">620</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">580</td>
<td align="right">6.3%</td>
<td align="right">580</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">400</td>
<td align="right">4.4%</td>
<td align="right">400</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">841,920</td>
<td align="right">100.0%</td>
<td align="right">844,852</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">1,404,602</td>
<td align="right">7.1%</td>
<td align="right">1,272,395</td>
<td align="right">6.5%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,186,674</td>
<td align="right">92.5%</td>
<td align="right">18,186,716</td>
<td align="right">93.2%</td>
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
<td align="right">44,840</td>
<td align="right">0.2%</td>
<td align="right">44,840</td>
<td align="right">0.2%</td>
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
<td align="right">8,800</td>
<td align="right">47.5%</td>
<td align="right">8,740</td>
<td align="right">47.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,720</td>
<td align="right">52.5%</td>
<td align="right">9,720</td>
<td align="right">52.7%</td>
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
<td align="left">list slice</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.8%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,920</td>
<td align="right">21.8%</td>
<td align="right">1,880</td>
<td align="right">21.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,700</td>
<td align="right">30.7%</td>
<td align="right">2,680</td>
<td align="right">30.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,640</td>
<td align="right">41.4%</td>
<td align="right">3,620</td>
<td align="right">41.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">260</td>
<td align="right">3.0%</td>
<td align="right">260</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">13,956,160</td>
<td align="right">9.3%</td>
<td align="right">13,022,988</td>
<td align="right">8.7%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">135,862,223</td>
<td align="right">90.5%</td>
<td align="right">136,766,726</td>
<td align="right">91.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,260</td>
<td align="right">0.0%</td>
<td align="right">10,237</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">139,960</td>
<td align="right">0.1%</td>
<td align="right">139,960</td>
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
<td align="right">387,203</td>
<td align="right">100.0%</td>
<td align="right">368,611</td>
<td align="right">100.0%</td>
<td align="right">-4.8%</td>
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
<td align="left">init not simple</td>
<td align="right">480</td>
<td align="right">480 / 0 !!</td>
<td align="right">480</td>
<td align="right">480 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">300</td>
<td align="right">300 / 0 !!</td>
<td align="right">300</td>
<td align="right">300 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">801,280</td>
<td align="right">97.5%</td>
<td align="right">744,821</td>
<td align="right">97.3%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,820</td>
<td align="right">1.3%</td>
<td align="right">10,820</td>
<td align="right">1.4%</td>
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
<td align="right">5,298,823</td>
<td align="right">10.7%</td>
<td align="right">1,858,345</td>
<td align="right">4.0%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,340</td>
<td align="right">0.0%</td>
<td align="right">12,200</td>
<td align="right">0.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,164,924</td>
<td align="right">89.2%</td>
<td align="right">44,164,556</td>
<td align="right">95.9%</td>
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
<td align="right">10,760</td>
<td align="right">48.0%</td>
<td align="right">9,924</td>
<td align="right">45.9%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,680</td>
<td align="right">52.0%</td>
<td align="right">11,680</td>
<td align="right">54.1%</td>
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
<td align="left">float long</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.6%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">860</td>
<td align="right">8.0%</td>
<td align="right">640</td>
<td align="right">6.4%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">840</td>
<td align="right">7.8%</td>
<td align="right">640</td>
<td align="right">6.4%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,340</td>
<td align="right">40.3%</td>
<td align="right">3,878</td>
<td align="right">39.1%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">3,440</td>
<td align="right">32.0%</td>
<td align="right">3,446</td>
<td align="right">34.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">3.2%</td>
<td align="right">340</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">3.2%</td>
<td align="right">340</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">220</td>
<td align="right">2.0%</td>
<td align="right">220</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">160</td>
<td align="right">1.5%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
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
<td align="right">2,520,305</td>
<td align="right">22.2%</td>
<td align="right">2,116,022</td>
<td align="right">20.6%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,480</td>
<td align="right">0.3%</td>
<td align="right">27,725</td>
<td align="right">0.3%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,764,880</td>
<td align="right">77.3%</td>
<td align="right">8,099,155</td>
<td align="right">78.9%</td>
<td align="right">-7.6%</td>
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
<td align="right">17,840</td>
<td align="right">78.9%</td>
<td align="right">17,342</td>
<td align="right">78.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,760</td>
<td align="right">21.1%</td>
<td align="right">4,675</td>
<td align="right">21.2%</td>
<td align="right">-1.8%</td>
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
<td align="right">8,220</td>
<td align="right">46.1%</td>
<td align="right">7,863</td>
<td align="right">45.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,240</td>
<td align="right">12.6%</td>
<td align="right">2,180</td>
<td align="right">12.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,520</td>
<td align="right">19.7%</td>
<td align="right">3,479</td>
<td align="right">20.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3,860</td>
<td align="right">21.6%</td>
<td align="right">3,820</td>
<td align="right">22.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">157,320</td>
<td align="right">0.6%</td>
<td align="right">98,733</td>
<td align="right">0.4%</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,376,022</td>
<td align="right">8.8%</td>
<td align="right">2,227,768</td>
<td align="right">8.4%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">24,576,981</td>
<td align="right">90.6%</td>
<td align="right">24,099,608</td>
<td align="right">91.1%</td>
<td align="right">-1.9%</td>
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
<td align="right">15,960</td>
<td align="right">50.3%</td>
<td align="right">14,882</td>
<td align="right">48.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">15,740</td>
<td align="right">49.7%</td>
<td align="right">15,755</td>
<td align="right">51.4%</td>
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
<td align="left">set</td>
<td align="right">3,380</td>
<td align="right">21.5%</td>
<td align="right">3,516</td>
<td align="right">22.3%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,100</td>
<td align="right">19.7%</td>
<td align="right">3,040</td>
<td align="right">19.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,000</td>
<td align="right">25.4%</td>
<td align="right">3,959</td>
<td align="right">25.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,680</td>
<td align="right">10.7%</td>
<td align="right">1,680</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,020</td>
<td align="right">6.5%</td>
<td align="right">1,020</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">700</td>
<td align="right">4.4%</td>
<td align="right">700</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">620</td>
<td align="right">3.9%</td>
<td align="right">620</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">440</td>
<td align="right">2.8%</td>
<td align="right">440</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">400</td>
<td align="right">2.5%</td>
<td align="right">400</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">0.6%</td>
<td align="right">100</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">422,060</td>
<td align="right">0.2%</td>
<td align="right">309,877</td>
<td align="right">0.1%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,217,699</td>
<td align="right">14.6%</td>
<td align="right">31,855,384</td>
<td align="right">13.0%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">28,639,781</td>
<td align="right">11.3%</td>
<td align="right">25,671,888</td>
<td align="right">10.5%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">188,168,934</td>
<td align="right">74.0%</td>
<td align="right">186,412,450</td>
<td align="right">76.3%</td>
<td align="right">-0.9%</td>
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
<td align="right">1,005,500</td>
<td align="right">92.9%</td>
<td align="right">887,411</td>
<td align="right">92.1%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,880</td>
<td align="right">7.1%</td>
<td align="right">75,669</td>
<td align="right">7.9%</td>
<td align="right">-1.6%</td>
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
<td align="left">method</td>
<td align="right">4,160</td>
<td align="right">5.4%</td>
<td align="right">4,019</td>
<td align="right">5.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,600</td>
<td align="right">25.5%</td>
<td align="right">19,077</td>
<td align="right">25.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,440</td>
<td align="right">5.8%</td>
<td align="right">4,339</td>
<td align="right">5.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,320</td>
<td align="right">1.7%</td>
<td align="right">1,300</td>
<td align="right">1.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">15,180</td>
<td align="right">19.7%</td>
<td align="right">14,979</td>
<td align="right">19.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,640</td>
<td align="right">2.1%</td>
<td align="right">1,620</td>
<td align="right">2.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,840</td>
<td align="right">27.1%</td>
<td align="right">20,638</td>
<td align="right">27.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,020</td>
<td align="right">1.3%</td>
<td align="right">1,018</td>
<td align="right">1.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,120</td>
<td align="right">1.5%</td>
<td align="right">1,119</td>
<td align="right">1.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">900</td>
<td align="right">1.2%</td>
<td align="right">900</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">101,075,568</td>
<td align="right">99.7%</td>
<td align="right">91,320,985</td>
<td align="right">99.7%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,180</td>
<td align="right">0.1%</td>
<td align="right">102,180</td>
<td align="right">0.1%</td>
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
<td align="right">1,500</td>
<td align="right">0.0%</td>
<td align="right">1,500</td>
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
<td align="right">82,140</td>
<td align="right">0.1%</td>
<td align="right">82,140</td>
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
<td align="right">98,040</td>
<td align="right">100.0%</td>
<td align="right">98,040</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,140</td>
<td align="right">0.1%</td>
<td align="right">2,140</td>
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
<td align="right">3,817,120</td>
<td align="right">99.9%</td>
<td align="right">3,817,120</td>
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
<td align="right">2,080</td>
<td align="right">100.0%</td>
<td align="right">2,080</td>
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
<td align="right">8,519,600</td>
<td align="right">55.2%</td>
<td align="right">8,519,600</td>
<td align="right">55.2%</td>
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
<td align="right">6,894,680</td>
<td align="right">44.7%</td>
<td align="right">6,894,680</td>
<td align="right">44.7%</td>
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
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,220</td>
<td align="right">91.3%</td>
<td align="right">9,220</td>
<td align="right">91.3%</td>
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
<td align="right">6,760</td>
<td align="right">73.3%</td>
<td align="right">6,760</td>
<td align="right">73.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,240</td>
<td align="right">24.3%</td>
<td align="right">2,240</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.4%</td>
<td align="right">220</td>
<td align="right">2.4%</td>
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
<td align="right">3,185,520</td>
<td align="right">6.4%</td>
<td align="right">2,910,250</td>
<td align="right">5.9%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,085,720</td>
<td align="right">30.5%</td>
<td align="right">15,085,106</td>
<td align="right">30.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,176,480</td>
<td align="right">63.0%</td>
<td align="right">31,176,949</td>
<td align="right">63.4%</td>
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
<td align="right">13,960</td>
<td align="right">4.5%</td>
<td align="right">13,861</td>
<td align="right">4.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">297,100</td>
<td align="right">95.5%</td>
<td align="right">297,080</td>
<td align="right">95.5%</td>
<td align="right">-0.0%</td>
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
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">540</td>
<td align="right">3.9%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,000</td>
<td align="right">21.5%</td>
<td align="right">2,961</td>
<td align="right">21.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">7,260</td>
<td align="right">52.0%</td>
<td align="right">7,260</td>
<td align="right">52.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,360</td>
<td align="right">9.7%</td>
<td align="right">1,360</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">560</td>
<td align="right">4.0%</td>
<td align="right">560</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">1.1%</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
<td align="right">4,720</td>
<td align="right">100.0%</td>
<td align="right">4,720</td>
<td align="right">100.0%</td>
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
<td align="right">122,440</td>
<td align="right">2.7%</td>
<td align="right">120,899</td>
<td align="right">2.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,356,500</td>
<td align="right">97.2%</td>
<td align="right">4,356,500</td>
<td align="right">97.2%</td>
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
<td align="right">1,440</td>
<td align="right">41.4%</td>
<td align="right">1,420</td>
<td align="right">41.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,040</td>
<td align="right">58.6%</td>
<td align="right">2,040</td>
<td align="right">59.0%</td>
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
<td align="right">120</td>
<td align="right">8.3%</td>
<td align="right">100</td>
<td align="right">7.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">800</td>
<td align="right">55.6%</td>
<td align="right">800</td>
<td align="right">56.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">260</td>
<td align="right">18.1%</td>
<td align="right">260</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">140</td>
<td align="right">9.7%</td>
<td align="right">140</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">8.3%</td>
<td align="right">120</td>
<td align="right">8.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,833,903</td>
<td align="right">2.5%</td>
<td align="right">2,422,465</td>
<td align="right">2.2%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">111,091,003</td>
<td align="right">96.7%</td>
<td align="right">105,783,628</td>
<td align="right">96.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">854,623</td>
<td align="right">0.7%</td>
<td align="right">855,331</td>
<td align="right">0.8%</td>
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
<td align="right">98,640</td>
<td align="right">81.1%</td>
<td align="right">90,841</td>
<td align="right">79.8%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">23,020</td>
<td align="right">18.9%</td>
<td align="right">22,967</td>
<td align="right">20.2%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,740</td>
<td align="right">7.6%</td>
<td align="right">1,795</td>
<td align="right">7.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,400</td>
<td align="right">6.1%</td>
<td align="right">1,412</td>
<td align="right">6.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">16,500</td>
<td align="right">71.7%</td>
<td align="right">16,380</td>
<td align="right">71.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,300</td>
<td align="right">5.6%</td>
<td align="right">1,300</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">900</td>
<td align="right">3.9%</td>
<td align="right">900</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">860</td>
<td align="right">3.7%</td>
<td align="right">860</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">120</td>
<td align="right">0.5%</td>
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
<td align="right">29,707,480</td>
<td align="right">100.0%</td>
<td align="right">29,595,574</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,160</td>
<td align="right">0.0%</td>
<td align="right">7,161</td>
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
<td align="right">4,260</td>
<td align="right">93.0%</td>
<td align="right">4,260</td>
<td align="right">93.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">320</td>
<td align="right">7.0%</td>
<td align="right">320</td>
<td align="right">7.0%</td>
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
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">80</td>
<td align="right">25.0%</td>
<td align="right">80</td>
<td align="right">25.0%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,154,859,326</td>
<td align="right">59.8%</td>
<td align="right">1,000,765,147</td>
<td align="right">59.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">55,711,056</td>
<td align="right">2.9%</td>
<td align="right">48,310,702</td>
<td align="right">2.8%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">650,728,441</td>
<td align="right">33.7%</td>
<td align="right">584,424,714</td>
<td align="right">34.4%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">70,228,659</td>
<td align="right">3.6%</td>
<td align="right">63,401,457</td>
<td align="right">3.7%</td>
<td align="right">-9.7%</td>
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
<td align="right">5,298,823</td>
<td align="right">9.7%</td>
<td align="right">1,858,345</td>
<td align="right">3.9%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,520,305</td>
<td align="right">4.6%</td>
<td align="right">2,116,022</td>
<td align="right">4.5%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,639,781</td>
<td align="right">52.2%</td>
<td align="right">25,671,888</td>
<td align="right">54.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,404,602</td>
<td align="right">2.6%</td>
<td align="right">1,272,395</td>
<td align="right">2.7%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,185,520</td>
<td align="right">5.8%</td>
<td align="right">2,910,250</td>
<td align="right">6.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,376,022</td>
<td align="right">4.3%</td>
<td align="right">2,227,768</td>
<td align="right">4.7%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">858,260</td>
<td align="right">1.6%</td>
<td align="right">843,899</td>
<td align="right">1.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">841,920</td>
<td align="right">1.5%</td>
<td align="right">844,852</td>
<td align="right">1.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">854,623</td>
<td align="right">1.6%</td>
<td align="right">855,331</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,519,600</td>
<td align="right">15.5%</td>
<td align="right">8,519,600</td>
<td align="right">17.9%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">17,831,532</td>
<td align="right">25.4%</td>
<td align="right">14,154,446</td>
<td align="right">22.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,084,823</td>
<td align="right">3.0%</td>
<td align="right">1,721,148</td>
<td align="right">2.7%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">6,032,211</td>
<td align="right">8.6%</td>
<td align="right">5,189,430</td>
<td align="right">8.2%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,008,420</td>
<td align="right">2.9%</td>
<td align="right">1,832,781</td>
<td align="right">2.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,697,642</td>
<td align="right">13.8%</td>
<td align="right">8,910,232</td>
<td align="right">14.1%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,460,001</td>
<td align="right">14.9%</td>
<td align="right">9,716,368</td>
<td align="right">15.3%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">743,480</td>
<td align="right">1.1%</td>
<td align="right">693,672</td>
<td align="right">1.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,144,880</td>
<td align="right">1.6%</td>
<td align="right">1,091,632</td>
<td align="right">1.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,381,268</td>
<td align="right">3.4%</td>
<td align="right">2,396,909</td>
<td align="right">3.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">15,085,660</td>
<td align="right">21.5%</td>
<td align="right">15,085,046</td>
<td align="right">23.8%</td>
<td align="right">-0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">786,467</td>
<td align="right">0.5%</td>
<td align="right">790,455</td>
<td align="right">0.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">2,517,440</td>
<td align="right">1.7%</td>
<td align="right">2,507,401</td>
<td align="right">1.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">8,919,120</td>
<td align="right">6.1%</td>
<td align="right">8,905,337</td>
<td align="right">6.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">38,122,087</td>
<td align="right">26.0%</td>
<td align="right">38,112,292</td>
<td align="right">26.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">38,122,087</td>
<td align="right">26.0%</td>
<td align="right">38,112,292</td>
<td align="right">26.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">29,188,567</td>
<td align="right">19.9%</td>
<td align="right">29,192,555</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">29,202,967</td>
<td align="right">19.9%</td>
<td align="right">29,206,955</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">108,531,987</td>
<td align="right">74.0%</td>
<td align="right">108,534,397</td>
<td align="right">74.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">116,499,214</td>
<td align="right">79.4%</td>
<td align="right">116,499,256</td>
<td align="right">79.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">838,420</td>
<td align="right">0.6%</td>
<td align="right">838,420</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">5,103,180</td>
<td align="right">3.5%</td>
<td align="right">5,103,180</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="right">1,115,433,019</td>
<td align="right">38.6%</td>
<td align="right">1,290,731,558</td>
<td align="right">43.6%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,050,706,514</td>
<td align="right">34.9%</td>
<td align="right">1,212,230,125</td>
<td align="right">39.1%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">847,864,459</td>
<td align="right">29.4%</td>
<td align="right">761,256,971</td>
<td align="right">25.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">341,586,282</td>
<td align="right">11.3%</td>
<td align="right">310,943,796</td>
<td align="right">10.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">356,575,263</td>
<td align="right">12.3%</td>
<td align="right">326,313,564</td>
<td align="right">11.0%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,071,612,545</td>
<td align="right">35.6%</td>
<td align="right">998,751,897</td>
<td align="right">32.2%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">620,919</td>
<td align="right"></td>
<td align="right">662,751</td>
<td align="right"></td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">547,780,696</td>
<td align="right">18.2%</td>
<td align="right">581,874,774</td>
<td align="right">18.7%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">680,834</td>
<td align="right">0.3%</td>
<td align="right">718,499</td>
<td align="right">0.3%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,534,327</td>
<td align="right"></td>
<td align="right">4,691,126</td>
<td align="right"></td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,942,855</td>
<td align="right"></td>
<td align="right">4,057,996</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">568,502,282</td>
<td align="right">19.7%</td>
<td align="right">581,138,484</td>
<td align="right">19.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">61,999,603</td>
<td align="right"></td>
<td align="right">60,974,638</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">127,675,514</td>
<td align="right"></td>
<td align="right">127,572,955</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">152,072,435</td>
<td align="right">68.7%</td>
<td align="right">152,006,972</td>
<td align="right">68.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">140,332,892</td>
<td align="right"></td>
<td align="right">140,299,485</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">153,005,149</td>
<td align="right">69.1%</td>
<td align="right">152,977,351</td>
<td align="right">69.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">68,425,484</td>
<td align="right">30.9%</td>
<td align="right">68,426,677</td>
<td align="right">30.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">68,464,104</td>
<td align="right"></td>
<td align="right">68,465,297</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">251,880</td>
<td align="right">0.1%</td>
<td align="right">251,880</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,348,920</td>
<td align="right"></td>
<td align="right">4,348,920</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">434,920</td>
<td align="right">10.0%</td>
<td align="right">434,920</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">39,180</td>
<td align="right">0.9%</td>
<td align="right">39,180</td>
<td align="right">0.9%</td>
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
<td align="right">5,380</td>
<td align="right">78,540</td>
<td align="right">484,851,964</td>
<td align="right">5,380</td>
<td align="right">78,540</td>
<td align="right">484,746,135</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">66,520</td>
<td align="right">30.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,840</td>
<td align="right">0.9%</td>
<td align="right">2,758</td>
<td align="right">1.1%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">188,829,866</td>
<td align="right"></td>
<td align="right">282,394,231</td>
<td align="right"></td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">159,430</td>
<td align="right">74.0%</td>
<td align="right">221,203</td>
<td align="right">86.2%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">56,041</td>
<td align="right">26.0%</td>
<td align="right">35,514</td>
<td align="right">13.8%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,405,515,028</td>
<td align="right">1,273.9%</td>
<td align="right">3,128,017,988</td>
<td align="right">1,107.7%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,981</td>
<td align="right">0.9%</td>
<td align="right">2,435</td>
<td align="right">0.9%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">215,471</td>
<td align="right"></td>
<td align="right">256,717</td>
<td align="right"></td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">500</td>
<td align="right">0.3%</td>
<td align="right">520</td>
<td align="right">0.2%</td>
<td align="right">4.0%</td>
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
<td align="right">156,390</td>
<td align="right">98.1%</td>
<td align="right">217,185</td>
<td align="right">98.2%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">159,430</td>
<td align="right"></td>
<td align="right">221,203</td>
<td align="right"></td>
<td align="right">38.7%</td>
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
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">16,458</td>
<td align="right">10.3%</td>
<td align="right">18,013</td>
<td align="right">8.1%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">29,258</td>
<td align="right">18.4%</td>
<td align="right">47,599</td>
<td align="right">21.5%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">59,573</td>
<td align="right">37.4%</td>
<td align="right">82,181</td>
<td align="right">37.2%</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">45,461</td>
<td align="right">28.5%</td>
<td align="right">60,404</td>
<td align="right">27.3%</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,020</td>
<td align="right">5.0%</td>
<td align="right">12,144</td>
<td align="right">5.5%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">640</td>
<td align="right">0.4%</td>
<td align="right">842</td>
<td align="right">0.4%</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">10,900</td>
<td align="right">6.8%</td>
<td align="right">6,723</td>
<td align="right">3.0%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">28,516</td>
<td align="right">17.9%</td>
<td align="right">47,788</td>
<td align="right">21.6%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,400</td>
<td align="right">12.2%</td>
<td align="right">32,584</td>
<td align="right">14.7%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">70,526</td>
<td align="right">44.2%</td>
<td align="right">93,574</td>
<td align="right">42.3%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">25,168</td>
<td align="right">15.8%</td>
<td align="right">33,847</td>
<td align="right">15.3%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,740</td>
<td align="right">1.1%</td>
<td align="right">2,529</td>
<td align="right">1.1%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">360</td>
<td align="right">210,280</td>
<td align="right">58,311.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">720</td>
<td align="right">411,241</td>
<td align="right">57,016.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">360</td>
<td align="right">200,961</td>
<td align="right">55,722.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2,400</td>
<td align="right">209,577</td>
<td align="right">8,632.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">372,280</td>
<td align="right">28,714,346</td>
<td align="right">7,613.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">55,340</td>
<td align="right">3,056,629</td>
<td align="right">5,423.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">56,040</td>
<td align="right">3,057,329</td>
<td align="right">5,355.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">10,180</td>
<td align="right">492,461</td>
<td align="right">4,737.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">360</td>
<td align="right">17,400</td>
<td align="right">4,733.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">13,360</td>
<td align="right">495,386</td>
<td align="right">3,608.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">61,000</td>
<td align="right">1,733,449</td>
<td align="right">2,741.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">6,440</td>
<td align="right">175,282</td>
<td align="right">2,621.8%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">45,680</td>
<td align="right">1,020,653</td>
<td align="right">2,134.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">27,960</td>
<td align="right">513,961</td>
<td align="right">1,738.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">267,820</td>
<td align="right">3,708,827</td>
<td align="right">1,284.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">114,660</td>
<td align="right">819,388</td>
<td align="right">614.6%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">1,380</td>
<td align="right">5,445</td>
<td align="right">294.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">151,860</td>
<td align="right">591,158</td>
<td align="right">289.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">140,140</td>
<td align="right">539,500</td>
<td align="right">285.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">577,600</td>
<td align="right">1,842,083</td>
<td align="right">218.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,980</td>
<td align="right">8,857</td>
<td align="right">197.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,053,768</td>
<td align="right">67,165,325</td>
<td align="right">168.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,926,277</td>
<td align="right">5,116,311</td>
<td align="right">165.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">107,980</td>
<td align="right">270,567</td>
<td align="right">150.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,161,687</td>
<td align="right">5,162,842</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,161,687</td>
<td align="right">5,162,842</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">80</td>
<td align="right">191</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">494,567</td>
<td align="right">1,164,023</td>
<td align="right">135.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">349,500</td>
<td align="right">805,215</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">349,500</td>
<td align="right">805,215</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">577,175</td>
<td align="right">1,328,904</td>
<td align="right">130.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">2,480</td>
<td align="right">5,496</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">204,760</td>
<td align="right">443,880</td>
<td align="right">116.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">45,920</td>
<td align="right">98,683</td>
<td align="right">114.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">269,940</td>
<td align="right">563,661</td>
<td align="right">108.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">218,700</td>
<td align="right">453,393</td>
<td align="right">107.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">26,945,886</td>
<td align="right">54,450,641</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,803,599</td>
<td align="right">11,372,786</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,901,652</td>
<td align="right">35,013,614</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">206,347</td>
<td align="right">398,754</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">429,940</td>
<td align="right">817,709</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">269,940</td>
<td align="right">481,602</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">213,960</td>
<td align="right">377,324</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">363,120</td>
<td align="right">638,515</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">124,120</td>
<td align="right">217,358</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2,399,066</td>
<td align="right">4,174,986</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,759,394</td>
<td align="right">3,061,689</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,549,762</td>
<td align="right">13,001,027</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">22,054,632</td>
<td align="right">6,192,461</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">17,358,023</td>
<td align="right">29,549,510</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">552,088</td>
<td align="right">925,660</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">396,740</td>
<td align="right">656,296</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">5,019,870</td>
<td align="right">8,233,008</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">13,084,050</td>
<td align="right">20,865,449</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,972,565</td>
<td align="right">4,740,360</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">12,124,355</td>
<td align="right">19,275,996</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">13,660,330</td>
<td align="right">21,646,176</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">10,516,540</td>
<td align="right">16,567,411</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">9,118,368</td>
<td align="right">14,210,305</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">32,438,076</td>
<td align="right">50,502,745</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">16,263,418</td>
<td align="right">25,306,029</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">2,320</td>
<td align="right">3,540</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">5,697,660</td>
<td align="right">8,536,514</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">188,829,866</td>
<td align="right">282,394,231</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,609,199</td>
<td align="right">9,877,649</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,186,740</td>
<td align="right">1,738,889</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,102,411</td>
<td align="right">7,475,586</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">31,419,904</td>
<td align="right">45,886,010</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,912,459</td>
<td align="right">2,791,245</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,881,660</td>
<td align="right">4,171,683</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">6,012,376</td>
<td align="right">3,362,761</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,739,774</td>
<td align="right">5,385,733</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,320,294</td>
<td align="right">1,869,625</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">535,340</td>
<td align="right">744,334</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">110,500</td>
<td align="right">152,763</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">2,670,569</td>
<td align="right">3,691,438</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">551,380</td>
<td align="right">760,867</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">551,380</td>
<td align="right">760,867</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">3,450,018</td>
<td align="right">4,750,942</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">25,705,328</td>
<td align="right">35,228,107</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">210,884,498</td>
<td align="right">288,586,692</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">784,000</td>
<td align="right">1,072,379</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">670,111</td>
<td align="right">915,134</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">645,217</td>
<td align="right">878,291</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">5,100</td>
<td align="right">3,280</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">5,100</td>
<td align="right">3,280</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,721,417</td>
<td align="right">2,327,377</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">4,500</td>
<td align="right">6,060</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">25,115,131</td>
<td align="right">33,607,351</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,171,114</td>
<td align="right">4,243,083</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">3,843,086</td>
<td align="right">5,137,646</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">193,312,172</td>
<td align="right">257,554,562</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">17,533,758</td>
<td align="right">23,357,125</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,970,413</td>
<td align="right">2,622,000</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,633,997</td>
<td align="right">3,488,646</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">4,563,258</td>
<td align="right">5,976,934</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">161,269,052</td>
<td align="right">210,783,353</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">111,221,179</td>
<td align="right">142,733,972</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">5,202,358</td>
<td align="right">6,623,102</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">65,440</td>
<td align="right">83,000</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,480,366</td>
<td align="right">1,101,503</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,344,569</td>
<td align="right">4,193,354</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">14,627,880</td>
<td align="right">18,315,345</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,082,742</td>
<td align="right">2,597,547</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">44,612,952</td>
<td align="right">55,481,085</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">828,857</td>
<td align="right">1,027,619</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">19,819,199</td>
<td align="right">24,135,838</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">13,910,321</td>
<td align="right">16,915,149</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">606,680</td>
<td align="right">736,660</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">31,669,077</td>
<td align="right">38,255,164</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,700</td>
<td align="right">3,760</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">22,853,684</td>
<td align="right">27,332,573</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">27,173,625</td>
<td align="right">32,202,776</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">147,523,538</td>
<td align="right">173,743,984</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,770,106</td>
<td align="right">12,661,368</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">7,360</td>
<td align="right">6,100</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">38,100</td>
<td align="right">31,620</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">361,904</td>
<td align="right">421,136</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">6,172,772</td>
<td align="right">7,137,523</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">28,419,314</td>
<td align="right">32,645,008</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">12,708,212</td>
<td align="right">14,516,439</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">4,660</td>
<td align="right">5,320</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">6,600,197</td>
<td align="right">7,531,391</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">23,669,133</td>
<td align="right">26,992,241</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,812,700</td>
<td align="right">3,193,778</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">7,042,314</td>
<td align="right">7,977,400</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">8,097,835</td>
<td align="right">9,083,559</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,040</td>
<td align="right">2,287</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">30,500</td>
<td align="right">27,062</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">87,653,503</td>
<td align="right">97,413,563</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">30,096,255</td>
<td align="right">33,363,116</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">6,494,318</td>
<td align="right">7,134,315</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">54,459,302</td>
<td align="right">59,604,074</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">25,434,402</td>
<td align="right">27,772,229</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">243,737</td>
<td align="right">265,909</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,986,596</td>
<td align="right">3,245,703</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,253,120</td>
<td align="right">1,359,361</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,843,538</td>
<td align="right">1,996,833</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">6,948,690</td>
<td align="right">7,518,453</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,650,220</td>
<td align="right">1,784,821</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">8,148,400</td>
<td align="right">8,799,339</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">227,650</td>
<td align="right">209,851</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,544,500</td>
<td align="right">1,653,713</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,465,576</td>
<td align="right">9,046,972</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,617,440</td>
<td align="right">3,856,544</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,180,477</td>
<td align="right">2,320,005</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">88,540</td>
<td align="right">94,203</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">12,024,334</td>
<td align="right">12,772,178</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,972,958</td>
<td align="right">2,806,851</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,700,861</td>
<td align="right">38,692,079</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">937,792</td>
<td align="right">977,756</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,327,279</td>
<td align="right">4,503,534</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,461,378</td>
<td align="right">7,740,806</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,191,280</td>
<td align="right">2,270,792</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,084,899</td>
<td align="right">4,232,814</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">630,208</td>
<td align="right">652,711</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">240,020</td>
<td align="right">248,512</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,212,418</td>
<td align="right">7,454,188</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">28,892,244</td>
<td align="right">29,798,580</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">4,292,218</td>
<td align="right">4,424,425</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">346,540</td>
<td align="right">355,032</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">346,540</td>
<td align="right">355,032</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,017,678</td>
<td align="right">6,164,160</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">93,401,941</td>
<td align="right">95,426,350</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">123,940</td>
<td align="right">126,620</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">122,480</td>
<td align="right">125,000</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">366,500</td>
<td align="right">359,004</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,675,645</td>
<td align="right">29,193,565</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,105,039</td>
<td align="right">4,167,170</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">890,097</td>
<td align="right">877,897</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">123,540</td>
<td align="right">125,081</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">2,310,658</td>
<td align="right">2,282,759</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,361,020</td>
<td align="right">1,375,381</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">48,000</td>
<td align="right">48,500</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">133,860</td>
<td align="right">135,243</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">41,149,904</td>
<td align="right">41,433,594</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">41,181,484</td>
<td align="right">41,459,391</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,351,820</td>
<td align="right">1,360,479</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">8,424,233</td>
<td align="right">8,476,553</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,080</td>
<td align="right">3,061</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">33,197,806</td>
<td align="right">33,392,779</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,039,214</td>
<td align="right">4,061,872</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">27,560,775</td>
<td align="right">27,704,533</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">246,120</td>
<td align="right">245,000</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">929,800</td>
<td align="right">926,868</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">5,255,399</td>
<td align="right">5,268,088</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">21,243,944</td>
<td align="right">21,207,607</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,076,880</td>
<td align="right">1,078,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">527,860</td>
<td align="right">527,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">47,360</td>
<td align="right">47,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">28,880</td>
<td align="right">28,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">10,520</td>
<td align="right">10,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,400</td>
<td align="right">10,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">2,840</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,600</td>
<td align="right">2,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">2,080</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">4,299,224</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">4,035,905</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right"></td>
<td align="right">332,808</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">26,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">17,058</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">4,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">3,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">3,370</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">3,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">1,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">500</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">180</td>
<td align="right">382</td>
<td align="right">112.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,980</td>
<td align="right">2,714</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">720</td>
<td align="right">896</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">10,580</td>
<td align="right">12,127</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right"></td>
<td align="right">431</td>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2024-10-21
