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
<td align="left">YIELD_VALUE</td>
<td align="right">691,760</td>
<td align="right">5,960</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,349,940</td>
<td align="right">44,380</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,178,780</td>
<td align="right">81,880</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,466,220</td>
<td align="right">30,020</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">448,960</td>
<td align="right">9,940</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">701,440</td>
<td align="right">16,820</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,740,560</td>
<td align="right">42,340</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,213,140</td>
<td align="right">58,960</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,311,880</td>
<td align="right">195,940</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,158,760</td>
<td align="right">58,820</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">761,980</td>
<td align="right">22,460</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,095,100</td>
<td align="right">35,220</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,200</td>
<td align="right">15,660</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,128,160</td>
<td align="right">44,560</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">461,000</td>
<td align="right">19,180</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">445,760</td>
<td align="right">19,920</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,072,060</td>
<td align="right">48,060</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">445,840</td>
<td align="right">20,000</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">222,920</td>
<td align="right">10,000</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3,317,380</td>
<td align="right">156,720</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,436,000</td>
<td align="right">69,180</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,165,980</td>
<td align="right">270,320</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">224,900</td>
<td align="right">11,800</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">225,640</td>
<td align="right">12,720</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">260,400</td>
<td align="right">15,120</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">228,360</td>
<td align="right">15,080</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28,194,740</td>
<td align="right">1,980,680</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,863,240</td>
<td align="right">135,300</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,157,700</td>
<td align="right">435,780</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,069,180</td>
<td align="right">349,840</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">245,900</td>
<td align="right">22,320</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">9,792,680</td>
<td align="right">959,780</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,000,420</td>
<td align="right">211,800</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,455,340</td>
<td align="right">260,800</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30,355,460</td>
<td align="right">3,302,520</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,434,740</td>
<td align="right">157,080</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">249,740</td>
<td align="right">28,580</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,722,380</td>
<td align="right">1,033,160</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,980,260</td>
<td align="right">1,205,440</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">773,280</td>
<td align="right">110,520</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">496,600</td>
<td align="right">73,020</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,734,980</td>
<td align="right">1,138,580</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,271,520</td>
<td align="right">496,500</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,370,100</td>
<td align="right">3,130,100</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,826,100</td>
<td align="right">284,560</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,463,620</td>
<td align="right">5,417,900</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">76,329,680</td>
<td align="right">12,750,920</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">22,200</td>
<td align="right">3,880</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,894,700</td>
<td align="right">1,418,360</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,180</td>
<td align="right">440</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,020,440</td>
<td align="right">218,860</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">6,893,620</td>
<td align="right">1,479,480</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,999,100</td>
<td align="right">1,599,120</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,130,100</td>
<td align="right">260,540</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,500,340</td>
<td align="right">1,503,560</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,322,740</td>
<td align="right">795,220</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,012,160</td>
<td align="right">257,460</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">997,280</td>
<td align="right">272,520</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">742,980</td>
<td align="right">209,960</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,713,800</td>
<td align="right">1,126,360</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">586,980</td>
<td align="right">189,760</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">266,360</td>
<td align="right">90,960</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">9,136,100</td>
<td align="right">3,142,440</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,061,340</td>
<td align="right">375,540</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">728,880</td>
<td align="right">262,400</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">130,140</td>
<td align="right">47,520</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">587,260</td>
<td align="right">215,260</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">105,540</td>
<td align="right">43,720</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,131,960</td>
<td align="right">470,080</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,194,680</td>
<td align="right">1,809,820</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,930,000</td>
<td align="right">1,732,940</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,701,240</td>
<td align="right">2,270,300</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">596,340</td>
<td align="right">309,180</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">901,980</td>
<td align="right">468,260</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,472,820</td>
<td align="right">3,002,780</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,121,000</td>
<td align="right">656,440</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">600</td>
<td align="right">360</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">363,860</td>
<td align="right">218,380</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">316,440</td>
<td align="right">201,660</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">523,640</td>
<td align="right">346,100</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,010,340</td>
<td align="right">4,057,700</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">224,740</td>
<td align="right">152,820</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">994,060</td>
<td align="right">692,620</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">466,580</td>
<td align="right">349,820</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">465,320</td>
<td align="right">349,660</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,940</td>
<td align="right">8,700</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">34,920</td>
<td align="right">34,200</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,560</td>
<td align="right">3,520</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,260</td>
<td align="right">12,180</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,920</td>
<td align="right">8,900</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">49,020</td>
<td align="right">49,000</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">256,980</td>
<td align="right">256,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">224,880</td>
<td align="right">224,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">72,200</td>
<td align="right">72,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">34,960</td>
<td align="right">34,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,680</td>
<td align="right">17,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,660</td>
<td align="right">11,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,600</td>
<td align="right">9,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">7,760</td>
<td align="right">7,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,580</td>
<td align="right">7,580</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,260</td>
<td align="right">6,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,700</td>
<td align="right">5,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,360</td>
<td align="right">4,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4,280</td>
<td align="right">4,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,100</td>
<td align="right">4,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">4,020</td>
<td align="right">4,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,880</td>
<td align="right">3,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,300</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,180</td>
<td align="right">1,180</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">920</td>
<td align="right">920</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">840</td>
<td align="right">840</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">660</td>
<td align="right">660</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
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
<td align="left">IMPORT_FROM</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">340</td>
<td align="right">340</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,480</td>
<td align="right">1.8%</td>
<td align="right">41,700</td>
<td align="right">0.8%</td>
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
<td align="right">5,635,240</td>
<td align="right">98.2%</td>
<td align="right">5,264,960</td>
<td align="right">99.2%</td>
<td align="right">-6.6%</td>
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
<td align="right">52.4%</td>
<td align="right">1,040</td>
<td align="right">51.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">980</td>
<td align="right">47.6%</td>
<td align="right">980</td>
<td align="right">48.5%</td>
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
<td align="left">xor</td>
<td align="right">220</td>
<td align="right">20.4%</td>
<td align="right">180</td>
<td align="right">17.3%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">240</td>
<td align="right">22.2%</td>
<td align="right">240</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">160</td>
<td align="right">14.8%</td>
<td align="right">160</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">140</td>
<td align="right">13.0%</td>
<td align="right">140</td>
<td align="right">13.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">100</td>
<td align="right">9.3%</td>
<td align="right">100</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">100</td>
<td align="right">9.3%</td>
<td align="right">100</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">60</td>
<td align="right">5.6%</td>
<td align="right">60</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">3.7%</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">20</td>
<td align="right">1.9%</td>
<td align="right">20</td>
<td align="right">1.9%</td>
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
<td align="right">773,280</td>
<td align="right">100.0%</td>
<td align="right">110,520</td>
<td align="right">100.0%</td>
<td align="right">-85.7%</td>
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
<td align="right">3,313,940</td>
<td align="right">19.1%</td>
<td align="right">787,980</td>
<td align="right">5.3%</td>
<td align="right">-76.2%</td>
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
<td align="right">14,025,620</td>
<td align="right">94.4%</td>
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
<td align="right">31,700</td>
<td align="right">0.2%</td>
<td align="right">31,700</td>
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
<td align="left">Failure</td>
<td align="right">5,960</td>
<td align="right">63.5%</td>
<td align="right">4,400</td>
<td align="right">56.3%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,420</td>
<td align="right">36.5%</td>
<td align="right">3,420</td>
<td align="right">43.7%</td>
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
<td align="left">buffer int</td>
<td align="right">960</td>
<td align="right">16.1%</td>
<td align="right">640</td>
<td align="right">14.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">4,140</td>
<td align="right">69.5%</td>
<td align="right">3,000</td>
<td align="right">68.2%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">640</td>
<td align="right">10.7%</td>
<td align="right">540</td>
<td align="right">12.3%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">220</td>
<td align="right">3.7%</td>
<td align="right">220</td>
<td align="right">5.0%</td>
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
<td align="right">1,781,200</td>
<td align="right">7.5%</td>
<td align="right">1,488,200</td>
<td align="right">6.2%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,015,660</td>
<td align="right">92.4%</td>
<td align="right">22,475,420</td>
<td align="right">93.7%</td>
<td align="right">2.1%</td>
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
<td align="right">10,260</td>
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
<td align="right">41,060</td>
<td align="right">99.9%</td>
<td align="right">35,520</td>
<td align="right">99.8%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<td align="left">init not inline values</td>
<td align="right">80</td>
<td align="right">133.3%</td>
<td align="right">80</td>
<td align="right">133.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,000</td>
<td align="right">0.1%</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">896,720</td>
<td align="right">5.1%</td>
<td align="right">463,480</td>
<td align="right">2.7%</td>
<td align="right">-48.3%</td>
</tr>
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
<td align="right">16,652,220</td>
<td align="right">97.3%</td>
<td align="right">-0.1%</td>
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
<td align="right">2,680</td>
<td align="right">49.4%</td>
<td align="right">2,220</td>
<td align="right">46.2%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,740</td>
<td align="right">50.6%</td>
<td align="right">2,580</td>
<td align="right">53.8%</td>
<td align="right">-5.8%</td>
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
<td align="right">1,180</td>
<td align="right">44.0%</td>
<td align="right">880</td>
<td align="right">39.6%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">540</td>
<td align="right">20.1%</td>
<td align="right">420</td>
<td align="right">18.9%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">5.2%</td>
<td align="right">120</td>
<td align="right">5.4%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">13.4%</td>
<td align="right">340</td>
<td align="right">15.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">8.2%</td>
<td align="right">220</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">200</td>
<td align="right">7.5%</td>
<td align="right">200</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">1.5%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
<td align="right">584,340</td>
<td align="right">12.0%</td>
<td align="right">212,640</td>
<td align="right">4.7%</td>
<td align="right">-63.6%</td>
</tr>
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
<td align="right">4,280,600</td>
<td align="right">95.2%</td>
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
<td align="right">1,980</td>
<td align="right">67.8%</td>
<td align="right">1,680</td>
<td align="right">64.1%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">940</td>
<td align="right">32.2%</td>
<td align="right">940</td>
<td align="right">35.9%</td>
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
<td align="right">900</td>
<td align="right">45.5%</td>
<td align="right">740</td>
<td align="right">44.0%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">920</td>
<td align="right">46.5%</td>
<td align="right">780</td>
<td align="right">46.4%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">6.1%</td>
<td align="right">120</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">40</td>
<td align="right">2.0%</td>
<td align="right">40</td>
<td align="right">2.4%</td>
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
<td align="right">522,360</td>
<td align="right">28.7%</td>
<td align="right">344,940</td>
<td align="right">25.5%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,295,980</td>
<td align="right">71.2%</td>
<td align="right">1,008,820</td>
<td align="right">74.5%</td>
<td align="right">-22.2%</td>
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
<td align="right">860</td>
<td align="right">74.1%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">23.4%</td>
<td align="right">300</td>
<td align="right">25.9%</td>
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
<td align="left">reversed list</td>
<td align="right">460</td>
<td align="right">46.9%</td>
<td align="right">340</td>
<td align="right">39.5%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">320</td>
<td align="right">32.7%</td>
<td align="right">320</td>
<td align="right">37.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">120</td>
<td align="right">12.2%</td>
<td align="right">120</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">6.1%</td>
<td align="right">60</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">20</td>
<td align="right">2.0%</td>
<td align="right">20</td>
<td align="right">2.3%</td>
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
<td align="right">3,249,740</td>
<td align="right">4.1%</td>
<td align="right">476,520</td>
<td align="right">0.6%</td>
<td align="right">-85.3%</td>
</tr>
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
<td align="right">75,281,740</td>
<td align="right">99.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">18,000</td>
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
<td align="right">6,920</td>
<td align="right">31.5%</td>
<td align="right">5,120</td>
<td align="right">25.3%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,080</td>
<td align="right">68.5%</td>
<td align="right">15,080</td>
<td align="right">74.7%</td>
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
<td align="left">method</td>
<td align="right">4,220</td>
<td align="right">61.0%</td>
<td align="right">2,800</td>
<td align="right">54.7%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,240</td>
<td align="right">17.9%</td>
<td align="right">880</td>
<td align="right">17.2%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">460</td>
<td align="right">6.6%</td>
<td align="right">460</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">400</td>
<td align="right">5.8%</td>
<td align="right">400</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
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
<td align="right">13,174,220</td>
<td align="right">99.9%</td>
<td align="right">3,014,540</td>
<td align="right">99.7%</td>
<td align="right">-77.1%</td>
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
<td align="right">4,940</td>
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
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">720</td>
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
<td align="right">4,660</td>
<td align="right">100.0%</td>
<td align="right">4,660</td>
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
<td align="right">60</td>
<td align="right">15.8%</td>
<td align="right">60</td>
<td align="right">15.8%</td>
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
<td align="right">260</td>
<td align="right">68.4%</td>
<td align="right">260</td>
<td align="right">68.4%</td>
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
<td align="right">257,500</td>
<td align="right">2.9%</td>
<td align="right">-64.4%</td>
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
<td align="right">8,600,380</td>
<td align="right">96.9%</td>
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
<td align="right">14,860</td>
<td align="right">0.2%</td>
<td align="right">14,860</td>
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
<td align="left">Failure</td>
<td align="right">1,720</td>
<td align="right">31.6%</td>
<td align="right">1,380</td>
<td align="right">27.1%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,720</td>
<td align="right">68.4%</td>
<td align="right">3,720</td>
<td align="right">72.9%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">980</td>
<td align="right">57.0%</td>
<td align="right">640</td>
<td align="right">46.4%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">400</td>
<td align="right">23.3%</td>
<td align="right">400</td>
<td align="right">29.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">18.6%</td>
<td align="right">320</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">20</td>
<td align="right">1.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,840</td>
<td align="right">0.2%</td>
<td align="right">3,840</td>
<td align="right">0.2%</td>
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
<td align="right">1,885,860</td>
<td align="right">99.8%</td>
<td align="right">1,885,860</td>
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
<td align="right">460</td>
<td align="right">88.5%</td>
<td align="right">460</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">11.5%</td>
<td align="right">60</td>
<td align="right">11.5%</td>
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
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="right">4,065,400</td>
<td align="right">23.6%</td>
<td align="right">346,960</td>
<td align="right">3.7%</td>
<td align="right">-91.5%</td>
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
<td align="right">4,920</td>
<td align="right">0.1%</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,088,800</td>
<td align="right">76.1%</td>
<td align="right">9,077,060</td>
<td align="right">96.2%</td>
<td align="right">-30.7%</td>
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
<td align="right">2,080</td>
<td align="right">47.1%</td>
<td align="right">1,180</td>
<td align="right">39.9%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,340</td>
<td align="right">52.9%</td>
<td align="right">1,780</td>
<td align="right">60.1%</td>
<td align="right">-23.9%</td>
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
<td align="right">1,020</td>
<td align="right">49.0%</td>
<td align="right">180</td>
<td align="right">15.3%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">320</td>
<td align="right">15.4%</td>
<td align="right">260</td>
<td align="right">22.0%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">460</td>
<td align="right">22.1%</td>
<td align="right">460</td>
<td align="right">39.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">180</td>
<td align="right">8.7%</td>
<td align="right">180</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80</td>
<td align="right">3.8%</td>
<td align="right">80</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.7%</td>
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
<td align="right">499,120</td>
<td align="right">99.9%</td>
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
<td align="right">217,897,660</td>
<td align="right">58.1%</td>
<td align="right">33,734,840</td>
<td align="right">50.9%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">140,973,960</td>
<td align="right">37.6%</td>
<td align="right">27,830,080</td>
<td align="right">42.0%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,316,660</td>
<td align="right">3.8%</td>
<td align="right">3,120,460</td>
<td align="right">4.7%</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,891,900</td>
<td align="right">0.5%</td>
<td align="right">1,560,580</td>
<td align="right">2.4%</td>
<td align="right">-17.5%</td>
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
<td align="right">4,065,400</td>
<td align="right">28.5%</td>
<td align="right">346,960</td>
<td align="right">11.3%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">773,280</td>
<td align="right">5.4%</td>
<td align="right">110,520</td>
<td align="right">3.6%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,249,740</td>
<td align="right">22.8%</td>
<td align="right">476,520</td>
<td align="right">15.6%</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,313,940</td>
<td align="right">23.3%</td>
<td align="right">787,980</td>
<td align="right">25.7%</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">723,640</td>
<td align="right">5.1%</td>
<td align="right">257,500</td>
<td align="right">8.4%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">584,340</td>
<td align="right">4.1%</td>
<td align="right">212,640</td>
<td align="right">6.9%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">103,480</td>
<td align="right">0.7%</td>
<td align="right">41,700</td>
<td align="right">1.4%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">896,720</td>
<td align="right">6.3%</td>
<td align="right">463,480</td>
<td align="right">15.1%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">522,360</td>
<td align="right">3.7%</td>
<td align="right">344,940</td>
<td align="right">11.3%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">10,260</td>
<td align="right">0.1%</td>
<td align="right">10,260</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">183,400</td>
<td align="right">9.7%</td>
<td align="right">12,980</td>
<td align="right">0.8%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">18,940</td>
<td align="right">1.0%</td>
<td align="right">4,560</td>
<td align="right">0.3%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,420,040</td>
<td align="right">75.1%</td>
<td align="right">1,297,460</td>
<td align="right">83.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">172,200</td>
<td align="right">9.1%</td>
<td align="right">172,200</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">31,340</td>
<td align="right">1.7%</td>
<td align="right">31,340</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">16,020</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,000</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,560</td>
<td align="right">0.5%</td>
<td align="right">8,560</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,900</td>
<td align="right">0.4%</td>
<td align="right">7,900</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,960</td>
<td align="right">0.4%</td>
<td align="right">6,960</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5,160</td>
<td align="right">0.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5,120</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">14,862,800</td>
<td align="right">98.3%</td>
<td align="right">14,862,800</td>
<td align="right">98.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">257,320</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">257,140</td>
<td align="right">1.7%</td>
<td align="right">257,140</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">256,460</td>
<td align="right">1.7%</td>
<td align="right">256,460</td>
<td align="right">1.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">11,760</td>
<td align="right">0.1%</td>
<td align="right">11,760</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">224,800</td>
<td align="right">1.5%</td>
<td align="right">224,800</td>
<td align="right">1.5%</td>
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
<tr>
<td align="left">Frames pushed</td>
<td align="right">14,653,080</td>
<td align="right">96.9%</td>
<td align="right">14,653,080</td>
<td align="right">96.9%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">2,970</td>
<td align="right"></td>
<td align="right">14,439</td>
<td align="right"></td>
<td align="right">386.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">112,756,408</td>
<td align="right">26.0%</td>
<td align="right">236,596,271</td>
<td align="right">52.2%</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">132,112,294</td>
<td align="right">31.9%</td>
<td align="right">266,416,828</td>
<td align="right">66.8%</td>
<td align="right">101.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">58,611,838</td>
<td align="right">13.5%</td>
<td align="right">113,580,455</td>
<td align="right">25.1%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">64,990,100</td>
<td align="right">15.7%</td>
<td align="right">9,447,440</td>
<td align="right">2.4%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">153,959,640</td>
<td align="right">37.2%</td>
<td align="right">36,973,520</td>
<td align="right">9.3%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">72,213,100</td>
<td align="right">16.6%</td>
<td align="right">18,983,180</td>
<td align="right">4.2%</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">21,777</td>
<td align="right"></td>
<td align="right">35,380</td>
<td align="right"></td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">190,606,580</td>
<td align="right">43.9%</td>
<td align="right">84,086,380</td>
<td align="right">18.6%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">63,097,983</td>
<td align="right">15.2%</td>
<td align="right">86,224,787</td>
<td align="right">21.6%</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">21,184</td>
<td align="right"></td>
<td align="right">23,443</td>
<td align="right"></td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,160,610</td>
<td align="right"></td>
<td align="right">1,148,721</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">142,160</td>
<td align="right">0.6%</td>
<td align="right">143,440</td>
<td align="right">0.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">6,120</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,552,656</td>
<td align="right"></td>
<td align="right">4,548,257</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">17,258,860</td>
<td align="right">72.8%</td>
<td align="right">17,261,520</td>
<td align="right">72.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">17,110,600</td>
<td align="right">72.2%</td>
<td align="right">17,111,960</td>
<td align="right">72.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,940,237</td>
<td align="right"></td>
<td align="right">15,941,329</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,422,640</td>
<td align="right"></td>
<td align="right">6,422,820</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,450,100</td>
<td align="right">27.2%</td>
<td align="right">6,450,280</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">234,280</td>
<td align="right"></td>
<td align="right">234,280</td>
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
<td align="right">680</td>
<td align="right">2,840</td>
<td align="right">19,361,680</td>
<td align="right">680</td>
<td align="right">2,840</td>
<td align="right">19,355,160</td>
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
<td align="right">80</td>
<td align="right">2.3%</td>
<td align="right">240</td>
<td align="right">4.7%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">327,196,660</td>
<td align="right">1,779.6%</td>
<td align="right">894,061,860</td>
<td align="right">2,342.2%</td>
<td align="right">173.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,640</td>
<td align="right">47.1%</td>
<td align="right">3,420</td>
<td align="right">67.1%</td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">18,385,960</td>
<td align="right"></td>
<td align="right">38,172,260</td>
<td align="right"></td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,420</td>
<td align="right">40.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,480</td>
<td align="right"></td>
<td align="right">5,100</td>
<td align="right"></td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,840</td>
<td align="right">52.9%</td>
<td align="right">1,680</td>
<td align="right">32.9%</td>
<td align="right">-8.7%</td>
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
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">1,640</td>
<td align="right"></td>
<td align="right">3,420</td>
<td align="right"></td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,640</td>
<td align="right">100.0%</td>
<td align="right">3,420</td>
<td align="right">100.0%</td>
<td align="right">108.5%</td>
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
<td align="right">120</td>
<td align="right">7.3%</td>
<td align="right">280</td>
<td align="right">8.2%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">240</td>
<td align="right">14.6%</td>
<td align="right">480</td>
<td align="right">14.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">240</td>
<td align="right">14.6%</td>
<td align="right">600</td>
<td align="right">17.5%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">700</td>
<td align="right">42.7%</td>
<td align="right">1,220</td>
<td align="right">35.7%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">9.8%</td>
<td align="right">520</td>
<td align="right">15.2%</td>
<td align="right">225.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">180</td>
<td align="right">11.0%</td>
<td align="right">320</td>
<td align="right">9.4%</td>
<td align="right">77.8%</td>
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
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">60</td>
<td align="right">1.8%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">160</td>
<td align="right">9.8%</td>
<td align="right">280</td>
<td align="right">8.2%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">140</td>
<td align="right">8.5%</td>
<td align="right">620</td>
<td align="right">18.1%</td>
<td align="right">342.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">540</td>
<td align="right">32.9%</td>
<td align="right">980</td>
<td align="right">28.7%</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">480</td>
<td align="right">29.3%</td>
<td align="right">940</td>
<td align="right">27.5%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">220</td>
<td align="right">13.4%</td>
<td align="right">480</td>
<td align="right">14.0%</td>
<td align="right">118.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.8%</td>
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
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">20</td>
<td align="right">439,040</td>
<td align="right">2,195,100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">120</td>
<td align="right">1,607,160</td>
<td align="right">1,339,200.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">180</td>
<td align="right">1,328,120</td>
<td align="right">737,744.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">820</td>
<td align="right">4,306,380</td>
<td align="right">525,068.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">420</td>
<td align="right">2,194,960</td>
<td align="right">522,509.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">160</td>
<td align="right">801,740</td>
<td align="right">500,987.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">440</td>
<td align="right">1,728,380</td>
<td align="right">392,713.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">780</td>
<td align="right">2,154,960</td>
<td align="right">276,176.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">980</td>
<td align="right">2,100,920</td>
<td align="right">214,279.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,800</td>
<td align="right">2,775,020</td>
<td align="right">154,067.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">540</td>
<td align="right">542,320</td>
<td align="right">100,329.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">340</td>
<td align="right">245,620</td>
<td align="right">72,141.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,140</td>
<td align="right">1,279,800</td>
<td align="right">59,703.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,200</td>
<td align="right">687,000</td>
<td align="right">57,150.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,460</td>
<td align="right">756,160</td>
<td align="right">51,691.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,460</td>
<td align="right">756,160</td>
<td align="right">51,691.8%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">140</td>
<td align="right">72,060</td>
<td align="right">51,371.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">140</td>
<td align="right">72,060</td>
<td align="right">51,371.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">21,260</td>
<td align="right">7,114,320</td>
<td align="right">33,363.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">36,740</td>
<td align="right">12,140,100</td>
<td align="right">32,943.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">22,980</td>
<td align="right">6,553,660</td>
<td align="right">28,419.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,860</td>
<td align="right">373,560</td>
<td align="right">19,983.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">49,280</td>
<td align="right">6,819,600</td>
<td align="right">13,738.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">105,240</td>
<td align="right">14,383,000</td>
<td align="right">13,566.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">13,180</td>
<td align="right">1,756,440</td>
<td align="right">13,226.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">8,220</td>
<td align="right">877,780</td>
<td align="right">10,578.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">24,740</td>
<td align="right">2,550,700</td>
<td align="right">10,210.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">16,940</td>
<td align="right">1,637,140</td>
<td align="right">9,564.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">7,640</td>
<td align="right">669,520</td>
<td align="right">8,663.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">24,640</td>
<td align="right">2,107,660</td>
<td align="right">8,453.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,260</td>
<td align="right">447,080</td>
<td align="right">8,399.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,720</td>
<td align="right">116,500</td>
<td align="right">6,673.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">108,660</td>
<td align="right">6,486,000</td>
<td align="right">5,869.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">10,840</td>
<td align="right">543,860</td>
<td align="right">4,917.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">107,680</td>
<td align="right">5,104,460</td>
<td align="right">4,640.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">6,540</td>
<td align="right">307,980</td>
<td align="right">4,609.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">25,260</td>
<td align="right">1,184,040</td>
<td align="right">4,587.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">38,540</td>
<td align="right">1,580,080</td>
<td align="right">3,999.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">440</td>
<td align="right">16,980</td>
<td align="right">3,759.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">52,700</td>
<td align="right">2,010,740</td>
<td align="right">3,715.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">239,600</td>
<td align="right">9,072,500</td>
<td align="right">3,686.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">17,720</td>
<td align="right">462,160</td>
<td align="right">2,508.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">41,740</td>
<td align="right">1,065,740</td>
<td align="right">2,453.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">27,780</td>
<td align="right">560,800</td>
<td align="right">1,918.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">37,960</td>
<td align="right">700,720</td>
<td align="right">1,745.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">28,200</td>
<td align="right">492,760</td>
<td align="right">1,647.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">27,140</td>
<td align="right">452,680</td>
<td align="right">1,567.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">183,380</td>
<td align="right">2,690,420</td>
<td align="right">1,367.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">33,040</td>
<td align="right">456,620</td>
<td align="right">1,282.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">22,080</td>
<td align="right">265,940</td>
<td align="right">1,104.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">10,780</td>
<td align="right">127,540</td>
<td align="right">1,083.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">692,100</td>
<td align="right">8,152,080</td>
<td align="right">1,077.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">17,080</td>
<td align="right">192,480</td>
<td align="right">1,026.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">17,240</td>
<td align="right">162,720</td>
<td align="right">843.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">90,660</td>
<td align="right">815,420</td>
<td align="right">799.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">27,920</td>
<td align="right">207,140</td>
<td align="right">641.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">494,880</td>
<td align="right">3,655,540</td>
<td align="right">638.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">2,477,360</td>
<td align="right">17,440,620</td>
<td align="right">604.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">300,200</td>
<td align="right">2,088,820</td>
<td align="right">595.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,478,040</td>
<td align="right">38,236,380</td>
<td align="right">490.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">82,920</td>
<td align="right">482,220</td>
<td align="right">481.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">440</td>
<td align="right">2,180</td>
<td align="right">395.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,400</td>
<td align="right">146,180</td>
<td align="right">365.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,629,400</td>
<td align="right">15,735,100</td>
<td align="right">333.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,033,600</td>
<td align="right">46,300,060</td>
<td align="right">319.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,560,140</td>
<td align="right">10,003,300</td>
<td align="right">290.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,186,020</td>
<td align="right">44,511,420</td>
<td align="right">265.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,507,840</td>
<td align="right">27,339,700</td>
<td align="right">264.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,231,040</td>
<td align="right">25,403,860</td>
<td align="right">251.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">699,880</td>
<td align="right">2,352,020</td>
<td align="right">236.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,081,860</td>
<td align="right">3,564,820</td>
<td align="right">229.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">42,260</td>
<td align="right">126,420</td>
<td align="right">199.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">167,200</td>
<td align="right">454,360</td>
<td align="right">171.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">167,200</td>
<td align="right">454,360</td>
<td align="right">171.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">17,491,700</td>
<td align="right">46,465,480</td>
<td align="right">165.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,561,500</td>
<td align="right">9,397,960</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,854,340</td>
<td align="right">4,891,760</td>
<td align="right">163.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,875,220</td>
<td align="right">4,893,840</td>
<td align="right">161.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,867,660</td>
<td align="right">4,800,360</td>
<td align="right">157.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">26,783,540</td>
<td align="right">68,309,620</td>
<td align="right">155.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,640,200</td>
<td align="right">9,201,800</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">20,924,780</td>
<td align="right">49,970,500</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">23,418,960</td>
<td align="right">55,835,660</td>
<td align="right">138.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,449,960</td>
<td align="right">8,171,880</td>
<td align="right">136.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,449,960</td>
<td align="right">8,171,880</td>
<td align="right">136.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">4,331,700</td>
<td align="right">9,965,460</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,923,820</td>
<td align="right">4,354,760</td>
<td align="right">126.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,923,820</td>
<td align="right">4,354,760</td>
<td align="right">126.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,923,820</td>
<td align="right">4,354,760</td>
<td align="right">126.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,460,720</td>
<td align="right">7,591,480</td>
<td align="right">119.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,177,780</td>
<td align="right">9,073,440</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">584,760</td>
<td align="right">1,241,560</td>
<td align="right">112.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,222,720</td>
<td align="right">2,581,240</td>
<td align="right">111.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">18,385,960</td>
<td align="right">38,172,260</td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">21,288,520</td>
<td align="right">41,074,820</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,824,040</td>
<td align="right">3,454,100</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">280</td>
<td align="right">520</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">280</td>
<td align="right">520</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">510,660</td>
<td align="right">942,720</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">555,920</td>
<td align="right">1,004,060</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,125,260</td>
<td align="right">7,081,580</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">636,420</td>
<td align="right">1,092,400</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,464,540</td>
<td align="right">5,786,560</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,639,620</td>
<td align="right">5,983,940</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">4,121,700</td>
<td align="right">6,635,380</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,963,780</td>
<td align="right">13,565,580</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,642,540</td>
<td align="right">4,880,360</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,150,500</td>
<td align="right">15,949,220</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,898,140</td>
<td align="right">20,721,100</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">648,080</td>
<td align="right">825,500</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,490,880</td>
<td align="right">4,346,200</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">3,596,640</td>
<td align="right">4,337,700</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,446,100</td>
<td align="right">4,020,680</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,446,100</td>
<td align="right">4,020,680</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,785,440</td>
<td align="right">2,024,700</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">587,160</td>
<td align="right">649,140</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">21,520</td>
<td align="right">22,240</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,472,460</td>
<td align="right">3,555,080</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,433,080</td>
<td align="right">3,505,020</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,380</td>
<td align="right">3,420</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">10,400</td>
<td align="right">10,480</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">685,100</td>
<td align="right">685,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,454,480</td>
<td align="right">3,454,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,902,560</td>
<td align="right">2,902,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,503,560</td>
<td align="right">2,503,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,503,560</td>
<td align="right">2,503,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,490,180</td>
<td align="right">2,490,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,480,440</td>
<td align="right">2,480,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">691,080</td>
<td align="right">691,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,300</td>
<td align="right">18,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">17,240</td>
<td align="right">17,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,240</td>
<td align="right">17,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,400</td>
<td align="right">7,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,400</td>
<td align="right">7,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,860</td>
<td align="right">5,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">3,340</td>
<td align="right">3,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">880</td>
<td align="right">880</td>
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
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">1,436,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">739,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">685,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">466,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">425,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">425,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">404,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">221,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">221,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">213,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">213,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">213,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">212,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">212,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right"></td>
<td align="right">80,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">40</td>
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
<td align="right">700</td>
<td align="right">1,260</td>
<td align="right">80.0%</td>
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
Stats gathered on: 2024-10-05
