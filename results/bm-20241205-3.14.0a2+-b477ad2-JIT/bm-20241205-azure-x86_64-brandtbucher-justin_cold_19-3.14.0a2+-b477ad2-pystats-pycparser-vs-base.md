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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">316,080</td>
<td align="right">46,040</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">798,540</td>
<td align="right">528,420</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">760</td>
<td align="right">880</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,732,240</td>
<td align="right">1,650,380</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,898,480</td>
<td align="right">9,591,840</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,554,420</td>
<td align="right">5,390,740</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,875,320</td>
<td align="right">2,793,400</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,842,240</td>
<td align="right">1,805,600</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,808,660</td>
<td align="right">8,673,720</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,768,340</td>
<td align="right">10,633,400</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,124,960</td>
<td align="right">6,066,740</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,552,900</td>
<td align="right">36,281,940</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">37,387,780</td>
<td align="right">37,152,620</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">22,384,760</td>
<td align="right">22,249,820</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">66,009,200</td>
<td align="right">65,719,000</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">33,651,420</td>
<td align="right">33,515,980</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">132,831,460</td>
<td align="right">132,425,120</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">127,585,120</td>
<td align="right">127,239,980</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">182,096,700</td>
<td align="right">181,826,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">786,961,260</td>
<td align="right">785,947,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">61,488,080</td>
<td align="right">61,416,680</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,440</td>
<td align="right">84,500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">26,052,260</td>
<td align="right">26,034,020</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,467,360</td>
<td align="right">1,467,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,383,380</td>
<td align="right">1,383,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">787,320</td>
<td align="right">787,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,424,180</td>
<td align="right">12,423,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,520,900</td>
<td align="right">3,521,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,780,180</td>
<td align="right">20,779,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">54,213,900</td>
<td align="right">54,212,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">57,674,140</td>
<td align="right">57,673,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">158,331,940</td>
<td align="right">158,330,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,199,780</td>
<td align="right">6,199,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">113,125,420</td>
<td align="right">113,124,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,713,940</td>
<td align="right">26,714,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">27,902,980</td>
<td align="right">27,903,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">60,217,580</td>
<td align="right">60,217,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">68,878,920</td>
<td align="right">68,879,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">84,951,020</td>
<td align="right">84,951,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,314,040</td>
<td align="right">16,314,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">158,458,180</td>
<td align="right">158,458,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">74,554,640</td>
<td align="right">74,554,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">73,134,280</td>
<td align="right">73,134,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,278,700</td>
<td align="right">47,278,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">45,924,300</td>
<td align="right">45,924,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">43,822,020</td>
<td align="right">43,822,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">34,325,400</td>
<td align="right">34,325,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">31,930,300</td>
<td align="right">31,930,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,930,300</td>
<td align="right">31,930,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">22,793,300</td>
<td align="right">22,793,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,936,140</td>
<td align="right">20,936,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">16,960,820</td>
<td align="right">16,960,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">13,579,800</td>
<td align="right">13,579,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,358,920</td>
<td align="right">12,358,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,752,100</td>
<td align="right">10,752,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,822,040</td>
<td align="right">9,822,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">9,697,900</td>
<td align="right">9,697,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,145,600</td>
<td align="right">9,145,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">9,029,760</td>
<td align="right">9,029,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,846,200</td>
<td align="right">8,846,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">7,360,180</td>
<td align="right">7,360,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,152,100</td>
<td align="right">7,152,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,771,800</td>
<td align="right">5,771,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">5,755,780</td>
<td align="right">5,755,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,443,140</td>
<td align="right">4,443,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,318,560</td>
<td align="right">4,318,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,014,940</td>
<td align="right">4,014,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3,239,880</td>
<td align="right">3,239,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,569,380</td>
<td align="right">2,569,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,523,240</td>
<td align="right">2,523,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,766,440</td>
<td align="right">1,766,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,591,100</td>
<td align="right">1,591,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,513,120</td>
<td align="right">1,513,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,161,160</td>
<td align="right">1,161,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,091,760</td>
<td align="right">1,091,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,091,700</td>
<td align="right">1,091,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,080,100</td>
<td align="right">1,080,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">981,700</td>
<td align="right">981,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">855,060</td>
<td align="right">855,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">669,540</td>
<td align="right">669,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">480,660</td>
<td align="right">480,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">410,860</td>
<td align="right">410,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">406,300</td>
<td align="right">406,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">379,680</td>
<td align="right">379,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">216,960</td>
<td align="right">216,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">180,960</td>
<td align="right">180,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">94,920</td>
<td align="right">94,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,980</td>
<td align="right">90,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">88,680</td>
<td align="right">88,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">56,100</td>
<td align="right">56,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">32,940</td>
<td align="right">32,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,600</td>
<td align="right">30,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,420</td>
<td align="right">30,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">30,420</td>
<td align="right">30,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13,860</td>
<td align="right">13,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">13,860</td>
<td align="right">13,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,840</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,080</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="right">798,060</td>
<td align="right">1.9%</td>
<td align="right">528,020</td>
<td align="right">1.3%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,525,620</td>
<td align="right">98.1%</td>
<td align="right">40,525,620</td>
<td align="right">98.7%</td>
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
<td align="right">460</td>
<td align="right">95.8%</td>
<td align="right">380</td>
<td align="right">95.0%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">4.2%</td>
<td align="right">20</td>
<td align="right">5.0%</td>
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
<td align="right">200</td>
<td align="right">43.5%</td>
<td align="right">200</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">120</td>
<td align="right">26.1%</td>
<td align="right">120</td>
<td align="right">31.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">5.3%</td>
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
<td align="right">5,771,800</td>
<td align="right">100.0%</td>
<td align="right">5,771,800</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">27,895,600</td>
<td align="right">9.6%</td>
<td align="right">27,895,660</td>
<td align="right">9.6%</td>
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
<td align="right">261,746,940</td>
<td align="right">90.4%</td>
<td align="right">261,746,940</td>
<td align="right">90.4%</td>
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
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,340</td>
<td align="right">99.5%</td>
<td align="right">7,340</td>
<td align="right">99.5%</td>
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
<td align="right">7,040</td>
<td align="right">95.9%</td>
<td align="right">7,040</td>
<td align="right">95.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,012,260</td>
<td align="right">1.3%</td>
<td align="right">4,012,260</td>
<td align="right">1.3%</td>
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
<td align="right">290,155,380</td>
<td align="right">90.8%</td>
<td align="right">290,155,380</td>
<td align="right">90.8%</td>
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
<td align="right">25,540,620</td>
<td align="right">8.0%</td>
<td align="right">25,540,620</td>
<td align="right">8.0%</td>
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
<td align="right">482,360</td>
<td align="right">99.5%</td>
<td align="right">482,360</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,220</td>
<td align="right">0.5%</td>
<td align="right">2,220</td>
<td align="right">0.5%</td>
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
<td align="left">out of versions</td>
<td align="right">2,220</td>
<td align="right">100.0%</td>
<td align="right">2,220</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,220</td>
<td align="right">100.0%</td>
<td align="right">2,220</td>
<td align="right">100.0%</td>
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
<td align="right">406,200</td>
<td align="right">0.3%</td>
<td align="right">406,200</td>
<td align="right">0.3%</td>
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
<td align="right">130,939,800</td>
<td align="right">99.7%</td>
<td align="right">130,939,800</td>
<td align="right">99.7%</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
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
<td align="left">list</td>
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
<td align="right">100.0%</td>
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
<td align="right">1,841,500</td>
<td align="right">5.0%</td>
<td align="right">1,804,900</td>
<td align="right">4.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,664,280</td>
<td align="right">95.0%</td>
<td align="right">34,664,280</td>
<td align="right">95.0%</td>
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
<td align="right">100.0%</td>
<td align="right">700</td>
<td align="right">100.0%</td>
<td align="right">-5.4%</td>
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
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">48.6%</td>
<td align="right">320</td>
<td align="right">45.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">27.0%</td>
<td align="right">200</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">180</td>
<td align="right">25.7%</td>
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
<td align="right">2,874,360</td>
<td align="right">65.7%</td>
<td align="right">2,792,460</td>
<td align="right">65.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,498,080</td>
<td align="right">34.3%</td>
<td align="right">1,498,260</td>
<td align="right">34.9%</td>
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
<td align="right">960</td>
<td align="right">100.0%</td>
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
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
<td align="left">ascii string</td>
<td align="right">120</td>
<td align="right">12.5%</td>
<td align="right">100</td>
<td align="right">10.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">540</td>
<td align="right">56.2%</td>
<td align="right">540</td>
<td align="right">57.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">160</td>
<td align="right">16.7%</td>
<td align="right">160</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">60</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">40</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">40</td>
<td align="right">4.3%</td>
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
<td align="right">12,565,760</td>
<td align="right">2.2%</td>
<td align="right">12,490,420</td>
<td align="right">2.2%</td>
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
<td align="right">559,157,780</td>
<td align="right">97.5%</td>
<td align="right">559,096,760</td>
<td align="right">97.6%</td>
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
<td align="right">1,511,920</td>
<td align="right">0.3%</td>
<td align="right">1,511,920</td>
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
<td align="right">237,320</td>
<td align="right">99.6%</td>
<td align="right">235,900</td>
<td align="right">99.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">840</td>
<td align="right">0.4%</td>
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
<td align="right">360</td>
<td align="right">42.9%</td>
<td align="right">360</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">140</td>
<td align="right">16.7%</td>
<td align="right">140</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">120</td>
<td align="right">14.3%</td>
<td align="right">120</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">11.9%</td>
<td align="right">100</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">60</td>
<td align="right">7.1%</td>
<td align="right">60</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">40</td>
<td align="right">4.8%</td>
<td align="right">40</td>
<td align="right">4.8%</td>
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
<td align="right">96,311,520</td>
<td align="right">100.0%</td>
<td align="right">96,174,720</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,060</td>
<td align="right">0.0%</td>
<td align="right">4,060</td>
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
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">340</td>
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
<td align="right">2,520</td>
<td align="right">0.0%</td>
<td align="right">2,520</td>
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
<td align="right">231,825,100</td>
<td align="right">96.5%</td>
<td align="right">231,825,100</td>
<td align="right">96.5%</td>
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
<td align="right">8,365,160</td>
<td align="right">3.5%</td>
<td align="right">8,365,160</td>
<td align="right">3.5%</td>
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
<td align="right">157,800</td>
<td align="right">100.0%</td>
<td align="right">157,800</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
<td align="right">26,704,960</td>
<td align="right">50.1%</td>
<td align="right">26,705,020</td>
<td align="right">50.1%</td>
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
<td align="right">26,554,200</td>
<td align="right">49.9%</td>
<td align="right">26,554,200</td>
<td align="right">49.9%</td>
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
<td align="right">8,980</td>
<td align="right">100.0%</td>
<td align="right">8,980</td>
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
<td align="left">py simple</td>
<td align="right">8,980</td>
<td align="right">100.0%</td>
<td align="right">8,980</td>
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
<td align="right">1,063,380</td>
<td align="right">0.8%</td>
<td align="right">1,063,380</td>
<td align="right">0.8%</td>
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
<td align="right">127,835,920</td>
<td align="right">96.8%</td>
<td align="right">127,835,920</td>
<td align="right">96.8%</td>
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
<td align="right">3,137,820</td>
<td align="right">2.4%</td>
<td align="right">3,137,820</td>
<td align="right">2.4%</td>
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
<td align="right">59,180</td>
<td align="right">78.0%</td>
<td align="right">59,180</td>
<td align="right">78.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,700</td>
<td align="right">22.0%</td>
<td align="right">16,700</td>
<td align="right">22.0%</td>
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
<td align="right">13,000</td>
<td align="right">77.8%</td>
<td align="right">13,000</td>
<td align="right">77.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,680</td>
<td align="right">16.0%</td>
<td align="right">2,680</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,000</td>
<td align="right">6.0%</td>
<td align="right">1,000</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">36,819,480</td>
<td align="right">100.0%</td>
<td align="right">36,819,480</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">72,922,160</td>
<td align="right">2.4%</td>
<td align="right">72,533,600</td>
<td align="right">2.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,715,883,640</td>
<td align="right">56.7%</td>
<td align="right">1,712,816,620</td>
<td align="right">56.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">49,615,140</td>
<td align="right">1.6%</td>
<td align="right">49,539,360</td>
<td align="right">1.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,185,209,900</td>
<td align="right">39.2%</td>
<td align="right">1,184,004,560</td>
<td align="right">39.2%</td>
<td align="right">-0.1%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">798,060</td>
<td align="right">1.1%</td>
<td align="right">528,020</td>
<td align="right">0.7%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,874,360</td>
<td align="right">3.9%</td>
<td align="right">2,792,460</td>
<td align="right">3.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,841,500</td>
<td align="right">2.5%</td>
<td align="right">1,804,900</td>
<td align="right">2.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,704,960</td>
<td align="right">36.6%</td>
<td align="right">26,705,020</td>
<td align="right">36.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">27,895,600</td>
<td align="right">38.3%</td>
<td align="right">27,895,660</td>
<td align="right">38.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,771,800</td>
<td align="right">7.9%</td>
<td align="right">5,771,800</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,012,260</td>
<td align="right">5.5%</td>
<td align="right">4,012,260</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,511,920</td>
<td align="right">2.1%</td>
<td align="right">1,511,920</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,063,380</td>
<td align="right">1.5%</td>
<td align="right">1,063,380</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">406,200</td>
<td align="right">0.6%</td>
<td align="right">406,200</td>
<td align="right">0.6%</td>
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
<td align="right">1,684,740</td>
<td align="right">3.4%</td>
<td align="right">1,609,400</td>
<td align="right">3.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20,119,080</td>
<td align="right">40.5%</td>
<td align="right">20,119,080</td>
<td align="right">40.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,655,660</td>
<td align="right">21.5%</td>
<td align="right">10,655,660</td>
<td align="right">21.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,181,980</td>
<td align="right">16.5%</td>
<td align="right">8,181,980</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,421,180</td>
<td align="right">10.9%</td>
<td align="right">5,421,180</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,778,800</td>
<td align="right">3.6%</td>
<td align="right">1,778,800</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,355,660</td>
<td align="right">2.7%</td>
<td align="right">1,355,660</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">225,360</td>
<td align="right">0.5%</td>
<td align="right">225,360</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">183,180</td>
<td align="right">0.4%</td>
<td align="right">183,180</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,300</td>
<td align="right">0.0%</td>
<td align="right">2,300</td>
<td align="right">0.0%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">45,924,360</td>
<td align="right">29.0%</td>
<td align="right">45,924,360</td>
<td align="right">29.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,640,040</td>
<td align="right">71.0%</td>
<td align="right">112,640,040</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">45,924,360</td>
<td align="right">29.0%</td>
<td align="right">45,924,360</td>
<td align="right">29.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">45,924,120</td>
<td align="right">29.0%</td>
<td align="right">45,924,120</td>
<td align="right">29.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">45,923,760</td>
<td align="right">29.0%</td>
<td align="right">45,923,760</td>
<td align="right">29.0%</td>
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
<td align="right">34,854,900</td>
<td align="right">22.0%</td>
<td align="right">34,854,900</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">73,800</td>
<td align="right">0.0%</td>
<td align="right">73,800</td>
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
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,565,240</td>
<td align="right">100.0%</td>
<td align="right">158,565,240</td>
<td align="right">100.0%</td>
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
<td align="left">Method cache misses</td>
<td align="right">161,937</td>
<td align="right"></td>
<td align="right">139,086</td>
<td align="right"></td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">504,721</td>
<td align="right"></td>
<td align="right">463,525</td>
<td align="right"></td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">351,448</td>
<td align="right"></td>
<td align="right">332,650</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">329,598,160</td>
<td align="right">6.6%</td>
<td align="right">328,718,960</td>
<td align="right">6.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">691,604,720</td>
<td align="right">11.5%</td>
<td align="right">690,195,380</td>
<td align="right">11.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">42,458,363</td>
<td align="right"></td>
<td align="right">42,405,874</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,424,548,479</td>
<td align="right">23.7%</td>
<td align="right">1,425,758,741</td>
<td align="right">23.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,042,178,909</td>
<td align="right">20.8%</td>
<td align="right">1,042,930,449</td>
<td align="right">20.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,463,415,380</td>
<td align="right">29.2%</td>
<td align="right">1,462,374,780</td>
<td align="right">29.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,184,552,434</td>
<td align="right">43.5%</td>
<td align="right">2,185,706,526</td>
<td align="right">43.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,765,177,500</td>
<td align="right">29.4%</td>
<td align="right">1,764,249,480</td>
<td align="right">29.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,122,973,177</td>
<td align="right">35.4%</td>
<td align="right">2,124,013,197</td>
<td align="right">35.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">88,570,372</td>
<td align="right"></td>
<td align="right">88,589,170</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">137,308,560</td>
<td align="right"></td>
<td align="right">137,306,840</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">137,309,260</td>
<td align="right">43.3%</td>
<td align="right">137,307,540</td>
<td align="right">43.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">207,222,198</td>
<td align="right"></td>
<td align="right">207,222,446</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">27,487,940</td>
<td align="right">8.7%</td>
<td align="right">27,487,920</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">179,632,500</td>
<td align="right">56.7%</td>
<td align="right">179,632,420</td>
<td align="right">56.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">152,141,500</td>
<td align="right">48.0%</td>
<td align="right">152,141,440</td>
<td align="right">48.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,060</td>
<td align="right">0.0%</td>
<td align="right">3,060</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">36,013,800</td>
<td align="right"></td>
<td align="right">36,013,800</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">222,232,135</td>
<td align="right">11,505,300</td>
<td align="right">21,229,460</td>
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">222,295,650</td>
<td align="right">11,480,380</td>
<td align="right">21,252,680</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,620</td>
<td align="right">11.7%</td>
<td align="right">1,560</td>
<td align="right">11.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">12,240</td>
<td align="right">88.3%</td>
<td align="right">12,280</td>
<td align="right">88.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">203,379,680</td>
<td align="right"></td>
<td align="right">203,804,580</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">13,860</td>
<td align="right"></td>
<td align="right">13,840</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">6,509,865,980</td>
<td align="right">3,200.8%</td>
<td align="right">6,517,582,180</td>
<td align="right">3,198.0%</td>
<td align="right">0.1%</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">8,160</td>
<td align="right">58.9%</td>
<td align="right">8,160</td>
<td align="right">59.0%</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">160</td>
<td align="right">1.2%</td>
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
<td align="right">540</td>
<td align="right">33.3%</td>
<td align="right">540</td>
<td align="right">34.6%</td>
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
<td align="right">1,600</td>
<td align="right">98.8%</td>
<td align="right">1,540</td>
<td align="right">98.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,620</td>
<td align="right"></td>
<td align="right">1,560</td>
<td align="right"></td>
<td align="right">-3.7%</td>
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
<td align="right">7.4%</td>
<td align="right">120</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">120</td>
<td align="right">7.4%</td>
<td align="right">80</td>
<td align="right">5.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">280</td>
<td align="right">17.3%</td>
<td align="right">260</td>
<td align="right">16.7%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">320</td>
<td align="right">19.8%</td>
<td align="right">320</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">11.1%</td>
<td align="right">180</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">540</td>
<td align="right">33.3%</td>
<td align="right">540</td>
<td align="right">34.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">3.7%</td>
<td align="right">60</td>
<td align="right">3.8%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">300</td>
<td align="right">18.5%</td>
<td align="right">260</td>
<td align="right">16.7%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">20</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">560</td>
<td align="right">34.6%</td>
<td align="right">540</td>
<td align="right">34.6%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">9.9%</td>
<td align="right">160</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">380</td>
<td align="right">23.5%</td>
<td align="right">380</td>
<td align="right">24.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">180</td>
<td align="right">11.1%</td>
<td align="right">180</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
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
<td align="left">_BINARY_OP</td>
<td align="right">519,120</td>
<td align="right">789,160</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">519,120</td>
<td align="right">789,160</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">259,560</td>
<td align="right">394,580</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">550,700</td>
<td align="right">685,700</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,491,420</td>
<td align="right">4,933,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,863,180</td>
<td align="right">1,998,620</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,863,180</td>
<td align="right">1,998,620</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,886,500</td>
<td align="right">2,021,940</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">6,650,240</td>
<td align="right">6,813,920</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">2,840,020</td>
<td align="right">2,896,820</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,124,880</td>
<td align="right">4,206,780</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">24,394,480</td>
<td align="right">24,828,320</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">22,830,260</td>
<td align="right">23,100,180</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">12,233,220</td>
<td align="right">12,368,160</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">30,491,280</td>
<td align="right">30,761,740</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">36,408,740</td>
<td align="right">36,707,440</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,813,440</td>
<td align="right">20,948,880</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">10,386,720</td>
<td align="right">10,443,580</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,674,400</td>
<td align="right">28,809,360</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">33,745,060</td>
<td align="right">33,880,020</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">72,671,540</td>
<td align="right">72,941,440</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">83,032,520</td>
<td align="right">83,340,100</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">38,476,720</td>
<td align="right">38,612,600</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">80,614,820</td>
<td align="right">80,885,780</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">25,478,780</td>
<td align="right">25,560,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">91,147,020</td>
<td align="right">91,417,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,150,620</td>
<td align="right">8,168,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">203,379,680</td>
<td align="right">203,804,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">17,545,460</td>
<td align="right">17,582,060</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">216,666,260</td>
<td align="right">217,109,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">73,306,640</td>
<td align="right">73,441,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">199,146,480</td>
<td align="right">199,436,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">13,286,580</td>
<td align="right">13,304,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">536,936,440</td>
<td align="right">537,461,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">67,040</td>
<td align="right">66,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">67,040</td>
<td align="right">66,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">167,570,340</td>
<td align="right">167,708,520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">45,283,260</td>
<td align="right">45,319,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">436,746,560</td>
<td align="right">437,072,940</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">107,060</td>
<td align="right">107,000</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">170,270,660</td>
<td align="right">170,352,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">327,979,040</td>
<td align="right">328,042,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,252,520</td>
<td align="right">1,252,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">645,520</td>
<td align="right">645,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">693,320</td>
<td align="right">693,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">298,520</td>
<td align="right">298,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2,346,700</td>
<td align="right">2,346,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">44,328,640</td>
<td align="right">44,330,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">44,328,640</td>
<td align="right">44,330,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">28,468,340</td>
<td align="right">28,469,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">28,478,440</td>
<td align="right">28,479,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,512,140</td>
<td align="right">26,512,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">11,983,880</td>
<td align="right">11,983,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">55,672,040</td>
<td align="right">55,672,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">10,275,400</td>
<td align="right">10,275,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">180,225,920</td>
<td align="right">180,227,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">200,738,120</td>
<td align="right">200,740,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">94,287,420</td>
<td align="right">94,288,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">118,655,900</td>
<td align="right">118,656,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,996,320</td>
<td align="right">7,996,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">31,147,440</td>
<td align="right">31,147,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">31,147,440</td>
<td align="right">31,147,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">163,676,040</td>
<td align="right">163,676,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">26,225,580</td>
<td align="right">26,225,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">29,028,840</td>
<td align="right">29,028,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">27,788,560</td>
<td align="right">27,788,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">81,978,520</td>
<td align="right">81,978,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">15,419,560</td>
<td align="right">15,419,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">708,922,040</td>
<td align="right">708,921,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">183,941,600</td>
<td align="right">183,941,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">129,553,140</td>
<td align="right">129,553,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">129,553,140</td>
<td align="right">129,553,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">93,995,880</td>
<td align="right">93,995,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">63,578,280</td>
<td align="right">63,578,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">63,578,280</td>
<td align="right">63,578,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">62,112,220</td>
<td align="right">62,112,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">61,470,120</td>
<td align="right">61,470,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">47,958,800</td>
<td align="right">47,958,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">36,650,080</td>
<td align="right">36,650,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">35,053,040</td>
<td align="right">35,053,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">33,966,180</td>
<td align="right">33,966,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">33,873,720</td>
<td align="right">33,873,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">33,682,580</td>
<td align="right">33,682,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">30,860,200</td>
<td align="right">30,860,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">27,143,040</td>
<td align="right">27,143,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">26,049,780</td>
<td align="right">26,049,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">25,703,300</td>
<td align="right">25,703,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">20,512,200</td>
<td align="right">20,512,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">20,418,740</td>
<td align="right">20,418,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">20,418,740</td>
<td align="right">20,418,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">20,418,740</td>
<td align="right">20,418,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">20,418,740</td>
<td align="right">20,418,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">20,418,740</td>
<td align="right">20,418,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">19,716,920</td>
<td align="right">19,716,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">19,716,920</td>
<td align="right">19,716,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">19,195,700</td>
<td align="right">19,195,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,950,260</td>
<td align="right">18,950,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">18,950,260</td>
<td align="right">18,950,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">18,926,940</td>
<td align="right">18,926,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">17,194,040</td>
<td align="right">17,194,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">17,153,840</td>
<td align="right">17,153,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">14,763,440</td>
<td align="right">14,763,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">11,556,880</td>
<td align="right">11,556,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">10,074,200</td>
<td align="right">10,074,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">7,982,440</td>
<td align="right">7,982,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">7,901,300</td>
<td align="right">7,901,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">7,370,060</td>
<td align="right">7,370,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">7,370,060</td>
<td align="right">7,370,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,370,060</td>
<td align="right">7,370,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,316,140</td>
<td align="right">4,316,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">4,186,820</td>
<td align="right">4,186,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,047,480</td>
<td align="right">4,047,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,695,440</td>
<td align="right">2,695,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,757,080</td>
<td align="right">1,757,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">629,360</td>
<td align="right">629,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">629,360</td>
<td align="right">629,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">40,020</td>
<td align="right">40,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">23,320</td>
<td align="right">23,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">8,700</td>
<td align="right">8,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,700</td>
<td align="right">8,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,080</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
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
<td align="right">4,360</td>
<td align="right">4,360</td>
<td align="right">0.0%</td>
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
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">160</td>
<td align="right">160</td>
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
Stats gathered on: 2024-12-06
