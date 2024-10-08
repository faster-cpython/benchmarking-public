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
<td align="right">59,840</td>
<td align="right">14,024,080</td>
<td align="right">23,336.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">29,420</td>
<td align="right">2,636,080</td>
<td align="right">8,860.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">3,000</td>
<td align="right">81,160</td>
<td align="right">2,605.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">100,600</td>
<td align="right">2,141,960</td>
<td align="right">2,029.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">105,940</td>
<td align="right">2,071,680</td>
<td align="right">1,855.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,060</td>
<td align="right">894,740</td>
<td align="right">1,468.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">84,140</td>
<td align="right">1,284,620</td>
<td align="right">1,426.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">272,740</td>
<td align="right">1,512,920</td>
<td align="right">454.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,158,860</td>
<td align="right">6,395,140</td>
<td align="right">451.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,200</td>
<td align="right">93,020</td>
<td align="right">384.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,987,040</td>
<td align="right">9,493,500</td>
<td align="right">377.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">862,240</td>
<td align="right">3,708,800</td>
<td align="right">330.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,164,960</td>
<td align="right">4,960,520</td>
<td align="right">325.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">920,440</td>
<td align="right">3,764,560</td>
<td align="right">309.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">286,920</td>
<td align="right">1,067,720</td>
<td align="right">272.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">652,780</td>
<td align="right">2,283,020</td>
<td align="right">249.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,059,360</td>
<td align="right">3,666,020</td>
<td align="right">246.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">357,760</td>
<td align="right">1,215,920</td>
<td align="right">239.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,969,760</td>
<td align="right">13,448,820</td>
<td align="right">238.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">155,200</td>
<td align="right">490,760</td>
<td align="right">216.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,115,320</td>
<td align="right">2,990,880</td>
<td align="right">168.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,880</td>
<td align="right">31,840</td>
<td align="right">168.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,168,540</td>
<td align="right">10,925,220</td>
<td align="right">162.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">150,620</td>
<td align="right">391,640</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,815,000</td>
<td align="right">9,809,400</td>
<td align="right">157.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">331,140</td>
<td align="right">815,080</td>
<td align="right">146.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">502,600</td>
<td align="right">1,195,320</td>
<td align="right">137.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,199,280</td>
<td align="right">2,728,420</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,789,100</td>
<td align="right">3,732,980</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,068,000</td>
<td align="right">33,216,800</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,974,620</td>
<td align="right">40,369,700</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,509,880</td>
<td align="right">17,147,080</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">16,557,360</td>
<td align="right">32,683,520</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">32,203,700</td>
<td align="right">63,562,740</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">802,160</td>
<td align="right">1,581,540</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,000,200</td>
<td align="right">141,941,820</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,622,100</td>
<td align="right">39,887,280</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,777,900</td>
<td align="right">18,870,160</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">39,060</td>
<td align="right">73,540</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">91,320</td>
<td align="right">171,420</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,259,720</td>
<td align="right">11,619,560</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,715,020</td>
<td align="right">3,174,700</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,959,140</td>
<td align="right">3,614,360</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,028,960</td>
<td align="right">12,949,860</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,422,020</td>
<td align="right">31,838,180</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">132,700</td>
<td align="right">242,400</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,893,780</td>
<td align="right">10,728,000</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,658,020</td>
<td align="right">12,067,800</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">588,200</td>
<td align="right">1,048,100</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,046,740</td>
<td align="right">41,580,880</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">608,200</td>
<td align="right">1,029,280</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,973,800</td>
<td align="right">21,829,840</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,661,560</td>
<td align="right">4,471,200</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">126,580</td>
<td align="right">211,020</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,976,920</td>
<td align="right">12,839,460</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,001,100</td>
<td align="right">1,605,460</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,978,620</td>
<td align="right">3,074,960</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,965,080</td>
<td align="right">9,231,800</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,865,720</td>
<td align="right">8,952,680</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,900,160</td>
<td align="right">7,221,240</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">156,240</td>
<td align="right">236,020</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,836,640</td>
<td align="right">4,275,140</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">583,020</td>
<td align="right">864,180</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,231,340</td>
<td align="right">6,040,160</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,938,640</td>
<td align="right">2,740,040</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">74,280</td>
<td align="right">99,920</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">74,280</td>
<td align="right">99,920</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,204,780</td>
<td align="right">17,564,160</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">123,720</td>
<td align="right">164,120</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,489,160</td>
<td align="right">1,910,240</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">103,380</td>
<td align="right">132,180</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">19,280</td>
<td align="right">24,440</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">157,020</td>
<td align="right">197,660</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">177,700</td>
<td align="right">221,780</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,963,080</td>
<td align="right">28,230,920</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,047,040</td>
<td align="right">1,276,780</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,068,100</td>
<td align="right">2,518,280</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">83,320</td>
<td align="right">100,560</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">143,260</td>
<td align="right">172,180</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">46,680</td>
<td align="right">55,640</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">32,220</td>
<td align="right">37,880</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">151,000</td>
<td align="right">176,640</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,220</td>
<td align="right">19,900</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,212,780</td>
<td align="right">3,654,580</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,969,860</td>
<td align="right">3,360,280</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,479,280</td>
<td align="right">3,928,780</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">207,100</td>
<td align="right">229,700</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">161,740</td>
<td align="right">178,260</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">817,660</td>
<td align="right">892,540</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">511,400</td>
<td align="right">558,160</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,542,040</td>
<td align="right">1,675,280</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">548,300</td>
<td align="right">576,180</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,179,120</td>
<td align="right">1,233,300</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">398,320</td>
<td align="right">411,520</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">161,200</td>
<td align="right">166,000</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,123,000</td>
<td align="right">3,211,320</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">30,400</td>
<td align="right">31,140</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,262,960</td>
<td align="right">2,313,520</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">192,040</td>
<td align="right">196,280</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">786,600</td>
<td align="right">800,680</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">90,840</td>
<td align="right">92,140</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,651,840</td>
<td align="right">1,669,760</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,975,100</td>
<td align="right">6,013,880</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,176,360</td>
<td align="right">5,195,760</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">40,100</td>
<td align="right">40,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,423,660</td>
<td align="right">10,427,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">417,860</td>
<td align="right">417,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">10,029,280</td>
<td align="right">10,029,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,030,080</td>
<td align="right">1,030,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,030,080</td>
<td align="right">1,030,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">291,360</td>
<td align="right">291,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">279,980</td>
<td align="right">279,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">193,760</td>
<td align="right">193,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">75,260</td>
<td align="right">75,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">73,580</td>
<td align="right">73,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">34,320</td>
<td align="right">34,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">29,360</td>
<td align="right">29,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">16,700</td>
<td align="right">16,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">16,600</td>
<td align="right">16,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,020</td>
<td align="right">11,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">6,320</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,120</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,980</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">2,080</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">16,060</td>
<td align="right">1.8%</td>
<td align="right">18,700</td>
<td align="right">2.1%</td>
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
<td align="right">867,940</td>
<td align="right">98.0%</td>
<td align="right">867,940</td>
<td align="right">97.8%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">680</td>
<td align="right">58.6%</td>
<td align="right">720</td>
<td align="right">60.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">480</td>
<td align="right">41.4%</td>
<td align="right">480</td>
<td align="right">40.0%</td>
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
<td align="left">add other</td>
<td align="right">640</td>
<td align="right">94.1%</td>
<td align="right">680</td>
<td align="right">94.4%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">40</td>
<td align="right">5.9%</td>
<td align="right">40</td>
<td align="right">5.6%</td>
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
<td align="right">19,200</td>
<td align="right">100.0%</td>
<td align="right">93,020</td>
<td align="right">100.0%</td>
<td align="right">384.5%</td>
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
<td align="right">15,700</td>
<td align="right">0.6%</td>
<td align="right">15,700</td>
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
<td align="right">2,451,660</td>
<td align="right">99.1%</td>
<td align="right">2,451,660</td>
<td align="right">99.1%</td>
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
<td align="right">6,340</td>
<td align="right">0.3%</td>
<td align="right">6,340</td>
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
<td align="left">Success</td>
<td align="right">760</td>
<td align="right">69.1%</td>
<td align="right">760</td>
<td align="right">69.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">340</td>
<td align="right">30.9%</td>
<td align="right">340</td>
<td align="right">30.9%</td>
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
<td align="right">240</td>
<td align="right">70.6%</td>
<td align="right">240</td>
<td align="right">70.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">100</td>
<td align="right">29.4%</td>
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
<td align="right">268,500</td>
<td align="right">0.3%</td>
<td align="right">678,640</td>
<td align="right">0.8%</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,248,800</td>
<td align="right">99.7%</td>
<td align="right">86,713,520</td>
<td align="right">99.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,160</td>
<td align="right">0.0%</td>
<td align="right">17,160</td>
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
<td align="right">23,600</td>
<td align="right">100.0%</td>
<td align="right">31,340</td>
<td align="right">100.0%</td>
<td align="right">32.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,500</td>
<td align="right">50.0%</td>
<td align="right">1,500</td>
<td align="right">50.0%</td>
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
<td align="right">812,580</td>
<td align="right">42.9%</td>
<td align="right">887,300</td>
<td align="right">45.1%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,074,720</td>
<td align="right">56.8%</td>
<td align="right">1,074,720</td>
<td align="right">54.6%</td>
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
<td align="right">4,280</td>
<td align="right">84.3%</td>
<td align="right">4,440</td>
<td align="right">84.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">800</td>
<td align="right">15.7%</td>
<td align="right">800</td>
<td align="right">15.3%</td>
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
<td align="left">string</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">180</td>
<td align="right">4.1%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">4.7%</td>
<td align="right">220</td>
<td align="right">5.0%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,860</td>
<td align="right">43.5%</td>
<td align="right">1,920</td>
<td align="right">43.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,500</td>
<td align="right">35.0%</td>
<td align="right">1,500</td>
<td align="right">33.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">9.8%</td>
<td align="right">420</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">120</td>
<td align="right">2.8%</td>
<td align="right">120</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">80</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">1.8%</td>
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
<td align="right">154,320</td>
<td align="right">21.5%</td>
<td align="right">234,080</td>
<td align="right">29.4%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">527,560</td>
<td align="right">73.5%</td>
<td align="right">527,560</td>
<td align="right">66.2%</td>
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
<td align="right">33,720</td>
<td align="right">4.7%</td>
<td align="right">33,720</td>
<td align="right">4.2%</td>
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
<td align="right">51.2%</td>
<td align="right">1,320</td>
<td align="right">51.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">48.8%</td>
<td align="right">1,240</td>
<td align="right">48.4%</td>
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
<td align="right">920</td>
<td align="right">70.8%</td>
<td align="right">940</td>
<td align="right">71.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">380</td>
<td align="right">29.2%</td>
<td align="right">380</td>
<td align="right">28.8%</td>
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
<td align="right">3,962,700</td>
<td align="right">45.9%</td>
<td align="right">13,439,280</td>
<td align="right">51.8%</td>
<td align="right">239.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,662,980</td>
<td align="right">54.0%</td>
<td align="right">12,505,000</td>
<td align="right">48.2%</td>
<td align="right">168.2%</td>
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
<td align="right">5,400</td>
<td align="right">76.5%</td>
<td align="right">7,880</td>
<td align="right">82.6%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,660</td>
<td align="right">23.5%</td>
<td align="right">1,660</td>
<td align="right">17.4%</td>
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
<td align="left">dict items</td>
<td align="right">2,720</td>
<td align="right">50.4%</td>
<td align="right">4,980</td>
<td align="right">63.2%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">320</td>
<td align="right">5.9%</td>
<td align="right">420</td>
<td align="right">5.3%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">3.7%</td>
<td align="right">240</td>
<td align="right">3.0%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">400</td>
<td align="right">5.1%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">740</td>
<td align="right">13.7%</td>
<td align="right">760</td>
<td align="right">9.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">440</td>
<td align="right">8.1%</td>
<td align="right">440</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">340</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">180</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">120</td>
<td align="right">2.2%</td>
<td align="right">120</td>
<td align="right">1.5%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">106,940</td>
<td align="right">0.2%</td>
<td align="right">439,820</td>
<td align="right">0.7%</td>
<td align="right">311.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,519,200</td>
<td align="right">8.0%</td>
<td align="right">10,113,580</td>
<td align="right">16.3%</td>
<td align="right">123.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">478,340</td>
<td align="right">0.9%</td>
<td align="right">525,020</td>
<td align="right">0.8%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,209,400</td>
<td align="right">91.1%</td>
<td align="right">51,328,440</td>
<td align="right">82.8%</td>
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
<td align="right">105,940</td>
<td align="right">90.2%</td>
<td align="right">211,440</td>
<td align="right">94.8%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,560</td>
<td align="right">9.8%</td>
<td align="right">11,640</td>
<td align="right">5.2%</td>
<td align="right">0.7%</td>
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
<td align="right">1,860</td>
<td align="right">16.1%</td>
<td align="right">1,880</td>
<td align="right">16.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">9,360</td>
<td align="right">81.0%</td>
<td align="right">9,420</td>
<td align="right">80.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
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
<td align="right">50,720,240</td>
<td align="right">99.9%</td>
<td align="right">95,434,340</td>
<td align="right">100.0%</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,680</td>
<td align="right">0.0%</td>
<td align="right">14,680</td>
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
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
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
<td align="right">14,760</td>
<td align="right">100.0%</td>
<td align="right">14,760</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
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
<td align="right">4,811,540</td>
<td align="right">100.0%</td>
<td align="right">4,811,540</td>
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
<td align="right">1,232,940</td>
<td align="right">32.8%</td>
<td align="right">1,941,000</td>
<td align="right">44.5%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,523,180</td>
<td align="right">67.1%</td>
<td align="right">2,419,460</td>
<td align="right">55.4%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
<td align="right">1,560</td>
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
<td align="right">24,780</td>
<td align="right">100.0%</td>
<td align="right">38,140</td>
<td align="right">100.0%</td>
<td align="right">53.9%</td>
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
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">380</td>
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
<td align="right">1,558,820</td>
<td align="right">100.0%</td>
<td align="right">1,558,820</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">380</td>
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
<td align="right">96,680</td>
<td align="right">0.2%</td>
<td align="right">2,061,860</td>
<td align="right">3.8%</td>
<td align="right">2,032.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,294,440</td>
<td align="right">2.6%</td>
<td align="right">3,136,460</td>
<td align="right">5.9%</td>
<td align="right">142.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,487,780</td>
<td align="right">97.2%</td>
<td align="right">48,370,880</td>
<td align="right">90.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">31,820</td>
<td align="right">95.7%</td>
<td align="right">66,540</td>
<td align="right">97.1%</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,420</td>
<td align="right">4.3%</td>
<td align="right">1,980</td>
<td align="right">2.9%</td>
<td align="right">39.4%</td>
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
<td align="right">300</td>
<td align="right">21.1%</td>
<td align="right">620</td>
<td align="right">31.3%</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">380</td>
<td align="right">26.8%</td>
<td align="right">620</td>
<td align="right">31.3%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">540</td>
<td align="right">38.0%</td>
<td align="right">540</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120</td>
<td align="right">8.5%</td>
<td align="right">120</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">80</td>
<td align="right">5.6%</td>
<td align="right">80</td>
<td align="right">4.0%</td>
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
<td align="right">15,660</td>
<td align="right">0.1%</td>
<td align="right">15,660</td>
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
<td align="right">15,645,940</td>
<td align="right">99.9%</td>
<td align="right">15,645,940</td>
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
<td align="right">780</td>
<td align="right">83.0%</td>
<td align="right">780</td>
<td align="right">83.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">17.0%</td>
<td align="right">160</td>
<td align="right">17.0%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,701,560</td>
<td align="right">1.2%</td>
<td align="right">17,424,280</td>
<td align="right">2.1%</td>
<td align="right">205.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,359,560</td>
<td align="right">1.6%</td>
<td align="right">15,949,440</td>
<td align="right">1.9%</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">184,014,560</td>
<td align="right">40.1%</td>
<td align="right">344,806,460</td>
<td align="right">41.8%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">262,169,760</td>
<td align="right">57.1%</td>
<td align="right">446,310,780</td>
<td align="right">54.1%</td>
<td align="right">70.2%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">96,680</td>
<td align="right">1.7%</td>
<td align="right">2,061,860</td>
<td align="right">11.9%</td>
<td align="right">2,032.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,200</td>
<td align="right">0.3%</td>
<td align="right">93,020</td>
<td align="right">0.5%</td>
<td align="right">384.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,962,700</td>
<td align="right">70.7%</td>
<td align="right">13,439,280</td>
<td align="right">77.6%</td>
<td align="right">239.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">154,320</td>
<td align="right">2.8%</td>
<td align="right">234,080</td>
<td align="right">1.4%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">16,060</td>
<td align="right">0.3%</td>
<td align="right">18,700</td>
<td align="right">0.1%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">478,340</td>
<td align="right">8.5%</td>
<td align="right">525,020</td>
<td align="right">3.0%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">812,580</td>
<td align="right">14.5%</td>
<td align="right">887,300</td>
<td align="right">5.1%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,160</td>
<td align="right">0.3%</td>
<td align="right">17,160</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">15,700</td>
<td align="right">0.3%</td>
<td align="right">15,700</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">15,660</td>
<td align="right">0.3%</td>
<td align="right">15,660</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">63,500</td>
<td align="right">0.9%</td>
<td align="right">301,780</td>
<td align="right">1.9%</td>
<td align="right">375.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">89,180</td>
<td align="right">1.2%</td>
<td align="right">264,880</td>
<td align="right">1.7%</td>
<td align="right">197.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,709,200</td>
<td align="right">36.8%</td>
<td align="right">7,300,520</td>
<td align="right">45.7%</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">920,500</td>
<td align="right">12.5%</td>
<td align="right">2,204,620</td>
<td align="right">13.8%</td>
<td align="right">139.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">165,800</td>
<td align="right">2.3%</td>
<td align="right">367,380</td>
<td align="right">2.3%</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">574,200</td>
<td align="right">7.8%</td>
<td align="right">1,227,300</td>
<td align="right">7.7%</td>
<td align="right">113.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">294,680</td>
<td align="right">4.0%</td>
<td align="right">613,540</td>
<td align="right">3.8%</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,232,940</td>
<td align="right">16.8%</td>
<td align="right">1,941,000</td>
<td align="right">12.1%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,175,300</td>
<td align="right">16.0%</td>
<td align="right">1,521,300</td>
<td align="right">9.5%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">44,340</td>
<td align="right">0.6%</td>
<td align="right">48,300</td>
<td align="right">0.3%</td>
<td align="right">8.9%</td>
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
<td align="right">3,199,300</td>
<td align="right">6.6%</td>
<td align="right">3,203,180</td>
<td align="right">6.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">4,514,940</td>
<td align="right">9.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">4,514,940</td>
<td align="right">9.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">10,427,540</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">10,427,540</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">37,731,580</td>
<td align="right">78.4%</td>
<td align="right">37,727,700</td>
<td align="right">78.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,912,600</td>
<td align="right">12.3%</td>
<td align="right">5,912,600</td>
<td align="right">12.3%</td>
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
<td align="right">1,068,500</td>
<td align="right">2.2%</td>
<td align="right">1,068,500</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">84,000</td>
<td align="right">0.2%</td>
<td align="right">84,000</td>
<td align="right">0.2%</td>
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
<td align="right">76,480</td>
<td align="right">0.2%</td>
<td align="right">76,480</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">34,911,540</td>
<td align="right">72.5%</td>
<td align="right">34,911,540</td>
<td align="right">72.5%</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">4,560</td>
<td align="right">0.0%</td>
<td align="right">1,528.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">80,380</td>
<td align="right">0.1%</td>
<td align="right">179,140</td>
<td align="right">0.2%</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">206,839,840</td>
<td align="right">206,839,840 / 0 !!</td>
<td align="right">338,822,000</td>
<td align="right">338,822,000 / 0 !!</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">434,244,397</td>
<td align="right">434,244,397 / 0 !!</td>
<td align="right">247,608,330</td>
<td align="right">247,608,330 / 0 !!</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">279,486,900</td>
<td align="right">279,486,900 / 0 !!</td>
<td align="right">397,843,220</td>
<td align="right">397,843,220 / 0 !!</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">448,496,975</td>
<td align="right">448,496,975 / 0 !!</td>
<td align="right">275,710,031</td>
<td align="right">275,710,031 / 0 !!</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">10,734,105</td>
<td align="right"></td>
<td align="right">12,504,019</td>
<td align="right"></td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">22,144</td>
<td align="right"></td>
<td align="right">20,088</td>
<td align="right"></td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">642,675</td>
<td align="right"></td>
<td align="right">660,201</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">658,238</td>
<td align="right"></td>
<td align="right">673,889</td>
<td align="right"></td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">62,868,016</td>
<td align="right"></td>
<td align="right">63,360,032</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">35,264,120</td>
<td align="right">36.8%</td>
<td align="right">35,393,060</td>
<td align="right">36.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">35,415,600</td>
<td align="right"></td>
<td align="right">35,543,640</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">61,574,989</td>
<td align="right"></td>
<td align="right">61,736,614</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,523,420</td>
<td align="right">63.2%</td>
<td align="right">60,660,600</td>
<td align="right">63.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,442,760</td>
<td align="right">63.1%</td>
<td align="right">60,476,900</td>
<td align="right">63.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">151,840</td>
<td align="right"></td>
<td align="right">151,840</td>
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
<td align="right">260</td>
<td align="right">185,240</td>
<td align="right">7,368,360</td>
<td align="right">240</td>
<td align="right">168,660</td>
<td align="right">7,176,080</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">7,180</td>
<td align="right">4.4%</td>
<td align="right">17,850.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">800</td>
<td align="right">4.4%</td>
<td align="right">15,340</td>
<td align="right">9.4%</td>
<td align="right">1,817.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,040</td>
<td align="right">50.3%</td>
<td align="right">145,520</td>
<td align="right">89.0%</td>
<td align="right">1,509.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">500</td>
<td align="right">2.8%</td>
<td align="right">7,780</td>
<td align="right">4.8%</td>
<td align="right">1,456.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,980</td>
<td align="right"></td>
<td align="right">163,460</td>
<td align="right"></td>
<td align="right">809.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">9,980</td>
<td align="right">55.5%</td>
<td align="right">40,640</td>
<td align="right">24.9%</td>
<td align="right">307.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">8,900</td>
<td align="right">49.5%</td>
<td align="right">17,900</td>
<td align="right">11.0%</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">64,265,020</td>
<td align="right"></td>
<td align="right">12,260,240</td>
<td align="right"></td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">947,401,940</td>
<td align="right">1,474.2%</td>
<td align="right">207,945,440</td>
<td align="right">1,696.1%</td>
<td align="right">-78.1%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">8,400</td>
<td align="right">92.9%</td>
<td align="right">144,800</td>
<td align="right">99.5%</td>
<td align="right">1,623.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">9,040</td>
<td align="right"></td>
<td align="right">145,520</td>
<td align="right"></td>
<td align="right">1,509.7%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">360</td>
<td align="right">4.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-83.3%</td>
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
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,560</td>
<td align="right">17.3%</td>
<td align="right">8,620</td>
<td align="right">5.9%</td>
<td align="right">452.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,200</td>
<td align="right">13.3%</td>
<td align="right">27,740</td>
<td align="right">19.1%</td>
<td align="right">2,211.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,940</td>
<td align="right">21.5%</td>
<td align="right">40,040</td>
<td align="right">27.5%</td>
<td align="right">1,963.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,900</td>
<td align="right">21.0%</td>
<td align="right">33,200</td>
<td align="right">22.8%</td>
<td align="right">1,647.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,360</td>
<td align="right">15.0%</td>
<td align="right">22,860</td>
<td align="right">15.7%</td>
<td align="right">1,580.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">740</td>
<td align="right">8.2%</td>
<td align="right">11,060</td>
<td align="right">7.6%</td>
<td align="right">1,394.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right">2,000</td>
<td align="right">1.4%</td>
<td align="right">2,400.0%</td>
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
<td align="right">1,280</td>
<td align="right">14.2%</td>
<td align="right">8,440</td>
<td align="right">5.8%</td>
<td align="right">559.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,220</td>
<td align="right">13.5%</td>
<td align="right">26,340</td>
<td align="right">18.1%</td>
<td align="right">2,059.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,740</td>
<td align="right">19.2%</td>
<td align="right">19,240</td>
<td align="right">13.2%</td>
<td align="right">1,005.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,700</td>
<td align="right">18.8%</td>
<td align="right">38,520</td>
<td align="right">26.5%</td>
<td align="right">2,165.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,360</td>
<td align="right">15.0%</td>
<td align="right">31,520</td>
<td align="right">21.7%</td>
<td align="right">2,217.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">840</td>
<td align="right">9.3%</td>
<td align="right">15,040</td>
<td align="right">10.3%</td>
<td align="right">1,690.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">5,700</td>
<td align="right">3.9%</td>
<td align="right">2,092.3%</td>
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
<td align="left">_DEOPT</td>
<td align="right">2,540</td>
<td align="right">16,480</td>
<td align="right">548.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">859,100</td>
<td align="right">780</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">38,820</td>
<td align="right">40</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">80,620</td>
<td align="right">520</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">407,460</td>
<td align="right">2,960</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">453,080</td>
<td align="right">3,580</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1,034,380</td>
<td align="right">16,740</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">55,120</td>
<td align="right">940</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">75,680</td>
<td align="right">1,860</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">136,680</td>
<td align="right">3,440</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,232,280</td>
<td align="right">31,160</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">462,460</td>
<td align="right">12,280</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">288,980</td>
<td align="right">7,820</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">621,460</td>
<td align="right">17,100</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">467,140</td>
<td align="right">13,760</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">467,140</td>
<td align="right">13,760</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,098,760</td>
<td align="right">37,660</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">1,286,080</td>
<td align="right">45,900</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,623,700</td>
<td align="right">129,420</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">809,620</td>
<td align="right">30,240</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">631,620</td>
<td align="right">23,900</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">92,520</td>
<td align="right">4,200</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">6,160</td>
<td align="right">320</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,038,140</td>
<td align="right">242,080</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,150,640</td>
<td align="right">81,180</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,949,560</td>
<td align="right">139,920</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,028,240</td>
<td align="right">75,980</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">905,340</td>
<td align="right">67,660</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,846,440</td>
<td align="right">455,900</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2,548,980</td>
<td align="right">203,060</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">1,204,260</td>
<td align="right">97,860</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,204,260</td>
<td align="right">97,860</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,224,760</td>
<td align="right">183,400</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,944,260</td>
<td align="right">852,000</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">9,800</td>
<td align="right">840</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,377,640</td>
<td align="right">290,680</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,745,540</td>
<td align="right">509,260</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,133,520</td>
<td align="right">286,960</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,787,640</td>
<td align="right">351,800</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">5,914,920</td>
<td align="right">555,080</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,791,280</td>
<td align="right">361,220</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,742,080</td>
<td align="right">693,240</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,760</td>
<td align="right">520</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,760</td>
<td align="right">520</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">4,501,660</td>
<td align="right">495,920</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">517,900</td>
<td align="right">58,000</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">4,520,820</td>
<td align="right">512,440</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">89,120</td>
<td align="right">10,960</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,272,800</td>
<td align="right">536,820</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">11,768,340</td>
<td align="right">1,509,460</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,126,840</td>
<td align="right">148,540</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,126,840</td>
<td align="right">148,540</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,794,480</td>
<td align="right">516,200</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">14,405,640</td>
<td align="right">1,983,640</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,691,160</td>
<td align="right">1,063,380</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,811,400</td>
<td align="right">531,220</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">10,631,100</td>
<td align="right">1,541,160</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">36,233,000</td>
<td align="right">5,389,680</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">9,316,160</td>
<td align="right">1,431,740</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,120</td>
<td align="right">960</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,187,140</td>
<td align="right">2,077,200</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">9,758,220</td>
<td align="right">1,545,720</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">57,785,800</td>
<td align="right">9,546,280</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3,767,760</td>
<td align="right">627,180</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">11,570,500</td>
<td align="right">1,934,880</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,047,440</td>
<td align="right">1,540,980</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,047,440</td>
<td align="right">1,540,980</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,047,580</td>
<td align="right">3,972,980</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">971,200</td>
<td align="right">169,800</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,049,460</td>
<td align="right">539,580</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">11,035,640</td>
<td align="right">1,959,640</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,349,120</td>
<td align="right">3,168,540</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">477,740</td>
<td align="right">87,400</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">7,229,960</td>
<td align="right">1,377,880</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">64,265,020</td>
<td align="right">12,260,240</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,296,840</td>
<td align="right">441,560</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,728,340</td>
<td align="right">1,108,460</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">23,509,440</td>
<td align="right">4,596,960</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">60,313,920</td>
<td align="right">11,796,320</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">36,000</td>
<td align="right">7,080</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">28,890,360</td>
<td align="right">5,731,420</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,066,620</td>
<td align="right">411,400</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">719,380</td>
<td align="right">145,580</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,064,760</td>
<td align="right">435,140</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">20,458,280</td>
<td align="right">4,332,120</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">32,835,140</td>
<td align="right">7,011,560</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,130,160</td>
<td align="right">457,040</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">89,428,340</td>
<td align="right">19,241,860</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,380,840</td>
<td align="right">297,800</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">107,980</td>
<td align="right">23,540</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">6,772,100</td>
<td align="right">1,484,860</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">291,020</td>
<td align="right">65,740</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">21,287,120</td>
<td align="right">4,814,000</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,763,240</td>
<td align="right">4,398,620</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,460</td>
<td align="right">820</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">33,640</td>
<td align="right">8,000</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">440,320</td>
<td align="right">104,760</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">440,320</td>
<td align="right">104,760</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">408,460</td>
<td align="right">98,800</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,172,920</td>
<td align="right">4,675,520</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">15,963,480</td>
<td align="right">3,999,420</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">68,080</td>
<td align="right">17,520</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">109,660</td>
<td align="right">29,900</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,043,200</td>
<td align="right">286,660</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">678,300</td>
<td align="right">194,360</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">32,039,720</td>
<td align="right">9,444,780</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,575,540</td>
<td align="right">766,720</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,799,300</td>
<td align="right">846,860</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">3,752,180</td>
<td align="right">1,145,520</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">17,447,920</td>
<td align="right">5,356,000</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">7,032,680</td>
<td align="right">2,170,140</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">248,660</td>
<td align="right">77,540</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">8,928,280</td>
<td align="right">2,920,920</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,921,100</td>
<td align="right">2,926,700</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,935,020</td>
<td align="right">3,000,980</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">21,808,560</td>
<td align="right">7,433,520</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">809,000</td>
<td align="right">276,240</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,245,440</td>
<td align="right">806,940</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">15,202,000</td>
<td align="right">5,725,420</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,463,520</td>
<td align="right">2,685,720</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">49,400</td>
<td align="right">21,520</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">169,940</td>
<td align="right">74,060</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,152,300</td>
<td align="right">2,712,660</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">25,400</td>
<td align="right">11,320</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">25,400</td>
<td align="right">11,320</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">39,260</td>
<td align="right">22,180</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">3,140</td>
<td align="right">1,840</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">3,140</td>
<td align="right">1,840</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">45,540</td>
<td align="right">27,180</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">195,260</td>
<td align="right">120,540</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,233,600</td>
<td align="right">1,452,800</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">39,420</td>
<td align="right">26,220</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">136,960</td>
<td align="right">92,880</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,611,500</td>
<td align="right">1,119,500</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">504,280</td>
<td align="right">394,580</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">83,120</td>
<td align="right">65,200</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">85,840</td>
<td align="right">68,960</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,200</td>
<td align="right">2,560</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,100,300</td>
<td align="right">950,040</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">13,160</td>
<td align="right">11,760</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">428,200</td>
<td align="right">387,800</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">413,040</td>
<td align="right">378,560</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">207,080</td>
<td align="right">189,840</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">429,780</td>
<td align="right">401,980</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">13,540</td>
<td align="right">13,500</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">13,540</td>
<td align="right">13,500</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">140,480</td>
<td align="right">140,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">590,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">421,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">421,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">421,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">415,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">25,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">25,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">21,440</td>
<td align="right">21,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">19,960</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">9,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">5,660</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">4,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">13,107,100</td>
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
<td align="right">440</td>
<td align="right">2,620</td>
<td align="right">495.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">420</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-23
