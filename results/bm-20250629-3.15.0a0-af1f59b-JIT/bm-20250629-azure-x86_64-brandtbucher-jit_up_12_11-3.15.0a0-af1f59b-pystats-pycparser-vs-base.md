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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">657,220</td>
<td align="right">1,312,400</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">801,200</td>
<td align="right">1,415,400</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,485,340</td>
<td align="right">4,180,960</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,050,840</td>
<td align="right">2,706,180</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">11,779,360</td>
<td align="right">14,892,240</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,607,860</td>
<td align="right">3,295,900</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,972,420</td>
<td align="right">7,527,680</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">327,380</td>
<td align="right">245,460</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">13,416,560</td>
<td align="right">16,529,560</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,561,940</td>
<td align="right">1,213,920</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,798,340</td>
<td align="right">1,411,800</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">22,982,480</td>
<td align="right">18,070,760</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,399,640</td>
<td align="right">18,487,920</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,054,920</td>
<td align="right">2,451,960</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">26,957,640</td>
<td align="right">22,045,920</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,225,460</td>
<td align="right">8,514,620</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">8,107,100</td>
<td align="right">9,455,240</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">95,601,620</td>
<td align="right">80,827,060</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">28,197,520</td>
<td align="right">23,849,860</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,191,280</td>
<td align="right">24,061,180</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">28,464,400</td>
<td align="right">32,530,320</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">19,860,100</td>
<td align="right">22,287,240</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">46,871,740</td>
<td align="right">52,512,400</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,455,680</td>
<td align="right">2,718,640</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,702,100</td>
<td align="right">1,876,580</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">49,139,100</td>
<td align="right">44,227,380</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">49,147,120</td>
<td align="right">44,235,400</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">38,690,520</td>
<td align="right">42,415,460</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">38,933,900</td>
<td align="right">42,495,160</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,746,240</td>
<td align="right">12,815,800</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">27,627,480</td>
<td align="right">30,054,620</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,658,980</td>
<td align="right">4,254,120</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,285,720</td>
<td align="right">2,483,840</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">45,097,980</td>
<td align="right">41,512,720</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,852,920</td>
<td align="right">3,051,100</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">163,398,940</td>
<td align="right">152,395,420</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">90,500,520</td>
<td align="right">96,211,200</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">19,821,960</td>
<td align="right">21,037,480</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">110,155,200</td>
<td align="right">116,376,220</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">35,906,180</td>
<td align="right">33,881,400</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">758,700</td>
<td align="right">717,740</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">225,673,640</td>
<td align="right">213,500,520</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">247,022,620</td>
<td align="right">233,825,880</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">35,250,500</td>
<td align="right">33,451,660</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">252,898,060</td>
<td align="right">240,606,480</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,129,520</td>
<td align="right">6,818,840</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,411,488,540</td>
<td align="right">1,354,251,320</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,869,360</td>
<td align="right">21,524,520</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">106,474,480</td>
<td align="right">103,160,540</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,782,480</td>
<td align="right">2,700,580</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">40,063,160</td>
<td align="right">41,212,700</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">246,005,020</td>
<td align="right">239,087,400</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">79,120,200</td>
<td align="right">81,288,200</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">11,580,820</td>
<td align="right">11,309,500</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">92,132,660</td>
<td align="right">90,260,720</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">64,257,640</td>
<td align="right">65,464,560</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">142,422,180</td>
<td align="right">144,779,100</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">182,614,360</td>
<td align="right">180,218,500</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,210,260</td>
<td align="right">1,195,880</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,281,880</td>
<td align="right">11,197,000</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">35,365,100</td>
<td align="right">35,100,560</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,465,640</td>
<td align="right">6,424,680</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">47,641,420</td>
<td align="right">47,439,620</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,327,560</td>
<td align="right">39,166,720</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">57,405,240</td>
<td align="right">57,605,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">7,973,180</td>
<td align="right">7,958,800</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,330,260</td>
<td align="right">9,316,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,644,400</td>
<td align="right">2,641,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">107,855,120</td>
<td align="right">107,889,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,703,740</td>
<td align="right">16,700,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">162,870,320</td>
<td align="right">162,850,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">52,631,660</td>
<td align="right">52,625,740</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">41,951,060</td>
<td align="right">41,951,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">35,531,200</td>
<td align="right">35,531,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,896,720</td>
<td align="right">28,896,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,834,260</td>
<td align="right">26,834,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,361,920</td>
<td align="right">12,361,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,044,940</td>
<td align="right">8,044,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,154,860</td>
<td align="right">4,154,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">4,022,760</td>
<td align="right">4,022,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">4,022,620</td>
<td align="right">4,022,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,092,160</td>
<td align="right">1,092,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,091,940</td>
<td align="right">1,091,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">854,940</td>
<td align="right">854,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">835,500</td>
<td align="right">835,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">753,780</td>
<td align="right">753,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">675,160</td>
<td align="right">675,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">514,700</td>
<td align="right">514,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">418,760</td>
<td align="right">418,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">266,500</td>
<td align="right">266,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">244,060</td>
<td align="right">244,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">182,240</td>
<td align="right">182,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">118,100</td>
<td align="right">118,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">109,640</td>
<td align="right">109,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">98,760</td>
<td align="right">98,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">72,920</td>
<td align="right">72,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">56,220</td>
<td align="right">56,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,940</td>
<td align="right">51,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">50,260</td>
<td align="right">50,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,200</td>
<td align="right">39,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">37,500</td>
<td align="right">37,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">32,940</td>
<td align="right">32,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,760</td>
<td align="right">31,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,520</td>
<td align="right">30,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">28,800</td>
<td align="right">28,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">16,740</td>
<td align="right">16,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">15,620</td>
<td align="right">15,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15,500</td>
<td align="right">15,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,660</td>
<td align="right">14,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">14,100</td>
<td align="right">14,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,820</td>
<td align="right">12,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,800</td>
<td align="right">10,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10,720</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,560</td>
<td align="right">8,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,560</td>
<td align="right">5,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">4,160</td>
<td align="right">4,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,960</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,400</td>
<td align="right">3,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,620</td>
<td align="right">2,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2,160</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,800</td>
<td align="right">1,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,080</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">680</td>
<td align="right">680</td>
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
<td align="left">IMPORT_NAME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
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
<td align="left">STORE_DEREF</td>
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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
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
<td align="right">28,879,160</td>
<td align="right">6.5%</td>
<td align="right">28,879,160</td>
<td align="right">6.5%</td>
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
<td align="right">416,338,580</td>
<td align="right">93.5%</td>
<td align="right">416,338,580</td>
<td align="right">93.5%</td>
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
<td align="right">13,440</td>
<td align="right">0.0%</td>
<td align="right">13,440</td>
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
<td align="right">7,260</td>
<td align="right">40.8%</td>
<td align="right">7,260</td>
<td align="right">40.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">10,540</td>
<td align="right">59.2%</td>
<td align="right">10,540</td>
<td align="right">59.2%</td>
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
<td align="left">out of range</td>
<td align="right">8,480</td>
<td align="right">80.5%</td>
<td align="right">8,480</td>
<td align="right">80.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">780</td>
<td align="right">7.4%</td>
<td align="right">780</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">560</td>
<td align="right">5.3%</td>
<td align="right">560</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">400</td>
<td align="right">3.8%</td>
<td align="right">400</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
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
<td align="right">23,399,640</td>
<td align="right">100.0%</td>
<td align="right">18,487,920</td>
<td align="right">100.0%</td>
<td align="right">-21.0%</td>
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
<td align="right">28,854,320</td>
<td align="right">9.3%</td>
<td align="right">29,285,920</td>
<td align="right">9.4%</td>
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
<td align="right">28,317,700</td>
<td align="right">9.1%</td>
<td align="right">28,741,160</td>
<td align="right">9.2%</td>
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
<td align="right">283,011,620</td>
<td align="right">90.7%</td>
<td align="right">282,386,520</td>
<td align="right">90.6%</td>
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
<td align="right">552,120</td>
<td align="right">100.0%</td>
<td align="right">560,260</td>
<td align="right">100.0%</td>
<td align="right">1.5%</td>
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
<td align="right">1,000</td>
<td align="right">100.0%</td>
<td align="right">1,000</td>
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
<td align="right">417,080</td>
<td align="right">0.3%</td>
<td align="right">417,080</td>
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
<td align="right">131,166,160</td>
<td align="right">99.7%</td>
<td align="right">131,166,160</td>
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
<td align="right">1,240</td>
<td align="right">72.9%</td>
<td align="right">1,240</td>
<td align="right">72.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">460</td>
<td align="right">27.1%</td>
<td align="right">460</td>
<td align="right">27.1%</td>
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
<td align="right">320</td>
<td align="right">69.6%</td>
<td align="right">320</td>
<td align="right">69.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">100</td>
<td align="right">21.7%</td>
<td align="right">100</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
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
<td align="right">2,048,440</td>
<td align="right">5.5%</td>
<td align="right">2,703,620</td>
<td align="right">7.2%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,983,260</td>
<td align="right">94.5%</td>
<td align="right">34,983,260</td>
<td align="right">92.8%</td>
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
<td align="right">2,240</td>
<td align="right">93.3%</td>
<td align="right">2,400</td>
<td align="right">93.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">6.7%</td>
<td align="right">160</td>
<td align="right">6.2%</td>
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
<td align="right">620</td>
<td align="right">27.7%</td>
<td align="right">780</td>
<td align="right">32.5%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">920</td>
<td align="right">41.1%</td>
<td align="right">920</td>
<td align="right">38.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">700</td>
<td align="right">31.2%</td>
<td align="right">700</td>
<td align="right">29.2%</td>
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
<td align="right">3,138,000</td>
<td align="right">52.4%</td>
<td align="right">2,535,040</td>
<td align="right">45.4%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,849,440</td>
<td align="right">47.6%</td>
<td align="right">3,047,560</td>
<td align="right">54.5%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">620</td>
<td align="right">0.0%</td>
<td align="right">620</td>
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
<td align="right">3,000</td>
<td align="right">85.7%</td>
<td align="right">3,060</td>
<td align="right">86.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">14.3%</td>
<td align="right">500</td>
<td align="right">14.0%</td>
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
<td align="left">reversed list</td>
<td align="right">680</td>
<td align="right">22.7%</td>
<td align="right">740</td>
<td align="right">24.2%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">820</td>
<td align="right">27.3%</td>
<td align="right">820</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">400</td>
<td align="right">13.3%</td>
<td align="right">400</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">300</td>
<td align="right">10.0%</td>
<td align="right">300</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">260</td>
<td align="right">8.7%</td>
<td align="right">260</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">200</td>
<td align="right">6.7%</td>
<td align="right">200</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">180</td>
<td align="right">6.0%</td>
<td align="right">180</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">160</td>
<td align="right">5.3%</td>
<td align="right">160</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
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
<td align="right">11,609,600</td>
<td align="right">11,609,600 / 0 !!</td>
<td align="right">11,609,600</td>
<td align="right">11,609,600 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">2,213,780</td>
<td align="right">2,213,780 / 0 !!</td>
<td align="right">2,213,780</td>
<td align="right">2,213,780 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">405,560</td>
<td align="right">405,560 / 0 !!</td>
<td align="right">405,560</td>
<td align="right">405,560 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,060</td>
<td align="right">21,060 / 0 !!</td>
<td align="right">21,060</td>
<td align="right">21,060 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">14,800</td>
<td align="right">14,800 / 0 !!</td>
<td align="right">14,800</td>
<td align="right">14,800 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">13,860</td>
<td align="right">13,860 / 0 !!</td>
<td align="right">13,860</td>
<td align="right">13,860 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">520</td>
<td align="right">520 / 0 !!</td>
<td align="right">520</td>
<td align="right">520 / 0 !!</td>
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
<td align="right">38,901,740</td>
<td align="right">7.0%</td>
<td align="right">42,462,100</td>
<td align="right">7.5%</td>
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
<td align="right">10,391,580</td>
<td align="right">1.9%</td>
<td align="right">10,310,980</td>
<td align="right">1.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">507,443,980</td>
<td align="right">91.1%</td>
<td align="right">509,958,720</td>
<td align="right">90.6%</td>
<td align="right">0.5%</td>
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
<td align="right">22,480</td>
<td align="right">9.9%</td>
<td align="right">23,380</td>
<td align="right">10.3%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">205,280</td>
<td align="right">90.1%</td>
<td align="right">203,800</td>
<td align="right">89.7%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,660</td>
<td align="right">7.4%</td>
<td align="right">2,060</td>
<td align="right">8.8%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">660</td>
<td align="right">2.9%</td>
<td align="right">660</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">360</td>
<td align="right">1.6%</td>
<td align="right">360</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">300</td>
<td align="right">1.3%</td>
<td align="right">300</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">153,586,800</td>
<td align="right">100.0%</td>
<td align="right">149,379,100</td>
<td align="right">100.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,340</td>
<td align="right">0.0%</td>
<td align="right">5,340</td>
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
<td align="right">22,880</td>
<td align="right">0.0%</td>
<td align="right">22,880</td>
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
<td align="right">5,740</td>
<td align="right">100.0%</td>
<td align="right">5,740</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">239,860</td>
<td align="right">0.1%</td>
<td align="right">219,720</td>
<td align="right">0.1%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">231,917,640</td>
<td align="right">96.6%</td>
<td align="right">231,937,400</td>
<td align="right">96.6%</td>
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
<td align="right">8,035,720</td>
<td align="right">3.3%</td>
<td align="right">8,035,720</td>
<td align="right">3.3%</td>
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
<td align="right">10,200</td>
<td align="right">74.5%</td>
<td align="right">9,820</td>
<td align="right">73.7%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,500</td>
<td align="right">25.5%</td>
<td align="right">3,500</td>
<td align="right">26.3%</td>
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
<td align="right">19,420</td>
<td align="right">554.9%</td>
<td align="right">19,920</td>
<td align="right">569.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,380</td>
<td align="right">96.6%</td>
<td align="right">3,380</td>
<td align="right">96.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">120</td>
<td align="right">3.4%</td>
<td align="right">120</td>
<td align="right">3.4%</td>
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
<td align="right">26,807,080</td>
<td align="right">49.9%</td>
<td align="right">26,807,080</td>
<td align="right">49.9%</td>
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
<td align="right">26,849,420</td>
<td align="right">50.0%</td>
<td align="right">26,849,420</td>
<td align="right">50.0%</td>
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
<td align="right">400</td>
<td align="right">1.5%</td>
<td align="right">400</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">26,780</td>
<td align="right">98.5%</td>
<td align="right">26,780</td>
<td align="right">98.5%</td>
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
<td align="right">26,720</td>
<td align="right">99.8%</td>
<td align="right">26,720</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">5,686,940</td>
<td align="right">4.3%</td>
<td align="right">6,623,200</td>
<td align="right">5.0%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,379,100</td>
<td align="right">1.8%</td>
<td align="right">2,624,200</td>
<td align="right">2.0%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">123,557,840</td>
<td align="right">93.8%</td>
<td align="right">123,393,620</td>
<td align="right">93.0%</td>
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
<td align="right">74,780</td>
<td align="right">40.7%</td>
<td align="right">92,620</td>
<td align="right">42.2%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">108,980</td>
<td align="right">59.3%</td>
<td align="right">126,640</td>
<td align="right">57.8%</td>
<td align="right">16.2%</td>
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
<td align="right">70,820</td>
<td align="right">94.7%</td>
<td align="right">88,660</td>
<td align="right">95.7%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,780</td>
<td align="right">3.7%</td>
<td align="right">2,780</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,060</td>
<td align="right">1.4%</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
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
<td align="right">37,167,660</td>
<td align="right">100.0%</td>
<td align="right">37,167,660</td>
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
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">340</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,142,889,140</td>
<td align="right">63.1%</td>
<td align="right">3,034,671,060</td>
<td align="right">62.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">45,212,040</td>
<td align="right">0.9%</td>
<td align="right">46,479,100</td>
<td align="right">1.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,650,958,940</td>
<td align="right">33.2%</td>
<td align="right">1,638,965,340</td>
<td align="right">33.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">138,575,540</td>
<td align="right">2.8%</td>
<td align="right">137,936,700</td>
<td align="right">2.8%</td>
<td align="right">-0.5%</td>
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
<td align="right">2,048,440</td>
<td align="right">1.3%</td>
<td align="right">2,703,620</td>
<td align="right">1.7%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,399,640</td>
<td align="right">14.4%</td>
<td align="right">18,487,920</td>
<td align="right">11.4%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,379,100</td>
<td align="right">1.5%</td>
<td align="right">2,624,200</td>
<td align="right">1.6%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">38,901,740</td>
<td align="right">24.0%</td>
<td align="right">42,462,100</td>
<td align="right">26.2%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,849,440</td>
<td align="right">1.8%</td>
<td align="right">3,047,560</td>
<td align="right">1.9%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">28,317,700</td>
<td align="right">17.5%</td>
<td align="right">28,741,160</td>
<td align="right">17.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,879,160</td>
<td align="right">17.8%</td>
<td align="right">28,879,160</td>
<td align="right">17.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,807,080</td>
<td align="right">16.5%</td>
<td align="right">26,807,080</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,035,720</td>
<td align="right">5.0%</td>
<td align="right">8,035,720</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">417,080</td>
<td align="right">0.3%</td>
<td align="right">417,080</td>
<td align="right">0.3%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,832,540</td>
<td align="right">8.5%</td>
<td align="right">4,617,400</td>
<td align="right">9.9%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">239,580</td>
<td align="right">0.5%</td>
<td align="right">219,440</td>
<td align="right">0.5%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,846,480</td>
<td align="right">4.1%</td>
<td align="right">1,997,880</td>
<td align="right">4.3%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,721,460</td>
<td align="right">3.8%</td>
<td align="right">1,640,860</td>
<td align="right">3.5%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,825,060</td>
<td align="right">32.8%</td>
<td align="right">15,053,720</td>
<td align="right">32.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">14,025,960</td>
<td align="right">31.0%</td>
<td align="right">14,228,900</td>
<td align="right">30.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,468,520</td>
<td align="right">18.7%</td>
<td align="right">8,468,520</td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">201,280</td>
<td align="right">0.4%</td>
<td align="right">201,280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">14,080</td>
<td align="right">0.0%</td>
<td align="right">14,080</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,900</td>
<td align="right">0.0%</td>
<td align="right">9,900</td>
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
<td align="right">41,960,820</td>
<td align="right">26.4%</td>
<td align="right">41,960,820</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">116,896,980</td>
<td align="right">73.6%</td>
<td align="right">116,896,980</td>
<td align="right">73.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">41,960,820</td>
<td align="right">26.4%</td>
<td align="right">41,960,820</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">41,960,420</td>
<td align="right">26.4%</td>
<td align="right">41,960,420</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">41,960,020</td>
<td align="right">26.4%</td>
<td align="right">41,960,020</td>
<td align="right">26.4%</td>
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
<td align="right">34,901,940</td>
<td align="right">22.0%</td>
<td align="right">34,901,940</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">73,940</td>
<td align="right">0.0%</td>
<td align="right">73,940</td>
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
<td align="right">20,160</td>
<td align="right">0.0%</td>
<td align="right">20,160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">162,880,020</td>
<td align="right">102.5%</td>
<td align="right">162,880,020</td>
<td align="right">102.5%</td>
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
<td align="left">Method cache misses</td>
<td align="right">317,400</td>
<td align="right"></td>
<td align="right">1,003,288</td>
<td align="right"></td>
<td align="right">216.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">526,246</td>
<td align="right"></td>
<td align="right">1,213,392</td>
<td align="right"></td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">206,092,460</td>
<td align="right">7.4%</td>
<td align="right">185,869,160</td>
<td align="right">6.6%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,051,580</td>
<td align="right">1.7%</td>
<td align="right">47,385,840</td>
<td align="right">1.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">728,122,127</td>
<td align="right">24.3%</td>
<td align="right">752,761,406</td>
<td align="right">25.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">639,850,231</td>
<td align="right">22.8%</td>
<td align="right">660,647,837</td>
<td align="right">23.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,444,480,340</td>
<td align="right">48.2%</td>
<td align="right">1,416,009,860</td>
<td align="right">47.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,260</td>
<td align="right">0.0%</td>
<td align="right">3,320</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">82,376,920</td>
<td align="right"></td>
<td align="right">81,591,252</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">221,200</td>
<td align="right"></td>
<td align="right">222,810</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">776,082,709</td>
<td align="right">25.9%</td>
<td align="right">780,322,410</td>
<td align="right">26.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,122,405,440</td>
<td align="right">40.1%</td>
<td align="right">1,116,493,800</td>
<td align="right">39.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">833,799,944</td>
<td align="right">29.8%</td>
<td align="right">835,880,425</td>
<td align="right">29.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">84,816,500</td>
<td align="right"></td>
<td align="right">84,814,890</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">134,172,200</td>
<td align="right">44.3%</td>
<td align="right">134,172,360</td>
<td align="right">44.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">168,498,200</td>
<td align="right">55.7%</td>
<td align="right">168,498,040</td>
<td align="right">55.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">168,520,200</td>
<td align="right"></td>
<td align="right">168,520,040</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">106,672,740</td>
<td align="right">35.2%</td>
<td align="right">106,672,820</td>
<td align="right">35.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">27,496,200</td>
<td align="right">9.1%</td>
<td align="right">27,496,220</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">157,338,583</td>
<td align="right"></td>
<td align="right">157,338,694</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">36,024,340</td>
<td align="right"></td>
<td align="right">36,024,340</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
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
<td align="right">6,700</td>
<td align="right">5,775,880</td>
<td align="right">202,854,970</td>
<td align="right">12,473,880</td>
<td align="right">18,717,880</td>
<td align="right">6,700</td>
<td align="right">5,775,880</td>
<td align="right">202,851,986</td>
<td align="right">12,473,180</td>
<td align="right">18,718,820</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">64,848,100</td>
<td align="right"></td>
<td align="right">51,740,420</td>
<td align="right"></td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">220</td>
<td align="right">16.4%</td>
<td align="right">260</td>
<td align="right">20.0%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,940</td>
<td align="right">20.8%</td>
<td align="right">2,040</td>
<td align="right">21.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,906,091,240</td>
<td align="right">6,023.4%</td>
<td align="right">4,082,644,860</td>
<td align="right">7,890.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">6,060</td>
<td align="right">64.9%</td>
<td align="right">6,300</td>
<td align="right">65.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">9,340</td>
<td align="right"></td>
<td align="right">9,660</td>
<td align="right"></td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,340</td>
<td align="right">14.3%</td>
<td align="right">1,300</td>
<td align="right">13.5%</td>
<td align="right">-3.0%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20 / 0 !!</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20 / 0 !!</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
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
<td align="right">440</td>
<td align="right">4.7%</td>
<td align="right">440</td>
<td align="right">4.6%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">960</td>
<td align="right">71.6%</td>
<td align="right">1,020</td>
<td align="right">78.5%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,340</td>
<td align="right"></td>
<td align="right">1,300</td>
<td align="right"></td>
<td align="right">-3.0%</td>
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

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">737,280</td>
<td align="right">4.3%</td>
<td align="right">81,920</td>
<td align="right">0.4%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">14,809,680</td>
<td align="right">85.7%</td>
<td align="right">19,185,220</td>
<td align="right">87.4%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">17,285,120</td>
<td align="right"></td>
<td align="right">21,954,560</td>
<td align="right"></td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">372,480</td>
<td align="right">2.2%</td>
<td align="right">467,680</td>
<td align="right">2.1%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,102,960</td>
<td align="right">12.2%</td>
<td align="right">2,301,660</td>
<td align="right">10.5%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">
Trampoline size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the trampolines of the JIT traces
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


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">260</td>
<td align="right">27.1%</td>
<td align="left">240</td>
<td align="right">23.5%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">120</td>
<td align="right">12.5%</td>
<td align="left">100</td>
<td align="right">9.8%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">200</td>
<td align="right">20.8%</td>
<td align="left">260</td>
<td align="right">25.5%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">180</td>
<td align="right">18.8%</td>
<td align="left">160</td>
<td align="right">15.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">200</td>
<td align="right">20.8%</td>
<td align="left">240</td>
<td align="right">23.5%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">20</td>
<td align="right">2.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

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
<td align="left"><= 8</td>
<td align="right">40</td>
<td align="right">3.0%</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">11.9%</td>
<td align="right">120</td>
<td align="right">9.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">60</td>
<td align="right">4.5%</td>
<td align="right">80</td>
<td align="right">6.2%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">280</td>
<td align="right">20.9%</td>
<td align="right">260</td>
<td align="right">20.0%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">13.4%</td>
<td align="right">160</td>
<td align="right">12.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">320</td>
<td align="right">23.9%</td>
<td align="right">300</td>
<td align="right">23.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">280</td>
<td align="right">20.9%</td>
<td align="right">320</td>
<td align="right">24.6%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">1.5%</td>
<td align="right">20</td>
<td align="right">1.5%</td>
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
<td align="left"><= 4</td>
<td align="right">20</td>
<td align="right">1.5%</td>
<td align="right">20</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">120</td>
<td align="right">9.0%</td>
<td align="right">80</td>
<td align="right">6.2%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">80</td>
<td align="right">6.0%</td>
<td align="right">100</td>
<td align="right">7.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">160</td>
<td align="right">11.9%</td>
<td align="right">140</td>
<td align="right">10.8%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">11.9%</td>
<td align="right">200</td>
<td align="right">15.4%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">13.4%</td>
<td align="right">180</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">240</td>
<td align="right">17.9%</td>
<td align="right">260</td>
<td align="right">20.0%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


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
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">3,209,980</td>
<td align="right">8,124,840</td>
<td align="right">153.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,209,980</td>
<td align="right">8,121,700</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">3,209,980</td>
<td align="right">8,121,700</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,209,980</td>
<td align="right">8,121,700</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3,209,980</td>
<td align="right">8,121,700</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">3,209,980</td>
<td align="right">8,121,700</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">9,691,340</td>
<td align="right">24,465,900</td>
<td align="right">152.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">15,760</td>
<td align="right">30,140</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">15,760</td>
<td align="right">30,140</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">15,760</td>
<td align="right">30,140</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">15,760</td>
<td align="right">30,140</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">15,760</td>
<td align="right">30,140</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">816,200</td>
<td align="right">128,160</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,346,480</td>
<td align="right">285,500</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">265,140</td>
<td align="right">67,020</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">6,401,920</td>
<td align="right">10,749,580</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">49,267,740</td>
<td align="right">74,439,480</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">6,920,400</td>
<td align="right">10,234,340</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">8,726,060</td>
<td align="right">12,744,160</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">10,107,480</td>
<td align="right">14,513,300</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">16,391,460</td>
<td align="right">23,410,200</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,505,680</td>
<td align="right">2,728,140</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">715,560</td>
<td align="right">979,720</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,066,300</td>
<td align="right">2,011,840</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">32,677,900</td>
<td align="right">43,681,420</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">32,677,900</td>
<td align="right">43,681,420</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">32,677,900</td>
<td align="right">43,681,420</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,779,560</td>
<td align="right">4,538,920</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">21,563,260</td>
<td align="right">28,685,220</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">124,020</td>
<td align="right">164,980</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,189,220</td>
<td align="right">24,162,200</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">231,115,040</td>
<td align="right">298,890,240</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">12,810,240</td>
<td align="right">9,249,880</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,761,500</td>
<td align="right">16,103,480</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">61,228,160</td>
<td align="right">75,650,580</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">927,900</td>
<td align="right">1,141,900</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">12,864,320</td>
<td align="right">10,157,380</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">64,848,100</td>
<td align="right">51,740,420</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">64,848,100</td>
<td align="right">51,740,420</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">41,039,040</td>
<td align="right">32,792,540</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">6,261,080</td>
<td align="right">5,054,160</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">6,261,080</td>
<td align="right">5,054,160</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">6,261,080</td>
<td align="right">5,054,160</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">8,896,080</td>
<td align="right">7,194,320</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">20,771,920</td>
<td align="right">17,046,980</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">44,209,440</td>
<td align="right">36,418,140</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">1,835,700</td>
<td align="right">2,144,900</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8,823,700</td>
<td align="right">7,425,960</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8,823,700</td>
<td align="right">7,425,960</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">82,765,000</td>
<td align="right">70,062,420</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">15,578,660</td>
<td align="right">13,233,440</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">8,365,800</td>
<td align="right">7,126,860</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">15,893,380</td>
<td align="right">13,562,340</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">16,429,920</td>
<td align="right">14,073,000</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">16,429,920</td>
<td align="right">14,073,000</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">16,429,920</td>
<td align="right">14,073,000</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">16,429,920</td>
<td align="right">14,073,000</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">23,153,640</td>
<td align="right">20,040,760</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">23,153,640</td>
<td align="right">20,040,760</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">16,247,940</td>
<td align="right">14,079,940</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">20,639,200</td>
<td align="right">18,349,800</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">43,840,900</td>
<td align="right">39,267,160</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">42,126,920</td>
<td align="right">37,876,000</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">68,728,080</td>
<td align="right">75,645,700</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,728,080</td>
<td align="right">75,645,700</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,612,540</td>
<td align="right">1,773,380</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">463,480</td>
<td align="right">507,400</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">926,960</td>
<td align="right">1,008,880</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">463,480</td>
<td align="right">504,440</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">463,480</td>
<td align="right">504,440</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">15,067,680</td>
<td align="right">13,757,360</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,533,840</td>
<td align="right">6,878,680</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">7,533,840</td>
<td align="right">6,878,680</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">7,533,840</td>
<td align="right">6,878,680</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">945,160</td>
<td align="right">1,027,060</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">481,740</td>
<td align="right">522,700</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">481,740</td>
<td align="right">522,700</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">481,740</td>
<td align="right">522,700</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">10,460,100</td>
<td align="right">9,606,820</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">51,491,960</td>
<td align="right">47,322,720</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">101,509,940</td>
<td align="right">93,409,120</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">521,580</td>
<td align="right">562,540</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,941,320</td>
<td align="right">15,615,560</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">32,764,860</td>
<td align="right">30,202,540</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">7,997,320</td>
<td align="right">7,383,120</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,997,320</td>
<td align="right">7,383,120</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">17,806,200</td>
<td align="right">16,462,980</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">10,793,020</td>
<td align="right">9,982,560</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">80,348,100</td>
<td align="right">74,752,500</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">685,957,420</td>
<td align="right">733,021,220</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">658,919,100</td>
<td align="right">703,139,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,105,780</td>
<td align="right">7,582,700</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">77,658,780</td>
<td align="right">72,653,920</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">36,709,840</td>
<td align="right">38,734,620</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">36,709,840</td>
<td align="right">38,734,620</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">50,458,480</td>
<td align="right">47,706,760</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">35,609,560</td>
<td align="right">37,481,500</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,444,940</td>
<td align="right">4,246,820</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,945,420</td>
<td align="right">8,293,440</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">115,884,760</td>
<td align="right">110,887,940</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">29,933,640</td>
<td align="right">28,644,480</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">29,933,640</td>
<td align="right">28,644,480</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">9,620,200</td>
<td align="right">10,025,060</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">20,379,920</td>
<td align="right">19,567,580</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">16,990,000</td>
<td align="right">16,334,820</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">17,381,620</td>
<td align="right">16,726,440</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">21,680,040</td>
<td align="right">20,987,580</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">17,916,900</td>
<td align="right">18,322,000</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">7,973,180</td>
<td align="right">7,798,700</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">27,603,960</td>
<td align="right">28,206,940</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">29,626,600</td>
<td align="right">30,229,560</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">29,626,600</td>
<td align="right">30,229,560</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">26,622,160</td>
<td align="right">27,011,140</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">26,140,420</td>
<td align="right">26,488,440</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">26,140,420</td>
<td align="right">26,488,440</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">29,752,700</td>
<td align="right">29,538,220</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">44,022,100</td>
<td align="right">43,887,980</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">857,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">656,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">288,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">142,260</td>
<td align="right">142,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">20,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">3,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right"></td>
<td align="right">2,960</td>
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
<td align="left">CALL</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">140</td>
<td align="right">180</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">140</td>
<td align="right">180</td>
<td align="right">28.6%</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-29
