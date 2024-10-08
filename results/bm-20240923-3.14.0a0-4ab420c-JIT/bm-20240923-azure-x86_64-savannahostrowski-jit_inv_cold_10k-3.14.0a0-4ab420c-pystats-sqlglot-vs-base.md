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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">3,000</td>
<td align="right">34,200</td>
<td align="right">1,040.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,640</td>
<td align="right">17,240</td>
<td align="right">951.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,280</td>
<td align="right">170,460</td>
<td align="right">740.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,960</td>
<td align="right">73,840</td>
<td align="right">724.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,300</td>
<td align="right">65,460</td>
<td align="right">688.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,880</td>
<td align="right">21,640</td>
<td align="right">457.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,640</td>
<td align="right">57,480</td>
<td align="right">440.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">991,100</td>
<td align="right">4,733,160</td>
<td align="right">377.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">288,880</td>
<td align="right">1,146,760</td>
<td align="right">297.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">170,520</td>
<td align="right">585,960</td>
<td align="right">243.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,780</td>
<td align="right">5,700</td>
<td align="right">220.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,800</td>
<td align="right">33,200</td>
<td align="right">207.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">444,880</td>
<td align="right">1,147,140</td>
<td align="right">157.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">36,120</td>
<td align="right">89,640</td>
<td align="right">148.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">469,520</td>
<td align="right">1,125,640</td>
<td align="right">139.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">39,880</td>
<td align="right">92,300</td>
<td align="right">131.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">950,800</td>
<td align="right">2,052,980</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">467,620</td>
<td align="right">977,620</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">44,760</td>
<td align="right">89,720</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">34,820</td>
<td align="right">64,260</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">551,260</td>
<td align="right">980,200</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,639,540</td>
<td align="right">804,680</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">130,360</td>
<td align="right">188,140</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,600,060</td>
<td align="right">12,341,840</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">259,340</td>
<td align="right">354,100</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,056,060</td>
<td align="right">1,306,880</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,727,500</td>
<td align="right">2,330,860</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,291,900</td>
<td align="right">1,720,840</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,205,700</td>
<td align="right">1,486,140</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">50,800</td>
<td align="right">67,180</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,647,740</td>
<td align="right">16,685,540</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,025,460</td>
<td align="right">5,206,500</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">10,960</td>
<td align="right">13,880</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,141,940</td>
<td align="right">15,270,940</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">234,100</td>
<td align="right">286,700</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">19,058,420</td>
<td align="right">15,231,280</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,443,720</td>
<td align="right">7,625,420</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,926,280</td>
<td align="right">8,414,840</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,716,140</td>
<td align="right">8,879,840</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">28,144,080</td>
<td align="right">24,878,060</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">607,300</td>
<td align="right">676,160</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,886,220</td>
<td align="right">4,320,500</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,886,440</td>
<td align="right">4,320,580</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">222,780</td>
<td align="right">247,080</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">33,199,480</td>
<td align="right">36,751,260</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,219,020</td>
<td align="right">6,491,260</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,083,900</td>
<td align="right">6,371,740</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">450,960</td>
<td align="right">491,600</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">307,220</td>
<td align="right">334,560</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">7,520,220</td>
<td align="right">6,857,860</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,625,080</td>
<td align="right">2,827,880</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,877,360</td>
<td align="right">9,139,700</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,859,380</td>
<td align="right">11,058,200</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95,847,780</td>
<td align="right">102,069,900</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">25,460</td>
<td align="right">26,820</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">30,709,080</td>
<td align="right">29,357,180</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,144,800</td>
<td align="right">4,321,460</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,673,720</td>
<td align="right">15,972,000</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,049,800</td>
<td align="right">1,084,400</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,968,280</td>
<td align="right">2,021,800</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,400</td>
<td align="right">2,340</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,676,020</td>
<td align="right">5,815,580</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">627,420</td>
<td align="right">640,780</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,812,640</td>
<td align="right">4,914,100</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,186,020</td>
<td align="right">20,807,000</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28,807,260</td>
<td align="right">29,320,140</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">21,596,980</td>
<td align="right">21,980,020</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,874,080</td>
<td align="right">5,951,280</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">22,161,400</td>
<td align="right">22,444,440</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,336,840</td>
<td align="right">17,149,360</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,230,540</td>
<td align="right">2,249,500</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">46,852,520</td>
<td align="right">47,157,920</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">3,069,120</td>
<td align="right">3,086,880</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">15,440</td>
<td align="right">15,520</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">16,060</td>
<td align="right">16,140</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,670,060</td>
<td align="right">1,678,360</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">4,460</td>
<td align="right">4,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">7,188,280</td>
<td align="right">7,219,240</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">636,620</td>
<td align="right">639,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">7,476,820</td>
<td align="right">7,447,320</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,975,560</td>
<td align="right">2,981,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">330,800</td>
<td align="right">331,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,324,240</td>
<td align="right">16,324,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">14,163,140</td>
<td align="right">14,163,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">10,599,840</td>
<td align="right">10,599,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,069,540</td>
<td align="right">4,069,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,557,940</td>
<td align="right">3,557,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,509,920</td>
<td align="right">3,509,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">3,307,800</td>
<td align="right">3,307,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">3,065,280</td>
<td align="right">3,065,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">3,065,280</td>
<td align="right">3,065,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">628,840</td>
<td align="right">628,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">543,840</td>
<td align="right">543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">542,600</td>
<td align="right">542,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">256,740</td>
<td align="right">256,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">148,680</td>
<td align="right">148,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">122,480</td>
<td align="right">122,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">114,100</td>
<td align="right">114,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">112,320</td>
<td align="right">112,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">71,900</td>
<td align="right">71,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">33,920</td>
<td align="right">33,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">28,260</td>
<td align="right">28,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,920</td>
<td align="right">23,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,400</td>
<td align="right">18,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,720</td>
<td align="right">13,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">12,040</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,920</td>
<td align="right">11,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">5,440</td>
<td align="right">5,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">3,940</td>
<td align="right">3,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,740</td>
<td align="right">2,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,760</td>
<td align="right">1,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,180</td>
<td align="right">1,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
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
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="right">23,420</td>
<td align="right">12.0%</td>
<td align="right">23,420</td>
<td align="right">12.0%</td>
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
<td align="right">171,780</td>
<td align="right">87.8%</td>
<td align="right">171,780</td>
<td align="right">87.8%</td>
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
<td align="right">300</td>
<td align="right">60.0%</td>
<td align="right">300</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">40.0%</td>
<td align="right">200</td>
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
<td align="right">180</td>
<td align="right">90.0%</td>
<td align="right">180</td>
<td align="right">90.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">10.0%</td>
<td align="right">20</td>
<td align="right">10.0%</td>
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
<td align="right">10,800</td>
<td align="right">100.0%</td>
<td align="right">33,200</td>
<td align="right">100.0%</td>
<td align="right">207.4%</td>
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
<td align="right">660</td>
<td align="right">0.1%</td>
<td align="right">660</td>
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
<td align="right">448,060</td>
<td align="right">99.7%</td>
<td align="right">448,060</td>
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
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">240</td>
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
<td align="right">260</td>
<td align="right">81.2%</td>
<td align="right">260</td>
<td align="right">81.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">18.8%</td>
<td align="right">60</td>
<td align="right">18.8%</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">305,600</td>
<td align="right">0.3%</td>
<td align="right">535,320</td>
<td align="right">0.6%</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">94,208,000</td>
<td align="right">99.7%</td>
<td align="right">93,871,720</td>
<td align="right">99.4%</td>
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
<td align="right">6,860</td>
<td align="right">0.0%</td>
<td align="right">6,860</td>
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
<td align="right">12,880</td>
<td align="right">100.0%</td>
<td align="right">17,200</td>
<td align="right">100.0%</td>
<td align="right">33.5%</td>
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
<td align="right">280</td>
<td align="right">50.0%</td>
<td align="right">280</td>
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
<td align="right">1,046,260</td>
<td align="right">71.5%</td>
<td align="right">1,080,760</td>
<td align="right">72.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">412,920</td>
<td align="right">28.2%</td>
<td align="right">412,920</td>
<td align="right">27.6%</td>
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
<td align="right">3,260</td>
<td align="right">92.1%</td>
<td align="right">3,360</td>
<td align="right">92.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">280</td>
<td align="right">7.9%</td>
<td align="right">280</td>
<td align="right">7.7%</td>
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
<td align="right">3.1%</td>
<td align="right">160</td>
<td align="right">4.8%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">140</td>
<td align="right">4.3%</td>
<td align="right">180</td>
<td align="right">5.4%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,360</td>
<td align="right">41.7%</td>
<td align="right">1,360</td>
<td align="right">40.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,160</td>
<td align="right">35.6%</td>
<td align="right">1,160</td>
<td align="right">34.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">12.9%</td>
<td align="right">420</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">2.5%</td>
<td align="right">80</td>
<td align="right">2.4%</td>
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
<td align="right">39,020</td>
<td align="right">63.3%</td>
<td align="right">91,340</td>
<td align="right">80.1%</td>
<td align="right">134.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,300</td>
<td align="right">5.4%</td>
<td align="right">3,320</td>
<td align="right">2.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,500</td>
<td align="right">30.0%</td>
<td align="right">18,480</td>
<td align="right">16.2%</td>
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
<td align="right">680</td>
<td align="right">73.9%</td>
<td align="right">780</td>
<td align="right">76.5%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">26.1%</td>
<td align="right">240</td>
<td align="right">23.5%</td>
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
<td align="right">680</td>
<td align="right">100.0%</td>
<td align="right">780</td>
<td align="right">100.0%</td>
<td align="right">14.7%</td>
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
<td align="right">6,901,900</td>
<td align="right">47.9%</td>
<td align="right">6,152,720</td>
<td align="right">47.3%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,515,660</td>
<td align="right">52.1%</td>
<td align="right">6,853,360</td>
<td align="right">52.7%</td>
<td align="right">-8.8%</td>
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
<td align="right">4,180</td>
<td align="right">91.7%</td>
<td align="right">4,120</td>
<td align="right">91.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">380</td>
<td align="right">8.3%</td>
<td align="right">380</td>
<td align="right">8.4%</td>
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
<td align="right">160</td>
<td align="right">3.8%</td>
<td align="right">220</td>
<td align="right">5.3%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,840</td>
<td align="right">67.9%</td>
<td align="right">2,700</td>
<td align="right">65.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">480</td>
<td align="right">11.5%</td>
<td align="right">500</td>
<td align="right">12.1%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">320</td>
<td align="right">7.7%</td>
<td align="right">320</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">3.8%</td>
<td align="right">160</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">120</td>
<td align="right">2.9%</td>
<td align="right">120</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">100</td>
<td align="right">2.4%</td>
<td align="right">100</td>
<td align="right">2.4%</td>
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
<td align="right">97,520</td>
<td align="right">0.2%</td>
<td align="right">383,940</td>
<td align="right">0.7%</td>
<td align="right">293.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,152,980</td>
<td align="right">5.5%</td>
<td align="right">4,332,040</td>
<td align="right">7.4%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">53,814,420</td>
<td align="right">94.2%</td>
<td align="right">54,458,480</td>
<td align="right">92.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">137,780</td>
<td align="right">0.2%</td>
<td align="right">137,780</td>
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
<td align="left">Success</td>
<td align="right">66,620</td>
<td align="right">95.3%</td>
<td align="right">88,880</td>
<td align="right">96.4%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,280</td>
<td align="right">4.7%</td>
<td align="right">3,280</td>
<td align="right">3.6%</td>
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
<td align="left">mutable class</td>
<td align="right">2,760</td>
<td align="right">84.1%</td>
<td align="right">2,760</td>
<td align="right">84.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">500</td>
<td align="right">15.2%</td>
<td align="right">500</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
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
<td align="right">65,934,040</td>
<td align="right">100.0%</td>
<td align="right">65,306,100</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,020</td>
<td align="right">0.0%</td>
<td align="right">6,020</td>
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
<td align="right">6,100</td>
<td align="right">100.0%</td>
<td align="right">6,100</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">10,085,160</td>
<td align="right">100.0%</td>
<td align="right">10,085,160</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
<td align="right">315,280</td>
<td align="right">43.0%</td>
<td align="right">303,240</td>
<td align="right">41.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">415,460</td>
<td align="right">56.7%</td>
<td align="right">427,740</td>
<td align="right">58.4%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">880</td>
<td align="right">0.1%</td>
<td align="right">880</td>
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
<td align="right">8,580</td>
<td align="right">100.0%</td>
<td align="right">8,820</td>
<td align="right">100.0%</td>
<td align="right">2.8%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">288,460</td>
<td align="right">100.0%</td>
<td align="right">288,460</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,639,320</td>
<td align="right">3.1%</td>
<td align="right">3,154,040</td>
<td align="right">5.8%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">46,940</td>
<td align="right">0.1%</td>
<td align="right">63,260</td>
<td align="right">0.1%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,018,700</td>
<td align="right">96.8%</td>
<td align="right">50,831,880</td>
<td align="right">94.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">34,240</td>
<td align="right">98.7%</td>
<td align="right">62,820</td>
<td align="right">99.2%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">460</td>
<td align="right">1.3%</td>
<td align="right">520</td>
<td align="right">0.8%</td>
<td align="right">13.0%</td>
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
<td align="right">120</td>
<td align="right">26.1%</td>
<td align="right">180</td>
<td align="right">34.6%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">340</td>
<td align="right">73.9%</td>
<td align="right">340</td>
<td align="right">65.4%</td>
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
<td align="right">113,500</td>
<td align="right">0.7%</td>
<td align="right">113,500</td>
<td align="right">0.7%</td>
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
<td align="right">16,300,740</td>
<td align="right">99.3%</td>
<td align="right">16,300,740</td>
<td align="right">99.3%</td>
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
<td align="right">63.3%</td>
<td align="right">380</td>
<td align="right">63.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">220</td>
<td align="right">36.7%</td>
<td align="right">220</td>
<td align="right">36.7%</td>
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
<td align="right">220</td>
<td align="right">100.0%</td>
<td align="right">220</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,521,200</td>
<td align="right">0.9%</td>
<td align="right">8,460,200</td>
<td align="right">1.3%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">245,141,560</td>
<td align="right">39.1%</td>
<td align="right">259,909,100</td>
<td align="right">40.1%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,987,380</td>
<td align="right">1.4%</td>
<td align="right">8,450,820</td>
<td align="right">1.3%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">367,296,320</td>
<td align="right">58.6%</td>
<td align="right">370,797,820</td>
<td align="right">57.3%</td>
<td align="right">1.0%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">10,800</td>
<td align="right">0.1%</td>
<td align="right">33,200</td>
<td align="right">0.4%</td>
<td align="right">207.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">39,020</td>
<td align="right">0.4%</td>
<td align="right">91,340</td>
<td align="right">1.1%</td>
<td align="right">134.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">46,940</td>
<td align="right">0.5%</td>
<td align="right">63,260</td>
<td align="right">0.8%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">7,515,660</td>
<td align="right">84.0%</td>
<td align="right">6,853,360</td>
<td align="right">81.5%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,046,260</td>
<td align="right">11.7%</td>
<td align="right">1,080,760</td>
<td align="right">12.8%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">137,780</td>
<td align="right">1.5%</td>
<td align="right">137,780</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">113,500</td>
<td align="right">1.3%</td>
<td align="right">113,500</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,420</td>
<td align="right">0.3%</td>
<td align="right">23,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,860</td>
<td align="right">0.1%</td>
<td align="right">6,860</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">6,020</td>
<td align="right">0.1%</td>
<td align="right">6,020</td>
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
<td align="right">92,220</td>
<td align="right">1.7%</td>
<td align="right">343,440</td>
<td align="right">4.1%</td>
<td align="right">272.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">210,780</td>
<td align="right">3.8%</td>
<td align="right">497,200</td>
<td align="right">5.9%</td>
<td align="right">135.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">123,620</td>
<td align="right">2.2%</td>
<td align="right">230,780</td>
<td align="right">2.7%</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">972,640</td>
<td align="right">17.6%</td>
<td align="right">1,770,520</td>
<td align="right">20.9%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">572,520</td>
<td align="right">10.4%</td>
<td align="right">1,038,280</td>
<td align="right">12.3%</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">181,980</td>
<td align="right">3.3%</td>
<td align="right">304,540</td>
<td align="right">3.6%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,245,040</td>
<td align="right">40.7%</td>
<td align="right">3,135,740</td>
<td align="right">37.1%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">415,460</td>
<td align="right">7.5%</td>
<td align="right">427,740</td>
<td align="right">5.1%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">669,040</td>
<td align="right">12.1%</td>
<td align="right">670,980</td>
<td align="right">7.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">28,120</td>
<td align="right">0.5%</td>
<td align="right">28,120</td>
<td align="right">0.3%</td>
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
<td align="right">14,163,140</td>
<td align="right">22.0%</td>
<td align="right">14,163,140</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">50,353,900</td>
<td align="right">78.0%</td>
<td align="right">50,353,900</td>
<td align="right">78.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">14,163,140</td>
<td align="right">22.0%</td>
<td align="right">14,163,140</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">5,780,900</td>
<td align="right">9.0%</td>
<td align="right">5,780,900</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">8,382,240</td>
<td align="right">13.0%</td>
<td align="right">8,382,240</td>
<td align="right">13.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">5,780,900</td>
<td align="right">9.0%</td>
<td align="right">5,780,900</td>
<td align="right">9.0%</td>
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
<td align="right">1,984,000</td>
<td align="right">3.1%</td>
<td align="right">1,984,000</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">32,160</td>
<td align="right">0.0%</td>
<td align="right">32,160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,774,020</td>
<td align="right">5.8%</td>
<td align="right">3,774,020</td>
<td align="right">5.8%</td>
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
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">41,460,640</td>
<td align="right">64.3%</td>
<td align="right">41,460,640</td>
<td align="right">64.3%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,953</td>
<td align="right"></td>
<td align="right">5,864</td>
<td align="right"></td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">41,620</td>
<td align="right">0.0%</td>
<td align="right">54,040</td>
<td align="right">0.1%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">404,415,037</td>
<td align="right">404,415,037 / 0 !!</td>
<td align="right">382,059,301</td>
<td align="right">382,059,301 / 0 !!</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">423,077,179</td>
<td align="right">423,077,179 / 0 !!</td>
<td align="right">399,793,096</td>
<td align="right">399,793,096 / 0 !!</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">265,613,640</td>
<td align="right">265,613,640 / 0 !!</td>
<td align="right">275,051,200</td>
<td align="right">275,051,200 / 0 !!</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">342,957,340</td>
<td align="right">342,957,340 / 0 !!</td>
<td align="right">353,359,540</td>
<td align="right">353,359,540 / 0 !!</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">584,881</td>
<td align="right"></td>
<td align="right">596,769</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">585,892</td>
<td align="right"></td>
<td align="right">595,597</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,311,448</td>
<td align="right"></td>
<td align="right">5,359,463</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">61,180,587</td>
<td align="right"></td>
<td align="right">61,077,176</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">65,458,871</td>
<td align="right"></td>
<td align="right">65,486,997</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">65,220,120</td>
<td align="right">62.4%</td>
<td align="right">65,238,280</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">39,390,320</td>
<td align="right"></td>
<td align="right">39,396,620</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">39,274,780</td>
<td align="right">37.6%</td>
<td align="right">39,279,440</td>
<td align="right">37.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">65,178,380</td>
<td align="right">62.4%</td>
<td align="right">65,183,400</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">20,880</td>
<td align="right"></td>
<td align="right">20,880</td>
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
<td align="right">80</td>
<td align="right">16,740</td>
<td align="right">5,434,160</td>
<td align="right">80</td>
<td align="right">20,420</td>
<td align="right">5,516,480</td>
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
<td align="right">420</td>
<td align="right">3.6%</td>
<td align="right">2,920</td>
<td align="right">8.2%</td>
<td align="right">595.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">3,660</td>
<td align="right">31.2%</td>
<td align="right">21,720</td>
<td align="right">61.3%</td>
<td align="right">493.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">420</td>
<td align="right">3.6%</td>
<td align="right">2,280</td>
<td align="right">6.4%</td>
<td align="right">442.9%</td>
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
<td align="right">0.2%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">11,720</td>
<td align="right"></td>
<td align="right">35,460</td>
<td align="right"></td>
<td align="right">202.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">8,380</td>
<td align="right">71.5%</td>
<td align="right">19,060</td>
<td align="right">53.8%</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">8,060</td>
<td align="right">68.8%</td>
<td align="right">13,740</td>
<td align="right">38.7%</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">61,280,060</td>
<td align="right"></td>
<td align="right">51,113,760</td>
<td align="right"></td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">862,378,160</td>
<td align="right">1,407.3%</td>
<td align="right">838,656,660</td>
<td align="right">1,640.8%</td>
<td align="right">-2.8%</td>
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
<td align="right">3,460</td>
<td align="right">94.5%</td>
<td align="right">21,020</td>
<td align="right">96.8%</td>
<td align="right">507.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">3,660</td>
<td align="right"></td>
<td align="right">21,720</td>
<td align="right"></td>
<td align="right">493.4%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">280</td>
<td align="right">1.3%</td>
<td align="right">366.7%</td>
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
<td align="right">160</td>
<td align="right">4.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">580</td>
<td align="right">15.8%</td>
<td align="right">3,040</td>
<td align="right">14.0%</td>
<td align="right">424.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">480</td>
<td align="right">13.1%</td>
<td align="right">2,340</td>
<td align="right">10.8%</td>
<td align="right">387.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">680</td>
<td align="right">18.6%</td>
<td align="right">7,800</td>
<td align="right">35.9%</td>
<td align="right">1,047.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">680</td>
<td align="right">18.6%</td>
<td align="right">2,420</td>
<td align="right">11.1%</td>
<td align="right">255.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">540</td>
<td align="right">14.8%</td>
<td align="right">3,580</td>
<td align="right">16.5%</td>
<td align="right">563.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">480</td>
<td align="right">13.1%</td>
<td align="right">1,880</td>
<td align="right">8.7%</td>
<td align="right">291.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">660</td>
<td align="right">3.0%</td>
<td align="right">1,000.0%</td>
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
<td align="right">660</td>
<td align="right">18.0%</td>
<td align="right">2,760</td>
<td align="right">12.7%</td>
<td align="right">318.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">400</td>
<td align="right">10.9%</td>
<td align="right">1,640</td>
<td align="right">7.6%</td>
<td align="right">310.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">560</td>
<td align="right">15.3%</td>
<td align="right">5,180</td>
<td align="right">23.8%</td>
<td align="right">825.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">580</td>
<td align="right">15.8%</td>
<td align="right">4,720</td>
<td align="right">21.7%</td>
<td align="right">713.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">560</td>
<td align="right">15.3%</td>
<td align="right">2,520</td>
<td align="right">11.6%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">560</td>
<td align="right">15.3%</td>
<td align="right">3,020</td>
<td align="right">13.9%</td>
<td align="right">439.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">3.8%</td>
<td align="right">1,180</td>
<td align="right">5.4%</td>
<td align="right">742.9%</td>
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
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">434,740</td>
<td align="right">600</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">859,080</td>
<td align="right">1,200</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">429,540</td>
<td align="right">600</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">429,540</td>
<td align="right">600</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">424,280</td>
<td align="right">660</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,756,520</td>
<td align="right">14,460</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">425,360</td>
<td align="right">9,920</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">7,660</td>
<td align="right">1,420</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,727,880</td>
<td align="right">487,960</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">68,280</td>
<td align="right">23,320</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,345,300</td>
<td align="right">471,140</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">440</td>
<td align="right">160</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">440</td>
<td align="right">160</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">46,860</td>
<td align="right">17,420</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,346,700</td>
<td align="right">529,720</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">6,800</td>
<td align="right">2,880</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,021,000</td>
<td align="right">2,983,200</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,839,740</td>
<td align="right">9,135,260</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">42,000</td>
<td align="right">19,600</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">30,040</td>
<td align="right">14,440</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">16,660</td>
<td align="right">8,360</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">280,320</td>
<td align="right">147,520</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,578,520</td>
<td align="right">2,316,180</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">65,960</td>
<td align="right">36,520</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,860</td>
<td align="right">3,280</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">120,660</td>
<td align="right">68,060</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,637,880</td>
<td align="right">5,149,320</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">8,240</td>
<td align="right">5,320</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">8,240</td>
<td align="right">5,320</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,356,860</td>
<td align="right">3,191,780</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">4,381,620</td>
<td align="right">5,919,300</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">596,520</td>
<td align="right">393,720</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">30,945,560</td>
<td align="right">20,844,960</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">8,025,140</td>
<td align="right">5,429,020</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,545,560</td>
<td align="right">3,319,860</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,726,720</td>
<td align="right">3,487,760</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">19,091,140</td>
<td align="right">13,774,920</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,770,160</td>
<td align="right">3,529,260</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,740,220</td>
<td align="right">3,459,780</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,168,200</td>
<td align="right">862,720</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,994,720</td>
<td align="right">3,765,780</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">121,280</td>
<td align="right">90,080</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">21,800</td>
<td align="right">16,580</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,924,940</td>
<td align="right">3,623,860</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,519,900</td>
<td align="right">4,321,080</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,288,880</td>
<td align="right">4,107,880</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">14,088,740</td>
<td align="right">11,011,780</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,313,760</td>
<td align="right">4,026,540</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,371,520</td>
<td align="right">4,218,040</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">280,160</td>
<td align="right">223,000</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">50,211,240</td>
<td align="right">40,067,500</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,913,720</td>
<td align="right">3,455,700</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">274,260</td>
<td align="right">224,100</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">10,442,280</td>
<td align="right">8,557,080</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">61,280,060</td>
<td align="right">51,113,760</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">292,080</td>
<td align="right">245,240</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,685,940</td>
<td align="right">5,398,100</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">30,388,320</td>
<td align="right">25,816,960</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,713,240</td>
<td align="right">4,010,980</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,283,260</td>
<td align="right">12,170,000</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">4,003,640</td>
<td align="right">4,585,120</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">480,700</td>
<td align="right">411,840</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">52,705,060</td>
<td align="right">45,982,360</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">103,320</td>
<td align="right">90,200</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">276,260</td>
<td align="right">241,760</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,139,340</td>
<td align="right">3,629,340</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">458,400</td>
<td align="right">404,880</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">458,400</td>
<td align="right">404,880</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,063,180</td>
<td align="right">3,398,400</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,018,520</td>
<td align="right">7,767,700</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,018,520</td>
<td align="right">7,767,700</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,333,600</td>
<td align="right">1,196,020</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,282,820</td>
<td align="right">4,745,800</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">84,369,640</td>
<td align="right">75,838,300</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,907,240</td>
<td align="right">5,383,260</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">887,960</td>
<td align="right">801,900</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">2,412,040</td>
<td align="right">2,180,420</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">443,980</td>
<td align="right">401,560</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">443,980</td>
<td align="right">401,560</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">1,524,080</td>
<td align="right">1,378,520</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">1,524,080</td>
<td align="right">1,378,520</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">574,920</td>
<td align="right">522,600</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">858,080</td>
<td align="right">780,880</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">14,828,060</td>
<td align="right">13,510,320</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">642,540</td>
<td align="right">585,660</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">218,980</td>
<td align="right">200,020</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">17,261,200</td>
<td align="right">18,736,200</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">14,570,880</td>
<td align="right">13,337,080</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">11,653,560</td>
<td align="right">10,692,180</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">26,019,820</td>
<td align="right">24,167,460</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,078,100</td>
<td align="right">1,943,620</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">4,226,980</td>
<td align="right">3,965,220</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">22,382,460</td>
<td align="right">21,059,860</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">454,700</td>
<td align="right">430,400</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">13,010,720</td>
<td align="right">13,673,020</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,722,040</td>
<td align="right">1,641,040</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,280</td>
<td align="right">1,220</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">10,493,920</td>
<td align="right">10,020,420</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">14,031,760</td>
<td align="right">13,420,300</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">20,885,380</td>
<td align="right">20,044,380</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">15,684,840</td>
<td align="right">15,092,600</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,338,000</td>
<td align="right">3,456,360</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,338,000</td>
<td align="right">3,456,360</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">4,820,780</td>
<td align="right">4,681,220</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">3,827,920</td>
<td align="right">3,726,460</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,084,700</td>
<td align="right">3,006,400</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">25,092,920</td>
<td align="right">24,463,700</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,711,460</td>
<td align="right">1,671,600</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,866,100</td>
<td align="right">5,746,580</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">3,551,120</td>
<td align="right">3,486,240</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">15,906,440</td>
<td align="right">15,623,400</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,284,020</td>
<td align="right">5,194,260</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">3,623,320</td>
<td align="right">3,565,540</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,805,420</td>
<td align="right">2,764,040</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">9,310,860</td>
<td align="right">9,407,900</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,296,620</td>
<td align="right">6,235,660</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">14,842,640</td>
<td align="right">14,982,220</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,494,120</td>
<td align="right">3,463,160</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">20,811,540</td>
<td align="right">20,981,420</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">7,016,040</td>
<td align="right">6,998,280</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">11,068,820</td>
<td align="right">11,044,820</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,045,120</td>
<td align="right">4,045,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">948,220</td>
<td align="right">948,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">764,880</td>
<td align="right">764,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">764,880</td>
<td align="right">764,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">509,960</td>
<td align="right">509,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">461,360</td>
<td align="right">461,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">272,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">268,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">17,360</td>
<td align="right">17,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,480</td>
<td align="right">12,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">12,400</td>
<td align="right">12,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">12,400</td>
<td align="right">12,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">7,120</td>
<td align="right">7,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">4,800</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,440</td>
<td align="right">2,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,320</td>
<td align="right">2,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">52,785,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">1,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
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
<td align="right">120</td>
<td align="right">240</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">440</td>
<td align="right">60</td>
<td align="right">-86.4%</td>
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
