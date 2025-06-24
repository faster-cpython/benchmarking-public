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
<td align="right">860,740</td>
<td align="right">2,368,940</td>
<td align="right">175.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,917,560</td>
<td align="right">1,048,080</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,394,120</td>
<td align="right">1,728,820</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,986,120</td>
<td align="right">589,220</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,592,180</td>
<td align="right">895,700</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">91,000</td>
<td align="right">33,860</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,885,920</td>
<td align="right">1,160,620</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,638,880</td>
<td align="right">8,831,040</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,722,040</td>
<td align="right">5,787,700</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,801,320</td>
<td align="right">14,583,500</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">740,040</td>
<td align="right">518,700</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,986,120</td>
<td align="right">7,286,900</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,194,440</td>
<td align="right">13,339,840</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">724,260</td>
<td align="right">534,060</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">848,400</td>
<td align="right">627,060</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,052,640</td>
<td align="right">20,922,140</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">93,384,280</td>
<td align="right">72,647,400</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,958,300</td>
<td align="right">3,871,400</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,209,260</td>
<td align="right">3,345,060</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,098,780</td>
<td align="right">13,603,300</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,892,920</td>
<td align="right">17,109,940</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,783,840</td>
<td align="right">4,820,880</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,163,240</td>
<td align="right">7,760,140</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">43,578,580</td>
<td align="right">49,532,780</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,263,600</td>
<td align="right">4,592,300</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">553,960</td>
<td align="right">484,680</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,820</td>
<td align="right">7,760</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,875,640</td>
<td align="right">18,428,400</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">110,510,060</td>
<td align="right">98,299,160</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">25,043,600</td>
<td align="right">22,286,040</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">701,800</td>
<td align="right">625,720</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,059,440</td>
<td align="right">10,800,100</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,161,320</td>
<td align="right">71,799,100</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">146,840</td>
<td align="right">132,920</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,280,420</td>
<td align="right">9,331,600</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,424,580</td>
<td align="right">3,124,460</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">14,971,460</td>
<td align="right">13,675,200</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">10,658,300</td>
<td align="right">9,741,600</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">34,499,600</td>
<td align="right">31,757,900</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">203,191,340</td>
<td align="right">187,228,700</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,686,920</td>
<td align="right">2,487,160</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,974,640</td>
<td align="right">4,612,100</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">184,569,140</td>
<td align="right">171,397,280</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">36,527,120</td>
<td align="right">34,035,020</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">112,437,680</td>
<td align="right">105,317,620</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">4,440</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,066,120</td>
<td align="right">2,877,180</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">47,669,740</td>
<td align="right">44,826,620</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">204,297,180</td>
<td align="right">192,165,880</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">191,559,100</td>
<td align="right">180,415,220</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">37,289,020</td>
<td align="right">39,453,040</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">55,860</td>
<td align="right">52,680</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">51,287,120</td>
<td align="right">48,384,580</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">311,590,100</td>
<td align="right">294,122,160</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">198,351,640</td>
<td align="right">187,949,180</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,902,400</td>
<td align="right">7,504,500</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,197,077,060</td>
<td align="right">1,143,276,720</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">19,075,820</td>
<td align="right">18,256,880</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">75,758,180</td>
<td align="right">72,520,440</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">298,559,920</td>
<td align="right">286,376,920</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,443,200</td>
<td align="right">1,385,880</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,700,940</td>
<td align="right">9,337,080</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">146,321,740</td>
<td align="right">141,189,200</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,755,640</td>
<td align="right">3,624,920</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,612,340</td>
<td align="right">49,964,980</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320,828,480</td>
<td align="right">311,008,060</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,362,780</td>
<td align="right">2,292,720</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">19,601,760</td>
<td align="right">19,093,920</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">36,521,800</td>
<td align="right">35,621,400</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">379,462,420</td>
<td align="right">370,496,180</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,890,460</td>
<td align="right">22,364,860</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,537,940</td>
<td align="right">16,180,680</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">77,501,200</td>
<td align="right">75,929,780</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">16,860,560</td>
<td align="right">16,522,900</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">49,701,180</td>
<td align="right">50,645,220</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">304,741,280</td>
<td align="right">298,979,120</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">178,372,420</td>
<td align="right">175,200,000</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">60,075,100</td>
<td align="right">59,020,300</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,605,620</td>
<td align="right">8,455,440</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,700,000</td>
<td align="right">4,627,220</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">124,098,580</td>
<td align="right">125,921,920</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,077,980</td>
<td align="right">29,692,360</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,095,620</td>
<td align="right">29,710,000</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">18,749,460</td>
<td align="right">18,527,940</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">25,948,080</td>
<td align="right">26,199,740</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,031,240</td>
<td align="right">2,011,900</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">120,171,440</td>
<td align="right">119,122,780</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,444,760</td>
<td align="right">33,154,200</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">30,785,960</td>
<td align="right">31,049,520</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">103,081,020</td>
<td align="right">102,227,580</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">19,903,420</td>
<td align="right">19,753,700</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,166,380</td>
<td align="right">22,995,660</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">67,406,440</td>
<td align="right">66,919,500</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,693,560</td>
<td align="right">1,682,360</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">36,530,440</td>
<td align="right">36,306,260</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,117,940</td>
<td align="right">7,084,440</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,265,260</td>
<td align="right">49,044,860</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,162,480</td>
<td align="right">19,077,920</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,365,600</td>
<td align="right">11,321,260</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,808,580</td>
<td align="right">3,794,560</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">116,234,940</td>
<td align="right">115,808,060</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,160,280</td>
<td align="right">92,966,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">34,478,200</td>
<td align="right">34,426,780</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">150,880,760</td>
<td align="right">150,893,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">4,587,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,116,580</td>
<td align="right">15,116,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">41,711,700</td>
<td align="right">41,711,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,687,720</td>
<td align="right">38,687,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,133,580</td>
<td align="right">37,133,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,888,420</td>
<td align="right">36,888,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,105,440</td>
<td align="right">22,105,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">9,619,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,364,240</td>
<td align="right">8,364,240</td>
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
<td align="right">7,146,480</td>
<td align="right">7,146,480</td>
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
<td align="right">4,979,940</td>
<td align="right">4,979,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,202,460</td>
<td align="right">4,202,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,840,600</td>
<td align="right">2,840,600</td>
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
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,134,820</td>
<td align="right">1,134,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">440,400</td>
<td align="right">440,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">351,240</td>
<td align="right">351,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,120</td>
<td align="right">267,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">228,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">213,240</td>
<td align="right">213,240</td>
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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">73,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">29,580</td>
<td align="right">29,580</td>
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
<td align="right">25,680</td>
<td align="right">25,680</td>
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
<td align="left">CALL</td>
<td align="right">3,960</td>
<td align="right">3,960</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
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
<td align="right">23,062,640</td>
<td align="right">11.8%</td>
<td align="right">22,891,960</td>
<td align="right">11.7%</td>
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
<td align="right">167,392,020</td>
<td align="right">85.6%</td>
<td align="right">167,392,020</td>
<td align="right">85.7%</td>
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
<td align="right">5,034,880</td>
<td align="right">2.6%</td>
<td align="right">5,034,880</td>
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
<td align="right">102,900</td>
<td align="right">51.8%</td>
<td align="right">102,860</td>
<td align="right">51.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">95,800</td>
<td align="right">48.2%</td>
<td align="right">95,800</td>
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
<td align="left">add other</td>
<td align="right">3,200</td>
<td align="right">3.1%</td>
<td align="right">3,180</td>
<td align="right">3.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">4,980</td>
<td align="right">4.8%</td>
<td align="right">4,960</td>
<td align="right">4.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">83,060</td>
<td align="right">80.7%</td>
<td align="right">83,060</td>
<td align="right">80.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,560</td>
<td align="right">7.3%</td>
<td align="right">7,560</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">3.1%</td>
<td align="right">3,160</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">0.2%</td>
<td align="right">240</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
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
<td align="right">10,280,420</td>
<td align="right">100.0%</td>
<td align="right">9,331,600</td>
<td align="right">100.0%</td>
<td align="right">-9.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,413,200</td>
<td align="right">3.0%</td>
<td align="right">17,231,620</td>
<td align="right">3.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">17,747,920</td>
<td align="right">3.1%</td>
<td align="right">17,562,860</td>
<td align="right">3.1%</td>
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
<td align="right">553,389,080</td>
<td align="right">96.9%</td>
<td align="right">553,770,980</td>
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
<td align="right">338,680</td>
<td align="right">100.0%</td>
<td align="right">335,200</td>
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
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">1,680,260</td>
<td align="right">4.6%</td>
<td align="right">1,669,060</td>
<td align="right">4.5%</td>
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
<td align="right">34,780,220</td>
<td align="right">94.7%</td>
<td align="right">34,780,220</td>
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
<td align="right">12,960</td>
<td align="right">71.3%</td>
<td align="right">12,960</td>
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
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">12,500</td>
<td align="right">96.5%</td>
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
<td align="right">8,717,140</td>
<td align="right">13.8%</td>
<td align="right">5,783,440</td>
<td align="right">9.6%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,353,340</td>
<td align="right">86.2%</td>
<td align="right">54,353,340</td>
<td align="right">90.4%</td>
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
<td align="right">4,780</td>
<td align="right">97.6%</td>
<td align="right">4,140</td>
<td align="right">97.2%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.4%</td>
<td align="right">120</td>
<td align="right">2.8%</td>
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
<td align="right">1,880</td>
<td align="right">39.3%</td>
<td align="right">1,460</td>
<td align="right">35.3%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">920</td>
<td align="right">19.2%</td>
<td align="right">800</td>
<td align="right">19.3%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,180</td>
<td align="right">24.7%</td>
<td align="right">1,080</td>
<td align="right">26.1%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">800</td>
<td align="right">19.3%</td>
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
<td align="right">21,795,140</td>
<td align="right">10.3%</td>
<td align="right">14,578,860</td>
<td align="right">7.7%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">156,456,580</td>
<td align="right">74.1%</td>
<td align="right">142,690,680</td>
<td align="right">75.1%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,835,560</td>
<td align="right">15.6%</td>
<td align="right">32,642,660</td>
<td align="right">17.2%</td>
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
<td align="left">Failure</td>
<td align="right">6,180</td>
<td align="right">1.0%</td>
<td align="right">4,640</td>
<td align="right">0.7%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">619,520</td>
<td align="right">99.0%</td>
<td align="right">615,880</td>
<td align="right">99.3%</td>
<td align="right">-0.6%</td>
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
<td align="right">400</td>
<td align="right">6.5%</td>
<td align="right">60</td>
<td align="right">1.3%</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">440</td>
<td align="right">7.1%</td>
<td align="right">160</td>
<td align="right">3.4%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,040</td>
<td align="right">16.8%</td>
<td align="right">680</td>
<td align="right">14.7%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,280</td>
<td align="right">20.7%</td>
<td align="right">880</td>
<td align="right">19.0%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">3.6%</td>
<td align="right">180</td>
<td align="right">3.9%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">9.1%</td>
<td align="right">480</td>
<td align="right">10.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,080</td>
<td align="right">33.7%</td>
<td align="right">2,040</td>
<td align="right">44.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.9%</td>
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
<td align="right">48,398,760</td>
<td align="right">48,398,760 / 0 !!</td>
<td align="right">48,398,760</td>
<td align="right">48,398,760 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">36,919,140</td>
<td align="right">36,919,140 / 0 !!</td>
<td align="right">36,919,140</td>
<td align="right">36,919,140 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">29,110,020</td>
<td align="right">29,110,020 / 0 !!</td>
<td align="right">29,110,020</td>
<td align="right">29,110,020 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,964,960</td>
<td align="right">5,964,960 / 0 !!</td>
<td align="right">5,964,960</td>
<td align="right">5,964,960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,162,220</td>
<td align="right">2,162,220 / 0 !!</td>
<td align="right">2,162,220</td>
<td align="right">2,162,220 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">200,280</td>
<td align="right">200,280 / 0 !!</td>
<td align="right">200,280</td>
<td align="right">200,280 / 0 !!</td>
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
<td align="right">55,380</td>
<td align="right">55,380 / 0 !!</td>
<td align="right">55,380</td>
<td align="right">55,380 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,900</td>
<td align="right">3,900 / 0 !!</td>
<td align="right">3,900</td>
<td align="right">3,900 / 0 !!</td>
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
<td align="right">645,089,140</td>
<td align="right">63.0%</td>
<td align="right">631,300,460</td>
<td align="right">62.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">275,230,080</td>
<td align="right">26.9%</td>
<td align="right">272,794,580</td>
<td align="right">27.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,424,600</td>
<td align="right">10.0%</td>
<td align="right">101,597,380</td>
<td align="right">10.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">5,134,480</td>
<td align="right">99.6%</td>
<td align="right">5,088,400</td>
<td align="right">99.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,180</td>
<td align="right">0.4%</td>
<td align="right">21,320</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
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
<td align="right">640</td>
<td align="right">3.0%</td>
<td align="right">620</td>
<td align="right">2.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">10,220</td>
<td align="right">48.3%</td>
<td align="right">10,500</td>
<td align="right">49.2%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,860</td>
<td align="right">22.9%</td>
<td align="right">4,780</td>
<td align="right">22.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">13.4%</td>
<td align="right">2,840</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">1.9%</td>
<td align="right">400</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">180</td>
<td align="right">0.8%</td>
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
<td align="right">274,107,680</td>
<td align="right">100.0%</td>
<td align="right">260,467,480</td>
<td align="right">100.0%</td>
<td align="right">-5.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,167,640</td>
<td align="right">38.3%</td>
<td align="right">47,180,760</td>
<td align="right">38.3%</td>
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
<td align="right">53,793,780</td>
<td align="right">43.7%</td>
<td align="right">53,780,400</td>
<td align="right">43.7%</td>
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
<td align="right">22,092,060</td>
<td align="right">18.0%</td>
<td align="right">22,092,060</td>
<td align="right">18.0%</td>
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
<td align="right">1,015,500</td>
<td align="right">98.7%</td>
<td align="right">1,015,240</td>
<td align="right">98.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,980</td>
<td align="right">1.3%</td>
<td align="right">12,980</td>
<td align="right">1.3%</td>
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
<td align="right">1,000</td>
<td align="right">7.7%</td>
<td align="right">960</td>
<td align="right">7.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
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
<td align="right">4,583,800</td>
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
<td align="right">7,792,740</td>
<td align="right">2.9%</td>
<td align="right">7,609,320</td>
<td align="right">2.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">252,971,480</td>
<td align="right">95.6%</td>
<td align="right">247,306,860</td>
<td align="right">95.6%</td>
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
<td align="right">3,640,700</td>
<td align="right">1.4%</td>
<td align="right">3,626,680</td>
<td align="right">1.4%</td>
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
<td align="right">147,900</td>
<td align="right">47.0%</td>
<td align="right">144,420</td>
<td align="right">46.4%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">166,980</td>
<td align="right">53.0%</td>
<td align="right">166,980</td>
<td align="right">53.6%</td>
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
<td align="right">2,340</td>
<td align="right">1.4%</td>
<td align="right">2,340</td>
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
<td align="right">48,300,460</td>
<td align="right">100.0%</td>
<td align="right">48,300,460</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,406,311,160</td>
<td align="right">34.5%</td>
<td align="right">2,246,925,660</td>
<td align="right">33.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">319,691,540</td>
<td align="right">4.6%</td>
<td align="right">306,492,460</td>
<td align="right">4.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,864,457,900</td>
<td align="right">55.3%</td>
<td align="right">3,732,133,260</td>
<td align="right">55.9%</td>
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
<td align="right">392,709,120</td>
<td align="right">5.6%</td>
<td align="right">389,698,720</td>
<td align="right">5.8%</td>
<td align="right">-0.8%</td>
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
<td align="right">8,717,140</td>
<td align="right">4.0%</td>
<td align="right">5,783,440</td>
<td align="right">2.8%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,795,140</td>
<td align="right">10.1%</td>
<td align="right">14,578,860</td>
<td align="right">7.2%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,280,420</td>
<td align="right">4.8%</td>
<td align="right">9,331,600</td>
<td align="right">4.6%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,413,200</td>
<td align="right">8.1%</td>
<td align="right">17,231,620</td>
<td align="right">8.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">102,424,600</td>
<td align="right">47.4%</td>
<td align="right">101,597,380</td>
<td align="right">49.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,062,640</td>
<td align="right">10.7%</td>
<td align="right">22,891,960</td>
<td align="right">11.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,680,260</td>
<td align="right">0.8%</td>
<td align="right">1,669,060</td>
<td align="right">0.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,640,700</td>
<td align="right">1.7%</td>
<td align="right">3,626,680</td>
<td align="right">1.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">2.1%</td>
<td align="right">4,583,800</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,092,060</td>
<td align="right">10.2%</td>
<td align="right">22,092,060</td>
<td align="right">10.8%</td>
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
<td align="right">32,176,580</td>
<td align="right">8.2%</td>
<td align="right">33,229,880</td>
<td align="right">8.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">84,527,280</td>
<td align="right">21.5%</td>
<td align="right">82,725,500</td>
<td align="right">21.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,354,720</td>
<td align="right">1.1%</td>
<td align="right">4,268,360</td>
<td align="right">1.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">99,675,880</td>
<td align="right">25.4%</td>
<td align="right">98,155,120</td>
<td align="right">25.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,764,900</td>
<td align="right">2.5%</td>
<td align="right">9,859,140</td>
<td align="right">2.5%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">48,749,360</td>
<td align="right">12.4%</td>
<td align="right">49,046,640</td>
<td align="right">12.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,417,940</td>
<td align="right">4.2%</td>
<td align="right">16,321,480</td>
<td align="right">4.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">16,417,620</td>
<td align="right">4.2%</td>
<td align="right">16,321,180</td>
<td align="right">4.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,790,600</td>
<td align="right">13.7%</td>
<td align="right">53,777,220</td>
<td align="right">13.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">1.9%</td>
<td align="right">7,565,220</td>
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
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,780,260</td>
<td align="right">88.8%</td>
<td align="right">314,780,260</td>
<td align="right">88.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,386,960</td>
<td align="right">11.1%</td>
<td align="right">39,386,960</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">343,140</td>
<td align="right">0.1%</td>
<td align="right">343,140</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,383,480</td>
<td align="right">11.1%</td>
<td align="right">39,383,480</td>
<td align="right">11.1%</td>
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
<td align="right">13,630,620</td>
<td align="right">3.8%</td>
<td align="right">13,630,620</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
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
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,583,080</td>
<td align="right">88.5%</td>
<td align="right">313,583,080</td>
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
<td align="right">2,227,658</td>
<td align="right"></td>
<td align="right">1,944,771</td>
<td align="right"></td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">492,400</td>
<td align="right">0.1%</td>
<td align="right">519,300</td>
<td align="right">0.1%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,404,989</td>
<td align="right"></td>
<td align="right">34,746,358</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,583,890,100</td>
<td align="right">29.9%</td>
<td align="right">1,520,843,940</td>
<td align="right">28.7%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">34,938,272</td>
<td align="right"></td>
<td align="right">33,562,685</td>
<td align="right"></td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,130,662,900</td>
<td align="right">40.2%</td>
<td align="right">2,198,379,623</td>
<td align="right">41.4%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,981,479,852</td>
<td align="right">35.3%</td>
<td align="right">2,033,412,328</td>
<td align="right">36.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,246,946,160</td>
<td align="right">40.1%</td>
<td align="right">2,199,764,120</td>
<td align="right">39.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">182,160,020</td>
<td align="right">3.4%</td>
<td align="right">179,384,000</td>
<td align="right">3.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,980</td>
<td align="right">0.1%</td>
<td align="right">348,380</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">195,256,582</td>
<td align="right"></td>
<td align="right">196,601,189</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,190,600</td>
<td align="right">1.6%</td>
<td align="right">89,747,900</td>
<td align="right">1.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">454,101,188</td>
<td align="right"></td>
<td align="right">455,126,955</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,404,759,996</td>
<td align="right">26.5%</td>
<td align="right">1,407,824,348</td>
<td align="right">26.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,289,762,064</td>
<td align="right">23.0%</td>
<td align="right">1,290,259,310</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">289,854,280</td>
<td align="right">48.5%</td>
<td align="right">289,777,100</td>
<td align="right">48.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">306,764,440</td>
<td align="right">51.3%</td>
<td align="right">306,842,380</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">306,765,340</td>
<td align="right"></td>
<td align="right">306,833,260</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">290,691,660</td>
<td align="right">48.7%</td>
<td align="right">290,644,780</td>
<td align="right">48.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">327,178,362</td>
<td align="right"></td>
<td align="right">327,158,945</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,543,020</td>
<td align="right"></td>
<td align="right">10,543,020</td>
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
<td align="right">25,920</td>
<td align="right">73,203,060</td>
<td align="right">1,161,866,163</td>
<td align="right">45,238,680</td>
<td align="right">100,674,900</td>
<td align="right">25,880</td>
<td align="right">73,214,120</td>
<td align="right">1,161,841,389</td>
<td align="right">44,629,420</td>
<td align="right">101,834,660</td>
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
<td align="right">1,000</td>
<td align="right">1.0%</td>
<td align="right">4,900.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">1,040</td>
<td align="right">1.0%</td>
<td align="right">550.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">740</td>
<td align="right">2.4%</td>
<td align="right">4,120</td>
<td align="right">4.0%</td>
<td align="right">456.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">8,780</td>
<td align="right">28.1%</td>
<td align="right">42,700</td>
<td align="right">41.0%</td>
<td align="right">386.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">7,140</td>
<td align="right">22.9%</td>
<td align="right">32,360</td>
<td align="right">31.0%</td>
<td align="right">353.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">180</td>
<td align="right">0.6%</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">311.1%</td>
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
<td align="right">1,120</td>
<td align="right">1.1%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">31,240</td>
<td align="right"></td>
<td align="right">104,260</td>
<td align="right"></td>
<td align="right">233.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">14,400</td>
<td align="right">46.1%</td>
<td align="right">24,340</td>
<td align="right">23.3%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,691,006,620</td>
<td align="right">1,908.4%</td>
<td align="right">5,513,654,520</td>
<td align="right">2,243.7%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">245,811,560</td>
<td align="right"></td>
<td align="right">245,737,860</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">5,920</td>
<td align="right">67.4%</td>
<td align="right">36,900</td>
<td align="right">86.4%</td>
<td align="right">523.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">8,780</td>
<td align="right"></td>
<td align="right">42,700</td>
<td align="right"></td>
<td align="right">386.3%</td>
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
<td align="right">0.0%</td>
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
<td align="right">12,516,600</td>
<td align="right">16.3%</td>
<td align="right">78,752,960</td>
<td align="right">18.2%</td>
<td align="right">529.2%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,591,840</td>
<td align="right">2.1%</td>
<td align="right">9,178,560</td>
<td align="right">2.1%</td>
<td align="right">476.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">76,922,880</td>
<td align="right"></td>
<td align="right">433,029,120</td>
<td align="right"></td>
<td align="right">462.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">62,814,440</td>
<td align="right">81.7%</td>
<td align="right">345,097,600</td>
<td align="right">79.7%</td>
<td align="right">449.4%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">115,425,280</td>
<td align="right">26.7%</td>
<td align="right">115,425,280 / 0 !!</td>
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
<td align="left">1,060</td>
<td align="right">17.9%</td>
<td align="left">6,020</td>
<td align="right">16.3%</td>
<td align="right">467.9%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">1,900</td>
<td align="right">32.1%</td>
<td align="left">15,560</td>
<td align="right">42.2%</td>
<td align="right">718.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">2,020</td>
<td align="right">34.1%</td>
<td align="left">10,480</td>
<td align="right">28.4%</td>
<td align="right">418.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">700</td>
<td align="right">11.8%</td>
<td align="left">4,180</td>
<td align="right">11.3%</td>
<td align="right">497.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">240</td>
<td align="right">4.1%</td>
<td align="left">580</td>
<td align="right">1.6%</td>
<td align="right">141.7%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">2,020</td>
<td align="right">4.7%</td>
<td align="right">10,000.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,320</td>
<td align="right">15.0%</td>
<td align="right">5,780</td>
<td align="right">13.5%</td>
<td align="right">337.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,100</td>
<td align="right">35.3%</td>
<td align="right">18,980</td>
<td align="right">44.4%</td>
<td align="right">512.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">620</td>
<td align="right">7.1%</td>
<td align="right">5,820</td>
<td align="right">13.6%</td>
<td align="right">838.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,340</td>
<td align="right">38.0%</td>
<td align="right">8,160</td>
<td align="right">19.1%</td>
<td align="right">144.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">320</td>
<td align="right">3.6%</td>
<td align="right">1,200</td>
<td align="right">2.8%</td>
<td align="right">275.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">400</td>
<td align="right">0.9%</td>
<td align="right">566.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">340</td>
<td align="right">0.8%</td>
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
<td align="left"><= 4</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">720</td>
<td align="right">1.7%</td>
<td align="right">720 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">340</td>
<td align="right">3.9%</td>
<td align="right">2,920</td>
<td align="right">6.8%</td>
<td align="right">758.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,520</td>
<td align="right">28.7%</td>
<td align="right">15,200</td>
<td align="right">35.6%</td>
<td align="right">503.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,960</td>
<td align="right">22.3%</td>
<td align="right">12,340</td>
<td align="right">28.9%</td>
<td align="right">529.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">480</td>
<td align="right">5.5%</td>
<td align="right">3,860</td>
<td align="right">9.0%</td>
<td align="right">704.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">500</td>
<td align="right">5.7%</td>
<td align="right">1,380</td>
<td align="right">3.2%</td>
<td align="right">176.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">380</td>
<td align="right">0.9%</td>
<td align="right">280.0%</td>
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
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">2,920</td>
<td align="right">60,240</td>
<td align="right">1,963.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">2,920</td>
<td align="right">60,240</td>
<td align="right">1,963.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,000</td>
<td align="right">47,340</td>
<td align="right">1,478.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,800</td>
<td align="right">1,812,840</td>
<td align="right">1,206.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">37,820</td>
<td align="right">435,720</td>
<td align="right">1,052.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">37,820</td>
<td align="right">435,720</td>
<td align="right">1,052.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">21,040</td>
<td align="right">191,720</td>
<td align="right">811.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">37,300</td>
<td align="right">337,420</td>
<td align="right">804.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">51,280</td>
<td align="right">408,540</td>
<td align="right">696.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">131,620</td>
<td align="right">1,032,640</td>
<td align="right">684.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">16,980</td>
<td align="right">118,460</td>
<td align="right">597.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">241,740</td>
<td align="right">1,671,220</td>
<td align="right">591.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">18,740</td>
<td align="right">96,280</td>
<td align="right">413.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,980</td>
<td align="right">71,120</td>
<td align="right">408.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">36,160</td>
<td align="right">155,820</td>
<td align="right">330.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,160</td>
<td align="right">155,820</td>
<td align="right">330.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">323,700</td>
<td align="right">1,371,060</td>
<td align="right">323.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,830,080</td>
<td align="right">7,679,040</td>
<td align="right">319.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">49,440</td>
<td align="right">199,620</td>
<td align="right">303.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">49,440</td>
<td align="right">199,620</td>
<td align="right">303.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">306,280</td>
<td align="right">1,234,620</td>
<td align="right">303.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">16,480</td>
<td align="right">66,360</td>
<td align="right">302.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">254,040</td>
<td align="right">297.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">129,920</td>
<td align="right">515,540</td>
<td align="right">296.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">129,920</td>
<td align="right">515,540</td>
<td align="right">296.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">36,000</td>
<td align="right">140,940</td>
<td align="right">291.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">36,040</td>
<td align="right">140,600</td>
<td align="right">290.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">17,500</td>
<td align="right">67,440</td>
<td align="right">285.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">36,040</td>
<td align="right">138,540</td>
<td align="right">284.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">36,040</td>
<td align="right">138,540</td>
<td align="right">284.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">303,720</td>
<td align="right">268.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">303,720</td>
<td align="right">268.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">387,500</td>
<td align="right">1,334,820</td>
<td align="right">244.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,896,240</td>
<td align="right">6,405,720</td>
<td align="right">237.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,593,540</td>
<td align="right">8,724,040</td>
<td align="right">236.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">41,600</td>
<td align="right">137,780</td>
<td align="right">231.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">681,060</td>
<td align="right">2,206,260</td>
<td align="right">223.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">298,600</td>
<td align="right">922,000</td>
<td align="right">208.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">387,500</td>
<td align="right">1,188,340</td>
<td align="right">206.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,712,160</td>
<td align="right">5,055,640</td>
<td align="right">195.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">869,760</td>
<td align="right">2,566,240</td>
<td align="right">195.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">869,760</td>
<td align="right">2,566,240</td>
<td align="right">195.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">848,080</td>
<td align="right">2,496,220</td>
<td align="right">194.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">864,560</td>
<td align="right">2,427,940</td>
<td align="right">180.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">2,223,380</td>
<td align="right">5,435,080</td>
<td align="right">144.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,781,820</td>
<td align="right">18,878,720</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,921,600</td>
<td align="right">4,368,840</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">154,320</td>
<td align="right">343,260</td>
<td align="right">122.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">154,320</td>
<td align="right">343,260</td>
<td align="right">122.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,093,840</td>
<td align="right">8,948,440</td>
<td align="right">118.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">154,160</td>
<td align="right">336,700</td>
<td align="right">118.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">300,160</td>
<td align="right">637,820</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">931,260</td>
<td align="right">1,977,700</td>
<td align="right">112.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,229,020</td>
<td align="right">10,991,180</td>
<td align="right">110.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">187,200</td>
<td align="right">386,960</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">181,860</td>
<td align="right">375,300</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">181,860</td>
<td align="right">375,300</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,856,200</td>
<td align="right">7,853,000</td>
<td align="right">103.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,765,240</td>
<td align="right">5,464,460</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,089,840</td>
<td align="right">23,726,600</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">17,034,500</td>
<td align="right">33,205,140</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">11,959,680</td>
<td align="right">23,025,600</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,005,800</td>
<td align="right">5,763,360</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">13,326,980</td>
<td align="right">25,339,980</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,481,940</td>
<td align="right">6,415,640</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">466,220</td>
<td align="right">828,760</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,424,360</td>
<td align="right">6,013,920</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,084,180</td>
<td align="right">31,677,780</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">19,084,180</td>
<td align="right">31,677,780</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">18,929,860</td>
<td align="right">31,334,520</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">18,814,060</td>
<td align="right">30,996,460</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">20,288,420</td>
<td align="right">32,817,480</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">118,160</td>
<td align="right">188,220</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">118,160</td>
<td align="right">187,440</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">388,200</td>
<td align="right">609,720</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">138,800</td>
<td align="right">214,880</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">19,203,400</td>
<td align="right">28,354,260</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,470,700</td>
<td align="right">2,142,000</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">109,940</td>
<td align="right">61,720</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">4,469,600</td>
<td align="right">6,322,120</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">2,348,740</td>
<td align="right">3,297,560</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">41,587,320</td>
<td align="right">58,068,960</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">41,587,320</td>
<td align="right">58,068,860</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">218,480</td>
<td align="right">303,040</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,318,620</td>
<td align="right">4,577,960</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">41,619,160</td>
<td align="right">57,047,700</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,841,220</td>
<td align="right">3,889,880</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">16,312,620</td>
<td align="right">22,298,500</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">13,818,980</td>
<td align="right">18,484,280</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">25,500,000</td>
<td align="right">34,070,120</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">39,456,460</td>
<td align="right">51,407,240</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,884,860</td>
<td align="right">6,287,960</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">3,258,500</td>
<td align="right">2,334,320</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">9,457,360</td>
<td align="right">12,120,920</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">92,948,780</td>
<td align="right">118,258,420</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,061,540</td>
<td align="right">16,557,020</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">45,094,880</td>
<td align="right">57,154,120</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">50,204,500</td>
<td align="right">63,590,700</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,557,360</td>
<td align="right">15,888,180</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">6,884,060</td>
<td align="right">8,684,980</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">16,381,540</td>
<td align="right">20,641,600</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,071,260</td>
<td align="right">67,445,340</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">44,075,860</td>
<td align="right">53,804,000</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,632,860</td>
<td align="right">5,650,280</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">3,375,180</td>
<td align="right">2,640,800</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,412,960</td>
<td align="right">2,920,800</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">25,432,140</td>
<td align="right">30,747,060</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">29,994,560</td>
<td align="right">36,210,580</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,501,860</td>
<td align="right">5,386,420</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">81,503,560</td>
<td align="right">97,151,120</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">168,196,060</td>
<td align="right">198,993,360</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">697,042,140</td>
<td align="right">822,159,100</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">69,915,840</td>
<td align="right">82,221,660</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,464,380</td>
<td align="right">2,891,260</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,413,860</td>
<td align="right">20,388,600</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">854,220,040</td>
<td align="right">999,315,020</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">109,940</td>
<td align="right">128,060</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">3,244,360</td>
<td align="right">2,747,460</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">7,505,080</td>
<td align="right">8,587,400</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">15,849,380</td>
<td align="right">18,064,940</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">7,674,200</td>
<td align="right">8,729,000</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">3,777,900</td>
<td align="right">3,267,180</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">27,344,760</td>
<td align="right">30,973,540</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">34,582,480</td>
<td align="right">39,102,200</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">15,776,800</td>
<td align="right">17,825,580</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">59,988,100</td>
<td align="right">67,445,340</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">40,652,720</td>
<td align="right">45,460,560</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">40,627,040</td>
<td align="right">45,314,040</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,342,120</td>
<td align="right">17,023,120</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,964,880</td>
<td align="right">4,383,540</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">39,162,900</td>
<td align="right">35,464,440</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">61,240,520</td>
<td align="right">66,917,400</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">32,759,700</td>
<td align="right">35,781,260</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">33,093,620</td>
<td align="right">36,143,600</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">12,013,220</td>
<td align="right">13,110,720</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">15,495,840</td>
<td align="right">16,892,740</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">45,115,060</td>
<td align="right">49,159,640</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">17,066,300</td>
<td align="right">18,574,240</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">4,050,420</td>
<td align="right">4,404,460</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">15,403,900</td>
<td align="right">16,655,180</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">236,774,840</td>
<td align="right">253,916,020</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,030,040</td>
<td align="right">4,320,600</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">214,420</td>
<td align="right">228,340</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,838,240</td>
<td align="right">15,738,260</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">14,959,240</td>
<td align="right">15,778,180</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">14,959,240</td>
<td align="right">15,778,180</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">22,122,080</td>
<td align="right">23,315,380</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">287,430,720</td>
<td align="right">302,785,560</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">61,810,400</td>
<td align="right">64,845,780</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">4,947,660</td>
<td align="right">5,171,840</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">4,947,660</td>
<td align="right">5,146,080</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">4,226,960</td>
<td align="right">4,376,680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,438,200</td>
<td align="right">15,935,480</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,053,260</td>
<td align="right">14,704,320</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">34,202,240</td>
<td align="right">34,988,200</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,856,580</td>
<td align="right">10,076,980</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">30,181,380</td>
<td align="right">30,738,360</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">26,857,240</td>
<td align="right">27,332,900</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">15,775,740</td>
<td align="right">15,524,080</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">19,594,960</td>
<td align="right">19,331,400</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">4,947,660</td>
<td align="right">5,012,360</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">14,283,220</td>
<td align="right">14,413,940</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">10,991,220</td>
<td align="right">10,909,200</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">245,679,940</td>
<td align="right">244,705,220</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">245,811,560</td>
<td align="right">245,737,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,008,480</td>
<td align="right">4,008,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">962,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">725,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">11,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">3,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">3,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">2,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">1,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
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
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">440</td>
<td align="right">1,000.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">940</td>
<td align="right">4,940</td>
<td align="right">425.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">1,120</td>
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
Stats gathered on: 2025-06-24
