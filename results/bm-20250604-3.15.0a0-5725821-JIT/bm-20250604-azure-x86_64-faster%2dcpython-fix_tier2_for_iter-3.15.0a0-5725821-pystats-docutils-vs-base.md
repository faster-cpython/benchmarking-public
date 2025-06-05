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
<td align="left">STORE_NAME</td>
<td align="right">240</td>
<td align="right">720</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">100</td>
<td align="right">300</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">80</td>
<td align="right">240</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">60</td>
<td align="right">180</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">20</td>
<td align="right">60</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">52,740</td>
<td align="right">156,900</td>
<td align="right">197.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">4,120</td>
<td align="right">11,400</td>
<td align="right">176.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,240</td>
<td align="right">3,420</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">328,640</td>
<td align="right">848,400</td>
<td align="right">158.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">293,900</td>
<td align="right">740,040</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">91,420</td>
<td align="right">228,720</td>
<td align="right">150.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,418,260</td>
<td align="right">5,783,840</td>
<td align="right">139.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,516,200</td>
<td align="right">5,657,940</td>
<td align="right">124.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">12,400</td>
<td align="right">27,480</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">520,420</td>
<td align="right">1,134,820</td>
<td align="right">118.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">350,460</td>
<td align="right">759,540</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">12,791,240</td>
<td align="right">27,604,200</td>
<td align="right">115.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,877,400</td>
<td align="right">19,104,120</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">167,300</td>
<td align="right">351,240</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">44,000</td>
<td align="right">91,560</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,603,940</td>
<td align="right">21,819,540</td>
<td align="right">105.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">831,560</td>
<td align="right">1,693,560</td>
<td align="right">103.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,340,360</td>
<td align="right">2,715,440</td>
<td align="right">102.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">415,760</td>
<td align="right">840,600</td>
<td align="right">102.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,594,200</td>
<td align="right">11,238,460</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,611,300</td>
<td align="right">5,137,740</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">88,300,520</td>
<td align="right">173,156,640</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">102,583,260</td>
<td align="right">200,179,900</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">11,743,720</td>
<td align="right">22,890,460</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,919,840</td>
<td align="right">3,682,800</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">75,980</td>
<td align="right">145,320</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">10,817,840</td>
<td align="right">20,552,380</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40,658,080</td>
<td align="right">76,879,380</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">93,560</td>
<td align="right">176,880</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,418,640</td>
<td align="right">2,681,080</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">12,008,100</td>
<td align="right">22,673,000</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">9,409,040</td>
<td align="right">17,618,860</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">164,522,580</td>
<td align="right">308,012,400</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">167,641,500</td>
<td align="right">313,606,800</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">82,001,920</td>
<td align="right">153,352,920</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">8,334,280</td>
<td align="right">15,560,100</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,523,240</td>
<td align="right">2,840,600</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">173,509,120</td>
<td align="right">323,428,980</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,194,120</td>
<td align="right">17,096,880</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">194,380</td>
<td align="right">361,260</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,427,980</td>
<td align="right">11,940,660</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">10,446,680</td>
<td align="right">19,369,800</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,371,240</td>
<td align="right">9,917,000</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,934,420</td>
<td align="right">5,416,320</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">114,402,020</td>
<td align="right">211,088,280</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,229,220</td>
<td align="right">90,658,800</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,405,620</td>
<td align="right">19,073,340</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">13,953,340</td>
<td align="right">25,572,740</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">687,629,800</td>
<td align="right">1,259,589,040</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">114,088,020</td>
<td align="right">208,261,160</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,526,240</td>
<td align="right">55,698,740</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">51,239,240</td>
<td align="right">93,251,600</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">242,400</td>
<td align="right">440,400</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,999,680</td>
<td align="right">5,440,860</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">780,100</td>
<td align="right">1,413,900</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">20,357,820</td>
<td align="right">36,888,420</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">20,500,300</td>
<td align="right">37,133,580</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">7,226,040</td>
<td align="right">13,085,260</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,809,300</td>
<td align="right">23,175,200</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">44,569,620</td>
<td align="right">80,459,320</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">23,133,300</td>
<td align="right">41,711,700</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">21,300,080</td>
<td align="right">38,363,500</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214,151,620</td>
<td align="right">385,091,620</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">27,476,520</td>
<td align="right">49,381,580</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,137,740</td>
<td align="right">7,435,980</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,389,420</td>
<td align="right">7,886,640</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,624,820</td>
<td align="right">2,918,220</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">67,110,040</td>
<td align="right">120,457,160</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">108,464,400</td>
<td align="right">194,613,620</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,424,420</td>
<td align="right">6,143,580</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,424,420</td>
<td align="right">6,143,580</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">99,587,600</td>
<td align="right">178,630,980</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,711,220</td>
<td align="right">26,378,180</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,178,860</td>
<td align="right">50,497,520</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">16,788,920</td>
<td align="right">30,074,760</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">16,806,560</td>
<td align="right">30,092,400</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">8,442,740</td>
<td align="right">15,116,580</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">28,874,400</td>
<td align="right">51,693,980</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">657,020</td>
<td align="right">1,175,460</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">21,529,580</td>
<td align="right">38,514,380</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,237,700</td>
<td align="right">5,787,480</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,286,240</td>
<td align="right">23,748,920</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,710,040</td>
<td align="right">106,669,060</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,339,940</td>
<td align="right">20,251,020</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">12,379,460</td>
<td align="right">22,105,440</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">65,139,580</td>
<td align="right">116,240,820</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">34,910,340</td>
<td align="right">62,204,280</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">86,067,820</td>
<td align="right">153,288,940</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">5,402,540</td>
<td align="right">9,619,980</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,814,400</td>
<td align="right">10,329,800</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,813,340</td>
<td align="right">3,220,440</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">68,632,360</td>
<td align="right">121,851,300</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,850,700</td>
<td align="right">15,691,340</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,867,560</td>
<td align="right">52,937,140</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,540,700</td>
<td align="right">2,728,440</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,543,680</td>
<td align="right">2,731,500</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">186,923,980</td>
<td align="right">330,641,220</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">43,685,400</td>
<td align="right">77,036,100</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">22,544,780</td>
<td align="right">39,736,120</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,355,260</td>
<td align="right">9,436,500</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">74,214,720</td>
<td align="right">130,600,360</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">4,331,320</td>
<td align="right">7,613,400</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,507,760</td>
<td align="right">7,914,260</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">152,440</td>
<td align="right">267,120</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">20,926,000</td>
<td align="right">36,659,980</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">4,080,020</td>
<td align="right">7,146,480</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,782,540</td>
<td align="right">8,364,240</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">51,393,760</td>
<td align="right">89,874,580</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">22,131,180</td>
<td align="right">38,687,720</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,003,960</td>
<td align="right">5,239,160</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">38,217,240</td>
<td align="right">66,267,440</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">2,872,500</td>
<td align="right">4,979,940</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">16,763,760</td>
<td align="right">29,039,060</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,197,940</td>
<td align="right">43,648,560</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,940</td>
<td align="right">3,360</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">28,459,180</td>
<td align="right">49,234,660</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,799,040</td>
<td align="right">70,568,040</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,601,760</td>
<td align="right">11,362,660</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,100,340</td>
<td align="right">5,325,060</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">29,291,140</td>
<td align="right">50,233,340</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,649,860</td>
<td align="right">16,539,060</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">843,940</td>
<td align="right">1,443,200</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">5,051,760</td>
<td align="right">8,607,300</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,692,900</td>
<td align="right">4,587,740</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,471,260</td>
<td align="right">4,202,460</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">6,842,240</td>
<td align="right">11,627,520</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,332,440</td>
<td align="right">3,947,400</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,480</td>
<td align="right">5,880</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">22,361,620</td>
<td align="right">37,749,500</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,481,160</td>
<td align="right">2,480,940</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">44,260</td>
<td align="right">73,620</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,309,800</td>
<td align="right">8,786,180</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,229,740</td>
<td align="right">2,031,240</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">46,020</td>
<td align="right">75,960</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">2,084,760</td>
<td align="right">3,425,140</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,620</td>
<td align="right">780</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,136,900</td>
<td align="right">7,666,220</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">144,220</td>
<td align="right">213,240</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,334,120</td>
<td align="right">1,885,920</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">548,540</td>
<td align="right">672,120</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,040</td>
<td align="right">4,740</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,220</td>
<td align="right">1,920</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,440</td>
<td align="right">3,960</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">38,900</td>
<td align="right">41,340</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">24,240</td>
<td align="right">25,680</td>
<td align="right">5.9%</td>
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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">89,943,520</td>
<td align="right">85.2%</td>
<td align="right">167,471,400</td>
<td align="right">85.6%</td>
<td align="right">86.2%</td>
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
<td align="right">23,071,460</td>
<td align="right">11.8%</td>
<td align="right">81.0%</td>
</tr>
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
<td align="right">5,034,880</td>
<td align="right">2.6%</td>
<td align="right">79.7%</td>
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
<td align="right">95,800</td>
<td align="right">48.2%</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60,340</td>
<td align="right">52.9%</td>
<td align="right">102,900</td>
<td align="right">51.8%</td>
<td align="right">70.5%</td>
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
<td align="left">subscr</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">4,280</td>
<td align="right">7.1%</td>
<td align="right">7,560</td>
<td align="right">7.3%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">47,880</td>
<td align="right">79.4%</td>
<td align="right">83,060</td>
<td align="right">80.7%</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,020</td>
<td align="right">3.3%</td>
<td align="right">3,200</td>
<td align="right">3.1%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,220</td>
<td align="right">5.3%</td>
<td align="right">4,980</td>
<td align="right">4.8%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">220</td>
<td align="right">0.4%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">3,160</td>
<td align="right">3.1%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.2%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">5,594,200</td>
<td align="right">100.0%</td>
<td align="right">11,238,460</td>
<td align="right">100.0%</td>
<td align="right">100.9%</td>
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
<td align="right">553,252,940</td>
<td align="right">96.9%</td>
<td align="right">84.9%</td>
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
<td align="right">17,812,360</td>
<td align="right">3.1%</td>
<td align="right">74.2%</td>
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
<td align="right">17,476,420</td>
<td align="right">3.1%</td>
<td align="right">74.2%</td>
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
<td align="right">339,900</td>
<td align="right">100.0%</td>
<td align="right">72.6%</td>
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
<td align="right">818,820</td>
<td align="right">4.0%</td>
<td align="right">1,680,260</td>
<td align="right">4.6%</td>
<td align="right">105.2%</td>
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
<td align="right">34,786,100</td>
<td align="right">94.7%</td>
<td align="right">78.9%</td>
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
<td align="right">259,420</td>
<td align="right">0.7%</td>
<td align="right">3.0%</td>
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
<td align="right">12,960</td>
<td align="right">71.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,060</td>
<td align="right">29.0%</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">3.2%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,060</td>
<td align="right">97.3%</td>
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">3.6%</td>
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
<td align="left">long float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
<td align="right">67.0%</td>
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
<td align="right">8,781,340</td>
<td align="right">13.9%</td>
<td align="right">65.5%</td>
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
<td align="right">3,200</td>
<td align="right">96.4%</td>
<td align="right">4,720</td>
<td align="right">97.5%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">3.6%</td>
<td align="right">120</td>
<td align="right">2.5%</td>
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
<td align="right">1,180</td>
<td align="right">36.9%</td>
<td align="right">1,880</td>
<td align="right">39.8%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">560</td>
<td align="right">17.5%</td>
<td align="right">860</td>
<td align="right">18.2%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">860</td>
<td align="right">26.9%</td>
<td align="right">1,180</td>
<td align="right">25.0%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">600</td>
<td align="right">18.8%</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">33.3%</td>
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
<td align="right">12,004,540</td>
<td align="right">11.7%</td>
<td align="right">22,666,660</td>
<td align="right">12.5%</td>
<td align="right">88.8%</td>
</tr>
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
<td align="right">26,635,380</td>
<td align="right">14.6%</td>
<td align="right">76.1%</td>
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
<td align="right">132,543,000</td>
<td align="right">72.9%</td>
<td align="right">75.6%</td>
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
<td align="right">3,560</td>
<td align="right">1.2%</td>
<td align="right">6,340</td>
<td align="right">1.2%</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">285,420</td>
<td align="right">98.8%</td>
<td align="right">502,540</td>
<td align="right">98.8%</td>
<td align="right">76.1%</td>
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
<td align="right">620</td>
<td align="right">17.4%</td>
<td align="right">1,380</td>
<td align="right">21.8%</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right">500</td>
<td align="right">7.9%</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,180</td>
<td align="right">33.1%</td>
<td align="right">2,120</td>
<td align="right">33.4%</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">560</td>
<td align="right">15.7%</td>
<td align="right">1,000</td>
<td align="right">15.8%</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right">400</td>
<td align="right">6.3%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">420</td>
<td align="right">11.8%</td>
<td align="right">560</td>
<td align="right">8.8%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">5.1%</td>
<td align="right">220</td>
<td align="right">3.5%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
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
<td align="left">dict keys</td>
<td align="right">1,300</td>
<td align="right">1,300 / 0 !!</td>
<td align="right">3,900</td>
<td align="right">3,900 / 0 !!</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">779,360</td>
<td align="right">779,360 / 0 !!</td>
<td align="right">2,162,220</td>
<td align="right">2,162,220 / 0 !!</td>
<td align="right">177.4%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">19,980</td>
<td align="right">19,980 / 0 !!</td>
<td align="right">55,380</td>
<td align="right">55,380 / 0 !!</td>
<td align="right">177.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">108,360</td>
<td align="right">108,360 / 0 !!</td>
<td align="right">197,340</td>
<td align="right">197,340 / 0 !!</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">20,373,320</td>
<td align="right">20,373,320 / 0 !!</td>
<td align="right">36,919,140</td>
<td align="right">36,919,140 / 0 !!</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,310,900</td>
<td align="right">3,310,900 / 0 !!</td>
<td align="right">5,964,960</td>
<td align="right">5,964,960 / 0 !!</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">27,081,740</td>
<td align="right">27,081,740 / 0 !!</td>
<td align="right">48,398,760</td>
<td align="right">48,398,760 / 0 !!</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">112,980</td>
<td align="right">112,980 / 0 !!</td>
<td align="right">198,000</td>
<td align="right">198,000 / 0 !!</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">16,715,520</td>
<td align="right">16,715,520 / 0 !!</td>
<td align="right">29,118,840</td>
<td align="right">29,118,840 / 0 !!</td>
<td align="right">74.2%</td>
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
<td align="right">347,951,220</td>
<td align="right">61.6%</td>
<td align="right">641,964,740</td>
<td align="right">62.1%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">157,555,140</td>
<td align="right">27.9%</td>
<td align="right">284,618,120</td>
<td align="right">27.5%</td>
<td align="right">80.6%</td>
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
<td align="right">106,010,220</td>
<td align="right">10.3%</td>
<td align="right">78.7%</td>
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
<td align="right">2,944,180</td>
<td align="right">99.5%</td>
<td align="right">5,311,620</td>
<td align="right">99.6%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,700</td>
<td align="right">0.5%</td>
<td align="right">22,040</td>
<td align="right">0.4%</td>
<td align="right">60.9%</td>
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
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">140.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,580</td>
<td align="right">11.5%</td>
<td align="right">2,840</td>
<td align="right">12.9%</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,320</td>
<td align="right">46.1%</td>
<td align="right">10,980</td>
<td align="right">49.8%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,160</td>
<td align="right">23.1%</td>
<td align="right">4,960</td>
<td align="right">22.5%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">260</td>
<td align="right">1.9%</td>
<td align="right">400</td>
<td align="right">1.8%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">420</td>
<td align="right">1.9%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">540</td>
<td align="right">3.9%</td>
<td align="right">640</td>
<td align="right">2.9%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.9%</td>
<td align="right">120</td>
<td align="right">0.5%</td>
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
<td align="right">154,744,580</td>
<td align="right">100.0%</td>
<td align="right">285,138,400</td>
<td align="right">100.0%</td>
<td align="right">84.3%</td>
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
<td align="right">2,140</td>
<td align="right">0.0%</td>
<td align="right">40.8%</td>
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
<td align="right">1,960</td>
<td align="right">100.0%</td>
<td align="right">-6.7%</td>
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
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">65.1%</td>
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
<td align="right">53,883,280</td>
<td align="right">43.8%</td>
<td align="right">82.5%</td>
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
<td align="right">47,079,840</td>
<td align="right">38.3%</td>
<td align="right">80.6%</td>
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
<td align="right">22,092,060</td>
<td align="right">18.0%</td>
<td align="right">78.6%</td>
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
<td align="right">1,017,200</td>
<td align="right">98.7%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,840</td>
<td align="right">1.6%</td>
<td align="right">12,980</td>
<td align="right">1.3%</td>
<td align="right">46.8%</td>
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
<td align="left">property</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">6,300</td>
<td align="right">71.3%</td>
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">780</td>
<td align="right">8.8%</td>
<td align="right">1,000</td>
<td align="right">7.7%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,020</td>
<td align="right">22.9%</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
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
<td align="right">152,440</td>
<td align="right">100.0%</td>
<td align="right">267,120</td>
<td align="right">100.0%</td>
<td align="right">75.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">136.2%</td>
</tr>
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
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
<td align="right">75.3%</td>
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
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
<td align="right">70.4%</td>
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
<td align="right">2,580</td>
<td align="right">94.9%</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">140</td>
<td align="right">5.1%</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">14.3%</td>
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
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">140</td>
<td align="right">5.4%</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">1,780</td>
<td align="right">69.0%</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">136,871,280</td>
<td align="right">94.6%</td>
<td align="right">255,003,400</td>
<td align="right">94.7%</td>
<td align="right">86.3%</td>
</tr>
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
<td align="right">10,186,400</td>
<td align="right">3.8%</td>
<td align="right">85.5%</td>
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
<td align="right">3,779,500</td>
<td align="right">1.4%</td>
<td align="right">69.2%</td>
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
<td align="right">193,060</td>
<td align="right">53.6%</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97,720</td>
<td align="right">48.3%</td>
<td align="right">167,000</td>
<td align="right">46.4%</td>
<td align="right">70.9%</td>
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
<td align="left">mapping</td>
<td align="right">1,340</td>
<td align="right">1.4%</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">70,160</td>
<td align="right">71.8%</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">25,080</td>
<td align="right">25.7%</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,020</td>
<td align="right">1.0%</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">17.6%</td>
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
<td align="right">26,170,220</td>
<td align="right">100.0%</td>
<td align="right">48,300,460</td>
<td align="right">100.0%</td>
<td align="right">84.6%</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">81.4%</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">11.8%</td>
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
<td align="right">1,319,980,480</td>
<td align="right">33.2%</td>
<td align="right">2,443,193,960</td>
<td align="right">33.8%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,253,136,240</td>
<td align="right">56.7%</td>
<td align="right">4,069,495,560</td>
<td align="right">56.2%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">220,989,360</td>
<td align="right">5.6%</td>
<td align="right">398,444,680</td>
<td align="right">5.5%</td>
<td align="right">80.3%</td>
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
<td align="right">325,606,800</td>
<td align="right">4.5%</td>
<td align="right">80.0%</td>
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
<td align="right">818,820</td>
<td align="right">0.7%</td>
<td align="right">1,680,260</td>
<td align="right">0.8%</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,594,200</td>
<td align="right">4.5%</td>
<td align="right">11,238,460</td>
<td align="right">5.1%</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">12,004,540</td>
<td align="right">9.7%</td>
<td align="right">22,666,660</td>
<td align="right">10.2%</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,748,040</td>
<td align="right">10.3%</td>
<td align="right">23,071,460</td>
<td align="right">10.4%</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,339,400</td>
<td align="right">48.1%</td>
<td align="right">106,010,220</td>
<td align="right">47.8%</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">12,370,200</td>
<td align="right">10.0%</td>
<td align="right">22,092,060</td>
<td align="right">10.0%</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">10,031,120</td>
<td align="right">8.1%</td>
<td align="right">17,476,420</td>
<td align="right">7.9%</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,690,200</td>
<td align="right">2.2%</td>
<td align="right">4,583,860</td>
<td align="right">2.1%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,233,720</td>
<td align="right">1.8%</td>
<td align="right">3,779,500</td>
<td align="right">1.7%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,306,480</td>
<td align="right">4.3%</td>
<td align="right">8,781,340</td>
<td align="right">4.0%</td>
<td align="right">65.5%</td>
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
<td align="right">45,863,920</td>
<td align="right">20.8%</td>
<td align="right">84,422,460</td>
<td align="right">21.2%</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">29,529,240</td>
<td align="right">13.4%</td>
<td align="right">53,880,100</td>
<td align="right">13.5%</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">56,680,280</td>
<td align="right">25.6%</td>
<td align="right">103,178,540</td>
<td align="right">25.9%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,085,580</td>
<td align="right">1.4%</td>
<td align="right">5,551,520</td>
<td align="right">1.4%</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,232,920</td>
<td align="right">1.9%</td>
<td align="right">7,565,220</td>
<td align="right">1.9%</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,013,060</td>
<td align="right">9.1%</td>
<td align="right">35,301,900</td>
<td align="right">8.9%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,563,260</td>
<td align="right">3.4%</td>
<td align="right">13,317,720</td>
<td align="right">3.3%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">7,563,520</td>
<td align="right">3.4%</td>
<td align="right">13,317,660</td>
<td align="right">3.3%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">29,511,240</td>
<td align="right">13.4%</td>
<td align="right">51,557,000</td>
<td align="right">12.9%</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,587,000</td>
<td align="right">2.5%</td>
<td align="right">9,677,220</td>
<td align="right">2.4%</td>
<td align="right">73.2%</td>
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
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">167,338,020</td>
<td align="right">88.1%</td>
<td align="right">314,800,840</td>
<td align="right">88.8%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">167,213,980</td>
<td align="right">88.0%</td>
<td align="right">313,603,660</td>
<td align="right">88.5%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">7,544,980</td>
<td align="right">4.0%</td>
<td align="right">13,630,620</td>
<td align="right">3.8%</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">5,380,740</td>
<td align="right">2.8%</td>
<td align="right">9,607,200</td>
<td align="right">2.7%</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">4,767,260</td>
<td align="right">2.5%</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,036,700</td>
<td align="right">0.5%</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">22,496,100</td>
<td align="right">11.8%</td>
<td align="right">39,386,960</td>
<td align="right">11.1%</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">22,494,940</td>
<td align="right">11.8%</td>
<td align="right">39,383,480</td>
<td align="right">11.1%</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">206,880</td>
<td align="right">0.1%</td>
<td align="right">343,140</td>
<td align="right">0.1%</td>
<td align="right">65.9%</td>
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
<td align="left">Inline values</td>
<td align="right">5,524,600</td>
<td align="right"></td>
<td align="right">10,543,020</td>
<td align="right"></td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">892,667,440</td>
<td align="right">29.6%</td>
<td align="right">1,635,872,920</td>
<td align="right">30.6%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,273,428,000</td>
<td align="right">40.1%</td>
<td align="right">2,328,055,980</td>
<td align="right">41.2%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">49,879,640</td>
<td align="right">1.6%</td>
<td align="right">90,190,600</td>
<td align="right">1.6%</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">105,718,960</td>
<td align="right">3.5%</td>
<td align="right">191,014,100</td>
<td align="right">3.6%</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">109,979,511</td>
<td align="right"></td>
<td align="right">198,326,789</td>
<td align="right"></td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">258,164,209</td>
<td align="right"></td>
<td align="right">460,303,056</td>
<td align="right"></td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">172,754,220</td>
<td align="right">51.3%</td>
<td align="right">306,871,080</td>
<td align="right">51.4%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">183,488,533</td>
<td align="right"></td>
<td align="right">325,927,269</td>
<td align="right"></td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">172,787,420</td>
<td align="right"></td>
<td align="right">306,871,520</td>
<td align="right"></td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">163,687,900</td>
<td align="right">48.6%</td>
<td align="right">289,871,320</td>
<td align="right">48.5%</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">164,207,560</td>
<td align="right">48.7%</td>
<td align="right">290,712,440</td>
<td align="right">48.6%</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">732,199,083</td>
<td align="right">23.0%</td>
<td align="right">1,290,934,887</td>
<td align="right">22.8%</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,215,699,181</td>
<td align="right">40.3%</td>
<td align="right">2,126,999,443</td>
<td align="right">39.7%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">800,250,566</td>
<td align="right">26.5%</td>
<td align="right">1,397,485,792</td>
<td align="right">26.1%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,121,879,697</td>
<td align="right">35.3%</td>
<td align="right">1,946,813,063</td>
<td align="right">34.4%</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">19,128,771</td>
<td align="right"></td>
<td align="right">32,730,104</td>
<td align="right"></td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">203,820</td>
<td align="right">0.1%</td>
<td align="right">344,940</td>
<td align="right">0.1%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">20,480,469</td>
<td align="right"></td>
<td align="right">34,317,279</td>
<td align="right"></td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">72,900</td>
<td align="right">1.3%</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">315,840</td>
<td align="right">0.1%</td>
<td align="right">496,180</td>
<td align="right">0.1%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,568,289</td>
<td align="right"></td>
<td align="right">2,348,371</td>
<td align="right"></td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.5%</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.1%</td>
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
<td align="right">15,000</td>
<td align="right">41,933,500</td>
<td align="right">681,174,339</td>
<td align="right">25,359,154</td>
<td align="right">57,991,206</td>
<td align="right">25,900</td>
<td align="right">72,479,460</td>
<td align="right">1,167,711,437</td>
<td align="right">43,540,762</td>
<td align="right">102,045,618</td>
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
<td align="right">180</td>
<td align="right">0.5%</td>
<td align="right">350.0%</td>
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
<td align="right">280</td>
<td align="right">0.9%</td>
<td align="right">133.3%</td>
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
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
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
<td align="right">2,320</td>
<td align="right">7.1%</td>
<td align="right">87.1%</td>
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
<td align="right">15,400</td>
<td align="right">46.9%</td>
<td align="right">81.6%</td>
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
<td align="right">32,840</td>
<td align="right"></td>
<td align="right">77.5%</td>
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
<td align="right">11,940</td>
<td align="right">36.4%</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,556,691,860</td>
<td align="right">1,624.2%</td>
<td align="right">4,425,119,460</td>
<td align="right">1,625.4%</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">157,411,660</td>
<td align="right"></td>
<td align="right">272,244,180</td>
<td align="right"></td>
<td align="right">73.0%</td>
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
<td align="right">4,760</td>
<td align="right">14.5%</td>
<td align="right">68.8%</td>
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
<td align="right">560</td>
<td align="right">1.7%</td>
<td align="right">64.7%</td>
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
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
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
<td align="right">15,400</td>
<td align="right"></td>
<td align="right">81.6%</td>
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
<td align="right">9,700</td>
<td align="right">63.0%</td>
<td align="right">81.0%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">43,600,060</td>
<td align="right">78.8%</td>
<td align="right">84,149,580</td>
<td align="right">79.9%</td>
<td align="right">93.0%</td>
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
<td align="right">105,349,120</td>
<td align="right"></td>
<td align="right">90.5%</td>
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
<td align="right">2,202,240</td>
<td align="right">2.1%</td>
<td align="right">85.6%</td>
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
<td align="right">18,997,300</td>
<td align="right">18.0%</td>
<td align="right">80.8%</td>
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
<td align="right">16,711,680</td>
<td align="right">30.2%</td>
<td align="right">16,711,680</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
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
<td align="left">2,600</td>
<td align="right">26.8%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">2,040</td>
<td align="right">38.1%</td>
<td align="left">3,500</td>
<td align="right">36.1%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1,520</td>
<td align="right">28.4%</td>
<td align="left">2,640</td>
<td align="right">27.2%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">300</td>
<td align="right">5.6%</td>
<td align="left">740</td>
<td align="right">7.6%</td>
<td align="right">146.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">60</td>
<td align="right">1.1%</td>
<td align="left">180</td>
<td align="right">1.9%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">20</td>
<td align="right">0.4%</td>
<td align="left">40</td>
<td align="right">0.4%</td>
<td align="right">100.0%</td>
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
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,620</td>
<td align="right">19.1%</td>
<td align="right">2,960</td>
<td align="right">19.2%</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,980</td>
<td align="right">35.1%</td>
<td align="right">5,020</td>
<td align="right">32.6%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">480</td>
<td align="right">5.7%</td>
<td align="right">940</td>
<td align="right">6.1%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,220</td>
<td align="right">38.0%</td>
<td align="right">6,040</td>
<td align="right">39.2%</td>
<td align="right">87.6%</td>
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
<td align="left"><= 1,024</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">100.0%</td>
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
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">940</td>
<td align="right">11.1%</td>
<td align="right">1,700</td>
<td align="right">11.0%</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,360</td>
<td align="right">27.8%</td>
<td align="right">4,140</td>
<td align="right">26.9%</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,600</td>
<td align="right">18.9%</td>
<td align="right">2,740</td>
<td align="right">17.8%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">2.1%</td>
<td align="right">520</td>
<td align="right">3.4%</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">180</td>
<td align="right">2.1%</td>
<td align="right">400</td>
<td align="right">2.6%</td>
<td align="right">122.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">133.3%</td>
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
<td align="right">92,240</td>
<td align="right">233.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,700</td>
<td align="right">92,240</td>
<td align="right">233.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">80,580</td>
<td align="right">241,740</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">27,460</td>
<td align="right">82,380</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">27,460</td>
<td align="right">82,380</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">21,280</td>
<td align="right">63,840</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">21,280</td>
<td align="right">63,840</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">21,520</td>
<td align="right">64,320</td>
<td align="right">198.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">675,220</td>
<td align="right">1,978,480</td>
<td align="right">193.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">43,340</td>
<td align="right">126,540</td>
<td align="right">192.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,721,400</td>
<td align="right">7,624,300</td>
<td align="right">180.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">29,500</td>
<td align="right">81,500</td>
<td align="right">176.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">679,880</td>
<td align="right">1,741,980</td>
<td align="right">156.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">679,880</td>
<td align="right">1,741,980</td>
<td align="right">156.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">679,880</td>
<td align="right">1,741,980</td>
<td align="right">156.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,469,700</td>
<td align="right">8,646,620</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,755,700</td>
<td align="right">11,562,940</td>
<td align="right">143.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">512,080</td>
<td align="right">1,223,800</td>
<td align="right">139.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">410,420</td>
<td align="right">977,700</td>
<td align="right">138.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">6,351,760</td>
<td align="right">14,766,520</td>
<td align="right">132.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">392,580</td>
<td align="right">878,320</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,536,220</td>
<td align="right">14,566,700</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">371,060</td>
<td align="right">797,740</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,510,100</td>
<td align="right">3,226,300</td>
<td align="right">113.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,643,160</td>
<td align="right">3,417,740</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,195,620</td>
<td align="right">2,462,440</td>
<td align="right">106.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">10,300</td>
<td align="right">21,040</td>
<td align="right">104.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">240</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">240</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,897,960</td>
<td align="right">3,787,140</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">11,761,680</td>
<td align="right">23,106,820</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,478,080</td>
<td align="right">12,541,460</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">16,037,520</td>
<td align="right">30,496,080</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">739,880</td>
<td align="right">1,396,580</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,272,740</td>
<td align="right">8,018,560</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,853,720</td>
<td align="right">9,029,460</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">786,440</td>
<td align="right">1,462,340</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">12,211,460</td>
<td align="right">22,666,060</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">579,900</td>
<td align="right">1,076,200</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">9,504,380</td>
<td align="right">17,627,460</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">7,626,200</td>
<td align="right">14,114,060</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,393,420</td>
<td align="right">2,561,380</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">28,698,600</td>
<td align="right">52,318,860</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,351,820</td>
<td align="right">2,464,380</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">5,471,100</td>
<td align="right">9,908,200</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">17,878,120</td>
<td align="right">32,372,140</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,584,340</td>
<td align="right">10,109,900</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">20,886,660</td>
<td align="right">37,754,320</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">18,930,820</td>
<td align="right">34,143,260</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,407,720</td>
<td align="right">9,737,320</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">7,499,280</td>
<td align="right">13,445,980</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">5,805,860</td>
<td align="right">10,395,560</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,904,040</td>
<td align="right">3,405,060</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">13,816,400</td>
<td align="right">24,689,860</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">7,107,460</td>
<td align="right">12,684,760</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">113,340</td>
<td align="right">201,920</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">17,678,300</td>
<td align="right">31,464,160</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">19,873,140</td>
<td align="right">35,236,480</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,873,140</td>
<td align="right">35,236,480</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,815,880</td>
<td align="right">20,935,220</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">12,918,340</td>
<td align="right">22,822,320</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">16,360,240</td>
<td align="right">28,893,640</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,733,380</td>
<td align="right">10,124,600</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,181,320</td>
<td align="right">3,844,680</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">13,173,180</td>
<td align="right">23,162,340</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">13,173,180</td>
<td align="right">23,162,340</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,173,180</td>
<td align="right">23,162,340</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">21,244,920</td>
<td align="right">37,346,920</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,213,060</td>
<td align="right">3,876,420</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">54,558,340</td>
<td align="right">95,482,200</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">359,855,640</td>
<td align="right">628,955,840</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">12,815,700</td>
<td align="right">22,386,200</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">462,086,520</td>
<td align="right">806,232,980</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">18,591,180</td>
<td align="right">32,419,000</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">50,851,660</td>
<td align="right">88,381,160</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">17,149,520</td>
<td align="right">29,805,040</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">178,656,580</td>
<td align="right">309,591,100</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">6,846,540</td>
<td align="right">11,863,600</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">157,411,660</td>
<td align="right">272,244,180</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">157,298,320</td>
<td align="right">272,042,260</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">107,762,480</td>
<td align="right">185,815,840</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">1,322,080</td>
<td align="right">2,276,900</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">11,275,220</td>
<td align="right">19,375,200</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">21,679,720</td>
<td align="right">37,245,960</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">7,444,140</td>
<td align="right">12,777,120</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">77,600</td>
<td align="right">133,140</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">77,600</td>
<td align="right">133,140</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">34,859,900</td>
<td align="right">59,701,020</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">6,023,420</td>
<td align="right">10,286,140</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,023,420</td>
<td align="right">10,286,140</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">6,146,320</td>
<td align="right">10,454,320</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">8,320,880</td>
<td align="right">14,141,360</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">125,668,460</td>
<td align="right">213,498,480</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">8,319,520</td>
<td align="right">14,132,960</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">9,186,200</td>
<td align="right">15,497,180</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">37,151,920</td>
<td align="right">62,614,460</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">40,494,660</td>
<td align="right">68,081,260</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">141,840</td>
<td align="right">238,340</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">47,036,060</td>
<td align="right">77,967,620</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">23,888,660</td>
<td align="right">39,164,220</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,748,300</td>
<td align="right">2,839,680</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">96,900</td>
<td align="right">36,740</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">182,840</td>
<td align="right">295,040</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,302,980</td>
<td align="right">2,092,880</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">24,153,560</td>
<td align="right">38,728,560</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">24,145,000</td>
<td align="right">38,702,880</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">492,720</td>
<td align="right">788,900</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">19,240,180</td>
<td align="right">30,387,900</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">13,854,760</td>
<td align="right">21,569,540</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">7,058,980</td>
<td align="right">10,946,520</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,057,280</td>
<td align="right">10,912,980</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">96,900</td>
<td align="right">50,160</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,420,800</td>
<td align="right">766,440</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">61,420</td>
<td align="right">89,300</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,420,480</td>
<td align="right">10,767,260</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,420,800</td>
<td align="right">782,360</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,422,420</td>
<td align="right">786,740</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,422,420</td>
<td align="right">786,740</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">9,508,420</td>
<td align="right">13,690,780</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,450,300</td>
<td align="right">823,640</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,146,320</td>
<td align="right">13,061,080</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,461,720</td>
<td align="right">845,540</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,450,300</td>
<td align="right">839,560</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">2,064,440</td>
<td align="right">1,481,860</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,602,360</td>
<td align="right">4,611,600</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,569,900</td>
<td align="right">3,184,160</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">43,780</td>
<td align="right">53,580</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">43,780</td>
<td align="right">53,580</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,007,720</td>
<td align="right">1,718,260</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">517,620</td>
<td align="right">577,720</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">607,440</td>
<td align="right">669,260</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">2,090,140</td>
<td align="right">1,882,960</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,870,520</td>
<td align="right">2,041,980</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">801,880</td>
<td align="right">871,340</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,272,540</td>
<td align="right">2,372,480</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,432,680</td>
<td align="right">2,427,440</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">164,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">31,740</td>
<td align="right">31,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">47,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">47,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">18,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">16,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">15,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">13,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">5,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">2,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">2,920</td>
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
<td align="right">1,040</td>
<td align="right">67.7%</td>
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
Stats gathered on: 2025-06-05
