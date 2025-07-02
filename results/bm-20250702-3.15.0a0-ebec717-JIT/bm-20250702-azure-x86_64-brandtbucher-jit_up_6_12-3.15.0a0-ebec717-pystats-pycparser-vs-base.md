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
<td align="left">STORE_NAME</td>
<td align="right">244,060</td>
<td align="right">15,780</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">16,740</td>
<td align="right">3,940</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">98,760</td>
<td align="right">23,560</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,561,940</td>
<td align="right">549,760</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,054,000</td>
<td align="right">1,221,760</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,940</td>
<td align="right">21,220</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">657,220</td>
<td align="right">302,980</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">22,982,480</td>
<td align="right">10,652,360</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,399,640</td>
<td align="right">11,064,900</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">753,780</td>
<td align="right">382,980</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">35,250,500</td>
<td align="right">18,025,620</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">327,380</td>
<td align="right">168,100</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">13,416,500</td>
<td align="right">6,959,020</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">26,957,640</td>
<td align="right">14,452,720</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">28,197,300</td>
<td align="right">15,337,480</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">11,779,360</td>
<td align="right">6,840,020</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">57,405,240</td>
<td align="right">33,712,680</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">95,601,620</td>
<td align="right">58,542,340</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">33,718,620</td>
<td align="right">21,390,900</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,999,420</td>
<td align="right">2,612,320</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">72,920</td>
<td align="right">49,400</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">2,348,440</td>
<td align="right">3,069,520</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">156,917,560</td>
<td align="right">109,183,040</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">248,847,700</td>
<td align="right">174,912,120</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">44,004,200</td>
<td align="right">31,272,660</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,193,920</td>
<td align="right">1,568,600</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">49,139,100</td>
<td align="right">36,812,340</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">49,147,120</td>
<td align="right">36,820,360</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">19,860,100</td>
<td align="right">15,077,380</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,762,420</td>
<td align="right">14,431,320</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,396,117,460</td>
<td align="right">1,083,325,600</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,485,340</td>
<td align="right">3,040,920</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">181,813,920</td>
<td align="right">145,158,040</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,626,160</td>
<td align="right">1,307,260</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">92,132,660</td>
<td align="right">74,361,140</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">225,673,640</td>
<td align="right">182,511,120</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,050,840</td>
<td align="right">1,676,760</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,660</td>
<td align="right">12,000</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">243,301,240</td>
<td align="right">199,299,340</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,330,260</td>
<td align="right">7,659,680</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">758,700</td>
<td align="right">622,880</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">118,100</td>
<td align="right">97,120</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">27,627,480</td>
<td align="right">22,837,320</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">15,620</td>
<td align="right">12,960</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,666,940</td>
<td align="right">2,216,560</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,760</td>
<td align="right">26,480</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">266,500</td>
<td align="right">223,460</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">246,072,180</td>
<td align="right">206,500,940</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">14,100</td>
<td align="right">11,860</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">27,370,580</td>
<td align="right">23,063,620</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">37,012,060</td>
<td align="right">31,426,820</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,132,640</td>
<td align="right">1,831,300</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">44,684,180</td>
<td align="right">38,413,260</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">27,859,260</td>
<td align="right">31,668,100</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,210,260</td>
<td align="right">1,055,600</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">514,700</td>
<td align="right">449,720</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">50,260</td>
<td align="right">44,180</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">105,380,700</td>
<td align="right">92,949,620</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">801,200</td>
<td align="right">716,840</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,131,680</td>
<td align="right">5,492,120</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">109,640</td>
<td align="right">100,340</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,702,100</td>
<td align="right">1,582,840</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">39,322,460</td>
<td align="right">41,940,040</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">107,382,960</td>
<td align="right">100,290,060</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">79,120,200</td>
<td align="right">73,896,820</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">11,580,820</td>
<td align="right">10,869,400</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,782,420</td>
<td align="right">2,622,180</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,878,640</td>
<td align="right">5,149,940</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,129,520</td>
<td align="right">6,743,460</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,764,400</td>
<td align="right">6,405,780</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,361,920</td>
<td align="right">11,770,540</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,869,360</td>
<td align="right">19,954,240</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">98,720</td>
<td align="right">95,800</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">675,160</td>
<td align="right">656,440</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">35,385,380</td>
<td align="right">34,597,380</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,202,560</td>
<td align="right">11,016,020</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,154,860</td>
<td align="right">4,089,160</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">64,257,640</td>
<td align="right">63,281,840</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,281,880</td>
<td align="right">11,122,600</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">107,195,560</td>
<td align="right">105,785,800</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">182,240</td>
<td align="right">179,880</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,465,640</td>
<td align="right">6,386,000</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">140,627,840</td>
<td align="right">138,905,480</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">47,641,640</td>
<td align="right">47,078,080</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,327,560</td>
<td align="right">38,901,320</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">86,681,920</td>
<td align="right">85,960,520</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">35,365,100</td>
<td align="right">35,156,940</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,703,740</td>
<td align="right">16,622,880</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">7,973,180</td>
<td align="right">7,939,000</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">162,870,320</td>
<td align="right">162,386,740</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">37,500</td>
<td align="right">37,400</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">52,631,660</td>
<td align="right">52,524,040</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,896,740</td>
<td align="right">28,837,980</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,834,220</td>
<td align="right">26,806,500</td>
<td align="right">-0.1%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">8,044,940</td>
<td align="right">8,044,940</td>
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
<td align="left">COPY</td>
<td align="right">2,644,400</td>
<td align="right">2,644,400</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">418,720</td>
<td align="right">418,720</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,200</td>
<td align="right">39,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">32,940</td>
<td align="right">32,940</td>
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
<td align="left">CALL</td>
<td align="right">15,500</td>
<td align="right">15,500</td>
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
<td align="right">28,820,420</td>
<td align="right">6.5%</td>
<td align="right">-0.2%</td>
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
<td align="left">Failure</td>
<td align="right">10,560</td>
<td align="right">59.3%</td>
<td align="right">10,540</td>
<td align="right">59.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,260</td>
<td align="right">40.7%</td>
<td align="right">7,260</td>
<td align="right">40.8%</td>
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
<td align="right">80.3%</td>
<td align="right">8,460</td>
<td align="right">80.3%</td>
<td align="right">-0.2%</td>
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
<td align="left">subscr range</td>
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
<td align="right">11,064,900</td>
<td align="right">100.0%</td>
<td align="right">-52.7%</td>
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
<td align="right">28,541,620</td>
<td align="right">9.1%</td>
<td align="right">28,017,980</td>
<td align="right">8.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">28,010,900</td>
<td align="right">9.0%</td>
<td align="right">27,497,140</td>
<td align="right">8.7%</td>
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
<td align="right">283,508,740</td>
<td align="right">90.8%</td>
<td align="right">287,627,960</td>
<td align="right">91.1%</td>
<td align="right">1.5%</td>
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
<td align="right">546,220</td>
<td align="right">100.0%</td>
<td align="right">536,340</td>
<td align="right">100.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">417,060</td>
<td align="right">0.3%</td>
<td align="right">417,060</td>
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
<td align="right">74.7%</td>
<td align="right">1,240</td>
<td align="right">74.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">420</td>
<td align="right">25.3%</td>
<td align="right">420</td>
<td align="right">25.3%</td>
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
<td align="right">76.2%</td>
<td align="right">320</td>
<td align="right">76.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80</td>
<td align="right">19.0%</td>
<td align="right">80</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right">20</td>
<td align="right">4.8%</td>
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
<td align="right">1,674,500</td>
<td align="right">4.6%</td>
<td align="right">-18.3%</td>
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
<td align="right">95.4%</td>
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
<td align="right">2,100</td>
<td align="right">92.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">6.7%</td>
<td align="right">160</td>
<td align="right">7.1%</td>
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
<td align="right">520</td>
<td align="right">24.8%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">920</td>
<td align="right">41.1%</td>
<td align="right">880</td>
<td align="right">41.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">700</td>
<td align="right">31.2%</td>
<td align="right">700</td>
<td align="right">33.3%</td>
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
<td align="right">3,137,700</td>
<td align="right">58.9%</td>
<td align="right">1,269,460</td>
<td align="right">44.7%</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,190,720</td>
<td align="right">41.1%</td>
<td align="right">1,565,660</td>
<td align="right">55.2%</td>
<td align="right">-28.5%</td>
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
<td align="right">2,700</td>
<td align="right">84.4%</td>
<td align="right">2,440</td>
<td align="right">83.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">15.6%</td>
<td align="right">500</td>
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
<td align="left">seq iter</td>
<td align="right">60</td>
<td align="right">2.2%</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">400</td>
<td align="right">14.8%</td>
<td align="right">240</td>
<td align="right">9.8%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">520</td>
<td align="right">19.3%</td>
<td align="right">440</td>
<td align="right">18.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">820</td>
<td align="right">30.4%</td>
<td align="right">720</td>
<td align="right">29.5%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">300</td>
<td align="right">11.1%</td>
<td align="right">280</td>
<td align="right">11.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">260</td>
<td align="right">9.6%</td>
<td align="right">260</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">180</td>
<td align="right">6.7%</td>
<td align="right">180</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">160</td>
<td align="right">5.9%</td>
<td align="right">160</td>
<td align="right">6.6%</td>
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
<td align="right">35,354,060</td>
<td align="right">6.3%</td>
<td align="right">34,566,320</td>
<td align="right">6.2%</td>
<td align="right">-2.2%</td>
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
<td align="right">10,508,380</td>
<td align="right">1.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">512,527,300</td>
<td align="right">91.8%</td>
<td align="right">510,425,660</td>
<td align="right">91.9%</td>
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
<td align="left">Failure</td>
<td align="right">21,640</td>
<td align="right">9.5%</td>
<td align="right">21,380</td>
<td align="right">9.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">205,280</td>
<td align="right">90.5%</td>
<td align="right">207,500</td>
<td align="right">90.7%</td>
<td align="right">1.1%</td>
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
<td align="left">overridden</td>
<td align="right">660</td>
<td align="right">3.0%</td>
<td align="right">600</td>
<td align="right">2.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,400</td>
<td align="right">6.5%</td>
<td align="right">1,520</td>
<td align="right">7.1%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">300</td>
<td align="right">1.4%</td>
<td align="right">280</td>
<td align="right">1.3%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">380</td>
<td align="right">1.8%</td>
<td align="right">380</td>
<td align="right">1.8%</td>
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
<td align="right">151,809,520</td>
<td align="right">100.0%</td>
<td align="right">147,666,160</td>
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
<td align="right">225,020</td>
<td align="right">0.1%</td>
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
<td align="right">231,917,640</td>
<td align="right">96.6%</td>
<td align="right">231,932,200</td>
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
<td align="right">9,920</td>
<td align="right">73.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,500</td>
<td align="right">25.5%</td>
<td align="right">3,500</td>
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
<td align="left">other</td>
<td align="right">18,820</td>
<td align="right">537.7%</td>
<td align="right">18,520</td>
<td align="right">529.1%</td>
<td align="right">-1.6%</td>
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
<td align="right">26,779,340</td>
<td align="right">49.9%</td>
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
<td align="left">Failure</td>
<td align="right">26,740</td>
<td align="right">98.5%</td>
<td align="right">26,760</td>
<td align="right">98.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">400</td>
<td align="right">1.5%</td>
<td align="right">400</td>
<td align="right">1.5%</td>
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
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">26,700</td>
<td align="right">99.9%</td>
<td align="right">26,700</td>
<td align="right">99.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,614,580</td>
<td align="right">2.0%</td>
<td align="right">2,155,600</td>
<td align="right">1.7%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,972,080</td>
<td align="right">3.8%</td>
<td align="right">4,235,860</td>
<td align="right">3.3%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">122,927,880</td>
<td align="right">94.1%</td>
<td align="right">123,082,540</td>
<td align="right">95.0%</td>
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
<td align="right">50,540</td>
<td align="right">34.6%</td>
<td align="right">59,140</td>
<td align="right">42.0%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">95,520</td>
<td align="right">65.4%</td>
<td align="right">81,640</td>
<td align="right">58.0%</td>
<td align="right">-14.5%</td>
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
<td align="right">46,640</td>
<td align="right">92.3%</td>
<td align="right">55,280</td>
<td align="right">93.5%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,060</td>
<td align="right">2.1%</td>
<td align="right">1,020</td>
<td align="right">1.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,780</td>
<td align="right">5.5%</td>
<td align="right">2,780</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
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
<td align="right">3,114,291,220</td>
<td align="right">63.3%</td>
<td align="right">2,489,370,960</td>
<td align="right">61.6%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,625,055,840</td>
<td align="right">33.0%</td>
<td align="right">1,393,835,400</td>
<td align="right">34.5%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">133,919,660</td>
<td align="right">2.7%</td>
<td align="right">117,873,560</td>
<td align="right">2.9%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">44,183,960</td>
<td align="right">0.9%</td>
<td align="right">43,025,800</td>
<td align="right">1.1%</td>
<td align="right">-2.6%</td>
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
<td align="right">23,399,640</td>
<td align="right">14.8%</td>
<td align="right">11,064,900</td>
<td align="right">7.8%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,190,720</td>
<td align="right">1.4%</td>
<td align="right">1,565,660</td>
<td align="right">1.1%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,048,440</td>
<td align="right">1.3%</td>
<td align="right">1,674,500</td>
<td align="right">1.2%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,614,580</td>
<td align="right">1.7%</td>
<td align="right">2,155,600</td>
<td align="right">1.5%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">35,354,060</td>
<td align="right">22.4%</td>
<td align="right">34,566,320</td>
<td align="right">24.2%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">28,010,900</td>
<td align="right">17.8%</td>
<td align="right">27,497,140</td>
<td align="right">19.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,879,160</td>
<td align="right">18.3%</td>
<td align="right">28,820,420</td>
<td align="right">20.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,807,080</td>
<td align="right">17.0%</td>
<td align="right">26,779,340</td>
<td align="right">18.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,035,720</td>
<td align="right">5.1%</td>
<td align="right">8,035,720</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">417,060</td>
<td align="right">0.3%</td>
<td align="right">417,060</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,844,360</td>
<td align="right">4.2%</td>
<td align="right">1,283,040</td>
<td align="right">3.0%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,830,920</td>
<td align="right">31.3%</td>
<td align="right">10,170,740</td>
<td align="right">23.6%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,707,400</td>
<td align="right">33.3%</td>
<td align="right">17,843,940</td>
<td align="right">41.5%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,721,460</td>
<td align="right">3.9%</td>
<td align="right">1,838,260</td>
<td align="right">4.3%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">239,580</td>
<td align="right">0.5%</td>
<td align="right">224,740</td>
<td align="right">0.5%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,120,020</td>
<td align="right">7.1%</td>
<td align="right">2,945,120</td>
<td align="right">6.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,468,520</td>
<td align="right">19.2%</td>
<td align="right">8,468,520</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">201,280</td>
<td align="right">0.5%</td>
<td align="right">201,280</td>
<td align="right">0.5%</td>
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
<td align="right">490,766</td>
<td align="right"></td>
<td align="right">679,793</td>
<td align="right"></td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">531,637</td>
<td align="right"></td>
<td align="right">710,157</td>
<td align="right"></td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">203,887,520</td>
<td align="right">7.3%</td>
<td align="right">144,373,300</td>
<td align="right">5.1%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">50,576,360</td>
<td align="right">1.7%</td>
<td align="right">39,769,820</td>
<td align="right">1.3%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">53,106</td>
<td align="right"></td>
<td align="right">42,666</td>
<td align="right"></td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">738,907,540</td>
<td align="right">24.6%</td>
<td align="right">879,642,731</td>
<td align="right">29.3%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,340</td>
<td align="right">0.0%</td>
<td align="right">3,760</td>
<td align="right">0.0%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">849,585,864</td>
<td align="right">30.3%</td>
<td align="right">951,203,810</td>
<td align="right">33.9%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,433,348,000</td>
<td align="right">47.8%</td>
<td align="right">1,296,294,940</td>
<td align="right">43.2%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">642,059,078</td>
<td align="right">22.9%</td>
<td align="right">702,104,962</td>
<td align="right">25.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,106,290,460</td>
<td align="right">39.5%</td>
<td align="right">1,008,354,120</td>
<td align="right">35.9%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">776,546,230</td>
<td align="right">25.9%</td>
<td align="right">787,882,673</td>
<td align="right">26.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">82,202,194</td>
<td align="right"></td>
<td align="right">82,371,127</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">84,984,614</td>
<td align="right"></td>
<td align="right">84,995,034</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">27,496,220</td>
<td align="right">9.1%</td>
<td align="right">27,498,340</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">134,170,640</td>
<td align="right">44.3%</td>
<td align="right">134,173,060</td>
<td align="right">44.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">168,521,700</td>
<td align="right"></td>
<td align="right">168,521,980</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">168,499,860</td>
<td align="right">55.7%</td>
<td align="right">168,500,120</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">157,332,174</td>
<td align="right"></td>
<td align="right">157,331,987</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">106,671,080</td>
<td align="right">35.2%</td>
<td align="right">106,670,960</td>
<td align="right">35.2%</td>
<td align="right">-0.0%</td>
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
<td align="right">6,680</td>
<td align="right">5,770,700</td>
<td align="right">200,438,906</td>
<td align="right">11,756,820</td>
<td align="right">18,698,380</td>
<td align="right">6,680</td>
<td align="right">5,770,700</td>
<td align="right">200,442,104</td>
<td align="right">11,754,820</td>
<td align="right">18,708,120</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">260</td>
<td align="right">18.1%</td>
<td align="right">920</td>
<td align="right">24.2%</td>
<td align="right">253.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,440</td>
<td align="right">15.8%</td>
<td align="right">3,800</td>
<td align="right">30.4%</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">440</td>
<td align="right">4.8%</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,085,139,120</td>
<td align="right">6,117.1%</td>
<td align="right">5,930,923,040</td>
<td align="right">8,165.1%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">9,120</td>
<td align="right"></td>
<td align="right">12,520</td>
<td align="right"></td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,920</td>
<td align="right">21.1%</td>
<td align="right">2,320</td>
<td align="right">18.5%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">5,740</td>
<td align="right">62.9%</td>
<td align="right">6,400</td>
<td align="right">51.1%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">66,782,460</td>
<td align="right"></td>
<td align="right">72,637,800</td>
<td align="right"></td>
<td align="right">8.8%</td>
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
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">120 / 0 !!</td>
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
<td align="right">180</td>
<td align="right">1.4%</td>
<td align="right">180 / 0 !!</td>
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
<td align="right">1,060</td>
<td align="right">73.6%</td>
<td align="right">3,540</td>
<td align="right">93.2%</td>
<td align="right">234.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,440</td>
<td align="right"></td>
<td align="right">3,800</td>
<td align="right"></td>
<td align="right">163.9%</td>
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
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">20 / 0 !!</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,279,980</td>
<td align="right">10.9%</td>
<td align="right">8,808,540</td>
<td align="right">15.2%</td>
<td align="right">286.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">20,889,600</td>
<td align="right"></td>
<td align="right">58,081,280</td>
<td align="right"></td>
<td align="right">178.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">449,280</td>
<td align="right">2.2%</td>
<td align="right">1,227,680</td>
<td align="right">2.1%</td>
<td align="right">173.3%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">18,160,340</td>
<td align="right">86.9%</td>
<td align="right">48,045,060</td>
<td align="right">82.7%</td>
<td align="right">164.6%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">737,280</td>
<td align="right">3.5%</td>
<td align="right">163,840</td>
<td align="right">0.3%</td>
<td align="right">-77.8%</td>
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
<td align="right">24.5%</td>
<td align="left">240</td>
<td align="right">6.8%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">120</td>
<td align="right">11.3%</td>
<td align="left">1,440</td>
<td align="right">40.7%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">220</td>
<td align="right">20.8%</td>
<td align="left">1,040</td>
<td align="right">29.4%</td>
<td align="right">372.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">220</td>
<td align="right">20.8%</td>
<td align="left">380</td>
<td align="right">10.7%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">240</td>
<td align="right">22.6%</td>
<td align="left">320</td>
<td align="right">9.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">120</td>
<td align="right">3.4%</td>
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
<td align="right">2.8%</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">11.1%</td>
<td align="right">100</td>
<td align="right">2.6%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">60</td>
<td align="right">4.2%</td>
<td align="right">140</td>
<td align="right">3.7%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">280</td>
<td align="right">19.4%</td>
<td align="right">1,760</td>
<td align="right">46.3%</td>
<td align="right">528.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">200</td>
<td align="right">13.9%</td>
<td align="right">740</td>
<td align="right">19.5%</td>
<td align="right">270.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">360</td>
<td align="right">25.0%</td>
<td align="right">280</td>
<td align="right">7.4%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">320</td>
<td align="right">22.2%</td>
<td align="right">640</td>
<td align="right">16.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">1.4%</td>
<td align="right">120</td>
<td align="right">3.2%</td>
<td align="right">500.0%</td>
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
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">120</td>
<td align="right">8.3%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">80</td>
<td align="right">5.6%</td>
<td align="right">140</td>
<td align="right">3.7%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">160</td>
<td align="right">11.1%</td>
<td align="right">1,480</td>
<td align="right">38.9%</td>
<td align="right">825.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">11.1%</td>
<td align="right">980</td>
<td align="right">25.8%</td>
<td align="right">512.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">240</td>
<td align="right">16.7%</td>
<td align="right">320</td>
<td align="right">8.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">280</td>
<td align="right">19.4%</td>
<td align="right">440</td>
<td align="right">11.6%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">120</td>
<td align="right">3.2%</td>
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
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">632,640</td>
<td align="right">10,382,300</td>
<td align="right">1,541.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">15,760</td>
<td align="right">250,540</td>
<td align="right">1,489.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">15,760</td>
<td align="right">170,420</td>
<td align="right">981.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">15,760</td>
<td align="right">81,920</td>
<td align="right">419.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,209,980</td>
<td align="right">15,714,900</td>
<td align="right">389.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">3,209,980</td>
<td align="right">15,623,340</td>
<td align="right">386.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3,209,980</td>
<td align="right">15,544,720</td>
<td align="right">384.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">3,209,980</td>
<td align="right">15,540,100</td>
<td align="right">384.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,209,980</td>
<td align="right">15,536,740</td>
<td align="right">384.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">3,209,980</td>
<td align="right">15,536,740</td>
<td align="right">384.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">9,691,340</td>
<td align="right">46,750,620</td>
<td align="right">382.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">15,760</td>
<td align="right">49,940</td>
<td align="right">216.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">15,760</td>
<td align="right">49,940</td>
<td align="right">216.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">6,401,920</td>
<td align="right">19,265,200</td>
<td align="right">200.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">50,877,740</td>
<td align="right">133,942,580</td>
<td align="right">163.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">8,014,180</td>
<td align="right">20,445,260</td>
<td align="right">155.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">17,485,240</td>
<td align="right">43,224,900</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,189,220</td>
<td align="right">42,959,560</td>
<td align="right">136.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">39,159,280</td>
<td align="right">86,893,800</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">39,159,280</td>
<td align="right">86,893,800</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">39,159,280</td>
<td align="right">86,893,800</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">238,214,980</td>
<td align="right">518,967,240</td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">124,020</td>
<td align="right">261,340</td>
<td align="right">110.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">64,509,500</td>
<td align="right">135,239,380</td>
<td align="right">109.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">23,860,280</td>
<td align="right">49,774,320</td>
<td align="right">108.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,108,880</td>
<td align="right">19,787,160</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,108,880</td>
<td align="right">19,787,160</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">15,153,160</td>
<td align="right">27,753,160</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">516,680</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">71,431,860</td>
<td align="right">115,433,760</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,431,860</td>
<td align="right">115,433,760</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">35,609,560</td>
<td align="right">53,381,080</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">716,446,060</td>
<td align="right">1,066,186,120</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">688,150,740</td>
<td align="right">1,021,920,840</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">142,260</td>
<td align="right">207,240</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">3,140,820</td>
<td align="right">4,571,320</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,228,240</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">924,700</td>
<td align="right">1,243,600</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,225,200</td>
<td align="right">15,037,480</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">10,503,340</td>
<td align="right">13,981,660</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">927,900</td>
<td align="right">1,229,200</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">16,247,940</td>
<td align="right">21,471,320</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">15,893,380</td>
<td align="right">20,978,320</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">15,578,660</td>
<td align="right">20,537,940</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">38,897,400</td>
<td align="right">51,225,120</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">38,897,400</td>
<td align="right">51,225,120</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">32,764,860</td>
<td align="right">42,956,980</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">715,560</td>
<td align="right">923,440</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">481,740</td>
<td align="right">617,560</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,612,540</td>
<td align="right">2,038,780</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">17,916,900</td>
<td align="right">13,345,600</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">55,637,200</td>
<td align="right">69,665,840</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">22,450,380</td>
<td align="right">28,035,620</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">120,410,400</td>
<td align="right">148,749,600</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,291,420</td>
<td align="right">1,592,760</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">108,331,760</td>
<td align="right">132,641,560</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">23,153,640</td>
<td align="right">28,092,980</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">23,153,640</td>
<td align="right">28,092,980</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">45,303,220</td>
<td align="right">54,927,360</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">41,039,040</td>
<td align="right">33,787,640</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">926,960</td>
<td align="right">1,086,240</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">463,480</td>
<td align="right">543,120</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">463,480</td>
<td align="right">543,120</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">463,480</td>
<td align="right">543,120</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">945,220</td>
<td align="right">1,105,460</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">481,740</td>
<td align="right">563,240</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">481,740</td>
<td align="right">562,380</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,505,680</td>
<td align="right">3,773,540</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">6,261,080</td>
<td align="right">7,236,880</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">6,261,080</td>
<td align="right">7,236,880</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">79,553,000</td>
<td align="right">91,851,700</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">6,261,080</td>
<td align="right">7,222,040</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">43,220,700</td>
<td align="right">49,135,120</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">10,279,760</td>
<td align="right">11,666,860</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">7,781,000</td>
<td align="right">8,820,160</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">5,104,500</td>
<td align="right">5,729,400</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">7,533,840</td>
<td align="right">8,448,960</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">7,533,840</td>
<td align="right">8,448,960</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">59,347,520</td>
<td align="right">66,316,380</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,945,420</td>
<td align="right">8,805,940</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,533,840</td>
<td align="right">8,319,260</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">18,224,260</td>
<td align="right">19,946,620</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">18,224,260</td>
<td align="right">19,946,620</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">18,224,260</td>
<td align="right">19,946,620</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">18,224,260</td>
<td align="right">19,946,620</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">66,782,460</td>
<td align="right">72,637,800</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">66,782,460</td>
<td align="right">72,637,780</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">10,690,420</td>
<td align="right">11,621,120</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">521,580</td>
<td align="right">565,080</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">22,339,600</td>
<td align="right">24,004,720</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">1,835,700</td>
<td align="right">1,968,780</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">21,039,480</td>
<td align="right">22,474,440</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">16,357,920</td>
<td align="right">17,400,860</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">29,626,660</td>
<td align="right">31,467,440</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">29,626,660</td>
<td align="right">31,459,060</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">11,452,580</td>
<td align="right">12,103,260</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">27,603,960</td>
<td align="right">29,075,420</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">85,389,900</td>
<td align="right">89,859,640</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">29,752,700</td>
<td align="right">31,186,580</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,105,780</td>
<td align="right">8,448,060</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">11,119,660</td>
<td align="right">11,569,560</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">26,622,160</td>
<td align="right">27,621,840</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">26,140,420</td>
<td align="right">27,060,500</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">18,281,420</td>
<td align="right">18,915,560</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">44,022,100</td>
<td align="right">45,536,220</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">26,140,420</td>
<td align="right">27,037,680</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">9,085,340</td>
<td align="right">9,387,220</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,160,080</td>
<td align="right">4,256,040</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">17,381,620</td>
<td align="right">17,755,560</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">16,990,000</td>
<td align="right">17,344,260</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,027,420</td>
<td align="right">31,666,980</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">31,027,420</td>
<td align="right">31,664,740</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">84,699,360</td>
<td align="right">85,983,400</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">7,973,180</td>
<td align="right">8,092,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">17,485,000</td>
<td align="right">17,670,080</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">7,997,320</td>
<td align="right">8,081,680</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,997,320</td>
<td align="right">8,081,680</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">21,732,980</td>
<td align="right">21,606,740</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">47,115,820</td>
<td align="right">46,987,120</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">15,067,680</td>
<td align="right">15,106,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">7,873,340</td>
<td align="right">7,886,040</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">591,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">483,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">248,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">248,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">96,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">80,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">79,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right">75,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">65,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">58,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">43,040</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">30,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">30,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">28,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">27,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">27,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">22,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">20,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">18,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">18,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">12,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">9,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right"></td>
<td align="right">6,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">6,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">5,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">4,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">2,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">2,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">2,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">2,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">2,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">2,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">1,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">20</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right"></td>
<td align="right">180</td>
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
<td align="right">240</td>
<td align="right">71.4%</td>
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
<td align="right">240</td>
<td align="right">71.4%</td>
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
Stats gathered on: 2025-07-02
