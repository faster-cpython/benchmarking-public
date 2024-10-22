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
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">120</td>
<td align="right">280</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,700</td>
<td align="right">11,540</td>
<td align="right">102.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,580</td>
<td align="right">15,340</td>
<td align="right">102.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,180</td>
<td align="right">2,380</td>
<td align="right">101.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,466,220</td>
<td align="right">2,934,540</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,740,560</td>
<td align="right">3,481,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">445,760</td>
<td align="right">891,520</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">80</td>
<td align="right">160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">691,760</td>
<td align="right">1,383,440</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">445,840</td>
<td align="right">891,600</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">222,920</td>
<td align="right">445,800</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,455,360</td>
<td align="right">4,910,240</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">249,740</td>
<td align="right">499,420</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,061,340</td>
<td align="right">2,122,220</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">9,792,840</td>
<td align="right">19,580,520</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,713,960</td>
<td align="right">7,423,600</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,213,140</td>
<td align="right">4,423,700</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">761,980</td>
<td align="right">1,522,940</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,100</td>
<td align="right">881,580</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,069,200</td>
<td align="right">8,132,660</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,020,480</td>
<td align="right">2,039,520</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,000,460</td>
<td align="right">3,998,040</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3,317,500</td>
<td align="right">6,630,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,434,760</td>
<td align="right">2,867,080</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">448,960</td>
<td align="right">897,120</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,178,840</td>
<td align="right">8,348,580</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,158,780</td>
<td align="right">4,312,140</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,500,580</td>
<td align="right">12,984,820</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,350,000</td>
<td align="right">8,688,240</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">460,780</td>
<td align="right">920,300</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,863,240</td>
<td align="right">3,721,000</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">224,900</td>
<td align="right">449,060</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,464,460</td>
<td align="right">68,811,220</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,132,040</td>
<td align="right">2,259,560</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,012,900</td>
<td align="right">2,021,740</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,998,680</td>
<td align="right">13,969,160</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,722,100</td>
<td align="right">15,412,820</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,896,280</td>
<td align="right">15,760,280</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">994,160</td>
<td align="right">1,983,440</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,322,960</td>
<td align="right">6,629,500</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">224,880</td>
<td align="right">448,640</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">224,880</td>
<td align="right">448,640</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,701,620</td>
<td align="right">9,376,500</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">363,900</td>
<td align="right">725,660</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">316,520</td>
<td align="right">631,160</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">6,893,680</td>
<td align="right">13,746,240</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,010,580</td>
<td align="right">11,984,960</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">225,640</td>
<td align="right">449,800</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,166,380</td>
<td align="right">10,298,600</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28,194,740</td>
<td align="right">56,201,920</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">743,060</td>
<td align="right">1,480,960</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">997,160</td>
<td align="right">1,987,100</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,474,340</td>
<td align="right">10,908,720</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">9,136,300</td>
<td align="right">18,202,700</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30,356,340</td>
<td align="right">60,467,640</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,370,860</td>
<td align="right">40,576,440</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">76,332,220</td>
<td align="right">152,043,120</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">701,540</td>
<td align="right">1,397,220</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,826,240</td>
<td align="right">3,636,400</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,735,300</td>
<td align="right">15,402,100</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">773,340</td>
<td align="right">1,539,700</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,121,120</td>
<td align="right">2,231,920</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">523,800</td>
<td align="right">1,042,620</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">596,500</td>
<td align="right">1,187,320</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,311,980</td>
<td align="right">14,553,280</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,195,280</td>
<td align="right">8,348,380</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,157,680</td>
<td align="right">10,261,660</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,980,900</td>
<td align="right">17,867,780</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,436,080</td>
<td align="right">2,856,320</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">728,880</td>
<td align="right">1,448,480</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,271,580</td>
<td align="right">6,501,180</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">266,360</td>
<td align="right">529,080</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">465,440</td>
<td align="right">923,760</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,929,780</td>
<td align="right">7,797,780</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">228,360</td>
<td align="right">453,080</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,072,100</td>
<td align="right">2,127,060</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">466,720</td>
<td align="right">925,920</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">260,360</td>
<td align="right">515,880</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,095,360</td>
<td align="right">2,169,940</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">256,980</td>
<td align="right">508,500</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,128,280</td>
<td align="right">2,231,960</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">245,960</td>
<td align="right">485,480</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">587,360</td>
<td align="right">1,157,980</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">72,240</td>
<td align="right">142,320</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">902,280</td>
<td align="right">1,777,260</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">586,980</td>
<td align="right">1,155,700</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,130,180</td>
<td align="right">2,219,780</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,100</td>
<td align="right">8,020</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,200</td>
<td align="right">4,280</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">22,200</td>
<td align="right">42,960</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">7,760</td>
<td align="right">14,640</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">496,620</td>
<td align="right">934,220</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">105,640</td>
<td align="right">197,720</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,940</td>
<td align="right">16,620</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">100</td>
<td align="right">180</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">840</td>
<td align="right">1,480</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">130,180</td>
<td align="right">225,380</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">920</td>
<td align="right">1,560</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,580</td>
<td align="right">5,660</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">140</td>
<td align="right">220</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">140</td>
<td align="right">220</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">480</td>
<td align="right">720</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">160</td>
<td align="right">240</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">160</td>
<td align="right">240</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,940</td>
<td align="right">5,280</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">4,140</td>
<td align="right">5,540</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,280</td>
<td align="right">8,360</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">580</td>
<td align="right">740</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,080</td>
<td align="right">11,560</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">340</td>
<td align="right">420</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">360</td>
<td align="right">440</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">700</td>
<td align="right">780</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,360</td>
<td align="right">13,620</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">880</td>
<td align="right">960</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">49,000</td>
<td align="right">51,400</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,020</td>
<td align="right">2,100</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">34,960</td>
<td align="right">36,080</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">35,000</td>
<td align="right">36,120</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,380</td>
<td align="right">4,520</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,740</td>
<td align="right">17,880</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,680</td>
<td align="right">9,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,660</td>
<td align="right">11,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">7,080</td>
<td align="right">7,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">6,520</td>
<td align="right">6,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4,280</td>
<td align="right">4,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">660</td>
<td align="right">660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">640</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">620</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">5,635,240</td>
<td align="right">98.2%</td>
<td align="right">11,178,760</td>
<td align="right">98.3%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,560</td>
<td align="right">1.8%</td>
<td align="right">195,080</td>
<td align="right">1.7%</td>
<td align="right">88.4%</td>
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
<td align="right">1,080</td>
<td align="right">51.9%</td>
<td align="right">1,640</td>
<td align="right">62.1%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,000</td>
<td align="right">48.1%</td>
<td align="right">1,000</td>
<td align="right">37.9%</td>
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
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">3.7%</td>
<td align="right">100</td>
<td align="right">6.1%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">60</td>
<td align="right">5.6%</td>
<td align="right">120</td>
<td align="right">7.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">160</td>
<td align="right">14.8%</td>
<td align="right">260</td>
<td align="right">15.9%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">240</td>
<td align="right">22.2%</td>
<td align="right">380</td>
<td align="right">23.2%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">140</td>
<td align="right">13.0%</td>
<td align="right">220</td>
<td align="right">13.4%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">220</td>
<td align="right">20.4%</td>
<td align="right">320</td>
<td align="right">19.5%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">100</td>
<td align="right">9.3%</td>
<td align="right">120</td>
<td align="right">7.3%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">100</td>
<td align="right">9.3%</td>
<td align="right">100</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">20</td>
<td align="right">1.9%</td>
<td align="right">20</td>
<td align="right">1.2%</td>
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
<td align="right">773,340</td>
<td align="right">100.0%</td>
<td align="right">1,539,700</td>
<td align="right">100.0%</td>
<td align="right">99.1%</td>
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
<td align="right">3,314,160</td>
<td align="right">19.1%</td>
<td align="right">6,618,640</td>
<td align="right">19.1%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,025,620</td>
<td align="right">80.7%</td>
<td align="right">27,956,660</td>
<td align="right">80.8%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,700</td>
<td align="right">0.2%</td>
<td align="right">31,860</td>
<td align="right">0.1%</td>
<td align="right">0.5%</td>
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
<td align="right">5,960</td>
<td align="right">63.5%</td>
<td align="right">8,020</td>
<td align="right">70.1%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,420</td>
<td align="right">36.5%</td>
<td align="right">3,420</td>
<td align="right">29.9%</td>
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
<td align="right">4,140</td>
<td align="right">69.5%</td>
<td align="right">5,740</td>
<td align="right">71.6%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">640</td>
<td align="right">10.7%</td>
<td align="right">880</td>
<td align="right">11.0%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">960</td>
<td align="right">16.1%</td>
<td align="right">1,140</td>
<td align="right">14.2%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">220</td>
<td align="right">3.7%</td>
<td align="right">260</td>
<td align="right">3.2%</td>
<td align="right">18.2%</td>
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
<td align="right">22,018,080</td>
<td align="right">92.5%</td>
<td align="right">43,841,520</td>
<td align="right">92.5%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,778,800</td>
<td align="right">7.5%</td>
<td align="right">3,541,800</td>
<td align="right">7.5%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,260</td>
<td align="right">0.0%</td>
<td align="right">10,320</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,080</td>
<td align="right">99.9%</td>
<td align="right">74,920</td>
<td align="right">99.8%</td>
<td align="right">82.4%</td>
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
<td align="left">out of versions</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">80</td>
<td align="right">133.3%</td>
<td align="right">140</td>
<td align="right">116.7%</td>
<td align="right">75.0%</td>
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
<td align="right">200</td>
<td align="right">50.0%</td>
<td align="right">200</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,666,940</td>
<td align="right">94.8%</td>
<td align="right">33,233,700</td>
<td align="right">94.9%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">896,980</td>
<td align="right">5.1%</td>
<td align="right">1,770,260</td>
<td align="right">5.1%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,000</td>
<td align="right">0.1%</td>
<td align="right">19,500</td>
<td align="right">0.1%</td>
<td align="right">95.0%</td>
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
<td align="right">2,700</td>
<td align="right">49.5%</td>
<td align="right">4,400</td>
<td align="right">59.9%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,760</td>
<td align="right">50.5%</td>
<td align="right">2,940</td>
<td align="right">40.1%</td>
<td align="right">6.5%</td>
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
<td align="right">360</td>
<td align="right">13.3%</td>
<td align="right">1,040</td>
<td align="right">23.6%</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">8.1%</td>
<td align="right">460</td>
<td align="right">10.5%</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">200</td>
<td align="right">7.4%</td>
<td align="right">340</td>
<td align="right">7.7%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,220</td>
<td align="right">45.2%</td>
<td align="right">1,800</td>
<td align="right">40.9%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">540</td>
<td align="right">20.0%</td>
<td align="right">600</td>
<td align="right">13.6%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">4.4%</td>
<td align="right">120</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">1.5%</td>
<td align="right">40</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,280,600</td>
<td align="right">87.9%</td>
<td align="right">8,534,760</td>
<td align="right">88.1%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">584,440</td>
<td align="right">12.0%</td>
<td align="right">1,154,520</td>
<td align="right">11.9%</td>
<td align="right">97.5%</td>
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
<td align="right">1,980</td>
<td align="right">67.8%</td>
<td align="right">2,520</td>
<td align="right">72.8%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">940</td>
<td align="right">32.2%</td>
<td align="right">940</td>
<td align="right">27.2%</td>
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
<td align="right">40</td>
<td align="right">2.0%</td>
<td align="right">140</td>
<td align="right">5.6%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">920</td>
<td align="right">46.5%</td>
<td align="right">1,220</td>
<td align="right">48.4%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">6.1%</td>
<td align="right">140</td>
<td align="right">5.6%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">900</td>
<td align="right">45.5%</td>
<td align="right">1,020</td>
<td align="right">40.5%</td>
<td align="right">13.3%</td>
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
<td align="right">1,296,320</td>
<td align="right">71.2%</td>
<td align="right">2,581,380</td>
<td align="right">71.2%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">522,520</td>
<td align="right">28.7%</td>
<td align="right">1,040,380</td>
<td align="right">28.7%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">260</td>
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
<td align="left">Failure</td>
<td align="right">980</td>
<td align="right">76.6%</td>
<td align="right">1,880</td>
<td align="right">83.2%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">23.4%</td>
<td align="right">380</td>
<td align="right">16.8%</td>
<td align="right">26.7%</td>
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
<td align="left">reversed list</td>
<td align="right">460</td>
<td align="right">46.9%</td>
<td align="right">1,080</td>
<td align="right">57.4%</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">320</td>
<td align="right">32.7%</td>
<td align="right">540</td>
<td align="right">28.7%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">120</td>
<td align="right">12.2%</td>
<td align="right">120</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">6.1%</td>
<td align="right">60</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">20</td>
<td align="right">2.0%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">3.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,281,940</td>
<td align="right">95.8%</td>
<td align="right">150,413,300</td>
<td align="right">95.8%</td>
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
<td align="right">3,249,780</td>
<td align="right">4.1%</td>
<td align="right">6,476,980</td>
<td align="right">4.1%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
<td align="right">31,080</td>
<td align="right">0.0%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">6,940</td>
<td align="right">31.5%</td>
<td align="right">9,160</td>
<td align="right">37.2%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,080</td>
<td align="right">68.5%</td>
<td align="right">15,460</td>
<td align="right">62.8%</td>
<td align="right">2.5%</td>
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
<td align="left">overridden</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">400</td>
<td align="right">5.8%</td>
<td align="right">580</td>
<td align="right">6.3%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">460</td>
<td align="right">6.6%</td>
<td align="right">640</td>
<td align="right">7.0%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,240</td>
<td align="right">61.1%</td>
<td align="right">5,620</td>
<td align="right">61.4%</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,240</td>
<td align="right">17.9%</td>
<td align="right">1,440</td>
<td align="right">15.7%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">1,440</td>
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
<td align="right">13,175,460</td>
<td align="right">99.9%</td>
<td align="right">26,214,720</td>
<td align="right">100.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,940</td>
<td align="right">0.0%</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
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
<td align="right">4,740</td>
<td align="right">100.0%</td>
<td align="right">4,760</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">260</td>
<td align="right">68.4%</td>
<td align="right">500</td>
<td align="right">80.6%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">60</td>
<td align="right">15.8%</td>
<td align="right">60</td>
<td align="right">9.7%</td>
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
<td align="right">100.0%</td>
<td align="right">60</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">723,640</td>
<td align="right">7.7%</td>
<td align="right">1,442,840</td>
<td align="right">7.7%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,600,380</td>
<td align="right">92.0%</td>
<td align="right">17,146,380</td>
<td align="right">92.1%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,860</td>
<td align="right">0.2%</td>
<td align="right">23,900</td>
<td align="right">0.1%</td>
<td align="right">60.8%</td>
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
<td align="right">1,720</td>
<td align="right">31.6%</td>
<td align="right">2,120</td>
<td align="right">35.3%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,720</td>
<td align="right">68.4%</td>
<td align="right">3,880</td>
<td align="right">64.7%</td>
<td align="right">4.3%</td>
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
<td align="left">no dict</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">40</td>
<td align="right">1.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">400</td>
<td align="right">23.3%</td>
<td align="right">540</td>
<td align="right">25.5%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">18.6%</td>
<td align="right">400</td>
<td align="right">18.9%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">980</td>
<td align="right">57.0%</td>
<td align="right">1,140</td>
<td align="right">53.8%</td>
<td align="right">16.3%</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1,885,860</td>
<td align="right">99.8%</td>
<td align="right">3,768,420</td>
<td align="right">99.9%</td>
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
<td align="right">3,880</td>
<td align="right">0.2%</td>
<td align="right">3,880</td>
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
<td align="right">40</td>
<td align="right">8.0%</td>
<td align="right">180</td>
<td align="right">28.1%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">92.0%</td>
<td align="right">460</td>
<td align="right">71.9%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">180</td>
<td align="right">100.0%</td>
<td align="right">350.0%</td>
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
<td align="right">4,065,420</td>
<td align="right">23.6%</td>
<td align="right">8,127,500</td>
<td align="right">23.7%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,088,860</td>
<td align="right">76.1%</td>
<td align="right">26,108,440</td>
<td align="right">76.1%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">35,200</td>
<td align="right">0.2%</td>
<td align="right">67,980</td>
<td align="right">0.2%</td>
<td align="right">93.1%</td>
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
<td align="right">2,040</td>
<td align="right">46.2%</td>
<td align="right">3,420</td>
<td align="right">53.4%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,380</td>
<td align="right">53.8%</td>
<td align="right">2,980</td>
<td align="right">46.6%</td>
<td align="right">25.2%</td>
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
<td align="right">180</td>
<td align="right">8.8%</td>
<td align="right">360</td>
<td align="right">10.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,020</td>
<td align="right">50.0%</td>
<td align="right">2,000</td>
<td align="right">58.5%</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">280</td>
<td align="right">13.7%</td>
<td align="right">380</td>
<td align="right">11.1%</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80</td>
<td align="right">3.9%</td>
<td align="right">100</td>
<td align="right">2.9%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">460</td>
<td align="right">22.5%</td>
<td align="right">560</td>
<td align="right">16.4%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">20</td>
<td align="right">1.0%</td>
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
<td align="right">500,000</td>
<td align="right">99.9%</td>
<td align="right">969,120</td>
<td align="right">100.0%</td>
<td align="right">93.8%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">140,981,960</td>
<td align="right">37.6%</td>
<td align="right">281,136,940</td>
<td align="right">37.6%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">217,906,900</td>
<td align="right">58.1%</td>
<td align="right">434,021,100</td>
<td align="right">58.1%</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,317,840</td>
<td align="right">3.8%</td>
<td align="right">28,460,220</td>
<td align="right">3.8%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,889,360</td>
<td align="right">0.5%</td>
<td align="right">3,717,940</td>
<td align="right">0.5%</td>
<td align="right">96.8%</td>
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
<td align="right">4,065,420</td>
<td align="right">28.5%</td>
<td align="right">8,127,500</td>
<td align="right">28.6%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,314,160</td>
<td align="right">23.3%</td>
<td align="right">6,618,640</td>
<td align="right">23.3%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">723,640</td>
<td align="right">5.1%</td>
<td align="right">1,442,840</td>
<td align="right">5.1%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,249,780</td>
<td align="right">22.8%</td>
<td align="right">6,476,980</td>
<td align="right">22.8%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">522,520</td>
<td align="right">3.7%</td>
<td align="right">1,040,380</td>
<td align="right">3.7%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">773,340</td>
<td align="right">5.4%</td>
<td align="right">1,539,700</td>
<td align="right">5.4%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">584,440</td>
<td align="right">4.1%</td>
<td align="right">1,154,520</td>
<td align="right">4.1%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">896,980</td>
<td align="right">6.3%</td>
<td align="right">1,770,260</td>
<td align="right">6.2%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">103,560</td>
<td align="right">0.7%</td>
<td align="right">195,080</td>
<td align="right">0.7%</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">10,260</td>
<td align="right">0.1%</td>
<td align="right">10,320</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
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
<td align="right">6,960</td>
<td align="right">0.4%</td>
<td align="right">14,080</td>
<td align="right">0.4%</td>
<td align="right">102.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">172,200</td>
<td align="right">9.1%</td>
<td align="right">344,500</td>
<td align="right">9.3%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">16,020</td>
<td align="right">0.8%</td>
<td align="right">31,920</td>
<td align="right">0.9%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,417,640</td>
<td align="right">75.0%</td>
<td align="right">2,823,960</td>
<td align="right">76.0%</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">183,400</td>
<td align="right">9.7%</td>
<td align="right">362,560</td>
<td align="right">9.8%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,000</td>
<td align="right">0.5%</td>
<td align="right">19,500</td>
<td align="right">0.5%</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">18,940</td>
<td align="right">1.0%</td>
<td align="right">35,500</td>
<td align="right">1.0%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,560</td>
<td align="right">0.5%</td>
<td align="right">16,040</td>
<td align="right">0.4%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">31,340</td>
<td align="right">1.7%</td>
<td align="right">31,500</td>
<td align="right">0.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,900</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">10,340</td>
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
<td align="right">224,800</td>
<td align="right">1.5%</td>
<td align="right">448,560</td>
<td align="right">1.5%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">14,862,800</td>
<td align="right">98.3%</td>
<td align="right">29,646,080</td>
<td align="right">98.3%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">14,653,080</td>
<td align="right">96.9%</td>
<td align="right">29,219,880</td>
<td align="right">96.9%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">256,460</td>
<td align="right">1.7%</td>
<td align="right">507,980</td>
<td align="right">1.7%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">257,140</td>
<td align="right">1.7%</td>
<td align="right">508,660</td>
<td align="right">1.7%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">508,840</td>
<td align="right">1.7%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">508,840</td>
<td align="right">1.7%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">11,760</td>
<td align="right">0.1%</td>
<td align="right">20,960</td>
<td align="right">0.1%</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
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
<td align="right">1,520</td>
<td align="right">0.0%</td>
<td align="right">1,520</td>
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
<td align="left">Method cache hits</td>
<td align="right">4,535,211</td>
<td align="right"></td>
<td align="right">9,069,926</td>
<td align="right"></td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,422,480</td>
<td align="right"></td>
<td align="right">12,822,220</td>
<td align="right"></td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">190,613,360</td>
<td align="right">190,613,360 / 0 !!</td>
<td align="right">379,928,060</td>
<td align="right">379,928,060 / 0 !!</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">153,966,760</td>
<td align="right">153,966,760 / 0 !!</td>
<td align="right">306,824,320</td>
<td align="right">306,824,320 / 0 !!</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,449,600</td>
<td align="right">27.2%</td>
<td align="right">12,848,980</td>
<td align="right">28.8%</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">234,280</td>
<td align="right"></td>
<td align="right">466,360</td>
<td align="right"></td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">141,620</td>
<td align="right">0.6%</td>
<td align="right">280,260</td>
<td align="right">0.6%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,161,121</td>
<td align="right"></td>
<td align="right">2,291,498</td>
<td align="right"></td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">132,117,518</td>
<td align="right">132,117,518 / 0 !!</td>
<td align="right">255,967,106</td>
<td align="right">255,967,106 / 0 !!</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">112,758,639</td>
<td align="right">112,758,639 / 0 !!</td>
<td align="right">216,536,858</td>
<td align="right">216,536,858 / 0 !!</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">11,700</td>
<td align="right">0.0%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,936,950</td>
<td align="right"></td>
<td align="right">30,420,310</td>
<td align="right"></td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">17,258,620</td>
<td align="right">72.8%</td>
<td align="right">31,697,280</td>
<td align="right">71.2%</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">17,110,900</td>
<td align="right">72.2%</td>
<td align="right">31,405,320</td>
<td align="right">70.5%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">38,649</td>
<td align="right"></td>
<td align="right">12,714</td>
<td align="right"></td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">38,380</td>
<td align="right"></td>
<td align="right">12,937</td>
<td align="right"></td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,459</td>
<td align="right"></td>
<td align="right">3,002</td>
<td align="right"></td>
<td align="right">22.1%</td>
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
<td align="right">680</td>
<td align="right">2,940</td>
<td align="right">19,344,300</td>
<td align="right">1,300</td>
<td align="right">453,420</td>
<td align="right">31,893,500</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">40</td>
<td align="right">1.3%</td>
<td align="right">100</td>
<td align="right">2.2%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">18,387,380</td>
<td align="right"></td>
<td align="right">36,743,960</td>
<td align="right"></td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">305,880,060</td>
<td align="right">1,663.5%</td>
<td align="right">577,839,000</td>
<td align="right">1,572.6%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,880</td>
<td align="right">62.3%</td>
<td align="right">3,280</td>
<td align="right">71.6%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,480</td>
<td align="right">49.0%</td>
<td align="right">2,460</td>
<td align="right">53.7%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,020</td>
<td align="right"></td>
<td align="right">4,580</td>
<td align="right"></td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,140</td>
<td align="right">37.7%</td>
<td align="right">1,300</td>
<td align="right">28.4%</td>
<td align="right">14.0%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,140</td>
<td align="right"></td>
<td align="right">1,300</td>
<td align="right"></td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,140</td>
<td align="right">100.0%</td>
<td align="right">1,300</td>
<td align="right">100.0%</td>
<td align="right">14.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">260</td>
<td align="right">22.8%</td>
<td align="right">260</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">140</td>
<td align="right">12.3%</td>
<td align="right">140</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">180</td>
<td align="right">15.8%</td>
<td align="right">180</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">400</td>
<td align="right">35.1%</td>
<td align="right">460</td>
<td align="right">35.4%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">80</td>
<td align="right">7.0%</td>
<td align="right">120</td>
<td align="right">9.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">7.0%</td>
<td align="right">140</td>
<td align="right">10.8%</td>
<td align="right">75.0%</td>
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
<td align="right">120</td>
<td align="right">10.5%</td>
<td align="right">120</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">160</td>
<td align="right">14.0%</td>
<td align="right">160</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">14.0%</td>
<td align="right">160</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">340</td>
<td align="right">29.8%</td>
<td align="right">360</td>
<td align="right">27.7%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">240</td>
<td align="right">21.1%</td>
<td align="right">300</td>
<td align="right">23.1%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">100</td>
<td align="right">8.8%</td>
<td align="right">160</td>
<td align="right">12.3%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">20</td>
<td align="right">1.8%</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">100.0%</td>
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
<td align="left">_MAP_ADD</td>
<td align="right">160</td>
<td align="right">1,920</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">120</td>
<td align="right">760</td>
<td align="right">533.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">520</td>
<td align="right">3,080</td>
<td align="right">492.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">720</td>
<td align="right">3,120</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">720</td>
<td align="right">3,120</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">400</td>
<td align="right">1,120</td>
<td align="right">180.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,640</td>
<td align="right">4,520</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">960</td>
<td align="right">2,480</td>
<td align="right">158.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,760</td>
<td align="right">4,320</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,200</td>
<td align="right">2,800</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">420</td>
<td align="right">980</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">60</td>
<td align="right">140</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">60</td>
<td align="right">140</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">24,520</td>
<td align="right">54,840</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">25,180</td>
<td align="right">55,420</td>
<td align="right">120.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">38,400</td>
<td align="right">82,160</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">24,440</td>
<td align="right">51,400</td>
<td align="right">110.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">17,200</td>
<td align="right">36,000</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">17,200</td>
<td align="right">36,000</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,200</td>
<td align="right">36,000</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">17,640</td>
<td align="right">36,440</td>
<td align="right">106.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">299,800</td>
<td align="right">619,080</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">183,220</td>
<td align="right">371,620</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">90,780</td>
<td align="right">183,500</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">82,880</td>
<td align="right">167,360</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">52,160</td>
<td align="right">105,120</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">636,160</td>
<td align="right">1,280,320</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">684,940</td>
<td align="right">1,376,220</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">584,640</td>
<td align="right">1,173,760</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">107,440</td>
<td align="right">215,520</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,177,380</td>
<td align="right">8,374,440</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">4,121,480</td>
<td align="right">8,258,680</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,223,200</td>
<td align="right">2,450,480</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,125,200</td>
<td align="right">8,259,680</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,785,280</td>
<td align="right">3,574,320</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">2,477,000</td>
<td align="right">4,958,440</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,184,600</td>
<td align="right">24,389,340</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">691,040</td>
<td align="right">1,382,720</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">692,080</td>
<td align="right">1,384,720</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">17,490,820</td>
<td align="right">34,992,860</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">20,923,940</td>
<td align="right">41,859,420</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,464,340</td>
<td align="right">6,930,500</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,433,120</td>
<td align="right">6,866,560</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">23,417,980</td>
<td align="right">46,828,920</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,230,840</td>
<td align="right">14,459,100</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,149,980</td>
<td align="right">24,289,580</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">494,760</td>
<td align="right">988,840</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,923,440</td>
<td align="right">3,844,080</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,923,440</td>
<td align="right">3,844,080</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,923,440</td>
<td align="right">3,844,080</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,899,940</td>
<td align="right">31,774,920</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">18,387,380</td>
<td align="right">36,743,960</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,867,580</td>
<td align="right">3,731,900</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">647,760</td>
<td align="right">1,294,360</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,449,980</td>
<td align="right">6,893,280</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,449,980</td>
<td align="right">6,893,280</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,490,720</td>
<td align="right">6,973,860</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,507,340</td>
<td align="right">14,993,500</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,454,500</td>
<td align="right">6,896,740</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">4,331,180</td>
<td align="right">8,646,460</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,446,140</td>
<td align="right">6,879,580</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,446,140</td>
<td align="right">6,879,580</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,639,860</td>
<td align="right">7,263,460</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,639,340</td>
<td align="right">7,261,580</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,460,660</td>
<td align="right">6,903,700</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,824,000</td>
<td align="right">3,638,400</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,873,620</td>
<td align="right">3,736,700</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">3,596,520</td>
<td align="right">7,169,720</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">699,740</td>
<td align="right">1,394,780</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,472,420</td>
<td align="right">6,914,420</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">587,000</td>
<td align="right">1,168,040</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,854,180</td>
<td align="right">3,688,020</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,560,940</td>
<td align="right">7,078,440</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,081,820</td>
<td align="right">2,144,820</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,120</td>
<td align="right">4,200</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">510,580</td>
<td align="right">1,001,700</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">239,440</td>
<td align="right">466,720</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">555,760</td>
<td align="right">1,075,920</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">780</td>
<td align="right">1,500</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,760</td>
<td align="right">3,280</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">167,200</td>
<td align="right">310,720</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">167,400</td>
<td align="right">310,920</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,360</td>
<td align="right">6,240</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">26,780,000</td>
<td align="right">48,466,960</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,031,980</td>
<td align="right">19,432,100</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,962,280</td>
<td align="right">15,367,680</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">108,020</td>
<td align="right">183,300</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">28,080</td>
<td align="right">47,520</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">36,960</td>
<td align="right">60,480</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,480</td>
<td align="right">8,920</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,476,980</td>
<td align="right">10,393,920</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">103,960</td>
<td align="right">161,880</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">10,640</td>
<td align="right">16,480</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">6,440</td>
<td align="right">9,800</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">42,240</td>
<td align="right">61,600</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">180</td>
<td align="right">260</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">7,560</td>
<td align="right">10,120</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">48,900</td>
<td align="right">65,220</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,642,420</td>
<td align="right">4,815,540</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">760</td>
<td align="right">1,000</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,760</td>
<td align="right">7,520</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">21,160</td>
<td align="right">26,840</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,280</td>
<td align="right">9,200</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,280</td>
<td align="right">9,200</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,280</td>
<td align="right">39,440</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">27,240</td>
<td align="right">34,280</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,628,820</td>
<td align="right">4,546,680</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">22,860</td>
<td align="right">28,620</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">27,740</td>
<td align="right">34,700</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">41,700</td>
<td align="right">49,380</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,901,540</td>
<td align="right">3,320,900</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">37,900</td>
<td align="right">41,700</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">13,140</td>
<td align="right">14,420</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">8,140</td>
<td align="right">8,780</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">10,760</td>
<td align="right">11,400</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">33,020</td>
<td align="right">34,780</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">17,080</td>
<td align="right">17,720</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">27,700</td>
<td align="right">28,340</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">10,380</td>
<td align="right">10,540</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">22,020</td>
<td align="right">22,260</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,560,020</td>
<td align="right">2,562,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,503,500</td>
<td align="right">2,503,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,503,500</td>
<td align="right">2,503,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,490,140</td>
<td align="right">2,490,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,480,400</td>
<td align="right">2,480,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">21,480</td>
<td align="right">21,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,280</td>
<td align="right">18,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">16,940</td>
<td align="right">16,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">3,300</td>
<td align="right">3,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,520</td>
<td align="right">1,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">380</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">1,280</td>
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
<td align="right">680</td>
<td align="right">1,140</td>
<td align="right">67.6%</td>
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
