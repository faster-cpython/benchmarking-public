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
<td align="left">END_FOR</td>
<td align="right">10,400</td>
<td align="right">20,800</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">320</td>
<td align="right">640</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">160</td>
<td align="right">320</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">160</td>
<td align="right">320</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">10,558,640</td>
<td align="right">21,117,200</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">10,597,340</td>
<td align="right">21,168,380</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,675,200</td>
<td align="right">21,255,420</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">18,800</td>
<td align="right">37,380</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">811,040</td>
<td align="right">1,611,360</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">814,720</td>
<td align="right">1,615,940</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">935,080</td>
<td align="right">1,851,400</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">10,888,560</td>
<td align="right">21,482,720</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,729,580</td>
<td align="right">26,760,020</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,706,040</td>
<td align="right">5,213,420</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,747,240</td>
<td align="right">49,545,880</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">12,220</td>
<td align="right">22,620</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">983,780</td>
<td align="right">1,819,760</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">12,040</td>
<td align="right">21,960</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,195,100</td>
<td align="right">3,988,660</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,082,580</td>
<td align="right">1,897,080</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">860</td>
<td align="right">1,500</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">12,960</td>
<td align="right">22,400</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">14,040</td>
<td align="right">23,960</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">14,580</td>
<td align="right">24,500</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">240</td>
<td align="right">400</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">191,560</td>
<td align="right">309,480</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">18,700</td>
<td align="right">29,580</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">21,580</td>
<td align="right">31,980</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">57,895,280</td>
<td align="right">81,486,560</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">25,520</td>
<td align="right">35,600</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,620</td>
<td align="right">3,580</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">34,520</td>
<td align="right">46,360</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,900</td>
<td align="right">42,720</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">319,220</td>
<td align="right">427,480</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">28,320</td>
<td align="right">37,440</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">44,438,720</td>
<td align="right">58,293,380</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,340</td>
<td align="right">3,060</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,240</td>
<td align="right">4,200</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">49,840</td>
<td align="right">63,760</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">146,640</td>
<td align="right">187,440</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">121,480</td>
<td align="right">153,300</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">86,610,740</td>
<td align="right">108,592,180</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,280</td>
<td align="right">1,600</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">59,523,080</td>
<td align="right">70,911,400</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,840</td>
<td align="right">2,160</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">116,580</td>
<td align="right">136,660</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">5,760</td>
<td align="right">6,720</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">11,120</td>
<td align="right">12,880</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,080</td>
<td align="right">2,400</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,080</td>
<td align="right">2,400</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">71,140</td>
<td align="right">81,900</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,180</td>
<td align="right">2,500</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">9,120</td>
<td align="right">10,400</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">9,200</td>
<td align="right">10,480</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">6,960</td>
<td align="right">7,920</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">13,720</td>
<td align="right">15,480</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">101,380</td>
<td align="right">113,680</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">34,502,920</td>
<td align="right">38,679,460</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">20,340</td>
<td align="right">22,740</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">118,700</td>
<td align="right">132,560</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,280</td>
<td align="right">9,240</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,140</td>
<td align="right">3,460</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,140</td>
<td align="right">3,460</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,140</td>
<td align="right">3,460</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">11,340</td>
<td align="right">12,460</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">16,360</td>
<td align="right">17,960</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">13,920</td>
<td align="right">15,200</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,740</td>
<td align="right">1,900</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">10,040</td>
<td align="right">10,940</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">12,560</td>
<td align="right">13,680</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">22,540</td>
<td align="right">24,460</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">197,460</td>
<td align="right">214,100</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,340</td>
<td align="right">26,200</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">19,760</td>
<td align="right">21,240</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">19,760</td>
<td align="right">21,240</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">30,900</td>
<td align="right">33,140</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">25,700</td>
<td align="right">27,560</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">11,280</td>
<td align="right">12,080</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,740</td>
<td align="right">5,060</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">212,420</td>
<td align="right">226,580</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,520</td>
<td align="right">2,680</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">40,899,440</td>
<td align="right">43,422,320</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">608,340</td>
<td align="right">642,860</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">34,800</td>
<td align="right">36,740</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">84,800</td>
<td align="right">89,000</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,320</td>
<td align="right">3,480</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,160</td>
<td align="right">10,640</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">63,980</td>
<td align="right">66,900</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,820</td>
<td align="right">9,140</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">61,960</td>
<td align="right">64,200</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">47,960</td>
<td align="right">49,580</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">32,200</td>
<td align="right">33,160</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">76,740</td>
<td align="right">78,920</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">181,740</td>
<td align="right">186,860</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">103,540</td>
<td align="right">105,820</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">69,060</td>
<td align="right">70,540</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,940</td>
<td align="right">5,040</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">64,920</td>
<td align="right">63,720</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">83,800</td>
<td align="right">85,340</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">32,120</td>
<td align="right">32,620</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">23,280</td>
<td align="right">23,600</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">23,400</td>
<td align="right">23,720</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">25,260</td>
<td align="right">25,520</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">9,340</td>
<td align="right">9,420</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">53,800</td>
<td align="right">54,220</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">44,760</td>
<td align="right">45,080</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">215,800</td>
<td align="right">216,460</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">48,920</td>
<td align="right">49,020</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">153,620</td>
<td align="right">153,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">16,333,080</td>
<td align="right">16,333,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">16,331,440</td>
<td align="right">16,331,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">22,960</td>
<td align="right">22,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">22,860</td>
<td align="right">22,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,980</td>
<td align="right">20,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">16,080</td>
<td align="right">16,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7,940</td>
<td align="right">7,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4,940</td>
<td align="right">4,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,580</td>
<td align="right">3,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,120</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,480</td>
<td align="right">2,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,760</td>
<td align="right">1,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,660</td>
<td align="right">1,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,600</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,600</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,520</td>
<td align="right">1,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">640</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,824,720</td>
<td align="right">100.0%</td>
<td align="right">39,149,520</td>
<td align="right">100.0%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,620</td>
<td align="right">0.0%</td>
<td align="right">6,620</td>
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
<td align="right">580</td>
<td align="right">43.9%</td>
<td align="right">580</td>
<td align="right">43.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">740</td>
<td align="right">56.1%</td>
<td align="right">740</td>
<td align="right">56.1%</td>
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
<td align="right">580</td>
<td align="right">78.4%</td>
<td align="right">580</td>
<td align="right">78.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">160</td>
<td align="right">21.6%</td>
<td align="right">160</td>
<td align="right">21.6%</td>
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
<td align="right">21,580</td>
<td align="right">100.0%</td>
<td align="right">31,980</td>
<td align="right">100.0%</td>
<td align="right">48.2%</td>
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
<td align="right">1,560</td>
<td align="right">0.0%</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,525,800</td>
<td align="right">100.0%</td>
<td align="right">14,794,280</td>
<td align="right">100.0%</td>
<td align="right">28.4%</td>
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
<td align="right">180</td>
<td align="right">23.1%</td>
<td align="right">260</td>
<td align="right">30.2%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">600</td>
<td align="right">76.9%</td>
<td align="right">600</td>
<td align="right">69.8%</td>
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
<td align="left">buffer int</td>
<td align="right">120</td>
<td align="right">66.7%</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">33.3%</td>
<td align="right">80</td>
<td align="right">30.8%</td>
<td align="right">33.3%</td>
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
<td align="right">167,118,200</td>
<td align="right">100.0%</td>
<td align="right">211,106,600</td>
<td align="right">100.0%</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,740</td>
<td align="right">0.0%</td>
<td align="right">3,220</td>
<td align="right">0.0%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,200</td>
<td align="right">0.0%</td>
<td align="right">12,200</td>
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
<td align="right">11,580</td>
<td align="right">100.0%</td>
<td align="right">11,580</td>
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
<td align="right">960</td>
<td align="right">51.6%</td>
<td align="right">960</td>
<td align="right">51.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,837,180</td>
<td align="right">99.7%</td>
<td align="right">3,572,060</td>
<td align="right">99.9%</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,360</td>
<td align="right">0.2%</td>
<td align="right">3,440</td>
<td align="right">0.1%</td>
<td align="right">2.4%</td>
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
<td align="right">300</td>
<td align="right">19.0%</td>
<td align="right">320</td>
<td align="right">20.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,280</td>
<td align="right">81.0%</td>
<td align="right">1,280</td>
<td align="right">80.0%</td>
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
<td align="left">bytes</td>
<td align="right">40</td>
<td align="right">13.3%</td>
<td align="right">60</td>
<td align="right">18.8%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">240</td>
<td align="right">80.0%</td>
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">20</td>
<td align="right">6.7%</td>
<td align="right">20</td>
<td align="right">6.2%</td>
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
<td align="right">11,500,240</td>
<td align="right">98.4%</td>
<td align="right">14,750,320</td>
<td align="right">98.7%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">176,520</td>
<td align="right">1.5%</td>
<td align="right">181,420</td>
<td align="right">1.2%</td>
<td align="right">2.8%</td>
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
<td align="right">5,060</td>
<td align="right">96.9%</td>
<td align="right">5,280</td>
<td align="right">97.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">3.1%</td>
<td align="right">160</td>
<td align="right">2.9%</td>
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
<td align="right">160</td>
<td align="right">3.2%</td>
<td align="right">220</td>
<td align="right">4.2%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">240</td>
<td align="right">4.7%</td>
<td align="right">260</td>
<td align="right">4.9%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">4,660</td>
<td align="right">92.1%</td>
<td align="right">4,800</td>
<td align="right">90.9%</td>
<td align="right">3.0%</td>
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
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,767,460</td>
<td align="right">93.8%</td>
<td align="right">3,502,200</td>
<td align="right">96.2%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">113,100</td>
<td align="right">6.0%</td>
<td align="right">133,000</td>
<td align="right">3.7%</td>
<td align="right">17.6%</td>
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
<td align="right">2,520</td>
<td align="right">72.4%</td>
<td align="right">2,700</td>
<td align="right">73.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">960</td>
<td align="right">27.6%</td>
<td align="right">960</td>
<td align="right">26.2%</td>
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
<td align="left">dict items</td>
<td align="right">60</td>
<td align="right">2.4%</td>
<td align="right">80</td>
<td align="right">3.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,160</td>
<td align="right">46.0%</td>
<td align="right">1,300</td>
<td align="right">48.1%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,060</td>
<td align="right">42.1%</td>
<td align="right">1,080</td>
<td align="right">40.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">240</td>
<td align="right">9.5%</td>
<td align="right">240</td>
<td align="right">8.9%</td>
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
<td align="right">2,694,760</td>
<td align="right">5.2%</td>
<td align="right">5,201,400</td>
<td align="right">7.3%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">49,212,140</td>
<td align="right">94.8%</td>
<td align="right">65,546,540</td>
<td align="right">92.6%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,660</td>
<td align="right">0.0%</td>
<td align="right">10,660</td>
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
<td align="right">5,580</td>
<td align="right">48.8%</td>
<td align="right">6,320</td>
<td align="right">51.9%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,860</td>
<td align="right">51.2%</td>
<td align="right">5,860</td>
<td align="right">48.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,560</td>
<td align="right">81.7%</td>
<td align="right">5,240</td>
<td align="right">82.9%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">14.3%</td>
<td align="right">840</td>
<td align="right">13.3%</td>
<td align="right">5.0%</td>
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
<td align="right">11,077,300</td>
<td align="right">99.7%</td>
<td align="right">21,688,100</td>
<td align="right">99.9%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,140</td>
<td align="right">0.1%</td>
<td align="right">11,140</td>
<td align="right">0.1%</td>
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
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">500</td>
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
<td align="right">9,560</td>
<td align="right">0.1%</td>
<td align="right">9,560</td>
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
<td align="right">9,840</td>
<td align="right">100.0%</td>
<td align="right">9,840</td>
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
<td align="right">1,920</td>
<td align="right">96.0%</td>
<td align="right">1,920</td>
<td align="right">96.0%</td>
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
<td align="right">18,600</td>
<td align="right">0.1%</td>
<td align="right">37,160</td>
<td align="right">0.2%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,348,760</td>
<td align="right">99.9%</td>
<td align="right">16,348,760</td>
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
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">80.0%</td>
<td align="right">180</td>
<td align="right">81.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">20.0%</td>
<td align="right">40</td>
<td align="right">18.2%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">180</td>
<td align="right">100.0%</td>
<td align="right">12.5%</td>
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
<td align="right">10,592,240</td>
<td align="right">92.8%</td>
<td align="right">21,163,280</td>
<td align="right">92.9%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">812,240</td>
<td align="right">7.1%</td>
<td align="right">1,613,200</td>
<td align="right">7.1%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,040</td>
<td align="right">0.1%</td>
<td align="right">6,040</td>
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
<td align="right">1,540</td>
<td align="right">61.6%</td>
<td align="right">1,800</td>
<td align="right">65.2%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">960</td>
<td align="right">38.4%</td>
<td align="right">960</td>
<td align="right">34.8%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">980</td>
<td align="right">63.6%</td>
<td align="right">1,200</td>
<td align="right">66.7%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">220</td>
<td align="right">14.3%</td>
<td align="right">240</td>
<td align="right">13.3%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">240</td>
<td align="right">15.6%</td>
<td align="right">260</td>
<td align="right">14.4%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">100</td>
<td align="right">6.5%</td>
<td align="right">100</td>
<td align="right">5.6%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
<td align="right">110,160</td>
<td align="right">99.8%</td>
<td align="right">128,720</td>
<td align="right">99.8%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">104,954,200</td>
<td align="right">99.9%</td>
<td align="right">127,760,600</td>
<td align="right">99.9%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">59,700</td>
<td align="right">0.1%</td>
<td align="right">60,340</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">41,200</td>
<td align="right">0.0%</td>
<td align="right">41,520</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
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
<td align="right">3,900</td>
<td align="right">84.8%</td>
<td align="right">3,900</td>
<td align="right">84.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">700</td>
<td align="right">15.2%</td>
<td align="right">700</td>
<td align="right">15.2%</td>
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
<td align="left">sequence</td>
<td align="right">380</td>
<td align="right">54.3%</td>
<td align="right">380</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">320</td>
<td align="right">45.7%</td>
<td align="right">320</td>
<td align="right">45.7%</td>
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
<td align="right">18,122,800</td>
<td align="right">100.0%</td>
<td align="right">19,741,040</td>
<td align="right">100.0%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
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
<td align="right">640</td>
<td align="right">100.0%</td>
<td align="right">640</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,966,860</td>
<td align="right">0.9%</td>
<td align="right">7,330,940</td>
<td align="right">1.2%</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">149,228,920</td>
<td align="right">33.0%</td>
<td align="right">215,367,080</td>
<td align="right">34.8%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">299,519,760</td>
<td align="right">66.1%</td>
<td align="right">395,776,100</td>
<td align="right">64.0%</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">89,120</td>
<td align="right">0.0%</td>
<td align="right">90,560</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
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
<td align="left">SEND</td>
<td align="right">18,600</td>
<td align="right">0.5%</td>
<td align="right">37,160</td>
<td align="right">0.5%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">812,240</td>
<td align="right">20.7%</td>
<td align="right">1,613,200</td>
<td align="right">22.2%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,694,760</td>
<td align="right">68.8%</td>
<td align="right">5,201,400</td>
<td align="right">71.5%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">21,580</td>
<td align="right">0.6%</td>
<td align="right">31,980</td>
<td align="right">0.4%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">113,100</td>
<td align="right">2.9%</td>
<td align="right">133,000</td>
<td align="right">1.8%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">176,520</td>
<td align="right">4.5%</td>
<td align="right">181,420</td>
<td align="right">2.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">41,200</td>
<td align="right">1.1%</td>
<td align="right">41,520</td>
<td align="right">0.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,200</td>
<td align="right">0.3%</td>
<td align="right">12,200</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11,140</td>
<td align="right">0.3%</td>
<td align="right">11,140</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,620</td>
<td align="right">0.2%</td>
<td align="right">6,620</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">640</td>
<td align="right">0.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">460</td>
<td align="right">0.5%</td>
<td align="right">620</td>
<td align="right">0.7%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,560</td>
<td align="right">1.7%</td>
<td align="right">1,880</td>
<td align="right">2.1%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">32,140</td>
<td align="right">36.0%</td>
<td align="right">32,780</td>
<td align="right">36.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,560</td>
<td align="right">30.9%</td>
<td align="right">27,560</td>
<td align="right">30.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,360</td>
<td align="right">10.5%</td>
<td align="right">9,360</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,040</td>
<td align="right">6.8%</td>
<td align="right">6,040</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,760</td>
<td align="right">6.5%</td>
<td align="right">5,760</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,800</td>
<td align="right">4.3%</td>
<td align="right">3,800</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,300</td>
<td align="right">1.5%</td>
<td align="right">1,300</td>
<td align="right">1.4%</td>
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
<td align="right">13,320</td>
<td align="right">0.0%</td>
<td align="right">22,920</td>
<td align="right">0.0%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">69,391,760</td>
<td align="right">62.9%</td>
<td align="right">96,265,920</td>
<td align="right">68.9%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">50,797,360</td>
<td align="right">46.0%</td>
<td align="right">68,815,680</td>
<td align="right">49.2%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">36,650,740</td>
<td align="right">33.2%</td>
<td align="right">47,220,500</td>
<td align="right">33.8%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">36,652,900</td>
<td align="right">33.2%</td>
<td align="right">47,222,660</td>
<td align="right">33.8%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">36,622,880</td>
<td align="right">33.2%</td>
<td align="right">47,181,120</td>
<td align="right">33.8%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">59,523,700</td>
<td align="right">54.0%</td>
<td align="right">70,912,660</td>
<td align="right">50.8%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">59,523,700</td>
<td align="right">54.0%</td>
<td align="right">70,912,660</td>
<td align="right">50.8%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">5,840</td>
<td align="right">0.0%</td>
<td align="right">6,800</td>
<td align="right">0.0%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,870,800</td>
<td align="right">20.7%</td>
<td align="right">23,690,000</td>
<td align="right">17.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">216,254,440</td>
<td align="right">10.9%</td>
<td align="right">312,775,160</td>
<td align="right">13.2%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">25,200</td>
<td align="right"></td>
<td align="right">36,400</td>
<td align="right"></td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">339,543,800</td>
<td align="right">14.9%</td>
<td align="right">468,959,080</td>
<td align="right">17.2%</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">287,595</td>
<td align="right"></td>
<td align="right">196,239</td>
<td align="right"></td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">446,412</td>
<td align="right"></td>
<td align="right">323,595</td>
<td align="right"></td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">154,150,886</td>
<td align="right"></td>
<td align="right">193,288,079</td>
<td align="right"></td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">79,128,640</td>
<td align="right">25.4%</td>
<td align="right">93,818,800</td>
<td align="right">26.5%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">79,181,300</td>
<td align="right"></td>
<td align="right">93,871,460</td>
<td align="right"></td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">171,974</td>
<td align="right"></td>
<td align="right">141,341</td>
<td align="right"></td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">1,760,831,487</td>
<td align="right">89.1%</td>
<td align="right">2,064,709,334</td>
<td align="right">86.8%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">1,940,794,484</td>
<td align="right">85.1%</td>
<td align="right">2,250,225,901</td>
<td align="right">82.8%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">57,254,545</td>
<td align="right"></td>
<td align="right">65,469,221</td>
<td align="right"></td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">82,500</td>
<td align="right">0.0%</td>
<td align="right">92,880</td>
<td align="right">0.0%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">231,950,520</td>
<td align="right">74.5%</td>
<td align="right">260,573,140</td>
<td align="right">73.5%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,162,980</td>
<td align="right">74.6%</td>
<td align="right">260,797,760</td>
<td align="right">73.5%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">233,428,304</td>
<td align="right"></td>
<td align="right">262,063,343</td>
<td align="right"></td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">129,960</td>
<td align="right">0.0%</td>
<td align="right">131,740</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
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
<td align="right">15,040</td>
<td align="right">37,640</td>
<td align="right">602,945,340</td>
<td align="right">16,160</td>
<td align="right">37,680</td>
<td align="right">622,666,280</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">85,898,400</td>
<td align="right"></td>
<td align="right">108,215,080</td>
<td align="right"></td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">10,220</td>
<td align="right">77.8%</td>
<td align="right">11,340</td>
<td align="right">79.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">10,740</td>
<td align="right">81.7%</td>
<td align="right">11,860</td>
<td align="right">82.8%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">13,140</td>
<td align="right"></td>
<td align="right">14,320</td>
<td align="right"></td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,533,983,200</td>
<td align="right">4,114.1%</td>
<td align="right">3,818,390,580</td>
<td align="right">3,528.5%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,920</td>
<td align="right">22.2%</td>
<td align="right">2,980</td>
<td align="right">20.8%</td>
<td align="right">2.1%</td>
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
<td align="right">500</td>
<td align="right">3.8%</td>
<td align="right">500</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">240</td>
<td align="right">1.8%</td>
<td align="right">240</td>
<td align="right">1.7%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,920</td>
<td align="right"></td>
<td align="right">2,980</td>
<td align="right"></td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,920</td>
<td align="right">100.0%</td>
<td align="right">2,980</td>
<td align="right">100.0%</td>
<td align="right">2.1%</td>
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
<td align="right">140</td>
<td align="right">4.8%</td>
<td align="right">160</td>
<td align="right">5.4%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">180</td>
<td align="right">6.2%</td>
<td align="right">180</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">5.5%</td>
<td align="right">160</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">700</td>
<td align="right">24.0%</td>
<td align="right">720</td>
<td align="right">24.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">920</td>
<td align="right">31.5%</td>
<td align="right">920</td>
<td align="right">30.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">540</td>
<td align="right">18.5%</td>
<td align="right">540</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">280</td>
<td align="right">9.6%</td>
<td align="right">300</td>
<td align="right">10.1%</td>
<td align="right">7.1%</td>
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
<td align="right">220</td>
<td align="right">7.5%</td>
<td align="right">240</td>
<td align="right">8.1%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">100</td>
<td align="right">3.4%</td>
<td align="right">260</td>
<td align="right">8.7%</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">240</td>
<td align="right">8.2%</td>
<td align="right">360</td>
<td align="right">12.1%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,240</td>
<td align="right">42.5%</td>
<td align="right">1,100</td>
<td align="right">36.9%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">560</td>
<td align="right">19.2%</td>
<td align="right">520</td>
<td align="right">17.4%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">460</td>
<td align="right">15.8%</td>
<td align="right">480</td>
<td align="right">16.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">100</td>
<td align="right">3.4%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">-80.0%</td>
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
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">15,360</td>
<td align="right">31,360</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">7,680</td>
<td align="right">15,680</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,680</td>
<td align="right">15,680</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">9,280</td>
<td align="right">18,720</td>
<td align="right">101.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,712,000</td>
<td align="right">3,425,920</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">815,660</td>
<td align="right">1,631,820</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">815,940</td>
<td align="right">1,632,260</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">160</td>
<td align="right">320</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,729,520</td>
<td align="right">3,443,280</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">99,849,140</td>
<td align="right">3,426,340</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,848,880</td>
<td align="right">3,579,180</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">420,639,220</td>
<td align="right">27,715,880</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,767,120</td>
<td align="right">3,382,920</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,767,120</td>
<td align="right">3,382,920</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">883,560</td>
<td align="right">1,691,460</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,780,140</td>
<td align="right">3,405,960</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">898,420</td>
<td align="right">1,716,020</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">943,340</td>
<td align="right">1,751,660</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">379,858,200</td>
<td align="right">575,936,740</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">30,549,280</td>
<td align="right">44,410,800</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">25,380</td>
<td align="right">34,820</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">13,285,240</td>
<td align="right">18,170,580</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">13,285,240</td>
<td align="right">18,170,580</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">25,427,740</td>
<td align="right">34,391,640</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">37,358,640</td>
<td align="right">50,287,740</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">12,359,720</td>
<td align="right">16,503,560</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">12,503,920</td>
<td align="right">16,588,880</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">23,692,520</td>
<td align="right">31,106,760</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">22,840,880</td>
<td align="right">29,450,760</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">11,398,920</td>
<td align="right">14,658,620</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">11,399,340</td>
<td align="right">14,659,040</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">11,402,160</td>
<td align="right">14,662,020</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">11,373,960</td>
<td align="right">14,624,220</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,374,380</td>
<td align="right">14,624,640</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">11,448,880</td>
<td align="right">14,706,280</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">11,489,680</td>
<td align="right">14,739,280</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">134,231,320</td>
<td align="right">170,769,200</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">122,493,220</td>
<td align="right">154,945,180</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">21,811,800</td>
<td align="right">27,486,380</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">88,284,560</td>
<td align="right">111,230,980</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">85,898,400</td>
<td align="right">108,215,080</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">21,963,000</td>
<td align="right">27,663,480</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">22,010,920</td>
<td align="right">27,711,580</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">22,081,640</td>
<td align="right">27,788,680</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">22,216,980</td>
<td align="right">27,942,020</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">51,513,700</td>
<td align="right">64,701,380</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">108,580</td>
<td align="right">135,780</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">42,927,900</td>
<td align="right">53,485,800</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">84,168,720</td>
<td align="right">104,771,480</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">80,024,300</td>
<td align="right">99,537,340</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">114,526,120</td>
<td align="right">141,373,520</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">20,856,640</td>
<td align="right">25,715,580</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">10,573,580</td>
<td align="right">13,030,920</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">31,667,120</td>
<td align="right">38,991,740</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">10,557,640</td>
<td align="right">12,999,140</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">10,561,000</td>
<td align="right">13,001,780</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">10,561,000</td>
<td align="right">13,001,780</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">10,619,760</td>
<td align="right">13,069,260</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">10,603,200</td>
<td align="right">13,044,480</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">49,567,140</td>
<td align="right">60,976,560</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">10,612,080</td>
<td align="right">13,053,580</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">74,472,480</td>
<td align="right">91,542,660</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,931,360</td>
<td align="right">21,988,780</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">62,236,380</td>
<td align="right">75,258,680</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">51,661,080</td>
<td align="right">62,217,200</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">51,661,920</td>
<td align="right">62,218,040</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">91,139,880</td>
<td align="right">109,054,540</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">70,813,580</td>
<td align="right">84,644,860</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">57,188,920</td>
<td align="right">67,923,100</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">170,651,920</td>
<td align="right">201,865,940</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">49,663,960</td>
<td align="right">58,683,380</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">98,880</td>
<td align="right">116,640</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">98,880</td>
<td align="right">116,640</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">156,300</td>
<td align="right">180,760</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">47,908,360</td>
<td align="right">55,315,560</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">48,086,620</td>
<td align="right">55,411,060</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">38,354,860</td>
<td align="right">44,110,440</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">38,374,180</td>
<td align="right">44,114,080</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">91,298,820</td>
<td align="right">103,531,360</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">6,515,520</td>
<td align="right">7,380,320</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,515,520</td>
<td align="right">7,380,320</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">56,537,480</td>
<td align="right">63,972,460</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">37,483,680</td>
<td align="right">42,366,460</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,420,360</td>
<td align="right">7,244,520</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,483,540</td>
<td align="right">7,291,540</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">6,538,080</td>
<td align="right">7,346,400</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">148,200</td>
<td align="right">164,660</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">85,200</td>
<td align="right">93,520</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">26,933,260</td>
<td align="right">29,424,040</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,098,060</td>
<td align="right">19,714,440</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">23,574,720</td>
<td align="right">25,224,320</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">18,140</td>
<td align="right">18,460</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">18,140</td>
<td align="right">18,460</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,740,160</td>
<td align="right">5,749,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">16,347,180</td>
<td align="right">16,347,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">16,328,240</td>
<td align="right">16,328,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">21,925,360</td>
<td align="right">21,925,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">16,330,340</td>
<td align="right">16,330,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">5,765,640</td>
<td align="right">5,765,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">5,765,640</td>
<td align="right">5,765,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">5,707,200</td>
<td align="right">5,707,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,650,760</td>
<td align="right">5,650,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">54,440</td>
<td align="right">54,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">54,440</td>
<td align="right">54,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">15,680</td>
<td align="right">15,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">4,520</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,520</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">2,420</td>
<td align="right">2,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">2,100</td>
<td align="right">2,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2,100</td>
<td align="right">2,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,800</td>
<td align="right">1,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,360</td>
<td align="right">1,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,360</td>
<td align="right">1,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,080</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">860</td>
<td align="right">860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">860</td>
<td align="right">860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">660</td>
<td align="right">660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<td align="left">SEND</td>
<td align="right">60</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40</td>
<td align="right">40</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-17
