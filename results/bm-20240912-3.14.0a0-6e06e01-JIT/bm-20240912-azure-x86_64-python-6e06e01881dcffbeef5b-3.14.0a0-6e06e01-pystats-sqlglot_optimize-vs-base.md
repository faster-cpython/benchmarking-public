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
<td align="right">22,657,920</td>
<td align="right">59,840</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,781,600</td>
<td align="right">29,420</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">92,120</td>
<td align="right">3,000</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,325,360</td>
<td align="right">100,600</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,432,040</td>
<td align="right">105,940</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">962,400</td>
<td align="right">57,060</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,315,780</td>
<td align="right">84,140</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">452,100</td>
<td align="right">39,060</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,520,520</td>
<td align="right">286,920</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,904,400</td>
<td align="right">1,158,860</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,558,820</td>
<td align="right">272,740</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,034,480</td>
<td align="right">1,987,040</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">94,880</td>
<td align="right">19,200</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">19,176,320</td>
<td align="right">3,969,760</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">636,980</td>
<td align="right">132,700</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,995,760</td>
<td align="right">862,240</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,222,400</td>
<td align="right">920,440</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4,811,540</td>
<td align="right">1,059,360</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">180,580</td>
<td align="right">40,100</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,201,680</td>
<td align="right">1,164,960</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">551,920</td>
<td align="right">123,720</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,718,160</td>
<td align="right">652,780</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">595,520</td>
<td align="right">155,200</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">290,400</td>
<td align="right">83,320</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,215,920</td>
<td align="right">357,760</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">14,008,320</td>
<td align="right">4,168,540</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,736,100</td>
<td align="right">3,815,000</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,009,440</td>
<td align="right">331,140</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,480,980</td>
<td align="right">502,600</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,137,200</td>
<td align="right">1,115,320</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,342,720</td>
<td align="right">1,199,280</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">31,840</td>
<td align="right">11,880</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">391,640</td>
<td align="right">150,620</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,081,560</td>
<td align="right">8,509,880</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">38,220</td>
<td align="right">16,700</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">45,553,440</td>
<td align="right">19,974,620</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">36,286,200</td>
<td align="right">16,068,000</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">37,015,640</td>
<td align="right">16,557,360</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,996,020</td>
<td align="right">1,789,100</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">71,821,580</td>
<td align="right">32,203,700</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">160,095,200</td>
<td align="right">72,000,200</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">44,745,960</td>
<td align="right">20,622,100</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,194,580</td>
<td align="right">1,978,620</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,025,760</td>
<td align="right">1,959,140</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12,022,400</td>
<td align="right">5,893,780</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">317,920</td>
<td align="right">157,020</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">19,722,160</td>
<td align="right">9,777,900</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,611,780</td>
<td align="right">802,160</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">34,781,940</td>
<td align="right">17,422,020</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,147,560</td>
<td align="right">6,658,020</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,174,640</td>
<td align="right">6,259,720</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,320,400</td>
<td align="right">1,715,020</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,323,280</td>
<td align="right">7,028,960</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">171,940</td>
<td align="right">91,320</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">15,009,600</td>
<td align="right">7,976,920</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,106,100</td>
<td align="right">588,200</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">44,933,400</td>
<td align="right">24,046,740</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">234,560</td>
<td align="right">126,580</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,371,000</td>
<td align="right">12,973,800</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,082,080</td>
<td align="right">2,836,640</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">314,660</td>
<td align="right">177,700</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,611,120</td>
<td align="right">2,661,560</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">265,940</td>
<td align="right">156,240</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,029,280</td>
<td align="right">608,200</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">9,715,380</td>
<td align="right">5,965,080</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">17,920</td>
<td align="right">11,020</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,622,560</td>
<td align="right">1,001,100</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,806,880</td>
<td align="right">4,231,340</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,243,360</td>
<td align="right">5,865,720</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">317,520</td>
<td align="right">207,100</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">246,620</td>
<td align="right">161,740</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,909,840</td>
<td align="right">1,938,640</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">872,000</td>
<td align="right">583,020</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">99,920</td>
<td align="right">74,280</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">99,920</td>
<td align="right">74,280</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">675,280</td>
<td align="right">511,400</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">25,400</td>
<td align="right">19,280</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,008,280</td>
<td align="right">13,204,780</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29,524,500</td>
<td align="right">22,963,080</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">132,640</td>
<td align="right">103,380</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,910,240</td>
<td align="right">1,489,160</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">179,260</td>
<td align="right">143,260</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,013,220</td>
<td align="right">817,660</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,530,560</td>
<td align="right">2,068,100</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">184,640</td>
<td align="right">151,000</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,277,920</td>
<td align="right">1,047,040</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">56,480</td>
<td align="right">46,680</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20,740</td>
<td align="right">17,220</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">37,880</td>
<td align="right">32,220</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,447,700</td>
<td align="right">2,969,860</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,657,540</td>
<td align="right">3,212,780</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,932,360</td>
<td align="right">3,479,280</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">437,740</td>
<td align="right">398,320</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">597,700</td>
<td align="right">548,300</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,678,720</td>
<td align="right">1,542,040</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,734,960</td>
<td align="right">1,651,840</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,234,240</td>
<td align="right">1,179,120</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,387,040</td>
<td align="right">5,176,360</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">93,980</td>
<td align="right">90,840</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">431,400</td>
<td align="right">417,860</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">812,000</td>
<td align="right">786,600</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,331,040</td>
<td align="right">2,262,960</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">166,000</td>
<td align="right">161,200</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,215,520</td>
<td align="right">3,123,000</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">196,800</td>
<td align="right">192,040</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">31,140</td>
<td align="right">30,400</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">6,013,920</td>
<td align="right">5,975,100</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,428,580</td>
<td align="right">10,423,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">10,029,280</td>
<td align="right">10,029,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,030,080</td>
<td align="right">1,030,080</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">14,900,160</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,520</td>
<td align="right">2.2%</td>
<td align="right">16,060</td>
<td align="right">1.8%</td>
<td align="right">-17.7%</td>
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
<td align="right">97.7%</td>
<td align="right">867,940</td>
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
<td align="left">Failure</td>
<td align="right">740</td>
<td align="right">60.7%</td>
<td align="right">680</td>
<td align="right">58.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">480</td>
<td align="right">39.3%</td>
<td align="right">480</td>
<td align="right">41.4%</td>
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
<td align="right">700</td>
<td align="right">94.6%</td>
<td align="right">640</td>
<td align="right">94.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">40</td>
<td align="right">5.4%</td>
<td align="right">40</td>
<td align="right">5.9%</td>
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
<td align="right">94,880</td>
<td align="right">100.0%</td>
<td align="right">19,200</td>
<td align="right">100.0%</td>
<td align="right">-79.8%</td>
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
<td align="right">37,140</td>
<td align="right">1.5%</td>
<td align="right">15,700</td>
<td align="right">0.6%</td>
<td align="right">-57.7%</td>
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
<td align="right">98.2%</td>
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
<td align="right">420</td>
<td align="right">35.6%</td>
<td align="right">340</td>
<td align="right">30.9%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">760</td>
<td align="right">64.4%</td>
<td align="right">760</td>
<td align="right">69.1%</td>
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
<td align="right">180</td>
<td align="right">42.9%</td>
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240</td>
<td align="right">57.1%</td>
<td align="right">240</td>
<td align="right">70.6%</td>
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
<td align="right">678,640</td>
<td align="right">0.8%</td>
<td align="right">268,500</td>
<td align="right">0.3%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">86,713,520</td>
<td align="right">99.2%</td>
<td align="right">87,248,800</td>
<td align="right">99.7%</td>
<td align="right">0.6%</td>
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
<td align="right">31,340</td>
<td align="right">100.0%</td>
<td align="right">23,600</td>
<td align="right">100.0%</td>
<td align="right">-24.7%</td>
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
<td align="right">1,007,840</td>
<td align="right">48.3%</td>
<td align="right">812,580</td>
<td align="right">42.9%</td>
<td align="right">-19.4%</td>
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
<td align="right">51.5%</td>
<td align="right">1,074,720</td>
<td align="right">56.8%</td>
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
<td align="right">4,580</td>
<td align="right">85.1%</td>
<td align="right">4,280</td>
<td align="right">84.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">800</td>
<td align="right">14.9%</td>
<td align="right">800</td>
<td align="right">15.7%</td>
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
<td align="left">string</td>
<td align="right">200</td>
<td align="right">4.4%</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">220</td>
<td align="right">4.8%</td>
<td align="right">200</td>
<td align="right">4.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">2,040</td>
<td align="right">44.5%</td>
<td align="right">1,860</td>
<td align="right">43.5%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,500</td>
<td align="right">32.8%</td>
<td align="right">1,500</td>
<td align="right">35.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">9.2%</td>
<td align="right">420</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">120</td>
<td align="right">2.6%</td>
<td align="right">120</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">80</td>
<td align="right">1.7%</td>
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
<td align="right">263,980</td>
<td align="right">31.9%</td>
<td align="right">154,320</td>
<td align="right">21.5%</td>
<td align="right">-41.5%</td>
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
<td align="right">63.8%</td>
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
<td align="right">4.1%</td>
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
<td align="right">1,340</td>
<td align="right">51.9%</td>
<td align="right">1,300</td>
<td align="right">51.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">48.1%</td>
<td align="right">1,240</td>
<td align="right">48.8%</td>
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
<td align="right">400</td>
<td align="right">29.9%</td>
<td align="right">380</td>
<td align="right">29.2%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">940</td>
<td align="right">70.1%</td>
<td align="right">920</td>
<td align="right">70.8%</td>
<td align="right">-2.1%</td>
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
<td align="right">19,164,700</td>
<td align="right">57.5%</td>
<td align="right">3,962,700</td>
<td align="right">45.9%</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,150,740</td>
<td align="right">42.5%</td>
<td align="right">4,662,980</td>
<td align="right">54.0%</td>
<td align="right">-67.0%</td>
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
<td align="right">9,960</td>
<td align="right">85.7%</td>
<td align="right">5,400</td>
<td align="right">76.5%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,660</td>
<td align="right">14.3%</td>
<td align="right">1,660</td>
<td align="right">23.5%</td>
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
<td align="right">6,360</td>
<td align="right">63.9%</td>
<td align="right">2,720</td>
<td align="right">50.4%</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">540</td>
<td align="right">5.4%</td>
<td align="right">320</td>
<td align="right">5.9%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">120</td>
<td align="right">2.2%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">520</td>
<td align="right">5.2%</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">460</td>
<td align="right">4.6%</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">260</td>
<td align="right">2.6%</td>
<td align="right">200</td>
<td align="right">3.7%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">540</td>
<td align="right">5.4%</td>
<td align="right">440</td>
<td align="right">8.1%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">880</td>
<td align="right">8.8%</td>
<td align="right">740</td>
<td align="right">13.7%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">-10.0%</td>
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
<td align="right">439,820</td>
<td align="right">0.7%</td>
<td align="right">106,940</td>
<td align="right">0.2%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,180,600</td>
<td align="right">16.3%</td>
<td align="right">4,519,200</td>
<td align="right">8.0%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">641,980</td>
<td align="right">1.0%</td>
<td align="right">478,340</td>
<td align="right">0.9%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,660,840</td>
<td align="right">82.6%</td>
<td align="right">51,209,400</td>
<td align="right">91.1%</td>
<td align="right">-0.9%</td>
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
<td align="right">212,680</td>
<td align="right">94.7%</td>
<td align="right">105,940</td>
<td align="right">90.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,800</td>
<td align="right">5.3%</td>
<td align="right">11,560</td>
<td align="right">9.8%</td>
<td align="right">-2.0%</td>
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
<td align="right">140</td>
<td align="right">1.2%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,900</td>
<td align="right">16.1%</td>
<td align="right">1,860</td>
<td align="right">16.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">9,540</td>
<td align="right">80.8%</td>
<td align="right">9,360</td>
<td align="right">81.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">220</td>
<td align="right">1.9%</td>
<td align="right">220</td>
<td align="right">1.9%</td>
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
<td align="right">106,599,280</td>
<td align="right">100.0%</td>
<td align="right">50,720,240</td>
<td align="right">99.9%</td>
<td align="right">-52.4%</td>
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
<td align="right">1,948,360</td>
<td align="right">44.6%</td>
<td align="right">1,232,940</td>
<td align="right">32.8%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,412,220</td>
<td align="right">55.3%</td>
<td align="right">2,523,180</td>
<td align="right">67.1%</td>
<td align="right">4.6%</td>
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
<td align="right">38,260</td>
<td align="right">100.0%</td>
<td align="right">24,780</td>
<td align="right">100.0%</td>
<td align="right">-35.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,422,100</td>
<td align="right">4.5%</td>
<td align="right">96,680</td>
<td align="right">0.2%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,210,680</td>
<td align="right">5.9%</td>
<td align="right">1,294,440</td>
<td align="right">2.6%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,622,620</td>
<td align="right">89.6%</td>
<td align="right">48,487,780</td>
<td align="right">97.2%</td>
<td align="right">-0.3%</td>
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
<td align="right">67,940</td>
<td align="right">97.0%</td>
<td align="right">31,820</td>
<td align="right">95.7%</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,080</td>
<td align="right">3.0%</td>
<td align="right">1,420</td>
<td align="right">4.3%</td>
<td align="right">-31.7%</td>
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
<td align="right">660</td>
<td align="right">31.7%</td>
<td align="right">300</td>
<td align="right">21.1%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">680</td>
<td align="right">32.7%</td>
<td align="right">380</td>
<td align="right">26.8%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">540</td>
<td align="right">26.0%</td>
<td align="right">540</td>
<td align="right">38.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120</td>
<td align="right">5.8%</td>
<td align="right">120</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">80</td>
<td align="right">3.8%</td>
<td align="right">80</td>
<td align="right">5.6%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">23,804,080</td>
<td align="right">2.6%</td>
<td align="right">5,701,560</td>
<td align="right">1.2%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">16,062,720</td>
<td align="right">1.8%</td>
<td align="right">7,359,560</td>
<td align="right">1.6%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">386,787,380</td>
<td align="right">42.2%</td>
<td align="right">184,014,560</td>
<td align="right">40.1%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">489,314,600</td>
<td align="right">53.4%</td>
<td align="right">262,169,760</td>
<td align="right">57.1%</td>
<td align="right">-46.4%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">2,422,100</td>
<td align="right">10.2%</td>
<td align="right">96,680</td>
<td align="right">1.7%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">94,880</td>
<td align="right">0.4%</td>
<td align="right">19,200</td>
<td align="right">0.3%</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">19,164,700</td>
<td align="right">80.9%</td>
<td align="right">3,962,700</td>
<td align="right">70.7%</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">37,140</td>
<td align="right">0.2%</td>
<td align="right">15,700</td>
<td align="right">0.3%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">263,980</td>
<td align="right">1.1%</td>
<td align="right">154,320</td>
<td align="right">2.8%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">641,980</td>
<td align="right">2.7%</td>
<td align="right">478,340</td>
<td align="right">8.5%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,007,840</td>
<td align="right">4.3%</td>
<td align="right">812,580</td>
<td align="right">14.5%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">19,520</td>
<td align="right">0.1%</td>
<td align="right">16,060</td>
<td align="right">0.3%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,160</td>
<td align="right">0.1%</td>
<td align="right">17,160</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">15,660</td>
<td align="right">0.1%</td>
<td align="right">15,660</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">301,780</td>
<td align="right">1.9%</td>
<td align="right">63,500</td>
<td align="right">0.9%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">264,880</td>
<td align="right">1.6%</td>
<td align="right">89,180</td>
<td align="right">1.2%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,359,540</td>
<td align="right">45.8%</td>
<td align="right">2,709,200</td>
<td align="right">36.8%</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,250,700</td>
<td align="right">14.0%</td>
<td align="right">920,500</td>
<td align="right">12.5%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">367,380</td>
<td align="right">2.3%</td>
<td align="right">165,800</td>
<td align="right">2.3%</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">641,680</td>
<td align="right">4.0%</td>
<td align="right">294,680</td>
<td align="right">4.0%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,234,180</td>
<td align="right">7.7%</td>
<td align="right">574,200</td>
<td align="right">7.8%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,948,360</td>
<td align="right">12.1%</td>
<td align="right">1,232,940</td>
<td align="right">16.8%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,521,360</td>
<td align="right">9.5%</td>
<td align="right">1,175,300</td>
<td align="right">16.0%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">49,360</td>
<td align="right">0.3%</td>
<td align="right">44,340</td>
<td align="right">0.6%</td>
<td align="right">-10.2%</td>
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
<td align="right">3,204,220</td>
<td align="right">6.7%</td>
<td align="right">3,199,300</td>
<td align="right">6.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,515,980</td>
<td align="right">9.4%</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,515,980</td>
<td align="right">9.4%</td>
<td align="right">4,511,060</td>
<td align="right">9.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">10,428,580</td>
<td align="right">21.7%</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,428,580</td>
<td align="right">21.7%</td>
<td align="right">10,423,660</td>
<td align="right">21.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">37,726,660</td>
<td align="right">78.3%</td>
<td align="right">37,731,580</td>
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
<td align="left">Increfs</td>
<td align="right">202,675,215</td>
<td align="right">35.8%</td>
<td align="right">434,231,447</td>
<td align="right">67.7%</td>
<td align="right">114.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">231,362,681</td>
<td align="right">35.4%</td>
<td align="right">448,484,016</td>
<td align="right">61.6%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">364,041,580</td>
<td align="right">64.2%</td>
<td align="right">206,839,840</td>
<td align="right">32.3%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">422,199,720</td>
<td align="right">64.6%</td>
<td align="right">279,486,900</td>
<td align="right">38.4%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">23,005</td>
<td align="right"></td>
<td align="right">19,145</td>
<td align="right"></td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">12,571,639</td>
<td align="right"></td>
<td align="right">10,744,377</td>
<td align="right"></td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">75,360</td>
<td align="right">0.1%</td>
<td align="right">80,380</td>
<td align="right">0.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">651,729</td>
<td align="right"></td>
<td align="right">645,166</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">63,376,555</td>
<td align="right"></td>
<td align="right">62,871,015</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">635,721</td>
<td align="right"></td>
<td align="right">632,403</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">61,545,900</td>
<td align="right"></td>
<td align="right">61,575,014</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,516,280</td>
<td align="right">63.2%</td>
<td align="right">60,523,420</td>
<td align="right">63.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">35,413,400</td>
<td align="right"></td>
<td align="right">35,415,600</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">35,262,820</td>
<td align="right">36.8%</td>
<td align="right">35,264,120</td>
<td align="right">36.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,440,760</td>
<td align="right">63.1%</td>
<td align="right">60,442,760</td>
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
<td align="right">240</td>
<td align="right">167,700</td>
<td align="right">7,179,960</td>
<td align="right">260</td>
<td align="right">185,240</td>
<td align="right">7,368,360</td>
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
Stats gathered on: 2024-09-22
