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
<td align="left">BUILD_TUPLE</td>
<td align="right">27,581,080</td>
<td align="right">31,911,280</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">24,334,440</td>
<td align="right">28,011,120</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">53,356,700</td>
<td align="right">61,073,780</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">34,891,100</td>
<td align="right">38,946,680</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">40,257,820</td>
<td align="right">44,612,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,991,520</td>
<td align="right">32,985,120</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">8,378,100</td>
<td align="right">9,086,380</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">33,639,600</td>
<td align="right">30,820,100</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,669,880</td>
<td align="right">1,535,660</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,070,260</td>
<td align="right">10,302,980</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">57,064,420</td>
<td align="right">60,788,480</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">28,426,560</td>
<td align="right">30,226,600</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">160,352,560</td>
<td align="right">170,271,020</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">103,251,920</td>
<td align="right">109,358,760</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,011,080</td>
<td align="right">22,614,740</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">326,800</td>
<td align="right">309,420</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">199,037,220</td>
<td align="right">209,316,580</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">60,755,440</td>
<td align="right">57,623,740</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,859,600</td>
<td align="right">18,875,500</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">61,209,000</td>
<td align="right">64,103,740</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">124,607,440</td>
<td align="right">130,486,660</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">89,120,980</td>
<td align="right">92,559,900</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">271,339,180</td>
<td align="right">281,200,840</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">65,275,220</td>
<td align="right">67,617,120</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">145,479,480</td>
<td align="right">150,252,920</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,564,140</td>
<td align="right">2,638,880</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,262,220</td>
<td align="right">2,203,100</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,997,920</td>
<td align="right">2,931,040</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,414,160</td>
<td align="right">4,322,460</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,126,160,200</td>
<td align="right">1,148,160,960</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,586,720</td>
<td align="right">11,365,380</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,630,500</td>
<td align="right">4,546,740</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">44,643,020</td>
<td align="right">43,900,100</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">141,954,740</td>
<td align="right">139,613,940</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">228,224,820</td>
<td align="right">224,535,320</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,842,400</td>
<td align="right">9,689,380</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,552,340</td>
<td align="right">4,483,240</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">895,420</td>
<td align="right">907,680</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,463,180</td>
<td align="right">16,240,000</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,823,460</td>
<td align="right">17,589,960</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,907,240</td>
<td align="right">10,769,620</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,990,360</td>
<td align="right">36,541,500</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,180</td>
<td align="right">34,760</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">58,700</td>
<td align="right">59,400</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">154,801,900</td>
<td align="right">156,519,220</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,850,120</td>
<td align="right">15,682,300</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">103,898,940</td>
<td align="right">102,806,860</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,441,880</td>
<td align="right">1,428,040</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,241,400</td>
<td align="right">9,155,020</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,170,640</td>
<td align="right">4,131,800</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">27,757,740</td>
<td align="right">28,010,540</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">37,944,900</td>
<td align="right">38,287,460</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">37,852,620</td>
<td align="right">38,181,080</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,034,060</td>
<td align="right">17,881,640</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,077,960</td>
<td align="right">16,212,120</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,923,860</td>
<td align="right">9,841,840</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,703,160</td>
<td align="right">6,648,240</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">148,436,780</td>
<td align="right">149,552,800</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,952,880</td>
<td align="right">12,855,500</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,662,160</td>
<td align="right">17,529,660</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,556,160</td>
<td align="right">7,500,380</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,011,460</td>
<td align="right">7,061,880</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,961,440</td>
<td align="right">4,925,940</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">234,350,720</td>
<td align="right">235,892,200</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">329,660</td>
<td align="right">331,820</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,814,020</td>
<td align="right">6,769,420</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,820,380</td>
<td align="right">17,709,160</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,083,520</td>
<td align="right">11,017,820</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,896,100</td>
<td align="right">28,732,960</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,896,160</td>
<td align="right">28,733,020</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,601,240</td>
<td align="right">1,592,360</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,438,740</td>
<td align="right">4,462,680</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,771,500</td>
<td align="right">2,757,380</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,409,540</td>
<td align="right">62,099,900</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">456,060</td>
<td align="right">458,300</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,613,520</td>
<td align="right">14,544,360</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,250,060</td>
<td align="right">11,300,300</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,431,820</td>
<td align="right">6,403,240</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">584,320</td>
<td align="right">586,820</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,340</td>
<td align="right">71,060</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">105,390,380</td>
<td align="right">104,977,480</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">215,044,200</td>
<td align="right">215,819,640</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">397,360</td>
<td align="right">398,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,334,260</td>
<td align="right">13,293,980</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,494,760</td>
<td align="right">20,435,140</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,239,180</td>
<td align="right">1,242,620</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,187,060</td>
<td align="right">38,098,360</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">206,774,440</td>
<td align="right">206,318,800</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,403,860</td>
<td align="right">2,409,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">139,357,780</td>
<td align="right">139,642,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,914,880</td>
<td align="right">12,889,560</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,780</td>
<td align="right">230,360</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,237,840</td>
<td align="right">38,169,060</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,133,380</td>
<td align="right">6,122,960</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,722,300</td>
<td align="right">2,718,540</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,043,260</td>
<td align="right">1,044,560</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">318,980</td>
<td align="right">318,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">152,300</td>
<td align="right">152,460</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,225,580</td>
<td align="right">3,228,620</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,979,000</td>
<td align="right">1,977,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,675,840</td>
<td align="right">9,682,460</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,038,840</td>
<td align="right">4,036,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,219,900</td>
<td align="right">91,194,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,278,080</td>
<td align="right">16,280,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">159,820,900</td>
<td align="right">159,805,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,765,020</td>
<td align="right">21,765,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,880</td>
<td align="right">4,581,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,139,120</td>
<td align="right">7,139,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,113,900</td>
<td align="right">37,113,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">36,886,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,760</td>
<td align="right">11,627,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,412,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">7,613,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,134,820</td>
<td align="right">6,134,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,134,820</td>
<td align="right">6,134,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,778,720</td>
<td align="right">5,778,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">4,951,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,730,960</td>
<td align="right">2,730,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,727,900</td>
<td align="right">2,727,900</td>
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
<td align="right">609,940</td>
<td align="right">609,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,520</td>
<td align="right">524,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">513,300</td>
<td align="right">513,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">332,160</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">75,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right">49,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">42,960</td>
<td align="right">42,960</td>
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
<td align="right">14,700</td>
<td align="right">14,700</td>
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
<td align="left">SEND_GEN</td>
<td align="right">6,660</td>
<td align="right">6,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,180</td>
<td align="right">6,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
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
<td align="left">CALL</td>
<td align="right">4,020</td>
<td align="right">4,020</td>
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
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,300</td>
<td align="right">3,300</td>
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
<td align="right">2,000</td>
<td align="right">2,000</td>
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
<td align="right">840</td>
<td align="right">840</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">480</td>
<td align="right">480</td>
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
<td align="right">280</td>
<td align="right">280</td>
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
<td align="right">11,576,780</td>
<td align="right">19.3%</td>
<td align="right">11,355,480</td>
<td align="right">19.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,411,900</td>
<td align="right">80.7%</td>
<td align="right">48,411,900</td>
<td align="right">81.0%</td>
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
<td align="right">9,720</td>
<td align="right">97.8%</td>
<td align="right">9,680</td>
<td align="right">97.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">2.2%</td>
<td align="right">220</td>
<td align="right">2.2%</td>
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
<td align="right">2,680</td>
<td align="right">27.6%</td>
<td align="right">2,640</td>
<td align="right">27.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.7%</td>
<td align="right">3,180</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.5%</td>
<td align="right">3,160</td>
<td align="right">32.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
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
<td align="right">6,431,820</td>
<td align="right">100.0%</td>
<td align="right">6,403,240</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,144,820</td>
<td align="right">2.0%</td>
<td align="right">2,140,840</td>
<td align="right">2.0%</td>
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
<td align="right">9,662,500</td>
<td align="right">9.1%</td>
<td align="right">9,669,280</td>
<td align="right">9.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,973,280</td>
<td align="right">88.8%</td>
<td align="right">93,971,140</td>
<td align="right">88.8%</td>
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
<td align="right">12,720</td>
<td align="right">23.7%</td>
<td align="right">12,560</td>
<td align="right">23.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,060</td>
<td align="right">76.3%</td>
<td align="right">40,980</td>
<td align="right">76.5%</td>
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
<td align="left">out of range</td>
<td align="right">9,460</td>
<td align="right">74.4%</td>
<td align="right">9,320</td>
<td align="right">74.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,680</td>
<td align="right">13.2%</td>
<td align="right">1,660</td>
<td align="right">13.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">5.7%</td>
<td align="right">720</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">5.3%</td>
<td align="right">680</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.4%</td>
<td align="right">180</td>
<td align="right">1.4%</td>
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
<td align="right">16,576,180</td>
<td align="right">2.9%</td>
<td align="right">16,403,760</td>
<td align="right">2.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">554,744,280</td>
<td align="right">97.1%</td>
<td align="right">554,951,700</td>
<td align="right">97.1%</td>
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
<td align="right">316,820</td>
<td align="right">100.0%</td>
<td align="right">313,520</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">104,920</td>
<td align="right">0.3%</td>
<td align="right">180,060</td>
<td align="right">0.5%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,663,640</td>
<td align="right">4.6%</td>
<td align="right">1,525,280</td>
<td align="right">4.2%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,683,780</td>
<td align="right">95.1%</td>
<td align="right">34,747,820</td>
<td align="right">95.3%</td>
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
<td align="right">5,900</td>
<td align="right">71.8%</td>
<td align="right">10,020</td>
<td align="right">72.8%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,320</td>
<td align="right">28.2%</td>
<td align="right">3,740</td>
<td align="right">27.2%</td>
<td align="right">61.2%</td>
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
<td align="right">5,440</td>
<td align="right">92.2%</td>
<td align="right">9,560</td>
<td align="right">95.4%</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">3.4%</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">1.4%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">1.4%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="right">4,957,440</td>
<td align="right">8.4%</td>
<td align="right">4,922,000</td>
<td align="right">8.3%</td>
<td align="right">-0.7%</td>
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
<td align="right">91.6%</td>
<td align="right">54,350,400</td>
<td align="right">91.7%</td>
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
<td align="right">3,880</td>
<td align="right">97.0%</td>
<td align="right">3,820</td>
<td align="right">97.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">120</td>
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
<td align="left">tuple</td>
<td align="right">920</td>
<td align="right">23.7%</td>
<td align="right">880</td>
<td align="right">23.0%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">38.1%</td>
<td align="right">1,460</td>
<td align="right">38.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">20.6%</td>
<td align="right">800</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">680</td>
<td align="right">17.5%</td>
<td align="right">680</td>
<td align="right">17.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,814,760</td>
<td align="right">14.8%</td>
<td align="right">21,518,020</td>
<td align="right">14.8%</td>
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
<td align="right">15,845,320</td>
<td align="right">10.8%</td>
<td align="right">15,677,560</td>
<td align="right">10.8%</td>
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
<td align="right">109,386,040</td>
<td align="right">74.4%</td>
<td align="right">108,350,760</td>
<td align="right">74.4%</td>
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
<td align="right">411,580</td>
<td align="right">98.8%</td>
<td align="right">405,980</td>
<td align="right">98.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,800</td>
<td align="right">1.2%</td>
<td align="right">4,740</td>
<td align="right">1.2%</td>
<td align="right">-1.2%</td>
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
<td align="right">100</td>
<td align="right">2.1%</td>
<td align="right">80</td>
<td align="right">1.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">760</td>
<td align="right">16.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">51.7%</td>
<td align="right">2,480</td>
<td align="right">52.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.2%</td>
<td align="right">680</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">360</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
<td align="right">88,495,820</td>
<td align="right">9.2%</td>
<td align="right">91,933,880</td>
<td align="right">9.5%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">220,418,500</td>
<td align="right">23.0%</td>
<td align="right">228,163,100</td>
<td align="right">23.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">648,764,180</td>
<td align="right">67.7%</td>
<td align="right">649,367,780</td>
<td align="right">66.9%</td>
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
<td align="left">Failure</td>
<td align="right">17,340</td>
<td align="right">0.4%</td>
<td align="right">18,180</td>
<td align="right">0.4%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,766,120</td>
<td align="right">99.6%</td>
<td align="right">4,912,340</td>
<td align="right">99.6%</td>
<td align="right">3.1%</td>
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
<td align="left">not in dict</td>
<td align="right">140</td>
<td align="right">0.8%</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,800</td>
<td align="right">39.2%</td>
<td align="right">7,560</td>
<td align="right">41.6%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,460</td>
<td align="right">31.5%</td>
<td align="right">5,560</td>
<td align="right">30.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">16.4%</td>
<td align="right">2,840</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.6%</td>
<td align="right">620</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.4%</td>
<td align="right">420</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">2.0%</td>
<td align="right">340</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.4%</td>
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">1.0%</td>
<td align="right">180</td>
<td align="right">1.0%</td>
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
<td align="right">222,759,960</td>
<td align="right">100.0%</td>
<td align="right">232,368,780</td>
<td align="right">100.0%</td>
<td align="right">4.3%</td>
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
<td align="right">2,040</td>
<td align="right">100.0%</td>
<td align="right">2,040</td>
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
<td align="right">16,066,020</td>
<td align="right">13.7%</td>
<td align="right">16,200,180</td>
<td align="right">13.8%</td>
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
<td align="right">47,041,480</td>
<td align="right">40.2%</td>
<td align="right">47,039,820</td>
<td align="right">40.1%</td>
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
<td align="right">53,913,660</td>
<td align="right">46.1%</td>
<td align="right">53,915,360</td>
<td align="right">46.0%</td>
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
<td align="right">1,017,740</td>
<td align="right">98.9%</td>
<td align="right">1,017,780</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,540</td>
<td align="right">1.1%</td>
<td align="right">11,540</td>
<td align="right">1.1%</td>
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
<td align="right">8,900</td>
<td align="right">77.1%</td>
<td align="right">8,900</td>
<td align="right">77.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.7%</td>
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
<td align="right">58,700</td>
<td align="right">100.0%</td>
<td align="right">59,400</td>
<td align="right">100.0%</td>
<td align="right">1.2%</td>
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
<td align="right">4,578,000</td>
<td align="right">9.7%</td>
<td align="right">4,577,980</td>
<td align="right">9.7%</td>
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
<td align="right">5,525,040</td>
<td align="right">2.0%</td>
<td align="right">5,187,360</td>
<td align="right">1.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,463,840</td>
<td align="right">0.9%</td>
<td align="right">2,553,680</td>
<td align="right">0.9%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">266,147,500</td>
<td align="right">97.1%</td>
<td align="right">265,850,060</td>
<td align="right">97.1%</td>
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
<td align="right">99,440</td>
<td align="right">48.6%</td>
<td align="right">84,320</td>
<td align="right">46.1%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105,060</td>
<td align="right">51.4%</td>
<td align="right">98,720</td>
<td align="right">53.9%</td>
<td align="right">-6.0%</td>
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
<td align="right">54,480</td>
<td align="right">54.8%</td>
<td align="right">39,420</td>
<td align="right">46.8%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,400</td>
<td align="right">41.6%</td>
<td align="right">41,340</td>
<td align="right">49.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">2,360</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.0%</td>
<td align="right">1,040</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.2%</td>
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
<td align="right">48,290,080</td>
<td align="right">100.0%</td>
<td align="right">48,290,080</td>
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
<td align="right">360</td>
<td align="right">100.0%</td>
<td align="right">360</td>
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
<td align="right">320,513,920</td>
<td align="right">5.6%</td>
<td align="right">327,525,220</td>
<td align="right">5.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">162,586,080</td>
<td align="right">2.9%</td>
<td align="right">165,653,740</td>
<td align="right">2.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,376,266,080</td>
<td align="right">59.5%</td>
<td align="right">3,437,486,700</td>
<td align="right">59.5%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,817,875,240</td>
<td align="right">32.0%</td>
<td align="right">1,842,155,060</td>
<td align="right">31.9%</td>
<td align="right">1.3%</td>
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
<td align="right">1,663,640</td>
<td align="right">1.0%</td>
<td align="right">1,525,280</td>
<td align="right">0.9%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">88,495,820</td>
<td align="right">54.7%</td>
<td align="right">91,933,880</td>
<td align="right">55.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,463,840</td>
<td align="right">1.5%</td>
<td align="right">2,553,680</td>
<td align="right">1.5%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,576,780</td>
<td align="right">7.2%</td>
<td align="right">11,355,480</td>
<td align="right">6.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,845,320</td>
<td align="right">9.8%</td>
<td align="right">15,677,560</td>
<td align="right">9.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,066,020</td>
<td align="right">9.9%</td>
<td align="right">16,200,180</td>
<td align="right">9.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,957,440</td>
<td align="right">3.1%</td>
<td align="right">4,922,000</td>
<td align="right">3.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,431,820</td>
<td align="right">4.0%</td>
<td align="right">6,403,240</td>
<td align="right">3.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,662,500</td>
<td align="right">6.0%</td>
<td align="right">9,669,280</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,578,000</td>
<td align="right">2.8%</td>
<td align="right">4,577,980</td>
<td align="right">2.8%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">22,802,820</td>
<td align="right">7.1%</td>
<td align="right">25,728,740</td>
<td align="right">7.9%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,456,740</td>
<td align="right">2.0%</td>
<td align="right">7,120,020</td>
<td align="right">2.2%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">42,770,720</td>
<td align="right">13.3%</td>
<td align="right">46,204,200</td>
<td align="right">14.1%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">66,550,240</td>
<td align="right">20.8%</td>
<td align="right">69,077,680</td>
<td align="right">21.1%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">79,969,660</td>
<td align="right">24.9%</td>
<td align="right">78,200,920</td>
<td align="right">23.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,906,820</td>
<td align="right">3.4%</td>
<td align="right">10,758,440</td>
<td align="right">3.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,907,940</td>
<td align="right">3.4%</td>
<td align="right">10,759,580</td>
<td align="right">3.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,085,320</td>
<td align="right">2.8%</td>
<td align="right">8,964,900</td>
<td align="right">2.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,981,260</td>
<td align="right">1.2%</td>
<td align="right">3,933,840</td>
<td align="right">1.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,910,480</td>
<td align="right">16.8%</td>
<td align="right">53,912,180</td>
<td align="right">16.5%</td>
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
<td align="right">8,074,740</td>
<td align="right">2.3%</td>
<td align="right">7,989,480</td>
<td align="right">2.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">38,917,680</td>
<td align="right">11.0%</td>
<td align="right">38,828,980</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">38,921,160</td>
<td align="right">11.0%</td>
<td align="right">38,832,460</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,229,020</td>
<td align="right">11.1%</td>
<td align="right">39,140,320</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,229,020</td>
<td align="right">11.1%</td>
<td align="right">39,140,320</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">315,166,800</td>
<td align="right">88.9%</td>
<td align="right">315,255,500</td>
<td align="right">89.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,620,060</td>
<td align="right">88.5%</td>
<td align="right">313,623,500</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,629,300</td>
<td align="right">3.8%</td>
<td align="right">13,629,300</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,880</td>
<td align="right">0.5%</td>
<td align="right">1,826,880</td>
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
<td align="right">9,598,440</td>
<td align="right">2.7%</td>
<td align="right">9,598,440</td>
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
<td align="right">3,669,860</td>
<td align="right"></td>
<td align="right">2,554,969</td>
<td align="right"></td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">42,251,021</td>
<td align="right"></td>
<td align="right">37,948,436</td>
<td align="right"></td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">39,342,069</td>
<td align="right"></td>
<td align="right">36,154,340</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">869,456,040</td>
<td align="right">10.0%</td>
<td align="right">894,890,940</td>
<td align="right">10.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">916,563,240</td>
<td align="right">9.8%</td>
<td align="right">934,790,220</td>
<td align="right">10.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,947,114,903</td>
<td align="right">22.3%</td>
<td align="right">1,917,023,977</td>
<td align="right">22.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,950,311,532</td>
<td align="right">20.8%</td>
<td align="right">1,929,906,239</td>
<td align="right">20.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,506,091,040</td>
<td align="right">28.7%</td>
<td align="right">2,530,430,260</td>
<td align="right">29.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,120,623,968</td>
<td align="right">33.4%</td>
<td align="right">3,091,671,529</td>
<td align="right">33.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,394,219,156</td>
<td align="right">38.9%</td>
<td align="right">3,364,276,406</td>
<td align="right">38.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,369,328,320</td>
<td align="right">36.0%</td>
<td align="right">3,392,846,620</td>
<td align="right">36.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">455,985,291</td>
<td align="right"></td>
<td align="right">458,970,520</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">195,554,140</td>
<td align="right"></td>
<td align="right">196,337,231</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">694,120</td>
<td align="right">0.1%</td>
<td align="right">692,040</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">346,320</td>
<td align="right">0.0%</td>
<td align="right">345,880</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">607,778,671</td>
<td align="right"></td>
<td align="right">607,859,027</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,797,500</td>
<td align="right">29.3%</td>
<td align="right">236,776,420</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,773,180</td>
<td align="right"></td>
<td align="right">236,757,480</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">570,936,120</td>
<td align="right">70.6%</td>
<td align="right">570,954,700</td>
<td align="right">70.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">571,976,560</td>
<td align="right">70.7%</td>
<td align="right">571,992,620</td>
<td align="right">70.7%</td>
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
<td align="right">25,940</td>
<td align="right">72,670,480</td>
<td align="right">1,461,848,160</td>
<td align="right">25,940</td>
<td align="right">72,734,100</td>
<td align="right">1,453,149,320</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">9,140</td>
<td align="right">2.3%</td>
<td align="right">7,140</td>
<td align="right">1.8%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,380</td>
<td align="right">0.4%</td>
<td align="right">1,540</td>
<td align="right">0.4%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,060</td>
<td align="right">0.5%</td>
<td align="right">2,140</td>
<td align="right">0.5%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">105,640</td>
<td align="right">27.0%</td>
<td align="right">108,720</td>
<td align="right">27.6%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">7,087,674,160</td>
<td align="right">1,255.7%</td>
<td align="right">6,931,678,800</td>
<td align="right">1,240.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">134,020</td>
<td align="right">34.3%</td>
<td align="right">136,000</td>
<td align="right">34.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">7,180</td>
<td align="right">1.8%</td>
<td align="right">7,100</td>
<td align="right">1.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">564,459,940</td>
<td align="right"></td>
<td align="right">558,953,880</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">390,620</td>
<td align="right"></td>
<td align="right">393,240</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">283,600</td>
<td align="right">72.6%</td>
<td align="right">282,980</td>
<td align="right">72.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">267,140</td>
<td align="right">94.2%</td>
<td align="right">265,600</td>
<td align="right">93.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">283,600</td>
<td align="right"></td>
<td align="right">282,980</td>
<td align="right"></td>
<td align="right">-0.2%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">12,920</td>
<td align="right">4.6%</td>
<td align="right">13,520</td>
<td align="right">4.8%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">39,680</td>
<td align="right">14.0%</td>
<td align="right">40,280</td>
<td align="right">14.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">93,760</td>
<td align="right">33.1%</td>
<td align="right">91,260</td>
<td align="right">32.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">86,240</td>
<td align="right">30.4%</td>
<td align="right">82,500</td>
<td align="right">29.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">40,120</td>
<td align="right">14.1%</td>
<td align="right">44,780</td>
<td align="right">15.8%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">8,760</td>
<td align="right">3.1%</td>
<td align="right">8,540</td>
<td align="right">3.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,020</td>
<td align="right">0.7%</td>
<td align="right">1,960</td>
<td align="right">0.7%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
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
<td align="right">7,780</td>
<td align="right">2.7%</td>
<td align="right">7,660</td>
<td align="right">2.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">27,460</td>
<td align="right">9.7%</td>
<td align="right">27,880</td>
<td align="right">9.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51,700</td>
<td align="right">18.2%</td>
<td align="right">53,220</td>
<td align="right">18.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">109,440</td>
<td align="right">38.6%</td>
<td align="right">105,500</td>
<td align="right">37.3%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">52,100</td>
<td align="right">18.4%</td>
<td align="right">51,760</td>
<td align="right">18.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">15,160</td>
<td align="right">5.3%</td>
<td align="right">15,940</td>
<td align="right">5.6%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,000</td>
<td align="right">1.1%</td>
<td align="right">3,060</td>
<td align="right">1.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">500</td>
<td align="right">0.2%</td>
<td align="right">580</td>
<td align="right">0.2%</td>
<td align="right">16.0%</td>
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
<td align="left">_CALL_TUPLE_1</td>
<td align="right">100</td>
<td align="right">520</td>
<td align="right">420.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">23,120</td>
<td align="right">61,960</td>
<td align="right">168.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">644,120</td>
<td align="right">39,080</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">102,280</td>
<td align="right">187,660</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">335,680</td>
<td align="right">598,920</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">14,391,940</td>
<td align="right">6,674,860</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">9,874,580</td>
<td align="right">5,544,380</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">45,377,340</td>
<td align="right">27,940,560</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">6,921,660</td>
<td align="right">4,476,120</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,651,620</td>
<td align="right">2,498,900</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">19,700</td>
<td align="right">25,860</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">19,700</td>
<td align="right">25,860</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">222,520</td>
<td align="right">289,400</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">222,520</td>
<td align="right">289,400</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">16,450,120</td>
<td align="right">12,396,200</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">30,291,600</td>
<td align="right">23,274,860</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">779,120</td>
<td align="right">919,720</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">43,120,780</td>
<td align="right">35,415,500</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">55,933,260</td>
<td align="right">46,016,880</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">12,242,580</td>
<td align="right">10,388,860</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">25,576,180</td>
<td align="right">21,832,580</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">40,600,760</td>
<td align="right">34,707,740</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,926,620</td>
<td align="right">4,492,500</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">485,480</td>
<td align="right">554,640</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">26,034,720</td>
<td align="right">22,358,040</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">35,274,500</td>
<td align="right">30,411,080</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">34,503,560</td>
<td align="right">29,880,380</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,311,800</td>
<td align="right">1,474,940</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,311,800</td>
<td align="right">1,474,940</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,280</td>
<td align="right">2,560</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,183,920</td>
<td align="right">9,168,020</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,341,080</td>
<td align="right">1,493,500</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,474,220</td>
<td align="right">4,976,700</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,802,140</td>
<td align="right">1,997,480</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">52,636,760</td>
<td align="right">58,111,780</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">26,130,340</td>
<td align="right">23,416,580</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">810,360</td>
<td align="right">894,120</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,524,700</td>
<td align="right">1,677,720</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,518,620</td>
<td align="right">3,176,060</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">122,133,660</td>
<td align="right">110,362,140</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">8,067,400</td>
<td align="right">8,834,680</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">89,404,440</td>
<td align="right">80,983,760</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">65,334,080</td>
<td align="right">59,279,600</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,364,040</td>
<td align="right">1,474,400</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">29,265,760</td>
<td align="right">26,923,860</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">40,035,920</td>
<td align="right">36,926,980</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">116,398,700</td>
<td align="right">125,430,740</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">47,274,420</td>
<td align="right">43,722,540</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">30,919,360</td>
<td align="right">28,622,440</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">119,167,320</td>
<td align="right">110,867,940</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">492,560</td>
<td align="right">525,880</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">31,314,780</td>
<td align="right">33,413,460</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">5,957,880</td>
<td align="right">6,330,520</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,187,980</td>
<td align="right">6,515,080</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">38,024,080</td>
<td align="right">40,029,920</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">199,328,140</td>
<td align="right">188,913,480</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,476,000</td>
<td align="right">15,218,920</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">47,066,400</td>
<td align="right">49,281,160</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">463,283,920</td>
<td align="right">442,512,800</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">54,115,680</td>
<td align="right">56,538,400</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,781,200</td>
<td align="right">1,855,140</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">108,091,280</td>
<td align="right">112,366,380</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">108,083,060</td>
<td align="right">112,345,920</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,951,920</td>
<td align="right">7,214,100</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,277,580</td>
<td align="right">6,511,080</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,905,600</td>
<td align="right">46,523,540</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">10,450,960</td>
<td align="right">10,825,980</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,334,060</td>
<td align="right">6,557,240</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">107,320</td>
<td align="right">111,000</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">133,460,960</td>
<td align="right">128,953,400</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">95,945,020</td>
<td align="right">99,094,100</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">39,614,140</td>
<td align="right">38,334,040</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,181,980</td>
<td align="right">2,251,060</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">40,246,060</td>
<td align="right">39,004,860</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,491,940</td>
<td align="right">6,690,700</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">42,980</td>
<td align="right">41,680</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">565,864,340</td>
<td align="right">549,045,180</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,444,560</td>
<td align="right">35,414,540</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,301,360</td>
<td align="right">15,705,260</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,372,240</td>
<td align="right">15,768,620</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">63,486,260</td>
<td align="right">61,879,880</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">43,618,860</td>
<td align="right">44,709,720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,828,600</td>
<td align="right">10,562,940</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">103,841,640</td>
<td align="right">106,345,720</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">35,676,020</td>
<td align="right">36,526,240</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">512,480,600</td>
<td align="right">524,643,720</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">17,600,380</td>
<td align="right">18,013,280</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,476,080</td>
<td align="right">9,697,380</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">443,100,080</td>
<td align="right">432,774,900</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,050,620</td>
<td align="right">10,284,660</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,825,020</td>
<td align="right">1,865,940</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,026,040</td>
<td align="right">5,891,880</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,453,600</td>
<td align="right">4,551,040</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">36,040,720</td>
<td align="right">36,816,720</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">71,252,880</td>
<td align="right">69,728,400</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,146,240</td>
<td align="right">10,362,100</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,461,980</td>
<td align="right">3,530,760</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">52,133,180</td>
<td align="right">51,119,080</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">77,053,620</td>
<td align="right">75,612,020</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">75,398,920</td>
<td align="right">74,005,880</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">42,321,660</td>
<td align="right">43,091,460</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,966,080</td>
<td align="right">13,713,280</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">110,502,000</td>
<td align="right">108,693,060</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,488,720</td>
<td align="right">5,577,480</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">26,560</td>
<td align="right">26,980</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">30,000</td>
<td align="right">30,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,764,480</td>
<td align="right">22,436,020</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">250,958,040</td>
<td align="right">247,386,760</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">236,300</td>
<td align="right">233,260</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">72,858,800</td>
<td align="right">73,770,340</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,095,720</td>
<td align="right">4,045,480</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,115,660</td>
<td align="right">2,141,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,115,660</td>
<td align="right">2,141,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,297,420</td>
<td align="right">18,510,580</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,343,380</td>
<td align="right">5,405,240</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">470,380</td>
<td align="right">465,240</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,335,640</td>
<td align="right">9,433,020</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">256,280</td>
<td align="right">253,780</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">564,459,940</td>
<td align="right">558,953,880</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">311,140</td>
<td align="right">308,440</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,488,320</td>
<td align="right">16,603,140</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,200,820</td>
<td align="right">16,312,040</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,200,820</td>
<td align="right">16,312,040</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,651,360</td>
<td align="right">13,743,060</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,151,660</td>
<td align="right">9,211,280</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">342,580</td>
<td align="right">340,420</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,245,960</td>
<td align="right">4,271,280</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,432,260</td>
<td align="right">15,522,160</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,308,540</td>
<td align="right">1,315,900</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,478,760</td>
<td align="right">12,548,900</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">611,526,340</td>
<td align="right">608,235,040</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,667,000</td>
<td align="right">5,695,580</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,235,820</td>
<td align="right">7,271,260</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,231,860</td>
<td align="right">2,242,340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,230,840</td>
<td align="right">2,241,260</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,960,940</td>
<td align="right">35,833,560</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">501,940</td>
<td align="right">503,700</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,860</td>
<td align="right">5,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">961,300</td>
<td align="right">958,040</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">208,420</td>
<td align="right">207,720</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,420</td>
<td align="right">7,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,826,060</td>
<td align="right">16,866,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">990,060</td>
<td align="right">987,820</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">990,060</td>
<td align="right">987,820</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">262,020</td>
<td align="right">262,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">842,660</td>
<td align="right">841,360</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,745,880</td>
<td align="right">1,748,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,207,580</td>
<td align="right">14,222,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,155,160</td>
<td align="right">17,172,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,367,880</td>
<td align="right">16,384,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,474,640</td>
<td align="right">47,519,240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">859,560</td>
<td align="right">858,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,646,400</td>
<td align="right">1,645,020</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">208,960</td>
<td align="right">208,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">102,304,700</td>
<td align="right">102,375,740</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,363,920</td>
<td align="right">3,366,240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">56,260,140</td>
<td align="right">56,223,020</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,271,740</td>
<td align="right">4,269,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,611,860</td>
<td align="right">18,620,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">694,340</td>
<td align="right">694,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,012,020</td>
<td align="right">4,012,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,802,480</td>
<td align="right">2,802,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,142,960</td>
<td align="right">3,143,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,142,960</td>
<td align="right">3,143,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,600</td>
<td align="right">699,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,740</td>
<td align="right">324,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">309,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,580</td>
<td align="right">263,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right">242,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right">63,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">200</td>
<td align="right"></td>
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
<td align="right">3,780</td>
<td align="right">3,540</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">9,180</td>
<td align="right">8,760</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,460</td>
<td align="right">1,520</td>
<td align="right">4.1%</td>
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
Stats gathered on: 2024-10-18
