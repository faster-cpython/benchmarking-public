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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,200</td>
<td align="right">2,940</td>
<td align="right">145.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">20,357,820</td>
<td align="right">1,440</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">242,400</td>
<td align="right">60</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">23,133,300</td>
<td align="right">11,880</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,371,240</td>
<td align="right">3,120</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,389,420</td>
<td align="right">3,000</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,197,940</td>
<td align="right">17,820</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,999,680</td>
<td align="right">2,940</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">20,500,300</td>
<td align="right">20,580</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">4,080,020</td>
<td align="right">8,880</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">16,788,920</td>
<td align="right">55,860</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,178,860</td>
<td align="right">94,500</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,867,560</td>
<td align="right">109,300</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">8,442,740</td>
<td align="right">32,340</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">5,402,540</td>
<td align="right">20,760</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">91,420</td>
<td align="right">360</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,603,940</td>
<td align="right">44,100</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">16,806,560</td>
<td align="right">73,500</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">28,874,400</td>
<td align="right">152,880</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">4,331,320</td>
<td align="right">23,520</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,526,240</td>
<td align="right">277,060</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,594,200</td>
<td align="right">52,920</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">74,214,720</td>
<td align="right">709,680</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,782,540</td>
<td align="right">47,040</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">10,446,680</td>
<td align="right">126,540</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,710,040</td>
<td align="right">743,220</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">52,740</td>
<td align="right">660</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">2,872,500</td>
<td align="right">36,840</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,339,940</td>
<td align="right">147,060</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">9,409,040</td>
<td align="right">125,920</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">20,926,000</td>
<td align="right">281,280</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,813,340</td>
<td align="right">27,180</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">13,953,340</td>
<td align="right">215,800</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">10,817,840</td>
<td align="right">167,580</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,507,760</td>
<td align="right">72,240</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">44,569,620</td>
<td align="right">723,420</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">12,008,100</td>
<td align="right">196,820</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">86,067,820</td>
<td align="right">1,411,980</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">102,583,240</td>
<td align="right">1,962,580</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">82,001,920</td>
<td align="right">1,576,880</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,424,420</td>
<td align="right">67,620</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,424,420</td>
<td align="right">67,620</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,934,420</td>
<td align="right">58,800</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,237,700</td>
<td align="right">67,620</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">11,743,720</td>
<td align="right">247,140</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">21,529,580</td>
<td align="right">462,120</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">22,544,780</td>
<td align="right">500,660</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,540,700</td>
<td align="right">41,220</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">68,632,360</td>
<td align="right">1,861,500</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">38,217,240</td>
<td align="right">1,078,920</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,543,680</td>
<td align="right">44,160</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">114,088,020</td>
<td align="right">3,373,440</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,427,980</td>
<td align="right">192,660</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">16,763,760</td>
<td align="right">514,280</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,340,360</td>
<td align="right">41,160</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,711,220</td>
<td align="right">459,780</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,418,260</td>
<td align="right">78,120</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,692,900</td>
<td align="right">88,240</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">164,522,580</td>
<td align="right">5,460,600</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">167,641,520</td>
<td align="right">5,691,060</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">657,020</td>
<td align="right">23,520</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">22,361,620</td>
<td align="right">801,280</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">12,379,460</td>
<td align="right">449,180</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,611,300</td>
<td align="right">94,760</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">67,110,040</td>
<td align="right">2,460,000</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,286,240</td>
<td align="right">493,780</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,418,640</td>
<td align="right">53,040</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">65,139,580</td>
<td align="right">2,454,180</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">22,131,180</td>
<td align="right">861,280</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">186,923,980</td>
<td align="right">7,311,520</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">108,464,400</td>
<td align="right">4,306,180</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,355,260</td>
<td align="right">214,780</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,405,620</td>
<td align="right">430,680</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">780,100</td>
<td align="right">32,340</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214,151,620</td>
<td align="right">8,940,680</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,809,300</td>
<td align="right">562,860</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">51,239,240</td>
<td align="right">2,251,660</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40,658,080</td>
<td align="right">1,795,980</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">687,629,860</td>
<td align="right">30,511,680</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">12,791,240</td>
<td align="right">608,640</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">99,587,600</td>
<td align="right">4,769,840</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">51,393,740</td>
<td align="right">2,476,500</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,229,220</td>
<td align="right">2,450,720</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">114,402,020</td>
<td align="right">5,791,260</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">88,300,540</td>
<td align="right">4,564,800</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">28,459,200</td>
<td align="right">1,476,120</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">27,476,520</td>
<td align="right">1,496,640</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">173,509,120</td>
<td align="right">9,993,820</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">7,226,040</td>
<td align="right">421,560</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,624,820</td>
<td align="right">98,760</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,799,040</td>
<td align="right">2,536,720</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">5,051,760</td>
<td align="right">314,640</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,850,700</td>
<td align="right">555,000</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">46,020</td>
<td align="right">2,940</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,471,260</td>
<td align="right">161,700</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">300</td>
<td align="right">20</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">44,000</td>
<td align="right">2,940</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,649,860</td>
<td align="right">670,320</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,194,120</td>
<td align="right">652,740</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,877,400</td>
<td align="right">640,920</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,137,740</td>
<td align="right">313,160</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,523,240</td>
<td align="right">115,520</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">831,560</td>
<td align="right">65,180</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">34,910,340</td>
<td align="right">2,810,780</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,229,740</td>
<td align="right">100,100</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">21,300,080</td>
<td align="right">1,737,720</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,601,760</td>
<td align="right">555,420</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">6,842,240</td>
<td align="right">617,520</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">29,291,140</td>
<td align="right">2,760,900</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">43,685,400</td>
<td align="right">4,154,300</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">843,940</td>
<td align="right">81,660</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">44,260</td>
<td align="right">4,380</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,003,960</td>
<td align="right">323,600</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">8,334,280</td>
<td align="right">946,920</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">167,300</td>
<td align="right">19,320</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">4,120</td>
<td align="right">480</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,100,340</td>
<td align="right">368,400</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300</td>
<td align="right">40</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,516,200</td>
<td align="right">355,740</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">520,420</td>
<td align="right">73,780</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">293,900</td>
<td align="right">42,720</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,332,440</td>
<td align="right">348,040</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">75,980</td>
<td align="right">11,700</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,440</td>
<td align="right">700</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">350,460</td>
<td align="right">58,920</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,220</td>
<td align="right">380</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">2,084,760</td>
<td align="right">358,680</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,919,840</td>
<td align="right">343,880</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,620</td>
<td align="right">2,940</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,481,160</td>
<td align="right">299,940</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">328,640</td>
<td align="right">68,760</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,334,120</td>
<td align="right">341,520</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,309,800</td>
<td align="right">1,406,200</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,814,400</td>
<td align="right">1,711,940</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">144,220</td>
<td align="right">47,040</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,136,900</td>
<td align="right">1,996,320</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">548,540</td>
<td align="right">385,320</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,040</td>
<td align="right">2,940</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">38,900</td>
<td align="right">35,400</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">24,240</td>
<td align="right">23,520</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">415,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">194,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">152,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">93,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">82,320</td>
<td align="right">82,320</td>
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
<td align="left">UNARY_INVERT</td>
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
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">12,400</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,480</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">DELETE_ATTR</td>
<td align="right">1,940</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">RESUME</td>
<td align="right">1,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">100</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">80</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">60</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">20</td>
<td align="right"></td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,801,060</td>
<td align="right">2.7%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">89,943,520</td>
<td align="right">85.2%</td>
<td align="right">2,481,720</td>
<td align="right">81.5%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,748,040</td>
<td align="right">12.1%</td>
<td align="right">561,780</td>
<td align="right">18.5%</td>
<td align="right">-95.6%</td>
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
<td align="right">53,700</td>
<td align="right">47.1%</td>
<td align="right">40</td>
<td align="right">3.7%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60,340</td>
<td align="right">52.9%</td>
<td align="right">1,040</td>
<td align="right">96.3%</td>
<td align="right">-98.3%</td>
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
<td align="left">add different types</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">20</td>
<td align="right">1.9%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">4,280</td>
<td align="right">7.1%</td>
<td align="right">60</td>
<td align="right">5.8%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,020</td>
<td align="right">3.3%</td>
<td align="right">100</td>
<td align="right">9.6%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,220</td>
<td align="right">5.3%</td>
<td align="right">480</td>
<td align="right">46.2%</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">220</td>
<td align="right">0.4%</td>
<td align="right">100</td>
<td align="right">9.6%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">47,880</td>
<td align="right">79.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">5,594,200</td>
<td align="right">100.0%</td>
<td align="right">52,920</td>
<td align="right">100.0%</td>
<td align="right">-99.1%</td>
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
<td align="right">299,139,380</td>
<td align="right">96.7%</td>
<td align="right">17,913,380</td>
<td align="right">91.0%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,031,120</td>
<td align="right">3.2%</td>
<td align="right">1,727,800</td>
<td align="right">8.8%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,223,600</td>
<td align="right">3.3%</td>
<td align="right">1,761,040</td>
<td align="right">9.0%</td>
<td align="right">-82.8%</td>
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
<td align="right">196,920</td>
<td align="right">100.0%</td>
<td align="right">33,940</td>
<td align="right">100.0%</td>
<td align="right">-82.8%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">-93.3%</td>
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
<td align="right">818,820</td>
<td align="right">4.0%</td>
<td align="right">53,480</td>
<td align="right">0.7%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,442,420</td>
<td align="right">94.7%</td>
<td align="right">7,113,780</td>
<td align="right">95.8%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">251,960</td>
<td align="right">1.2%</td>
<td align="right">244,900</td>
<td align="right">3.3%</td>
<td align="right">-2.8%</td>
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
<td align="right">12,400</td>
<td align="right">71.0%</td>
<td align="right">11,580</td>
<td align="right">71.0%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,060</td>
<td align="right">29.0%</td>
<td align="right">4,740</td>
<td align="right">29.0%</td>
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
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,060</td>
<td align="right">97.3%</td>
<td align="right">11,540</td>
<td align="right">99.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">32,549,580</td>
<td align="right">86.0%</td>
<td align="right">4,574,760</td>
<td align="right">76.5%</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,306,480</td>
<td align="right">14.0%</td>
<td align="right">1,405,380</td>
<td align="right">23.5%</td>
<td align="right">-73.5%</td>
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
<td align="right">3.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,200</td>
<td align="right">96.4%</td>
<td align="right">820</td>
<td align="right">100.0%</td>
<td align="right">-74.4%</td>
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
<td align="right">1,180</td>
<td align="right">36.9%</td>
<td align="right">80</td>
<td align="right">9.8%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">600</td>
<td align="right">18.8%</td>
<td align="right">80</td>
<td align="right">9.8%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">560</td>
<td align="right">17.5%</td>
<td align="right">180</td>
<td align="right">22.0%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">860</td>
<td align="right">26.9%</td>
<td align="right">480</td>
<td align="right">58.5%</td>
<td align="right">-44.2%</td>
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
<td align="right">15,126,780</td>
<td align="right">14.7%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,004,540</td>
<td align="right">11.7%</td>
<td align="right">196,680</td>
<td align="right">3.8%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,472,180</td>
<td align="right">73.6%</td>
<td align="right">5,020,220</td>
<td align="right">96.2%</td>
<td align="right">-93.3%</td>
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
<td align="right">285,420</td>
<td align="right">98.8%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,560</td>
<td align="right">1.2%</td>
<td align="right">140</td>
<td align="right">87.5%</td>
<td align="right">-96.1%</td>
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
<td align="right">560</td>
<td align="right">15.7%</td>
<td align="right">40</td>
<td align="right">28.6%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">5.1%</td>
<td align="right">60</td>
<td align="right">42.9%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,180</td>
<td align="right">33.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">620</td>
<td align="right">17.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">420</td>
<td align="right">11.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">20</td>
<td align="right">0.6%</td>
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
<td align="left">generator</td>
<td align="right">20,373,320</td>
<td align="right">20,373,320 / 0 !!</td>
<td align="right">1,440</td>
<td align="right">1,440 / 0 !!</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">19,980</td>
<td align="right">19,980 / 0 !!</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">779,360</td>
<td align="right">779,360 / 0 !!</td>
<td align="right">2,940</td>
<td align="right">2,940 / 0 !!</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">16,715,520</td>
<td align="right">16,715,520 / 0 !!</td>
<td align="right">502,860</td>
<td align="right">502,860 / 0 !!</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,310,900</td>
<td align="right">3,310,900 / 0 !!</td>
<td align="right">114,720</td>
<td align="right">114,720 / 0 !!</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">27,081,740</td>
<td align="right">27,081,740 / 0 !!</td>
<td align="right">2,153,580</td>
<td align="right">2,153,580 / 0 !!</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">112,980</td>
<td align="right">112,980 / 0 !!</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">108,360</td>
<td align="right">108,360 / 0 !!</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,300</td>
<td align="right">1,300 / 0 !!</td>
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
<td align="right">157,553,020</td>
<td align="right">27.9%</td>
<td align="right">1,518,500</td>
<td align="right">5.4%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,339,400</td>
<td align="right">10.5%</td>
<td align="right">735,240</td>
<td align="right">2.6%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">347,953,320</td>
<td align="right">61.6%</td>
<td align="right">25,825,760</td>
<td align="right">91.9%</td>
<td align="right">-92.6%</td>
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
<td align="right">2,944,140</td>
<td align="right">99.5%</td>
<td align="right">29,720</td>
<td align="right">95.7%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,700</td>
<td align="right">0.5%</td>
<td align="right">1,340</td>
<td align="right">4.3%</td>
<td align="right">-90.2%</td>
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
<td align="right">6,320</td>
<td align="right">46.1%</td>
<td align="right">100</td>
<td align="right">7.5%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,160</td>
<td align="right">23.1%</td>
<td align="right">460</td>
<td align="right">34.3%</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">540</td>
<td align="right">3.9%</td>
<td align="right">80</td>
<td align="right">6.0%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">200</td>
<td align="right">14.9%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">180</td>
<td align="right">13.4%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,580</td>
<td align="right">11.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">260</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.9%</td>
<td align="right">120</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">100</td>
<td align="right">0.7%</td>
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
<td align="right">154,744,580</td>
<td align="right">100.0%</td>
<td align="right">5,169,420</td>
<td align="right">100.0%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,520</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">2,100</td>
<td align="right">100.0%</td>
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">-81.9%</td>
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
<td align="right">46,020</td>
<td align="right">100.0%</td>
<td align="right">2,940</td>
<td align="right">100.0%</td>
<td align="right">-93.6%</td>
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
<td align="right">29,530,300</td>
<td align="right">43.4%</td>
<td align="right">412,760</td>
<td align="right">14.0%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,370,200</td>
<td align="right">18.2%</td>
<td align="right">447,000</td>
<td align="right">15.2%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,073,840</td>
<td align="right">38.4%</td>
<td align="right">2,076,900</td>
<td align="right">70.7%</td>
<td align="right">-92.0%</td>
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
<td align="right">557,720</td>
<td align="right">98.4%</td>
<td align="right">8,260</td>
<td align="right">79.7%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,840</td>
<td align="right">1.6%</td>
<td align="right">2,100</td>
<td align="right">20.3%</td>
<td align="right">-76.2%</td>
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
<td align="right">6,300</td>
<td align="right">71.3%</td>
<td align="right">260</td>
<td align="right">12.4%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">60</td>
<td align="right">2.9%</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">80</td>
<td align="right">3.8%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,020</td>
<td align="right">22.9%</td>
<td align="right">1,660</td>
<td align="right">79.0%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">780</td>
<td align="right">8.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">1.9%</td>
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
<td align="right">152,440</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">24,286,040</td>
<td align="right">90.0%</td>
<td align="right">685,080</td>
<td align="right">88.6%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,690,200</td>
<td align="right">10.0%</td>
<td align="right">88,200</td>
<td align="right">11.4%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">5.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,580</td>
<td align="right">94.9%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">-98.4%</td>
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
<td align="right">620</td>
<td align="right">24.0%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">1,780</td>
<td align="right">69.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">140</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">5,492,300</td>
<td align="right">3.8%</td>
<td align="right">147,700</td>
<td align="right">3.2%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">136,871,280</td>
<td align="right">94.6%</td>
<td align="right">4,051,320</td>
<td align="right">89.1%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,233,720</td>
<td align="right">1.5%</td>
<td align="right">344,620</td>
<td align="right">7.6%</td>
<td align="right">-84.6%</td>
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
<td align="right">104,680</td>
<td align="right">51.7%</td>
<td align="right">3,100</td>
<td align="right">49.5%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97,720</td>
<td align="right">48.3%</td>
<td align="right">3,160</td>
<td align="right">50.5%</td>
<td align="right">-96.8%</td>
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
<td align="right">25,080</td>
<td align="right">25.7%</td>
<td align="right">2,480</td>
<td align="right">78.5%</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,020</td>
<td align="right">1.0%</td>
<td align="right">640</td>
<td align="right">20.3%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">70,160</td>
<td align="right">71.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,340</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
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
<td align="right">26,170,220</td>
<td align="right">100.0%</td>
<td align="right">2,892,840</td>
<td align="right">100.0%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">-88.2%</td>
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
<td align="right">220,987,280</td>
<td align="right">5.6%</td>
<td align="right">4,085,640</td>
<td align="right">2.6%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">180,937,540</td>
<td align="right">4.6%</td>
<td align="right">6,373,800</td>
<td align="right">4.1%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,319,982,580</td>
<td align="right">33.2%</td>
<td align="right">52,911,740</td>
<td align="right">33.7%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,253,136,300</td>
<td align="right">56.7%</td>
<td align="right">93,548,920</td>
<td align="right">59.6%</td>
<td align="right">-95.8%</td>
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
<td align="right">5,594,200</td>
<td align="right">4.5%</td>
<td align="right">52,920</td>
<td align="right">0.9%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,339,400</td>
<td align="right">48.1%</td>
<td align="right">735,240</td>
<td align="right">13.1%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">12,004,540</td>
<td align="right">9.7%</td>
<td align="right">196,680</td>
<td align="right">3.5%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,690,200</td>
<td align="right">2.2%</td>
<td align="right">88,200</td>
<td align="right">1.6%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">12,370,200</td>
<td align="right">10.0%</td>
<td align="right">447,000</td>
<td align="right">8.0%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,748,040</td>
<td align="right">10.3%</td>
<td align="right">561,780</td>
<td align="right">10.0%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">818,820</td>
<td align="right">0.7%</td>
<td align="right">53,480</td>
<td align="right">1.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,233,720</td>
<td align="right">1.8%</td>
<td align="right">344,620</td>
<td align="right">6.1%</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">10,031,120</td>
<td align="right">8.1%</td>
<td align="right">1,727,800</td>
<td align="right">30.8%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,306,480</td>
<td align="right">4.3%</td>
<td align="right">1,405,380</td>
<td align="right">25.0%</td>
<td align="right">-73.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">45,861,800</td>
<td align="right">20.8%</td>
<td align="right">367,720</td>
<td align="right">9.0%</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">56,680,280</td>
<td align="right">25.6%</td>
<td align="right">686,040</td>
<td align="right">16.8%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">29,529,240</td>
<td align="right">13.4%</td>
<td align="right">412,760</td>
<td align="right">10.1%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">29,511,240</td>
<td align="right">13.4%</td>
<td align="right">449,800</td>
<td align="right">11.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,085,580</td>
<td align="right">1.4%</td>
<td align="right">61,060</td>
<td align="right">1.5%</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,587,000</td>
<td align="right">2.5%</td>
<td align="right">1,710,260</td>
<td align="right">41.9%</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,013,060</td>
<td align="right">9.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">7,563,520</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,563,260</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,232,920</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">244,900</td>
<td align="right">6.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">50,900</td>
<td align="right">1.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">41,740</td>
<td align="right">1.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">26,060</td>
<td align="right">0.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">7,544,980</td>
<td align="right">4.0%</td>
<td align="right">26,520</td>
<td align="right">0.5%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">4,767,260</td>
<td align="right">2.5%</td>
<td align="right">17,600</td>
<td align="right">0.3%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">5,380,740</td>
<td align="right">2.8%</td>
<td align="right">117,660</td>
<td align="right">2.1%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">167,338,020</td>
<td align="right">88.1%</td>
<td align="right">4,847,360</td>
<td align="right">84.9%</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">167,213,980</td>
<td align="right">88.0%</td>
<td align="right">5,728,000</td>
<td align="right">100.3%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">22,496,100</td>
<td align="right">11.8%</td>
<td align="right">826,000</td>
<td align="right">14.5%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">22,494,940</td>
<td align="right">11.8%</td>
<td align="right">826,000</td>
<td align="right">14.5%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,036,700</td>
<td align="right">0.5%</td>
<td align="right">38,280</td>
<td align="right">0.7%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">864,280</td>
<td align="right">15.1%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">864,280</td>
<td align="right">15.1%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">206,880</td>
<td align="right">0.1%</td>
<td align="right">38,280</td>
<td align="right">0.7%</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache dunder hits</td>
<td align="right">110,040,718</td>
<td align="right"></td>
<td align="right">1,284,769</td>
<td align="right"></td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">105,718,960</td>
<td align="right">3.5%</td>
<td align="right">1,775,540</td>
<td align="right">1.1%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">49,879,640</td>
<td align="right">1.6%</td>
<td align="right">930,940</td>
<td align="right">0.5%</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">18,459,964</td>
<td align="right"></td>
<td align="right">422,650</td>
<td align="right"></td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">19,750,984</td>
<td align="right"></td>
<td align="right">472,202</td>
<td align="right"></td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,273,427,980</td>
<td align="right">40.1%</td>
<td align="right">40,628,600</td>
<td align="right">22.2%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,507,082</td>
<td align="right"></td>
<td align="right">49,931</td>
<td align="right"></td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">258,830,876</td>
<td align="right"></td>
<td align="right">10,136,970</td>
<td align="right"></td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">892,669,540</td>
<td align="right">29.6%</td>
<td align="right">35,012,720</td>
<td align="right">20.9%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">172,787,460</td>
<td align="right"></td>
<td align="right">9,379,220</td>
<td align="right"></td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">172,754,260</td>
<td align="right">51.3%</td>
<td align="right">9,381,180</td>
<td align="right">47.1%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,214,923,374</td>
<td align="right">40.3%</td>
<td align="right">72,963,420</td>
<td align="right">43.5%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">163,687,860</td>
<td align="right">48.6%</td>
<td align="right">10,414,680</td>
<td align="right">52.3%</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">164,207,520</td>
<td align="right">48.7%</td>
<td align="right">10,545,680</td>
<td align="right">52.9%</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">183,488,883</td>
<td align="right"></td>
<td align="right">12,528,816</td>
<td align="right"></td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">799,246,048</td>
<td align="right">26.5%</td>
<td align="right">58,054,837</td>
<td align="right">34.6%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,121,106,389</td>
<td align="right">35.3%</td>
<td align="right">84,921,320</td>
<td align="right">46.5%</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">731,512,323</td>
<td align="right">23.0%</td>
<td align="right">56,156,202</td>
<td align="right">30.7%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">203,820</td>
<td align="right">0.1%</td>
<td align="right">16,100</td>
<td align="right">0.1%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">5,524,600</td>
<td align="right"></td>
<td align="right">485,160</td>
<td align="right"></td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">72,900</td>
<td align="right">1.3%</td>
<td align="right">11,760</td>
<td align="right">2.4%</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">315,840</td>
<td align="right">0.1%</td>
<td align="right">114,900</td>
<td align="right">0.6%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.5%</td>
<td align="right">26,460</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.1%</td>
<td align="right">2,940</td>
<td align="right">0.6%</td>
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
<td align="right">15,000</td>
<td align="right">41,933,500</td>
<td align="right">681,171,258</td>
<td align="right">25,358,728</td>
<td align="right">57,991,172</td>
<td align="right">1,440</td>
<td align="right">3,407,700</td>
<td align="right">62,059,026</td>
<td align="right">2,515,000</td>
<td align="right">3,804,680</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,820</td>
<td align="right">36.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,240</td>
<td align="right">6.7%</td>
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
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">8,480</td>
<td align="right">45.8%</td>
<td align="right">240</td>
<td align="right">23.1%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">157,411,600</td>
<td align="right"></td>
<td align="right">4,747,000</td>
<td align="right"></td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,500</td>
<td align="right"></td>
<td align="right">1,040</td>
<td align="right"></td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,556,691,260</td>
<td align="right">1,624.2%</td>
<td align="right">395,582,820</td>
<td align="right">8,333.3%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">340</td>
<td align="right">1.8%</td>
<td align="right">60</td>
<td align="right">5.8%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,820</td>
<td align="right">15.2%</td>
<td align="right">680</td>
<td align="right">65.4%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">-66.7%</td>
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
<td align="right">8,480</td>
<td align="right"></td>
<td align="right">240</td>
<td align="right"></td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">5,360</td>
<td align="right">63.2%</td>
<td align="right">200</td>
<td align="right">83.3%</td>
<td align="right">-96.3%</td>
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
<td align="right">16,711,680</td>
<td align="right">30.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">43,600,060</td>
<td align="right">78.8%</td>
<td align="right">1,488,700</td>
<td align="right">72.7%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,186,720</td>
<td align="right">2.1%</td>
<td align="right">43,520</td>
<td align="right">2.1%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">55,296,000</td>
<td align="right"></td>
<td align="right">2,048,000</td>
<td align="right"></td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">10,509,220</td>
<td align="right">19.0%</td>
<td align="right">515,780</td>
<td align="right">25.2%</td>
<td align="right">-95.1%</td>
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
<td align="left">1,420</td>
<td align="right">26.5%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">2,040</td>
<td align="right">38.1%</td>
<td align="left">140</td>
<td align="right">70.0%</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1,520</td>
<td align="right">28.4%</td>
<td align="left">40</td>
<td align="right">20.0%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">300</td>
<td align="right">5.6%</td>
<td align="left">20</td>
<td align="right">10.0%</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">60</td>
<td align="right">1.1%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">20</td>
<td align="right">0.4%</td>
<td align="left"></td>
<td align="right"></td>
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
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,620</td>
<td align="right">19.1%</td>
<td align="right">20</td>
<td align="right">8.3%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,980</td>
<td align="right">35.1%</td>
<td align="right">160</td>
<td align="right">66.7%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">480</td>
<td align="right">5.7%</td>
<td align="right">20</td>
<td align="right">8.3%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,220</td>
<td align="right">38.0%</td>
<td align="right">40</td>
<td align="right">16.7%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left"><= 8</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">940</td>
<td align="right">11.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,360</td>
<td align="right">27.8%</td>
<td align="right">100</td>
<td align="right">41.7%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,600</td>
<td align="right">18.9%</td>
<td align="right">80</td>
<td align="right">33.3%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">2.1%</td>
<td align="right">20</td>
<td align="right">8.3%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">180</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">27,700</td>
<td align="right">208,600</td>
<td align="right">653.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,700</td>
<td align="right">208,600</td>
<td align="right">653.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">164,300</td>
<td align="right">640,440</td>
<td align="right">289.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">96,900</td>
<td align="right">249,900</td>
<td align="right">157.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">96,900</td>
<td align="right">249,900</td>
<td align="right">157.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,213,060</td>
<td align="right">11,760</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,181,320</td>
<td align="right">11,760</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,407,720</td>
<td align="right">35,280</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,904,040</td>
<td align="right">14,700</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">9,504,380</td>
<td align="right">182,560</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">1,322,080</td>
<td align="right">30,940</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">13,816,400</td>
<td align="right">327,880</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,302,980</td>
<td align="right">30,940</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">7,107,460</td>
<td align="right">170,800</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">21,679,680</td>
<td align="right">586,460</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">157,411,600</td>
<td align="right">4,747,000</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">157,298,240</td>
<td align="right">4,747,000</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">17,678,300</td>
<td align="right">586,460</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,272,740</td>
<td align="right">156,800</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,733,380</td>
<td align="right">249,900</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">12,815,700</td>
<td align="right">749,700</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">12,918,340</td>
<td align="right">811,240</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">28,698,600</td>
<td align="right">2,096,080</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">16,037,520</td>
<td align="right">1,236,580</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">178,656,520</td>
<td align="right">14,529,460</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">125,668,440</td>
<td align="right">10,764,900</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">6,846,540</td>
<td align="right">640,440</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">23,888,640</td>
<td align="right">2,520,660</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">9,186,200</td>
<td align="right">999,600</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">7,499,280</td>
<td align="right">827,360</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">18,591,180</td>
<td align="right">2,238,420</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">17,149,520</td>
<td align="right">2,244,300</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">6,146,320</td>
<td align="right">815,600</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">6,023,420</td>
<td align="right">815,600</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,023,420</td>
<td align="right">815,600</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,510,100</td>
<td align="right">208,600</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">19,873,140</td>
<td align="right">2,892,260</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,873,140</td>
<td align="right">2,892,260</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,584,340</td>
<td align="right">815,600</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">24,153,560</td>
<td align="right">3,566,100</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">24,145,000</td>
<td align="right">3,566,100</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">54,558,340</td>
<td align="right">8,086,620</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">5,471,100</td>
<td align="right">815,600</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">462,086,440</td>
<td align="right">71,295,640</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">50,851,660</td>
<td align="right">8,086,620</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">359,855,600</td>
<td align="right">65,354,080</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">34,859,900</td>
<td align="right">6,785,040</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">37,151,900</td>
<td align="right">7,238,600</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">107,762,480</td>
<td align="right">22,250,020</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">40,494,660</td>
<td align="right">8,866,340</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">12,211,460</td>
<td align="right">2,691,740</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,393,420</td>
<td align="right">315,600</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,351,820</td>
<td align="right">315,600</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">11,761,680</td>
<td align="right">2,820,960</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">47,036,040</td>
<td align="right">12,045,600</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">2,064,440</td>
<td align="right">3,587,760</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">16,360,240</td>
<td align="right">4,648,400</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">20,886,660</td>
<td align="right">6,152,520</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">679,880</td>
<td align="right">208,600</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">679,880</td>
<td align="right">208,600</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">675,220</td>
<td align="right">208,600</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">18,930,820</td>
<td align="right">5,902,620</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">7,058,980</td>
<td align="right">2,238,420</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,057,280</td>
<td align="right">2,238,420</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">17,878,120</td>
<td align="right">5,864,400</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">13,854,760</td>
<td align="right">4,711,900</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">19,240,160</td>
<td align="right">7,085,400</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,478,080</td>
<td align="right">2,441,840</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,422,420</td>
<td align="right">2,241,360</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,422,420</td>
<td align="right">2,241,360</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,420,800</td>
<td align="right">2,238,420</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,420,800</td>
<td align="right">2,238,420</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,461,720</td>
<td align="right">2,269,360</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,450,300</td>
<td align="right">2,238,420</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,450,300</td>
<td align="right">2,238,420</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">21,244,920</td>
<td align="right">9,782,460</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">9,508,420</td>
<td align="right">4,650,580</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">371,060</td>
<td align="right">211,680</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,420,480</td>
<td align="right">4,391,860</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">7,444,140</td>
<td align="right">4,507,780</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,602,360</td>
<td align="right">2,250,180</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,146,320</td>
<td align="right">5,775,760</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">607,440</td>
<td align="right">815,600</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">2,090,140</td>
<td align="right">2,690,960</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,870,520</td>
<td align="right">2,314,860</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">182,840</td>
<td align="right">208,600</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,007,720</td>
<td align="right">2,238,420</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,432,680</td>
<td align="right">2,690,960</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,569,900</td>
<td align="right">2,314,860</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,272,540</td>
<td align="right">2,238,420</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">13,173,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">13,173,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,173,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,815,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">11,275,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">8,320,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">8,319,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">7,626,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,536,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">6,351,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">5,805,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,853,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,755,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,469,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,721,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,897,960</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,748,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,643,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,195,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">801,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">786,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">739,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">679,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">579,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">517,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">512,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">492,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">410,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">392,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">141,840</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">113,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">80,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">77,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">77,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">61,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">43,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">43,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">43,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">31,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">29,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">27,460</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">27,460</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">21,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">21,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">21,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">10,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLER_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">208,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLER_INSTR_PTR</td>
<td align="right"></td>
<td align="right">208,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">208,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">208,600</td>
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
<td align="right">620</td>
<td align="right">60</td>
<td align="right">-90.3%</td>
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
Stats gathered on: 2025-05-29
