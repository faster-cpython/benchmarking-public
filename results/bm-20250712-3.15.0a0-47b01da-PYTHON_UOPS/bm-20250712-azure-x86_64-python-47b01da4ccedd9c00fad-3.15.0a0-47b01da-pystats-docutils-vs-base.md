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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">208,791,640</td>
<td align="right">68,680</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,813,300</td>
<td align="right">2,527,880</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">54,460,260</td>
<td align="right">13,706,100</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">18,049,040</td>
<td align="right">4,940,740</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">17,098,160</td>
<td align="right">5,252,780</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">20,338,820</td>
<td align="right">6,869,740</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,399,880</td>
<td align="right">5,111,940</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">48,517,840</td>
<td align="right">22,730,180</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,433,460</td>
<td align="right">22,546,920</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">69,544,460</td>
<td align="right">35,246,480</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,949,680</td>
<td align="right">15,246,660</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">30,399,720</td>
<td align="right">17,747,200</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">41,807,640</td>
<td align="right">24,934,160</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">134,362,600</td>
<td align="right">80,855,320</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">58,389,360</td>
<td align="right">35,298,800</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">34,104,240</td>
<td align="right">20,619,860</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">50,503,240</td>
<td align="right">30,600,060</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">374,680</td>
<td align="right">237,140</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">166,062,760</td>
<td align="right">110,487,700</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,066,480</td>
<td align="right">9,545,860</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">69,688,580</td>
<td align="right">48,622,900</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">51,411,720</td>
<td align="right">37,065,160</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,485,200</td>
<td align="right">9,021,820</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">443,896,180</td>
<td align="right">322,768,020</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">253,406,480</td>
<td align="right">185,310,840</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">15,261,020</td>
<td align="right">11,440,040</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">147,919,380</td>
<td align="right">113,422,620</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,879,940</td>
<td align="right">3,002,180</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">44,192,080</td>
<td align="right">34,534,000</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,577,500</td>
<td align="right">10,828,580</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,382,700</td>
<td align="right">12,294,060</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">255,909,780</td>
<td align="right">207,498,760</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">64,973,180</td>
<td align="right">52,760,080</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">7,203,520</td>
<td align="right">5,869,400</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">94,655,560</td>
<td align="right">77,388,980</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">22,416,620</td>
<td align="right">18,442,200</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">94,711,120</td>
<td align="right">78,120,400</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">382,456,160</td>
<td align="right">316,563,340</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,454,761,780</td>
<td align="right">1,207,635,000</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">59,228,020</td>
<td align="right">49,479,580</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">67,857,020</td>
<td align="right">56,896,400</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,819,800</td>
<td align="right">10,767,220</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,155,180</td>
<td align="right">20,318,160</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">41,575,480</td>
<td align="right">35,009,780</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">37,748,600</td>
<td align="right">32,184,080</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">169,502,640</td>
<td align="right">145,807,520</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">226,696,640</td>
<td align="right">195,915,340</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">106,000</td>
<td align="right">92,580</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,205,780</td>
<td align="right">7,299,080</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">866,460</td>
<td align="right">778,020</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">28,197,820</td>
<td align="right">25,421,760</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">837,080</td>
<td align="right">754,700</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">29,848,360</td>
<td align="right">26,991,440</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">22,141,800</td>
<td align="right">20,087,420</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">53,071,960</td>
<td align="right">48,183,400</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">224,171,380</td>
<td align="right">204,633,540</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">958,860</td>
<td align="right">876,480</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,488,280</td>
<td align="right">5,034,020</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,067,820</td>
<td align="right">979,660</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,148,880</td>
<td align="right">4,726,360</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,925,920</td>
<td align="right">2,687,280</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">800,620</td>
<td align="right">736,780</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">41,537,960</td>
<td align="right">38,236,100</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">110,234,580</td>
<td align="right">101,547,420</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,594,480</td>
<td align="right">5,161,240</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">71,298,340</td>
<td align="right">65,996,700</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">131,682,560</td>
<td align="right">121,899,640</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">23,262,280</td>
<td align="right">21,589,380</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">318,589,080</td>
<td align="right">299,806,700</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">398,680,320</td>
<td align="right">380,829,680</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">155,617,180</td>
<td align="right">150,642,360</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,770,540</td>
<td align="right">1,826,020</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,493,920</td>
<td align="right">2,418,800</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">195,986,320</td>
<td align="right">191,242,560</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,228,000</td>
<td align="right">3,152,880</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">311,219,440</td>
<td align="right">304,157,460</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,149,780</td>
<td align="right">4,061,320</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">118,839,260</td>
<td align="right">116,444,080</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">123,164,580</td>
<td align="right">120,689,040</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,911,060</td>
<td align="right">4,833,880</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,447,220</td>
<td align="right">51,681,880</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,736,160</td>
<td align="right">2,699,300</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,283,960</td>
<td align="right">19,036,580</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,250,020</td>
<td align="right">17,035,940</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,467,000</td>
<td align="right">3,433,180</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">180,825,540</td>
<td align="right">179,234,400</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,409,640</td>
<td align="right">19,280,800</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,912,920</td>
<td align="right">8,865,160</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,212,720</td>
<td align="right">30,078,320</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,232,640</td>
<td align="right">30,098,240</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,972,540</td>
<td align="right">7,938,860</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,623,240</td>
<td align="right">16,576,000</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,932,940</td>
<td align="right">5,917,340</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,073,460</td>
<td align="right">93,827,400</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">23,208,140</td>
<td align="right">23,181,080</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,411,240</td>
<td align="right">23,398,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">41,711,760</td>
<td align="right">41,711,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,801,180</td>
<td align="right">38,801,180</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">22,179,680</td>
<td align="right">22,179,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,122,620</td>
<td align="right">15,122,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,642,980</td>
<td align="right">11,642,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,498,680</td>
<td align="right">11,498,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,321,600</td>
<td align="right">10,321,600</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">4,214,560</td>
<td align="right">4,214,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,867,260</td>
<td align="right">2,867,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,737,680</td>
<td align="right">2,737,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,734,060</td>
<td align="right">2,734,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,888,040</td>
<td align="right">1,888,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,447,500</td>
<td align="right">1,447,500</td>
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
<td align="right">389,320</td>
<td align="right">389,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,280</td>
<td align="right">267,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">247,440</td>
<td align="right">247,440</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">134,360</td>
<td align="right">134,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">128,720</td>
<td align="right">128,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">92,060</td>
<td align="right">92,060</td>
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
<td align="left">MAP_ADD</td>
<td align="right">77,900</td>
<td align="right">77,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">74,180</td>
<td align="right">74,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">60,540</td>
<td align="right">60,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">42,900</td>
<td align="right">42,900</td>
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
<td align="right">30,620</td>
<td align="right">30,620</td>
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
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">15,620</td>
<td align="right">15,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">12,740</td>
<td align="right">12,740</td>
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
<td align="right">5,840</td>
<td align="right">5,840</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">94,995,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">43,139,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">679,900</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,103,640</td>
<td align="right">85.5%</td>
<td align="right">141,377,340</td>
<td align="right">83.2%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">23,266,580</td>
<td align="right">11.8%</td>
<td align="right">23,253,820</td>
<td align="right">13.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">3.1%</td>
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
<td align="right">117,160</td>
<td align="right">48.2%</td>
<td align="right">117,160</td>
<td align="right">48.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">125,880</td>
<td align="right">51.8%</td>
<td align="right">125,880</td>
<td align="right">51.8%</td>
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
<td align="left">subscr tuple slice</td>
<td align="right">82,900</td>
<td align="right">65.9%</td>
<td align="right">82,900</td>
<td align="right">65.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">10,280</td>
<td align="right">8.2%</td>
<td align="right">10,280</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,240</td>
<td align="right">8.1%</td>
<td align="right">10,240</td>
<td align="right">8.1%</td>
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
<td align="left">add other</td>
<td align="right">8,480</td>
<td align="right">6.7%</td>
<td align="right">8,480</td>
<td align="right">6.7%</td>
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
<td align="left">subscr</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">760</td>
<td align="right">0.6%</td>
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
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
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
<td align="right">12,819,800</td>
<td align="right">100.0%</td>
<td align="right">10,767,220</td>
<td align="right">100.0%</td>
<td align="right">-16.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">555,830,860</td>
<td align="right">96.9%</td>
<td align="right">484,441,560</td>
<td align="right">96.4%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">17,842,160</td>
<td align="right">3.1%</td>
<td align="right">17,751,740</td>
<td align="right">3.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,576,740</td>
<td align="right">3.1%</td>
<td align="right">17,488,020</td>
<td align="right">3.5%</td>
<td align="right">-0.5%</td>
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
<td align="right">394,140</td>
<td align="right">100.0%</td>
<td align="right">392,440</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">255,400</td>
<td align="right">0.7%</td>
<td align="right">195,820</td>
<td align="right">0.6%</td>
<td align="right">-23.3%</td>
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
<td align="right">29,076,860</td>
<td align="right">93.5%</td>
<td align="right">-18.6%</td>
</tr>
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
<td align="right">1,807,480</td>
<td align="right">5.8%</td>
<td align="right">3.3%</td>
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
<td align="right">13,260</td>
<td align="right">59.7%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,080</td>
<td align="right">38.9%</td>
<td align="right">8,940</td>
<td align="right">40.3%</td>
<td align="right">-11.3%</td>
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
<td align="right">11,080</td>
<td align="right">83.6%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">640</td>
<td align="right">4.1%</td>
<td align="right">640</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">600</td>
<td align="right">3.8%</td>
<td align="right">600</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">360</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">2.2%</td>
<td align="right">340</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.3%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,707,700</td>
<td align="right">81.4%</td>
<td align="right">13,953,540</td>
<td align="right">60.7%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,467,160</td>
<td align="right">18.6%</td>
<td align="right">9,004,620</td>
<td align="right">39.2%</td>
<td align="right">-27.8%</td>
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
<td align="right">16,360</td>
<td align="right">90.7%</td>
<td align="right">15,520</td>
<td align="right">90.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,680</td>
<td align="right">9.3%</td>
<td align="right">1,680</td>
<td align="right">9.8%</td>
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
<td align="right">3,280</td>
<td align="right">20.0%</td>
<td align="right">2,880</td>
<td align="right">18.6%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">6,180</td>
<td align="right">37.8%</td>
<td align="right">5,800</td>
<td align="right">37.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,140</td>
<td align="right">25.3%</td>
<td align="right">4,080</td>
<td align="right">26.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,760</td>
<td align="right">16.9%</td>
<td align="right">2,760</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,409,580</td>
<td align="right">13.9%</td>
<td align="right">22,528,620</td>
<td align="right">10.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">243,414,960</td>
<td align="right">74.5%</td>
<td align="right">157,451,200</td>
<td align="right">73.9%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,783,960</td>
<td align="right">11.6%</td>
<td align="right">32,996,920</td>
<td align="right">15.5%</td>
<td align="right">-12.7%</td>
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
<td align="right">19,260</td>
<td align="right">2.6%</td>
<td align="right">13,680</td>
<td align="right">2.1%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">717,460</td>
<td align="right">97.4%</td>
<td align="right">627,140</td>
<td align="right">97.9%</td>
<td align="right">-12.6%</td>
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
<td align="right">2,200</td>
<td align="right">11.4%</td>
<td align="right">1,040</td>
<td align="right">7.6%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,620</td>
<td align="right">29.2%</td>
<td align="right">2,720</td>
<td align="right">19.9%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">5.0%</td>
<td align="right">600</td>
<td align="right">4.4%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">3,140</td>
<td align="right">16.3%</td>
<td align="right">2,380</td>
<td align="right">17.4%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,980</td>
<td align="right">15.5%</td>
<td align="right">2,600</td>
<td align="right">19.0%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,440</td>
<td align="right">12.7%</td>
<td align="right">2,420</td>
<td align="right">17.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,000</td>
<td align="right">5.2%</td>
<td align="right">1,000</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">1.1%</td>
<td align="right">220</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">332,138,380</td>
<td align="right">30.1%</td>
<td align="right">274,110,840</td>
<td align="right">28.8%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">661,096,980</td>
<td align="right">59.9%</td>
<td align="right">574,511,480</td>
<td align="right">60.5%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,459,200</td>
<td align="right">9.9%</td>
<td align="right">100,788,720</td>
<td align="right">10.6%</td>
<td align="right">-7.9%</td>
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
<td align="right">6,287,440</td>
<td align="right">99.4%</td>
<td align="right">5,192,800</td>
<td align="right">99.3%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,360</td>
<td align="right">0.6%</td>
<td align="right">35,420</td>
<td align="right">0.7%</td>
<td align="right">-5.2%</td>
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
<td align="right">13,120</td>
<td align="right">35.1%</td>
<td align="right">11,940</td>
<td align="right">33.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">10,260</td>
<td align="right">27.5%</td>
<td align="right">9,500</td>
<td align="right">26.8%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,200</td>
<td align="right">8.6%</td>
<td align="right">3,200</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,380</td>
<td align="right">6.4%</td>
<td align="right">2,380</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,220</td>
<td align="right">3.3%</td>
<td align="right">1,220</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,020</td>
<td align="right">2.7%</td>
<td align="right">1,020</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">560</td>
<td align="right">1.5%</td>
<td align="right">560</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">500</td>
<td align="right">1.3%</td>
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
<td align="right">321,324,680</td>
<td align="right">100.0%</td>
<td align="right">273,276,800</td>
<td align="right">100.0%</td>
<td align="right">-15.0%</td>
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
<td align="right">27,520</td>
<td align="right">0.0%</td>
<td align="right">27,520</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,896,440</td>
<td align="right">43.5%</td>
<td align="right">53,718,160</td>
<td align="right">43.5%</td>
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
<td align="right">47,797,740</td>
<td align="right">38.6%</td>
<td align="right">47,729,960</td>
<td align="right">38.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">22,137,900</td>
<td align="right">17.9%</td>
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
<td align="right">1,025,960</td>
<td align="right">97.0%</td>
<td align="right">1,022,600</td>
<td align="right">97.0%</td>
<td align="right">-0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,671,940</td>
<td align="right">89.7%</td>
<td align="right">25,710,020</td>
<td align="right">84.2%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,898,600</td>
<td align="right">10.3%</td>
<td align="right">4,821,420</td>
<td align="right">15.8%</td>
<td align="right">-1.6%</td>
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
<td align="left">Success</td>
<td align="right">2,220</td>
<td align="right">17.8%</td>
<td align="right">2,220</td>
<td align="right">17.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">10,280</td>
<td align="right">82.2%</td>
<td align="right">10,280</td>
<td align="right">82.2%</td>
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
<td align="right">7,220</td>
<td align="right">70.2%</td>
<td align="right">7,220</td>
<td align="right">70.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,540</td>
<td align="right">15.0%</td>
<td align="right">1,540</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">700</td>
<td align="right">6.8%</td>
<td align="right">700</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">600</td>
<td align="right">5.8%</td>
<td align="right">600</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">220</td>
<td align="right">2.1%</td>
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
<td align="right">11,332,880</td>
<td align="right">4.0%</td>
<td align="right">8,399,600</td>
<td align="right">3.6%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">270,225,240</td>
<td align="right">94.6%</td>
<td align="right">220,136,600</td>
<td align="right">94.6%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,963,200</td>
<td align="right">1.4%</td>
<td align="right">3,874,760</td>
<td align="right">1.7%</td>
<td align="right">-2.2%</td>
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
<td align="right">229,000</td>
<td align="right">57.3%</td>
<td align="right">173,680</td>
<td align="right">50.5%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">170,380</td>
<td align="right">42.7%</td>
<td align="right">170,360</td>
<td align="right">49.5%</td>
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
<td align="right">5,700</td>
<td align="right">3.3%</td>
<td align="right">5,680</td>
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
<td align="right">24.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,552,100</td>
<td align="right">100.0%</td>
<td align="right">22,777,860</td>
<td align="right">100.0%</td>
<td align="right">-53.1%</td>
</tr>
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
<td align="right">3,039,647,240</td>
<td align="right">36.2%</td>
<td align="right">2,422,287,320</td>
<td align="right">34.5%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">4,548,284,360</td>
<td align="right">54.1%</td>
<td align="right">3,886,529,280</td>
<td align="right">55.3%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">458,519,620</td>
<td align="right">5.5%</td>
<td align="right">392,443,920</td>
<td align="right">5.6%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">361,031,140</td>
<td align="right">4.3%</td>
<td align="right">321,343,020</td>
<td align="right">4.6%</td>
<td align="right">-11.0%</td>
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
<td align="right">45,409,580</td>
<td align="right">17.9%</td>
<td align="right">22,528,620</td>
<td align="right">10.4%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,467,160</td>
<td align="right">4.9%</td>
<td align="right">9,004,620</td>
<td align="right">4.2%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,819,800</td>
<td align="right">5.0%</td>
<td align="right">10,767,220</td>
<td align="right">5.0%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">109,459,200</td>
<td align="right">43.1%</td>
<td align="right">100,788,720</td>
<td align="right">46.5%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,749,440</td>
<td align="right">0.7%</td>
<td align="right">1,807,480</td>
<td align="right">0.8%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,963,200</td>
<td align="right">1.6%</td>
<td align="right">3,874,760</td>
<td align="right">1.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,898,600</td>
<td align="right">1.9%</td>
<td align="right">4,821,420</td>
<td align="right">2.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,576,740</td>
<td align="right">6.9%</td>
<td align="right">17,488,020</td>
<td align="right">8.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,266,580</td>
<td align="right">9.2%</td>
<td align="right">23,253,820</td>
<td align="right">10.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,137,900</td>
<td align="right">8.7%</td>
<td align="right">22,137,900</td>
<td align="right">10.2%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">132,970,220</td>
<td align="right">29.0%</td>
<td align="right">100,828,240</td>
<td align="right">25.7%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,093,000</td>
<td align="right">1.3%</td>
<td align="right">4,623,100</td>
<td align="right">1.2%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,675,160</td>
<td align="right">22.0%</td>
<td align="right">84,983,300</td>
<td align="right">21.7%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,325,500</td>
<td align="right">7.7%</td>
<td align="right">30,530,620</td>
<td align="right">7.8%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">18,890,900</td>
<td align="right">4.1%</td>
<td align="right">16,497,420</td>
<td align="right">4.2%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,893,060</td>
<td align="right">4.1%</td>
<td align="right">16,499,500</td>
<td align="right">4.2%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">51,820,040</td>
<td align="right">11.3%</td>
<td align="right">47,450,460</td>
<td align="right">12.1%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,691,660</td>
<td align="right">2.1%</td>
<td align="right">9,601,240</td>
<td align="right">2.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,893,260</td>
<td align="right">11.8%</td>
<td align="right">53,714,980</td>
<td align="right">13.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,560,280</td>
<td align="right">1.6%</td>
<td align="right">7,560,280</td>
<td align="right">1.9%</td>
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
<td align="right">39,856,500</td>
<td align="right">11.2%</td>
<td align="right">39,856,500</td>
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
<td align="right">39,856,500</td>
<td align="right">11.2%</td>
<td align="right">39,856,500</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,506,260</td>
<td align="right">11.1%</td>
<td align="right">39,506,260</td>
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
<td align="right">5,840</td>
<td align="right">0.0%</td>
<td align="right">5,840</td>
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
<td align="right">314,845,740</td>
<td align="right">88.5%</td>
<td align="right">314,845,740</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">2,208,295</td>
<td align="right"></td>
<td align="right">1,870,259</td>
<td align="right"></td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">39,724,002</td>
<td align="right"></td>
<td align="right">36,733,940</td>
<td align="right"></td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">38,044,520</td>
<td align="right"></td>
<td align="right">35,394,071</td>
<td align="right"></td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">466,940,540</td>
<td align="right"></td>
<td align="right">451,352,409</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">198,914,545</td>
<td align="right"></td>
<td align="right">194,362,361</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,971,490,414</td>
<td align="right">37.1%</td>
<td align="right">1,939,754,663</td>
<td align="right">36.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,273,426,481</td>
<td align="right">22.8%</td>
<td align="right">1,255,030,707</td>
<td align="right">22.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,390,277,108</td>
<td align="right">26.2%</td>
<td align="right">1,371,824,675</td>
<td align="right">26.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">527,560</td>
<td align="right">0.1%</td>
<td align="right">532,820</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,733,466,780</td>
<td align="right">32.6%</td>
<td align="right">1,743,507,420</td>
<td align="right">33.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,471,580,500</td>
<td align="right">44.3%</td>
<td align="right">2,458,294,560</td>
<td align="right">44.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,740,957,719</td>
<td align="right">31.2%</td>
<td align="right">1,732,575,129</td>
<td align="right">31.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">349,340</td>
<td align="right">0.1%</td>
<td align="right">350,160</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">218,930,680</td>
<td align="right">4.1%</td>
<td align="right">219,105,600</td>
<td align="right">4.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,811,480</td>
<td align="right">1.6%</td>
<td align="right">90,842,460</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">308,478,320</td>
<td align="right"></td>
<td align="right">308,520,600</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">308,431,720</td>
<td align="right">51.3%</td>
<td align="right">308,466,280</td>
<td align="right">51.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,870,400</td>
<td align="right">48.5%</td>
<td align="right">291,838,540</td>
<td align="right">48.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">323,379,297</td>
<td align="right"></td>
<td align="right">323,346,968</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,747,300</td>
<td align="right">48.7%</td>
<td align="right">292,721,520</td>
<td align="right">48.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">70,283,660</td>
<td align="right">1,130,566,066</td>
<td align="right">43,087,940</td>
<td align="right">97,763,340</td>
<td align="right">26,100</td>
<td align="right">70,295,060</td>
<td align="right">1,127,459,926</td>
<td align="right">43,519,540</td>
<td align="right">97,630,880</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-14
