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
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,860</td>
<td align="right">1,109,660</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">45,956,560</td>
<td align="right">17,097,900</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,867,360</td>
<td align="right">6,158,320</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,764,820</td>
<td align="right">8,668,540</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">23,621,900</td>
<td align="right">11,070,480</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">20,823,200</td>
<td align="right">10,542,700</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,187,240</td>
<td align="right">49,892,240</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">42,960</td>
<td align="right">25,280</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">85,998,880</td>
<td align="right">54,720,980</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">56,298,600</td>
<td align="right">36,884,640</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,794,400</td>
<td align="right">15,703,920</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,941,220</td>
<td align="right">26,368,480</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">37,261,140</td>
<td align="right">25,817,660</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,771,500</td>
<td align="right">12,600,020</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">38,438,400</td>
<td align="right">28,850,180</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,498,780</td>
<td align="right">47,795,040</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">188,913,180</td>
<td align="right">144,679,560</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">150,953,140</td>
<td align="right">116,084,160</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">27,378,260</td>
<td align="right">21,063,000</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">95,257,680</td>
<td align="right">73,505,020</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">118,994,820</td>
<td align="right">93,997,060</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,297,780</td>
<td align="right">12,927,980</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">53,736,600</td>
<td align="right">42,708,900</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,083,400</td>
<td align="right">3,261,980</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">258,753,940</td>
<td align="right">211,580,040</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,992,520</td>
<td align="right">5,861,080</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">33,092,200</td>
<td align="right">27,585,180</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">61,958,200</td>
<td align="right">72,171,740</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,103,467,060</td>
<td align="right">932,630,380</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,904,780</td>
<td align="right">42,333,760</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">226,900,480</td>
<td align="right">194,316,400</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,988,880</td>
<td align="right">3,443,320</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,628,040</td>
<td align="right">124,892,260</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">5,895,860</td>
<td align="right">5,163,600</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">231,348,960</td>
<td align="right">203,630,640</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">230,514,620</td>
<td align="right">203,636,720</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,415,840</td>
<td align="right">3,913,820</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,413,120</td>
<td align="right">14,548,120</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,045,880</td>
<td align="right">1,156,240</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,281,320</td>
<td align="right">2,511,600</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,499,680</td>
<td align="right">1,353,040</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,280</td>
<td align="right">38,580</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">26,632,180</td>
<td align="right">24,351,420</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">153,412,460</td>
<td align="right">140,443,720</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">307,740</td>
<td align="right">281,820</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,841,120</td>
<td align="right">7,414,040</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,341,760</td>
<td align="right">8,606,700</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,882,440</td>
<td align="right">9,138,240</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">63,341,120</td>
<td align="right">58,764,300</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">206,731,460</td>
<td align="right">192,266,420</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,725,400</td>
<td align="right">16,546,060</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">45,055,040</td>
<td align="right">42,297,360</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,713,440</td>
<td align="right">20,787,740</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,843,640</td>
<td align="right">12,151,940</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,392,400</td>
<td align="right">12,740,660</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">146,540,780</td>
<td align="right">139,867,100</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,252,360</td>
<td align="right">2,168,500</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">299,664,600</td>
<td align="right">288,598,220</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,426,060</td>
<td align="right">19,685,920</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">108,568,100</td>
<td align="right">112,275,200</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,206,120</td>
<td align="right">7,445,360</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,136,100</td>
<td align="right">12,709,880</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,428,800</td>
<td align="right">7,199,560</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,605,300</td>
<td align="right">1,555,800</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,458,860</td>
<td align="right">1,501,160</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,322,360</td>
<td align="right">15,860,080</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">103,719,320</td>
<td align="right">100,801,660</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">335,560</td>
<td align="right">344,280</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,773,600</td>
<td align="right">18,213,620</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,243,180</td>
<td align="right">3,322,580</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">581,640</td>
<td align="right">595,840</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,367,000</td>
<td align="right">39,283,360</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">9,850,600</td>
<td align="right">9,626,280</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">320,080</td>
<td align="right">327,220</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,942,540</td>
<td align="right">1,900,600</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">147,520</td>
<td align="right">150,660</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,844,840</td>
<td align="right">11,061,400</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">54,580,620</td>
<td align="right">53,727,840</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,982,920</td>
<td align="right">29,415,540</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,984,300</td>
<td align="right">29,416,920</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,120,660</td>
<td align="right">10,956,020</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,363,740</td>
<td align="right">6,269,780</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,880,680</td>
<td align="right">10,025,120</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,099,600</td>
<td align="right">18,361,160</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">399,980</td>
<td align="right">405,740</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">452,560</td>
<td align="right">458,320</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,645,340</td>
<td align="right">14,806,720</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">143,409,300</td>
<td align="right">144,974,960</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">34,412,360</td>
<td align="right">34,049,940</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,960</td>
<td align="right">72,700</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,415,560</td>
<td align="right">4,457,460</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,969,340</td>
<td align="right">2,944,040</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">32,903,740</td>
<td align="right">32,635,240</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,701,400</td>
<td align="right">6,754,560</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,490,460</td>
<td align="right">4,520,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">27,951,160</td>
<td align="right">28,131,860</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,394,900</td>
<td align="right">2,408,320</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,563,700</td>
<td align="right">4,589,260</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,270,700</td>
<td align="right">11,209,900</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,078,000</td>
<td align="right">38,257,120</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,243,920</td>
<td align="right">1,248,440</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">58,220</td>
<td align="right">58,420</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">897,400</td>
<td align="right">900,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,127,000</td>
<td align="right">6,144,460</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,753,620</td>
<td align="right">2,747,540</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,710,000</td>
<td align="right">9,729,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,649,060</td>
<td align="right">38,624,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">230,760</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">611,380</td>
<td align="right">611,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,718,460</td>
<td align="right">2,717,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,660</td>
<td align="right">524,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,413,040</td>
<td align="right">0.0%</td>
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
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
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
<td align="right">11,784,420</td>
<td align="right">19.6%</td>
<td align="right">15,693,020</td>
<td align="right">24.5%</td>
<td align="right">33.2%</td>
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
<td align="right">80.4%</td>
<td align="right">48,411,720</td>
<td align="right">75.5%</td>
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
<td align="right">9,780</td>
<td align="right">100.0%</td>
<td align="right">10,700</td>
<td align="right">100.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">remainder</td>
<td align="right">2,760</td>
<td align="right">28.2%</td>
<td align="right">3,680</td>
<td align="right">34.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.5%</td>
<td align="right">3,180</td>
<td align="right">29.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.3%</td>
<td align="right">3,160</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">320</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.5%</td>
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
<td align="right">6,363,740</td>
<td align="right">100.0%</td>
<td align="right">6,269,780</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">9,697,280</td>
<td align="right">9.2%</td>
<td align="right">9,717,580</td>
<td align="right">9.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,148,800</td>
<td align="right">2.0%</td>
<td align="right">2,151,980</td>
<td align="right">2.0%</td>
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
<td align="right">93,974,840</td>
<td align="right">88.8%</td>
<td align="right">93,957,360</td>
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
<td align="right">12,100</td>
<td align="right">22.7%</td>
<td align="right">11,700</td>
<td align="right">22.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,140</td>
<td align="right">77.3%</td>
<td align="right">41,200</td>
<td align="right">77.9%</td>
<td align="right">0.1%</td>
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
<td align="right">8,840</td>
<td align="right">73.1%</td>
<td align="right">8,460</td>
<td align="right">72.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,680</td>
<td align="right">13.9%</td>
<td align="right">1,660</td>
<td align="right">14.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.0%</td>
<td align="right">720</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">5.6%</td>
<td align="right">680</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">180</td>
<td align="right">1.5%</td>
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
<td align="right">16,706,640</td>
<td align="right">2.9%</td>
<td align="right">15,510,000</td>
<td align="right">2.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">554,480,840</td>
<td align="right">97.1%</td>
<td align="right">555,887,120</td>
<td align="right">97.3%</td>
<td align="right">0.3%</td>
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
<td align="right">319,260</td>
<td align="right">100.0%</td>
<td align="right">296,740</td>
<td align="right">100.0%</td>
<td align="right">-7.1%</td>
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
<td align="right">233,700</td>
<td align="right">0.6%</td>
<td align="right">149,820</td>
<td align="right">0.4%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,487,840</td>
<td align="right">4.1%</td>
<td align="right">1,344,660</td>
<td align="right">3.7%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,757,180</td>
<td align="right">95.2%</td>
<td align="right">34,706,340</td>
<td align="right">95.8%</td>
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
<td align="left">Success</td>
<td align="right">4,740</td>
<td align="right">29.2%</td>
<td align="right">3,160</td>
<td align="right">28.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,480</td>
<td align="right">70.8%</td>
<td align="right">8,020</td>
<td align="right">71.7%</td>
<td align="right">-30.1%</td>
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
<td align="right">11,020</td>
<td align="right">96.0%</td>
<td align="right">7,560</td>
<td align="right">94.3%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">80</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">80</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
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
<td align="right">4,988,600</td>
<td align="right">8.4%</td>
<td align="right">5,856,880</td>
<td align="right">9.7%</td>
<td align="right">17.4%</td>
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
<td align="right">90.3%</td>
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
<td align="right">3,800</td>
<td align="right">100.0%</td>
<td align="right">4,080</td>
<td align="right">100.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">38.9%</td>
<td align="right">1,720</td>
<td align="right">42.2%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">840</td>
<td align="right">22.1%</td>
<td align="right">880</td>
<td align="right">21.6%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">21.1%</td>
<td align="right">800</td>
<td align="right">19.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">680</td>
<td align="right">17.9%</td>
<td align="right">680</td>
<td align="right">16.7%</td>
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
<td align="right">15,862,540</td>
<td align="right">10.8%</td>
<td align="right">6,155,900</td>
<td align="right">4.3%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,768,800</td>
<td align="right">14.9%</td>
<td align="right">24,623,300</td>
<td align="right">17.0%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">108,841,480</td>
<td align="right">74.3%</td>
<td align="right">113,926,900</td>
<td align="right">78.7%</td>
<td align="right">4.7%</td>
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
<td align="right">4,820</td>
<td align="right">1.2%</td>
<td align="right">2,420</td>
<td align="right">0.5%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">410,700</td>
<td align="right">98.8%</td>
<td align="right">464,540</td>
<td align="right">99.5%</td>
<td align="right">13.1%</td>
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
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">260</td>
<td align="right">10.7%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">51.5%</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.1%</td>
<td align="right">420</td>
<td align="right">17.4%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">2.1%</td>
<td align="right">80</td>
<td align="right">3.3%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">380</td>
<td align="right">15.7%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">820</td>
<td align="right">17.0%</td>
<td align="right">800</td>
<td align="right">33.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.7%</td>
<td align="right">180</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">1.7%</td>
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
<td align="right">85,374,500</td>
<td align="right">9.0%</td>
<td align="right">54,515,900</td>
<td align="right">6.1%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">211,075,340</td>
<td align="right">22.3%</td>
<td align="right">157,386,000</td>
<td align="right">17.5%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">651,313,340</td>
<td align="right">68.7%</td>
<td align="right">685,385,080</td>
<td align="right">76.4%</td>
<td align="right">5.2%</td>
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
<td align="right">4,589,840</td>
<td align="right">99.6%</td>
<td align="right">3,159,960</td>
<td align="right">99.5%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,620</td>
<td align="right">0.4%</td>
<td align="right">14,360</td>
<td align="right">0.5%</td>
<td align="right">-13.6%</td>
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
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.4%</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">2.0%</td>
<td align="right">180</td>
<td align="right">1.3%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,180</td>
<td align="right">37.2%</td>
<td align="right">4,740</td>
<td align="right">33.0%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,320</td>
<td align="right">32.0%</td>
<td align="right">4,760</td>
<td align="right">33.1%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.5%</td>
<td align="right">440</td>
<td align="right">3.1%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">17.1%</td>
<td align="right">2,840</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.7%</td>
<td align="right">620</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">1.1%</td>
<td align="right">180</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">213,449,780</td>
<td align="right">100.0%</td>
<td align="right">163,877,060</td>
<td align="right">100.0%</td>
<td align="right">-23.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,914,560</td>
<td align="right">45.9%</td>
<td align="right">15,756,480</td>
<td align="right">19.0%</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,040,300</td>
<td align="right">40.1%</td>
<td align="right">52,757,980</td>
<td align="right">63.5%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">16,401,120</td>
<td align="right">14.0%</td>
<td align="right">14,536,560</td>
<td align="right">17.5%</td>
<td align="right">-11.4%</td>
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
<td align="right">1,017,760</td>
<td align="right">98.9%</td>
<td align="right">297,900</td>
<td align="right">96.4%</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,600</td>
<td align="right">1.1%</td>
<td align="right">11,160</td>
<td align="right">3.6%</td>
<td align="right">-3.8%</td>
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
<td align="right">8,960</td>
<td align="right">77.2%</td>
<td align="right">8,520</td>
<td align="right">76.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.6%</td>
<td align="right">2,040</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">360</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
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
<td align="right">58,220</td>
<td align="right">100.0%</td>
<td align="right">58,420</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">4,577,980</td>
<td align="right">9.7%</td>
<td align="right">1,106,640</td>
<td align="right">2.5%</td>
<td align="right">-75.8%</td>
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
<td align="right">97.5%</td>
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
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">2,900</td>
<td align="right">94.8%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
<td align="right">5.2%</td>
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
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">200</td>
<td align="right">6.9%</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">84.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">220</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.4%</td>
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
<td align="right">4,565,440</td>
<td align="right">1.7%</td>
<td align="right">3,567,500</td>
<td align="right">1.3%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,216,120</td>
<td align="right">0.8%</td>
<td align="right">2,478,860</td>
<td align="right">0.9%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">265,219,680</td>
<td align="right">97.5%</td>
<td align="right">268,660,180</td>
<td align="right">97.8%</td>
<td align="right">1.3%</td>
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
<td align="right">64,340</td>
<td align="right">42.5%</td>
<td align="right">31,840</td>
<td align="right">31.9%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">86,940</td>
<td align="right">57.5%</td>
<td align="right">68,120</td>
<td align="right">68.1%</td>
<td align="right">-21.6%</td>
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
<td align="right">41,540</td>
<td align="right">64.6%</td>
<td align="right">17,080</td>
<td align="right">53.6%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">19,240</td>
<td align="right">29.9%</td>
<td align="right">11,240</td>
<td align="right">35.3%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.6%</td>
<td align="right">1,000</td>
<td align="right">3.1%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">3.7%</td>
<td align="right">2,360</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.2%</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">310,429,300</td>
<td align="right">5.5%</td>
<td align="right">219,162,220</td>
<td align="right">4.4%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">159,567,620</td>
<td align="right">2.8%</td>
<td align="right">118,031,340</td>
<td align="right">2.4%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,184,613,600</td>
<td align="right">56.2%</td>
<td align="right">2,812,509,420</td>
<td align="right">56.9%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,010,320,800</td>
<td align="right">35.5%</td>
<td align="right">1,796,977,560</td>
<td align="right">36.3%</td>
<td align="right">-10.6%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">4,577,980</td>
<td align="right">2.9%</td>
<td align="right">1,106,640</td>
<td align="right">0.9%</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,862,540</td>
<td align="right">10.0%</td>
<td align="right">6,155,900</td>
<td align="right">5.2%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">85,374,500</td>
<td align="right">53.8%</td>
<td align="right">54,515,900</td>
<td align="right">46.3%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,784,420</td>
<td align="right">7.4%</td>
<td align="right">15,693,020</td>
<td align="right">13.3%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,988,600</td>
<td align="right">3.1%</td>
<td align="right">5,856,880</td>
<td align="right">5.0%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,216,120</td>
<td align="right">1.4%</td>
<td align="right">2,478,860</td>
<td align="right">2.1%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,401,120</td>
<td align="right">10.3%</td>
<td align="right">14,536,560</td>
<td align="right">12.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,487,840</td>
<td align="right">0.9%</td>
<td align="right">1,344,660</td>
<td align="right">1.1%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,363,740</td>
<td align="right">4.0%</td>
<td align="right">6,269,780</td>
<td align="right">5.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,697,280</td>
<td align="right">6.1%</td>
<td align="right">9,717,580</td>
<td align="right">8.3%</td>
<td align="right">0.2%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,911,380</td>
<td align="right">17.4%</td>
<td align="right">15,753,300</td>
<td align="right">7.2%</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,257,280</td>
<td align="right">6.5%</td>
<td align="right">13,999,600</td>
<td align="right">6.4%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">79,446,800</td>
<td align="right">25.6%</td>
<td align="right">55,696,880</td>
<td align="right">25.4%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,536,660</td>
<td align="right">12.7%</td>
<td align="right">28,963,800</td>
<td align="right">13.2%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">65,249,540</td>
<td align="right">21.0%</td>
<td align="right">53,242,180</td>
<td align="right">24.3%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,884,620</td>
<td align="right">3.5%</td>
<td align="right">12,312,220</td>
<td align="right">5.6%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,884,180</td>
<td align="right">3.5%</td>
<td align="right">12,311,080</td>
<td align="right">5.6%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,773,720</td>
<td align="right">1.5%</td>
<td align="right">4,148,140</td>
<td align="right">1.9%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,118,860</td>
<td align="right">2.9%</td>
<td align="right">8,129,020</td>
<td align="right">3.7%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,089,380</td>
<td align="right">1.3%</td>
<td align="right">3,882,940</td>
<td align="right">1.8%</td>
<td align="right">-5.0%</td>
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
<td align="right">8,541,780</td>
<td align="right">2.4%</td>
<td align="right">8,521,480</td>
<td align="right">2.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,379,680</td>
<td align="right">11.1%</td>
<td align="right">39,354,860</td>
<td align="right">11.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,383,160</td>
<td align="right">11.1%</td>
<td align="right">39,358,340</td>
<td align="right">11.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,691,020</td>
<td align="right">11.2%</td>
<td align="right">39,666,200</td>
<td align="right">11.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,691,020</td>
<td align="right">11.2%</td>
<td align="right">39,666,200</td>
<td align="right">11.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,705,340</td>
<td align="right">88.8%</td>
<td align="right">314,730,160</td>
<td align="right">88.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,625,340</td>
<td align="right">88.5%</td>
<td align="right">313,629,860</td>
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
<td align="right">13,629,240</td>
<td align="right">3.8%</td>
<td align="right">13,629,240</td>
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
<td align="right">2,497,754</td>
<td align="right"></td>
<td align="right">1,797,097</td>
<td align="right"></td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,170,192,532</td>
<td align="right">33.8%</td>
<td align="right">3,715,989,699</td>
<td align="right">38.8%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,447,389,002</td>
<td align="right">41.0%</td>
<td align="right">4,022,525,068</td>
<td align="right">46.5%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,472,960,700</td>
<td align="right">29.4%</td>
<td align="right">2,170,280,180</td>
<td align="right">25.1%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">38,049,469</td>
<td align="right"></td>
<td align="right">33,621,435</td>
<td align="right"></td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">528,643,040</td>
<td align="right">6.3%</td>
<td align="right">471,176,160</td>
<td align="right">5.4%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">36,313,081</td>
<td align="right"></td>
<td align="right">32,584,966</td>
<td align="right"></td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">708,260</td>
<td align="right">0.1%</td>
<td align="right">769,300</td>
<td align="right">0.1%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,340,521,100</td>
<td align="right">35.6%</td>
<td align="right">3,066,122,700</td>
<td align="right">32.0%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">898,061,300</td>
<td align="right">9.6%</td>
<td align="right">833,762,460</td>
<td align="right">8.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">350,160</td>
<td align="right">0.0%</td>
<td align="right">373,220</td>
<td align="right">0.0%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">457,236,199</td>
<td align="right"></td>
<td align="right">440,246,814</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,961,528,520</td>
<td align="right">23.3%</td>
<td align="right">1,993,306,740</td>
<td align="right">23.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">195,669,706</td>
<td align="right"></td>
<td align="right">193,043,223</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,966,158,882</td>
<td align="right">21.0%</td>
<td align="right">1,954,324,011</td>
<td align="right">20.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">608,265,965</td>
<td align="right"></td>
<td align="right">607,740,014</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">571,992,820</td>
<td align="right">70.7%</td>
<td align="right">572,089,340</td>
<td align="right">70.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,732,360</td>
<td align="right"></td>
<td align="right">236,698,780</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,759,380</td>
<td align="right">29.3%</td>
<td align="right">236,737,340</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">570,934,400</td>
<td align="right">70.6%</td>
<td align="right">570,946,820</td>
<td align="right">70.6%</td>
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
<td align="right">72,878,300</td>
<td align="right">1,458,838,280</td>
<td align="right">25,960</td>
<td align="right">72,517,920</td>
<td align="right">1,460,564,480</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">7,423,923,960</td>
<td align="right">1,267.7%</td>
<td align="right">12,747,694,280</td>
<td align="right">1,471.7%</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">585,618,940</td>
<td align="right"></td>
<td align="right">866,200,620</td>
<td align="right"></td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">133,520</td>
<td align="right">34.3%</td>
<td align="right">168,500</td>
<td align="right">36.1%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">282,580</td>
<td align="right">72.5%</td>
<td align="right">343,460</td>
<td align="right">73.5%</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">389,520</td>
<td align="right"></td>
<td align="right">467,140</td>
<td align="right"></td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">105,760</td>
<td align="right">27.2%</td>
<td align="right">122,680</td>
<td align="right">26.3%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,180</td>
<td align="right">0.3%</td>
<td align="right">1,000</td>
<td align="right">0.2%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,240</td>
<td align="right">0.8%</td>
<td align="right">2,800</td>
<td align="right">0.6%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">7,500</td>
<td align="right">1.9%</td>
<td align="right">8,120</td>
<td align="right">1.7%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,800</td>
<td align="right">0.5%</td>
<td align="right">1,880</td>
<td align="right">0.4%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">267,220</td>
<td align="right">94.6%</td>
<td align="right">343,400</td>
<td align="right">100.0%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">282,580</td>
<td align="right"></td>
<td align="right">343,460</td>
<td align="right"></td>
<td align="right">21.5%</td>
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
<td align="right">13,160</td>
<td align="right">4.7%</td>
<td align="right">14,180</td>
<td align="right">4.1%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40,060</td>
<td align="right">14.2%</td>
<td align="right">43,680</td>
<td align="right">12.7%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">91,980</td>
<td align="right">32.6%</td>
<td align="right">117,420</td>
<td align="right">34.2%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">86,120</td>
<td align="right">30.5%</td>
<td align="right">108,420</td>
<td align="right">31.6%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">38,420</td>
<td align="right">13.6%</td>
<td align="right">46,040</td>
<td align="right">13.4%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">10,760</td>
<td align="right">3.8%</td>
<td align="right">12,000</td>
<td align="right">3.5%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,940</td>
<td align="right">0.7%</td>
<td align="right">1,580</td>
<td align="right">0.5%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="right">1,700</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">33,100</td>
<td align="right">11.7%</td>
<td align="right">14,180</td>
<td align="right">4.1%</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">52,540</td>
<td align="right">18.6%</td>
<td align="right">44,240</td>
<td align="right">12.9%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">108,600</td>
<td align="right">38.4%</td>
<td align="right">125,540</td>
<td align="right">36.6%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">50,540</td>
<td align="right">17.9%</td>
<td align="right">104,280</td>
<td align="right">30.4%</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,420</td>
<td align="right">5.8%</td>
<td align="right">42,580</td>
<td align="right">12.4%</td>
<td align="right">159.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,800</td>
<td align="right">1.3%</td>
<td align="right">10,880</td>
<td align="right">3.2%</td>
<td align="right">186.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">520</td>
<td align="right">0.2%</td>
<td align="right">1,580</td>
<td align="right">0.5%</td>
<td align="right">203.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">120</td>
<td align="right">2,489,440</td>
<td align="right">2,074,433.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">144,720</td>
<td align="right">116,305,220</td>
<td align="right">80,265.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">17,900</td>
<td align="right">13,441,140</td>
<td align="right">74,990.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">26,460</td>
<td align="right">17,736,640</td>
<td align="right">66,931.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">26,460</td>
<td align="right">17,736,640</td>
<td align="right">66,931.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,880</td>
<td align="right">3,477,220</td>
<td align="right">59,036.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">278,980</td>
<td align="right">124,724,260</td>
<td align="right">44,607.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">110,954,380</td>
<td align="right">4,206,052,640</td>
<td align="right">3,690.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,780</td>
<td align="right">10,715,420</td>
<td align="right">1,431.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">291,440</td>
<td align="right">3,661,240</td>
<td align="right">1,156.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">52,980</td>
<td align="right">525,380</td>
<td align="right">891.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">478,260</td>
<td align="right">4,094,240</td>
<td align="right">756.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">110,240</td>
<td align="right">931,660</td>
<td align="right">745.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">5,690,940</td>
<td align="right">39,276,040</td>
<td align="right">590.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,148,340</td>
<td align="right">11,002,940</td>
<td align="right">412.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,148,340</td>
<td align="right">11,002,940</td>
<td align="right">412.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,361,820</td>
<td align="right">15,984,960</td>
<td align="right">375.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,497,620</td>
<td align="right">16,212,540</td>
<td align="right">260.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">21,795,680</td>
<td align="right">50,654,340</td>
<td align="right">132.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">30,241,920</td>
<td align="right">70,053,160</td>
<td align="right">131.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">239,240</td>
<td align="right">515,560</td>
<td align="right">115.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,442,620</td>
<td align="right">71,822,880</td>
<td align="right">114.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,347,960</td>
<td align="right">21,418,860</td>
<td align="right">107.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">9,346,960</td>
<td align="right">18,837,880</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,477,220</td>
<td align="right">32,877,680</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">13,833,640</td>
<td align="right">26,385,060</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">112,403,120</td>
<td align="right">11,879,820</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">466,537,100</td>
<td align="right">830,770,400</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,166,380</td>
<td align="right">17,926,540</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,179,540</td>
<td align="right">2,040,960</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">4,377,400</td>
<td align="right">7,531,280</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">43,911,020</td>
<td align="right">75,308,120</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,960,160</td>
<td align="right">3,306,460</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">46,158,500</td>
<td align="right">74,934,600</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">4,780</td>
<td align="right">1,920</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">213,457,900</td>
<td align="right">335,546,180</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">71,382,460</td>
<td align="right">110,486,000</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,042,140</td>
<td align="right">6,221,780</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">65,495,740</td>
<td align="right">100,536,960</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">552,512,680</td>
<td align="right">840,336,580</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">131,820,480</td>
<td align="right">199,210,580</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">23,355,480</td>
<td align="right">34,798,960</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">585,618,940</td>
<td align="right">866,200,620</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,660</td>
<td align="right">920</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">29,304,600</td>
<td align="right">42,289,700</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">633,354,780</td>
<td align="right">908,899,980</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,268,380</td>
<td align="right">5,359,780</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">139,016,980</td>
<td align="right">195,455,120</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">47,738,420</td>
<td align="right">65,944,640</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">218,700</td>
<td align="right">139,300</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">52,821,540</td>
<td align="right">71,822,880</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,484,660</td>
<td align="right">2,016,520</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,587,640</td>
<td align="right">2,153,480</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">454,980</td>
<td align="right">293,600</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">97,501,940</td>
<td align="right">62,947,100</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,386,880</td>
<td align="right">9,936,300</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,224,980</td>
<td align="right">792,360</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,224,980</td>
<td align="right">792,360</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,316,000</td>
<td align="right">9,908,460</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">29,545,960</td>
<td align="right">39,809,120</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">32,050,480</td>
<td align="right">43,054,260</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">38,485,080</td>
<td align="right">51,400,880</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">72,642,400</td>
<td align="right">96,750,100</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">76,576,440</td>
<td align="right">101,818,340</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,245,980</td>
<td align="right">21,417,460</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,245,980</td>
<td align="right">21,417,460</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,526,260</td>
<td align="right">18,421,800</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,795,780</td>
<td align="right">2,341,220</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">18,258,120</td>
<td align="right">23,765,360</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">78,324,100</td>
<td align="right">101,498,440</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">101,336,520</td>
<td align="right">129,977,300</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">11,473,720</td>
<td align="right">14,708,520</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right">81,080</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,469,080</td>
<td align="right">8,270,280</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,332,820</td>
<td align="right">2,416,460</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,629,260</td>
<td align="right">8,410,760</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">96,891,660</td>
<td align="right">121,566,680</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">40,800,020</td>
<td align="right">50,237,900</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">51,094,260</td>
<td align="right">62,535,620</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">41,407,220</td>
<td align="right">50,659,560</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">16,748,920</td>
<td align="right">13,041,820</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">55,688,540</td>
<td align="right">43,597,160</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">126,572,500</td>
<td align="right">153,196,520</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,275,420</td>
<td align="right">1,013,860</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,063,860</td>
<td align="right">16,821,540</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">33,356,120</td>
<td align="right">39,790,540</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">112,846,240</td>
<td align="right">93,257,340</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,421,040</td>
<td align="right">42,706,440</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">818,160</td>
<td align="right">944,520</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">31,199,380</td>
<td align="right">35,776,200</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">45,426,720</td>
<td align="right">38,930,220</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">40,360</td>
<td align="right">34,600</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">840,040</td>
<td align="right">729,680</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">110,624,760</td>
<td align="right">125,129,320</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">110,615,480</td>
<td align="right">125,115,400</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">257,965,980</td>
<td align="right">291,642,940</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,329,960</td>
<td align="right">7,255,660</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">26,460</td>
<td align="right">23,160</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,204,600</td>
<td align="right">6,336,320</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">27,758,260</td>
<td align="right">30,849,820</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,024,620</td>
<td align="right">4,450,840</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">47,735,840</td>
<td align="right">42,699,360</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">251,100</td>
<td align="right">276,400</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">251,100</td>
<td align="right">276,400</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">102,238,540</td>
<td align="right">92,091,140</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">36,033,000</td>
<td align="right">39,603,660</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">27,220</td>
<td align="right">24,860</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,220,120</td>
<td align="right">9,960,260</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,665,220</td>
<td align="right">2,873,200</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">538,400</td>
<td align="right">580,340</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,444,640</td>
<td align="right">10,136,340</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,474,880</td>
<td align="right">6,937,160</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,886,780</td>
<td align="right">6,405,360</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,327,380</td>
<td align="right">5,887,360</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,496,480</td>
<td align="right">5,122,520</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">43,797,840</td>
<td align="right">46,712,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">71,887,920</td>
<td align="right">67,229,940</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">6,527,020</td>
<td align="right">6,916,860</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,095,920</td>
<td align="right">9,525,700</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">258,960</td>
<td align="right">244,760</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,385,400</td>
<td align="right">3,206,280</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,241,760</td>
<td align="right">32,633,860</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">124,140</td>
<td align="right">119,100</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,395,780</td>
<td align="right">5,181,780</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,561,160</td>
<td align="right">17,208,120</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,767,920</td>
<td align="right">17,419,660</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,516,320</td>
<td align="right">16,098,500</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,649,620</td>
<td align="right">14,133,960</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,317,120</td>
<td align="right">18,852,580</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">877,160</td>
<td align="right">851,600</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">479,100</td>
<td align="right">465,680</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">336,500</td>
<td align="right">327,780</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">9,287,060</td>
<td align="right">9,511,380</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">41,476,420</td>
<td align="right">42,447,740</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">54,454,560</td>
<td align="right">55,644,760</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,270,820</td>
<td align="right">45,210,820</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,735,080</td>
<td align="right">5,829,040</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">4,451,300</td>
<td align="right">4,519,720</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,075,020</td>
<td align="right">4,135,820</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">213,740</td>
<td align="right">210,600</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,857,400</td>
<td align="right">1,830,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,015,920</td>
<td align="right">4,074,780</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,243,840</td>
<td align="right">2,214,020</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,772,660</td>
<td align="right">13,591,960</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,447,540</td>
<td align="right">46,874,620</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">56,899,040</td>
<td align="right">56,274,520</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,238,300</td>
<td align="right">2,220,780</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,237,220</td>
<td align="right">2,219,760</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">820,700</td>
<td align="right">814,760</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,437,780</td>
<td align="right">12,526,940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">35,921,380</td>
<td align="right">35,711,380</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">993,560</td>
<td align="right">987,800</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">993,560</td>
<td align="right">987,800</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,645,940</td>
<td align="right">1,636,880</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">111,060</td>
<td align="right">111,520</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">11,638,460</td>
<td align="right">11,682,600</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right">242,020</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">963,880</td>
<td align="right">966,820</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,420</td>
<td align="right">7,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,607,800</td>
<td align="right">18,657,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,141,860</td>
<td align="right">3,134,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,141,860</td>
<td align="right">3,134,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,174,220</td>
<td align="right">17,200,140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,802,040</td>
<td align="right">2,798,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">208,900</td>
<td align="right">208,700</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,225,480</td>
<td align="right">14,237,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,740</td>
<td align="right">324,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,380</td>
<td align="right">263,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">591,332,020</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">488,233,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">9,943,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,354,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,329,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">698,020</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">570,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">309,120</td>
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
<td align="left">_CALL_TUPLE_1</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">1,500</td>
<td align="right">1,060</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">9,240</td>
<td align="right">11,160</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,840</td>
<td align="right">3,580</td>
<td align="right">-6.8%</td>
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
Stats gathered on: 2024-11-19
