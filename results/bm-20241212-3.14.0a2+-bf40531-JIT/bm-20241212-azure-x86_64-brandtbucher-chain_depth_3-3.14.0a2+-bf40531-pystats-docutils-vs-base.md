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
<td align="left">COPY</td>
<td align="right">17,706,060</td>
<td align="right">13,305,780</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">7,861,120</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,491,260</td>
<td align="right">16,931,400</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,268,420</td>
<td align="right">7,209,760</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,533,540</td>
<td align="right">3,141,280</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,944,720</td>
<td align="right">3,519,840</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">17,852,480</td>
<td align="right">16,158,520</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">105,173,660</td>
<td align="right">113,578,140</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,340,720</td>
<td align="right">52,296,760</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">34,923,820</td>
<td align="right">37,429,860</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">93,026,280</td>
<td align="right">88,105,720</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,839,720</td>
<td align="right">4,612,820</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,324,560</td>
<td align="right">25,166,220</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,005,860</td>
<td align="right">22,954,440</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">45,857,780</td>
<td align="right">47,839,940</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">44,056,560</td>
<td align="right">45,890,020</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">173,113,760</td>
<td align="right">166,081,380</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,573,100</td>
<td align="right">37,294,400</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">303,380,780</td>
<td align="right">293,826,900</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">314,603,820</td>
<td align="right">305,585,580</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,734,820</td>
<td align="right">5,576,860</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,124,540</td>
<td align="right">34,017,920</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">195,636,800</td>
<td align="right">190,392,520</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">119,386,680</td>
<td align="right">116,586,720</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,360,680</td>
<td align="right">49,474,180</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">77,650,480</td>
<td align="right">79,394,220</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">10,034,400</td>
<td align="right">9,816,560</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">7,938,940</td>
<td align="right">7,788,780</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,255,940</td>
<td align="right">15,953,080</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,594,320</td>
<td align="right">29,103,020</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">62,869,860</td>
<td align="right">63,987,960</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">44,322,200</td>
<td align="right">43,559,460</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">37,474,220</td>
<td align="right">36,849,600</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">148,702,400</td>
<td align="right">150,984,900</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">24,990,900</td>
<td align="right">24,621,020</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">197,883,620</td>
<td align="right">200,755,220</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,205,520</td>
<td align="right">1,190,220</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,372,081,240</td>
<td align="right">1,355,940,000</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">76,303,980</td>
<td align="right">75,457,580</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">223,302,620</td>
<td align="right">220,921,180</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,826,540</td>
<td align="right">20,624,500</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">39,377,100</td>
<td align="right">39,743,780</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,735,800</td>
<td align="right">102,494,140</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">122,717,420</td>
<td align="right">121,829,280</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,836,320</td>
<td align="right">77,299,380</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,016,520</td>
<td align="right">17,916,840</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,585,540</td>
<td align="right">10,529,000</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,760,100</td>
<td align="right">2,773,920</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,452,140</td>
<td align="right">10,502,460</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,898,840</td>
<td align="right">9,853,000</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,560,640</td>
<td align="right">51,339,100</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">325,221,160</td>
<td align="right">326,582,940</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,005,500</td>
<td align="right">12,045,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,806,820</td>
<td align="right">8,778,260</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">207,729,900</td>
<td align="right">208,403,540</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">234,015,320</td>
<td align="right">233,289,860</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">307,607,740</td>
<td align="right">308,049,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">294,453,160</td>
<td align="right">294,799,620</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">68,748,500</td>
<td align="right">68,670,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,358,660</td>
<td align="right">19,375,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,706,540</td>
<td align="right">15,716,480</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,227,540</td>
<td align="right">5,230,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">55,677,280</td>
<td align="right">55,645,580</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,298,480</td>
<td align="right">49,318,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,924,980</td>
<td align="right">1,925,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,744,980</td>
<td align="right">39,755,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">66,691,800</td>
<td align="right">66,707,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,072,980</td>
<td align="right">30,080,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,074,360</td>
<td align="right">30,081,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">19,311,060</td>
<td align="right">19,313,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">122,727,460</td>
<td align="right">122,743,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,563,460</td>
<td align="right">27,566,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,534,540</td>
<td align="right">38,537,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,803,020</td>
<td align="right">5,803,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,219,980</td>
<td align="right">3,220,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,440</td>
<td align="right">5,440,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,369,400</td>
<td align="right">13,369,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,475,120</td>
<td align="right">26,475,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,783,620</td>
<td align="right">10,783,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,944,460</td>
<td align="right">91,944,460</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,954,300</td>
<td align="right">17,954,300</td>
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
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">7,035,220</td>
<td align="right">7,035,220</td>
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
<td align="left">DICT_MERGE</td>
<td align="right">3,425,140</td>
<td align="right">3,425,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,874,000</td>
<td align="right">2,874,000</td>
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
<td align="right">10,783,740</td>
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
<td align="right">10,490,680</td>
<td align="right">9.8%</td>
<td align="right">0.5%</td>
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
<td align="right">93,971,640</td>
<td align="right">88.1%</td>
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
<td align="right">2,163,860</td>
<td align="right">2.0%</td>
<td align="right">2,163,860</td>
<td align="right">2.0%</td>
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
<td align="right">11,160</td>
<td align="right">21.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,400</td>
<td align="right">78.8%</td>
<td align="right">41,400</td>
<td align="right">78.8%</td>
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
<td align="right">1,740</td>
<td align="right">15.6%</td>
<td align="right">1,760</td>
<td align="right">15.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,820</td>
<td align="right">70.2%</td>
<td align="right">7,820</td>
<td align="right">70.1%</td>
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
<td align="right">17,641,900</td>
<td align="right">3.1%</td>
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
<td align="right">553,235,460</td>
<td align="right">96.9%</td>
<td align="right">553,202,960</td>
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
<td align="right">337,020</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">8,773,420</td>
<td align="right">13.9%</td>
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
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
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
<td align="right">4,720</td>
<td align="right">97.5%</td>
<td align="right">-0.4%</td>
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
<td align="left">str</td>
<td align="right">880</td>
<td align="right">18.6%</td>
<td align="right">860</td>
<td align="right">18.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,880</td>
<td align="right">39.7%</td>
<td align="right">1,880</td>
<td align="right">39.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,180</td>
<td align="right">24.9%</td>
<td align="right">1,180</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">800</td>
<td align="right">16.9%</td>
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
<td align="right">24,614,200</td>
<td align="right">13.5%</td>
<td align="right">-1.5%</td>
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
<td align="right">130,633,880</td>
<td align="right">71.8%</td>
<td align="right">1.1%</td>
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
<td align="right">26,574,100</td>
<td align="right">14.6%</td>
<td align="right">0.9%</td>
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
<td align="right">6,820</td>
<td align="right">1.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">496,680</td>
<td align="right">98.6%</td>
<td align="right">501,380</td>
<td align="right">98.7%</td>
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
<td align="left">ascii string</td>
<td align="right">600</td>
<td align="right">8.7%</td>
<td align="right">540</td>
<td align="right">7.9%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,460</td>
<td align="right">21.2%</td>
<td align="right">1,420</td>
<td align="right">20.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,020</td>
<td align="right">14.8%</td>
<td align="right">1,040</td>
<td align="right">15.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">35.9%</td>
<td align="right">2,480</td>
<td align="right">36.4%</td>
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
<td align="right">266,240,500</td>
<td align="right">26.0%</td>
<td align="right">-3.9%</td>
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
<td align="right">101,837,140</td>
<td align="right">9.9%</td>
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
<td align="right">659,000,820</td>
<td align="right">63.5%</td>
<td align="right">654,777,820</td>
<td align="right">64.0%</td>
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
<td align="left">Success</td>
<td align="right">5,865,280</td>
<td align="right">99.7%</td>
<td align="right">5,659,800</td>
<td align="right">99.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20,040</td>
<td align="right">0.3%</td>
<td align="right">20,220</td>
<td align="right">0.4%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">9,660</td>
<td align="right">48.2%</td>
<td align="right">9,920</td>
<td align="right">49.1%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,180</td>
<td align="right">25.8%</td>
<td align="right">5,100</td>
<td align="right">25.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">14.2%</td>
<td align="right">2,840</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">3.2%</td>
<td align="right">640</td>
<td align="right">3.2%</td>
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
<td align="right">278,052,460</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">16,919,300</td>
<td align="right">14.4%</td>
<td align="right">-17.4%</td>
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
<td align="right">39.9%</td>
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
<td align="right">45.7%</td>
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
<td align="right">12,580</td>
<td align="right">1.2%</td>
<td align="right">11,700</td>
<td align="right">1.1%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
<td align="right">1,017,800</td>
<td align="right">98.9%</td>
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
<td align="right">9,060</td>
<td align="right">77.4%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">16.2%</td>
<td align="right">2,040</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">2.9%</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">200</td>
<td align="right">1.7%</td>
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
<td align="right">8,379,300</td>
<td align="right">3.0%</td>
<td align="right">-17.0%</td>
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
<td align="right">3,419,740</td>
<td align="right">1.2%</td>
<td align="right">-9.5%</td>
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
<td align="right">269,564,840</td>
<td align="right">95.8%</td>
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
<td align="right">167,000</td>
<td align="right">46.6%</td>
<td align="right">99,240</td>
<td align="right">38.4%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">191,300</td>
<td align="right">53.4%</td>
<td align="right">158,940</td>
<td align="right">61.6%</td>
<td align="right">-16.9%</td>
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
<td align="right">53,980</td>
<td align="right">54.4%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">41,540</td>
<td align="right">41.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">1,200</td>
<td align="right">1.2%</td>
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
<td align="right">375,189,820</td>
<td align="right">5.4%</td>
<td align="right">-3.2%</td>
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
<td align="right">205,218,420</td>
<td align="right">3.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">2,599,391,120</td>
<td align="right">37.4%</td>
<td align="right">-0.7%</td>
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
<td align="right">3,769,100,680</td>
<td align="right">54.2%</td>
<td align="right">-0.6%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">20,478,280</td>
<td align="right">9.9%</td>
<td align="right">16,919,300</td>
<td align="right">8.3%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,776,840</td>
<td align="right">1.8%</td>
<td align="right">3,419,740</td>
<td align="right">1.7%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">24,984,000</td>
<td align="right">12.0%</td>
<td align="right">24,614,200</td>
<td align="right">12.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,078,980</td>
<td align="right">48.6%</td>
<td align="right">101,837,140</td>
<td align="right">49.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,440,380</td>
<td align="right">5.0%</td>
<td align="right">10,490,680</td>
<td align="right">5.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,801,960</td>
<td align="right">4.2%</td>
<td align="right">8,773,420</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,783,620</td>
<td align="right">5.2%</td>
<td align="right">10,783,740</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,036,720</td>
<td align="right">10.1%</td>
<td align="right">21,036,720</td>
<td align="right">10.3%</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">2.0%</td>
<td align="right">6,246,340</td>
<td align="right">1.7%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">102,868,700</td>
<td align="right">26.5%</td>
<td align="right">96,155,840</td>
<td align="right">25.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">82,567,200</td>
<td align="right">21.3%</td>
<td align="right">78,831,560</td>
<td align="right">21.0%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,538,240</td>
<td align="right">8.1%</td>
<td align="right">32,608,580</td>
<td align="right">8.7%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,162,480</td>
<td align="right">3.4%</td>
<td align="right">13,287,120</td>
<td align="right">3.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,162,680</td>
<td align="right">3.4%</td>
<td align="right">13,286,980</td>
<td align="right">3.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,573,760</td>
<td align="right">2.5%</td>
<td align="right">9,589,680</td>
<td align="right">2.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">49,832,920</td>
<td align="right">12.9%</td>
<td align="right">49,799,880</td>
<td align="right">13.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">13.9%</td>
<td align="right">53,912,180</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,507,320</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4,476,820</td>
<td align="right">1.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">7,132,280</td>
<td align="right">2.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,304,200</td>
<td align="right">11.1%</td>
<td align="right">38,025,500</td>
<td align="right">10.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,307,680</td>
<td align="right">11.1%</td>
<td align="right">38,028,980</td>
<td align="right">10.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,615,540</td>
<td align="right">11.2%</td>
<td align="right">38,336,840</td>
<td align="right">10.8%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,615,540</td>
<td align="right">11.2%</td>
<td align="right">38,336,840</td>
<td align="right">10.8%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,780,820</td>
<td align="right">88.8%</td>
<td align="right">316,059,520</td>
<td align="right">89.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,586,940</td>
<td align="right">88.5%</td>
<td align="right">313,571,640</td>
<td align="right">88.5%</td>
<td align="right">-0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,630,860</td>
<td align="right">3.8%</td>
<td align="right">13,630,860</td>
<td align="right">3.8%</td>
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
<td align="right">2,259,544</td>
<td align="right"></td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">32,866,044</td>
<td align="right"></td>
<td align="right">36,206,626</td>
<td align="right"></td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">31,937,641</td>
<td align="right"></td>
<td align="right">34,708,538</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,710,719,324</td>
<td align="right">33.4%</td>
<td align="right">2,755,449,965</td>
<td align="right">33.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,915,579,820</td>
<td align="right">35.9%</td>
<td align="right">2,880,910,960</td>
<td align="right">35.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,692,403,473</td>
<td align="right">18.8%</td>
<td align="right">1,710,355,396</td>
<td align="right">19.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,486,626,055</td>
<td align="right">27.6%</td>
<td align="right">2,509,670,858</td>
<td align="right">27.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">710,702,360</td>
<td align="right">8.8%</td>
<td align="right">714,997,040</td>
<td align="right">8.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,729,626,980</td>
<td align="right">41.5%</td>
<td align="right">3,716,824,920</td>
<td align="right">41.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">197,576,311</td>
<td align="right"></td>
<td align="right">198,196,636</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">499,780</td>
<td align="right">0.1%</td>
<td align="right">498,820</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,784,865,460</td>
<td align="right">22.0%</td>
<td align="right">1,787,700,464</td>
<td align="right">22.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">459,808,179</td>
<td align="right"></td>
<td align="right">459,596,822</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,087,398,660</td>
<td align="right">12.1%</td>
<td align="right">1,087,897,280</td>
<td align="right">12.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,318,220</td>
<td align="right"></td>
<td align="right">236,368,740</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,323,500</td>
<td align="right">35.1%</td>
<td align="right">236,370,040</td>
<td align="right">35.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">437,701,320</td>
<td align="right">64.9%</td>
<td align="right">437,669,240</td>
<td align="right">64.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">436,857,020</td>
<td align="right">64.8%</td>
<td align="right">436,825,880</td>
<td align="right">64.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">473,817,378</td>
<td align="right"></td>
<td align="right">473,849,800</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,520</td>
<td align="right">0.1%</td>
<td align="right">344,540</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">26,140</td>
<td align="right">73,028,960</td>
<td align="right">1,154,912,947</td>
<td align="right">44,971,980</td>
<td align="right">99,386,580</td>
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
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">33.3%</td>
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
<td align="right">12,680</td>
<td align="right">36.8%</td>
<td align="right">17.4%</td>
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
<td align="right">1,800</td>
<td align="right">5.2%</td>
<td align="right">-10.9%</td>
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
<td align="right">13,920</td>
<td align="right">40.3%</td>
<td align="right">6.1%</td>
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
<td align="right">320</td>
<td align="right">0.9%</td>
<td align="right">-5.9%</td>
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
<td align="right">34,500</td>
<td align="right"></td>
<td align="right">5.8%</td>
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
<td align="right">4,156,385,640</td>
<td align="right">1,252.2%</td>
<td align="right">3.3%</td>
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
<td align="right">21,620</td>
<td align="right">62.7%</td>
<td align="right">0.1%</td>
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
<td align="right">331,917,540</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">14,800</td>
<td align="right">68.5%</td>
<td align="right">-4.9%</td>
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
<td align="right">21,620</td>
<td align="right"></td>
<td align="right">0.1%</td>
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
<td align="right">1,260</td>
<td align="right">5.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,840</td>
<td align="right">8.5%</td>
<td align="right">1,980</td>
<td align="right">9.2%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,300</td>
<td align="right">33.8%</td>
<td align="right">6,620</td>
<td align="right">30.6%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,040</td>
<td align="right">23.3%</td>
<td align="right">4,800</td>
<td align="right">22.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,480</td>
<td align="right">16.1%</td>
<td align="right">4,100</td>
<td align="right">19.0%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">12.0%</td>
<td align="right">2,600</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">20.0%</td>
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
<td align="right">2,240</td>
<td align="right">10.4%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,380</td>
<td align="right">15.6%</td>
<td align="right">3,080</td>
<td align="right">14.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,080</td>
<td align="right">32.8%</td>
<td align="right">6,860</td>
<td align="right">31.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,020</td>
<td align="right">9.4%</td>
<td align="right">1,800</td>
<td align="right">8.3%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">780</td>
<td align="right">3.6%</td>
<td align="right">580</td>
<td align="right">2.7%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.3%</td>
<td align="right">200.0%</td>
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
<td align="left">_TO_BOOL</td>
<td align="right">2,660</td>
<td align="right">1,323,080</td>
<td align="right">49,639.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,431,600</td>
<td align="right">5,831,880</td>
<td align="right">307.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,613,780</td>
<td align="right">5,172,760</td>
<td align="right">220.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">100,220</td>
<td align="right">185.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">100,220</td>
<td align="right">185.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,514,720</td>
<td align="right">12,755,380</td>
<td align="right">182.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,862,340</td>
<td align="right">5,182,840</td>
<td align="right">178.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">66,000</td>
<td align="right">15,700</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">303,080</td>
<td align="right">526,860</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">3,760,940</td>
<td align="right">6,191,740</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">4,200</td>
<td align="right">1,600</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">2,073,520</td>
<td align="right">896,620</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">840</td>
<td align="right">400</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">840</td>
<td align="right">400</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">420</td>
<td align="right">200</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">420</td>
<td align="right">200</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">420</td>
<td align="right">200</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">420</td>
<td align="right">200</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">9,448,440</td>
<td align="right">14,371,820</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">460</td>
<td align="right">240</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">460</td>
<td align="right">240</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,170,320</td>
<td align="right">1,179,400</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,492,920</td>
<td align="right">3,510,960</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">6,022,780</td>
<td align="right">3,937,720</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">21,158,080</td>
<td align="right">28,262,500</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">22,255,280</td>
<td align="right">29,358,180</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">22,035,940</td>
<td align="right">28,263,860</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">49,003,640</td>
<td align="right">62,851,120</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">36,280</td>
<td align="right">26,120</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">25,622,320</td>
<td align="right">19,049,300</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">27,782,680</td>
<td align="right">34,612,800</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">33,733,560</td>
<td align="right">25,761,080</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,882,380</td>
<td align="right">3,764,280</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">31,136,700</td>
<td align="right">37,943,040</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">42,770,440</td>
<td align="right">51,664,080</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,331,000</td>
<td align="right">3,437,620</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,400,420</td>
<td align="right">22,182,820</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">47,040,600</td>
<td align="right">37,551,300</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,366,420</td>
<td align="right">1,909,000</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">70,160</td>
<td align="right">56,640</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">28,295,220</td>
<td align="right">33,534,440</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,086,300</td>
<td align="right">1,719,620</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">87,457,040</td>
<td align="right">101,307,220</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,834,600</td>
<td align="right">13,703,180</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">106,620</td>
<td align="right">90,040</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,383,060</td>
<td align="right">10,696,480</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">38,947,980</td>
<td align="right">44,143,920</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">19,493,520</td>
<td align="right">17,211,020</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,356,700</td>
<td align="right">22,572,860</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">9,760,000</td>
<td align="right">10,818,660</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">10,011,620</td>
<td align="right">11,063,040</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">10,011,620</td>
<td align="right">11,063,040</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">10,004,300</td>
<td align="right">11,046,820</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">16,890,020</td>
<td align="right">15,146,280</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">44,820,560</td>
<td align="right">49,402,320</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">10,564,800</td>
<td align="right">11,623,200</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">10,615,240</td>
<td align="right">11,673,340</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">7,817,320</td>
<td align="right">8,588,900</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">21,538,660</td>
<td align="right">23,640,880</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">899,780</td>
<td align="right">982,880</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">899,780</td>
<td align="right">982,880</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">347,947,500</td>
<td align="right">379,847,500</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,343,040</td>
<td align="right">3,648,840</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">34,579,080</td>
<td align="right">31,636,960</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">14,657,960</td>
<td align="right">15,871,600</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,246,160</td>
<td align="right">3,464,560</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,274,440</td>
<td align="right">3,476,480</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">304,285,880</td>
<td align="right">322,455,320</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">22,955,220</td>
<td align="right">21,619,720</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,013,700</td>
<td align="right">4,231,540</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,182,680</td>
<td align="right">26,656,300</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">134,920</td>
<td align="right">127,840</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">134,920</td>
<td align="right">127,840</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">36,007,660</td>
<td align="right">34,123,040</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">12,894,940</td>
<td align="right">13,519,560</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">16,292,980</td>
<td align="right">17,055,720</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">36,436,180</td>
<td align="right">38,130,140</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,605,680</td>
<td align="right">2,713,040</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,129,500</td>
<td align="right">12,620,800</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">16,276,080</td>
<td align="right">15,645,720</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">24,801,540</td>
<td align="right">25,689,580</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">33,938,160</td>
<td align="right">32,797,840</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">35,975,340</td>
<td align="right">37,100,580</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">14,385,240</td>
<td align="right">14,825,780</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,302,940</td>
<td align="right">8,554,540</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">82,540,680</td>
<td align="right">80,130,680</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">13,948,420</td>
<td align="right">14,340,680</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,164,380</td>
<td align="right">2,220,920</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">12,559,400</td>
<td align="right">12,871,740</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">242,734,840</td>
<td align="right">238,188,860</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,244,580</td>
<td align="right">2,284,760</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">32,397,780</td>
<td align="right">31,912,860</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,223,080</td>
<td align="right">11,381,040</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">63,494,940</td>
<td align="right">62,648,800</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,274,160</td>
<td align="right">12,424,320</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,340,220</td>
<td align="right">3,300,480</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">14,931,800</td>
<td align="right">15,088,100</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,728,540</td>
<td align="right">14,882,580</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">98,921,880</td>
<td align="right">99,949,280</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,062,120</td>
<td align="right">37,708,980</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">324,890,620</td>
<td align="right">322,076,760</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,391,240</td>
<td align="right">3,419,780</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,143,800</td>
<td align="right">12,243,480</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,454,180</td>
<td align="right">1,444,240</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,589,560</td>
<td align="right">2,573,200</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">69,777,840</td>
<td align="right">70,201,760</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,954,840</td>
<td align="right">1,944,580</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">88,323,040</td>
<td align="right">88,782,460</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">58,991,800</td>
<td align="right">59,265,780</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">651,440</td>
<td align="right">648,840</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">193,264,600</td>
<td align="right">193,994,240</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">44,391,880</td>
<td align="right">44,256,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">44,391,880</td>
<td align="right">44,256,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">367,970,360</td>
<td align="right">369,018,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,820,420</td>
<td align="right">9,800,440</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,082,720</td>
<td align="right">2,080,080</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,977,220</td>
<td align="right">2,974,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,183,560</td>
<td align="right">1,184,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">988,320</td>
<td align="right">988,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">362,720</td>
<td align="right">362,500</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">931,120</td>
<td align="right">930,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,784,320</td>
<td align="right">1,783,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,568,280</td>
<td align="right">1,567,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">331,995,020</td>
<td align="right">331,917,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,249,880</td>
<td align="right">1,249,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,968,860</td>
<td align="right">3,968,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,315,200</td>
<td align="right">1,315,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">814,660</td>
<td align="right">814,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,781,900</td>
<td align="right">4,781,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,231,580</td>
<td align="right">2,231,580</td>
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
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,329,020</td>
<td align="right">1,329,020</td>
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
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">1,735,820</td>
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
Stats gathered on: 2024-12-13
