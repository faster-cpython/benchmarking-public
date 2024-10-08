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
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">29,420</td>
<td align="right">12,220</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">357,760</td>
<td align="right">156,040</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">100,600</td>
<td align="right">145,080</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">3,000</td>
<td align="right">1,680</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">103,380</td>
<td align="right">58,600</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,200</td>
<td align="right">11,160</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,164,960</td>
<td align="right">732,760</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">74,280</td>
<td align="right">96,680</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">74,280</td>
<td align="right">96,680</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,978,620</td>
<td align="right">1,511,100</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">161,740</td>
<td align="right">128,720</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">331,140</td>
<td align="right">263,680</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">652,780</td>
<td align="right">532,460</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,060</td>
<td align="right">47,140</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">862,240</td>
<td align="right">714,540</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">151,000</td>
<td align="right">173,200</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,115,320</td>
<td align="right">952,040</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">608,200</td>
<td align="right">520,040</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">502,600</td>
<td align="right">436,860</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">150,620</td>
<td align="right">133,900</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">272,740</td>
<td align="right">245,920</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,658,020</td>
<td align="right">6,151,200</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,789,100</td>
<td align="right">1,655,820</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,509,880</td>
<td align="right">7,974,000</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,489,160</td>
<td align="right">1,401,000</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,715,020</td>
<td align="right">1,619,740</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,880</td>
<td align="right">11,220</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">177,700</td>
<td align="right">167,880</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,158,860</td>
<td align="right">1,103,040</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,777,900</td>
<td align="right">9,320,420</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,893,780</td>
<td align="right">5,618,580</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,220</td>
<td align="right">16,440</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">920,440</td>
<td align="right">878,920</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,020</td>
<td align="right">10,540</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">511,400</td>
<td align="right">532,860</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,969,860</td>
<td align="right">3,091,860</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">32,220</td>
<td align="right">30,900</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">161,200</td>
<td align="right">154,620</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,974,620</td>
<td align="right">19,195,260</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,028,960</td>
<td align="right">6,759,980</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">84,140</td>
<td align="right">81,240</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,479,280</td>
<td align="right">3,359,860</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,068,000</td>
<td align="right">15,519,180</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">32,203,700</td>
<td align="right">31,168,600</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,661,560</td>
<td align="right">2,746,040</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,622,100</td>
<td align="right">19,981,180</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,212,780</td>
<td align="right">3,113,320</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">583,020</td>
<td align="right">565,320</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,000,200</td>
<td align="right">69,839,300</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">16,557,360</td>
<td align="right">16,126,440</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,900,160</td>
<td align="right">15,270,000</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">46,680</td>
<td align="right">45,540</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">105,940</td>
<td align="right">103,360</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">132,700</td>
<td align="right">129,480</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">786,600</td>
<td align="right">767,780</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,987,040</td>
<td align="right">1,940,120</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">123,720</td>
<td align="right">120,820</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,965,080</td>
<td align="right">5,832,620</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">30,400</td>
<td align="right">29,740</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">91,320</td>
<td align="right">89,340</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,422,020</td>
<td align="right">17,049,640</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,815,000</td>
<td align="right">3,736,680</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,973,800</td>
<td align="right">13,236,100</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,651,840</td>
<td align="right">1,618,820</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,047,040</td>
<td align="right">1,026,360</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,168,540</td>
<td align="right">4,090,880</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">90,840</td>
<td align="right">89,160</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">39,060</td>
<td align="right">38,340</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,259,720</td>
<td align="right">6,145,840</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,059,360</td>
<td align="right">1,041,880</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">207,100</td>
<td align="right">203,800</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,969,760</td>
<td align="right">3,912,860</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,068,100</td>
<td align="right">2,038,480</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">548,300</td>
<td align="right">540,820</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,001,100</td>
<td align="right">1,014,180</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">802,160</td>
<td align="right">792,060</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,046,740</td>
<td align="right">23,769,200</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,963,080</td>
<td align="right">22,702,780</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,865,720</td>
<td align="right">5,799,620</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,199,280</td>
<td align="right">1,212,040</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">143,260</td>
<td align="right">141,740</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,976,920</td>
<td align="right">7,899,200</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">16,700</td>
<td align="right">16,860</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">588,200</td>
<td align="right">583,920</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">192,040</td>
<td align="right">190,720</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">59,840</td>
<td align="right">60,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,262,960</td>
<td align="right">2,249,420</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">83,320</td>
<td align="right">82,860</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">156,240</td>
<td align="right">157,100</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,204,780</td>
<td align="right">13,136,960</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">817,660</td>
<td align="right">813,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">155,200</td>
<td align="right">154,560</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">398,320</td>
<td align="right">397,020</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">286,920</td>
<td align="right">286,020</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,231,340</td>
<td align="right">4,219,640</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,836,640</td>
<td align="right">2,829,420</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">126,580</td>
<td align="right">126,280</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,542,040</td>
<td align="right">1,540,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,176,360</td>
<td align="right">5,170,580</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,123,000</td>
<td align="right">3,119,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,179,120</td>
<td align="right">1,178,040</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,959,140</td>
<td align="right">1,957,460</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">417,860</td>
<td align="right">417,580</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,975,100</td>
<td align="right">5,972,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,030,080</td>
<td align="right">1,029,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,423,660</td>
<td align="right">10,423,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">10,029,280</td>
<td align="right">10,029,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,938,640</td>
<td align="right">1,938,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,030,080</td>
<td align="right">1,030,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">291,360</td>
<td align="right">291,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">279,980</td>
<td align="right">279,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">193,760</td>
<td align="right">193,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">157,020</td>
<td align="right">157,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">76,480</td>
<td align="right">76,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">75,260</td>
<td align="right">75,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">73,580</td>
<td align="right">73,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">40,100</td>
<td align="right">40,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">34,320</td>
<td align="right">34,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">29,360</td>
<td align="right">29,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">19,280</td>
<td align="right">19,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">16,600</td>
<td align="right">16,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">6,320</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,120</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,980</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">2,080</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">16,060</td>
<td align="right">1.8%</td>
<td align="right">15,200</td>
<td align="right">1.7%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">867,940</td>
<td align="right">98.0%</td>
<td align="right">867,940</td>
<td align="right">98.1%</td>
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
<td align="right">680</td>
<td align="right">58.6%</td>
<td align="right">760</td>
<td align="right">61.3%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">480</td>
<td align="right">41.4%</td>
<td align="right">480</td>
<td align="right">38.7%</td>
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
<td align="right">640</td>
<td align="right">94.1%</td>
<td align="right">720</td>
<td align="right">94.7%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">40</td>
<td align="right">5.9%</td>
<td align="right">40</td>
<td align="right">5.3%</td>
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
<td align="right">19,200</td>
<td align="right">100.0%</td>
<td align="right">11,160</td>
<td align="right">100.0%</td>
<td align="right">-41.9%</td>
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
<td align="right">15,700</td>
<td align="right">0.6%</td>
<td align="right">15,700</td>
<td align="right">0.6%</td>
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
<td align="right">2,451,660</td>
<td align="right">99.1%</td>
<td align="right">2,451,660</td>
<td align="right">99.1%</td>
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
<td align="right">6,340</td>
<td align="right">0.3%</td>
<td align="right">6,340</td>
<td align="right">0.3%</td>
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
<td align="right">340</td>
<td align="right">30.9%</td>
<td align="right">500</td>
<td align="right">39.7%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">760</td>
<td align="right">69.1%</td>
<td align="right">760</td>
<td align="right">60.3%</td>
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
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">180</td>
<td align="right">36.0%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240</td>
<td align="right">70.6%</td>
<td align="right">320</td>
<td align="right">64.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">268,500</td>
<td align="right">0.3%</td>
<td align="right">419,420</td>
<td align="right">0.5%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,248,800</td>
<td align="right">99.7%</td>
<td align="right">87,089,780</td>
<td align="right">99.5%</td>
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
<td align="right">17,160</td>
<td align="right">0.0%</td>
<td align="right">17,160</td>
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
<td align="right">23,600</td>
<td align="right">100.0%</td>
<td align="right">27,000</td>
<td align="right">100.0%</td>
<td align="right">14.4%</td>
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
<td align="right">1,500</td>
<td align="right">50.0%</td>
<td align="right">1,500</td>
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
<td align="right">812,580</td>
<td align="right">42.9%</td>
<td align="right">804,700</td>
<td align="right">42.6%</td>
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
<td align="right">1,074,720</td>
<td align="right">56.8%</td>
<td align="right">1,074,720</td>
<td align="right">56.9%</td>
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
<td align="right">4,280</td>
<td align="right">84.3%</td>
<td align="right">8,480</td>
<td align="right">91.4%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">800</td>
<td align="right">15.7%</td>
<td align="right">800</td>
<td align="right">8.6%</td>
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
<td align="left">set</td>
<td align="right">200</td>
<td align="right">4.7%</td>
<td align="right">2,400</td>
<td align="right">28.3%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,860</td>
<td align="right">43.5%</td>
<td align="right">3,060</td>
<td align="right">36.1%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,500</td>
<td align="right">35.0%</td>
<td align="right">2,260</td>
<td align="right">26.7%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">140</td>
<td align="right">1.7%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">9.8%</td>
<td align="right">420</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">120</td>
<td align="right">2.8%</td>
<td align="right">120</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">80</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">0.9%</td>
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
<td align="right">154,320</td>
<td align="right">21.5%</td>
<td align="right">154,280</td>
<td align="right">21.5%</td>
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
<td align="right">527,560</td>
<td align="right">73.5%</td>
<td align="right">527,560</td>
<td align="right">73.4%</td>
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
<td align="right">33,720</td>
<td align="right">4.7%</td>
<td align="right">33,720</td>
<td align="right">4.7%</td>
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
<td align="right">1,300</td>
<td align="right">51.2%</td>
<td align="right">2,200</td>
<td align="right">64.0%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">48.8%</td>
<td align="right">1,240</td>
<td align="right">36.0%</td>
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
<td align="right">70.8%</td>
<td align="right">1,680</td>
<td align="right">76.4%</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">380</td>
<td align="right">29.2%</td>
<td align="right">520</td>
<td align="right">23.6%</td>
<td align="right">36.8%</td>
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
<td align="right">3,962,700</td>
<td align="right">45.9%</td>
<td align="right">3,898,960</td>
<td align="right">45.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,662,980</td>
<td align="right">54.0%</td>
<td align="right">4,615,420</td>
<td align="right">54.1%</td>
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
<td align="left">Failure</td>
<td align="right">5,400</td>
<td align="right">76.5%</td>
<td align="right">12,240</td>
<td align="right">88.1%</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,660</td>
<td align="right">23.5%</td>
<td align="right">1,660</td>
<td align="right">11.9%</td>
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
<td align="left">ascii string</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">500</td>
<td align="right">4.1%</td>
<td align="right">177.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,720</td>
<td align="right">50.4%</td>
<td align="right">7,160</td>
<td align="right">58.5%</td>
<td align="right">163.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">740</td>
<td align="right">6.0%</td>
<td align="right">117.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">740</td>
<td align="right">6.0%</td>
<td align="right">117.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">120</td>
<td align="right">2.2%</td>
<td align="right">240</td>
<td align="right">2.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">740</td>
<td align="right">13.7%</td>
<td align="right">1,300</td>
<td align="right">10.6%</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">3.7%</td>
<td align="right">340</td>
<td align="right">2.8%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">440</td>
<td align="right">8.1%</td>
<td align="right">720</td>
<td align="right">5.9%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">320</td>
<td align="right">5.9%</td>
<td align="right">500</td>
<td align="right">4.1%</td>
<td align="right">56.2%</td>
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
<td align="right">106,940</td>
<td align="right">0.2%</td>
<td align="right">48,520</td>
<td align="right">0.1%</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,519,200</td>
<td align="right">8.0%</td>
<td align="right">4,162,000</td>
<td align="right">7.5%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">478,340</td>
<td align="right">0.9%</td>
<td align="right">497,980</td>
<td align="right">0.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,209,400</td>
<td align="right">91.1%</td>
<td align="right">51,082,960</td>
<td align="right">91.6%</td>
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
<td align="left">Failure</td>
<td align="right">11,560</td>
<td align="right">9.8%</td>
<td align="right">13,380</td>
<td align="right">11.9%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105,940</td>
<td align="right">90.2%</td>
<td align="right">99,300</td>
<td align="right">88.1%</td>
<td align="right">-6.3%</td>
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
<td align="left">builtin class method</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">360</td>
<td align="right">2.7%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,860</td>
<td align="right">16.1%</td>
<td align="right">2,460</td>
<td align="right">18.4%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">9,360</td>
<td align="right">81.0%</td>
<td align="right">10,340</td>
<td align="right">77.3%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">220</td>
<td align="right">1.6%</td>
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
<td align="right">50,720,240</td>
<td align="right">99.9%</td>
<td align="right">50,763,440</td>
<td align="right">99.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,680</td>
<td align="right">0.0%</td>
<td align="right">14,680</td>
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
<td align="right">14,760</td>
<td align="right">100.0%</td>
<td align="right">14,760</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
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
<td align="right">4,811,540</td>
<td align="right">100.0%</td>
<td align="right">4,811,540</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">1,232,940</td>
<td align="right">32.8%</td>
<td align="right">877,600</td>
<td align="right">26.5%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,523,180</td>
<td align="right">67.1%</td>
<td align="right">2,427,000</td>
<td align="right">73.4%</td>
<td align="right">-3.8%</td>
</tr>
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
<td align="right">1,560</td>
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
<td align="right">24,780</td>
<td align="right">100.0%</td>
<td align="right">18,100</td>
<td align="right">100.0%</td>
<td align="right">-27.0%</td>
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
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">380</td>
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
<td align="right">1,558,820</td>
<td align="right">100.0%</td>
<td align="right">1,558,820</td>
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
<td align="right">1,294,440</td>
<td align="right">2.6%</td>
<td align="right">1,122,680</td>
<td align="right">2.3%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">96,680</td>
<td align="right">0.2%</td>
<td align="right">93,600</td>
<td align="right">0.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,487,780</td>
<td align="right">97.2%</td>
<td align="right">48,540,060</td>
<td align="right">97.5%</td>
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
<td align="right">1,420</td>
<td align="right">4.3%</td>
<td align="right">1,920</td>
<td align="right">6.3%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">31,820</td>
<td align="right">95.7%</td>
<td align="right">28,620</td>
<td align="right">93.7%</td>
<td align="right">-10.1%</td>
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
<td align="right">120</td>
<td align="right">8.5%</td>
<td align="right">380</td>
<td align="right">19.8%</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">80</td>
<td align="right">5.6%</td>
<td align="right">160</td>
<td align="right">8.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">380</td>
<td align="right">26.8%</td>
<td align="right">540</td>
<td align="right">28.1%</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">540</td>
<td align="right">38.0%</td>
<td align="right">540</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">300</td>
<td align="right">21.1%</td>
<td align="right">300</td>
<td align="right">15.6%</td>
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
<td align="right">15,660</td>
<td align="right">0.1%</td>
<td align="right">15,660</td>
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
<td align="right">15,645,940</td>
<td align="right">99.9%</td>
<td align="right">15,645,940</td>
<td align="right">99.9%</td>
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
<td align="right">780</td>
<td align="right">83.0%</td>
<td align="right">780</td>
<td align="right">83.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">17.0%</td>
<td align="right">160</td>
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
<td align="left">other</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
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
<td align="right">7,359,560</td>
<td align="right">1.6%</td>
<td align="right">6,626,160</td>
<td align="right">1.5%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">184,014,560</td>
<td align="right">40.1%</td>
<td align="right">178,883,320</td>
<td align="right">39.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">262,169,760</td>
<td align="right">57.1%</td>
<td align="right">257,010,440</td>
<td align="right">57.3%</td>
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
<td align="right">5,701,560</td>
<td align="right">1.2%</td>
<td align="right">5,652,060</td>
<td align="right">1.3%</td>
<td align="right">-0.9%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">16,060</td>
<td align="right">0.3%</td>
<td align="right">15,200</td>
<td align="right">0.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">478,340</td>
<td align="right">8.5%</td>
<td align="right">497,980</td>
<td align="right">9.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">96,680</td>
<td align="right">1.7%</td>
<td align="right">93,600</td>
<td align="right">1.7%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,962,700</td>
<td align="right">70.7%</td>
<td align="right">3,898,960</td>
<td align="right">70.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">812,580</td>
<td align="right">14.5%</td>
<td align="right">804,700</td>
<td align="right">14.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">154,320</td>
<td align="right">2.8%</td>
<td align="right">154,280</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,200</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,160</td>
<td align="right">0.3%</td>
<td align="right">17,160</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">15,700</td>
<td align="right">0.3%</td>
<td align="right">15,700</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">15,660</td>
<td align="right">0.3%</td>
<td align="right">15,660</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">14,680</td>
<td align="right">0.3%</td>
<td align="right"></td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">165,800</td>
<td align="right">2.3%</td>
<td align="right">313,200</td>
<td align="right">4.7%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">63,500</td>
<td align="right">0.9%</td>
<td align="right">32,760</td>
<td align="right">0.5%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,232,940</td>
<td align="right">16.8%</td>
<td align="right">877,600</td>
<td align="right">13.2%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">294,680</td>
<td align="right">4.0%</td>
<td align="right">252,380</td>
<td align="right">3.8%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">920,500</td>
<td align="right">12.5%</td>
<td align="right">821,780</td>
<td align="right">12.4%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,709,200</td>
<td align="right">36.8%</td>
<td align="right">2,450,100</td>
<td align="right">37.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,175,300</td>
<td align="right">16.0%</td>
<td align="right">1,108,400</td>
<td align="right">16.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">89,180</td>
<td align="right">1.2%</td>
<td align="right">94,160</td>
<td align="right">1.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">574,200</td>
<td align="right">7.8%</td>
<td align="right">543,000</td>
<td align="right">8.2%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">44,340</td>
<td align="right">0.6%</td>
<td align="right">44,340</td>
<td align="right">0.7%</td>
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
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">37,731,580</td>
<td align="right">78.4%</td>
<td align="right">37,731,580</td>
<td align="right">78.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,912,600</td>
<td align="right">12.3%</td>
<td align="right">5,912,600</td>
<td align="right">12.3%</td>
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
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
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
<td align="right">1,068,500</td>
<td align="right">2.2%</td>
<td align="right">1,068,500</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">84,000</td>
<td align="right">0.2%</td>
<td align="right">84,000</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,199,300</td>
<td align="right">6.6%</td>
<td align="right">3,199,300</td>
<td align="right">6.6%</td>
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
<td align="right">76,480</td>
<td align="right">0.2%</td>
<td align="right">76,480</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">34,911,540</td>
<td align="right">72.5%</td>
<td align="right">34,911,540</td>
<td align="right">72.5%</td>
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
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">19,145</td>
<td align="right"></td>
<td align="right">20,383</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">10,744,377</td>
<td align="right"></td>
<td align="right">11,259,404</td>
<td align="right"></td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">448,484,016</td>
<td align="right">61.6%</td>
<td align="right">462,119,520</td>
<td align="right">62.7%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">434,231,447</td>
<td align="right">67.7%</td>
<td align="right">446,754,971</td>
<td align="right">68.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">206,839,840</td>
<td align="right">32.3%</td>
<td align="right">203,081,340</td>
<td align="right">31.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">645,166</td>
<td align="right"></td>
<td align="right">656,604</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">279,486,900</td>
<td align="right">38.4%</td>
<td align="right">274,619,300</td>
<td align="right">37.3%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">632,403</td>
<td align="right"></td>
<td align="right">642,656</td>
<td align="right"></td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">80,380</td>
<td align="right">0.1%</td>
<td align="right">81,060</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">62,871,015</td>
<td align="right"></td>
<td align="right">62,902,097</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">61,575,014</td>
<td align="right"></td>
<td align="right">61,580,397</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">35,415,600</td>
<td align="right"></td>
<td align="right">35,413,940</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,523,420</td>
<td align="right">63.2%</td>
<td align="right">60,525,820</td>
<td align="right">63.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">35,264,120</td>
<td align="right">36.8%</td>
<td align="right">35,263,020</td>
<td align="right">36.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,442,760</td>
<td align="right">63.1%</td>
<td align="right">60,444,440</td>
<td align="right">63.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">151,840</td>
<td align="right"></td>
<td align="right">151,840</td>
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
<td align="right">260</td>
<td align="right">185,240</td>
<td align="right">7,368,360</td>
<td align="right">260</td>
<td align="right">186,540</td>
<td align="right">7,351,480</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">8,900</td>
<td align="right">49.5%</td>
<td align="right">11,380</td>
<td align="right">52.1%</td>
<td align="right">27.9%</td>
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
<td align="right">2.8%</td>
<td align="right">620</td>
<td align="right">2.8%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">9,980</td>
<td align="right">55.5%</td>
<td align="right">12,340</td>
<td align="right">56.5%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">800</td>
<td align="right">4.4%</td>
<td align="right">980</td>
<td align="right">4.5%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,980</td>
<td align="right"></td>
<td align="right">21,840</td>
<td align="right"></td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,040</td>
<td align="right">50.3%</td>
<td align="right">10,420</td>
<td align="right">47.7%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">64,265,020</td>
<td align="right"></td>
<td align="right">71,796,280</td>
<td align="right"></td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">947,401,940</td>
<td align="right">1,474.2%</td>
<td align="right">993,010,700</td>
<td align="right">1,383.1%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">360</td>
<td align="right">4.0%</td>
<td align="right">460</td>
<td align="right">4.4%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">8,400</td>
<td align="right">92.9%</td>
<td align="right">9,700</td>
<td align="right">93.1%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">9,040</td>
<td align="right"></td>
<td align="right">10,420</td>
<td align="right"></td>
<td align="right">15.3%</td>
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
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">400</td>
<td align="right">3.8%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,560</td>
<td align="right">17.3%</td>
<td align="right">1,740</td>
<td align="right">16.7%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,200</td>
<td align="right">13.3%</td>
<td align="right">1,440</td>
<td align="right">13.8%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,940</td>
<td align="right">21.5%</td>
<td align="right">2,280</td>
<td align="right">21.9%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,900</td>
<td align="right">21.0%</td>
<td align="right">2,140</td>
<td align="right">20.5%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,360</td>
<td align="right">15.0%</td>
<td align="right">1,520</td>
<td align="right">14.6%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">740</td>
<td align="right">8.2%</td>
<td align="right">820</td>
<td align="right">7.9%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
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
<td align="right">1,280</td>
<td align="right">14.2%</td>
<td align="right">1,600</td>
<td align="right">15.4%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,220</td>
<td align="right">13.5%</td>
<td align="right">1,360</td>
<td align="right">13.1%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,740</td>
<td align="right">19.2%</td>
<td align="right">2,040</td>
<td align="right">19.6%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,700</td>
<td align="right">18.8%</td>
<td align="right">1,860</td>
<td align="right">17.9%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,360</td>
<td align="right">15.0%</td>
<td align="right">1,620</td>
<td align="right">15.5%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">840</td>
<td align="right">9.3%</td>
<td align="right">960</td>
<td align="right">9.2%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">260</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">631,620</td>
<td align="right">1,523,460</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">4,800</td>
<td align="right">11,380</td>
<td align="right">137.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,800</td>
<td align="right">11,380</td>
<td align="right">137.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,098,760</td>
<td align="right">2,549,440</td>
<td align="right">132.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">467,140</td>
<td align="right">1,025,980</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">467,140</td>
<td align="right">1,025,980</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,043,200</td>
<td align="right">2,048,000</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">740</td>
<td align="right">1,400</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">25,640</td>
<td align="right">3,240</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">25,640</td>
<td align="right">3,240</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">590,980</td>
<td align="right">1,035,820</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">25,400</td>
<td align="right">44,220</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">25,400</td>
<td align="right">44,220</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">33,640</td>
<td align="right">11,440</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">3,140</td>
<td align="right">4,820</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">3,140</td>
<td align="right">4,820</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">1,204,260</td>
<td align="right">1,683,280</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,204,260</td>
<td align="right">1,683,280</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">83,120</td>
<td align="right">116,140</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">85,840</td>
<td align="right">118,860</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">6,160</td>
<td align="right">8,500</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">169,940</td>
<td align="right">218,520</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,760</td>
<td align="right">6,080</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,760</td>
<td align="right">6,080</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">421,380</td>
<td align="right">535,400</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2,540</td>
<td align="right">3,220</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">453,080</td>
<td align="right">572,500</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">477,740</td>
<td align="right">355,740</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,460</td>
<td align="right">4,320</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">859,100</td>
<td align="right">1,060,820</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">5,660</td>
<td align="right">6,980</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,623,700</td>
<td align="right">4,427,620</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">421,080</td>
<td align="right">509,240</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">421,080</td>
<td align="right">509,240</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">68,080</td>
<td align="right">81,620</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">809,000</td>
<td align="right">668,240</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">49,400</td>
<td align="right">56,880</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2,548,980</td>
<td align="right">2,164,720</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">36,233,000</td>
<td align="right">41,529,720</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">248,660</td>
<td align="right">284,520</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">57,785,800</td>
<td align="right">65,420,000</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">14,405,640</td>
<td align="right">16,136,820</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">64,265,020</td>
<td align="right">71,796,280</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">9,800</td>
<td align="right">10,940</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">719,380</td>
<td align="right">641,180</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,038,140</td>
<td align="right">4,470,560</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,126,840</td>
<td align="right">1,007,060</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,126,840</td>
<td align="right">1,007,060</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">75,680</td>
<td align="right">83,720</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">415,320</td>
<td align="right">459,440</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">407,460</td>
<td align="right">365,880</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">678,300</td>
<td align="right">745,760</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">408,460</td>
<td align="right">447,260</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,028,240</td>
<td align="right">1,108,180</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,791,280</td>
<td align="right">4,083,320</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,380,840</td>
<td align="right">1,275,800</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">136,960</td>
<td align="right">146,780</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">11,035,640</td>
<td align="right">11,821,880</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">9,316,160</td>
<td align="right">9,977,280</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right">7,380</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,049,460</td>
<td align="right">3,259,260</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">462,460</td>
<td align="right">492,080</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">288,980</td>
<td align="right">306,680</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">89,428,340</td>
<td align="right">94,715,500</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">38,820</td>
<td align="right">41,100</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,064,760</td>
<td align="right">2,185,060</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,133,520</td>
<td align="right">3,281,220</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,944,260</td>
<td align="right">10,401,740</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">39,260</td>
<td align="right">41,000</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,846,440</td>
<td align="right">6,099,820</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,949,560</td>
<td align="right">1,865,080</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,272,800</td>
<td align="right">4,456,540</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">36,000</td>
<td align="right">37,520</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">60,313,920</td>
<td align="right">62,797,580</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">15,963,480</td>
<td align="right">16,609,080</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">195,260</td>
<td align="right">203,140</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">6,772,100</td>
<td align="right">7,038,180</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">17,447,920</td>
<td align="right">18,055,680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">92,520</td>
<td align="right">95,680</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">11,570,500</td>
<td align="right">11,186,940</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">19,960</td>
<td align="right">20,620</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">39,420</td>
<td align="right">40,720</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,296,840</td>
<td align="right">2,372,540</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,799,300</td>
<td align="right">2,708,000</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,728,340</td>
<td align="right">5,904,580</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">11,768,340</td>
<td align="right">12,126,700</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">45,540</td>
<td align="right">46,840</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">23,509,440</td>
<td align="right">24,147,720</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,787,640</td>
<td align="right">3,886,020</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">32,039,720</td>
<td align="right">32,870,200</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">32,835,140</td>
<td align="right">33,658,560</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">80,620</td>
<td align="right">82,600</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,691,160</td>
<td align="right">7,510,220</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">10,631,100</td>
<td align="right">10,388,940</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">21,808,560</td>
<td align="right">22,296,120</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,794,480</td>
<td align="right">3,879,240</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">7,229,960</td>
<td align="right">7,069,040</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">20,458,280</td>
<td align="right">20,889,200</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">621,460</td>
<td align="right">608,380</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">1,286,080</td>
<td align="right">1,312,900</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">13,540</td>
<td align="right">13,820</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">13,540</td>
<td align="right">13,820</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,811,400</td>
<td align="right">3,890,060</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,224,760</td>
<td align="right">2,180,280</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">55,120</td>
<td align="right">56,200</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,377,640</td>
<td align="right">3,443,740</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">5,914,920</td>
<td align="right">6,028,800</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,047,580</td>
<td align="right">23,489,540</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">4,501,660</td>
<td align="right">4,585,080</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,187,140</td>
<td align="right">12,943,560</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">9,758,220</td>
<td align="right">9,591,100</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,463,520</td>
<td align="right">6,359,900</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">89,120</td>
<td align="right">90,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">136,680</td>
<td align="right">138,660</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,742,080</td>
<td align="right">6,835,160</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">809,620</td>
<td align="right">819,720</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,349,120</td>
<td align="right">17,563,060</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3,767,760</td>
<td align="right">3,812,680</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,172,920</td>
<td align="right">18,947,720</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">7,032,680</td>
<td align="right">7,110,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">905,340</td>
<td align="right">915,260</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">4,520,820</td>
<td align="right">4,569,820</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1,034,380</td>
<td align="right">1,044,980</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,611,500</td>
<td align="right">1,627,500</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,745,540</td>
<td align="right">5,801,360</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,935,020</td>
<td align="right">9,016,960</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,921,100</td>
<td align="right">8,999,420</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">517,900</td>
<td align="right">522,180</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,152,300</td>
<td align="right">6,195,440</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">428,200</td>
<td align="right">431,100</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,763,240</td>
<td align="right">18,887,980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">504,280</td>
<td align="right">507,500</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,047,440</td>
<td align="right">9,094,360</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,047,440</td>
<td align="right">9,094,360</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">429,780</td>
<td align="right">431,840</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">3,752,180</td>
<td align="right">3,769,660</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,575,540</td>
<td align="right">2,587,240</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,100,300</td>
<td align="right">1,105,140</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,150,640</td>
<td align="right">1,155,660</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">15,202,000</td>
<td align="right">15,265,740</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,245,440</td>
<td align="right">2,252,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,232,280</td>
<td align="right">1,235,840</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">107,980</td>
<td align="right">108,280</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,130,160</td>
<td align="right">2,135,820</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">28,890,360</td>
<td align="right">28,818,600</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">8,928,280</td>
<td align="right">8,948,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">207,080</td>
<td align="right">207,540</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">413,040</td>
<td align="right">413,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">21,287,120</td>
<td align="right">21,251,200</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">440,320</td>
<td align="right">440,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">440,320</td>
<td align="right">440,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,066,620</td>
<td align="right">2,068,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,233,600</td>
<td align="right">2,234,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">109,660</td>
<td align="right">109,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">971,200</td>
<td align="right">971,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">291,020</td>
<td align="right">291,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">140,480</td>
<td align="right">140,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">21,440</td>
<td align="right">21,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">13,160</td>
<td align="right">13,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">9,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,120</td>
<td align="right">6,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">280</td>
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
<td align="right">420</td>
<td align="right">960</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">440</td>
<td align="right">300</td>
<td align="right">-31.8%</td>
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
Stats gathered on: 2024-09-13
