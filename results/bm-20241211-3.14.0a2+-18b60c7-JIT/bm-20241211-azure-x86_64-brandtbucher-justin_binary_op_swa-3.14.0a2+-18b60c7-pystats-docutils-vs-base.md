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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,533,540</td>
<td align="right">3,297,360</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">44,056,560</td>
<td align="right">46,553,420</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">45,857,780</td>
<td align="right">48,372,760</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,124,540</td>
<td align="right">34,759,460</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">17,852,480</td>
<td align="right">18,682,920</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">34,923,820</td>
<td align="right">36,496,740</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">62,869,860</td>
<td align="right">65,556,500</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">37,474,220</td>
<td align="right">38,970,560</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,360,680</td>
<td align="right">50,165,400</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">119,386,680</td>
<td align="right">122,466,940</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">10,034,400</td>
<td align="right">9,790,820</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,268,420</td>
<td align="right">8,467,800</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">234,015,320</td>
<td align="right">238,758,560</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,806,820</td>
<td align="right">8,628,420</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">197,883,620</td>
<td align="right">201,754,980</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">68,748,500</td>
<td align="right">70,052,780</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">93,026,280</td>
<td align="right">94,783,540</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">148,702,400</td>
<td align="right">151,258,960</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">24,990,900</td>
<td align="right">24,563,520</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">325,221,160</td>
<td align="right">330,634,180</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,735,800</td>
<td align="right">103,318,280</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">77,650,480</td>
<td align="right">78,852,280</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,734,820</td>
<td align="right">5,655,800</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,839,720</td>
<td align="right">4,905,940</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,826,540</td>
<td align="right">20,553,540</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,016,520</td>
<td align="right">17,821,460</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">55,677,280</td>
<td align="right">55,095,900</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,255,940</td>
<td align="right">16,090,840</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,372,081,240</td>
<td align="right">1,385,788,140</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">7,938,940</td>
<td align="right">7,861,440</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">76,303,980</td>
<td align="right">75,588,900</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,452,140</td>
<td align="right">10,357,740</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,005,500</td>
<td align="right">11,897,940</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,005,860</td>
<td align="right">24,209,940</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">44,322,200</td>
<td align="right">43,975,600</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">303,380,780</td>
<td align="right">305,731,140</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">195,636,800</td>
<td align="right">197,143,640</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">207,729,900</td>
<td align="right">209,144,920</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">173,113,760</td>
<td align="right">172,100,360</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,585,540</td>
<td align="right">10,530,060</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,836,320</td>
<td align="right">77,514,060</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,594,320</td>
<td align="right">28,702,940</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,744,980</td>
<td align="right">39,601,620</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">39,377,100</td>
<td align="right">39,507,700</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">294,453,160</td>
<td align="right">295,366,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">314,603,820</td>
<td align="right">315,368,380</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">66,691,800</td>
<td align="right">66,561,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,706,540</td>
<td align="right">15,677,160</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">105,173,660</td>
<td align="right">105,281,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,560,640</td>
<td align="right">51,522,960</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">122,717,420</td>
<td align="right">122,632,020</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">307,607,740</td>
<td align="right">307,818,780</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">223,302,620</td>
<td align="right">223,166,120</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,340,720</td>
<td align="right">56,373,940</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,072,980</td>
<td align="right">30,055,780</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,074,360</td>
<td align="right">30,057,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,924,980</td>
<td align="right">1,925,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,573,100</td>
<td align="right">38,581,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,324,560</td>
<td align="right">26,328,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,227,540</td>
<td align="right">5,227,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,205,520</td>
<td align="right">1,205,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">7,035,220</td>
<td align="right">7,034,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">9,620,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,475,120</td>
<td align="right">26,475,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,369,400</td>
<td align="right">13,369,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,954,300</td>
<td align="right">17,954,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">19,311,060</td>
<td align="right">19,311,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,491,260</td>
<td align="right">20,491,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,298,480</td>
<td align="right">49,298,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,563,460</td>
<td align="right">27,563,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">122,727,460</td>
<td align="right">122,727,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,944,460</td>
<td align="right">91,944,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,534,540</td>
<td align="right">38,534,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,114,500</td>
<td align="right">37,114,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">36,886,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,888,280</td>
<td align="right">22,888,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,048,940</td>
<td align="right">21,048,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,565,660</td>
<td align="right">20,565,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,358,660</td>
<td align="right">19,358,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,706,060</td>
<td align="right">17,706,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,539,060</td>
<td align="right">16,539,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,100,320</td>
<td align="right">15,100,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,362,660</td>
<td align="right">11,362,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,783,620</td>
<td align="right">10,783,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,898,840</td>
<td align="right">9,898,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,607,300</td>
<td align="right">8,607,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,742,940</td>
<td align="right">7,742,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">7,613,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,146,540</td>
<td align="right">7,146,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,134,760</td>
<td align="right">6,134,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,134,760</td>
<td align="right">6,134,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,803,020</td>
<td align="right">5,803,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,778,660</td>
<td align="right">5,778,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,719,020</td>
<td align="right">5,719,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,440</td>
<td align="right">5,440,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,322,120</td>
<td align="right">5,322,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">4,951,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">4,587,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,193,640</td>
<td align="right">4,193,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,944,720</td>
<td align="right">3,944,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,425,140</td>
<td align="right">3,425,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,219,980</td>
<td align="right">3,219,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,874,000</td>
<td align="right">2,874,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,760,100</td>
<td align="right">2,760,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,731,500</td>
<td align="right">2,731,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,728,440</td>
<td align="right">2,728,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,620,720</td>
<td align="right">2,620,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,448,340</td>
<td align="right">2,448,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,885,920</td>
<td align="right">1,885,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,677,240</td>
<td align="right">1,677,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,423,400</td>
<td align="right">1,423,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,413,900</td>
<td align="right">1,413,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,175,460</td>
<td align="right">1,175,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">853,740</td>
<td align="right">853,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">840,600</td>
<td align="right">840,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">740,040</td>
<td align="right">740,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">724,200</td>
<td align="right">724,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">672,060</td>
<td align="right">672,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">440,340</td>
<td align="right">440,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">361,260</td>
<td align="right">361,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">332,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,120</td>
<td align="right">267,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">230,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">228,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">176,880</td>
<td align="right">176,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">156,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">91,560</td>
<td align="right">91,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">75,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">73,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,560</td>
<td align="right">61,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right">49,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">16,860</td>
<td align="right">16,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,640</td>
<td align="right">14,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">11,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,820</td>
<td align="right">8,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,260</td>
<td align="right">7,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,000</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,420</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
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
<td align="right">21,036,720</td>
<td align="right">30.3%</td>
<td align="right">21,036,720</td>
<td align="right">30.3%</td>
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
<td align="right">48,411,720</td>
<td align="right">69.7%</td>
<td align="right">48,411,720</td>
<td align="right">69.7%</td>
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
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,020</td>
<td align="right">98.4%</td>
<td align="right">12,020</td>
<td align="right">98.4%</td>
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
<td align="right">4,980</td>
<td align="right">41.4%</td>
<td align="right">4,980</td>
<td align="right">41.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,200</td>
<td align="right">26.6%</td>
<td align="right">3,200</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">26.3%</td>
<td align="right">3,160</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">2.7%</td>
<td align="right">320</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">160</td>
<td align="right">1.3%</td>
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
<td align="right">10,783,620</td>
<td align="right">100.0%</td>
<td align="right">10,783,620</td>
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
<td align="right">10,440,380</td>
<td align="right">9.8%</td>
<td align="right">10,346,000</td>
<td align="right">9.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,163,860</td>
<td align="right">2.0%</td>
<td align="right">2,161,840</td>
<td align="right">2.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,971,640</td>
<td align="right">88.2%</td>
<td align="right">93,973,620</td>
<td align="right">88.2%</td>
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
<td align="right">11,140</td>
<td align="right">21.2%</td>
<td align="right">11,120</td>
<td align="right">21.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,400</td>
<td align="right">78.8%</td>
<td align="right">41,360</td>
<td align="right">78.8%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,740</td>
<td align="right">15.6%</td>
<td align="right">1,720</td>
<td align="right">15.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,820</td>
<td align="right">70.2%</td>
<td align="right">7,820</td>
<td align="right">70.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.5%</td>
<td align="right">720</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">6.1%</td>
<td align="right">680</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.6%</td>
<td align="right">180</td>
<td align="right">1.6%</td>
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
<td align="right">17,611,960</td>
<td align="right">3.1%</td>
<td align="right">17,615,020</td>
<td align="right">3.1%</td>
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
<td align="right">553,235,460</td>
<td align="right">96.9%</td>
<td align="right">553,231,620</td>
<td align="right">96.9%</td>
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
<td align="right">336,420</td>
<td align="right">100.0%</td>
<td align="right">336,480</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
<td align="right">1,663,960</td>
<td align="right">4.5%</td>
<td align="right">1,663,960</td>
<td align="right">4.5%</td>
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
<td align="right">34,778,780</td>
<td align="right">94.7%</td>
<td align="right">34,778,780</td>
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
<td align="right">259,420</td>
<td align="right">0.7%</td>
<td align="right">259,420</td>
<td align="right">0.7%</td>
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
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,940</td>
<td align="right">71.3%</td>
<td align="right">12,940</td>
<td align="right">71.3%</td>
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
<td align="right">12,480</td>
<td align="right">96.4%</td>
<td align="right">12,480</td>
<td align="right">96.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">8,801,960</td>
<td align="right">13.9%</td>
<td align="right">8,623,620</td>
<td align="right">13.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
<td align="right">54,350,400</td>
<td align="right">86.3%</td>
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
<td align="right">4,740</td>
<td align="right">97.5%</td>
<td align="right">4,680</td>
<td align="right">97.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.5%</td>
<td align="right">120</td>
<td align="right">2.5%</td>
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
<td align="right">1,180</td>
<td align="right">24.9%</td>
<td align="right">1,140</td>
<td align="right">24.4%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">880</td>
<td align="right">18.6%</td>
<td align="right">860</td>
<td align="right">18.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,880</td>
<td align="right">39.7%</td>
<td align="right">1,880</td>
<td align="right">40.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">800</td>
<td align="right">17.1%</td>
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
<td align="right">24,984,000</td>
<td align="right">13.8%</td>
<td align="right">24,556,720</td>
<td align="right">13.6%</td>
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
<td align="right">129,223,180</td>
<td align="right">71.6%</td>
<td align="right">129,973,100</td>
<td align="right">71.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,325,160</td>
<td align="right">14.6%</td>
<td align="right">26,433,080</td>
<td align="right">14.6%</td>
<td align="right">0.4%</td>
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
<td align="right">6,900</td>
<td align="right">1.4%</td>
<td align="right">6,800</td>
<td align="right">1.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">496,680</td>
<td align="right">98.6%</td>
<td align="right">498,720</td>
<td align="right">98.7%</td>
<td align="right">0.4%</td>
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
<td align="right">600</td>
<td align="right">8.7%</td>
<td align="right">560</td>
<td align="right">8.2%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,020</td>
<td align="right">14.8%</td>
<td align="right">980</td>
<td align="right">14.4%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,460</td>
<td align="right">21.2%</td>
<td align="right">1,440</td>
<td align="right">21.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">35.9%</td>
<td align="right">2,480</td>
<td align="right">36.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">8.1%</td>
<td align="right">560</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">5.8%</td>
<td align="right">400</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">3.2%</td>
<td align="right">220</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
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
<td align="right">277,131,700</td>
<td align="right">26.7%</td>
<td align="right">281,862,600</td>
<td align="right">27.0%</td>
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
<td align="right">101,078,980</td>
<td align="right">9.7%</td>
<td align="right">102,661,060</td>
<td align="right">9.8%</td>
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
<td align="right">659,000,820</td>
<td align="right">63.5%</td>
<td align="right">657,362,740</td>
<td align="right">63.1%</td>
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
<td align="left">Failure</td>
<td align="right">20,040</td>
<td align="right">0.3%</td>
<td align="right">20,440</td>
<td align="right">0.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,865,280</td>
<td align="right">99.7%</td>
<td align="right">5,954,500</td>
<td align="right">99.7%</td>
<td align="right">1.5%</td>
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
<td align="right">9,660</td>
<td align="right">48.2%</td>
<td align="right">10,100</td>
<td align="right">49.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,180</td>
<td align="right">25.8%</td>
<td align="right">5,140</td>
<td align="right">25.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">14.2%</td>
<td align="right">2,840</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">3.2%</td>
<td align="right">640</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.1%</td>
<td align="right">420</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">2.0%</td>
<td align="right">400</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.2%</td>
<td align="right">240</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
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
<td align="right">275,717,800</td>
<td align="right">100.0%</td>
<td align="right">279,266,900</td>
<td align="right">100.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,140</td>
<td align="right">0.0%</td>
<td align="right">2,140</td>
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
<td align="right">1,960</td>
<td align="right">100.0%</td>
<td align="right">1,960</td>
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
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">7,260</td>
<td align="right">100.0%</td>
<td align="right">7,260</td>
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
<td align="right">20,478,280</td>
<td align="right">16.9%</td>
<td align="right">20,478,240</td>
<td align="right">16.9%</td>
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
<td align="right">47,039,540</td>
<td align="right">38.7%</td>
<td align="right">47,039,540</td>
<td align="right">38.7%</td>
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
<td align="right">53,915,360</td>
<td align="right">44.4%</td>
<td align="right">53,915,360</td>
<td align="right">44.4%</td>
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
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,580</td>
<td align="right">1.2%</td>
<td align="right">12,580</td>
<td align="right">1.2%</td>
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
<td align="left">class attr simple</td>
<td align="right">9,940</td>
<td align="right">79.0%</td>
<td align="right">9,940</td>
<td align="right">79.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">16.2%</td>
<td align="right">2,040</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">2.9%</td>
<td align="right">360</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
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
<td align="right">267,120</td>
<td align="right">100.0%</td>
<td align="right">267,120</td>
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
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
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
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
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
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
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
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.1%</td>
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
<td align="right">10,094,000</td>
<td align="right">3.6%</td>
<td align="right">10,175,680</td>
<td align="right">3.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">269,039,400</td>
<td align="right">95.0%</td>
<td align="right">268,999,180</td>
<td align="right">95.0%</td>
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
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
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
<td align="right">191,300</td>
<td align="right">53.4%</td>
<td align="right">192,840</td>
<td align="right">53.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,000</td>
<td align="right">46.6%</td>
<td align="right">167,000</td>
<td align="right">46.4%</td>
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
<td align="left">number</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,290,020</td>
<td align="right">100.0%</td>
<td align="right">48,290,020</td>
<td align="right">100.0%</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">387,516,960</td>
<td align="right">5.5%</td>
<td align="right">392,438,480</td>
<td align="right">5.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,790,174,780</td>
<td align="right">54.1%</td>
<td align="right">3,823,417,900</td>
<td align="right">54.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,617,489,940</td>
<td align="right">37.4%</td>
<td align="right">2,635,013,700</td>
<td align="right">37.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">208,792,820</td>
<td align="right">3.0%</td>
<td align="right">209,675,080</td>
<td align="right">3.0%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">8,801,960</td>
<td align="right">4.2%</td>
<td align="right">8,623,620</td>
<td align="right">4.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">24,984,000</td>
<td align="right">12.0%</td>
<td align="right">24,556,720</td>
<td align="right">11.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,078,980</td>
<td align="right">48.6%</td>
<td align="right">102,661,060</td>
<td align="right">49.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,440,380</td>
<td align="right">5.0%</td>
<td align="right">10,346,000</td>
<td align="right">5.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,478,280</td>
<td align="right">9.9%</td>
<td align="right">20,478,240</td>
<td align="right">9.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,036,720</td>
<td align="right">10.1%</td>
<td align="right">21,036,720</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,783,620</td>
<td align="right">5.2%</td>
<td align="right">10,783,620</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">2.2%</td>
<td align="right">4,583,860</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,776,840</td>
<td align="right">1.8%</td>
<td align="right">3,776,840</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,663,960</td>
<td align="right">0.8%</td>
<td align="right">1,663,960</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,538,240</td>
<td align="right">8.1%</td>
<td align="right">33,214,340</td>
<td align="right">8.5%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">49,832,920</td>
<td align="right">12.9%</td>
<td align="right">51,050,440</td>
<td align="right">13.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">82,567,200</td>
<td align="right">21.3%</td>
<td align="right">83,989,300</td>
<td align="right">21.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,507,320</td>
<td align="right">1.4%</td>
<td align="right">5,548,000</td>
<td align="right">1.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">102,868,700</td>
<td align="right">26.5%</td>
<td align="right">103,342,180</td>
<td align="right">26.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,162,680</td>
<td align="right">3.4%</td>
<td align="right">13,216,740</td>
<td align="right">3.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,162,480</td>
<td align="right">3.4%</td>
<td align="right">13,216,340</td>
<td align="right">3.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">2.0%</td>
<td align="right">7,574,760</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,573,760</td>
<td align="right">2.5%</td>
<td align="right">9,576,880</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">13.9%</td>
<td align="right">53,912,180</td>
<td align="right">13.7%</td>
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
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">8,435,640</td>
<td align="right">2.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,304,200</td>
<td align="right">11.1%</td>
<td align="right">39,311,520</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,307,680</td>
<td align="right">11.1%</td>
<td align="right">39,315,000</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,615,540</td>
<td align="right">11.2%</td>
<td align="right">39,622,860</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,615,540</td>
<td align="right">11.2%</td>
<td align="right">39,622,860</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,630,860</td>
<td align="right">3.8%</td>
<td align="right">13,628,880</td>
<td align="right">3.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,780,820</td>
<td align="right">88.8%</td>
<td align="right">314,773,500</td>
<td align="right">88.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,586,940</td>
<td align="right">88.5%</td>
<td align="right">313,587,000</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">1,826,760</td>
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
<td align="right">9,598,380</td>
<td align="right">2.7%</td>
<td align="right">9,598,380</td>
<td align="right">2.7%</td>
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
<td align="right">1,689,869</td>
<td align="right"></td>
<td align="right">3,046,580</td>
<td align="right"></td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">32,866,044</td>
<td align="right"></td>
<td align="right">38,215,099</td>
<td align="right"></td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">31,937,641</td>
<td align="right"></td>
<td align="right">35,929,988</td>
<td align="right"></td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">710,702,360</td>
<td align="right">8.8%</td>
<td align="right">724,266,480</td>
<td align="right">8.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,486,626,055</td>
<td align="right">27.6%</td>
<td align="right">2,459,461,144</td>
<td align="right">27.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,710,719,324</td>
<td align="right">33.4%</td>
<td align="right">2,683,398,469</td>
<td align="right">33.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,087,398,660</td>
<td align="right">12.1%</td>
<td align="right">1,096,997,520</td>
<td align="right">12.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,692,403,473</td>
<td align="right">18.8%</td>
<td align="right">1,680,305,698</td>
<td align="right">18.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">459,808,179</td>
<td align="right"></td>
<td align="right">456,661,992</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,915,579,820</td>
<td align="right">35.9%</td>
<td align="right">2,929,112,240</td>
<td align="right">36.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,784,865,460</td>
<td align="right">22.0%</td>
<td align="right">1,778,283,050</td>
<td align="right">21.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,729,626,980</td>
<td align="right">41.5%</td>
<td align="right">3,741,668,820</td>
<td align="right">41.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">197,576,311</td>
<td align="right"></td>
<td align="right">196,965,580</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">473,817,378</td>
<td align="right"></td>
<td align="right">472,882,042</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">499,780</td>
<td align="right">0.1%</td>
<td align="right">499,180</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,520</td>
<td align="right">0.1%</td>
<td align="right">344,580</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,323,500</td>
<td align="right">35.1%</td>
<td align="right">236,346,720</td>
<td align="right">35.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,318,220</td>
<td align="right"></td>
<td align="right">236,340,880</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">437,701,320</td>
<td align="right">64.9%</td>
<td align="right">437,677,180</td>
<td align="right">64.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">436,857,020</td>
<td align="right">64.8%</td>
<td align="right">436,833,420</td>
<td align="right">64.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">26,180</td>
<td align="right">72,973,060</td>
<td align="right">1,154,400,571</td>
<td align="right">45,165,900</td>
<td align="right">99,479,060</td>
<td align="right">26,160</td>
<td align="right">72,510,300</td>
<td align="right">1,146,900,713</td>
<td align="right">44,971,020</td>
<td align="right">99,408,420</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">340</td>
<td align="right">1.0%</td>
<td align="right">300</td>
<td align="right">0.9%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">2,020</td>
<td align="right">6.2%</td>
<td align="right">1,880</td>
<td align="right">5.8%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">331,995,020</td>
<td align="right"></td>
<td align="right">312,188,260</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,022,382,220</td>
<td align="right">1,211.6%</td>
<td align="right">3,863,387,420</td>
<td align="right">1,237.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">13,120</td>
<td align="right">40.2%</td>
<td align="right">12,840</td>
<td align="right">39.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">21,600</td>
<td align="right">66.3%</td>
<td align="right">21,400</td>
<td align="right">65.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">10,800</td>
<td align="right">33.1%</td>
<td align="right">10,880</td>
<td align="right">33.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">32,600</td>
<td align="right"></td>
<td align="right">32,480</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">200</td>
<td align="right">0.6%</td>
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
<td align="right">15,560</td>
<td align="right">72.0%</td>
<td align="right">14,860</td>
<td align="right">69.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">21,600</td>
<td align="right"></td>
<td align="right">21,400</td>
<td align="right"></td>
<td align="right">-0.9%</td>
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
<td align="right">1,120</td>
<td align="right">5.2%</td>
<td align="right">1,000</td>
<td align="right">4.7%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,840</td>
<td align="right">8.5%</td>
<td align="right">1,820</td>
<td align="right">8.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,300</td>
<td align="right">33.8%</td>
<td align="right">6,980</td>
<td align="right">32.6%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,040</td>
<td align="right">23.3%</td>
<td align="right">4,760</td>
<td align="right">22.2%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,480</td>
<td align="right">16.1%</td>
<td align="right">4,020</td>
<td align="right">18.8%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">12.0%</td>
<td align="right">2,600</td>
<td align="right">12.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,040</td>
<td align="right">9.4%</td>
<td align="right">1,920</td>
<td align="right">9.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,380</td>
<td align="right">15.6%</td>
<td align="right">3,360</td>
<td align="right">15.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,080</td>
<td align="right">32.8%</td>
<td align="right">6,780</td>
<td align="right">31.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,020</td>
<td align="right">9.4%</td>
<td align="right">1,760</td>
<td align="right">8.2%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">780</td>
<td align="right">3.6%</td>
<td align="right">820</td>
<td align="right">3.8%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
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
<td align="left">_BINARY_SUBSCR</td>
<td align="right">66,000</td>
<td align="right">160,380</td>
<td align="right">143.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,882,380</td>
<td align="right">2,195,740</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,170,320</td>
<td align="right">1,135,260</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,492,920</td>
<td align="right">2,978,780</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">6,022,780</td>
<td align="right">3,501,540</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">2,073,520</td>
<td align="right">1,260,520</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,331,000</td>
<td align="right">2,696,080</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,383,060</td>
<td align="right">6,868,920</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">38,947,980</td>
<td align="right">30,456,560</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">303,080</td>
<td align="right">237,940</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">7,817,320</td>
<td align="right">6,545,180</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,356,700</td>
<td align="right">21,548,860</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">47,040,600</td>
<td align="right">40,631,740</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">19,493,520</td>
<td align="right">16,936,960</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">134,920</td>
<td align="right">152,120</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">134,920</td>
<td align="right">152,120</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">12,894,940</td>
<td align="right">11,398,600</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">34,579,080</td>
<td align="right">30,706,400</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">49,003,640</td>
<td align="right">44,252,860</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,366,420</td>
<td align="right">2,155,440</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">87,457,040</td>
<td align="right">80,115,280</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,274,440</td>
<td align="right">3,547,440</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">25,622,320</td>
<td align="right">23,689,060</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,246,160</td>
<td align="right">3,489,780</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,954,840</td>
<td align="right">2,098,200</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">16,276,080</td>
<td align="right">15,104,560</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">16,890,020</td>
<td align="right">15,688,220</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,728,540</td>
<td align="right">13,697,180</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">33,733,560</td>
<td align="right">31,409,120</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">14,931,800</td>
<td align="right">13,922,780</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">242,734,840</td>
<td align="right">226,750,080</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">22,955,220</td>
<td align="right">21,486,380</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">36,007,660</td>
<td align="right">33,728,840</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,086,300</td>
<td align="right">1,955,700</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">82,540,680</td>
<td align="right">77,386,380</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">324,890,620</td>
<td align="right">304,936,100</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,013,700</td>
<td align="right">4,257,280</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">331,995,020</td>
<td align="right">312,188,260</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,400,420</td>
<td align="right">19,413,040</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">63,494,940</td>
<td align="right">60,009,260</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">27,782,680</td>
<td align="right">26,281,160</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">28,295,220</td>
<td align="right">26,793,700</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,391,240</td>
<td align="right">3,569,580</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">367,970,360</td>
<td align="right">349,858,060</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">21,158,080</td>
<td align="right">22,170,380</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">35,975,340</td>
<td align="right">37,669,800</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">22,255,280</td>
<td align="right">23,267,900</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">31,136,700</td>
<td align="right">29,778,840</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">33,938,160</td>
<td align="right">32,485,120</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">32,397,780</td>
<td align="right">31,021,100</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">899,780</td>
<td align="right">937,460</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">899,780</td>
<td align="right">937,460</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">22,035,940</td>
<td align="right">22,956,420</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,182,680</td>
<td align="right">27,079,800</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">42,770,440</td>
<td align="right">41,206,760</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,514,720</td>
<td align="right">4,678,480</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">304,285,880</td>
<td align="right">293,271,140</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">3,760,940</td>
<td align="right">3,894,120</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,340,220</td>
<td align="right">3,447,780</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">347,947,500</td>
<td align="right">338,305,040</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">69,777,840</td>
<td align="right">67,910,460</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">14,385,240</td>
<td align="right">14,757,080</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,164,380</td>
<td align="right">2,219,860</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,244,580</td>
<td align="right">2,300,060</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,062,120</td>
<td align="right">37,166,340</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">36,436,180</td>
<td align="right">35,605,740</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">16,292,980</td>
<td align="right">16,639,580</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">98,921,880</td>
<td align="right">100,986,280</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">9,760,000</td>
<td align="right">9,560,620</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">10,011,620</td>
<td align="right">9,807,540</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">10,011,620</td>
<td align="right">9,807,540</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,454,180</td>
<td align="right">1,483,560</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">10,004,300</td>
<td align="right">9,804,960</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">10,564,800</td>
<td align="right">10,365,380</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">10,615,240</td>
<td align="right">10,415,820</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">13,948,420</td>
<td align="right">14,184,600</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">21,538,660</td>
<td align="right">21,191,260</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,143,800</td>
<td align="right">12,338,860</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">12,559,400</td>
<td align="right">12,744,720</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">88,323,040</td>
<td align="right">89,298,480</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">58,991,800</td>
<td align="right">59,565,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,129,500</td>
<td align="right">13,020,880</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">14,657,960</td>
<td align="right">14,543,160</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">193,264,600</td>
<td align="right">191,806,580</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">44,820,560</td>
<td align="right">44,486,380</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,223,080</td>
<td align="right">11,302,100</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">44,391,880</td>
<td align="right">44,104,780</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">44,391,880</td>
<td align="right">44,104,780</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,274,160</td>
<td align="right">12,351,660</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,343,040</td>
<td align="right">3,357,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">9,448,440</td>
<td align="right">9,410,960</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">24,801,540</td>
<td align="right">24,888,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,605,680</td>
<td align="right">2,613,780</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,302,940</td>
<td align="right">8,327,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">988,320</td>
<td align="right">988,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,834,600</td>
<td align="right">11,838,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,568,280</td>
<td align="right">1,567,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,329,020</td>
<td align="right">1,329,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,784,320</td>
<td align="right">1,784,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">814,660</td>
<td align="right">814,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,613,780</td>
<td align="right">1,613,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,082,720</td>
<td align="right">2,082,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,781,900</td>
<td align="right">4,781,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,977,220</td>
<td align="right">2,977,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,968,860</td>
<td align="right">3,968,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,820,420</td>
<td align="right">9,820,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,589,560</td>
<td align="right">2,589,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,231,580</td>
<td align="right">2,231,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,862,340</td>
<td align="right">1,862,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,431,600</td>
<td align="right">1,431,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,391,160</td>
<td align="right">1,391,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,391,160</td>
<td align="right">1,391,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,329,980</td>
<td align="right">1,329,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,315,200</td>
<td align="right">1,315,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,249,880</td>
<td align="right">1,249,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,183,560</td>
<td align="right">1,183,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">931,120</td>
<td align="right">931,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">841,220</td>
<td align="right">841,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">841,220</td>
<td align="right">841,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">651,440</td>
<td align="right">651,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">362,720</td>
<td align="right">362,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">262,940</td>
<td align="right">262,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">255,620</td>
<td align="right">255,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">116,700</td>
<td align="right">116,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">106,620</td>
<td align="right">106,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">82,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">82,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">70,160</td>
<td align="right">70,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">64,820</td>
<td align="right">64,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">64,820</td>
<td align="right">64,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">63,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">50,160</td>
<td align="right">50,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">47,760</td>
<td align="right">47,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">39,560</td>
<td align="right">39,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">39,420</td>
<td align="right">39,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,740</td>
<td align="right">36,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">36,280</td>
<td align="right">36,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">35,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">35,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">34,020</td>
<td align="right">34,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">32,600</td>
<td align="right">32,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">22,720</td>
<td align="right">22,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">22,720</td>
<td align="right">22,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">16,360</td>
<td align="right">16,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">16,300</td>
<td align="right">16,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">16,080</td>
<td align="right">16,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,420</td>
<td align="right">13,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">4,200</td>
<td align="right">4,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">460</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">460</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">9,187,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right"></td>
<td align="right">4,124,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">2,264,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">32,720</td>
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
<td align="right">1,200</td>
<td align="right">1,200</td>
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
Stats gathered on: 2024-12-12
