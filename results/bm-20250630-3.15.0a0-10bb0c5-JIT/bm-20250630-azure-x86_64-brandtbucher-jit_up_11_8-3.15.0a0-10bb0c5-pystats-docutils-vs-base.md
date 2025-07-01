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
<td align="right">673,500</td>
<td align="right">1,135,760</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,061,660</td>
<td align="right">3,610,080</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,794,720</td>
<td align="right">4,989,640</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">237,140</td>
<td align="right">175,780</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,001,740</td>
<td align="right">2,275,660</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,735,460</td>
<td align="right">10,725,780</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,726,340</td>
<td align="right">3,711,400</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,888,040</td>
<td align="right">1,529,760</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,940,740</td>
<td align="right">4,063,600</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">754,700</td>
<td align="right">631,820</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,473,280</td>
<td align="right">2,081,900</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,770,200</td>
<td align="right">15,930,200</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">736,780</td>
<td align="right">628,720</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">876,480</td>
<td align="right">753,600</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,321,080</td>
<td align="right">23,865,020</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,304,120</td>
<td align="right">19,800,920</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">9,008,420</td>
<td align="right">8,033,640</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">22,649,300</td>
<td align="right">20,474,700</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">980,440</td>
<td align="right">887,340</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,545,840</td>
<td align="right">8,640,020</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">34,343,060</td>
<td align="right">37,161,300</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,930,860</td>
<td align="right">10,115,580</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,667,440</td>
<td align="right">16,368,620</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">95,415,420</td>
<td align="right">88,445,420</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,917,820</td>
<td align="right">5,492,240</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,226,960</td>
<td align="right">4,859,840</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">35,246,140</td>
<td align="right">32,990,640</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">34,719,980</td>
<td align="right">32,735,900</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">207,983,020</td>
<td align="right">196,574,960</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">778,000</td>
<td align="right">737,960</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,321,640</td>
<td align="right">9,790,720</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,161,700</td>
<td align="right">4,897,820</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,619,840</td>
<td align="right">19,575,940</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,767,700</td>
<td align="right">10,236,900</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,730,300</td>
<td align="right">76,823,580</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">204,859,020</td>
<td align="right">195,225,320</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">185,408,080</td>
<td align="right">176,700,640</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">78,122,120</td>
<td align="right">74,572,360</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,034,420</td>
<td align="right">4,806,420</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">49,079,760</td>
<td align="right">46,881,460</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">52,806,580</td>
<td align="right">50,454,620</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">21,588,240</td>
<td align="right">20,668,440</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,687,280</td>
<td align="right">2,574,700</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,701,200</td>
<td align="right">2,588,140</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">192,172,780</td>
<td align="right">184,151,600</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">111,074,180</td>
<td align="right">106,498,060</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,869,420</td>
<td align="right">5,630,240</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">25,421,760</td>
<td align="right">24,386,820</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">36,529,980</td>
<td align="right">35,068,500</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">317,358,680</td>
<td align="right">304,953,060</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,406,120</td>
<td align="right">36,943,900</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,293,200</td>
<td align="right">11,829,500</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">56,706,000</td>
<td align="right">58,734,380</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">145,922,760</td>
<td align="right">140,886,500</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">34,884,760</td>
<td align="right">36,066,980</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">300,199,980</td>
<td align="right">290,047,700</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">23,181,080</td>
<td align="right">22,405,880</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">24,857,200</td>
<td align="right">25,612,560</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,207,934,180</td>
<td align="right">1,173,191,980</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">196,056,360</td>
<td align="right">190,508,600</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,086,440</td>
<td align="right">49,364,240</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,088,900</td>
<td align="right">32,895,360</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,334,580</td>
<td align="right">75,463,900</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">121,709,720</td>
<td align="right">124,468,820</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">113,296,720</td>
<td align="right">110,819,400</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,418,800</td>
<td align="right">2,366,220</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,152,880</td>
<td align="right">3,088,520</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,834,700</td>
<td align="right">4,740,720</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,932,480</td>
<td align="right">7,786,340</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">322,977,440</td>
<td align="right">317,351,100</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,220,880</td>
<td align="right">14,958,560</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">20,085,180</td>
<td align="right">19,743,820</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">42,867,640</td>
<td align="right">43,501,900</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,681,880</td>
<td align="right">50,974,660</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,440,000</td>
<td align="right">11,290,240</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,036,560</td>
<td align="right">18,797,620</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,035,940</td>
<td align="right">16,822,720</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,318,160</td>
<td align="right">20,070,440</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">65,836,860</td>
<td align="right">66,601,640</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">92,020</td>
<td align="right">93,000</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">304,408,500</td>
<td align="right">301,259,080</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,060,900</td>
<td align="right">4,020,860</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">380,895,720</td>
<td align="right">377,614,800</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">179,280,520</td>
<td align="right">177,786,300</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,337,800</td>
<td align="right">7,277,960</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,432,620</td>
<td align="right">3,406,960</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">150,545,500</td>
<td align="right">151,670,680</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">120,609,920</td>
<td align="right">119,951,200</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,398,540</td>
<td align="right">23,301,200</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,452,200</td>
<td align="right">101,742,820</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">116,444,080</td>
<td align="right">116,166,060</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,078,320</td>
<td align="right">30,017,420</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,098,240</td>
<td align="right">30,037,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,478,540</td>
<td align="right">49,386,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,834,780</td>
<td align="right">93,687,080</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,574,880</td>
<td align="right">16,550,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,280,800</td>
<td align="right">19,294,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,447,500</td>
<td align="right">1,446,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">30,520,700</td>
<td align="right">30,508,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,863,480</td>
<td align="right">8,866,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,498,680</td>
<td align="right">11,498,040</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,770,480</td>
<td align="right">1,770,480</td>
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
<td align="right">129,040</td>
<td align="right">129,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">91,960</td>
<td align="right">91,960</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">68,680</td>
<td align="right">68,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">60,720</td>
<td align="right">60,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">42,860</td>
<td align="right">42,860</td>
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
<td align="right">8,240</td>
<td align="right">8,240</td>
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
<td align="right">23,253,840</td>
<td align="right">11.8%</td>
<td align="right">23,156,560</td>
<td align="right">11.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">169,103,620</td>
<td align="right">85.5%</td>
<td align="right">169,103,640</td>
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
<td align="right">125,860</td>
<td align="right">51.8%</td>
<td align="right">125,800</td>
<td align="right">51.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117,220</td>
<td align="right">48.2%</td>
<td align="right">117,220</td>
<td align="right">48.2%</td>
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
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">8,460</td>
<td align="right">6.7%</td>
<td align="right">8,440</td>
<td align="right">6.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,240</td>
<td align="right">8.1%</td>
<td align="right">10,220</td>
<td align="right">8.1%</td>
<td align="right">-0.2%</td>
</tr>
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
<td align="right">10,767,700</td>
<td align="right">100.0%</td>
<td align="right">10,236,900</td>
<td align="right">100.0%</td>
<td align="right">-4.9%</td>
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
<td align="right">17,834,200</td>
<td align="right">3.1%</td>
<td align="right">17,446,360</td>
<td align="right">3.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,569,060</td>
<td align="right">3.1%</td>
<td align="right">17,188,560</td>
<td align="right">3.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">555,834,680</td>
<td align="right">96.9%</td>
<td align="right">556,595,320</td>
<td align="right">96.9%</td>
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
<td align="left">Success</td>
<td align="right">394,180</td>
<td align="right">100.0%</td>
<td align="right">386,840</td>
<td align="right">100.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">1,749,380</td>
<td align="right">4.6%</td>
<td align="right">1,749,380</td>
<td align="right">4.6%</td>
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
<td align="right">35,740,640</td>
<td align="right">94.6%</td>
<td align="right">35,740,640</td>
<td align="right">94.6%</td>
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
<td align="right">255,440</td>
<td align="right">0.7%</td>
<td align="right">255,440</td>
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
<td align="right">10,080</td>
<td align="right">38.9%</td>
<td align="right">10,080</td>
<td align="right">38.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">15,800</td>
<td align="right">61.1%</td>
<td align="right">15,800</td>
<td align="right">61.1%</td>
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
<td align="right">13,600</td>
<td align="right">86.1%</td>
<td align="right">13,600</td>
<td align="right">86.1%</td>
<td align="right">0.0%</td>
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
<td align="right">620</td>
<td align="right">3.9%</td>
<td align="right">620</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
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
<td align="right">8,991,120</td>
<td align="right">14.1%</td>
<td align="right">8,016,580</td>
<td align="right">12.8%</td>
<td align="right">-10.8%</td>
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
<td align="right">85.9%</td>
<td align="right">54,707,700</td>
<td align="right">87.2%</td>
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
<td align="right">15,600</td>
<td align="right">90.2%</td>
<td align="right">15,360</td>
<td align="right">90.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,700</td>
<td align="right">9.8%</td>
<td align="right">1,700</td>
<td align="right">10.0%</td>
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
<td align="right">37.2%</td>
<td align="right">5,660</td>
<td align="right">36.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,080</td>
<td align="right">26.2%</td>
<td align="right">4,020</td>
<td align="right">26.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,960</td>
<td align="right">19.0%</td>
<td align="right">2,920</td>
<td align="right">19.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,760</td>
<td align="right">17.7%</td>
<td align="right">2,760</td>
<td align="right">18.0%</td>
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
<td align="right">22,286,080</td>
<td align="right">10.4%</td>
<td align="right">19,783,500</td>
<td align="right">9.7%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">158,035,720</td>
<td align="right">74.1%</td>
<td align="right">151,547,840</td>
<td align="right">74.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,998,100</td>
<td align="right">15.5%</td>
<td align="right">31,928,280</td>
<td align="right">15.7%</td>
<td align="right">-3.2%</td>
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
<td align="right">13,400</td>
<td align="right">2.1%</td>
<td align="right">12,780</td>
<td align="right">2.1%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">627,180</td>
<td align="right">97.9%</td>
<td align="right">606,980</td>
<td align="right">97.9%</td>
<td align="right">-3.2%</td>
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
<td align="right">4.5%</td>
<td align="right">460</td>
<td align="right">3.6%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,660</td>
<td align="right">19.9%</td>
<td align="right">2,420</td>
<td align="right">18.9%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,040</td>
<td align="right">7.8%</td>
<td align="right">960</td>
<td align="right">7.5%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,380</td>
<td align="right">17.8%</td>
<td align="right">2,280</td>
<td align="right">17.8%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,000</td>
<td align="right">7.5%</td>
<td align="right">980</td>
<td align="right">7.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,600</td>
<td align="right">19.4%</td>
<td align="right">2,580</td>
<td align="right">20.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,200</td>
<td align="right">16.4%</td>
<td align="right">2,200</td>
<td align="right">17.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">1.6%</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">0.9%</td>
<td align="right">120</td>
<td align="right">0.9%</td>
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
<td align="right">650,042,740</td>
<td align="right">63.4%</td>
<td align="right">638,747,120</td>
<td align="right">63.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">273,413,420</td>
<td align="right">26.7%</td>
<td align="right">270,464,320</td>
<td align="right">26.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">100,693,540</td>
<td align="right">9.8%</td>
<td align="right">100,995,760</td>
<td align="right">10.0%</td>
<td align="right">0.3%</td>
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
<td align="right">5,179,640</td>
<td align="right">99.3%</td>
<td align="right">5,123,980</td>
<td align="right">99.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">35,380</td>
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
<td align="left">metaclass attribute</td>
<td align="right">11,920</td>
<td align="right">33.7%</td>
<td align="right">12,260</td>
<td align="right">34.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">9,480</td>
<td align="right">26.8%</td>
<td align="right">9,360</td>
<td align="right">26.3%</td>
<td align="right">-1.3%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,020</td>
<td align="right">2.9%</td>
<td align="right">1,020</td>
<td align="right">2.9%</td>
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
<td align="right">273,363,440</td>
<td align="right">100.0%</td>
<td align="right">265,945,000</td>
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
<td align="right">30,840</td>
<td align="right">0.0%</td>
<td align="right">30,840</td>
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
<td align="right">30,400</td>
<td align="right">100.0%</td>
<td align="right">30,400</td>
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
<td align="right">48,020,980</td>
<td align="right">38.8%</td>
<td align="right">0.1%</td>
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
<td align="right">53,668,900</td>
<td align="right">43.3%</td>
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
<td align="right">1,022,600</td>
<td align="right">97.0%</td>
<td align="right">1,021,660</td>
<td align="right">97.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">4,822,180</td>
<td align="right">10.2%</td>
<td align="right">4,728,260</td>
<td align="right">10.0%</td>
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
<td align="right">42,671,920</td>
<td align="right">89.8%</td>
<td align="right">42,671,920</td>
<td align="right">90.0%</td>
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
<td align="right">10,320</td>
<td align="right">82.2%</td>
<td align="right">10,260</td>
<td align="right">82.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,240</td>
<td align="right">17.8%</td>
<td align="right">2,240</td>
<td align="right">17.9%</td>
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
<td align="right">620</td>
<td align="right">6.0%</td>
<td align="right">560</td>
<td align="right">5.5%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,240</td>
<td align="right">70.2%</td>
<td align="right">7,240</td>
<td align="right">70.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,520</td>
<td align="right">14.7%</td>
<td align="right">1,520</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">720</td>
<td align="right">7.0%</td>
<td align="right">720</td>
<td align="right">7.0%</td>
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
<td align="right">8,399,760</td>
<td align="right">3.2%</td>
<td align="right">7,922,400</td>
<td align="right">3.0%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">254,173,640</td>
<td align="right">95.3%</td>
<td align="right">247,979,520</td>
<td align="right">95.4%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,874,260</td>
<td align="right">1.5%</td>
<td align="right">3,834,220</td>
<td align="right">1.5%</td>
<td align="right">-1.0%</td>
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
<td align="right">164,680</td>
<td align="right">49.1%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">170,460</td>
<td align="right">49.5%</td>
<td align="right">170,460</td>
<td align="right">50.9%</td>
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
<td align="right">119,600</td>
<td align="right">70.2%</td>
<td align="right">119,600</td>
<td align="right">70.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">42,200</td>
<td align="right">24.8%</td>
<td align="right">42,200</td>
<td align="right">24.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">5,680</td>
<td align="right">3.3%</td>
<td align="right">5,680</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,340</td>
<td align="right">1.4%</td>
<td align="right">2,340</td>
<td align="right">1.4%</td>
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
<td align="right">2,425,650,440</td>
<td align="right">34.5%</td>
<td align="right">2,336,560,740</td>
<td align="right">34.1%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,886,887,540</td>
<td align="right">55.3%</td>
<td align="right">3,809,895,740</td>
<td align="right">55.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">320,858,380</td>
<td align="right">4.6%</td>
<td align="right">316,250,140</td>
<td align="right">4.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">391,889,440</td>
<td align="right">5.6%</td>
<td align="right">386,956,380</td>
<td align="right">5.6%</td>
<td align="right">-1.3%</td>
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
<td align="right">22,286,080</td>
<td align="right">10.3%</td>
<td align="right">19,783,500</td>
<td align="right">9.3%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,991,120</td>
<td align="right">4.2%</td>
<td align="right">8,016,580</td>
<td align="right">3.8%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,767,700</td>
<td align="right">5.0%</td>
<td align="right">10,236,900</td>
<td align="right">4.8%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,569,060</td>
<td align="right">8.1%</td>
<td align="right">17,188,560</td>
<td align="right">8.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,822,180</td>
<td align="right">2.2%</td>
<td align="right">4,728,260</td>
<td align="right">2.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,874,260</td>
<td align="right">1.8%</td>
<td align="right">3,834,220</td>
<td align="right">1.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,253,840</td>
<td align="right">10.7%</td>
<td align="right">23,156,560</td>
<td align="right">10.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100,693,540</td>
<td align="right">46.5%</td>
<td align="right">100,995,760</td>
<td align="right">47.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,137,900</td>
<td align="right">10.2%</td>
<td align="right">22,137,900</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,749,380</td>
<td align="right">0.8%</td>
<td align="right">1,749,380</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,623,260</td>
<td align="right">1.2%</td>
<td align="right">4,388,140</td>
<td align="right">1.1%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">30,436,280</td>
<td align="right">7.8%</td>
<td align="right">31,747,760</td>
<td align="right">8.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,499,460</td>
<td align="right">4.2%</td>
<td align="right">15,964,160</td>
<td align="right">4.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">16,498,640</td>
<td align="right">4.2%</td>
<td align="right">15,964,120</td>
<td align="right">4.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">84,498,920</td>
<td align="right">21.6%</td>
<td align="right">82,281,420</td>
<td align="right">21.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">100,809,180</td>
<td align="right">25.7%</td>
<td align="right">98,545,300</td>
<td align="right">25.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,350,820</td>
<td align="right">12.1%</td>
<td align="right">47,933,440</td>
<td align="right">12.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,714,960</td>
<td align="right">13.7%</td>
<td align="right">53,665,720</td>
<td align="right">13.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,683,720</td>
<td align="right">2.5%</td>
<td align="right">9,685,440</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">1,979,104</td>
<td align="right"></td>
<td align="right">2,417,673</td>
<td align="right"></td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,592,476,060</td>
<td align="right">30.0%</td>
<td align="right">1,552,756,820</td>
<td align="right">29.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,130,121,293</td>
<td align="right">40.1%</td>
<td align="right">2,171,249,264</td>
<td align="right">40.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,970,038,295</td>
<td align="right">35.4%</td>
<td align="right">1,999,368,144</td>
<td align="right">35.8%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,259,383,640</td>
<td align="right">40.6%</td>
<td align="right">2,232,176,000</td>
<td align="right">40.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">31,810,805</td>
<td align="right"></td>
<td align="right">31,490,673</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">532,640</td>
<td align="right">0.1%</td>
<td align="right">537,860</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">454,778,795</td>
<td align="right"></td>
<td align="right">457,617,827</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">194,157,236</td>
<td align="right"></td>
<td align="right">195,058,487</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,251,086,013</td>
<td align="right">22.5%</td>
<td align="right">1,255,497,578</td>
<td align="right">22.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">33,261,463</td>
<td align="right"></td>
<td align="right">33,378,247</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">180,739,040</td>
<td align="right">3.4%</td>
<td align="right">181,360,860</td>
<td align="right">3.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,687,840</td>
<td align="right">1.6%</td>
<td align="right">90,471,720</td>
<td align="right">1.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">350,280</td>
<td align="right">0.1%</td>
<td align="right">351,100</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,405,439,672</td>
<td align="right">26.5%</td>
<td align="right">1,408,412,082</td>
<td align="right">26.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">322,956,854</td>
<td align="right"></td>
<td align="right">323,445,639</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">308,406,720</td>
<td align="right"></td>
<td align="right">308,391,520</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">308,325,280</td>
<td align="right">51.3%</td>
<td align="right">308,329,600</td>
<td align="right">51.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,979,000</td>
<td align="right">48.6%</td>
<td align="right">291,975,080</td>
<td align="right">48.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,861,920</td>
<td align="right">48.7%</td>
<td align="right">292,864,040</td>
<td align="right">48.7%</td>
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
<td align="right">26,160</td>
<td align="right">69,986,080</td>
<td align="right">1,113,857,548</td>
<td align="right">44,188,320</td>
<td align="right">95,525,000</td>
<td align="right">26,180</td>
<td align="right">70,261,280</td>
<td align="right">1,131,286,289</td>
<td align="right">44,432,220</td>
<td align="right">97,984,300</td>
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
<td align="right">180</td>
<td align="right">0.4%</td>
<td align="right">800.0%</td>
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
<td align="right">880</td>
<td align="right">1.9%</td>
<td align="right">528.6%</td>
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
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,580</td>
<td align="right">21.5%</td>
<td align="right">14,120</td>
<td align="right">30.0%</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">300</td>
<td align="right">1.0%</td>
<td align="right">580</td>
<td align="right">1.2%</td>
<td align="right">93.3%</td>
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
<td align="right">1,380</td>
<td align="right">2.9%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">8,940</td>
<td align="right">29.3%</td>
<td align="right">15,380</td>
<td align="right">32.7%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">30,560</td>
<td align="right"></td>
<td align="right">47,060</td>
<td align="right"></td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">14,100</td>
<td align="right">46.1%</td>
<td align="right">15,960</td>
<td align="right">33.9%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,619,334,480</td>
<td align="right">2,010.7%</td>
<td align="right">5,116,038,440</td>
<td align="right">2,049.1%</td>
<td align="right">10.8%</td>
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
<td align="right">220</td>
<td align="right">0.5%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">229,733,180</td>
<td align="right"></td>
<td align="right">249,671,400</td>
<td align="right"></td>
<td align="right">8.7%</td>
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
<td align="right">6,060</td>
<td align="right">67.8%</td>
<td align="right">12,240</td>
<td align="right">79.6%</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">8,940</td>
<td align="right"></td>
<td align="right">15,380</td>
<td align="right"></td>
<td align="right">72.0%</td>
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
<td align="right">27,115,520</td>
<td align="right">17.2%</td>
<td align="right">33,000.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">61,189,040</td>
<td align="right">80.7%</td>
<td align="right">129,901,760</td>
<td align="right">82.3%</td>
<td align="right">112.3%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,599,680</td>
<td align="right">2.1%</td>
<td align="right">3,391,840</td>
<td align="right">2.1%</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">75,776,000</td>
<td align="right"></td>
<td align="right">157,859,840</td>
<td align="right"></td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">12,987,280</td>
<td align="right">17.1%</td>
<td align="right">24,566,240</td>
<td align="right">15.6%</td>
<td align="right">89.2%</td>
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
<td align="left">1,160</td>
<td align="right">19.1%</td>
<td align="left">2,160</td>
<td align="right">17.6%</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">1,960</td>
<td align="right">32.3%</td>
<td align="left">3,800</td>
<td align="right">31.0%</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">2,020</td>
<td align="right">33.3%</td>
<td align="left">4,480</td>
<td align="right">36.6%</td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">760</td>
<td align="right">12.5%</td>
<td align="left">1,420</td>
<td align="right">11.6%</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">160</td>
<td align="right">2.6%</td>
<td align="left">340</td>
<td align="right">2.8%</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">40</td>
<td align="right">0.3%</td>
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
<td align="right">380</td>
<td align="right">2.5%</td>
<td align="right">280.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,400</td>
<td align="right">15.7%</td>
<td align="right">2,300</td>
<td align="right">15.0%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,200</td>
<td align="right">35.8%</td>
<td align="right">5,740</td>
<td align="right">37.3%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">620</td>
<td align="right">6.9%</td>
<td align="right">2,220</td>
<td align="right">14.4%</td>
<td align="right">258.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,300</td>
<td align="right">36.9%</td>
<td align="right">3,940</td>
<td align="right">25.6%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">280</td>
<td align="right">3.1%</td>
<td align="right">620</td>
<td align="right">4.0%</td>
<td align="right">121.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">5.1%</td>
<td align="right">920</td>
<td align="right">6.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,560</td>
<td align="right">28.6%</td>
<td align="right">4,500</td>
<td align="right">29.3%</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,980</td>
<td align="right">22.1%</td>
<td align="right">4,600</td>
<td align="right">29.9%</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">520</td>
<td align="right">5.8%</td>
<td align="right">1,020</td>
<td align="right">6.6%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">460</td>
<td align="right">5.1%</td>
<td align="right">820</td>
<td align="right">5.3%</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right">240</td>
<td align="right">1.6%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">80</td>
<td align="right">0.5%</td>
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
<td align="right">15,120</td>
<td align="right">440,700</td>
<td align="right">2,814.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">146,280</td>
<td align="right">1,907,460</td>
<td align="right">1,204.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">12,760</td>
<td align="right">110,040</td>
<td align="right">762.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">88,440</td>
<td align="right">741,300</td>
<td align="right">738.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">241,740</td>
<td align="right">1,367,520</td>
<td align="right">465.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,080</td>
<td align="right">16,760</td>
<td align="right">444.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">40,060</td>
<td align="right">186,200</td>
<td align="right">364.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">40,060</td>
<td align="right">186,200</td>
<td align="right">364.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">480</td>
<td align="right">2,040</td>
<td align="right">325.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">608,720</td>
<td align="right">2,094,940</td>
<td align="right">244.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,864,440</td>
<td align="right">5,315,360</td>
<td align="right">185.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">373,660</td>
<td align="right">1,055,100</td>
<td align="right">182.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,802,640</td>
<td align="right">5,073,320</td>
<td align="right">181.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">46,020</td>
<td align="right">129,020</td>
<td align="right">180.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">171,900</td>
<td align="right">169.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,573,480</td>
<td align="right">4,134,880</td>
<td align="right">162.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">205,260</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">205,260</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">75,120</td>
<td align="right">186,540</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">1,174,400</td>
<td align="right">2,872,240</td>
<td align="right">144.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,527,240</td>
<td align="right">5,983,300</td>
<td align="right">136.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,384,440</td>
<td align="right">3,142,900</td>
<td align="right">127.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">76,440</td>
<td align="right">170,360</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">135,820</td>
<td align="right">289,680</td>
<td align="right">113.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">87,380</td>
<td align="right">180,480</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">214,080</td>
<td align="right">427,300</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">380,880</td>
<td align="right">749,100</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">247,400</td>
<td align="right">486,340</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">931,260</td>
<td align="right">1,789,340</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">766,440</td>
<td align="right">1,472,580</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">75,120</td>
<td align="right">139,480</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">75,120</td>
<td align="right">139,480</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">139,440</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">864,200</td>
<td align="right">1,583,740</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">878,200</td>
<td align="right">1,604,280</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">878,200</td>
<td align="right">1,604,280</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">8,592,780</td>
<td align="right">15,508,800</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,646,420</td>
<td align="right">6,486,420</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">34,380</td>
<td align="right">60,040</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">75,120</td>
<td align="right">127,700</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,397,860</td>
<td align="right">5,517,080</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">235,320</td>
<td align="right">382,080</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">235,320</td>
<td align="right">382,080</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">432,760</td>
<td align="right">696,640</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">18,389,340</td>
<td align="right">28,541,880</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,674,020</td>
<td align="right">2,593,820</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">18,770,220</td>
<td align="right">28,840,820</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">18,770,220</td>
<td align="right">28,840,820</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">13,864,040</td>
<td align="right">21,295,660</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">18,695,100</td>
<td align="right">28,701,340</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">2,035,900</td>
<td align="right">3,123,420</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">46,020</td>
<td align="right">69,960</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">17,653,060</td>
<td align="right">26,679,540</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">48,360</td>
<td align="right">73,040</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,691,220</td>
<td align="right">16,047,420</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">238,640</td>
<td align="right">351,220</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">6,810,920</td>
<td align="right">9,960,340</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">134,400</td>
<td align="right">195,300</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">134,400</td>
<td align="right">195,300</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">88,440</td>
<td align="right">128,480</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">137,540</td>
<td align="right">198,900</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">14,527,020</td>
<td align="right">20,906,080</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,392,060</td>
<td align="right">20,649,380</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,935,300</td>
<td align="right">4,157,060</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,776,060</td>
<td align="right">3,811,000</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">23,126,840</td>
<td align="right">30,789,360</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">34,556,920</td>
<td align="right">45,298,320</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,646,700</td>
<td align="right">3,461,980</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,813,820</td>
<td align="right">18,053,680</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,476,040</td>
<td align="right">4,450,580</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,022,240</td>
<td align="right">3,616,180</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">2,052,100</td>
<td align="right">2,582,900</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,554,660</td>
<td align="right">3,213,380</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">4,893,260</td>
<td align="right">3,640,220</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">20,975,580</td>
<td align="right">26,088,640</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,919,180</td>
<td align="right">3,731,300</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,835,300</td>
<td align="right">47,184,080</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">38,835,300</td>
<td align="right">47,184,080</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">16,585,140</td>
<td align="right">20,135,300</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">91,575,000</td>
<td align="right">111,082,660</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">5,423,600</td>
<td align="right">6,525,520</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,520,640</td>
<td align="right">5,426,460</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">22,983,120</td>
<td align="right">27,579,220</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">40,458,280</td>
<td align="right">48,102,380</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">11,150,980</td>
<td align="right">9,122,600</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">6,690,720</td>
<td align="right">5,484,880</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,334,280</td>
<td align="right">1,573,500</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">6,690,720</td>
<td align="right">5,500,040</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">6,690,720</td>
<td align="right">5,508,500</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">13,855,300</td>
<td align="right">16,257,920</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,056,620</td>
<td align="right">2,397,980</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">5,419,280</td>
<td align="right">4,523,340</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,089,500</td>
<td align="right">3,553,200</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">64,130,280</td>
<td align="right">73,751,800</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">52,755,740</td>
<td align="right">60,602,600</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">44,420,660</td>
<td align="right">50,996,460</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">80,551,320</td>
<td align="right">92,115,240</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,659,700</td>
<td align="right">4,853,240</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,676,180</td>
<td align="right">4,868,420</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">6,177,340</td>
<td align="right">5,300,700</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">5,679,300</td>
<td align="right">4,875,700</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">47,818,200</td>
<td align="right">54,334,040</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">3,840,320</td>
<td align="right">4,361,060</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">13,544,100</td>
<td align="right">15,349,180</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">14,694,680</td>
<td align="right">16,627,620</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">32,027,560</td>
<td align="right">35,949,180</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">14,139,920</td>
<td align="right">15,791,620</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,161,600</td>
<td align="right">16,927,780</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,395,180</td>
<td align="right">2,673,200</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,840</td>
<td align="right">114,800</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,732,280</td>
<td align="right">14,031,100</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,881,740</td>
<td align="right">16,346,900</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,702,520</td>
<td align="right">11,483,480</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">689,484,080</td>
<td align="right">755,266,740</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">836,795,580</td>
<td align="right">911,995,020</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">30,113,300</td>
<td align="right">32,782,140</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">229,733,180</td>
<td align="right">249,671,400</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">229,596,880</td>
<td align="right">249,379,680</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">25,840,580</td>
<td align="right">28,016,540</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">16,480</td>
<td align="right">15,180</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">13,484,400</td>
<td align="right">14,528,300</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">13,484,400</td>
<td align="right">14,528,300</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">271,316,500</td>
<td align="right">292,122,360</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">8,859,360</td>
<td align="right">8,191,860</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">14,096,400</td>
<td align="right">15,146,080</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">40,724,800</td>
<td align="right">43,734,480</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,781,620</td>
<td align="right">26,602,540</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">29,726,580</td>
<td align="right">31,891,320</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,708,180</td>
<td align="right">3,976,080</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">49,440</td>
<td align="right">45,960</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,980</td>
<td align="right">13,000</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,108,300</td>
<td align="right">13,985,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">40,699,120</td>
<td align="right">43,406,680</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">49,440</td>
<td align="right">46,200</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,837,020</td>
<td align="right">4,084,740</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">63,036,080</td>
<td align="right">67,057,100</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">167,778,900</td>
<td align="right">177,483,280</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,950,440</td>
<td align="right">16,195,080</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">3,820,800</td>
<td align="right">3,969,680</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">17,977,600</td>
<td align="right">18,646,060</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,881,980</td>
<td align="right">12,253,960</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">15,246,200</td>
<td align="right">15,670,280</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">18,688,720</td>
<td align="right">19,206,560</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">15,339,920</td>
<td align="right">15,731,300</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,940,860</td>
<td align="right">56,282,240</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">54,940,860</td>
<td align="right">56,282,240</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">13,980</td>
<td align="right">13,640</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">44,906,680</td>
<td align="right">45,939,580</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">30,110,300</td>
<td align="right">30,780,160</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">41,583,320</td>
<td align="right">42,450,960</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,749,480</td>
<td align="right">9,841,300</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">34,252,400</td>
<td align="right">34,562,500</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">26,960,440</td>
<td align="right">27,187,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">238,633,860</td>
<td align="right">236,838,200</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">35,996,160</td>
<td align="right">36,253,160</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">23,008,720</td>
<td align="right">22,859,220</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">9,375,740</td>
<td align="right">9,332,200</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">63,894,920</td>
<td align="right">64,130,580</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">19,982,520</td>
<td align="right">19,994,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,788,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,112,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">358,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">58,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">11,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right"></td>
<td align="right">11,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">11,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right"></td>
<td align="right">11,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">11,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">11,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">8,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">600</td>
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
<td align="right">1,400</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right">300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">80</td>
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
Stats gathered on: 2025-07-01
