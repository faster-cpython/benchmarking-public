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
<td align="left">NOT_TAKEN</td>
<td align="right">660,280</td>
<td align="right">1,646,540</td>
<td align="right">149.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,192,500</td>
<td align="right">1,102,240</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,950,460</td>
<td align="right">1,790,600</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,002,540</td>
<td align="right">948,380</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,527,880</td>
<td align="right">887,160</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">92,580</td>
<td align="right">33,260</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">247,440</td>
<td align="right">140,640</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,888,040</td>
<td align="right">1,168,500</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,344,300</td>
<td align="right">14,261,060</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,735,460</td>
<td align="right">8,883,520</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">9,051,020</td>
<td align="right">5,938,020</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,726,340</td>
<td align="right">3,255,700</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">754,700</td>
<td align="right">533,360</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">237,140</td>
<td align="right">168,400</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,930,800</td>
<td align="right">7,854,180</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,769,760</td>
<td align="right">13,510,000</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">736,780</td>
<td align="right">542,820</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">876,480</td>
<td align="right">651,640</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">95,275,420</td>
<td align="right">71,708,360</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">22,638,360</td>
<td align="right">17,080,780</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,940,740</td>
<td align="right">3,730,160</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">979,860</td>
<td align="right">743,860</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,252,820</td>
<td align="right">3,995,180</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,655,380</td>
<td align="right">13,480,860</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,482,800</td>
<td align="right">21,166,780</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,917,500</td>
<td align="right">4,693,460</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,545,800</td>
<td align="right">7,692,340</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,869,400</td>
<td align="right">4,837,320</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">43,126,580</td>
<td align="right">50,354,520</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,699,780</td>
<td align="right">2,293,640</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">778,020</td>
<td align="right">663,740</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,522,040</td>
<td align="right">9,857,460</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">21,657,580</td>
<td align="right">18,725,360</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,937,300</td>
<td align="right">70,735,700</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,767,380</td>
<td align="right">9,418,860</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">25,503,860</td>
<td align="right">22,350,960</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">110,894,140</td>
<td align="right">97,233,800</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,280,660</td>
<td align="right">10,812,700</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">35,548,340</td>
<td align="right">31,768,240</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,619,840</td>
<td align="right">18,428,220</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,243,300</td>
<td align="right">4,687,400</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">208,018,240</td>
<td align="right">187,160,900</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,246,660</td>
<td align="right">13,751,060</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,475,980</td>
<td align="right">34,886,080</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">34,533,740</td>
<td align="right">37,705,940</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,321,600</td>
<td align="right">9,377,960</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">185,562,760</td>
<td align="right">169,295,980</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,433,180</td>
<td align="right">3,133,380</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">52,805,660</td>
<td align="right">48,237,040</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">48,852,860</td>
<td align="right">44,724,380</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">113,489,080</td>
<td align="right">104,600,840</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,755,480</td>
<td align="right">2,541,340</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,152,880</td>
<td align="right">2,919,100</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">317,350,740</td>
<td align="right">294,907,560</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">205,403,300</td>
<td align="right">190,963,340</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,389,140</td>
<td align="right">72,338,700</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">192,172,820</td>
<td align="right">179,697,100</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">42,860</td>
<td align="right">40,140</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">12,740</td>
<td align="right">11,960</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,210,340,300</td>
<td align="right">1,137,415,060</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,034,160</td>
<td align="right">4,735,880</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">196,471,620</td>
<td align="right">185,178,240</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">20,087,420</td>
<td align="right">18,986,260</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,948,200</td>
<td align="right">7,525,620</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">146,015,860</td>
<td align="right">138,485,380</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">300,735,240</td>
<td align="right">285,757,620</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">323,357,600</td>
<td align="right">308,175,060</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">23,181,080</td>
<td align="right">22,122,800</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">35,245,740</td>
<td align="right">33,649,320</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">78,119,560</td>
<td align="right">74,609,680</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">37,065,120</td>
<td align="right">35,441,900</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,834,200</td>
<td align="right">4,624,440</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,418,800</td>
<td align="right">2,323,080</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,447,500</td>
<td align="right">1,390,700</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,681,840</td>
<td align="right">49,942,160</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,183,280</td>
<td align="right">49,678,680</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">381,034,280</td>
<td align="right">370,546,820</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,036,560</td>
<td align="right">18,518,960</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,318,160</td>
<td align="right">19,792,940</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,035,940</td>
<td align="right">16,641,700</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">134,360</td>
<td align="right">131,360</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,337,800</td>
<td align="right">7,177,160</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,865,160</td>
<td align="right">8,672,900</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,576,000</td>
<td align="right">16,216,880</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">179,280,520</td>
<td align="right">175,610,140</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">304,503,560</td>
<td align="right">298,313,340</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">121,899,800</td>
<td align="right">124,343,840</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">15,620</td>
<td align="right">15,320</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">30,615,780</td>
<td align="right">30,062,600</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">77,900</td>
<td align="right">76,640</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">24,943,160</td>
<td align="right">25,333,600</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">120,610,500</td>
<td align="right">118,990,980</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,096,060</td>
<td align="right">29,717,740</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,076,140</td>
<td align="right">29,698,380</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,398,460</td>
<td align="right">23,105,840</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">35,009,780</td>
<td align="right">35,435,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,061,300</td>
<td align="right">4,014,100</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,280,800</td>
<td align="right">19,105,480</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,183,920</td>
<td align="right">32,463,520</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">91,960</td>
<td align="right">91,280</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">116,444,100</td>
<td align="right">115,649,000</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,479,600</td>
<td align="right">49,164,080</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">56,896,140</td>
<td align="right">57,256,940</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,498,680</td>
<td align="right">11,428,640</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,834,780</td>
<td align="right">93,309,100</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,770,540</td>
<td align="right">1,764,860</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,547,240</td>
<td align="right">101,233,220</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">65,947,060</td>
<td align="right">65,781,640</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">150,642,240</td>
<td align="right">150,825,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,734,060</td>
<td align="right">2,731,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,737,680</td>
<td align="right">2,735,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,214,560</td>
<td align="right">4,214,360</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,122,620</td>
<td align="right">15,122,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,179,680</td>
<td align="right">22,179,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">41,711,760</td>
<td align="right">41,711,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,801,160</td>
<td align="right">38,801,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,136,560</td>
<td align="right">37,136,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,888,360</td>
<td align="right">36,888,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,642,980</td>
<td align="right">11,642,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,631,260</td>
<td align="right">9,631,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,400,820</td>
<td align="right">8,400,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,612,720</td>
<td align="right">7,612,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,149,580</td>
<td align="right">7,149,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,146,920</td>
<td align="right">6,146,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,146,920</td>
<td align="right">6,146,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,790,700</td>
<td align="right">5,790,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,984,220</td>
<td align="right">4,984,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,867,260</td>
<td align="right">2,867,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,414,220</td>
<td align="right">1,414,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,175,720</td>
<td align="right">1,175,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,158,740</td>
<td align="right">1,158,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">452,580</td>
<td align="right">452,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">389,300</td>
<td align="right">389,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,280</td>
<td align="right">267,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">239,460</td>
<td align="right">239,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">216,240</td>
<td align="right">216,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">178,500</td>
<td align="right">178,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">164,880</td>
<td align="right">164,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">152,460</td>
<td align="right">152,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">128,700</td>
<td align="right">128,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">84,260</td>
<td align="right">84,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">81,840</td>
<td align="right">81,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">74,180</td>
<td align="right">74,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">68,680</td>
<td align="right">68,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">60,540</td>
<td align="right">60,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">39,200</td>
<td align="right">39,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">31,000</td>
<td align="right">31,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">30,600</td>
<td align="right">30,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">16,400</td>
<td align="right">16,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,580</td>
<td align="right">11,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,000</td>
<td align="right">8,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">7,480</td>
<td align="right">7,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,200</td>
<td align="right">7,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,960</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">6,860</td>
<td align="right">6,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">5,820</td>
<td align="right">5,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,000</td>
<td align="right">4,000</td>
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
<td align="right">2,920</td>
<td align="right">2,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,920</td>
<td align="right">2,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1,900</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,460</td>
<td align="right">1,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,460</td>
<td align="right">1,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">380</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
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
<td align="right">23,253,800</td>
<td align="right">11.8%</td>
<td align="right">22,961,600</td>
<td align="right">11.6%</td>
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
<td align="right">169,103,660</td>
<td align="right">85.5%</td>
<td align="right">169,103,920</td>
<td align="right">85.6%</td>
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
<td align="right">5,231,940</td>
<td align="right">2.6%</td>
<td align="right">5,231,940</td>
<td align="right">2.6%</td>
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
<td align="right">125,880</td>
<td align="right">51.8%</td>
<td align="right">125,460</td>
<td align="right">51.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117,160</td>
<td align="right">48.2%</td>
<td align="right">117,160</td>
<td align="right">48.3%</td>
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
<td align="left">floor divide</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">680</td>
<td align="right">0.5%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">10,280</td>
<td align="right">8.2%</td>
<td align="right">10,180</td>
<td align="right">8.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,240</td>
<td align="right">8.1%</td>
<td align="right">10,160</td>
<td align="right">8.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">8,480</td>
<td align="right">6.7%</td>
<td align="right">8,460</td>
<td align="right">6.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">82,900</td>
<td align="right">65.9%</td>
<td align="right">82,900</td>
<td align="right">66.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">9,220</td>
<td align="right">7.3%</td>
<td align="right">9,220</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">1,720</td>
<td align="right">1.4%</td>
<td align="right">1,720</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">720</td>
<td align="right">0.6%</td>
<td align="right">720</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">580</td>
<td align="right">0.5%</td>
<td align="right">580</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">440</td>
<td align="right">0.3%</td>
<td align="right">440</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">10,767,380</td>
<td align="right">100.0%</td>
<td align="right">9,418,860</td>
<td align="right">100.0%</td>
<td align="right">-12.5%</td>
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
<td align="right">17,834,260</td>
<td align="right">3.1%</td>
<td align="right">17,323,620</td>
<td align="right">3.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,568,960</td>
<td align="right">3.1%</td>
<td align="right">17,067,940</td>
<td align="right">3.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">555,834,740</td>
<td align="right">96.9%</td>
<td align="right">556,779,860</td>
<td align="right">97.0%</td>
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
<td align="right">394,000</td>
<td align="right">100.0%</td>
<td align="right">384,380</td>
<td align="right">100.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
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
<td align="right">3,580</td>
<td align="right">52.2%</td>
<td align="right">3,580</td>
<td align="right">52.2%</td>
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
<td align="right">3,280</td>
<td align="right">100.0%</td>
<td align="right">3,280</td>
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
<td align="right">1,749,440</td>
<td align="right">4.6%</td>
<td align="right">1,743,780</td>
<td align="right">4.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">255,400</td>
<td align="right">0.7%</td>
<td align="right">255,440</td>
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
<td align="right">35,740,620</td>
<td align="right">94.6%</td>
<td align="right">35,740,640</td>
<td align="right">94.6%</td>
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
<td align="right">15,800</td>
<td align="right">61.1%</td>
<td align="right">15,780</td>
<td align="right">61.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,080</td>
<td align="right">38.9%</td>
<td align="right">10,080</td>
<td align="right">39.0%</td>
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
<td align="right">13,620</td>
<td align="right">86.2%</td>
<td align="right">13,600</td>
<td align="right">86.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">640</td>
<td align="right">4.1%</td>
<td align="right">640</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">600</td>
<td align="right">3.8%</td>
<td align="right">600</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">2.2%</td>
<td align="right">340</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.3%</td>
<td align="right">200</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">9,033,780</td>
<td align="right">14.2%</td>
<td align="right">5,921,580</td>
<td align="right">9.8%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,707,700</td>
<td align="right">85.8%</td>
<td align="right">54,707,700</td>
<td align="right">90.2%</td>
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
<td align="right">15,560</td>
<td align="right">90.3%</td>
<td align="right">14,760</td>
<td align="right">89.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,680</td>
<td align="right">9.7%</td>
<td align="right">1,680</td>
<td align="right">10.2%</td>
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
<td align="right">5,800</td>
<td align="right">37.3%</td>
<td align="right">5,340</td>
<td align="right">36.2%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,920</td>
<td align="right">18.8%</td>
<td align="right">2,720</td>
<td align="right">18.4%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,080</td>
<td align="right">26.2%</td>
<td align="right">3,940</td>
<td align="right">26.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,760</td>
<td align="right">17.7%</td>
<td align="right">2,760</td>
<td align="right">18.7%</td>
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
<td align="right">22,326,140</td>
<td align="right">10.5%</td>
<td align="right">14,245,200</td>
<td align="right">7.6%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">157,855,020</td>
<td align="right">74.0%</td>
<td align="right">141,229,800</td>
<td align="right">75.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,999,160</td>
<td align="right">15.5%</td>
<td align="right">32,313,460</td>
<td align="right">17.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">13,540</td>
<td align="right">2.1%</td>
<td align="right">11,240</td>
<td align="right">1.8%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">627,180</td>
<td align="right">97.9%</td>
<td align="right">614,240</td>
<td align="right">98.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">600</td>
<td align="right">4.4%</td>
<td align="right">240</td>
<td align="right">2.1%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,040</td>
<td align="right">7.7%</td>
<td align="right">680</td>
<td align="right">6.0%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,380</td>
<td align="right">17.6%</td>
<td align="right">1,820</td>
<td align="right">16.2%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,660</td>
<td align="right">19.6%</td>
<td align="right">2,040</td>
<td align="right">18.1%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,340</td>
<td align="right">17.3%</td>
<td align="right">2,100</td>
<td align="right">18.7%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,000</td>
<td align="right">7.4%</td>
<td align="right">900</td>
<td align="right">8.0%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,600</td>
<td align="right">19.2%</td>
<td align="right">2,560</td>
<td align="right">22.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">1.6%</td>
<td align="right">220</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">160</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">0.9%</td>
<td align="right">120</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">48,464,900</td>
<td align="right">48,464,900 / 0 !!</td>
<td align="right">48,464,900</td>
<td align="right">48,464,900 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">36,919,280</td>
<td align="right">36,919,280 / 0 !!</td>
<td align="right">36,919,280</td>
<td align="right">36,919,280 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">29,129,680</td>
<td align="right">29,129,680 / 0 !!</td>
<td align="right">29,129,680</td>
<td align="right">29,129,680 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,026,700</td>
<td align="right">6,026,700 / 0 !!</td>
<td align="right">6,026,700</td>
<td align="right">6,026,700 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,162,280</td>
<td align="right">2,162,280 / 0 !!</td>
<td align="right">2,162,280</td>
<td align="right">2,162,280 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">202,520</td>
<td align="right">202,520 / 0 !!</td>
<td align="right">202,520</td>
<td align="right">202,520 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">198,000</td>
<td align="right">198,000 / 0 !!</td>
<td align="right">198,000</td>
<td align="right">198,000 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">55,460</td>
<td align="right">55,460 / 0 !!</td>
<td align="right">55,460</td>
<td align="right">55,460 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,700</td>
<td align="right">5,700 / 0 !!</td>
<td align="right">5,700</td>
<td align="right">5,700 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">650,223,080</td>
<td align="right">63.4%</td>
<td align="right">634,945,540</td>
<td align="right">63.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">274,084,300</td>
<td align="right">26.7%</td>
<td align="right">270,372,300</td>
<td align="right">26.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">100,788,560</td>
<td align="right">9.8%</td>
<td align="right">100,502,200</td>
<td align="right">10.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
<td align="right">5,192,300</td>
<td align="right">99.3%</td>
<td align="right">5,122,180</td>
<td align="right">99.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">35,400</td>
<td align="right">0.7%</td>
<td align="right">35,600</td>
<td align="right">0.7%</td>
<td align="right">0.6%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,020</td>
<td align="right">2.9%</td>
<td align="right">940</td>
<td align="right">2.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">11,940</td>
<td align="right">33.7%</td>
<td align="right">12,360</td>
<td align="right">34.7%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">9,480</td>
<td align="right">26.8%</td>
<td align="right">9,340</td>
<td align="right">26.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,200</td>
<td align="right">9.0%</td>
<td align="right">3,200</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,380</td>
<td align="right">6.7%</td>
<td align="right">2,380</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,220</td>
<td align="right">3.4%</td>
<td align="right">1,220</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">560</td>
<td align="right">1.6%</td>
<td align="right">560</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">500</td>
<td align="right">1.4%</td>
<td align="right">500</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">320</td>
<td align="right">0.9%</td>
<td align="right">320</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">100</td>
<td align="right">0.3%</td>
<td align="right">100</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
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
<td align="right">273,833,260</td>
<td align="right">100.0%</td>
<td align="right">257,489,440</td>
<td align="right">100.0%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,760</td>
<td align="right">0.0%</td>
<td align="right">30,760</td>
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
<td align="right">880</td>
<td align="right">0.0%</td>
<td align="right">880</td>
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
<td align="right">27,500</td>
<td align="right">0.0%</td>
<td align="right">27,500</td>
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
<td align="right">30,300</td>
<td align="right">100.0%</td>
<td align="right">30,300</td>
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
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
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
<td align="right">84,640</td>
<td align="right">99.8%</td>
<td align="right">84,640</td>
<td align="right">99.8%</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">120</td>
<td align="right">1.6%</td>
<td align="right">120</td>
<td align="right">1.6%</td>
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
<td align="right">7,200</td>
<td align="right">97.6%</td>
<td align="right">7,200</td>
<td align="right">97.6%</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
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
<td align="right">47,972,680</td>
<td align="right">38.7%</td>
<td align="right">47,990,560</td>
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
<td align="right">53,718,140</td>
<td align="right">43.4%</td>
<td align="right">53,699,920</td>
<td align="right">43.4%</td>
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
<td align="right">22,137,900</td>
<td align="right">17.9%</td>
<td align="right">22,137,700</td>
<td align="right">17.9%</td>
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
<td align="right">1,022,600</td>
<td align="right">97.0%</td>
<td align="right">1,022,260</td>
<td align="right">97.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">31,920</td>
<td align="right">3.0%</td>
<td align="right">31,920</td>
<td align="right">3.0%</td>
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
<td align="right">21,760</td>
<td align="right">68.2%</td>
<td align="right">21,760</td>
<td align="right">68.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,140</td>
<td align="right">19.2%</td>
<td align="right">6,140</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,820</td>
<td align="right">12.0%</td>
<td align="right">3,820</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,340</td>
<td align="right">7.3%</td>
<td align="right">2,340</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">720</td>
<td align="right">2.3%</td>
<td align="right">720</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">180</td>
<td align="right">0.6%</td>
<td align="right">180</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">267,280</td>
<td align="right">100.0%</td>
<td align="right">267,280</td>
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
<td align="right">4,821,740</td>
<td align="right">10.1%</td>
<td align="right">4,612,200</td>
<td align="right">9.8%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,671,940</td>
<td align="right">89.8%</td>
<td align="right">42,671,940</td>
<td align="right">90.2%</td>
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
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
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
<td align="right">10,280</td>
<td align="right">82.2%</td>
<td align="right">10,060</td>
<td align="right">81.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,220</td>
<td align="right">17.8%</td>
<td align="right">2,220</td>
<td align="right">18.1%</td>
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
<td align="right">600</td>
<td align="right">5.8%</td>
<td align="right">380</td>
<td align="right">3.8%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,220</td>
<td align="right">70.2%</td>
<td align="right">7,220</td>
<td align="right">71.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,520</td>
<td align="right">14.8%</td>
<td align="right">1,520</td>
<td align="right">15.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">720</td>
<td align="right">7.0%</td>
<td align="right">720</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">220</td>
<td align="right">2.2%</td>
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
<td align="right">8,399,640</td>
<td align="right">3.2%</td>
<td align="right">7,544,640</td>
<td align="right">2.9%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">254,170,700</td>
<td align="right">95.3%</td>
<td align="right">245,072,820</td>
<td align="right">95.5%</td>
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
<td align="right">3,874,740</td>
<td align="right">1.5%</td>
<td align="right">3,827,560</td>
<td align="right">1.5%</td>
<td align="right">-1.2%</td>
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
<td align="right">173,680</td>
<td align="right">50.5%</td>
<td align="right">157,620</td>
<td align="right">48.1%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">170,360</td>
<td align="right">49.5%</td>
<td align="right">170,340</td>
<td align="right">51.9%</td>
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
<td align="left">mapping</td>
<td align="right">5,680</td>
<td align="right">3.3%</td>
<td align="right">5,660</td>
<td align="right">3.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">119,600</td>
<td align="right">70.2%</td>
<td align="right">119,600</td>
<td align="right">70.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">42,160</td>
<td align="right">24.7%</td>
<td align="right">42,160</td>
<td align="right">24.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,280</td>
<td align="right">1.3%</td>
<td align="right">2,280</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">620</td>
<td align="right">0.4%</td>
<td align="right">620</td>
<td align="right">0.4%</td>
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
<td align="right">3,760</td>
<td align="right">0.0%</td>
<td align="right">3,760</td>
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
<td align="right">48,552,100</td>
<td align="right">100.0%</td>
<td align="right">48,552,100</td>
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
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
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
<td align="right">3,760</td>
<td align="right">100.0%</td>
<td align="right">3,760</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,428,366,300</td>
<td align="right">34.5%</td>
<td align="right">2,233,857,380</td>
<td align="right">33.6%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">321,035,820</td>
<td align="right">4.6%</td>
<td align="right">306,002,060</td>
<td align="right">4.6%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,892,065,640</td>
<td align="right">55.3%</td>
<td align="right">3,718,391,900</td>
<td align="right">56.0%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">392,561,660</td>
<td align="right">5.6%</td>
<td align="right">386,780,180</td>
<td align="right">5.8%</td>
<td align="right">-1.5%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">22,326,140</td>
<td align="right">10.3%</td>
<td align="right">14,245,200</td>
<td align="right">7.0%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">9,033,780</td>
<td align="right">4.2%</td>
<td align="right">5,921,580</td>
<td align="right">2.9%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,767,380</td>
<td align="right">5.0%</td>
<td align="right">9,418,860</td>
<td align="right">4.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,821,740</td>
<td align="right">2.2%</td>
<td align="right">4,612,200</td>
<td align="right">2.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,568,960</td>
<td align="right">8.1%</td>
<td align="right">17,067,940</td>
<td align="right">8.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,253,800</td>
<td align="right">10.7%</td>
<td align="right">22,961,600</td>
<td align="right">11.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,874,740</td>
<td align="right">1.8%</td>
<td align="right">3,827,560</td>
<td align="right">1.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,749,440</td>
<td align="right">0.8%</td>
<td align="right">1,743,780</td>
<td align="right">0.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100,788,560</td>
<td align="right">46.5%</td>
<td align="right">100,502,200</td>
<td align="right">49.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,137,900</td>
<td align="right">10.2%</td>
<td align="right">22,137,700</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
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
<td align="right">4,623,100</td>
<td align="right">1.2%</td>
<td align="right">4,201,580</td>
<td align="right">1.1%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">30,530,620</td>
<td align="right">7.8%</td>
<td align="right">32,212,880</td>
<td align="right">8.3%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">84,983,260</td>
<td align="right">21.6%</td>
<td align="right">82,413,220</td>
<td align="right">21.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">100,801,740</td>
<td align="right">25.7%</td>
<td align="right">97,842,440</td>
<td align="right">25.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,500,520</td>
<td align="right">4.2%</td>
<td align="right">16,157,080</td>
<td align="right">4.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">16,498,640</td>
<td align="right">4.2%</td>
<td align="right">16,156,380</td>
<td align="right">4.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,450,460</td>
<td align="right">12.1%</td>
<td align="right">48,125,620</td>
<td align="right">12.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,683,760</td>
<td align="right">2.5%</td>
<td align="right">9,692,000</td>
<td align="right">2.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,714,960</td>
<td align="right">13.7%</td>
<td align="right">53,696,740</td>
<td align="right">13.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,560,280</td>
<td align="right">1.9%</td>
<td align="right">7,560,280</td>
<td align="right">2.0%</td>
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
<td align="right">39,856,480</td>
<td align="right">11.2%</td>
<td align="right">39,856,480</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">315,899,760</td>
<td align="right">88.8%</td>
<td align="right">315,899,760</td>
<td align="right">88.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,856,480</td>
<td align="right">11.2%</td>
<td align="right">39,856,480</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,506,240</td>
<td align="right">11.1%</td>
<td align="right">39,506,240</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">350,240</td>
<td align="right">0.1%</td>
<td align="right">350,240</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,495,840</td>
<td align="right">11.1%</td>
<td align="right">39,495,840</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">5,820</td>
<td align="right">0.0%</td>
<td align="right">5,820</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,718,960</td>
<td align="right">3.9%</td>
<td align="right">13,718,960</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,829,500</td>
<td align="right">0.5%</td>
<td align="right">1,829,500</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">8,432,220</td>
<td align="right">2.4%</td>
<td align="right">8,432,220</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">9,632,820</td>
<td align="right">2.7%</td>
<td align="right">9,632,820</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">314,845,720</td>
<td align="right">88.5%</td>
<td align="right">314,845,720</td>
<td align="right">88.5%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">532,780</td>
<td align="right">0.1%</td>
<td align="right">562,880</td>
<td align="right">0.1%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,593,403,800</td>
<td align="right">30.0%</td>
<td align="right">1,516,110,360</td>
<td align="right">28.4%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,133,807,799</td>
<td align="right">40.1%</td>
<td align="right">2,218,609,403</td>
<td align="right">41.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,974,517,403</td>
<td align="right">35.4%</td>
<td align="right">2,042,062,372</td>
<td align="right">36.5%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,260,301,940</td>
<td align="right">40.5%</td>
<td align="right">2,200,339,140</td>
<td align="right">39.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">181,114,900</td>
<td align="right">3.4%</td>
<td align="right">178,052,080</td>
<td align="right">3.3%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">350,280</td>
<td align="right">0.1%</td>
<td align="right">354,320</td>
<td align="right">0.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">193,899,120</td>
<td align="right"></td>
<td align="right">195,606,276</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,687,880</td>
<td align="right">1.6%</td>
<td align="right">90,027,740</td>
<td align="right">1.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,411,789,709</td>
<td align="right">26.5%</td>
<td align="right">1,417,429,129</td>
<td align="right">26.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">450,933,912</td>
<td align="right"></td>
<td align="right">452,273,304</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,256,020,257</td>
<td align="right">22.5%</td>
<td align="right">1,259,489,344</td>
<td align="right">22.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,333,340</td>
<td align="right"></td>
<td align="right">2,330,244</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">35,787,508</td>
<td align="right"></td>
<td align="right">35,828,356</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">37,590,773</td>
<td align="right"></td>
<td align="right">37,628,233</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,838,040</td>
<td align="right">48.5%</td>
<td align="right">291,793,260</td>
<td align="right">48.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">308,466,120</td>
<td align="right">51.3%</td>
<td align="right">308,512,140</td>
<td align="right">51.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">308,520,420</td>
<td align="right"></td>
<td align="right">308,551,260</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,721,100</td>
<td align="right">48.7%</td>
<td align="right">292,710,460</td>
<td align="right">48.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">323,347,151</td>
<td align="right"></td>
<td align="right">323,347,348</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,578,480</td>
<td align="right"></td>
<td align="right">10,578,480</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,580</td>
<td align="right">0.3%</td>
<td align="right">26,580</td>
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
<td align="right">26,100</td>
<td align="right">70,295,060</td>
<td align="right">1,127,304,329</td>
<td align="right">43,518,480</td>
<td align="right">97,623,520</td>
<td align="right">26,080</td>
<td align="right">70,311,560</td>
<td align="right">1,136,590,500</td>
<td align="right">43,101,360</td>
<td align="right">98,121,400</td>
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
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">1,280</td>
<td align="right">1.1%</td>
<td align="right">6,300.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">140</td>
<td align="right">0.5%</td>
<td align="right">960</td>
<td align="right">0.8%</td>
<td align="right">585.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">740</td>
<td align="right">2.4%</td>
<td align="right">4,440</td>
<td align="right">3.9%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">450.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,460</td>
<td align="right">21.2%</td>
<td align="right">34,220</td>
<td align="right">29.7%</td>
<td align="right">429.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,200</td>
<td align="right">30.1%</td>
<td align="right">47,160</td>
<td align="right">40.9%</td>
<td align="right">412.6%</td>
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
<td align="right">0.7%</td>
<td align="right">760</td>
<td align="right">0.7%</td>
<td align="right">280.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">30,540</td>
<td align="right"></td>
<td align="right">115,220</td>
<td align="right"></td>
<td align="right">277.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">320</td>
<td align="right">1.0%</td>
<td align="right">1,000</td>
<td align="right">0.9%</td>
<td align="right">212.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">13,940</td>
<td align="right">45.6%</td>
<td align="right">28,640</td>
<td align="right">24.9%</td>
<td align="right">105.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,595,729,140</td>
<td align="right">2,007.7%</td>
<td align="right">5,709,577,100</td>
<td align="right">2,243.4%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">228,901,700</td>
<td align="right"></td>
<td align="right">254,501,900</td>
<td align="right"></td>
<td align="right">11.2%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">6,200</td>
<td align="right">67.4%</td>
<td align="right">41,200</td>
<td align="right">87.4%</td>
<td align="right">564.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">9,200</td>
<td align="right"></td>
<td align="right">47,160</td>
<td align="right"></td>
<td align="right">412.6%</td>
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
<td align="right">81,920</td>
<td align="right">0.1%</td>
<td align="right">105,021,440</td>
<td align="right">21.8%</td>
<td align="right">128,100.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">13,315,240</td>
<td align="right">17.2%</td>
<td align="right">90,894,320</td>
<td align="right">18.9%</td>
<td align="right">582.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,630,080</td>
<td align="right">2.1%</td>
<td align="right">10,316,160</td>
<td align="right">2.1%</td>
<td align="right">532.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">77,414,400</td>
<td align="right"></td>
<td align="right">481,935,360</td>
<td align="right"></td>
<td align="right">522.5%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">62,469,080</td>
<td align="right">80.7%</td>
<td align="right">380,724,880</td>
<td align="right">79.0%</td>
<td align="right">509.5%</td>
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
<td align="left">1,180</td>
<td align="right">19.0%</td>
<td align="left">6,780</td>
<td align="right">16.5%</td>
<td align="right">474.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">1,960</td>
<td align="right">31.6%</td>
<td align="left">17,460</td>
<td align="right">42.4%</td>
<td align="right">790.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">2,140</td>
<td align="right">34.5%</td>
<td align="left">11,280</td>
<td align="right">27.4%</td>
<td align="right">427.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">760</td>
<td align="right">12.3%</td>
<td align="left">4,980</td>
<td align="right">12.1%</td>
<td align="right">555.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">160</td>
<td align="right">2.6%</td>
<td align="left">620</td>
<td align="right">1.5%</td>
<td align="right">287.5%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">80</td>
<td align="right">0.2%</td>
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
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">2,240</td>
<td align="right">4.7%</td>
<td align="right">2,140.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,420</td>
<td align="right">15.4%</td>
<td align="right">6,580</td>
<td align="right">14.0%</td>
<td align="right">363.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,200</td>
<td align="right">34.8%</td>
<td align="right">20,680</td>
<td align="right">43.9%</td>
<td align="right">546.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">760</td>
<td align="right">8.3%</td>
<td align="right">6,900</td>
<td align="right">14.6%</td>
<td align="right">807.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,400</td>
<td align="right">37.0%</td>
<td align="right">8,660</td>
<td align="right">18.4%</td>
<td align="right">154.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">280</td>
<td align="right">3.0%</td>
<td align="right">1,300</td>
<td align="right">2.8%</td>
<td align="right">364.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">380</td>
<td align="right">0.8%</td>
<td align="right">850.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">420</td>
<td align="right">0.9%</td>
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
<td align="left"><= 16</td>
<td align="right">460</td>
<td align="right">5.0%</td>
<td align="right">3,240</td>
<td align="right">6.9%</td>
<td align="right">604.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,580</td>
<td align="right">28.0%</td>
<td align="right">16,740</td>
<td align="right">35.5%</td>
<td align="right">548.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,100</td>
<td align="right">22.8%</td>
<td align="right">13,020</td>
<td align="right">27.6%</td>
<td align="right">520.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">520</td>
<td align="right">5.7%</td>
<td align="right">5,340</td>
<td align="right">11.3%</td>
<td align="right">926.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">460</td>
<td align="right">5.0%</td>
<td align="right">1,540</td>
<td align="right">3.3%</td>
<td align="right">234.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right">340</td>
<td align="right">0.7%</td>
<td align="right">325.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">880</td>
<td align="right">1.9%</td>
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
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">15,440</td>
<td align="right">1,239,480</td>
<td align="right">7,927.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">88,440</td>
<td align="right">3,309,940</td>
<td align="right">3,642.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">640</td>
<td align="right">22,500</td>
<td align="right">3,415.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,080</td>
<td align="right">97,040</td>
<td align="right">3,050.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">12,760</td>
<td align="right">304,960</td>
<td align="right">2,290.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">24,340</td>
<td align="right">446,920</td>
<td align="right">1,736.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">24,340</td>
<td align="right">446,920</td>
<td align="right">1,736.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">146,280</td>
<td align="right">2,668,600</td>
<td align="right">1,724.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">75,120</td>
<td align="right">864,360</td>
<td align="right">1,050.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">138,120</td>
<td align="right">1,528,260</td>
<td align="right">1,006.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">13,420</td>
<td align="right">142,780</td>
<td align="right">963.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,680</td>
<td align="right">835,380</td>
<td align="right">886.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">33,820</td>
<td align="right">333,620</td>
<td align="right">886.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">47,240</td>
<td align="right">406,360</td>
<td align="right">760.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">241,740</td>
<td align="right">1,989,220</td>
<td align="right">722.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,420</td>
<td align="right">72,740</td>
<td align="right">442.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">47,760</td>
<td align="right">240,020</td>
<td align="right">402.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">15,920</td>
<td align="right">79,520</td>
<td align="right">399.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">46,020</td>
<td align="right">213,020</td>
<td align="right">362.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">608,720</td>
<td align="right">2,748,280</td>
<td align="right">351.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">47,760</td>
<td align="right">214,020</td>
<td align="right">348.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">328,460</td>
<td align="right">337.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,864,440</td>
<td align="right">7,813,840</td>
<td align="right">319.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">75,120</td>
<td align="right">308,900</td>
<td align="right">311.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">75,120</td>
<td align="right">308,900</td>
<td align="right">311.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">1,091,940</td>
<td align="right">4,440,400</td>
<td align="right">306.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">257,800</td>
<td align="right">303.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">373,660</td>
<td align="right">1,427,640</td>
<td align="right">282.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">136,580</td>
<td align="right">514,900</td>
<td align="right">277.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">136,580</td>
<td align="right">514,340</td>
<td align="right">276.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">307,220</td>
<td align="right">272.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">76,860</td>
<td align="right">286,400</td>
<td align="right">272.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">303,720</td>
<td align="right">268.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">87,960</td>
<td align="right">323,960</td>
<td align="right">268.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,365,560</td>
<td align="right">8,681,580</td>
<td align="right">267.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,802,640</td>
<td align="right">6,587,700</td>
<td align="right">265.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">380,880</td>
<td align="right">1,380,060</td>
<td align="right">262.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,573,480</td>
<td align="right">5,618,300</td>
<td align="right">257.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">877,400</td>
<td align="right">2,931,560</td>
<td align="right">234.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">877,400</td>
<td align="right">2,931,560</td>
<td align="right">234.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,304,980</td>
<td align="right">4,356,960</td>
<td align="right">233.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">766,480</td>
<td align="right">2,506,100</td>
<td align="right">227.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">235,320</td>
<td align="right">760,660</td>
<td align="right">223.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">235,320</td>
<td align="right">760,660</td>
<td align="right">223.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">864,000</td>
<td align="right">2,760,340</td>
<td align="right">219.5%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">247,400</td>
<td align="right">760,700</td>
<td align="right">207.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">46,020</td>
<td align="right">133,640</td>
<td align="right">190.4%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">214,080</td>
<td align="right">608,260</td>
<td align="right">184.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,604,700</td>
<td align="right">4,536,920</td>
<td align="right">182.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">2,035,900</td>
<td align="right">5,737,520</td>
<td align="right">181.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">351,180</td>
<td align="right">907,080</td>
<td align="right">158.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">931,260</td>
<td align="right">2,285,540</td>
<td align="right">145.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,646,860</td>
<td align="right">8,906,620</td>
<td align="right">144.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,840</td>
<td align="right">304,160</td>
<td align="right">136.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,328,540</td>
<td align="right">7,803,580</td>
<td align="right">134.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">88,440</td>
<td align="right">202,720</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">75,120</td>
<td align="right">170,840</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">170,440</td>
<td align="right">384,580</td>
<td align="right">125.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">8,502,220</td>
<td align="right">19,159,100</td>
<td align="right">125.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,933,420</td>
<td align="right">6,502,760</td>
<td align="right">121.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,693,960</td>
<td align="right">5,846,860</td>
<td align="right">117.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,646,700</td>
<td align="right">5,723,380</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">17,507,920</td>
<td align="right">36,401,500</td>
<td align="right">107.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">6,715,860</td>
<td align="right">12,906,080</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,433,380</td>
<td align="right">6,545,580</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">17,854,200</td>
<td align="right">32,832,100</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">18,235,080</td>
<td align="right">33,501,820</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">18,235,080</td>
<td align="right">33,501,820</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">13,688,800</td>
<td align="right">25,141,920</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">18,159,960</td>
<td align="right">33,192,920</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">14,330,320</td>
<td align="right">26,033,380</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,334,280</td>
<td align="right">2,421,740</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,193,180</td>
<td align="right">25,337,560</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,499,000</td>
<td align="right">18,432,460</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">20,769,340</td>
<td align="right">35,940,300</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">3,758,280</td>
<td align="right">6,339,600</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">2,052,420</td>
<td align="right">3,400,940</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">5,355,600</td>
<td align="right">8,767,320</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,554,080</td>
<td align="right">4,173,600</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">22,596,200</td>
<td align="right">35,740,440</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,054,380</td>
<td align="right">3,155,540</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,843,060</td>
<td align="right">58,966,280</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">38,843,060</td>
<td align="right">58,966,280</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">137,540</td>
<td align="right">206,280</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,102,040</td>
<td align="right">4,570,000</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,814,240</td>
<td align="right">20,265,620</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">3,738,760</td>
<td align="right">5,386,740</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,520,680</td>
<td align="right">6,374,140</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">23,085,080</td>
<td align="right">32,263,120</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">13,388,360</td>
<td align="right">18,548,220</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">41,406,980</td>
<td align="right">57,057,560</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">40,230,480</td>
<td align="right">54,689,740</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">91,193,020</td>
<td align="right">123,364,100</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,395,160</td>
<td align="right">3,190,260</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,744,340</td>
<td align="right">16,918,860</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">64,077,720</td>
<td align="right">84,687,820</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">4,798,200</td>
<td align="right">3,334,540</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">5,226,280</td>
<td align="right">3,637,380</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">47,346,280</td>
<td align="right">61,417,340</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">52,535,920</td>
<td align="right">68,122,980</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">29,618,900</td>
<td align="right">38,087,420</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">14,542,240</td>
<td align="right">18,243,100</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">80,019,260</td>
<td align="right">99,963,000</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">9,164,540</td>
<td align="right">11,412,820</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,591,540</td>
<td align="right">30,615,340</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">55,122,600</td>
<td align="right">68,516,100</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">13,855,720</td>
<td align="right">17,222,240</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">55,122,600</td>
<td align="right">68,504,000</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">833,189,560</td>
<td align="right">1,024,190,860</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">686,174,620</td>
<td align="right">843,398,020</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,823,560</td>
<td align="right">3,735,940</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">17,883,580</td>
<td align="right">21,862,320</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">29,952,540</td>
<td align="right">36,427,920</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">167,537,000</td>
<td align="right">203,066,360</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">45,030,160</td>
<td align="right">54,555,380</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">25,852,640</td>
<td align="right">31,240,360</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">16,587,700</td>
<td align="right">20,034,600</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">4,927,180</td>
<td align="right">3,906,540</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">14,070,080</td>
<td align="right">16,942,420</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">18,613,880</td>
<td align="right">21,935,540</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">43,881,100</td>
<td align="right">51,033,880</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">13,484,400</td>
<td align="right">15,676,020</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">13,484,400</td>
<td align="right">15,676,020</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">32,007,180</td>
<td align="right">37,187,640</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">270,308,680</td>
<td align="right">311,559,460</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,837,020</td>
<td align="right">4,362,240</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">14,026,520</td>
<td align="right">15,837,300</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">36,021,980</td>
<td align="right">40,617,940</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">15,220,980</td>
<td align="right">17,070,160</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">8,716,940</td>
<td align="right">9,759,540</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">40,724,800</td>
<td align="right">45,576,740</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">40,699,120</td>
<td align="right">45,424,140</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,346,600</td>
<td align="right">15,971,100</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">228,901,700</td>
<td align="right">254,501,900</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,855,640</td>
<td align="right">13,173,100</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">15,285,420</td>
<td align="right">16,926,940</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">228,762,940</td>
<td align="right">252,951,140</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">22,830,640</td>
<td align="right">25,118,860</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">237,357,220</td>
<td align="right">259,660,580</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">14,544,440</td>
<td align="right">15,906,720</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">62,235,840</td>
<td align="right">68,046,280</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,108,300</td>
<td align="right">14,318,880</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">6,082,160</td>
<td align="right">6,641,980</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">6,565,700</td>
<td align="right">5,969,520</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">63,824,300</td>
<td align="right">69,526,060</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,708,180</td>
<td align="right">4,011,640</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">6,565,700</td>
<td align="right">6,111,280</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">6,565,700</td>
<td align="right">6,140,180</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">30,024,340</td>
<td align="right">31,726,820</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,564,680</td>
<td align="right">5,285,080</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,475,980</td>
<td align="right">11,877,560</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,580,600</td>
<td align="right">5,355,480</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,960,860</td>
<td align="right">10,600,060</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,748,420</td>
<td align="right">10,063,940</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">34,557,260</td>
<td align="right">35,542,680</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">19,887,460</td>
<td align="right">20,440,640</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,864,480</td>
<td align="right">16,474,040</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">34,252,820</td>
<td align="right">35,018,140</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">5,583,720</td>
<td align="right">5,672,660</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">26,960,880</td>
<td align="right">27,353,500</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,552,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,552,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">719,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">158,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">151,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right"></td>
<td align="right">138,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">138,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">138,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">120,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right"></td>
<td align="right">118,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">106,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">87,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">70,040</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">56,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">56,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">19,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">6,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">5,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right"></td>
<td align="right">4,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">3,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">2,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">2,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">2,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">1,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">60</td>
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
<td align="right">880</td>
<td align="right">5,400</td>
<td align="right">513.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">1,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right">420</td>
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
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
Stats gathered on: 2025-07-02
