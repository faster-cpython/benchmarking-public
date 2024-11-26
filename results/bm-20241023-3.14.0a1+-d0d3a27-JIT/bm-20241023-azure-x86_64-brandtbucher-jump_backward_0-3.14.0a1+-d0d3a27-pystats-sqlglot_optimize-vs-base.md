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
<td align="left">JUMP_BACKWARD</td>
<td align="right">43,260</td>
<td align="right">243,920</td>
<td align="right">463.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">13,620</td>
<td align="right">41,520</td>
<td align="right">204.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">263,020</td>
<td align="right">794,460</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,091,800</td>
<td align="right">3,095,940</td>
<td align="right">183.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,155,460</td>
<td align="right">24,199,920</td>
<td align="right">116.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,469,800</td>
<td align="right">2,961,300</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">705,740</td>
<td align="right">960</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">55,320</td>
<td align="right">110,340</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">85,220</td>
<td align="right">560</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,483,380</td>
<td align="right">53,700</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">62,680</td>
<td align="right">1,140</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">62,680</td>
<td align="right">1,140</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,312,840</td>
<td align="right">46,260</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,274,880</td>
<td align="right">27,620</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">840</td>
<td align="right">20</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,217,020</td>
<td align="right">137,940</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,723,180</td>
<td align="right">101,100</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">681,920</td>
<td align="right">95,940</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">834,460</td>
<td align="right">119,700</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">124,920</td>
<td align="right">18,840</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">94,340</td>
<td align="right">171,840</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">918,660</td>
<td align="right">168,340</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">181,340</td>
<td align="right">34,900</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">62,700</td>
<td align="right">12,300</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,524,480</td>
<td align="right">313,620</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">23,360</td>
<td align="right">5,360</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,497,260</td>
<td align="right">579,600</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">56,160</td>
<td align="right">13,560</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">76,020</td>
<td align="right">20,040</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">146,640</td>
<td align="right">41,360</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">119,940</td>
<td align="right">34,920</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,539,200</td>
<td align="right">5,656,400</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">7,980</td>
<td align="right">2,700</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">23,557,740</td>
<td align="right">8,059,300</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">123,800</td>
<td align="right">42,500</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">904,740</td>
<td align="right">328,720</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">4,447,760</td>
<td align="right">2,046,760</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,696,060</td>
<td align="right">5,673,880</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">566,260</td>
<td align="right">264,920</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,182,700</td>
<td align="right">1,080,340</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,857,280</td>
<td align="right">7,371,740</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,047,400</td>
<td align="right">1,093,100</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,274,100</td>
<td align="right">1,860,360</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">134,340</td>
<td align="right">73,140</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,134,940</td>
<td align="right">6,665,780</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">600,400</td>
<td align="right">345,900</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,433,600</td>
<td align="right">3,143,740</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">53,242,120</td>
<td align="right">32,088,860</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,924,000</td>
<td align="right">1,775,480</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">834,680</td>
<td align="right">518,780</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,600,320</td>
<td align="right">4,114,560</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">33,020</td>
<td align="right">44,720</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,826,440</td>
<td align="right">1,830,200</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,357,040</td>
<td align="right">2,826,420</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">15,062,980</td>
<td align="right">9,820,000</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">98,540</td>
<td align="right">132,180</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,057,080</td>
<td align="right">8,684,780</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">65,460</td>
<td align="right">44,020</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">437,780</td>
<td align="right">296,620</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,092,360</td>
<td align="right">2,097,200</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">25,920</td>
<td align="right">18,300</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,280</td>
<td align="right">1,620</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">34,340</td>
<td align="right">44,240</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,538,940</td>
<td align="right">5,836,940</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">434,600</td>
<td align="right">313,260</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">165,560</td>
<td align="right">119,620</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">182,820</td>
<td align="right">231,900</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,917,780</td>
<td align="right">21,305,260</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">98,140</td>
<td align="right">72,920</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,252,000</td>
<td align="right">7,636,300</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,452,540</td>
<td align="right">1,815,740</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,247,120</td>
<td align="right">14,035,840</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">288,120</td>
<td align="right">359,440</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,097,420</td>
<td align="right">5,351,500</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">200,980</td>
<td align="right">161,360</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,300</td>
<td align="right">77,540</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">313,640</td>
<td align="right">259,220</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">380,080</td>
<td align="right">319,880</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">371,120</td>
<td align="right">314,380</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">592,760</td>
<td align="right">520,840</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">61,480</td>
<td align="right">55,080</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">7,069,760</td>
<td align="right">6,386,540</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">17,760</td>
<td align="right">19,420</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,205,160</td>
<td align="right">1,094,440</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,513,380</td>
<td align="right">2,294,960</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">114,680</td>
<td align="right">106,140</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">590,040</td>
<td align="right">629,780</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">307,740</td>
<td align="right">320,640</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,836,640</td>
<td align="right">3,991,980</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">29,400</td>
<td align="right">28,240</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,916,900</td>
<td align="right">5,685,460</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">65,800</td>
<td align="right">63,820</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">211,000</td>
<td align="right">205,540</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,815,180</td>
<td align="right">10,053,380</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">588,520</td>
<td align="right">577,720</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">116,000</td>
<td align="right">114,080</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">805,580</td>
<td align="right">817,280</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,146,240</td>
<td align="right">1,130,040</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">782,260</td>
<td align="right">793,200</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">2,283,160</td>
<td align="right">2,313,300</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">68,800</td>
<td align="right">69,660</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">349,060</td>
<td align="right">344,900</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">147,480</td>
<td align="right">145,800</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,009,780</td>
<td align="right">1,001,780</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,817,980</td>
<td align="right">7,801,180</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,520</td>
<td align="right">56,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">7,521,960</td>
<td align="right">7,521,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,453,800</td>
<td align="right">1,453,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">772,560</td>
<td align="right">772,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">772,560</td>
<td align="right">772,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,520</td>
<td align="right">218,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">210,000</td>
<td align="right">210,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">55,200</td>
<td align="right">55,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">36,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">19,080</td>
<td align="right">19,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">13,460</td>
<td align="right">13,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,220</td>
<td align="right">11,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">8,040</td>
<td align="right">8,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
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
<td align="right">13,220</td>
<td align="right">2.0%</td>
<td align="right">13,220</td>
<td align="right">2.0%</td>
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
<td align="right">651,300</td>
<td align="right">98.0%</td>
<td align="right">651,300</td>
<td align="right">98.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">100.0%</td>
<td align="right">240</td>
<td align="right">100.0%</td>
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
<td align="right">220</td>
<td align="right">91.7%</td>
<td align="right">220</td>
<td align="right">91.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">20</td>
<td align="right">8.3%</td>
<td align="right">20</td>
<td align="right">8.3%</td>
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
<td align="right">36,760</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">17,540</td>
<td align="right">0.9%</td>
<td align="right">19,200</td>
<td align="right">1.0%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,839,300</td>
<td align="right">98.8%</td>
<td align="right">1,839,300</td>
<td align="right">98.7%</td>
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
<td align="right">4,760</td>
<td align="right">0.3%</td>
<td align="right">4,760</td>
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
<td align="right">100</td>
<td align="right">33.3%</td>
<td align="right">100</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">66.7%</td>
<td align="right">200</td>
<td align="right">66.7%</td>
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
<td align="right">120</td>
<td align="right">60.0%</td>
<td align="right">140</td>
<td align="right">70.0%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">30.0%</td>
<td align="right">60</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">10.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">301,760</td>
<td align="right">0.5%</td>
<td align="right">177,020</td>
<td align="right">0.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,343,180</td>
<td align="right">99.5%</td>
<td align="right">65,486,260</td>
<td align="right">99.7%</td>
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
<td align="left">Success</td>
<td align="right">5,900</td>
<td align="right">100.0%</td>
<td align="right">3,560</td>
<td align="right">100.0%</td>
<td align="right">-39.7%</td>
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
<td align="right">591,620</td>
<td align="right">42.3%</td>
<td align="right">519,880</td>
<td align="right">39.2%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">806,640</td>
<td align="right">57.6%</td>
<td align="right">806,640</td>
<td align="right">60.8%</td>
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
<td align="right">1,140</td>
<td align="right">100.0%</td>
<td align="right">960</td>
<td align="right">100.0%</td>
<td align="right">-15.8%</td>
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
<td align="left">different types</td>
<td align="right">420</td>
<td align="right">36.8%</td>
<td align="right">300</td>
<td align="right">31.2%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">540</td>
<td align="right">47.4%</td>
<td align="right">480</td>
<td align="right">50.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">5.3%</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">3.5%</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.5%</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">3.5%</td>
<td align="right">40</td>
<td align="right">4.2%</td>
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
<td align="right">25,440</td>
<td align="right">4.9%</td>
<td align="right">6,360</td>
<td align="right">1.3%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">93,960</td>
<td align="right">18.2%</td>
<td align="right">77,280</td>
<td align="right">15.5%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">396,000</td>
<td align="right">76.8%</td>
<td align="right">414,720</td>
<td align="right">83.2%</td>
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
<td align="left">Success</td>
<td align="right">480</td>
<td align="right">58.5%</td>
<td align="right">120</td>
<td align="right">31.6%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">340</td>
<td align="right">41.5%</td>
<td align="right">260</td>
<td align="right">68.4%</td>
<td align="right">-23.5%</td>
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
<td align="right">41.2%</td>
<td align="right">80</td>
<td align="right">30.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">200</td>
<td align="right">58.8%</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">-10.0%</td>
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
<td align="right">3,097,260</td>
<td align="right">51.4%</td>
<td align="right">5,092,860</td>
<td align="right">74.1%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,922,540</td>
<td align="right">48.5%</td>
<td align="right">1,774,480</td>
<td align="right">25.8%</td>
<td align="right">-39.3%</td>
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
<td align="right">1,460</td>
<td align="right">100.0%</td>
<td align="right">1,000</td>
<td align="right">100.0%</td>
<td align="right">-31.5%</td>
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
<td align="left">enumerate</td>
<td align="right">60</td>
<td align="right">4.1%</td>
<td align="right">20</td>
<td align="right">2.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">900</td>
<td align="right">61.6%</td>
<td align="right">580</td>
<td align="right">58.0%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">100</td>
<td align="right">6.8%</td>
<td align="right">80</td>
<td align="right">8.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">100</td>
<td align="right">6.8%</td>
<td align="right">80</td>
<td align="right">8.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">160</td>
<td align="right">11.0%</td>
<td align="right">140</td>
<td align="right">14.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">60</td>
<td align="right">4.1%</td>
<td align="right">60</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">3,262,800</td>
<td align="right">7.8%</td>
<td align="right">1,999,040</td>
<td align="right">5.1%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">366,740</td>
<td align="right">0.9%</td>
<td align="right">311,200</td>
<td align="right">0.8%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,320</td>
<td align="right">0.0%</td>
<td align="right">4,620</td>
<td align="right">0.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,422,540</td>
<td align="right">91.4%</td>
<td align="right">36,525,100</td>
<td align="right">94.0%</td>
<td align="right">-4.9%</td>
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
<td align="right">61,560</td>
<td align="right">93.6%</td>
<td align="right">37,840</td>
<td align="right">92.7%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,200</td>
<td align="right">6.4%</td>
<td align="right">3,000</td>
<td align="right">7.3%</td>
<td align="right">-28.6%</td>
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
<td align="right">80</td>
<td align="right">1.9%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">640</td>
<td align="right">15.2%</td>
<td align="right">360</td>
<td align="right">12.0%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,420</td>
<td align="right">81.4%</td>
<td align="right">2,600</td>
<td align="right">86.7%</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">38,398,960</td>
<td align="right">100.0%</td>
<td align="right">16,744,080</td>
<td align="right">100.0%</td>
<td align="right">-56.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,608,760</td>
<td align="right">100.0%</td>
<td align="right">3,608,760</td>
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
<td align="right">694,000</td>
<td align="right">26.8%</td>
<td align="right">1,390,960</td>
<td align="right">42.9%</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,898,300</td>
<td align="right">73.2%</td>
<td align="right">1,848,160</td>
<td align="right">57.1%</td>
<td align="right">-2.6%</td>
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
<td align="right">13,260</td>
<td align="right">100.0%</td>
<td align="right">26,420</td>
<td align="right">100.0%</td>
<td align="right">99.2%</td>
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
<td align="right">1,169,400</td>
<td align="right">100.0%</td>
<td align="right">1,169,400</td>
<td align="right">100.0%</td>
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
<td align="right">60,820</td>
<td align="right">0.2%</td>
<td align="right">54,700</td>
<td align="right">0.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">769,780</td>
<td align="right">2.1%</td>
<td align="right">779,820</td>
<td align="right">2.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,229,280</td>
<td align="right">97.8%</td>
<td align="right">35,963,180</td>
<td align="right">97.7%</td>
<td align="right">-0.7%</td>
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
<td align="right">660</td>
<td align="right">4.4%</td>
<td align="right">380</td>
<td align="right">2.5%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,400</td>
<td align="right">95.6%</td>
<td align="right">14,560</td>
<td align="right">97.5%</td>
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
<td align="left">dict</td>
<td align="right">320</td>
<td align="right">48.5%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">9.1%</td>
<td align="right">20</td>
<td align="right">5.3%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">160</td>
<td align="right">24.2%</td>
<td align="right">160</td>
<td align="right">42.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">100</td>
<td align="right">15.2%</td>
<td align="right">100</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">20</td>
<td align="right">3.0%</td>
<td align="right">20</td>
<td align="right">5.3%</td>
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
<td align="right">11,160</td>
<td align="right">0.1%</td>
<td align="right">11,160</td>
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
<td align="right">11,735,100</td>
<td align="right">99.9%</td>
<td align="right">11,735,100</td>
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
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
<td align="right">136,820,040</td>
<td align="right">40.1%</td>
<td align="right">78,769,160</td>
<td align="right">30.6%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">4,123,160</td>
<td align="right">1.2%</td>
<td align="right">2,787,720</td>
<td align="right">1.1%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,058,820</td>
<td align="right">1.5%</td>
<td align="right">4,358,480</td>
<td align="right">1.7%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">195,534,060</td>
<td align="right">57.3%</td>
<td align="right">171,790,800</td>
<td align="right">66.7%</td>
<td align="right">-12.1%</td>
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
<td align="right">36,760</td>
<td align="right">0.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,922,540</td>
<td align="right">71.0%</td>
<td align="right">1,774,480</td>
<td align="right">63.8%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,960</td>
<td align="right">2.3%</td>
<td align="right">77,280</td>
<td align="right">2.8%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">366,740</td>
<td align="right">8.9%</td>
<td align="right">311,200</td>
<td align="right">11.2%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">591,620</td>
<td align="right">14.4%</td>
<td align="right">519,880</td>
<td align="right">18.7%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60,820</td>
<td align="right">1.5%</td>
<td align="right">54,700</td>
<td align="right">2.0%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">17,540</td>
<td align="right">0.4%</td>
<td align="right">19,200</td>
<td align="right">0.7%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">13,220</td>
<td align="right">0.3%</td>
<td align="right">13,220</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,160</td>
<td align="right">0.3%</td>
<td align="right">11,160</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">694,000</td>
<td align="right">13.7%</td>
<td align="right">1,390,960</td>
<td align="right">31.9%</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">816,440</td>
<td align="right">16.1%</td>
<td align="right">34,280</td>
<td align="right">0.8%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">445,640</td>
<td align="right">8.8%</td>
<td align="right">801,020</td>
<td align="right">18.4%</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">233,400</td>
<td align="right">4.6%</td>
<td align="right">104,760</td>
<td align="right">2.4%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">35,660</td>
<td align="right">0.7%</td>
<td align="right">18,540</td>
<td align="right">0.4%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,951,980</td>
<td align="right">38.6%</td>
<td align="right">1,145,060</td>
<td align="right">26.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">59,440</td>
<td align="right">1.2%</td>
<td align="right">63,340</td>
<td align="right">1.5%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">168,420</td>
<td align="right">3.3%</td>
<td align="right">177,360</td>
<td align="right">4.1%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">585,880</td>
<td align="right">11.6%</td>
<td align="right">587,200</td>
<td align="right">13.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,960</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">11,960</td>
<td align="right">0.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,399,980</td>
<td align="right">6.6%</td>
<td align="right">2,383,180</td>
<td align="right">6.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,383,800</td>
<td align="right">9.4%</td>
<td align="right">3,367,000</td>
<td align="right">9.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,383,800</td>
<td align="right">9.4%</td>
<td align="right">3,367,000</td>
<td align="right">9.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,818,040</td>
<td align="right">21.6%</td>
<td align="right">7,801,240</td>
<td align="right">21.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,818,040</td>
<td align="right">21.6%</td>
<td align="right">7,801,240</td>
<td align="right">21.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">28,298,660</td>
<td align="right">78.4%</td>
<td align="right">28,315,460</td>
<td align="right">78.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">4,434,240</td>
<td align="right">12.3%</td>
<td align="right">4,434,240</td>
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
<td align="right">801,360</td>
<td align="right">2.2%</td>
<td align="right">801,360</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">62,940</td>
<td align="right">0.2%</td>
<td align="right">62,940</td>
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
<td align="right">57,360</td>
<td align="right">0.2%</td>
<td align="right">57,360</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">26,183,940</td>
<td align="right">72.5%</td>
<td align="right">26,183,940</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">70,420</td>
<td align="right">0.1%</td>
<td align="right">94,940</td>
<td align="right">0.1%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">41,707,940</td>
<td align="right">6.3%</td>
<td align="right">30,644,320</td>
<td align="right">4.4%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">328,696,540</td>
<td align="right">49.3%</td>
<td align="right">406,851,189</td>
<td align="right">58.0%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">154,282,600</td>
<td align="right">23.1%</td>
<td align="right">120,390,840</td>
<td align="right">17.2%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">339,523,190</td>
<td align="right">46.2%</td>
<td align="right">397,299,242</td>
<td align="right">50.2%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,774,977</td>
<td align="right"></td>
<td align="right">6,776,035</td>
<td align="right"></td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,605,160</td>
<td align="right">4.8%</td>
<td align="right">31,837,460</td>
<td align="right">4.0%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">151,499,036</td>
<td align="right">20.6%</td>
<td align="right">167,350,560</td>
<td align="right">21.1%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">208,629,560</td>
<td align="right">28.4%</td>
<td align="right">195,114,180</td>
<td align="right">24.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">491,423</td>
<td align="right"></td>
<td align="right">468,725</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">510,453</td>
<td align="right"></td>
<td align="right">487,290</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">19,179</td>
<td align="right"></td>
<td align="right">18,716</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">141,952,025</td>
<td align="right">21.3%</td>
<td align="right">143,872,973</td>
<td align="right">20.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">47,061,921</td>
<td align="right"></td>
<td align="right">46,987,324</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,411,640</td>
<td align="right">63.2%</td>
<td align="right">45,447,180</td>
<td align="right">63.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">46,291,476</td>
<td align="right"></td>
<td align="right">46,303,915</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,340,880</td>
<td align="right">63.1%</td>
<td align="right">45,351,820</td>
<td align="right">63.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,417,040</td>
<td align="right">36.8%</td>
<td align="right">26,417,400</td>
<td align="right">36.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,454,480</td>
<td align="right"></td>
<td align="right">26,454,840</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">113,880</td>
<td align="right"></td>
<td align="right">113,880</td>
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
<td align="right">140</td>
<td align="right">136,360</td>
<td align="right">1,447,320</td>
<td align="right">140</td>
<td align="right">123,620</td>
<td align="right">1,447,600</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">1,940</td>
<td align="right">2.8%</td>
<td align="right">870.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,800</td>
<td align="right">26.4%</td>
<td align="right">24,440</td>
<td align="right">34.9%</td>
<td align="right">259.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">380</td>
<td align="right">1.5%</td>
<td align="right">1,220</td>
<td align="right">1.7%</td>
<td align="right">221.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">20,460</td>
<td align="right">79.4%</td>
<td align="right">56,320</td>
<td align="right">80.4%</td>
<td align="right">175.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,780</td>
<td align="right"></td>
<td align="right">70,060</td>
<td align="right"></td>
<td align="right">171.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,260</td>
<td align="right">20.4%</td>
<td align="right">13,680</td>
<td align="right">19.5%</td>
<td align="right">160.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">47,777,740</td>
<td align="right"></td>
<td align="right">82,884,160</td>
<td align="right"></td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">764,894,620</td>
<td align="right">1,600.9%</td>
<td align="right">1,029,571,960</td>
<td align="right">1,242.2%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">620</td>
<td align="right">2.4%</td>
<td align="right">540</td>
<td align="right">0.8%</td>
<td align="right">-12.9%</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">120 / 0 !!</td>
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
<td align="right">20,080</td>
<td align="right">98.1%</td>
<td align="right">55,660</td>
<td align="right">98.8%</td>
<td align="right">177.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">20,460</td>
<td align="right"></td>
<td align="right">56,320</td>
<td align="right"></td>
<td align="right">175.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">1,580</td>
<td align="right">2.8%</td>
<td align="right">1,580 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,540</td>
<td align="right">7.5%</td>
<td align="right">2,580</td>
<td align="right">4.6%</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,040</td>
<td align="right">19.7%</td>
<td align="right">9,220</td>
<td align="right">16.4%</td>
<td align="right">128.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,640</td>
<td align="right">32.5%</td>
<td align="right">21,760</td>
<td align="right">38.6%</td>
<td align="right">227.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,620</td>
<td align="right">17.7%</td>
<td align="right">14,880</td>
<td align="right">26.4%</td>
<td align="right">311.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,700</td>
<td align="right">13.2%</td>
<td align="right">4,640</td>
<td align="right">8.2%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,700</td>
<td align="right">8.3%</td>
<td align="right">1,320</td>
<td align="right">2.3%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">220</td>
<td align="right">1.1%</td>
<td align="right">340</td>
<td align="right">0.6%</td>
<td align="right">54.5%</td>
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
<td align="right">1,120</td>
<td align="right">5.5%</td>
<td align="right">3,260</td>
<td align="right">5.8%</td>
<td align="right">191.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">3,120</td>
<td align="right">15.2%</td>
<td align="right">5,340</td>
<td align="right">9.5%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,080</td>
<td align="right">19.9%</td>
<td align="right">13,320</td>
<td align="right">23.7%</td>
<td align="right">226.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,820</td>
<td align="right">28.4%</td>
<td align="right">23,340</td>
<td align="right">41.4%</td>
<td align="right">301.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,200</td>
<td align="right">15.6%</td>
<td align="right">7,720</td>
<td align="right">13.7%</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,060</td>
<td align="right">10.1%</td>
<td align="right">2,280</td>
<td align="right">4.0%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">680</td>
<td align="right">3.3%</td>
<td align="right">400</td>
<td align="right">0.7%</td>
<td align="right">-41.2%</td>
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
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40</td>
<td align="right">18,040</td>
<td align="right">45,000.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">27,060</td>
<td align="right">4,456,740</td>
<td align="right">16,369.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,100</td>
<td align="right">1,647,180</td>
<td align="right">6,462.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">26,400</td>
<td align="right">1,273,660</td>
<td align="right">4,724.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">21,000</td>
<td align="right">597,020</td>
<td align="right">2,743.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,120</td>
<td align="right">31,180</td>
<td align="right">2,683.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,680</td>
<td align="right">254,100</td>
<td align="right">2,525.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,680</td>
<td align="right">244,260</td>
<td align="right">2,423.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">90,340</td>
<td align="right">2,007,680</td>
<td align="right">2,122.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">146,100</td>
<td align="right">2,509,680</td>
<td align="right">1,617.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">10,780</td>
<td align="right">151,940</td>
<td align="right">1,309.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">319,100</td>
<td align="right">3,058,340</td>
<td align="right">858.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">10,720</td>
<td align="right">65,140</td>
<td align="right">507.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">10,720</td>
<td align="right">65,140</td>
<td align="right">507.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">12,260</td>
<td align="right">73,800</td>
<td align="right">502.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">12,260</td>
<td align="right">73,800</td>
<td align="right">502.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">18,540</td>
<td align="right">103,560</td>
<td align="right">458.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">8,720</td>
<td align="right">45,480</td>
<td align="right">421.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">400,760</td>
<td align="right">2,025,640</td>
<td align="right">405.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,540</td>
<td align="right">11,260</td>
<td align="right">343.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">373,500</td>
<td align="right">1,584,360</td>
<td align="right">324.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">39,360</td>
<td align="right">163,600</td>
<td align="right">315.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">540</td>
<td align="right">2,220</td>
<td align="right">311.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">540</td>
<td align="right">2,220</td>
<td align="right">311.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,119,000</td>
<td align="right">23,610,760</td>
<td align="right">190.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">996,080</td>
<td align="right">2,684,700</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">996,080</td>
<td align="right">2,684,700</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,888,140</td>
<td align="right">4,967,220</td>
<td align="right">163.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">511,240</td>
<td align="right">1,216,020</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">600,760</td>
<td align="right">1,419,860</td>
<td align="right">136.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,167,180</td>
<td align="right">39,140</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,344,920</td>
<td align="right">61,400</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">28,740</td>
<td align="right">840</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,369,120</td>
<td align="right">118,160</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,549,520</td>
<td align="right">58,020</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">62,760</td>
<td align="right">2,640</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">665,040</td>
<td align="right">31,380</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">81,580</td>
<td align="right">4,080</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">732,960</td>
<td align="right">38,640</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">566,720</td>
<td align="right">35,280</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,071,020</td>
<td align="right">188,160</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,429,520</td>
<td align="right">886,700</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">877,900</td>
<td align="right">154,200</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">24,022,680</td>
<td align="right">43,278,900</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">23,973,200</td>
<td align="right">42,371,160</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">43,193,180</td>
<td align="right">76,257,420</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">15,976,160</td>
<td align="right">28,188,200</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">5,055,780</td>
<td align="right">8,898,620</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,220</td>
<td align="right">820</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">47,777,740</td>
<td align="right">82,884,160</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">70,840</td>
<td align="right">122,660</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">79,500</td>
<td align="right">24,480</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,628,860</td>
<td align="right">2,731,220</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,410,880</td>
<td align="right">2,365,180</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">49,848,760</td>
<td align="right">83,072,320</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">20,820</td>
<td align="right">7,920</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">20,820</td>
<td align="right">7,920</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3,265,420</td>
<td align="right">1,281,020</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,576,140</td>
<td align="right">4,106,760</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">219,460</td>
<td align="right">340,800</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">21,676,760</td>
<td align="right">33,354,400</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">5,358,260</td>
<td align="right">8,219,840</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">7,057,800</td>
<td align="right">10,788,260</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">436,100</td>
<td align="right">654,520</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">9,234,980</td>
<td align="right">13,846,660</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,118,700</td>
<td align="right">1,609,580</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,594,680</td>
<td align="right">6,720,580</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">163,660</td>
<td align="right">235,400</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">2,000</td>
<td align="right">1,140</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">2,000</td>
<td align="right">1,140</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">4,583,440</td>
<td align="right">6,543,000</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,384,940</td>
<td align="right">20,396,220</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">12,261,920</td>
<td align="right">17,191,380</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">6,435,760</td>
<td align="right">9,017,200</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">141,900</td>
<td align="right">197,880</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">933,420</td>
<td align="right">1,289,120</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">7,046,940</td>
<td align="right">4,438,240</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">15,628,620</td>
<td align="right">21,097,780</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">17,419,660</td>
<td align="right">23,439,380</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">7,474,620</td>
<td align="right">10,054,340</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">63,780</td>
<td align="right">85,220</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">13,717,760</td>
<td align="right">18,324,020</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">15,960</td>
<td align="right">21,240</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,139,020</td>
<td align="right">3,477,200</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">300,340</td>
<td align="right">396,280</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,469,280</td>
<td align="right">8,505,620</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">17,881,200</td>
<td align="right">23,124,320</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,471,520</td>
<td align="right">2,484,320</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">305,040</td>
<td align="right">391,180</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">290,320</td>
<td align="right">371,620</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,431,900</td>
<td align="right">2,472,620</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,184,960</td>
<td align="right">5,180,820</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,184,960</td>
<td align="right">5,180,820</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">855,960</td>
<td align="right">631,180</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">128,480</td>
<td align="right">98,340</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">530,600</td>
<td align="right">408,540</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,700,020</td>
<td align="right">9,445,940</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">12,970,980</td>
<td align="right">15,880,760</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">11,020,720</td>
<td align="right">13,448,320</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">475,620</td>
<td align="right">578,160</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2,142,380</td>
<td align="right">2,602,940</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">45,942,780</td>
<td align="right">54,787,500</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">68,210,740</td>
<td align="right">80,665,920</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">343,740</td>
<td align="right">404,940</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,608,460</td>
<td align="right">3,847,000</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">4,343,840</td>
<td align="right">5,058,600</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,872,900</td>
<td align="right">2,407,440</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">103,560</td>
<td align="right">120,240</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,869,360</td>
<td align="right">2,409,560</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,330,460</td>
<td align="right">2,807,140</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">16,176,840</td>
<td align="right">18,700,240</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">282,960</td>
<td align="right">325,560</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,726,220</td>
<td align="right">7,722,460</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">112,920</td>
<td align="right">129,120</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">4,900,060</td>
<td align="right">5,583,280</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,007,640</td>
<td align="right">2,621,840</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,430,680</td>
<td align="right">2,732,020</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">595,320</td>
<td align="right">659,060</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,068,460</td>
<td align="right">3,384,360</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">11,449,800</td>
<td align="right">12,597,860</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">9,236,380</td>
<td align="right">8,343,260</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">574,860</td>
<td align="right">525,780</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,518,400</td>
<td align="right">2,679,700</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,399,480</td>
<td align="right">4,661,940</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">924,260</td>
<td align="right">979,340</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,658,800</td>
<td align="right">1,743,460</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,193,280</td>
<td align="right">1,253,840</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">24,966,300</td>
<td align="right">26,219,940</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">8,572,400</td>
<td align="right">8,161,420</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">35,500</td>
<td align="right">33,840</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,340,420</td>
<td align="right">5,571,860</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">968,420</td>
<td align="right">1,008,040</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,659,300</td>
<td align="right">1,719,500</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">219,000</td>
<td align="right">226,880</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">354,920</td>
<td align="right">345,260</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,304,760</td>
<td align="right">12,957,860</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">332,080</td>
<td align="right">340,620</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">332,080</td>
<td align="right">340,620</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">422,900</td>
<td align="right">430,900</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">620,600</td>
<td align="right">631,400</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">687,460</td>
<td align="right">677,560</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">106,080</td>
<td align="right">107,240</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">422,900</td>
<td align="right">427,060</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">2,803,180</td>
<td align="right">2,791,480</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,679,600</td>
<td align="right">1,685,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">846,360</td>
<td align="right">848,260</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,107,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,107,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">728,640</td>
<td align="right">728,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">676,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">676,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">676,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">630,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">630,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">69,120</td>
<td align="right">69,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">10,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">5,400</td>
<td align="right">5,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">2,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">106,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">106,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">52,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">9,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">1,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">20</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">720</td>
<td align="right">3,180</td>
<td align="right">341.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">540</td>
<td align="right">320</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">240</td>
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
Stats gathered on: 2024-10-23
