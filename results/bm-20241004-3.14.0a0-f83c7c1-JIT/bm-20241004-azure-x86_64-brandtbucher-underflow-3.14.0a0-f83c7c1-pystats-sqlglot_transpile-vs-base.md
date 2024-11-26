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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">558,340</td>
<td align="right">10,480</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">705,580</td>
<td align="right">28,280</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">630,660</td>
<td align="right">43,380</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">807,840</td>
<td align="right">108,780</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,432,260</td>
<td align="right">259,180</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">716,760</td>
<td align="right">134,600</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,060,320</td>
<td align="right">666,820</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,694,980</td>
<td align="right">610,160</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">592,500</td>
<td align="right">164,360</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">301,820</td>
<td align="right">94,620</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,059,380</td>
<td align="right">651,360</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,828,480</td>
<td align="right">2,045,900</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">501,760</td>
<td align="right">190,120</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,705,360</td>
<td align="right">7,324,660</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,471,080</td>
<td align="right">1,090,300</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,044,060</td>
<td align="right">934,900</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">7,320</td>
<td align="right">3,480</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">4,554,280</td>
<td align="right">2,224,160</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,470,440</td>
<td align="right">7,562,860</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,430,320</td>
<td align="right">712,540</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,786,960</td>
<td align="right">924,580</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,740,480</td>
<td align="right">913,000</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">211,880</td>
<td align="right">112,960</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,541,140</td>
<td align="right">8,490,360</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">954,740</td>
<td align="right">523,680</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">5,100</td>
<td align="right">2,800</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">5,100</td>
<td align="right">2,820</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">30,077,720</td>
<td align="right">16,929,360</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,800</td>
<td align="right">20,220</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">658,620</td>
<td align="right">372,060</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">82,120</td>
<td align="right">47,220</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,468,120</td>
<td align="right">7,766,940</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,063,720</td>
<td align="right">5,276,980</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">6,280</td>
<td align="right">3,660</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,100,400</td>
<td align="right">663,220</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">39,888,360</td>
<td align="right">24,437,740</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,972,100</td>
<td align="right">6,300,680</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12,985,300</td>
<td align="right">8,213,800</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,953,580</td>
<td align="right">1,258,040</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,775,220</td>
<td align="right">8,984,480</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">106,007,340</td>
<td align="right">69,791,560</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">87,040</td>
<td align="right">57,400</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,095,560</td>
<td align="right">1,397,840</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,401,640</td>
<td align="right">4,289,820</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,445,660</td>
<td align="right">5,669,960</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,714,860</td>
<td align="right">1,882,120</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,465,080</td>
<td align="right">1,728,640</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,263,800</td>
<td align="right">15,067,700</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,281,600</td>
<td align="right">14,572,220</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,705,500</td>
<td align="right">1,945,900</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,584,780</td>
<td align="right">6,267,040</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,751,500</td>
<td align="right">6,462,300</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20,592,200</td>
<td align="right">15,735,400</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">166,800</td>
<td align="right">127,880</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,146,540</td>
<td align="right">1,695,280</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,447,800</td>
<td align="right">1,938,540</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">30,764,880</td>
<td align="right">24,942,980</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">559,640</td>
<td align="right">453,980</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,956,940</td>
<td align="right">1,597,660</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,378,940</td>
<td align="right">1,949,860</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,973,600</td>
<td align="right">4,943,280</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">62,700</td>
<td align="right">54,160</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,649,960</td>
<td align="right">1,446,680</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">626,240</td>
<td align="right">549,380</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">631,200</td>
<td align="right">555,180</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">397,580</td>
<td align="right">362,160</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,714,380</td>
<td align="right">2,473,740</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">30,720</td>
<td align="right">28,120</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">854,160</td>
<td align="right">794,880</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">999,780</td>
<td align="right">931,020</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">3,181,700</td>
<td align="right">3,025,120</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">327,540</td>
<td align="right">311,960</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">686,420</td>
<td align="right">653,820</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">245,960</td>
<td align="right">235,400</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">275,360</td>
<td align="right">264,700</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,775,260</td>
<td align="right">11,531,320</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">62,900</td>
<td align="right">61,620</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,059,900</td>
<td align="right">3,006,920</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">156,540</td>
<td align="right">154,280</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">4,180,060</td>
<td align="right">4,134,240</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">753,840</td>
<td align="right">748,400</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">15,360</td>
<td align="right">15,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,143,580</td>
<td align="right">1,141,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,246,780</td>
<td align="right">6,246,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,502,680</td>
<td align="right">3,502,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,516,720</td>
<td align="right">1,516,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,189,200</td>
<td align="right">1,189,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">957,080</td>
<td align="right">957,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">706,540</td>
<td align="right">706,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">578,720</td>
<td align="right">578,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">250,880</td>
<td align="right">250,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">240,640</td>
<td align="right">240,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">201,420</td>
<td align="right">201,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">148,480</td>
<td align="right">148,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">81,900</td>
<td align="right">81,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">61,400</td>
<td align="right">61,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">57,000</td>
<td align="right">57,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">56,320</td>
<td align="right">56,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">56,320</td>
<td align="right">56,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">56,320</td>
<td align="right">56,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">40,960</td>
<td align="right">40,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">40,960</td>
<td align="right">40,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">29,880</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">25,680</td>
<td align="right">25,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,020</td>
<td align="right">20,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,560</td>
<td align="right">17,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">16,800</td>
<td align="right">16,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">15,940</td>
<td align="right">15,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">15,440</td>
<td align="right">15,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">15,360</td>
<td align="right">15,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">14,200</td>
<td align="right">14,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">10,240</td>
<td align="right">10,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">10,220</td>
<td align="right">10,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,040</td>
<td align="right">9,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,860</td>
<td align="right">7,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">6,300</td>
<td align="right">6,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">5,120</td>
<td align="right">5,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">5,120</td>
<td align="right">5,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,120</td>
<td align="right">5,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">5,120</td>
<td align="right">5,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,520</td>
<td align="right">3,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2,760</td>
<td align="right">2,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,140</td>
<td align="right">2,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,720</td>
<td align="right">1,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
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
<td align="right">25,922,120</td>
<td align="right">100.0%</td>
<td align="right">25,922,120</td>
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
<td align="right">15,360</td>
<td align="right">100.0%</td>
<td align="right">15,400</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">5,780</td>
<td align="right">0.0%</td>
<td align="right">3,180</td>
<td align="right">0.0%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,392,280</td>
<td align="right">99.9%</td>
<td align="right">17,392,280</td>
<td align="right">99.9%</td>
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
<td align="right">15,640</td>
<td align="right">0.1%</td>
<td align="right">15,640</td>
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
<td align="left">Failure</td>
<td align="right">140</td>
<td align="right">17.9%</td>
<td align="right">120</td>
<td align="right">15.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">640</td>
<td align="right">82.1%</td>
<td align="right">640</td>
<td align="right">84.2%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">-14.3%</td>
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
<td align="right">1,594,520</td>
<td align="right">2.7%</td>
<td align="right">1,571,840</td>
<td align="right">2.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,639,920</td>
<td align="right">97.2%</td>
<td align="right">56,692,340</td>
<td align="right">97.3%</td>
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
<td align="right">8,780</td>
<td align="right">0.0%</td>
<td align="right">8,780</td>
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
<td align="right">39,680</td>
<td align="right">100.0%</td>
<td align="right">39,260</td>
<td align="right">100.0%</td>
<td align="right">-1.1%</td>
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
<td align="right">860</td>
<td align="right">50.0%</td>
<td align="right">860</td>
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
<td align="right">6,397,920</td>
<td align="right">25.6%</td>
<td align="right">4,286,700</td>
<td align="right">18.7%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,631,180</td>
<td align="right">74.4%</td>
<td align="right">18,631,180</td>
<td align="right">81.3%</td>
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
<td align="right">3,220</td>
<td align="right">86.6%</td>
<td align="right">2,620</td>
<td align="right">84.0%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">13.4%</td>
<td align="right">500</td>
<td align="right">16.0%</td>
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
<td align="left">baseobject</td>
<td align="right">3,060</td>
<td align="right">95.0%</td>
<td align="right">2,460</td>
<td align="right">93.9%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">160</td>
<td align="right">5.0%</td>
<td align="right">160</td>
<td align="right">6.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">813,800</td>
<td align="right">8.4%</td>
<td align="right">324,360</td>
<td align="right">3.4%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,780</td>
<td align="right">0.1%</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,867,800</td>
<td align="right">91.5%</td>
<td align="right">9,348,020</td>
<td align="right">96.6%</td>
<td align="right">5.4%</td>
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
<td align="right">15,640</td>
<td align="right">98.5%</td>
<td align="right">6,420</td>
<td align="right">97.0%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">3.0%</td>
<td align="right">-16.7%</td>
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
<td align="right">140</td>
<td align="right">58.3%</td>
<td align="right">100</td>
<td align="right">50.0%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100</td>
<td align="right">41.7%</td>
<td align="right">100</td>
<td align="right">50.0%</td>
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
<td align="right">2,093,200</td>
<td align="right">81.6%</td>
<td align="right">1,395,720</td>
<td align="right">76.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">470,920</td>
<td align="right">18.3%</td>
<td align="right">432,000</td>
<td align="right">23.6%</td>
<td align="right">-8.3%</td>
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
<td align="right">1,920</td>
<td align="right">81.4%</td>
<td align="right">1,680</td>
<td align="right">79.2%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">440</td>
<td align="right">18.6%</td>
<td align="right">440</td>
<td align="right">20.8%</td>
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
<td align="right">360</td>
<td align="right">18.8%</td>
<td align="right">140</td>
<td align="right">8.3%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">280</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">15.5%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">840</td>
<td align="right">43.8%</td>
<td align="right">840</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">440</td>
<td align="right">22.9%</td>
<td align="right">440</td>
<td align="right">26.2%</td>
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
<td align="right">8,411,720</td>
<td align="right">3.8%</td>
<td align="right">5,637,020</td>
<td align="right">2.6%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">212,668,160</td>
<td align="right">95.1%</td>
<td align="right">212,076,040</td>
<td align="right">96.3%</td>
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
<td align="right">455,740</td>
<td align="right">0.2%</td>
<td align="right">455,740</td>
<td align="right">0.2%</td>
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
<td align="right">2,565,180</td>
<td align="right">1.1%</td>
<td align="right">2,565,180</td>
<td align="right">1.2%</td>
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
<td align="right">21,260</td>
<td align="right">25.8%</td>
<td align="right">20,260</td>
<td align="right">24.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,020</td>
<td align="right">74.2%</td>
<td align="right">61,020</td>
<td align="right">75.1%</td>
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
<td align="left">class method obj</td>
<td align="right">620</td>
<td align="right">2.9%</td>
<td align="right">580</td>
<td align="right">2.9%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">17,040</td>
<td align="right">80.2%</td>
<td align="right">16,140</td>
<td align="right">79.7%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,220</td>
<td align="right">15.1%</td>
<td align="right">3,160</td>
<td align="right">15.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.7%</td>
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
<td align="right">25,546,240</td>
<td align="right">99.9%</td>
<td align="right">20,511,560</td>
<td align="right">99.9%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
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
<td align="right">4,600</td>
<td align="right">100.0%</td>
<td align="right">4,600</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">40,940</td>
<td align="right">99.9%</td>
<td align="right">40,940</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">2,137,480</td>
<td align="right">4.4%</td>
<td align="right">791,240</td>
<td align="right">1.7%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,157,600</td>
<td align="right">95.6%</td>
<td align="right">47,055,700</td>
<td align="right">98.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">900</td>
<td align="right">0.0%</td>
<td align="right">900</td>
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
<td align="right">41,560</td>
<td align="right">100.0%</td>
<td align="right">16,160</td>
<td align="right">100.0%</td>
<td align="right">-61.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">230,280</td>
<td align="right">99.9%</td>
<td align="right">169,520</td>
<td align="right">99.9%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
<td align="right">1,599,380</td>
<td align="right">3.3%</td>
<td align="right">1,156,620</td>
<td align="right">2.6%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,213,120</td>
<td align="right">96.7%</td>
<td align="right">43,586,620</td>
<td align="right">97.3%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,080</td>
<td align="right">0.1%</td>
<td align="right">25,080</td>
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
<td align="right">34,220</td>
<td align="right">98.7%</td>
<td align="right">25,920</td>
<td align="right">98.3%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">440</td>
<td align="right">1.3%</td>
<td align="right">440</td>
<td align="right">1.7%</td>
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
<td align="right">160</td>
<td align="right">36.4%</td>
<td align="right">160</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">31.8%</td>
<td align="right">140</td>
<td align="right">31.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">140</td>
<td align="right">31.8%</td>
<td align="right">140</td>
<td align="right">31.8%</td>
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
<td align="right">5,186,360</td>
<td align="right">100.0%</td>
<td align="right">4,326,600</td>
<td align="right">100.0%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">200</td>
<td align="right">100.0%</td>
<td align="right">200</td>
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
<td align="right">276,849,600</td>
<td align="right">52.8%</td>
<td align="right">173,451,300</td>
<td align="right">49.9%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">17,033,600</td>
<td align="right">3.2%</td>
<td align="right">11,441,940</td>
<td align="right">3.3%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">222,193,820</td>
<td align="right">42.3%</td>
<td align="right">156,078,620</td>
<td align="right">44.9%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">8,730,820</td>
<td align="right">1.7%</td>
<td align="right">6,429,840</td>
<td align="right">1.9%</td>
<td align="right">-26.4%</td>
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
<td align="right">6,780</td>
<td align="right">0.0%</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,780</td>
<td align="right">0.0%</td>
<td align="right">3,180</td>
<td align="right">0.0%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,093,200</td>
<td align="right">12.3%</td>
<td align="right">1,395,720</td>
<td align="right">12.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,397,920</td>
<td align="right">37.7%</td>
<td align="right">4,286,700</td>
<td align="right">37.7%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,411,720</td>
<td align="right">49.6%</td>
<td align="right">5,637,020</td>
<td align="right">49.5%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">15,360</td>
<td align="right">0.1%</td>
<td align="right">15,400</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">25,080</td>
<td align="right">0.1%</td>
<td align="right">25,080</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8,780</td>
<td align="right">0.1%</td>
<td align="right">8,780</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">900</td>
<td align="right">0.0%</td>
<td align="right">900</td>
<td align="right">0.0%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,137,480</td>
<td align="right">24.5%</td>
<td align="right">791,240</td>
<td align="right">12.3%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">406,760</td>
<td align="right">4.7%</td>
<td align="right">162,180</td>
<td align="right">2.5%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">699,200</td>
<td align="right">8.0%</td>
<td align="right">484,020</td>
<td align="right">7.5%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">482,580</td>
<td align="right">5.5%</td>
<td align="right">397,000</td>
<td align="right">6.2%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">706,040</td>
<td align="right">8.1%</td>
<td align="right">676,000</td>
<td align="right">10.5%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">874,700</td>
<td align="right">10.0%</td>
<td align="right">882,060</td>
<td align="right">13.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,340,840</td>
<td align="right">15.4%</td>
<td align="right">1,340,840</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">706,480</td>
<td align="right">8.1%</td>
<td align="right">706,480</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">486,680</td>
<td align="right">5.6%</td>
<td align="right">486,680</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">407,040</td>
<td align="right">4.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">181,080</td>
<td align="right">2.8%</td>
<td align="right"></td>
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
<td align="right">6,246,780</td>
<td align="right">14.0%</td>
<td align="right">6,246,780</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">38,502,180</td>
<td align="right">86.0%</td>
<td align="right">38,502,180</td>
<td align="right">86.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">6,246,780</td>
<td align="right">14.0%</td>
<td align="right">6,246,780</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">5,637,440</td>
<td align="right">12.6%</td>
<td align="right">5,637,440</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">609,340</td>
<td align="right">1.4%</td>
<td align="right">609,340</td>
<td align="right">1.4%</td>
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
<td align="right">5,637,440</td>
<td align="right">12.6%</td>
<td align="right">5,637,440</td>
<td align="right">12.6%</td>
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
<td align="right">563,220</td>
<td align="right">1.3%</td>
<td align="right">563,220</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">15,520</td>
<td align="right">0.0%</td>
<td align="right">15,520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,440,940</td>
<td align="right">7.7%</td>
<td align="right">3,440,940</td>
<td align="right">7.7%</td>
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
<td align="right">56,320</td>
<td align="right">0.1%</td>
<td align="right">56,320</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">43,996,320</td>
<td align="right">98.3%</td>
<td align="right">43,996,320</td>
<td align="right">98.3%</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">83,651,580</td>
<td align="right">8.3%</td>
<td align="right">53,056,920</td>
<td align="right">5.3%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">107,578</td>
<td align="right"></td>
<td align="right">72,444</td>
<td align="right"></td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">83,992,840</td>
<td align="right">8.0%</td>
<td align="right">60,644,540</td>
<td align="right">5.7%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">269,885,860</td>
<td align="right">26.8%</td>
<td align="right">198,267,600</td>
<td align="right">19.8%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">443,484,612</td>
<td align="right">44.1%</td>
<td align="right">526,717,163</td>
<td align="right">52.6%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">326,112,840</td>
<td align="right">30.9%</td>
<td align="right">273,086,200</td>
<td align="right">25.5%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">431,131,304</td>
<td align="right">40.8%</td>
<td align="right">496,645,082</td>
<td align="right">46.4%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">214,891,248</td>
<td align="right">20.3%</td>
<td align="right">239,207,506</td>
<td align="right">22.4%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,284,770</td>
<td align="right"></td>
<td align="right">1,175,904</td>
<td align="right"></td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">209,196,103</td>
<td align="right">20.8%</td>
<td align="right">223,397,453</td>
<td align="right">22.3%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,182,381</td>
<td align="right"></td>
<td align="right">1,108,838</td>
<td align="right"></td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">38,120</td>
<td align="right">0.1%</td>
<td align="right">39,360</td>
<td align="right">0.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">36,650,764</td>
<td align="right"></td>
<td align="right">37,520,869</td>
<td align="right"></td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">37,074,420</td>
<td align="right">76.9%</td>
<td align="right">37,935,860</td>
<td align="right">77.3%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">37,036,160</td>
<td align="right">76.8%</td>
<td align="right">37,896,180</td>
<td align="right">77.2%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">33,381,119</td>
<td align="right"></td>
<td align="right">32,935,722</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">14,643,682</td>
<td align="right"></td>
<td align="right">14,678,816</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,141,880</td>
<td align="right"></td>
<td align="right">11,142,480</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,142,520</td>
<td align="right">23.1%</td>
<td align="right">11,143,120</td>
<td align="right">22.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">855,040</td>
<td align="right"></td>
<td align="right">855,040</td>
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
<td align="right">820</td>
<td align="right">1,115,820</td>
<td align="right">15,697,220</td>
<td align="right">820</td>
<td align="right">1,120,740</td>
<td align="right">15,678,500</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">340</td>
<td align="right">3.6%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">4,860</td>
<td align="right">53.4%</td>
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
<td align="right">4,320</td>
<td align="right">47.5%</td>
<td align="right">2,120</td>
<td align="right">22.7%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">4,740</td>
<td align="right">52.1%</td>
<td align="right">6,880</td>
<td align="right">73.7%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">400</td>
<td align="right">4.4%</td>
<td align="right">560</td>
<td align="right">6.0%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">38,493,520</td>
<td align="right"></td>
<td align="right">52,375,520</td>
<td align="right"></td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,272,564,160</td>
<td align="right">3,305.9%</td>
<td align="right">1,604,618,940</td>
<td align="right">3,063.7%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">9,100</td>
<td align="right"></td>
<td align="right">9,340</td>
<td align="right"></td>
<td align="right">2.6%</td>
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
<td align="right">240</td>
<td align="right">2.6%</td>
<td align="right">240</td>
<td align="right">2.6%</td>
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
<td align="right">4,260</td>
<td align="right">89.9%</td>
<td align="right">6,400</td>
<td align="right">93.0%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">4,740</td>
<td align="right"></td>
<td align="right">6,880</td>
<td align="right"></td>
<td align="right">45.1%</td>
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
<td align="right">1.3%</td>
<td align="right">60</td>
<td align="right">0.9%</td>
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
<td align="right">880</td>
<td align="right">18.6%</td>
<td align="right">1,060</td>
<td align="right">15.4%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">820</td>
<td align="right">17.3%</td>
<td align="right">1,320</td>
<td align="right">19.2%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">1,140</td>
<td align="right">16.6%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">920</td>
<td align="right">19.4%</td>
<td align="right">1,280</td>
<td align="right">18.6%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">780</td>
<td align="right">16.5%</td>
<td align="right">1,080</td>
<td align="right">15.7%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">480</td>
<td align="right">10.1%</td>
<td align="right">940</td>
<td align="right">13.7%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">1.3%</td>
<td align="right">60</td>
<td align="right">0.9%</td>
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
<td align="right">500</td>
<td align="right">10.5%</td>
<td align="right">240</td>
<td align="right">3.5%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">760</td>
<td align="right">16.0%</td>
<td align="right">1,440</td>
<td align="right">20.9%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">880</td>
<td align="right">18.6%</td>
<td align="right">1,160</td>
<td align="right">16.9%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">1,380</td>
<td align="right">20.1%</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">700</td>
<td align="right">14.8%</td>
<td align="right">1,100</td>
<td align="right">16.0%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">420</td>
<td align="right">8.9%</td>
<td align="right">640</td>
<td align="right">9.3%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">200</td>
<td align="right">4.2%</td>
<td align="right">440</td>
<td align="right">6.4%</td>
<td align="right">120.0%</td>
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
<td align="left">_DEOPT</td>
<td align="right">4,880</td>
<td align="right">283,420</td>
<td align="right">5,707.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">3,560</td>
<td align="right">109,220</td>
<td align="right">2,968.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">31,640</td>
<td align="right">708,940</td>
<td align="right">2,140.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">31,640</td>
<td align="right">708,940</td>
<td align="right">2,140.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">137,120</td>
<td align="right">1,542,620</td>
<td align="right">1,025.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">80,020</td>
<td align="right">839,620</td>
<td align="right">949.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,462,460</td>
<td align="right">11,959,720</td>
<td align="right">717.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">13,040</td>
<td align="right">89,900</td>
<td align="right">589.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">13,040</td>
<td align="right">89,900</td>
<td align="right">589.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">169,800</td>
<td align="right">882,700</td>
<td align="right">419.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,132,620</td>
<td align="right">5,339,940</td>
<td align="right">371.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">951,040</td>
<td align="right">4,260,260</td>
<td align="right">348.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">555,020</td>
<td align="right">2,104,420</td>
<td align="right">279.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">21,360</td>
<td align="right">80,640</td>
<td align="right">277.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">230,100</td>
<td align="right">777,960</td>
<td align="right">238.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">853,720</td>
<td align="right">2,842,240</td>
<td align="right">232.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">18,400</td>
<td align="right">56,560</td>
<td align="right">207.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">969,400</td>
<td align="right">2,928,800</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">456,260</td>
<td align="right">1,311,580</td>
<td align="right">187.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">745,400</td>
<td align="right">2,134,180</td>
<td align="right">186.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,861,220</td>
<td align="right">7,786,360</td>
<td align="right">172.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">8,138,260</td>
<td align="right">21,954,740</td>
<td align="right">169.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">8,244,280</td>
<td align="right">21,861,240</td>
<td align="right">165.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">358,280</td>
<td align="right">940,440</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">224,080</td>
<td align="right">583,360</td>
<td align="right">160.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">22,260</td>
<td align="right">57,680</td>
<td align="right">159.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">801,300</td>
<td align="right">1,929,240</td>
<td align="right">140.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">890,100</td>
<td align="right">2,130,940</td>
<td align="right">139.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">54,880</td>
<td align="right">130,900</td>
<td align="right">138.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">315,900</td>
<td align="right">694,960</td>
<td align="right">120.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,315,440</td>
<td align="right">4,779,520</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">682,960</td>
<td align="right">1,378,920</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">722,920</td>
<td align="right">1,421,980</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,597,620</td>
<td align="right">2,966,080</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,982,140</td>
<td align="right">7,243,560</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,430,500</td>
<td align="right">4,359,480</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,555,580</td>
<td align="right">4,414,540</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">6,606,860</td>
<td align="right">11,341,640</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,523,880</td>
<td align="right">5,924,920</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">373,220</td>
<td align="right">613,860</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,989,220</td>
<td align="right">3,270,560</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">155,540</td>
<td align="right">254,860</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,216,280</td>
<td align="right">1,952,720</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,872,460</td>
<td align="right">2,981,620</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">788,820</td>
<td align="right">1,211,560</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">5,021,160</td>
<td align="right">7,688,740</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">11,100,720</td>
<td align="right">16,935,460</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">11,547,780</td>
<td align="right">17,471,120</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,454,060</td>
<td align="right">18,719,860</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">12,006,320</td>
<td align="right">17,997,400</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,572,680</td>
<td align="right">18,838,480</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">202,220</td>
<td align="right">301,540</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,342,180</td>
<td align="right">9,441,880</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">107,220</td>
<td align="right">158,000</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,108,880</td>
<td align="right">1,596,860</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,184,040</td>
<td align="right">13,140,040</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">7,486,420</td>
<td align="right">10,667,620</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">19,687,560</td>
<td align="right">27,655,120</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">5,317,140</td>
<td align="right">7,428,360</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">38,493,520</td>
<td align="right">52,375,520</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,560</td>
<td align="right">4,840</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">3,560</td>
<td align="right">4,840</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">5,456,160</td>
<td align="right">7,414,160</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,180,660</td>
<td align="right">19,048,740</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,792,060</td>
<td align="right">5,065,980</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">41,915,660</td>
<td align="right">55,797,660</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">29,410,600</td>
<td align="right">39,027,640</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,343,840</td>
<td align="right">1,774,900</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,785,100</td>
<td align="right">2,341,500</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">107,120</td>
<td align="right">139,720</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,763,760</td>
<td align="right">8,765,700</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,122,100</td>
<td align="right">10,452,220</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">75,769,700</td>
<td align="right">97,130,660</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,800,140</td>
<td align="right">27,589,740</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">15,888,060</td>
<td align="right">19,897,120</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,179,460</td>
<td align="right">1,466,020</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">66,667,040</td>
<td align="right">81,833,560</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">32,255,140</td>
<td align="right">39,332,120</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">50,860</td>
<td align="right">61,420</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,439,460</td>
<td align="right">6,426,240</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">269,080</td>
<td align="right">314,900</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">34,460</td>
<td align="right">39,900</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">160,042,300</td>
<td align="right">183,456,420</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">105,836,560</td>
<td align="right">121,287,180</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,318,500</td>
<td align="right">16,403,320</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">151,638,740</td>
<td align="right">173,245,560</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">10,187,080</td>
<td align="right">11,631,360</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,279,600</td>
<td align="right">1,457,520</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,391,080</td>
<td align="right">7,088,560</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,832,200</td>
<td align="right">7,527,740</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">8,235,960</td>
<td align="right">9,068,700</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">13,866,680</td>
<td align="right">15,247,460</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">39,600</td>
<td align="right">43,400</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">26,152,600</td>
<td align="right">28,482,460</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">37,026,180</td>
<td align="right">40,118,180</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">11,337,600</td>
<td align="right">12,265,200</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">508,740</td>
<td align="right">547,660</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">508,740</td>
<td align="right">547,660</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">13,768,160</td>
<td align="right">14,818,580</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">737,300</td>
<td align="right">788,640</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,083,300</td>
<td align="right">1,136,280</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,352,440</td>
<td align="right">9,803,700</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">39,710,300</td>
<td align="right">41,579,900</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">13,515,840</td>
<td align="right">14,103,120</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,740,040</td>
<td align="right">3,896,620</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">298,960</td>
<td align="right">309,780</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">13,795,140</td>
<td align="right">14,224,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,218,640</td>
<td align="right">14,655,820</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,001,320</td>
<td align="right">2,054,300</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,001,320</td>
<td align="right">2,054,300</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">34,047,980</td>
<td align="right">34,602,060</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">687,280</td>
<td align="right">697,940</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,094,100</td>
<td align="right">2,109,500</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,555,000</td>
<td align="right">1,563,540</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">2,628,980</td>
<td align="right">2,616,260</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">458,860</td>
<td align="right">460,860</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">696,020</td>
<td align="right">698,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,302,580</td>
<td align="right">3,305,200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,776,640</td>
<td align="right">1,776,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,468,560</td>
<td align="right">4,468,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,422,140</td>
<td align="right">3,422,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">918,020</td>
<td align="right">918,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">725,240</td>
<td align="right">725,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">725,240</td>
<td align="right">725,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">526,140</td>
<td align="right">526,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">218,960</td>
<td align="right">218,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">215,400</td>
<td align="right">215,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">85,540</td>
<td align="right">85,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">61,180</td>
<td align="right">61,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">33,080</td>
<td align="right">33,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,820</td>
<td align="right">4,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,820</td>
<td align="right">4,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,820</td>
<td align="right">3,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">859,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">548,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">311,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">60,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">29,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">17,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">17,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">17,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">15,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">15,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">15,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">14,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">7,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">2,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right"></td>
<td align="right">2,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right">2,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">2,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">2,280</td>
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
<td align="right">100</td>
<td align="right">440</td>
<td align="right">340.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">400</td>
<td align="right">540</td>
<td align="right">35.0%</td>
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
