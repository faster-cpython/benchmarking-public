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
<td align="left">END_SEND</td>
<td align="right">1,030,080</td>
<td align="right">55,340</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,964,600</td>
<td align="right">139,560</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,553,540</td>
<td align="right">143,960</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">73,580</td>
<td align="right">8,840</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">75,260</td>
<td align="right">10,520</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,217,980</td>
<td align="right">201,120</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,480,560</td>
<td align="right">597,300</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">279,980</td>
<td align="right">48,060</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,195,480</td>
<td align="right">1,013,100</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">574,680</td>
<td align="right">190,560</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,873,860</td>
<td align="right">2,118,360</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">467,000</td>
<td align="right">171,280</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,867,580</td>
<td align="right">9,027,100</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,980,000</td>
<td align="right">2,365,940</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,296,240</td>
<td align="right">1,836,460</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,003,360</td>
<td align="right">2,652,280</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,173,160</td>
<td align="right">2,929,000</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,298,320</td>
<td align="right">1,105,920</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,913,720</td>
<td align="right">9,815,260</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,139,780</td>
<td align="right">1,732,460</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,728,560</td>
<td align="right">973,560</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,075,420</td>
<td align="right">609,080</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,020,040</td>
<td align="right">578,700</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,026,800</td>
<td align="right">4,648,440</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,732,600</td>
<td align="right">7,956,440</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,274,040</td>
<td align="right">6,116,540</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">581,100</td>
<td align="right">359,560</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,031,840</td>
<td align="right">10,903,920</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">21,231,380</td>
<td align="right">13,873,180</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">10,029,280</td>
<td align="right">6,764,940</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">21,011,520</td>
<td align="right">14,279,500</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">851,100</td>
<td align="right">583,820</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,752,000</td>
<td align="right">1,895,780</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,839,020</td>
<td align="right">2,671,720</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,966,420</td>
<td align="right">11,128,780</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,960,820</td>
<td align="right">2,772,840</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,955,720</td>
<td align="right">1,402,180</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,192,600</td>
<td align="right">3,023,720</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">74,705,800</td>
<td align="right">54,471,840</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">33,037,920</td>
<td align="right">24,606,220</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">127,280</td>
<td align="right">94,860</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">411,120</td>
<td align="right">307,580</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,335,340</td>
<td align="right">7,001,480</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">904,640</td>
<td align="right">693,060</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,269,560</td>
<td align="right">20,838,860</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,240,440</td>
<td align="right">11,013,340</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">61,680</td>
<td align="right">71,900</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,745,440</td>
<td align="right">4,806,220</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">130,460</td>
<td align="right">150,840</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">512,880</td>
<td align="right">442,260</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,473,300</td>
<td align="right">1,272,200</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,134,260</td>
<td align="right">986,140</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,942,740</td>
<td align="right">13,024,080</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,695,720</td>
<td align="right">6,765,900</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">592,340</td>
<td align="right">524,160</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,082,420</td>
<td align="right">1,862,040</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">35,300</td>
<td align="right">37,880</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">112,980</td>
<td align="right">106,560</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,648,700</td>
<td align="right">6,272,440</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">277,160</td>
<td align="right">262,620</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">62,920</td>
<td align="right">66,180</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">229,320</td>
<td align="right">217,800</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">796,140</td>
<td align="right">761,020</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,331,880</td>
<td align="right">3,188,420</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,893,320</td>
<td align="right">2,786,960</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">800,600</td>
<td align="right">772,520</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">86,840</td>
<td align="right">89,420</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">941,280</td>
<td align="right">963,060</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">194,520</td>
<td align="right">190,140</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">53,220</td>
<td align="right">54,380</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,900</td>
<td align="right">58,020</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">19,640</td>
<td align="right">19,260</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,860</td>
<td align="right">11,680</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,046,400</td>
<td align="right">2,024,860</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,207,860</td>
<td align="right">1,195,760</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">361,640</td>
<td align="right">358,200</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,091,620</td>
<td align="right">1,101,840</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,176,460</td>
<td align="right">1,166,100</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">417,800</td>
<td align="right">414,360</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">543,260</td>
<td align="right">538,840</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">149,740</td>
<td align="right">150,900</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">91,620</td>
<td align="right">92,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">16,600</td>
<td align="right">16,500</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">84,860</td>
<td align="right">85,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">84,860</td>
<td align="right">85,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,855,480</td>
<td align="right">1,848,020</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">161,540</td>
<td align="right">161,960</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,684,660</td>
<td align="right">1,680,280</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,560,960</td>
<td align="right">1,557,420</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">163,080</td>
<td align="right">162,860</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,427,540</td>
<td align="right">10,414,100</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">713,720</td>
<td align="right">712,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">131,120</td>
<td align="right">131,260</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,938,620</td>
<td align="right">1,936,960</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">220,920</td>
<td align="right">221,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">341,480</td>
<td align="right">341,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">192,800</td>
<td align="right">192,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">104,420</td>
<td align="right">104,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,211,680</td>
<td align="right">3,211,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">287,120</td>
<td align="right">287,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">196,260</td>
<td align="right">196,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">193,760</td>
<td align="right">193,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">178,460</td>
<td align="right">178,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">166,000</td>
<td align="right">166,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">156,840</td>
<td align="right">156,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">156,200</td>
<td align="right">156,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">155,040</td>
<td align="right">155,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">100,060</td>
<td align="right">100,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">91,200</td>
<td align="right">91,200</td>
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
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">72,540</td>
<td align="right">72,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">40,040</td>
<td align="right">40,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">34,320</td>
<td align="right">34,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">31,100</td>
<td align="right">31,100</td>
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
<td align="right">24,060</td>
<td align="right">24,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">16,680</td>
<td align="right">16,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,000</td>
<td align="right">11,000</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,960</td>
<td align="right">2,960</td>
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
<td align="right">18,460</td>
<td align="right">2.1%</td>
<td align="right">18,080</td>
<td align="right">2.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">97.8%</td>
<td align="right">867,940</td>
<td align="right">97.8%</td>
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
<td align="left">Success</td>
<td align="right">480</td>
<td align="right">40.7%</td>
<td align="right">480</td>
<td align="right">40.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">700</td>
<td align="right">59.3%</td>
<td align="right">700</td>
<td align="right">59.3%</td>
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
<td align="right">660</td>
<td align="right">94.3%</td>
<td align="right">660</td>
<td align="right">94.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">40</td>
<td align="right">5.7%</td>
<td align="right">40</td>
<td align="right">5.7%</td>
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
<td align="right">62,920</td>
<td align="right">100.0%</td>
<td align="right">66,180</td>
<td align="right">100.0%</td>
<td align="right">5.2%</td>
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
<td align="right">15,680</td>
<td align="right">0.6%</td>
<td align="right">15,680</td>
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
<td align="left">Success</td>
<td align="right">760</td>
<td align="right">69.1%</td>
<td align="right">760</td>
<td align="right">69.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">340</td>
<td align="right">30.9%</td>
<td align="right">340</td>
<td align="right">30.9%</td>
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
<td align="right">240</td>
<td align="right">70.6%</td>
<td align="right">240</td>
<td align="right">70.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">100</td>
<td align="right">29.4%</td>
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
<td align="right">441,880</td>
<td align="right">0.5%</td>
<td align="right">453,540</td>
<td align="right">0.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,035,540</td>
<td align="right">99.5%</td>
<td align="right">87,024,100</td>
<td align="right">99.4%</td>
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
<td align="right">26,880</td>
<td align="right">100.0%</td>
<td align="right">27,100</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">845,940</td>
<td align="right">43.9%</td>
<td align="right">578,840</td>
<td align="right">35.7%</td>
<td align="right">-31.6%</td>
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
<td align="right">55.8%</td>
<td align="right">1,036,780</td>
<td align="right">64.0%</td>
<td align="right">-3.5%</td>
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
<td align="right">4,360</td>
<td align="right">84.5%</td>
<td align="right">4,180</td>
<td align="right">83.9%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">800</td>
<td align="right">15.5%</td>
<td align="right">800</td>
<td align="right">16.1%</td>
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
<td align="right">420</td>
<td align="right">9.6%</td>
<td align="right">240</td>
<td align="right">5.7%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,920</td>
<td align="right">44.0%</td>
<td align="right">1,920</td>
<td align="right">45.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,500</td>
<td align="right">34.4%</td>
<td align="right">1,500</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">220</td>
<td align="right">5.0%</td>
<td align="right">220</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">120</td>
<td align="right">2.8%</td>
<td align="right">120</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">100</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">80</td>
<td align="right">1.8%</td>
<td align="right">80</td>
<td align="right">1.9%</td>
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
<td align="right">154,280</td>
<td align="right">21.5%</td>
<td align="right">154,280</td>
<td align="right">21.5%</td>
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
<td align="right">527,560</td>
<td align="right">73.5%</td>
<td align="right">527,560</td>
<td align="right">73.5%</td>
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
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">48.8%</td>
<td align="right">1,240</td>
<td align="right">48.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,300</td>
<td align="right">51.2%</td>
<td align="right">1,300</td>
<td align="right">51.2%</td>
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
<td align="right">920</td>
<td align="right">70.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">380</td>
<td align="right">29.2%</td>
<td align="right">380</td>
<td align="right">29.2%</td>
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
<td align="right">3,953,740</td>
<td align="right">47.3%</td>
<td align="right">2,766,080</td>
<td align="right">43.1%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,404,340</td>
<td align="right">52.7%</td>
<td align="right">3,649,340</td>
<td align="right">56.8%</td>
<td align="right">-17.1%</td>
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
<td align="right">5,420</td>
<td align="right">76.6%</td>
<td align="right">5,100</td>
<td align="right">75.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,660</td>
<td align="right">23.4%</td>
<td align="right">1,660</td>
<td align="right">24.6%</td>
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
<td align="right">2,720</td>
<td align="right">50.2%</td>
<td align="right">2,460</td>
<td align="right">48.2%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">740</td>
<td align="right">13.7%</td>
<td align="right">680</td>
<td align="right">13.3%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">440</td>
<td align="right">8.1%</td>
<td align="right">440</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">360</td>
<td align="right">6.6%</td>
<td align="right">360</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">340</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">320</td>
<td align="right">5.9%</td>
<td align="right">320</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">3.7%</td>
<td align="right">200</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">180</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">120</td>
<td align="right">2.2%</td>
<td align="right">120</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,743,840</td>
<td align="right">8.3%</td>
<td align="right">3,592,960</td>
<td align="right">7.1%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,967,380</td>
<td align="right">90.8%</td>
<td align="right">46,449,140</td>
<td align="right">91.8%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">510,140</td>
<td align="right">0.9%</td>
<td align="right">505,740</td>
<td align="right">1.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">103,100</td>
<td align="right">0.2%</td>
<td align="right">103,100</td>
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
<td align="right">110,120</td>
<td align="right">90.5%</td>
<td align="right">88,500</td>
<td align="right">88.4%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,620</td>
<td align="right">9.5%</td>
<td align="right">11,600</td>
<td align="right">11.6%</td>
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
<td align="left">mutable class</td>
<td align="right">9,420</td>
<td align="right">81.1%</td>
<td align="right">9,400</td>
<td align="right">81.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,860</td>
<td align="right">16.0%</td>
<td align="right">1,860</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
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
<td align="right">53,164,780</td>
<td align="right">99.9%</td>
<td align="right">36,568,280</td>
<td align="right">99.9%</td>
<td align="right">-31.2%</td>
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
<td align="right">1,136,400</td>
<td align="right">31.5%</td>
<td align="right">732,320</td>
<td align="right">20.5%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,467,300</td>
<td align="right">68.4%</td>
<td align="right">2,837,520</td>
<td align="right">79.4%</td>
<td align="right">15.0%</td>
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
<td align="right">22,940</td>
<td align="right">100.0%</td>
<td align="right">15,320</td>
<td align="right">100.0%</td>
<td align="right">-33.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,577,020</td>
<td align="right">97.1%</td>
<td align="right">47,830,760</td>
<td align="right">97.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,354,940</td>
<td align="right">2.7%</td>
<td align="right">1,344,640</td>
<td align="right">2.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">95,040</td>
<td align="right">0.2%</td>
<td align="right">95,020</td>
<td align="right">0.2%</td>
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
<td align="right">32,960</td>
<td align="right">95.5%</td>
<td align="right">32,800</td>
<td align="right">95.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,540</td>
<td align="right">4.5%</td>
<td align="right">1,540</td>
<td align="right">4.5%</td>
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
<td align="left">dict</td>
<td align="right">540</td>
<td align="right">35.1%</td>
<td align="right">540</td>
<td align="right">35.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">380</td>
<td align="right">24.7%</td>
<td align="right">380</td>
<td align="right">24.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">300</td>
<td align="right">19.5%</td>
<td align="right">300</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">240</td>
<td align="right">15.6%</td>
<td align="right">240</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">80</td>
<td align="right">5.2%</td>
<td align="right">80</td>
<td align="right">5.2%</td>
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
<td align="right">15,560</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
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
<td align="right">15,644,280</td>
<td align="right">99.9%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">190,872,120</td>
<td align="right">40.5%</td>
<td align="right">130,556,760</td>
<td align="right">40.2%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">266,777,680</td>
<td align="right">56.6%</td>
<td align="right">183,851,940</td>
<td align="right">56.6%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,802,480</td>
<td align="right">1.2%</td>
<td align="right">4,345,560</td>
<td align="right">1.3%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,721,860</td>
<td align="right">1.6%</td>
<td align="right">6,168,140</td>
<td align="right">1.9%</td>
<td align="right">-20.1%</td>
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
<td align="right">845,940</td>
<td align="right">14.8%</td>
<td align="right">578,840</td>
<td align="right">13.6%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,953,740</td>
<td align="right">69.3%</td>
<td align="right">2,766,080</td>
<td align="right">65.1%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">62,920</td>
<td align="right">1.1%</td>
<td align="right">66,180</td>
<td align="right">1.6%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,460</td>
<td align="right">0.3%</td>
<td align="right">18,080</td>
<td align="right">0.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">510,140</td>
<td align="right">8.9%</td>
<td align="right">505,740</td>
<td align="right">11.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">15,660</td>
<td align="right">0.3%</td>
<td align="right">15,560</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">95,040</td>
<td align="right">1.7%</td>
<td align="right">95,020</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">154,280</td>
<td align="right">2.7%</td>
<td align="right">154,280</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,160</td>
<td align="right">0.3%</td>
<td align="right">17,160</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">15,680</td>
<td align="right">0.3%</td>
<td align="right">15,680</td>
<td align="right">0.4%</td>
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
<td align="right">2,882,240</td>
<td align="right">37.3%</td>
<td align="right">1,757,160</td>
<td align="right">28.5%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,136,400</td>
<td align="right">14.7%</td>
<td align="right">732,320</td>
<td align="right">11.9%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">48,300</td>
<td align="right">0.6%</td>
<td align="right">34,560</td>
<td align="right">0.6%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">305,260</td>
<td align="right">4.0%</td>
<td align="right">316,920</td>
<td align="right">5.1%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">612,560</td>
<td align="right">7.9%</td>
<td align="right">600,500</td>
<td align="right">9.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">970,280</td>
<td align="right">12.6%</td>
<td align="right">964,440</td>
<td align="right">15.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">305,700</td>
<td align="right">4.0%</td>
<td align="right">304,640</td>
<td align="right">4.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,184,580</td>
<td align="right">15.3%</td>
<td align="right">1,184,580</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">123,100</td>
<td align="right">1.6%</td>
<td align="right">123,100</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">62,440</td>
<td align="right">0.8%</td>
<td align="right">62,440</td>
<td align="right">1.0%</td>
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
<td align="right">3,203,180</td>
<td align="right">6.7%</td>
<td align="right">3,189,740</td>
<td align="right">6.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,514,940</td>
<td align="right">9.4%</td>
<td align="right">4,501,500</td>
<td align="right">9.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,514,940</td>
<td align="right">9.4%</td>
<td align="right">4,501,500</td>
<td align="right">9.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">10,427,540</td>
<td align="right">21.7%</td>
<td align="right">10,414,100</td>
<td align="right">21.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,427,540</td>
<td align="right">21.7%</td>
<td align="right">10,414,100</td>
<td align="right">21.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">37,727,700</td>
<td align="right">78.3%</td>
<td align="right">37,741,140</td>
<td align="right">78.4%</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">213,542,020</td>
<td align="right">24.1%</td>
<td align="right">161,724,360</td>
<td align="right">18.3%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">57,782,620</td>
<td align="right">6.5%</td>
<td align="right">46,312,400</td>
<td align="right">5.2%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">282,437,360</td>
<td align="right">28.9%</td>
<td align="right">230,365,140</td>
<td align="right">23.5%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">10,775,720</td>
<td align="right"></td>
<td align="right">12,685,397</td>
<td align="right"></td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">426,509,290</td>
<td align="right">48.1%</td>
<td align="right">484,985,002</td>
<td align="right">54.8%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">444,530,985</td>
<td align="right">45.5%</td>
<td align="right">503,268,249</td>
<td align="right">51.3%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">49,120,940</td>
<td align="right">5.0%</td>
<td align="right">43,200,720</td>
<td align="right">4.4%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">24,047</td>
<td align="right"></td>
<td align="right">25,679</td>
<td align="right"></td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">93,460</td>
<td align="right">0.1%</td>
<td align="right">96,940</td>
<td align="right">0.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">654,760</td>
<td align="right"></td>
<td align="right">641,423</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">200,616,207</td>
<td align="right">20.5%</td>
<td align="right">204,327,473</td>
<td align="right">20.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">188,901,723</td>
<td align="right">21.3%</td>
<td align="right">192,183,921</td>
<td align="right">21.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">672,751</td>
<td align="right"></td>
<td align="right">661,072</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">62,805,973</td>
<td align="right"></td>
<td align="right">62,791,641</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,548,680</td>
<td align="right">63.2%</td>
<td align="right">60,557,200</td>
<td align="right">63.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">61,602,359</td>
<td align="right"></td>
<td align="right">61,609,621</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,454,000</td>
<td align="right">63.1%</td>
<td align="right">60,458,920</td>
<td align="right">63.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">35,258,740</td>
<td align="right">36.8%</td>
<td align="right">35,258,980</td>
<td align="right">36.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">35,409,080</td>
<td align="right"></td>
<td align="right">35,409,320</td>
<td align="right"></td>
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
<td align="right">181,060</td>
<td align="right">7,434,580</td>
<td align="right">260</td>
<td align="right">181,080</td>
<td align="right">7,435,580</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">11,940</td>
<td align="right">31.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">9,160</td>
<td align="right">24.3%</td>
<td align="right">4,620</td>
<td align="right">11.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">988,347,280</td>
<td align="right">1,592.9%</td>
<td align="right">1,284,487,260</td>
<td align="right">1,707.4%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">28,420</td>
<td align="right">75.5%</td>
<td align="right">35,640</td>
<td align="right">88.4%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">62,045,500</td>
<td align="right"></td>
<td align="right">75,231,820</td>
<td align="right"></td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">860</td>
<td align="right">2.3%</td>
<td align="right">980</td>
<td align="right">2.4%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,420</td>
<td align="right">6.4%</td>
<td align="right">2,640</td>
<td align="right">6.6%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">37,640</td>
<td align="right"></td>
<td align="right">40,300</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">480</td>
<td align="right">1.3%</td>
<td align="right">500</td>
<td align="right">1.2%</td>
<td align="right">4.2%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">400</td>
<td align="right">1.4%</td>
<td align="right">580</td>
<td align="right">1.6%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">28,420</td>
<td align="right"></td>
<td align="right">35,640</td>
<td align="right"></td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">27,620</td>
<td align="right">97.2%</td>
<td align="right">34,600</td>
<td align="right">97.1%</td>
<td align="right">25.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,600</td>
<td align="right">9.1%</td>
<td align="right">3,760</td>
<td align="right">10.5%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,440</td>
<td align="right">19.1%</td>
<td align="right">7,420</td>
<td align="right">20.8%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">8,680</td>
<td align="right">30.5%</td>
<td align="right">9,780</td>
<td align="right">27.4%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,420</td>
<td align="right">19.1%</td>
<td align="right">6,680</td>
<td align="right">18.7%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,580</td>
<td align="right">12.6%</td>
<td align="right">4,900</td>
<td align="right">13.7%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,140</td>
<td align="right">7.5%</td>
<td align="right">2,440</td>
<td align="right">6.8%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">560</td>
<td align="right">2.0%</td>
<td align="right">660</td>
<td align="right">1.9%</td>
<td align="right">17.9%</td>
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
<td align="right">1,880</td>
<td align="right">6.6%</td>
<td align="right">1,400</td>
<td align="right">3.9%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,260</td>
<td align="right">15.0%</td>
<td align="right">7,480</td>
<td align="right">21.0%</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,560</td>
<td align="right">19.6%</td>
<td align="right">6,400</td>
<td align="right">18.0%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,360</td>
<td align="right">25.9%</td>
<td align="right">9,020</td>
<td align="right">25.3%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,740</td>
<td align="right">16.7%</td>
<td align="right">5,860</td>
<td align="right">16.4%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,420</td>
<td align="right">8.5%</td>
<td align="right">2,920</td>
<td align="right">8.2%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,400</td>
<td align="right">4.9%</td>
<td align="right">1,520</td>
<td align="right">4.3%</td>
<td align="right">8.6%</td>
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
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">33,920</td>
<td align="right">3,647,980</td>
<td align="right">10,654.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,720</td>
<td align="right">1,225,120</td>
<td align="right">3,644.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,740</td>
<td align="right">1,483,060</td>
<td align="right">1,858.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">23,020</td>
<td align="right">407,140</td>
<td align="right">1,668.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">125,180</td>
<td align="right">1,534,760</td>
<td align="right">1,126.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">451,800</td>
<td align="right">3,335,060</td>
<td align="right">638.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">357,160</td>
<td align="right">1,778,540</td>
<td align="right">398.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,069,120</td>
<td align="right">23,552,400</td>
<td align="right">288.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">6,848,480</td>
<td align="right">24,871,340</td>
<td align="right">263.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">26,620</td>
<td align="right">92,220</td>
<td align="right">246.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">11,400</td>
<td align="right">39,480</td>
<td align="right">246.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">11,400</td>
<td align="right">39,480</td>
<td align="right">246.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">27,960</td>
<td align="right">93,560</td>
<td align="right">234.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">161,900</td>
<td align="right">466,940</td>
<td align="right">188.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,260</td>
<td align="right">9,100</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">115,800</td>
<td align="right">258,960</td>
<td align="right">123.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,369,500</td>
<td align="right">7,125,000</td>
<td align="right">111.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,306,480</td>
<td align="right">6,723,460</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,510,640</td>
<td align="right">4,970,420</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,061,160</td>
<td align="right">3,886,200</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">290,900</td>
<td align="right">512,440</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">602,520</td>
<td align="right">1,043,860</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,641,740</td>
<td align="right">10,626,780</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">9,833,400</td>
<td align="right">15,609,740</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,102,480</td>
<td align="right">11,237,500</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">410,240</td>
<td align="right">634,240</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">6,171,280</td>
<td align="right">9,522,360</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">698,320</td>
<td align="right">322,920</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,598,640</td>
<td align="right">12,945,740</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">11,966,620</td>
<td align="right">17,890,380</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">448,140</td>
<td align="right">668,520</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,982,800</td>
<td align="right">10,361,160</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,834,420</td>
<td align="right">12,998,540</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,636,420</td>
<td align="right">3,870,480</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">639,100</td>
<td align="right">934,820</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,859,120</td>
<td align="right">2,715,340</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">436,940</td>
<td align="right">638,040</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">26,380</td>
<td align="right">38,480</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">14,051,840</td>
<td align="right">19,852,160</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">10,657,520</td>
<td align="right">15,031,240</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,756,960</td>
<td align="right">5,287,020</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">16,594,620</td>
<td align="right">23,270,580</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">21,642,080</td>
<td align="right">30,077,620</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">20,885,800</td>
<td align="right">28,682,900</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">27,726,780</td>
<td align="right">37,738,680</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,060</td>
<td align="right">1,440</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">3,260</td>
<td align="right">2,100</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">88,121,480</td>
<td align="right">119,365,480</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,481,980</td>
<td align="right">2,001,660</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">59,194,360</td>
<td align="right">79,316,420</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">17,919,940</td>
<td align="right">23,833,480</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">22,077,760</td>
<td align="right">29,061,300</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">13,200</td>
<td align="right">17,280</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">19,983,800</td>
<td align="right">26,111,720</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">107,280</td>
<td align="right">139,700</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">31,176,440</td>
<td align="right">40,353,560</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">2,360</td>
<td align="right">1,680</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">2,360</td>
<td align="right">1,680</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">22,999,380</td>
<td align="right">29,607,600</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,357,420</td>
<td align="right">23,605,660</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">31,984,840</td>
<td align="right">40,537,380</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">13,600</td>
<td align="right">17,040</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">13,600</td>
<td align="right">17,040</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">10,568,300</td>
<td align="right">12,850,800</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,115,120</td>
<td align="right">7,421,480</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">62,045,500</td>
<td align="right">75,231,820</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,743,920</td>
<td align="right">4,523,800</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">64,717,580</td>
<td align="right">77,924,480</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">8,068,340</td>
<td align="right">9,611,020</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">32,988,400</td>
<td align="right">39,154,520</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,221,540</td>
<td align="right">1,442,080</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,448,120</td>
<td align="right">11,038,500</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,058,960</td>
<td align="right">4,727,380</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">15,008,140</td>
<td align="right">17,379,640</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">436,940</td>
<td align="right">505,120</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,265,060</td>
<td align="right">19,951,140</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,871,600</td>
<td align="right">4,458,660</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,584,320</td>
<td align="right">2,937,800</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,897,080</td>
<td align="right">10,064,380</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">31,960</td>
<td align="right">28,700</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">50,300</td>
<td align="right">54,680</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">53,080</td>
<td align="right">57,460</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,305,920</td>
<td align="right">10,060,920</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,305,920</td>
<td align="right">10,060,920</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">15,210,960</td>
<td align="right">16,398,620</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">55,961,360</td>
<td align="right">51,660,340</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">704,680</td>
<td align="right">650,620</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,011,080</td>
<td align="right">1,081,700</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,091,120</td>
<td align="right">3,302,700</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2,492,380</td>
<td align="right">2,643,340</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,188,760</td>
<td align="right">2,295,120</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,120,560</td>
<td align="right">1,066,500</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,120,560</td>
<td align="right">1,066,500</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">4,483,080</td>
<td align="right">4,694,180</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">815,640</td>
<td align="right">850,760</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">11,776,260</td>
<td align="right">12,243,580</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">29,520</td>
<td align="right">28,360</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,457,360</td>
<td align="right">1,405,220</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">741,560</td>
<td align="right">767,800</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">2,217,380</td>
<td align="right">2,151,040</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">15,060</td>
<td align="right">14,640</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">15,060</td>
<td align="right">14,640</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">155,920</td>
<td align="right">159,520</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">204,420</td>
<td align="right">208,900</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">760,020</td>
<td align="right">745,820</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">760,020</td>
<td align="right">745,820</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,828,300</td>
<td align="right">5,935,620</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">23,100</td>
<td align="right">22,680</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">1,281,660</td>
<td align="right">1,296,200</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,820</td>
<td align="right">1,800</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,194,900</td>
<td align="right">2,174,520</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,770,500</td>
<td align="right">3,804,900</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">19,980</td>
<td align="right">20,160</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">791,800</td>
<td align="right">798,840</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,709,660</td>
<td align="right">5,755,820</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,672,080</td>
<td align="right">2,692,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">9,006,480</td>
<td align="right">9,063,440</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">1,689,200</td>
<td align="right">1,698,440</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,689,200</td>
<td align="right">1,698,440</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">647,800</td>
<td align="right">651,240</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,765,380</td>
<td align="right">6,801,120</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,784,840</td>
<td align="right">3,801,940</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,030,020</td>
<td align="right">1,033,980</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">3,719,920</td>
<td align="right">3,709,700</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,228,940</td>
<td align="right">1,226,360</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,727,940</td>
<td align="right">5,738,300</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,268,000</td>
<td align="right">4,273,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">905,500</td>
<td align="right">904,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">93,740</td>
<td align="right">93,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,641,660</td>
<td align="right">3,645,200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">388,840</td>
<td align="right">389,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,152,220</td>
<td align="right">1,151,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">4,513,280</td>
<td align="right">4,515,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,003,820</td>
<td align="right">2,004,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,015,380</td>
<td align="right">1,015,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">366,240</td>
<td align="right">366,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">875,120</td>
<td align="right">875,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">549,480</td>
<td align="right">549,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,233,400</td>
<td align="right">2,233,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">971,220</td>
<td align="right">971,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">458,520</td>
<td align="right">458,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">440,480</td>
<td align="right">440,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">440,480</td>
<td align="right">440,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">415,880</td>
<td align="right">415,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">379,560</td>
<td align="right">379,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">291,080</td>
<td align="right">291,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">190,340</td>
<td align="right">190,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">140,540</td>
<td align="right">140,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">109,700</td>
<td align="right">109,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">89,160</td>
<td align="right">89,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">80,740</td>
<td align="right">80,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">22,320</td>
<td align="right">22,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">21,460</td>
<td align="right">21,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,920</td>
<td align="right">6,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,340</td>
<td align="right">2,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">3,264,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">974,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">320,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">64,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">64,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">64,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">1,760</td>
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
<td align="right">640</td>
<td align="right">880</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right"></td>
<td align="right">20</td>
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
Stats gathered on: 2024-10-21
