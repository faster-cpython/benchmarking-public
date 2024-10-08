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
<td align="right">425,980</td>
<td align="right">233,337,300</td>
<td align="right">54,676.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">593,040</td>
<td align="right">18,971,320</td>
<td align="right">3,099.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">192,560</td>
<td align="right">5,295,920</td>
<td align="right">2,650.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">7,368,060</td>
<td align="right">70,338,240</td>
<td align="right">854.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,605,020</td>
<td align="right">50,325,860</td>
<td align="right">797.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">8,682,440</td>
<td align="right">65,475,860</td>
<td align="right">654.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,313,280</td>
<td align="right">90,761,280</td>
<td align="right">637.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,003,300</td>
<td align="right">20,603,360</td>
<td align="right">586.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,100</td>
<td align="right">491,940</td>
<td align="right">492.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">32,829,040</td>
<td align="right">193,424,680</td>
<td align="right">489.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,592,940</td>
<td align="right">23,776,260</td>
<td align="right">417.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,796,380</td>
<td align="right">7,799,200</td>
<td align="right">334.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">458,480</td>
<td align="right">1,777,140</td>
<td align="right">287.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,226,320</td>
<td align="right">47,201,900</td>
<td align="right">286.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,831,620</td>
<td align="right">68,493,780</td>
<td align="right">284.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,612,340</td>
<td align="right">170,943,280</td>
<td align="right">244.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,471,700</td>
<td align="right">81,710,100</td>
<td align="right">233.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">28,581,480</td>
<td align="right">88,835,920</td>
<td align="right">210.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,234,700</td>
<td align="right">6,866,980</td>
<td align="right">207.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">417,860</td>
<td align="right">1,213,220</td>
<td align="right">190.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,234,380</td>
<td align="right">58,406,940</td>
<td align="right">188.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,908,980</td>
<td align="right">35,361,700</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">591,320</td>
<td align="right">1,605,340</td>
<td align="right">171.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">8,160</td>
<td align="right">21,840</td>
<td align="right">167.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,131,660</td>
<td align="right">44,580,100</td>
<td align="right">160.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">436,220</td>
<td align="right">1,120,820</td>
<td align="right">156.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,473,540</td>
<td align="right">13,712,800</td>
<td align="right">150.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">229,101,480</td>
<td align="right">571,542,960</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,720</td>
<td align="right">9,000</td>
<td align="right">141.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,049,120</td>
<td align="right">67,047,340</td>
<td align="right">139.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,712,620</td>
<td align="right">94,012,160</td>
<td align="right">136.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,800,820</td>
<td align="right">25,141,800</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,153,960</td>
<td align="right">26,843,100</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,920,940</td>
<td align="right">34,795,160</td>
<td align="right">118.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">13,065,360</td>
<td align="right">27,848,660</td>
<td align="right">113.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">188,422,380</td>
<td align="right">387,524,780</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">144,755,400</td>
<td align="right">289,436,360</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">248,416,440</td>
<td align="right">489,750,780</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">165,070,220</td>
<td align="right">322,626,160</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">148,688,020</td>
<td align="right">289,930,180</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">557,280</td>
<td align="right">1,082,120</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">287,936,860</td>
<td align="right">20,708,380</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,098,180</td>
<td align="right">15,545,940</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,806,120</td>
<td align="right">5,342,900</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">97,420</td>
<td align="right">179,640</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">118,826,340</td>
<td align="right">218,827,480</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">95,714,740</td>
<td align="right">173,642,180</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,205,420</td>
<td align="right">7,607,460</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,782,760</td>
<td align="right">65,527,540</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,116,820</td>
<td align="right">34,042,660</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,980,280</td>
<td align="right">15,976,600</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">13,891,500</td>
<td align="right">24,670,400</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">69,524,020</td>
<td align="right">122,930,420</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,185,382,840</td>
<td align="right">2,056,161,560</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,361,900</td>
<td align="right">2,356,200</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,569,600</td>
<td align="right">19,989,760</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,409,400</td>
<td align="right">2,392,500</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">148,948,120</td>
<td align="right">252,434,140</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">45,234,160</td>
<td align="right">76,204,580</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">115,526,560</td>
<td align="right">186,600,520</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">231,867,100</td>
<td align="right">374,102,040</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">261,943,500</td>
<td align="right">411,101,300</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">104,640,260</td>
<td align="right">163,742,840</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">41,304,460</td>
<td align="right">64,473,960</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,426,760</td>
<td align="right">31,801,740</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,630,020</td>
<td align="right">27,364,380</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">76,257,060</td>
<td align="right">117,956,920</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">51,160,200</td>
<td align="right">78,607,400</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">93,069,060</td>
<td align="right">141,650,080</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,168,900</td>
<td align="right">3,293,660</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,158,240</td>
<td align="right">22,693,640</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1,380</td>
<td align="right">2,060</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,729,520</td>
<td align="right">20,261,100</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,995,300</td>
<td align="right">8,832,200</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,054,120</td>
<td align="right">28,880,120</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">674,980</td>
<td align="right">965,600</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,885,660</td>
<td align="right">29,546,100</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">39,263,780</td>
<td align="right">55,454,120</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">24,803,520</td>
<td align="right">34,172,640</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,973,180</td>
<td align="right">2,714,620</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,236,800</td>
<td align="right">7,194,560</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">77,900</td>
<td align="right">106,680</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">809,440</td>
<td align="right">1,104,540</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,019,140</td>
<td align="right">10,807,940</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">705,560</td>
<td align="right">939,840</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,820</td>
<td align="right">10,340</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,153,920</td>
<td align="right">10,567,580</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,678,280</td>
<td align="right">7,291,820</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,753,840</td>
<td align="right">14,939,420</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">20,200</td>
<td align="right">25,420</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,091,880</td>
<td align="right">3,861,980</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,491,660</td>
<td align="right">4,298,460</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">510,300</td>
<td align="right">602,360</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,555,000</td>
<td align="right">13,552,500</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">22,891,640</td>
<td align="right">25,738,320</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,014,080</td>
<td align="right">5,603,640</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">49,232,620</td>
<td align="right">55,021,340</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">255,975,160</td>
<td align="right">285,585,900</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">278,680</td>
<td align="right">310,680</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,124,360</td>
<td align="right">1,250,860</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">27,469,280</td>
<td align="right">30,540,820</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,701,140</td>
<td align="right">1,528,560</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">4,056,960</td>
<td align="right">4,460,620</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">37,287,740</td>
<td align="right">40,213,380</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">37,289,460</td>
<td align="right">40,215,100</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">49,705,560</td>
<td align="right">53,079,560</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,707,320</td>
<td align="right">193,545,420</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">18,995,060</td>
<td align="right">20,118,960</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">117,762,680</td>
<td align="right">124,725,000</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36,600</td>
<td align="right">38,520</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,175,920</td>
<td align="right">1,234,620</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">3,615,380</td>
<td align="right">3,792,420</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">11,410,120</td>
<td align="right">11,752,520</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">210,984,120</td>
<td align="right">215,988,940</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,386,820</td>
<td align="right">21,874,000</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,559,780</td>
<td align="right">12,838,900</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">479,560</td>
<td align="right">484,720</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">51,215,940</td>
<td align="right">51,673,220</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,626,820</td>
<td align="right">3,641,940</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">3,631,560</td>
<td align="right">3,646,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">9,509,520</td>
<td align="right">9,522,900</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">49,483,140</td>
<td align="right">49,488,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">49,182,620</td>
<td align="right">49,182,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">15,519,420</td>
<td align="right">15,519,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,150,520</td>
<td align="right">10,150,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">7,717,040</td>
<td align="right">7,717,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,607,040</td>
<td align="right">6,607,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,885,520</td>
<td align="right">1,885,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,567,560</td>
<td align="right">1,567,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">316,640</td>
<td align="right">316,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">237,500</td>
<td align="right">237,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">217,520</td>
<td align="right">217,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">201,000</td>
<td align="right">201,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">130,660</td>
<td align="right">130,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">109,540</td>
<td align="right">109,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">96,860</td>
<td align="right">96,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">94,860</td>
<td align="right">94,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">91,680</td>
<td align="right">91,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">62,360</td>
<td align="right">62,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">36,640</td>
<td align="right">36,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">36,440</td>
<td align="right">36,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">32,180</td>
<td align="right">32,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,020</td>
<td align="right">20,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">15,660</td>
<td align="right">15,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,800</td>
<td align="right">13,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,980</td>
<td align="right">11,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">9,040</td>
<td align="right">9,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">7,340</td>
<td align="right">7,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">6,900</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">6,100</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,300</td>
<td align="right">4,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
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
<td align="right">12,116,040</td>
<td align="right">15.7%</td>
<td align="right">26,801,080</td>
<td align="right">29.1%</td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,230,660</td>
<td align="right">84.3%</td>
<td align="right">65,230,660</td>
<td align="right">70.8%</td>
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
<td align="right">30,940</td>
<td align="right">81.6%</td>
<td align="right">35,040</td>
<td align="right">83.4%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,980</td>
<td align="right">18.4%</td>
<td align="right">6,980</td>
<td align="right">16.6%</td>
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
<td align="right">7,360</td>
<td align="right">23.8%</td>
<td align="right">11,160</td>
<td align="right">31.8%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">260</td>
<td align="right">0.7%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,180</td>
<td align="right">3.8%</td>
<td align="right">1,260</td>
<td align="right">3.6%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,500</td>
<td align="right">4.8%</td>
<td align="right">1,520</td>
<td align="right">4.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,200</td>
<td align="right">29.7%</td>
<td align="right">9,280</td>
<td align="right">26.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,700</td>
<td align="right">34.6%</td>
<td align="right">10,760</td>
<td align="right">30.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">2.1%</td>
<td align="right">660</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">17,630,020</td>
<td align="right">100.0%</td>
<td align="right">27,364,380</td>
<td align="right">100.0%</td>
<td align="right">55.2%</td>
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
<td align="right">564,600</td>
<td align="right">0.4%</td>
<td align="right">1,581,740</td>
<td align="right">1.2%</td>
<td align="right">180.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,046,560</td>
<td align="right">2.3%</td>
<td align="right">3,074,080</td>
<td align="right">2.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">126,122,040</td>
<td align="right">97.2%</td>
<td align="right">126,118,960</td>
<td align="right">96.4%</td>
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
<td align="left">Failure</td>
<td align="right">15,420</td>
<td align="right">18.4%</td>
<td align="right">12,300</td>
<td align="right">15.1%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,500</td>
<td align="right">81.6%</td>
<td align="right">69,020</td>
<td align="right">84.9%</td>
<td align="right">0.8%</td>
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
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">14,180</td>
<td align="right">92.0%</td>
<td align="right">11,040</td>
<td align="right">89.8%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160</td>
<td align="right">7.5%</td>
<td align="right">1,160</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">19,190,900</td>
<td align="right">2.5%</td>
<td align="right">23,103,780</td>
<td align="right">3.0%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">745,587,600</td>
<td align="right">97.5%</td>
<td align="right">740,681,880</td>
<td align="right">97.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">71,480</td>
<td align="right">0.0%</td>
<td align="right">71,480</td>
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
<td align="right">423,540</td>
<td align="right">100.0%</td>
<td align="right">497,380</td>
<td align="right">100.0%</td>
<td align="right">17.4%</td>
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
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
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
<td align="right">3,600</td>
<td align="right">52.2%</td>
<td align="right">3,600</td>
<td align="right">52.2%</td>
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
<td align="right">1,393,460</td>
<td align="right">2.8%</td>
<td align="right">2,371,500</td>
<td align="right">4.8%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140,640</td>
<td align="right">0.3%</td>
<td align="right">193,380</td>
<td align="right">0.4%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,360,220</td>
<td align="right">96.8%</td>
<td align="right">47,260,560</td>
<td align="right">94.8%</td>
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
<td align="right">10,380</td>
<td align="right">55.9%</td>
<td align="right">15,400</td>
<td align="right">62.6%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,200</td>
<td align="right">44.1%</td>
<td align="right">9,220</td>
<td align="right">37.4%</td>
<td align="right">12.4%</td>
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
<td align="right">8,060</td>
<td align="right">77.6%</td>
<td align="right">13,060</td>
<td align="right">84.8%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">320</td>
<td align="right">3.1%</td>
<td align="right">340</td>
<td align="right">2.2%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">720</td>
<td align="right">6.9%</td>
<td align="right">720</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">660</td>
<td align="right">6.4%</td>
<td align="right">660</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">3.5%</td>
<td align="right">360</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">5,457,620</td>
<td align="right">7.0%</td>
<td align="right">13,694,080</td>
<td align="right">15.8%</td>
<td align="right">150.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,826,620</td>
<td align="right">93.0%</td>
<td align="right">72,826,620</td>
<td align="right">84.2%</td>
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
<td align="right">14,180</td>
<td align="right">89.1%</td>
<td align="right">16,980</td>
<td align="right">90.7%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,740</td>
<td align="right">10.9%</td>
<td align="right">1,740</td>
<td align="right">9.3%</td>
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
<td align="right">3,160</td>
<td align="right">22.3%</td>
<td align="right">4,420</td>
<td align="right">26.0%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,520</td>
<td align="right">17.8%</td>
<td align="right">3,020</td>
<td align="right">17.8%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,580</td>
<td align="right">39.4%</td>
<td align="right">6,620</td>
<td align="right">39.0%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,920</td>
<td align="right">20.6%</td>
<td align="right">2,920</td>
<td align="right">17.2%</td>
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
<td align="right">5,592,080</td>
<td align="right">5.2%</td>
<td align="right">50,301,720</td>
<td align="right">12.9%</td>
<td align="right">799.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,352,260</td>
<td align="right">5.9%</td>
<td align="right">49,802,080</td>
<td align="right">12.7%</td>
<td align="right">684.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">94,807,900</td>
<td align="right">88.8%</td>
<td align="right">291,197,080</td>
<td align="right">74.4%</td>
<td align="right">207.1%</td>
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
<td align="right">124,380</td>
<td align="right">93.7%</td>
<td align="right">944,160</td>
<td align="right">98.0%</td>
<td align="right">659.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,360</td>
<td align="right">6.3%</td>
<td align="right">19,560</td>
<td align="right">2.0%</td>
<td align="right">134.0%</td>
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
<td align="left">dict values</td>
<td align="right">640</td>
<td align="right">7.7%</td>
<td align="right">3,720</td>
<td align="right">19.0%</td>
<td align="right">481.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">260</td>
<td align="right">3.1%</td>
<td align="right">1,180</td>
<td align="right">6.0%</td>
<td align="right">353.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,520</td>
<td align="right">18.2%</td>
<td align="right">5,640</td>
<td align="right">28.8%</td>
<td align="right">271.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">520</td>
<td align="right">6.2%</td>
<td align="right">1,860</td>
<td align="right">9.5%</td>
<td align="right">257.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,800</td>
<td align="right">21.5%</td>
<td align="right">3,420</td>
<td align="right">17.5%</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">120</td>
<td align="right">1.4%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">23.7%</td>
<td align="right">2,040</td>
<td align="right">10.4%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">860</td>
<td align="right">10.3%</td>
<td align="right">860</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">2.4%</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">180</td>
<td align="right">2.2%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">1.7%</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">1.4%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">177,880,040</td>
<td align="right">15.8%</td>
<td align="right">439,161,560</td>
<td align="right">30.1%</td>
<td align="right">146.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">92,148,560</td>
<td align="right">8.2%</td>
<td align="right">140,714,300</td>
<td align="right">9.6%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">853,981,320</td>
<td align="right">75.9%</td>
<td align="right">878,802,740</td>
<td align="right">60.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
<td align="right">4,242,680</td>
<td align="right">99.4%</td>
<td align="right">9,175,160</td>
<td align="right">99.6%</td>
<td align="right">116.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">27,400</td>
<td align="right">0.6%</td>
<td align="right">40,060</td>
<td align="right">0.4%</td>
<td align="right">46.2%</td>
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
<td align="right">6,160</td>
<td align="right">22.5%</td>
<td align="right">16,440</td>
<td align="right">41.0%</td>
<td align="right">166.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">500</td>
<td align="right">1.8%</td>
<td align="right">580</td>
<td align="right">1.4%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,160</td>
<td align="right">7.9%</td>
<td align="right">2,500</td>
<td align="right">6.2%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">10,400</td>
<td align="right">38.0%</td>
<td align="right">11,880</td>
<td align="right">29.7%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,300</td>
<td align="right">4.7%</td>
<td align="right">1,360</td>
<td align="right">3.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,160</td>
<td align="right">15.2%</td>
<td align="right">4,160</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">940</td>
<td align="right">3.4%</td>
<td align="right">940</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">540</td>
<td align="right">2.0%</td>
<td align="right">540</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">260</td>
<td align="right">0.9%</td>
<td align="right">260</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">120</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">400</td>
<td align="right">1.0%</td>
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
<td align="right">224,916,380</td>
<td align="right">100.0%</td>
<td align="right">407,858,400</td>
<td align="right">100.0%</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,560</td>
<td align="right">0.0%</td>
<td align="right">31,560</td>
<td align="right">0.0%</td>
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
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
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
<td align="right">28,700</td>
<td align="right">0.0%</td>
<td align="right">28,700</td>
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
<td align="right">31,380</td>
<td align="right">100.0%</td>
<td align="right">31,380</td>
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
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">109,980</td>
<td align="right">99.8%</td>
<td align="right">109,980</td>
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
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">1.8%</td>
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
<td align="right">9,620</td>
<td align="right">97.4%</td>
<td align="right">9,620</td>
<td align="right">97.4%</td>
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
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">25.0%</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,843,280</td>
<td align="right">13.5%</td>
<td align="right">29,501,400</td>
<td align="right">17.9%</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">69,256,760</td>
<td align="right">44.7%</td>
<td align="right">71,862,460</td>
<td align="right">43.6%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,811,360</td>
<td align="right">41.8%</td>
<td align="right">63,488,080</td>
<td align="right">38.5%</td>
<td align="right">-2.0%</td>
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
<td align="right">32,440</td>
<td align="right">2.4%</td>
<td align="right">34,760</td>
<td align="right">2.5%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,316,000</td>
<td align="right">97.6%</td>
<td align="right">1,365,180</td>
<td align="right">97.5%</td>
<td align="right">3.7%</td>
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
<td align="right">22,180</td>
<td align="right">68.4%</td>
<td align="right">24,480</td>
<td align="right">70.4%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,480</td>
<td align="right">7.6%</td>
<td align="right">2,500</td>
<td align="right">7.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,420</td>
<td align="right">19.8%</td>
<td align="right">6,420</td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">460</td>
<td align="right">1.4%</td>
<td align="right">460</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">380</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">360</td>
<td align="right">1.1%</td>
<td align="right">360</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
<td align="right">0.5%</td>
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
<td align="right">192,560</td>
<td align="right">100.0%</td>
<td align="right">5,295,920</td>
<td align="right">100.0%</td>
<td align="right">2,650.3%</td>
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
<td align="right">1,164,960</td>
<td align="right">2.0%</td>
<td align="right">1,223,480</td>
<td align="right">2.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,859,000</td>
<td align="right">98.0%</td>
<td align="right">56,859,000</td>
<td align="right">97.9%</td>
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
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">8,740</td>
<td align="right">79.5%</td>
<td align="right">8,920</td>
<td align="right">79.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,260</td>
<td align="right">20.5%</td>
<td align="right">2,260</td>
<td align="right">20.2%</td>
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
<td align="left">bytearray int</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">540</td>
<td align="right">6.1%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">720</td>
<td align="right">8.2%</td>
<td align="right">780</td>
<td align="right">8.7%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,380</td>
<td align="right">84.4%</td>
<td align="right">7,380</td>
<td align="right">82.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.5%</td>
<td align="right">220</td>
<td align="right">2.5%</td>
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
<td align="right">5,085,580</td>
<td align="right">1.4%</td>
<td align="right">15,091,400</td>
<td align="right">4.0%</td>
<td align="right">196.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,693,480</td>
<td align="right">0.8%</td>
<td align="right">5,100,500</td>
<td align="right">1.3%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">349,920,820</td>
<td align="right">97.8%</td>
<td align="right">357,825,740</td>
<td align="right">94.6%</td>
<td align="right">2.3%</td>
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
<td align="right">111,420</td>
<td align="right">53.6%</td>
<td align="right">300,180</td>
<td align="right">57.0%</td>
<td align="right">169.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">96,380</td>
<td align="right">46.4%</td>
<td align="right">226,040</td>
<td align="right">43.0%</td>
<td align="right">134.5%</td>
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
<td align="right">32,540</td>
<td align="right">33.8%</td>
<td align="right">160,140</td>
<td align="right">70.8%</td>
<td align="right">392.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,020</td>
<td align="right">2.1%</td>
<td align="right">2,600</td>
<td align="right">1.2%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">54,760</td>
<td align="right">56.8%</td>
<td align="right">56,120</td>
<td align="right">24.8%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">6,420</td>
<td align="right">6.7%</td>
<td align="right">6,520</td>
<td align="right">2.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">set</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,640,680</td>
<td align="right">100.0%</td>
<td align="right">64,639,560</td>
<td align="right">100.0%</td>
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
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,680</td>
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
<td align="right">3,700</td>
<td align="right">100.0%</td>
<td align="right">3,740</td>
<td align="right">100.0%</td>
<td align="right">1.1%</td>
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
<td align="right">280,996,060</td>
<td align="right">4.6%</td>
<td align="right">602,511,140</td>
<td align="right">5.8%</td>
<td align="right">114.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">161,200,280</td>
<td align="right">2.6%</td>
<td align="right">305,521,300</td>
<td align="right">2.9%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,918,341,280</td>
<td align="right">31.5%</td>
<td align="right">3,574,407,500</td>
<td align="right">34.4%</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,733,216,740</td>
<td align="right">61.3%</td>
<td align="right">5,920,374,260</td>
<td align="right">56.9%</td>
<td align="right">58.6%</td>
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
<td align="right">5,592,080</td>
<td align="right">3.5%</td>
<td align="right">50,301,720</td>
<td align="right">16.5%</td>
<td align="right">799.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">564,600</td>
<td align="right">0.4%</td>
<td align="right">1,581,740</td>
<td align="right">0.5%</td>
<td align="right">180.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,457,620</td>
<td align="right">3.4%</td>
<td align="right">13,694,080</td>
<td align="right">4.5%</td>
<td align="right">150.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,116,040</td>
<td align="right">7.6%</td>
<td align="right">26,801,080</td>
<td align="right">8.8%</td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,693,480</td>
<td align="right">1.7%</td>
<td align="right">5,100,500</td>
<td align="right">1.7%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,393,460</td>
<td align="right">0.9%</td>
<td align="right">2,371,500</td>
<td align="right">0.8%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,630,020</td>
<td align="right">11.0%</td>
<td align="right">27,364,380</td>
<td align="right">9.0%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">92,148,560</td>
<td align="right">57.6%</td>
<td align="right">140,714,300</td>
<td align="right">46.3%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,843,280</td>
<td align="right">13.0%</td>
<td align="right">29,501,400</td>
<td align="right">9.7%</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,164,960</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5,295,920</td>
<td align="right">1.7%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,174,860</td>
<td align="right">1.1%</td>
<td align="right">24,900,840</td>
<td align="right">4.1%</td>
<td align="right">684.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,177,400</td>
<td align="right">1.1%</td>
<td align="right">24,901,240</td>
<td align="right">4.1%</td>
<td align="right">683.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">11,869,840</td>
<td align="right">4.2%</td>
<td align="right">46,104,200</td>
<td align="right">7.6%</td>
<td align="right">288.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">50,472,680</td>
<td align="right">18.0%</td>
<td align="right">132,792,400</td>
<td align="right">22.0%</td>
<td align="right">163.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,896,880</td>
<td align="right">26.3%</td>
<td align="right">176,355,040</td>
<td align="right">29.3%</td>
<td align="right">138.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">30,005,740</td>
<td align="right">10.7%</td>
<td align="right">69,049,320</td>
<td align="right">11.5%</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,706,420</td>
<td align="right">3.5%</td>
<td align="right">12,244,320</td>
<td align="right">2.0%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">69,252,520</td>
<td align="right">24.6%</td>
<td align="right">71,858,220</td>
<td align="right">11.9%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,804,580</td>
<td align="right">3.5%</td>
<td align="right">10,094,740</td>
<td align="right">1.7%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,856,240</td>
<td align="right">1.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">8,108,380</td>
<td align="right">1.3%</td>
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
<td align="right">10,968,980</td>
<td align="right">2.3%</td>
<td align="right">11,253,680</td>
<td align="right">2.4%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">52,188,960</td>
<td align="right">11.0%</td>
<td align="right">52,646,240</td>
<td align="right">11.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">52,200,860</td>
<td align="right">11.0%</td>
<td align="right">52,658,140</td>
<td align="right">11.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">53,076,060</td>
<td align="right">11.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">53,076,060</td>
<td align="right">11.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">421,180,760</td>
<td align="right">88.9%</td>
<td align="right">420,723,480</td>
<td align="right">88.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">419,473,100</td>
<td align="right">88.5%</td>
<td align="right">419,300,520</td>
<td align="right">88.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
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
<td align="right">704,660</td>
<td align="right">0.1%</td>
<td align="right">1,340,440</td>
<td align="right">0.1%</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">5,046,775,447</td>
<td align="right">55.2%</td>
<td align="right">2,501,024,749</td>
<td align="right">32.1%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">5,486,771,389</td>
<td align="right">65.7%</td>
<td align="right">2,853,488,300</td>
<td align="right">40.8%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">2,860,458,840</td>
<td align="right">34.3%</td>
<td align="right">4,147,124,220</td>
<td align="right">59.2%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">4,096,254,180</td>
<td align="right">44.8%</td>
<td align="right">5,297,569,920</td>
<td align="right">67.9%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">43,673,440</td>
<td align="right"></td>
<td align="right">41,112,476</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">45,763,363</td>
<td align="right"></td>
<td align="right">43,326,436</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,899,643</td>
<td align="right"></td>
<td align="right">3,024,060</td>
<td align="right"></td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">254,570,577</td>
<td align="right"></td>
<td align="right">264,728,140</td>
<td align="right"></td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">464,480</td>
<td align="right">0.0%</td>
<td align="right">467,740</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">633,907,700</td>
<td align="right"></td>
<td align="right">630,691,144</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">333,755,480</td>
<td align="right">30.4%</td>
<td align="right">334,718,380</td>
<td align="right">30.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">333,782,380</td>
<td align="right"></td>
<td align="right">334,742,840</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">806,629,861</td>
<td align="right"></td>
<td align="right">807,735,542</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">765,582,720</td>
<td align="right">69.6%</td>
<td align="right">766,178,060</td>
<td align="right">69.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">764,413,580</td>
<td align="right">69.5%</td>
<td align="right">764,369,880</td>
<td align="right">69.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
<td align="right">3,920</td>
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
<td align="right">34,840</td>
<td align="right">93,574,180</td>
<td align="right">1,880,293,680</td>
<td align="right">34,760</td>
<td align="right">93,794,800</td>
<td align="right">1,869,748,740</td>
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
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">11,540</td>
<td align="right">1.5%</td>
<td align="right">11,440.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">26,780</td>
<td align="right">24.5%</td>
<td align="right">729,720</td>
<td align="right">96.6%</td>
<td align="right">2,624.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">520</td>
<td align="right">0.5%</td>
<td align="right">9,580</td>
<td align="right">1.3%</td>
<td align="right">1,742.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,420</td>
<td align="right">1.3%</td>
<td align="right">20,900</td>
<td align="right">2.8%</td>
<td align="right">1,371.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">109,520</td>
<td align="right"></td>
<td align="right">755,220</td>
<td align="right"></td>
<td align="right">589.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.9%</td>
<td align="right">2,320</td>
<td align="right">0.3%</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,155,220,840</td>
<td align="right"></td>
<td align="right">40,943,400</td>
<td align="right"></td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">12,929,144,260</td>
<td align="right">1,119.2%</td>
<td align="right">1,159,479,740</td>
<td align="right">2,831.9%</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">81,720</td>
<td align="right">74.6%</td>
<td align="right">23,180</td>
<td align="right">3.1%</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">81,580</td>
<td align="right">74.5%</td>
<td align="right">56,380</td>
<td align="right">7.5%</td>
<td align="right">-30.9%</td>
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
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">22,900</td>
<td align="right">85.5%</td>
<td align="right">723,740</td>
<td align="right">99.2%</td>
<td align="right">3,060.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">26,780</td>
<td align="right"></td>
<td align="right">729,720</td>
<td align="right"></td>
<td align="right">2,624.9%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">200</td>
<td align="right">0.7%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
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
<td align="right">400</td>
<td align="right">1.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,740</td>
<td align="right">10.2%</td>
<td align="right">10,520</td>
<td align="right">1.4%</td>
<td align="right">283.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,600</td>
<td align="right">13.4%</td>
<td align="right">62,660</td>
<td align="right">8.6%</td>
<td align="right">1,640.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,820</td>
<td align="right">25.5%</td>
<td align="right">282,980</td>
<td align="right">38.8%</td>
<td align="right">4,049.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,360</td>
<td align="right">20.0%</td>
<td align="right">238,820</td>
<td align="right">32.7%</td>
<td align="right">4,355.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,320</td>
<td align="right">12.4%</td>
<td align="right">104,820</td>
<td align="right">14.4%</td>
<td align="right">3,057.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,860</td>
<td align="right">14.4%</td>
<td align="right">25,560</td>
<td align="right">3.5%</td>
<td align="right">562.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">680</td>
<td align="right">2.5%</td>
<td align="right">4,360</td>
<td align="right">0.6%</td>
<td align="right">541.2%</td>
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
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">2,400</td>
<td align="right">9.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,460</td>
<td align="right">9.2%</td>
<td align="right">55,640</td>
<td align="right">7.6%</td>
<td align="right">2,161.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,500</td>
<td align="right">20.5%</td>
<td align="right">68,060</td>
<td align="right">9.3%</td>
<td align="right">1,137.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,180</td>
<td align="right">23.1%</td>
<td align="right">382,740</td>
<td align="right">52.5%</td>
<td align="right">6,093.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,020</td>
<td align="right">15.0%</td>
<td align="right">162,620</td>
<td align="right">22.3%</td>
<td align="right">3,945.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,680</td>
<td align="right">6.3%</td>
<td align="right">46,580</td>
<td align="right">6.4%</td>
<td align="right">2,672.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">620</td>
<td align="right">2.3%</td>
<td align="right">8,040</td>
<td align="right">1.1%</td>
<td align="right">1,196.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
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
<td align="left">_CALL_TYPE_1</td>
<td align="right">589,760</td>
<td align="right">200</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">9,895,220</td>
<td align="right">3,860</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">5,112,060</td>
<td align="right">8,700</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">251,020</td>
<td align="right">460</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">28,840</td>
<td align="right">60</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">810,680</td>
<td align="right">3,880</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">810,680</td>
<td align="right">3,880</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,345,700</td>
<td align="right">16,880</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">32,180</td>
<td align="right">180</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,892,640</td>
<td align="right">16,200</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">1,610,420</td>
<td align="right">9,280</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">59,501,220</td>
<td align="right">398,640</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">137,520</td>
<td align="right">1,020</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">412,220</td>
<td align="right">3,380</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">11,428,880</td>
<td align="right">127,460</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">93,120</td>
<td align="right">1,060</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">27,772,200</td>
<td align="right">325,000</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">19,455,820</td>
<td align="right">275,340</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,451,260</td>
<td align="right">260,920</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,143,020</td>
<td align="right">19,120</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,650,460</td>
<td align="right">98,080</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,612,080</td>
<td align="right">83,780</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">28,722,100</td>
<td align="right">558,140</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">168,100</td>
<td align="right">3,400</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">24,267,300</td>
<td align="right">517,720</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">2,994,320</td>
<td align="right">68,680</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">314,847,940</td>
<td align="right">7,292,240</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,995,040</td>
<td align="right">69,400</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,474,440</td>
<td align="right">81,140</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,152,940</td>
<td align="right">28,180</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">76,165,660</td>
<td align="right">1,888,460</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">61,859,280</td>
<td align="right">1,603,060</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,211,660</td>
<td align="right">83,780</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">22,781,520</td>
<td align="right">596,780</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">42,677,260</td>
<td align="right">1,158,540</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,070,860</td>
<td align="right">29,800</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">115,842,900</td>
<td align="right">3,356,840</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">793,560</td>
<td align="right">23,460</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">28,296,160</td>
<td align="right">847,720</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">28,296,160</td>
<td align="right">847,720</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,736,160</td>
<td align="right">204,580</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,734,360</td>
<td align="right">359,380</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">58,599,120</td>
<td align="right">1,805,700</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">65,186,680</td>
<td align="right">2,216,500</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">77,761,660</td>
<td align="right">2,671,320</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">57,295,680</td>
<td align="right">1,975,820</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">8,600,380</td>
<td align="right">297,620</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,031,014,260</td>
<td align="right">36,081,420</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">14,865,020</td>
<td align="right">524,040</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,155,220,840</td>
<td align="right">40,943,400</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">7,816,420</td>
<td align="right">281,020</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">40,474,560</td>
<td align="right">1,480,780</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">4,266,920</td>
<td align="right">170,620</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,152,131,520</td>
<td align="right">46,921,420</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">17,371,920</td>
<td align="right">720,580</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">2,972,140</td>
<td align="right">125,460</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">99,771,180</td>
<td align="right">4,340,860</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">61,120,840</td>
<td align="right">2,688,780</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">12,086,700</td>
<td align="right">550,800</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,200,800</td>
<td align="right">104,380</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">91,327,240</td>
<td align="right">4,520,120</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">99,777,600</td>
<td align="right">5,101,200</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">257,026,860</td>
<td align="right">13,166,480</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">918,525,740</td>
<td align="right">47,789,440</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">181,738,780</td>
<td align="right">9,900,360</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">183,920</td>
<td align="right">10,200</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">118,035,660</td>
<td align="right">6,677,400</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">25,014,600</td>
<td align="right">1,429,140</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">286,040</td>
<td align="right">16,440</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">286,040</td>
<td align="right">16,440</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">56,672,220</td>
<td align="right">3,265,820</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,480</td>
<td align="right">320</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">155,683,240</td>
<td align="right">10,192,300</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">165,392,040</td>
<td align="right">11,149,860</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,730,720</td>
<td align="right">117,180</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,659,300</td>
<td align="right">253,620</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">97,277,760</td>
<td align="right">6,794,860</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">87,981,280</td>
<td align="right">6,414,920</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">6,144,580</td>
<td align="right">464,680</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,144,580</td>
<td align="right">464,680</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">114,215,100</td>
<td align="right">8,710,260</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">402,121,700</td>
<td align="right">31,272,680</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">291,259,800</td>
<td align="right">22,833,780</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">153,981,240</td>
<td align="right">12,199,320</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">37,989,800</td>
<td align="right">3,014,220</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">2,092,600</td>
<td align="right">168,100</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">58,596,660</td>
<td align="right">4,794,880</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">164,391,060</td>
<td align="right">13,758,100</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,362,220</td>
<td align="right">116,520</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">16,152,760</td>
<td align="right">1,467,720</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">6,367,360</td>
<td align="right">578,640</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">138,300,440</td>
<td align="right">12,604,120</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,848,240</td>
<td align="right">1,010,320</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">70,082,960</td>
<td align="right">6,752,620</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">36,528,820</td>
<td align="right">3,556,260</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,612,560</td>
<td align="right">1,813,060</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,530,840</td>
<td align="right">345,260</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">92,700,380</td>
<td align="right">9,215,460</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">65,056,960</td>
<td align="right">6,497,820</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">16,800</td>
<td align="right">1,680</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">16,800</td>
<td align="right">1,680</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">157,027,480</td>
<td align="right">15,843,280</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">1,471,160</td>
<td align="right">152,500</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">1,471,160</td>
<td align="right">152,500</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">958,199,140</td>
<td align="right">100,084,740</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">63,917,580</td>
<td align="right">6,911,480</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">84,066,820</td>
<td align="right">9,105,100</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">82,694,680</td>
<td align="right">9,022,400</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">19,831,480</td>
<td align="right">2,175,960</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">589,580</td>
<td align="right">64,740</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">133,087,820</td>
<td align="right">15,333,340</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">170,061,880</td>
<td align="right">19,777,940</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">169,955,760</td>
<td align="right">19,776,460</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">3,159,720</td>
<td align="right">368,400</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">3,156,940</td>
<td align="right">368,140</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">388,440</td>
<td align="right">46,040</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">57,735,720</td>
<td align="right">7,088,460</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">56,383,860</td>
<td align="right">7,040,620</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">17,469,720</td>
<td align="right">2,209,320</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">81,409,560</td>
<td align="right">10,390,240</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">11,194,000</td>
<td align="right">1,459,640</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">444,149,780</td>
<td align="right">60,251,700</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">58,296,340</td>
<td align="right">8,008,100</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,154,780</td>
<td align="right">160,480</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">27,903,260</td>
<td align="right">3,997,180</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">23,798,320</td>
<td align="right">3,421,560</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">6,060</td>
<td align="right">900</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">186,825,080</td>
<td align="right">27,884,140</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">186,835,860</td>
<td align="right">28,139,720</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,532,760</td>
<td align="right">5,562,340</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,100,300</td>
<td align="right">170,160</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">11,023,700</td>
<td align="right">1,723,220</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">11,923,020</td>
<td align="right">1,918,380</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">59,913,520</td>
<td align="right">10,198,160</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">8,304,080</td>
<td align="right">1,415,340</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,064,520</td>
<td align="right">1,597,680</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,364,380</td>
<td align="right">241,000</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,529,100</td>
<td align="right">629,640</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">131,382,740</td>
<td align="right">23,527,700</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,814,960</td>
<td align="right">1,988,960</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">17,190,100</td>
<td align="right">3,203,300</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">172,427,980</td>
<td align="right">32,259,660</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">8,670,020</td>
<td align="right">1,625,940</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,407,260</td>
<td align="right">3,481,420</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">856,640</td>
<td align="right">172,040</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,049,580</td>
<td align="right">4,670,900</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">26,903,420</td>
<td align="right">5,498,300</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">26,311,380</td>
<td align="right">5,459,260</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">90,251,360</td>
<td align="right">19,093,320</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,533,320</td>
<td align="right">5,659,100</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">20,950,960</td>
<td align="right">4,935,460</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">11,066,620</td>
<td align="right">2,830,160</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">564,280</td>
<td align="right">160,620</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">235,716,140</td>
<td align="right">69,057,680</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,605,080</td>
<td align="right">4,667,060</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">15,957,000</td>
<td align="right">5,178,940</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">436,500</td>
<td align="right">145,880</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">358,240</td>
<td align="right">123,960</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">78,014,520</td>
<td align="right">28,131,580</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,239,360</td>
<td align="right">809,700</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">766,660</td>
<td align="right">279,480</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">465,540</td>
<td align="right">170,440</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">14,928,560</td>
<td align="right">5,559,440</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">5,671,900</td>
<td align="right">2,297,900</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">22,520</td>
<td align="right">9,140</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">174,460</td>
<td align="right">92,240</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,500</td>
<td align="right">1,480</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">25,281,800</td>
<td align="right">19,278,980</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">8,320</td>
<td align="right">6,400</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">14,983,800</td>
<td align="right">11,989,600</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">314,180</td>
<td align="right">255,660</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,614,740</td>
<td align="right">3,819,380</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,614,740</td>
<td align="right">3,819,380</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">135,180</td>
<td align="right">120,440</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,112,740</td>
<td align="right">3,675,500</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">273,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,360</td>
<td align="right">10,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">5,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">3,920</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,600</td>
<td align="right">2,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,600</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">69,074,980</td>
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
<td align="right">2,660</td>
<td align="right">23,200</td>
<td align="right">772.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,700</td>
<td align="right">1,340</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">400</td>
<td align="right"></td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
