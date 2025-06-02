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
<td align="left">DELETE_FAST</td>
<td align="right">780</td>
<td align="right">1,620</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">207,857,040</td>
<td align="right">38,900</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,481,960</td>
<td align="right">1,340,360</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">54,288,660</td>
<td align="right">8,334,280</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">16,979,260</td>
<td align="right">2,934,420</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">20,213,100</td>
<td align="right">4,137,740</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,356,140</td>
<td align="right">3,003,960</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">18,038,860</td>
<td align="right">4,507,760</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">165,808,120</td>
<td align="right">43,685,400</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,320,200</td>
<td align="right">12,008,100</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">48,268,560</td>
<td align="right">13,953,340</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,923,140</td>
<td align="right">8,850,700</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">30,160,320</td>
<td align="right">9,409,040</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">69,498,200</td>
<td align="right">22,361,580</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">720</td>
<td align="right">240</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">300</td>
<td align="right">100</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">240</td>
<td align="right">80</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">180</td>
<td align="right">60</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">60</td>
<td align="right">20</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">52,740</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">930,780</td>
<td align="right">328,640</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">822,420</td>
<td align="right">293,900</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">4,120</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,420</td>
<td align="right">1,240</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">133,997,640</td>
<td align="right">49,229,220</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">6,734,080</td>
<td align="right">2,516,200</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,048,100</td>
<td align="right">5,355,260</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">34,035,060</td>
<td align="right">13,286,240</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">22,288,280</td>
<td align="right">8,877,400</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">91,420</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">41,723,820</td>
<td align="right">16,763,760</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,467,820</td>
<td align="right">1,418,640</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,783,840</td>
<td align="right">2,418,260</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,345,720</td>
<td align="right">6,427,980</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">104,980</td>
<td align="right">44,000</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">441,124,260</td>
<td align="right">186,923,960</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">823,380</td>
<td align="right">350,460</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">68,785,260</td>
<td align="right">29,291,140</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">50,377,980</td>
<td align="right">21,529,580</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">252,395,400</td>
<td align="right">108,464,380</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">29,646,180</td>
<td align="right">12,791,240</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,204,760</td>
<td align="right">5,309,800</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">93,395,960</td>
<td align="right">40,658,080</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,635,040</td>
<td align="right">5,594,200</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">12,400</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">253,321,740</td>
<td align="right">114,402,000</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">195,447,880</td>
<td align="right">88,300,540</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">380,940,040</td>
<td align="right">173,509,120</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">12,757,240</td>
<td align="right">5,814,400</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">223,772,120</td>
<td align="right">102,583,240</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,134,820</td>
<td align="right">520,420</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">59,118,900</td>
<td align="right">27,476,520</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">147,649,800</td>
<td align="right">68,632,360</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">22,797,240</td>
<td align="right">10,603,940</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">65,019,900</td>
<td align="right">30,526,240</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,127,440</td>
<td align="right">11,339,940</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">94,575,840</td>
<td align="right">44,569,600</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,446,646,620</td>
<td align="right">687,629,860</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">15,178,140</td>
<td align="right">7,226,040</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">351,240</td>
<td align="right">167,300</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">169,026,500</td>
<td align="right">82,001,900</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">58,019,820</td>
<td align="right">28,459,200</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,693,560</td>
<td align="right">831,560</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">22,014,720</td>
<td align="right">10,817,840</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">840,600</td>
<td align="right">415,760</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">226,034,660</td>
<td align="right">114,088,000</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,146,200</td>
<td align="right">2,611,300</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,925,500</td>
<td align="right">11,743,720</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">75,980</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">28,096,440</td>
<td align="right">14,711,220</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">317,393,940</td>
<td align="right">167,641,520</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">176,880</td>
<td align="right">93,560</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40,170,720</td>
<td align="right">21,300,080</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">309,990,880</td>
<td align="right">164,522,580</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,160,720</td>
<td align="right">9,194,120</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,840,600</td>
<td align="right">1,523,240</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">361,260</td>
<td align="right">194,380</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,401,540</td>
<td align="right">10,446,680</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">396,212,340</td>
<td align="right">214,151,620</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,917,000</td>
<td align="right">5,371,240</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">110,116,080</td>
<td align="right">59,710,040</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">41,478,100</td>
<td align="right">22,544,780</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,137,660</td>
<td align="right">10,405,620</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">123,018,540</td>
<td align="right">67,110,040</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">51,368,860</td>
<td align="right">28,178,860</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">118,705,200</td>
<td align="right">65,139,580</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,344,420</td>
<td align="right">51,239,240</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">440,400</td>
<td align="right">242,400</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,458,180</td>
<td align="right">28,874,400</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,860</td>
<td align="right">2,999,680</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,413,900</td>
<td align="right">780,100</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,888,420</td>
<td align="right">20,357,820</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,133,580</td>
<td align="right">20,500,300</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,196,260</td>
<td align="right">12,809,300</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,940,220</td>
<td align="right">4,389,420</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">179,936,980</td>
<td align="right">99,587,600</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">41,711,700</td>
<td align="right">23,133,300</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,207,900</td>
<td align="right">16,788,920</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,225,540</td>
<td align="right">16,806,560</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,918,220</td>
<td align="right">1,624,820</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,143,580</td>
<td align="right">3,424,420</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,143,580</td>
<td align="right">3,424,420</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">154,353,180</td>
<td align="right">86,067,820</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">37,483,620</td>
<td align="right">20,926,000</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,116,580</td>
<td align="right">8,442,740</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,175,460</td>
<td align="right">657,020</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,787,480</td>
<td align="right">3,237,700</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,105,440</td>
<td align="right">12,379,460</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">5,402,540</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,220,440</td>
<td align="right">1,813,340</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">53,018,640</td>
<td align="right">29,867,560</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">67,749,300</td>
<td align="right">38,217,240</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,728,440</td>
<td align="right">1,540,700</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,731,500</td>
<td align="right">1,543,680</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">130,778,340</td>
<td align="right">74,214,720</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">4,331,320</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,120</td>
<td align="right">152,440</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,146,480</td>
<td align="right">4,080,020</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,364,240</td>
<td align="right">4,782,540</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,687,720</td>
<td align="right">22,131,180</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">71,205,520</td>
<td align="right">40,799,040</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">43,779,360</td>
<td align="right">25,197,940</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,979,940</td>
<td align="right">2,872,500</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">3,360</td>
<td align="right">1,940</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,365,660</td>
<td align="right">6,601,760</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,589,220</td>
<td align="right">9,649,860</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,325,060</td>
<td align="right">3,100,340</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,446,120</td>
<td align="right">843,940</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,655,060</td>
<td align="right">5,051,760</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">2,692,900</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,202,460</td>
<td align="right">2,471,260</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">6,842,240</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,947,400</td>
<td align="right">2,332,440</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right">3,480</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,480,940</td>
<td align="right">1,481,160</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">44,260</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,461,880</td>
<td align="right">2,084,760</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,031,240</td>
<td align="right">1,229,740</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">46,020</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,105,400</td>
<td align="right">5,136,900</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">213,240</td>
<td align="right">144,220</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,885,920</td>
<td align="right">1,334,120</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">672,120</td>
<td align="right">548,540</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,920</td>
<td align="right">2,220</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">4,040</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,960</td>
<td align="right">4,440</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,680</td>
<td align="right">24,240</td>
<td align="right">-5.6%</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">51,393,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">34,910,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">1,919,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right"></td>
<td align="right">1,200</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">167,471,400</td>
<td align="right">85.6%</td>
<td align="right">80,437,020</td>
<td align="right">83.7%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">23,092,500</td>
<td align="right">11.8%</td>
<td align="right">12,748,040</td>
<td align="right">13.3%</td>
<td align="right">-44.8%</td>
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
<td align="right">2,801,060</td>
<td align="right">2.9%</td>
<td align="right">-44.4%</td>
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
<td align="right">95,800</td>
<td align="right">48.2%</td>
<td align="right">53,700</td>
<td align="right">47.1%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">102,920</td>
<td align="right">51.8%</td>
<td align="right">60,340</td>
<td align="right">52.9%</td>
<td align="right">-41.4%</td>
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
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,560</td>
<td align="right">7.3%</td>
<td align="right">4,280</td>
<td align="right">7.1%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">83,060</td>
<td align="right">80.7%</td>
<td align="right">47,880</td>
<td align="right">79.4%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,220</td>
<td align="right">3.1%</td>
<td align="right">2,020</td>
<td align="right">3.3%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">4,980</td>
<td align="right">4.8%</td>
<td align="right">3,220</td>
<td align="right">5.3%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.4%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">3.1%</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">0.2%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">12,635,040</td>
<td align="right">100.0%</td>
<td align="right">5,594,200</td>
<td align="right">100.0%</td>
<td align="right">-55.7%</td>
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
<td align="right">553,242,720</td>
<td align="right">96.9%</td>
<td align="right">258,448,100</td>
<td align="right">96.2%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">17,825,280</td>
<td align="right">3.1%</td>
<td align="right">10,223,600</td>
<td align="right">3.8%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,489,100</td>
<td align="right">3.1%</td>
<td align="right">10,031,120</td>
<td align="right">3.7%</td>
<td align="right">-42.6%</td>
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
<td align="right">340,140</td>
<td align="right">100.0%</td>
<td align="right">196,920</td>
<td align="right">100.0%</td>
<td align="right">-42.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,786,100</td>
<td align="right">94.7%</td>
<td align="right">14,439,840</td>
<td align="right">93.0%</td>
<td align="right">-58.5%</td>
</tr>
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
<td align="right">818,820</td>
<td align="right">5.3%</td>
<td align="right">-51.3%</td>
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
<td align="right">251,960</td>
<td align="right">1.6%</td>
<td align="right">-2.9%</td>
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
<td align="right">12,960</td>
<td align="right">71.3%</td>
<td align="right">12,400</td>
<td align="right">71.0%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">5,060</td>
<td align="right">29.0%</td>
<td align="right">-3.1%</td>
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
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">12,060</td>
<td align="right">97.3%</td>
<td align="right">-3.5%</td>
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
<td align="right">54,350,400</td>
<td align="right">81.7%</td>
<td align="right">8,396,020</td>
<td align="right">61.3%</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,199,080</td>
<td align="right">18.3%</td>
<td align="right">5,306,480</td>
<td align="right">38.7%</td>
<td align="right">-56.5%</td>
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
<td align="right">5,560</td>
<td align="right">97.9%</td>
<td align="right">3,200</td>
<td align="right">96.4%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.1%</td>
<td align="right">120</td>
<td align="right">3.6%</td>
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
<td align="left">str</td>
<td align="right">1,260</td>
<td align="right">22.7%</td>
<td align="right">560</td>
<td align="right">17.5%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,240</td>
<td align="right">40.3%</td>
<td align="right">1,180</td>
<td align="right">36.9%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,260</td>
<td align="right">22.7%</td>
<td align="right">860</td>
<td align="right">26.9%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">14.4%</td>
<td align="right">600</td>
<td align="right">18.8%</td>
<td align="right">-25.0%</td>
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
<td align="right">45,308,280</td>
<td align="right">13.9%</td>
<td align="right">12,004,540</td>
<td align="right">11.7%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">242,709,280</td>
<td align="right">74.5%</td>
<td align="right">75,472,140</td>
<td align="right">73.6%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,776,560</td>
<td align="right">11.6%</td>
<td align="right">15,126,780</td>
<td align="right">14.7%</td>
<td align="right">-60.0%</td>
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
<td align="right">11,920</td>
<td align="right">1.6%</td>
<td align="right">3,560</td>
<td align="right">1.2%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">712,740</td>
<td align="right">98.4%</td>
<td align="right">285,420</td>
<td align="right">98.8%</td>
<td align="right">-60.0%</td>
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
<td align="right">4,280</td>
<td align="right">35.9%</td>
<td align="right">620</td>
<td align="right">17.4%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,600</td>
<td align="right">13.4%</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,840</td>
<td align="right">15.4%</td>
<td align="right">560</td>
<td align="right">15.7%</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">780</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.7%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">20.8%</td>
<td align="right">1,180</td>
<td align="right">33.1%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">4.7%</td>
<td align="right">420</td>
<td align="right">11.8%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">5.1%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">1.1%</td>
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
<td align="right">3,900</td>
<td align="right">3,900 / 0 !!</td>
<td align="right">1,300</td>
<td align="right">1,300 / 0 !!</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,162,220</td>
<td align="right">2,162,220 / 0 !!</td>
<td align="right">779,360</td>
<td align="right">779,360 / 0 !!</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">55,380</td>
<td align="right">55,380 / 0 !!</td>
<td align="right">19,980</td>
<td align="right">19,980 / 0 !!</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">197,340</td>
<td align="right">197,340 / 0 !!</td>
<td align="right">108,360</td>
<td align="right">108,360 / 0 !!</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">36,919,140</td>
<td align="right">36,919,140 / 0 !!</td>
<td align="right">20,373,320</td>
<td align="right">20,373,320 / 0 !!</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,964,960</td>
<td align="right">5,964,960 / 0 !!</td>
<td align="right">3,310,900</td>
<td align="right">3,310,900 / 0 !!</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">48,398,760</td>
<td align="right">48,398,760 / 0 !!</td>
<td align="right">27,081,740</td>
<td align="right">27,081,740 / 0 !!</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">198,000</td>
<td align="right">198,000 / 0 !!</td>
<td align="right">112,980</td>
<td align="right">112,980 / 0 !!</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">29,118,840</td>
<td align="right">29,118,840 / 0 !!</td>
<td align="right">16,715,520</td>
<td align="right">16,715,520 / 0 !!</td>
<td align="right">-42.6%</td>
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
<td align="right">658,769,700</td>
<td align="right">59.9%</td>
<td align="right">312,775,120</td>
<td align="right">59.0%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">331,811,080</td>
<td align="right">30.1%</td>
<td align="right">157,553,020</td>
<td align="right">29.7%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,441,840</td>
<td align="right">9.9%</td>
<td align="right">59,339,400</td>
<td align="right">11.2%</td>
<td align="right">-45.8%</td>
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
<td align="right">6,201,800</td>
<td align="right">99.6%</td>
<td align="right">2,944,140</td>
<td align="right">99.5%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">22,700</td>
<td align="right">0.4%</td>
<td align="right">13,700</td>
<td align="right">0.5%</td>
<td align="right">-39.6%</td>
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
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">12.5%</td>
<td align="right">1,580</td>
<td align="right">11.5%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,600</td>
<td align="right">24.7%</td>
<td align="right">3,160</td>
<td align="right">23.1%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">11,000</td>
<td align="right">48.5%</td>
<td align="right">6,320</td>
<td align="right">46.1%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">1.8%</td>
<td align="right">260</td>
<td align="right">1.9%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">1.9%</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">2.8%</td>
<td align="right">540</td>
<td align="right">3.9%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">120</td>
<td align="right">0.9%</td>
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
<td align="right">319,428,480</td>
<td align="right">100.0%</td>
<td align="right">154,744,560</td>
<td align="right">100.0%</td>
<td align="right">-51.6%</td>
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
<td align="right">1,520</td>
<td align="right">0.0%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
<td align="right">1,960</td>
<td align="right">100.0%</td>
<td align="right">2,100</td>
<td align="right">100.0%</td>
<td align="right">7.1%</td>
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
<td align="right">46,020</td>
<td align="right">100.0%</td>
<td align="right">-39.4%</td>
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
<td align="right">53,915,340</td>
<td align="right">43.8%</td>
<td align="right">29,530,300</td>
<td align="right">43.5%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,048,360</td>
<td align="right">38.2%</td>
<td align="right">26,046,140</td>
<td align="right">38.3%</td>
<td align="right">-44.6%</td>
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
<td align="right">12,370,200</td>
<td align="right">18.2%</td>
<td align="right">-44.0%</td>
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
<td align="right">1,017,780</td>
<td align="right">98.7%</td>
<td align="right">557,720</td>
<td align="right">98.4%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,980</td>
<td align="right">1.3%</td>
<td align="right">8,840</td>
<td align="right">1.6%</td>
<td align="right">-31.9%</td>
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
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">6,300</td>
<td align="right">71.3%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,000</td>
<td align="right">7.7%</td>
<td align="right">780</td>
<td align="right">8.8%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">2,020</td>
<td align="right">22.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right"></td>
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
<td align="right">152,440</td>
<td align="right">100.0%</td>
<td align="right">-42.9%</td>
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
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
<td align="right">17,178,580</td>
<td align="right">86.4%</td>
<td align="right">-59.6%</td>
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
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">-57.7%</td>
</tr>
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
<td align="right">2,690,200</td>
<td align="right">13.5%</td>
<td align="right">-41.3%</td>
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
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">2,580</td>
<td align="right">94.9%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">140</td>
<td align="right">5.1%</td>
<td align="right">-12.5%</td>
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
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">620</td>
<td align="right">24.0%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">140</td>
<td align="right">5.4%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">1,780</td>
<td align="right">69.0%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.6%</td>
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
<td align="right">269,417,840</td>
<td align="right">94.6%</td>
<td align="right">125,067,220</td>
<td align="right">94.1%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">11,378,560</td>
<td align="right">4.0%</td>
<td align="right">5,492,300</td>
<td align="right">4.1%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,779,500</td>
<td align="right">1.3%</td>
<td align="right">2,233,720</td>
<td align="right">1.7%</td>
<td align="right">-40.9%</td>
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
<td align="right">215,540</td>
<td align="right">56.3%</td>
<td align="right">104,680</td>
<td align="right">51.7%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,000</td>
<td align="right">43.7%</td>
<td align="right">97,720</td>
<td align="right">48.3%</td>
<td align="right">-41.5%</td>
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
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">1,340</td>
<td align="right">1.4%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">70,160</td>
<td align="right">71.8%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">25,080</td>
<td align="right">25.7%</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">1,020</td>
<td align="right">1.0%</td>
<td align="right">-15.0%</td>
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
<td align="right">13,958,760</td>
<td align="right">100.0%</td>
<td align="right">-71.1%</td>
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
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">-44.9%</td>
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
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">3,025,519,680</td>
<td align="right">36.2%</td>
<td align="right">1,319,982,380</td>
<td align="right">33.2%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">458,014,640</td>
<td align="right">5.5%</td>
<td align="right">220,987,340</td>
<td align="right">5.6%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">4,520,455,940</td>
<td align="right">54.1%</td>
<td align="right">2,253,136,260</td>
<td align="right">56.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">359,098,620</td>
<td align="right">4.3%</td>
<td align="right">180,937,540</td>
<td align="right">4.6%</td>
<td align="right">-49.6%</td>
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
<td align="right">45,308,280</td>
<td align="right">17.9%</td>
<td align="right">12,004,540</td>
<td align="right">9.7%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,199,080</td>
<td align="right">4.8%</td>
<td align="right">5,306,480</td>
<td align="right">4.3%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,635,040</td>
<td align="right">5.0%</td>
<td align="right">5,594,200</td>
<td align="right">4.5%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,680,260</td>
<td align="right">0.7%</td>
<td align="right">818,820</td>
<td align="right">0.7%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">109,441,840</td>
<td align="right">43.3%</td>
<td align="right">59,339,400</td>
<td align="right">48.1%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,092,500</td>
<td align="right">9.1%</td>
<td align="right">12,748,040</td>
<td align="right">10.3%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,092,060</td>
<td align="right">8.7%</td>
<td align="right">12,370,200</td>
<td align="right">10.0%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,489,100</td>
<td align="right">6.9%</td>
<td align="right">10,031,120</td>
<td align="right">8.1%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">1.8%</td>
<td align="right">2,690,200</td>
<td align="right">2.2%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,779,500</td>
<td align="right">1.5%</td>
<td align="right">2,233,720</td>
<td align="right">1.8%</td>
<td align="right">-40.9%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,888,680</td>
<td align="right">4.1%</td>
<td align="right">7,563,260</td>
<td align="right">3.4%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">18,887,880</td>
<td align="right">4.1%</td>
<td align="right">7,563,520</td>
<td align="right">3.4%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">132,973,760</td>
<td align="right">29.0%</td>
<td align="right">56,680,280</td>
<td align="right">25.6%</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,609,520</td>
<td align="right">22.0%</td>
<td align="right">45,861,800</td>
<td align="right">20.8%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,154,400</td>
<td align="right">1.3%</td>
<td align="right">3,085,580</td>
<td align="right">1.4%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,160</td>
<td align="right">11.8%</td>
<td align="right">29,529,240</td>
<td align="right">13.4%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">1.7%</td>
<td align="right">4,232,920</td>
<td align="right">1.9%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,301,900</td>
<td align="right">7.7%</td>
<td align="right">20,013,060</td>
<td align="right">9.1%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">51,720,400</td>
<td align="right">11.3%</td>
<td align="right">29,511,240</td>
<td align="right">13.4%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,690,140</td>
<td align="right">2.1%</td>
<td align="right">5,587,000</td>
<td align="right">2.5%</td>
<td align="right">-42.3%</td>
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
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,800,840</td>
<td align="right">88.8%</td>
<td align="right">167,338,020</td>
<td align="right">88.1%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,603,660</td>
<td align="right">88.5%</td>
<td align="right">167,213,980</td>
<td align="right">88.0%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,630,620</td>
<td align="right">3.8%</td>
<td align="right">7,544,980</td>
<td align="right">4.0%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">9,607,200</td>
<td align="right">2.7%</td>
<td align="right">5,380,740</td>
<td align="right">2.8%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">4,767,260</td>
<td align="right">2.5%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">1,036,700</td>
<td align="right">0.5%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,386,960</td>
<td align="right">11.1%</td>
<td align="right">22,496,100</td>
<td align="right">11.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,383,480</td>
<td align="right">11.1%</td>
<td align="right">22,494,940</td>
<td align="right">11.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,730,100</td>
<td align="right">11.2%</td>
<td align="right">22,702,980</td>
<td align="right">11.9%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">343,140</td>
<td align="right">0.1%</td>
<td align="right">206,880</td>
<td align="right">0.1%</td>
<td align="right">-39.7%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">2,721,990</td>
<td align="right"></td>
<td align="right">1,338,625</td>
<td align="right"></td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">34,324,535</td>
<td align="right"></td>
<td align="right">17,846,182</td>
<td align="right"></td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,285,635</td>
<td align="right"></td>
<td align="right">18,968,091</td>
<td align="right"></td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,543,020</td>
<td align="right"></td>
<td align="right">5,524,600</td>
<td align="right"></td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">218,136,320</td>
<td align="right">4.1%</td>
<td align="right">119,172,900</td>
<td align="right">4.0%</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,462,056,860</td>
<td align="right">44.0%</td>
<td align="right">1,348,556,420</td>
<td align="right">43.2%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,725,759,460</td>
<td align="right">32.6%</td>
<td align="right">947,896,900</td>
<td align="right">32.0%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">470,232,905</td>
<td align="right"></td>
<td align="right">259,444,658</td>
<td align="right"></td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,314,200</td>
<td align="right">1.6%</td>
<td align="right">49,920,840</td>
<td align="right">1.6%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">197,955,290</td>
<td align="right"></td>
<td align="right">110,209,175</td>
<td align="right"></td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,300,810,856</td>
<td align="right">23.3%</td>
<td align="right">730,676,894</td>
<td align="right">23.4%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">326,627,869</td>
<td align="right"></td>
<td align="right">183,488,440</td>
<td align="right"></td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">306,912,700</td>
<td align="right">51.4%</td>
<td align="right">172,754,500</td>
<td align="right">51.3%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">306,954,840</td>
<td align="right"></td>
<td align="right">172,787,700</td>
<td align="right"></td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,962,958,664</td>
<td align="right">37.1%</td>
<td align="right">1,107,530,171</td>
<td align="right">37.4%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">289,826,520</td>
<td align="right">48.5%</td>
<td align="right">163,687,620</td>
<td align="right">48.6%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">290,658,000</td>
<td align="right">48.6%</td>
<td align="right">164,207,280</td>
<td align="right">48.7%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,381,782,729</td>
<td align="right">26.1%</td>
<td align="right">784,668,446</td>
<td align="right">26.5%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,739,892,934</td>
<td align="right">31.1%</td>
<td align="right">993,811,880</td>
<td align="right">31.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,040</td>
<td align="right">0.1%</td>
<td align="right">203,820</td>
<td align="right">0.1%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">72,900</td>
<td align="right">1.3%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">487,440</td>
<td align="right">0.1%</td>
<td align="right">315,840</td>
<td align="right">0.1%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">26,460</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">2,940</td>
<td align="right">0.1%</td>
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
<td align="right">25,880</td>
<td align="right">72,901,980</td>
<td align="right">1,167,480,871</td>
<td align="right">43,440,686</td>
<td align="right">102,096,534</td>
<td align="right">15,000</td>
<td align="right">41,933,500</td>
<td align="right">681,191,873</td>
<td align="right">25,351,918</td>
<td align="right">57,998,902</td>
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
Stats gathered on: 2025-06-02
