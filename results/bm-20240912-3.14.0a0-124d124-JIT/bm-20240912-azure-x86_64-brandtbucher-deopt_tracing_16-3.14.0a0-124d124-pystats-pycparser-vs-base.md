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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">118,760</td>
<td align="right">1,369,460</td>
<td align="right">1,053.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,499,840</td>
<td align="right">6,925,540</td>
<td align="right">361.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">40,760</td>
<td align="right">78,360</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,144,560</td>
<td align="right">3,668,440</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">7,180</td>
<td align="right">2,140</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,917,880</td>
<td align="right">3,210,780</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,600</td>
<td align="right">1,520</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,162,160</td>
<td align="right">27,989,020</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,780</td>
<td align="right">2,720</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">53,600</td>
<td align="right">25,720</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,100</td>
<td align="right">2,520</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">63,820</td>
<td align="right">35,380</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">26,940</td>
<td align="right">15,000</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">31,920</td>
<td align="right">19,280</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,640</td>
<td align="right">2,900</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">11,428,020</td>
<td align="right">15,638,100</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">7,940</td>
<td align="right">5,300</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">12,513,180</td>
<td align="right">16,387,980</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">10,461,160</td>
<td align="right">7,365,960</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,880</td>
<td align="right">10,680</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,000</td>
<td align="right">2,940</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">125,400</td>
<td align="right">95,320</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,000</td>
<td align="right">6,380</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,100</td>
<td align="right">28,220</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,600</td>
<td align="right">7,000</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,042,120</td>
<td align="right">851,740</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">147,380</td>
<td align="right">123,200</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,240</td>
<td align="right">8,620</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">9,100</td>
<td align="right">7,700</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">82,220</td>
<td align="right">71,180</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">87,340</td>
<td align="right">76,000</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,780</td>
<td align="right">4,160</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">42,980,840</td>
<td align="right">48,207,120</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">36,700</td>
<td align="right">32,800</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">15,640</td>
<td align="right">14,160</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">78,654,640</td>
<td align="right">71,513,800</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">10,120</td>
<td align="right">9,320</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,419,180</td>
<td align="right">6,902,640</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,983,700</td>
<td align="right">5,594,420</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">168,981,920</td>
<td align="right">179,566,380</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,089,300</td>
<td align="right">7,588,180</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">77,380</td>
<td align="right">72,600</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">61,567,560</td>
<td align="right">57,932,120</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,060,600</td>
<td align="right">11,381,220</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">234,600</td>
<td align="right">221,440</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">104,336,060</td>
<td align="right">98,540,340</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">50,620</td>
<td align="right">47,860</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">25,443,300</td>
<td align="right">26,787,760</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,936,760</td>
<td align="right">5,635,980</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">21,600</td>
<td align="right">20,640</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">61,417,760</td>
<td align="right">64,120,080</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,654,020</td>
<td align="right">12,103,280</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">87,840</td>
<td align="right">84,360</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">87,840</td>
<td align="right">84,360</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">43,920</td>
<td align="right">42,180</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">42,100</td>
<td align="right">43,360</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,669,380</td>
<td align="right">25,022,980</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">343,840</td>
<td align="right">336,340</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">147,046,540</td>
<td align="right">143,872,660</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,014,760</td>
<td align="right">90,252,740</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,431,440</td>
<td align="right">1,455,840</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,431,760</td>
<td align="right">1,456,160</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">4,780</td>
<td align="right">4,700</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">718,340</td>
<td align="right">706,460</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">9,450,180</td>
<td align="right">9,296,100</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">45,876,460</td>
<td align="right">46,540,500</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">35,436,040</td>
<td align="right">34,940,480</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,397,480</td>
<td align="right">35,900,560</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">138,122,960</td>
<td align="right">139,982,320</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,199,700</td>
<td align="right">3,239,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">930,070,940</td>
<td align="right">919,543,360</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">88,138,700</td>
<td align="right">87,141,980</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">319,346,960</td>
<td align="right">316,246,660</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">90,613,060</td>
<td align="right">91,444,260</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">230,880</td>
<td align="right">229,180</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">509,600</td>
<td align="right">506,200</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">515,360</td>
<td align="right">512,120</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,227,460</td>
<td align="right">36,010,240</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,782,940</td>
<td align="right">12,709,880</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">51,431,940</td>
<td align="right">51,175,360</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,855,160</td>
<td align="right">3,840,680</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,353,880</td>
<td align="right">4,339,840</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,763,960</td>
<td align="right">10,730,260</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">81,667,700</td>
<td align="right">81,913,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">6,872,660</td>
<td align="right">6,852,020</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,433,080</td>
<td align="right">7,411,720</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">859,740</td>
<td align="right">857,320</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">64,356,940</td>
<td align="right">64,181,640</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,236,800</td>
<td align="right">9,212,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,173,960</td>
<td align="right">5,162,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22,055,220</td>
<td align="right">22,004,520</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,154,360</td>
<td align="right">12,129,780</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,225,280</td>
<td align="right">11,242,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,880,760</td>
<td align="right">1,878,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">27,256,500</td>
<td align="right">27,290,480</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">55,964,200</td>
<td align="right">55,903,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">21,922,480</td>
<td align="right">21,901,760</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">118,802,200</td>
<td align="right">118,911,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,517,820</td>
<td align="right">3,520,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">41,763,540</td>
<td align="right">41,739,340</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">87,294,480</td>
<td align="right">87,246,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">41,758,320</td>
<td align="right">41,738,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">45,515,060</td>
<td align="right">45,504,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">16,315,760</td>
<td align="right">16,314,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">61,270,460</td>
<td align="right">61,270,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,139,960</td>
<td align="right">1,139,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">554,280</td>
<td align="right">554,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">128,300</td>
<td align="right">128,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">74,920</td>
<td align="right">74,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">49,340</td>
<td align="right">49,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">40,660</td>
<td align="right">40,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15,140</td>
<td align="right">15,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">11,680</td>
<td align="right">11,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10,680</td>
<td align="right">10,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,320</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">7,220</td>
<td align="right">7,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,580</td>
<td align="right">5,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,400</td>
<td align="right">3,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,280</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,200</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">640</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">40</td>
<td align="right">40</td>
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
<td align="right">716,260</td>
<td align="right">1.3%</td>
<td align="right">703,400</td>
<td align="right">1.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,214,480</td>
<td align="right">98.7%</td>
<td align="right">54,214,480</td>
<td align="right">98.7%</td>
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
<td align="right">1,820</td>
<td align="right">87.5%</td>
<td align="right">2,800</td>
<td align="right">91.5%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">260</td>
<td align="right">12.5%</td>
<td align="right">260</td>
<td align="right">8.5%</td>
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
<td align="right">340</td>
<td align="right">18.7%</td>
<td align="right">820</td>
<td align="right">29.3%</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">240</td>
<td align="right">13.2%</td>
<td align="right">500</td>
<td align="right">17.9%</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">200</td>
<td align="right">11.0%</td>
<td align="right">320</td>
<td align="right">11.4%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">120</td>
<td align="right">6.6%</td>
<td align="right">180</td>
<td align="right">6.4%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">900</td>
<td align="right">49.5%</td>
<td align="right">960</td>
<td align="right">34.3%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
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
<td align="right">7,433,080</td>
<td align="right">100.0%</td>
<td align="right">7,411,720</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">36,380,020</td>
<td align="right">9.4%</td>
<td align="right">35,876,840</td>
<td align="right">9.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">349,446,780</td>
<td align="right">90.6%</td>
<td align="right">349,446,780</td>
<td align="right">90.7%</td>
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
<td align="right">10,040</td>
<td align="right">0.0%</td>
<td align="right">10,040</td>
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
<td align="right">10,760</td>
<td align="right">61.0%</td>
<td align="right">17,020</td>
<td align="right">71.2%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,880</td>
<td align="right">39.0%</td>
<td align="right">6,880</td>
<td align="right">28.8%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">240</td>
<td align="right">1.4%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">10,700</td>
<td align="right">99.4%</td>
<td align="right">16,760</td>
<td align="right">98.5%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
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
<td align="right">33,945,580</td>
<td align="right">8.1%</td>
<td align="right">35,399,240</td>
<td align="right">8.4%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">387,344,780</td>
<td align="right">91.9%</td>
<td align="right">386,075,040</td>
<td align="right">91.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,580</td>
<td align="right">0.0%</td>
<td align="right">7,580</td>
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
<td align="right">649,000</td>
<td align="right">100.0%</td>
<td align="right">682,240</td>
<td align="right">100.0%</td>
<td align="right">5.1%</td>
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
<td align="right">960</td>
<td align="right">960 / 0 !!</td>
<td align="right">960</td>
<td align="right">960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
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
<td align="right">1,000</td>
<td align="right">50.0%</td>
<td align="right">1,000</td>
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
<td align="right">552,480</td>
<td align="right">0.3%</td>
<td align="right">552,480</td>
<td align="right">0.3%</td>
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
<td align="right">174,812,740</td>
<td align="right">99.7%</td>
<td align="right">174,812,740</td>
<td align="right">99.7%</td>
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
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
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
<td align="right">1,320</td>
<td align="right">73.3%</td>
<td align="right">1,320</td>
<td align="right">73.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">480</td>
<td align="right">26.7%</td>
<td align="right">480</td>
<td align="right">26.7%</td>
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
<td align="right">340</td>
<td align="right">70.8%</td>
<td align="right">340</td>
<td align="right">70.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">100</td>
<td align="right">20.8%</td>
<td align="right">100</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">8.3%</td>
<td align="right">40</td>
<td align="right">8.3%</td>
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
<td align="right">1,878,500</td>
<td align="right">3.9%</td>
<td align="right">1,872,540</td>
<td align="right">3.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,538,060</td>
<td align="right">96.1%</td>
<td align="right">46,538,060</td>
<td align="right">96.1%</td>
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
<td align="right">2,040</td>
<td align="right">90.3%</td>
<td align="right">5,480</td>
<td align="right">96.1%</td>
<td align="right">168.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">9.7%</td>
<td align="right">220</td>
<td align="right">3.9%</td>
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
<td align="left">str</td>
<td align="right">360</td>
<td align="right">17.6%</td>
<td align="right">2,020</td>
<td align="right">36.9%</td>
<td align="right">461.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">940</td>
<td align="right">46.1%</td>
<td align="right">2,720</td>
<td align="right">49.6%</td>
<td align="right">189.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">740</td>
<td align="right">36.3%</td>
<td align="right">740</td>
<td align="right">13.5%</td>
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
<td align="right">371,900</td>
<td align="right">9.6%</td>
<td align="right">358,400</td>
<td align="right">9.2%</td>
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
<td align="right">3,514,760</td>
<td align="right">90.3%</td>
<td align="right">3,513,280</td>
<td align="right">90.6%</td>
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
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">720</td>
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
<td align="right">2,580</td>
<td align="right">83.8%</td>
<td align="right">6,260</td>
<td align="right">92.6%</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">16.2%</td>
<td align="right">500</td>
<td align="right">7.4%</td>
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
<td align="left">enumerate</td>
<td align="right">120</td>
<td align="right">4.7%</td>
<td align="right">1,020</td>
<td align="right">16.3%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">540</td>
<td align="right">8.6%</td>
<td align="right">237.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">600</td>
<td align="right">23.3%</td>
<td align="right">1,600</td>
<td align="right">25.6%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">320</td>
<td align="right">5.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">320</td>
<td align="right">12.4%</td>
<td align="right">620</td>
<td align="right">9.9%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">900</td>
<td align="right">34.9%</td>
<td align="right">1,640</td>
<td align="right">26.2%</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">280</td>
<td align="right">4.5%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">240</td>
<td align="right">3.8%</td>
<td align="right">50.0%</td>
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
<td align="right">134,340</td>
<td align="right">0.0%</td>
<td align="right">104,320</td>
<td align="right">0.0%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">746,465,840</td>
<td align="right">98.2%</td>
<td align="right">699,953,220</td>
<td align="right">98.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,613,740</td>
<td align="right">1.8%</td>
<td align="right">13,499,280</td>
<td align="right">1.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">2,120</td>
<td align="right">0.8%</td>
<td align="right">7,960</td>
<td align="right">2.9%</td>
<td align="right">275.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">266,900</td>
<td align="right">99.2%</td>
<td align="right">264,840</td>
<td align="right">97.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">300</td>
<td align="right">14.2%</td>
<td align="right">3,020</td>
<td align="right">37.9%</td>
<td align="right">906.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">480</td>
<td align="right">22.6%</td>
<td align="right">1,740</td>
<td align="right">21.9%</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">500</td>
<td align="right">23.6%</td>
<td align="right">1,760</td>
<td align="right">22.1%</td>
<td align="right">252.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">260</td>
<td align="right">12.3%</td>
<td align="right">680</td>
<td align="right">8.5%</td>
<td align="right">161.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">60</td>
<td align="right">2.8%</td>
<td align="right">80</td>
<td align="right">1.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">460</td>
<td align="right">21.7%</td>
<td align="right">580</td>
<td align="right">7.3%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">20</td>
<td align="right">0.9%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right"></td>
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
<td align="right">155,926,880</td>
<td align="right">100.0%</td>
<td align="right">154,751,920</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
<td align="right">5,280</td>
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
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">26,560</td>
<td align="right">0.0%</td>
<td align="right">26,560</td>
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
<td align="right">5,800</td>
<td align="right">100.0%</td>
<td align="right">5,800</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">9,540</td>
<td align="right">0.0%</td>
<td align="right">7,800</td>
<td align="right">0.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,937,640</td>
<td align="right">3.4%</td>
<td align="right">10,899,640</td>
<td align="right">3.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">309,252,580</td>
<td align="right">96.6%</td>
<td align="right">308,444,260</td>
<td align="right">96.6%</td>
<td align="right">-0.3%</td>
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
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">380</td>
<td align="right">0.2%</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">212,240</td>
<td align="right">99.9%</td>
<td align="right">211,480</td>
<td align="right">99.8%</td>
<td align="right">-0.4%</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">216.7%</td>
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
<td align="right">35,406,260</td>
<td align="right">49.8%</td>
<td align="right">34,910,840</td>
<td align="right">49.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,700,820</td>
<td align="right">50.2%</td>
<td align="right">35,700,820</td>
<td align="right">50.5%</td>
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
<td align="right">29,380</td>
<td align="right">98.7%</td>
<td align="right">29,240</td>
<td align="right">98.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">400</td>
<td align="right">1.3%</td>
<td align="right">400</td>
<td align="right">1.3%</td>
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
<td align="left">bytearray int</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">29,300</td>
<td align="right">99.7%</td>
<td align="right">29,060</td>
<td align="right">99.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">415,600</td>
<td align="right">0.2%</td>
<td align="right">2,479,320</td>
<td align="right">1.5%</td>
<td align="right">496.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">57,320</td>
<td align="right">0.0%</td>
<td align="right">26,860</td>
<td align="right">0.0%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">165,867,340</td>
<td align="right">99.7%</td>
<td align="right">158,142,540</td>
<td align="right">98.4%</td>
<td align="right">-4.7%</td>
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
<td align="right">9,600</td>
<td align="right">67.2%</td>
<td align="right">48,580</td>
<td align="right">87.9%</td>
<td align="right">406.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,680</td>
<td align="right">32.8%</td>
<td align="right">6,680</td>
<td align="right">12.1%</td>
<td align="right">42.7%</td>
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
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">2,240</td>
<td align="right">33.5%</td>
<td align="right">1,144.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">80</td>
<td align="right">1.7%</td>
<td align="right">220</td>
<td align="right">3.3%</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">760</td>
<td align="right">16.2%</td>
<td align="right">560</td>
<td align="right">8.4%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">3,660</td>
<td align="right">78.2%</td>
<td align="right">3,660</td>
<td align="right">54.8%</td>
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
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
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
<td align="right">49,441,460</td>
<td align="right">100.0%</td>
<td align="right">49,441,460</td>
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
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">320</td>
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
<td align="right">58,951,420</td>
<td align="right">1.7%</td>
<td align="right">62,316,060</td>
<td align="right">1.8%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">86,193,100</td>
<td align="right">2.5%</td>
<td align="right">85,112,960</td>
<td align="right">2.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,149,054,740</td>
<td align="right">32.9%</td>
<td align="right">1,153,353,340</td>
<td align="right">33.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,194,448,220</td>
<td align="right">62.9%</td>
<td align="right">2,193,486,540</td>
<td align="right">62.8%</td>
<td align="right">-0.0%</td>
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
<td align="right">57,320</td>
<td align="right">0.1%</td>
<td align="right">26,860</td>
<td align="right">0.0%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">134,340</td>
<td align="right">0.2%</td>
<td align="right">104,320</td>
<td align="right">0.1%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,540</td>
<td align="right">0.0%</td>
<td align="right">7,800</td>
<td align="right">0.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">716,260</td>
<td align="right">0.8%</td>
<td align="right">703,400</td>
<td align="right">0.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">35,406,260</td>
<td align="right">41.1%</td>
<td align="right">34,910,840</td>
<td align="right">41.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,380,020</td>
<td align="right">42.3%</td>
<td align="right">35,876,840</td>
<td align="right">42.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,878,500</td>
<td align="right">2.2%</td>
<td align="right">1,872,540</td>
<td align="right">2.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,433,080</td>
<td align="right">8.6%</td>
<td align="right">7,411,720</td>
<td align="right">8.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,514,760</td>
<td align="right">4.1%</td>
<td align="right">3,513,280</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">552,480</td>
<td align="right">0.6%</td>
<td align="right">552,480</td>
<td align="right">0.7%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">111,800</td>
<td align="right">0.2%</td>
<td align="right">1,142,540</td>
<td align="right">1.8%</td>
<td align="right">921.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">295,400</td>
<td align="right">0.5%</td>
<td align="right">1,328,560</td>
<td align="right">2.1%</td>
<td align="right">349.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,390,740</td>
<td align="right">44.8%</td>
<td align="right">28,025,700</td>
<td align="right">45.0%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,493,800</td>
<td align="right">2.5%</td>
<td align="right">1,443,300</td>
<td align="right">2.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,551,440</td>
<td align="right">12.8%</td>
<td align="right">7,370,140</td>
<td align="right">11.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">276,640</td>
<td align="right">0.5%</td>
<td align="right">274,900</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,842,860</td>
<td align="right">20.1%</td>
<td align="right">11,780,640</td>
<td align="right">18.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">239,600</td>
<td align="right">0.4%</td>
<td align="right">238,380</td>
<td align="right">0.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">10,698,040</td>
<td align="right">18.1%</td>
<td align="right">10,661,260</td>
<td align="right">17.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">15,640</td>
<td align="right">0.0%</td>
<td align="right">15,640</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">150,432,040</td>
<td align="right">71.1%</td>
<td align="right">150,432,040</td>
<td align="right">71.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">61,279,680</td>
<td align="right">28.9%</td>
<td align="right">61,279,680</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">61,279,160</td>
<td align="right">28.9%</td>
<td align="right">61,279,160</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
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
<td align="right">46,520,240</td>
<td align="right">22.0%</td>
<td align="right">46,520,240</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">98,540</td>
<td align="right">0.0%</td>
<td align="right">98,540</td>
<td align="right">0.0%</td>
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
<td align="right">20,280</td>
<td align="right">0.0%</td>
<td align="right">20,280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">211,723,400</td>
<td align="right">100.0%</td>
<td align="right">211,723,400</td>
<td align="right">100.0%</td>
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
<td align="right">759,972</td>
<td align="right"></td>
<td align="right">37,490</td>
<td align="right"></td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,756,150</td>
<td align="right"></td>
<td align="right">100,970,173</td>
<td align="right"></td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,797,131</td>
<td align="right"></td>
<td align="right">630,985</td>
<td align="right"></td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,052,910</td>
<td align="right"></td>
<td align="right">609,367</td>
<td align="right"></td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">3,050,894,413</td>
<td align="right">58.2%</td>
<td align="right">3,180,806,019</td>
<td align="right">59.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">3,144,448,943</td>
<td align="right">63.8%</td>
<td align="right">3,277,119,861</td>
<td align="right">64.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,940</td>
<td align="right">0.0%</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">117,919,288</td>
<td align="right"></td>
<td align="right">118,642,550</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,787,787,120</td>
<td align="right">36.2%</td>
<td align="right">1,783,887,600</td>
<td align="right">35.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">2,194,900,860</td>
<td align="right">41.8%</td>
<td align="right">2,193,761,500</td>
<td align="right">40.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">36,669,540</td>
<td align="right">8.6%</td>
<td align="right">36,671,980</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">240,158,960</td>
<td align="right">56.6%</td>
<td align="right">240,162,000</td>
<td align="right">56.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">273,126,823</td>
<td align="right"></td>
<td align="right">273,128,122</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">203,485,480</td>
<td align="right">48.0%</td>
<td align="right">203,486,120</td>
<td align="right">48.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">183,804,520</td>
<td align="right">43.4%</td>
<td align="right">183,804,620</td>
<td align="right">43.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">183,828,060</td>
<td align="right"></td>
<td align="right">183,828,120</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">48,028,940</td>
<td align="right"></td>
<td align="right">48,028,940</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="right">8,920</td>
<td align="right">13,126,300</td>
<td align="right">310,448,840</td>
<td align="right">8,920</td>
<td align="right">13,123,620</td>
<td align="right">310,379,820</td>
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
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.4%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">560</td>
<td align="right">1.5%</td>
<td align="right">1,140</td>
<td align="right">2.7%</td>
<td align="right">103.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">324,014,680</td>
<td align="right"></td>
<td align="right">454,159,460</td>
<td align="right"></td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,480</td>
<td align="right">25.8%</td>
<td align="right">12,880</td>
<td align="right">30.2%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,140</td>
<td align="right">33.1%</td>
<td align="right">4,140</td>
<td align="right">32.1%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">36,780</td>
<td align="right"></td>
<td align="right">42,660</td>
<td align="right"></td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">27,300</td>
<td align="right">74.2%</td>
<td align="right">29,780</td>
<td align="right">69.8%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">9,209,004,520</td>
<td align="right">2,842.2%</td>
<td align="right">9,521,144,320</td>
<td align="right">2,096.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">19,060</td>
<td align="right">51.8%</td>
<td align="right">19,520</td>
<td align="right">45.8%</td>
<td align="right">2.4%</td>
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
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">9,480</td>
<td align="right"></td>
<td align="right">12,880</td>
<td align="right"></td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">8,960</td>
<td align="right">94.5%</td>
<td align="right">12,120</td>
<td align="right">94.1%</td>
<td align="right">35.3%</td>
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
<td align="right">3.8%</td>
<td align="right">440</td>
<td align="right">3.4%</td>
<td align="right">22.2%</td>
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
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">100</td>
<td align="right">0.8%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">740</td>
<td align="right">7.8%</td>
<td align="right">820</td>
<td align="right">6.4%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">500</td>
<td align="right">5.3%</td>
<td align="right">1,140</td>
<td align="right">8.9%</td>
<td align="right">128.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,400</td>
<td align="right">25.3%</td>
<td align="right">2,720</td>
<td align="right">21.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,280</td>
<td align="right">24.1%</td>
<td align="right">2,760</td>
<td align="right">21.4%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,320</td>
<td align="right">13.9%</td>
<td align="right">2,980</td>
<td align="right">23.1%</td>
<td align="right">125.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,120</td>
<td align="right">22.4%</td>
<td align="right">2,300</td>
<td align="right">17.9%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="right">500</td>
<td align="right">5.3%</td>
<td align="right">800</td>
<td align="right">6.2%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">680</td>
<td align="right">7.2%</td>
<td align="right">900</td>
<td align="right">7.0%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,220</td>
<td align="right">12.9%</td>
<td align="right">1,600</td>
<td align="right">12.4%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,720</td>
<td align="right">28.7%</td>
<td align="right">3,520</td>
<td align="right">27.3%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,520</td>
<td align="right">16.0%</td>
<td align="right">2,960</td>
<td align="right">23.0%</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,880</td>
<td align="right">19.8%</td>
<td align="right">1,800</td>
<td align="right">14.0%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">440</td>
<td align="right">4.6%</td>
<td align="right">540</td>
<td align="right">4.2%</td>
<td align="right">22.7%</td>
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
<td align="right">206,900</td>
<td align="right">1,054,200</td>
<td align="right">409.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">560</td>
<td align="right">2,640</td>
<td align="right">371.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">13,523,940</td>
<td align="right">59,628,600</td>
<td align="right">340.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">520</td>
<td align="right">2,260</td>
<td align="right">334.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">560</td>
<td align="right">2,180</td>
<td align="right">289.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">560</td>
<td align="right">2,180</td>
<td align="right">289.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">18,120,040</td>
<td align="right">53,088,560</td>
<td align="right">193.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">312,820</td>
<td align="right">816,000</td>
<td align="right">160.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">324,820</td>
<td align="right">820,240</td>
<td align="right">152.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">11,380</td>
<td align="right">22,720</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">1,040</td>
<td align="right">100</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,600,440</td>
<td align="right">307,540</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">305,520</td>
<td align="right">79,220</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">47,470,140</td>
<td align="right">15,149,640</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">171,100</td>
<td align="right">73,960</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">45,112,400</td>
<td align="right">68,560,480</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,780</td>
<td align="right">4,180</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">2,780</td>
<td align="right">4,180</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1,600</td>
<td align="right">2,400</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">15,361,740</td>
<td align="right">22,502,580</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">15,160</td>
<td align="right">22,040</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,492,940</td>
<td align="right">828,900</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,492,940</td>
<td align="right">828,900</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,495,720</td>
<td align="right">833,080</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,137,520</td>
<td align="right">1,638,640</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">318,156,840</td>
<td align="right">449,085,640</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,298,440</td>
<td align="right">1,358,000</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">52,020</td>
<td align="right">30,740</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">324,014,680</td>
<td align="right">454,159,460</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,460</td>
<td align="right">3,420</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,777,220</td>
<td align="right">9,351,520</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">571,820</td>
<td align="right">762,200</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">35,820</td>
<td align="right">46,860</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,591,960</td>
<td align="right">1,793,320</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,700</td>
<td align="right">3,500</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,240</td>
<td align="right">18,440</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">137,292,480</td>
<td align="right">174,891,560</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">186,040</td>
<td align="right">236,740</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,237,780</td>
<td align="right">5,282,040</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">53,032,340</td>
<td align="right">39,495,920</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">10,780</td>
<td align="right">13,420</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">70,514,000</td>
<td align="right">54,439,080</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">195,100</td>
<td align="right">155,500</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">282,571,480</td>
<td align="right">226,077,040</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">114,298,680</td>
<td align="right">93,540,320</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">311,311,880</td>
<td align="right">255,537,160</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3,480</td>
<td align="right">2,940</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">238,665,860</td>
<td align="right">203,186,240</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,620</td>
<td align="right">13,320</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">34,960</td>
<td align="right">40,000</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">626,312,300</td>
<td align="right">712,153,460</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">1,201,940</td>
<td align="right">1,356,020</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">1,201,940</td>
<td align="right">1,356,020</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">104,160</td>
<td align="right">117,320</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4,932,040</td>
<td align="right">4,313,980</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">747,643,080</td>
<td align="right">834,753,440</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">44,800</td>
<td align="right">49,840</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">44,800</td>
<td align="right">49,840</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">17,616,980</td>
<td align="right">15,664,500</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">12,747,660</td>
<td align="right">11,496,960</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">45,540</td>
<td align="right">49,860</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">150,120</td>
<td align="right">164,160</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">29,656,440</td>
<td align="right">27,006,520</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,645,560</td>
<td align="right">9,400,020</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">35,657,280</td>
<td align="right">38,752,480</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">37,860</td>
<td align="right">41,140</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">17,613,320</td>
<td align="right">16,110,500</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">12,800</td>
<td align="right">13,860</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">516,457,300</td>
<td align="right">478,279,480</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">53,284,900</td>
<td align="right">49,409,820</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">28,122,180</td>
<td align="right">26,132,480</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">28,160,720</td>
<td align="right">26,173,440</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">28,156,820</td>
<td align="right">26,171,540</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">46,165,660</td>
<td align="right">49,241,560</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">38,540</td>
<td align="right">40,960</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,126,820</td>
<td align="right">9,624,720</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">24,975,380</td>
<td align="right">23,714,040</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">30,386,140</td>
<td align="right">28,892,760</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">118,284,560</td>
<td align="right">124,080,280</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">20,360</td>
<td align="right">21,320</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">20,360</td>
<td align="right">21,320</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,500</td>
<td align="right">15,120</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">190,650,300</td>
<td align="right">183,306,020</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">102,051,000</td>
<td align="right">105,171,800</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,362,120</td>
<td align="right">4,240,740</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">38,930,940</td>
<td align="right">39,927,660</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">28,740,400</td>
<td align="right">29,460,120</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">53,833,520</td>
<td align="right">52,489,060</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">700,700</td>
<td align="right">715,300</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">121,223,840</td>
<td align="right">118,818,240</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">41,565,040</td>
<td align="right">42,336,460</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">998,019,360</td>
<td align="right">1,015,273,320</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,613,420</td>
<td align="right">3,672,080</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">38,453,940</td>
<td align="right">39,006,320</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">273,920</td>
<td align="right">277,320</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">167,060</td>
<td align="right">169,120</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">259,572,440</td>
<td align="right">262,676,440</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,081,100</td>
<td align="right">1,093,960</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">263,549,700</td>
<td align="right">260,916,340</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">38,420</td>
<td align="right">38,060</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">299,817,040</td>
<td align="right">302,180,480</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,584,280</td>
<td align="right">1,596,220</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">57,900</td>
<td align="right">58,260</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">57,900</td>
<td align="right">58,260</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">48,634,180</td>
<td align="right">48,934,960</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">67,798,400</td>
<td align="right">68,145,840</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,171,320</td>
<td align="right">54,890,340</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">240,166,120</td>
<td align="right">239,025,780</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,499,500</td>
<td align="right">5,523,580</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,077,200</td>
<td align="right">1,081,100</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">78,852,120</td>
<td align="right">78,580,140</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">10,581,960</td>
<td align="right">10,546,200</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">10,581,960</td>
<td align="right">10,546,200</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,581,960</td>
<td align="right">10,546,200</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">45,426,740</td>
<td align="right">45,552,640</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">86,829,660</td>
<td align="right">87,004,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">36,528,280</td>
<td align="right">36,463,220</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">34,561,060</td>
<td align="right">34,620,840</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">971,800</td>
<td align="right">973,400</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">134,081,400</td>
<td align="right">134,298,620</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">32,388,680</td>
<td align="right">32,439,840</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,667,000</td>
<td align="right">1,669,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">190,415,500</td>
<td align="right">190,133,100</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">19,022,520</td>
<td align="right">19,047,140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">90,455,120</td>
<td align="right">90,561,600</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">190,659,300</td>
<td align="right">190,445,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">15,168,100</td>
<td align="right">15,182,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">28,052,140</td>
<td align="right">28,076,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">28,043,240</td>
<td align="right">28,067,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">14,277,800</td>
<td align="right">14,290,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">89,384,360</td>
<td align="right">89,457,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">89,384,360</td>
<td align="right">89,457,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">46,447,040</td>
<td align="right">46,409,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">28,108,740</td>
<td align="right">28,130,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">28,044,640</td>
<td align="right">28,065,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">84,426,140</td>
<td align="right">84,487,140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">28,040,440</td>
<td align="right">28,060,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">20,827,180</td>
<td align="right">20,814,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,646,360</td>
<td align="right">11,653,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">49,307,500</td>
<td align="right">49,337,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">38,165,460</td>
<td align="right">38,184,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">43,214,160</td>
<td align="right">43,233,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">23,680,800</td>
<td align="right">23,689,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">11,211,760</td>
<td align="right">11,215,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">62,023,480</td>
<td align="right">62,039,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">24,013,880</td>
<td align="right">24,019,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,112,440</td>
<td align="right">6,113,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">40,021,480</td>
<td align="right">40,028,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">43,209,460</td>
<td align="right">43,216,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">527,800</td>
<td align="right">527,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">38,907,020</td>
<td align="right">38,911,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">23,451,520</td>
<td align="right">23,454,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">36,627,100</td>
<td align="right">36,630,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,255,860</td>
<td align="right">3,255,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">123,840</td>
<td align="right">123,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">24,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">24,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">12,980</td>
<td align="right">12,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">5,740</td>
<td align="right">5,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">3,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">3,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">3,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">1,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right"></td>
<td align="right">160</td>
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
<td align="right">500</td>
<td align="right">760</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">9,500</td>
<td align="right">11,960</td>
<td align="right">25.9%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
Stats gathered on: 2024-09-13
