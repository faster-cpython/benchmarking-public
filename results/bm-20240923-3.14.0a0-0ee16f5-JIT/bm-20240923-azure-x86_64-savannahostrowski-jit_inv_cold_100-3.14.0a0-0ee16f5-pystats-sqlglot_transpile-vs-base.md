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
<td align="left">TO_BOOL_INT</td>
<td align="right">6,380</td>
<td align="right">3,516,240</td>
<td align="right">55,013.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">39,000</td>
<td align="right">7,974,960</td>
<td align="right">20,348.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">6,300</td>
<td align="right">441,660</td>
<td align="right">6,910.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">15,500</td>
<td align="right">798,160</td>
<td align="right">5,049.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">342,820</td>
<td align="right">7,938,500</td>
<td align="right">2,215.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">59,300</td>
<td align="right">1,140,480</td>
<td align="right">1,823.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">622,980</td>
<td align="right">8,950,000</td>
<td align="right">1,336.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2,800</td>
<td align="right">35,840</td>
<td align="right">1,180.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,104,840</td>
<td align="right">9,833,220</td>
<td align="right">790.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,180</td>
<td align="right">47,020</td>
<td align="right">660.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">15,960</td>
<td align="right">110,200</td>
<td align="right">590.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,900</td>
<td align="right">40,940</td>
<td align="right">418.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,383,360</td>
<td align="right">10,971,760</td>
<td align="right">360.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,487,520</td>
<td align="right">11,140,160</td>
<td align="right">347.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">177,960</td>
<td align="right">775,300</td>
<td align="right">335.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,697,420</td>
<td align="right">11,602,820</td>
<td align="right">330.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,609,780</td>
<td align="right">35,156,940</td>
<td align="right">308.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">16,900</td>
<td align="right">60,560</td>
<td align="right">258.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">276,540</td>
<td align="right">951,960</td>
<td align="right">244.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,497,380</td>
<td align="right">8,453,060</td>
<td align="right">238.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,192,140</td>
<td align="right">7,309,920</td>
<td align="right">233.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,960,560</td>
<td align="right">6,186,980</td>
<td align="right">215.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">201,540</td>
<td align="right">615,740</td>
<td align="right">205.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">167,960</td>
<td align="right">508,760</td>
<td align="right">202.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,107,520</td>
<td align="right">6,118,620</td>
<td align="right">190.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,883,860</td>
<td align="right">8,218,500</td>
<td align="right">185.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">29,900</td>
<td align="right">83,420</td>
<td align="right">179.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,309,300</td>
<td align="right">109,906,840</td>
<td align="right">172.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,752,260</td>
<td align="right">4,386,300</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,798,760</td>
<td align="right">4,478,640</td>
<td align="right">149.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">950,900</td>
<td align="right">2,110,500</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">108,651,460</td>
<td align="right">238,741,100</td>
<td align="right">119.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">4,537,040</td>
<td align="right">9,773,680</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">13,435,460</td>
<td align="right">26,758,680</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">9,583,380</td>
<td align="right">18,301,700</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,836,120</td>
<td align="right">11,020,220</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">3,578,360</td>
<td align="right">6,714,620</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,643,280</td>
<td align="right">3,029,540</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">658,840</td>
<td align="right">1,159,860</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,373,840</td>
<td align="right">54,697,740</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,413,220</td>
<td align="right">10,750,320</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,092,500</td>
<td align="right">5,178,420</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">604,060</td>
<td align="right">1,008,580</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,695,840</td>
<td align="right">35,886,540</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,055,780</td>
<td align="right">3,284,420</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">807,920</td>
<td align="right">1,269,960</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">82,140</td>
<td align="right">127,980</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,207,640</td>
<td align="right">13,954,360</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,789,200</td>
<td align="right">23,627,300</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,459,500</td>
<td align="right">12,275,660</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,068,520</td>
<td align="right">18,595,040</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">557,520</td>
<td align="right">787,120</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,227,580</td>
<td align="right">26,864,380</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,479,660</td>
<td align="right">3,395,780</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,097,060</td>
<td align="right">19,292,380</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">711,380</td>
<td align="right">954,960</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,441,400</td>
<td align="right">1,901,740</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">30,843,820</td>
<td align="right">39,801,120</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,170,520</td>
<td align="right">4,080,880</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,521,720</td>
<td align="right">19,778,360</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,477,560</td>
<td align="right">3,122,600</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,825,240</td>
<td align="right">4,326,080</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,525,280</td>
<td align="right">12,678,560</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">246,060</td>
<td align="right">291,820</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,029,620</td>
<td align="right">16,506,900</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,990,760</td>
<td align="right">2,176,160</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20,552,020</td>
<td align="right">22,349,640</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">57,020</td>
<td align="right">61,060</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">647,260</td>
<td align="right">686,040</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">62,940</td>
<td align="right">66,460</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">753,020</td>
<td align="right">788,300</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,378,940</td>
<td align="right">21,278,440</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,471,620</td>
<td align="right">1,529,020</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">705,660</td>
<td align="right">732,460</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">405,360</td>
<td align="right">419,840</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">224,220</td>
<td align="right">230,280</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">854,400</td>
<td align="right">875,520</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,577,640</td>
<td align="right">1,602,440</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,128,520</td>
<td align="right">1,146,200</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">728,800</td>
<td align="right">722,460</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">4,417,440</td>
<td align="right">4,449,140</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,705,680</td>
<td align="right">2,723,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">559,680</td>
<td align="right">563,160</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">626,320</td>
<td align="right">629,840</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,980,320</td>
<td align="right">2,996,980</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,868,740</td>
<td align="right">1,878,460</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,728,640</td>
<td align="right">1,735,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,168,960</td>
<td align="right">1,172,480</td>
<td align="right">0.3%</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">501,760</td>
<td align="right">501,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">327,540</td>
<td align="right">327,540</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">148,480</td>
<td align="right">148,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">87,040</td>
<td align="right">87,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">82,000</td>
<td align="right">82,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">61,400</td>
<td align="right">61,400</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">35,800</td>
<td align="right">35,800</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">25,680</td>
<td align="right">25,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,560</td>
<td align="right">17,560</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">5,100</td>
<td align="right">5,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">5,100</td>
<td align="right">5,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,520</td>
<td align="right">3,520</td>
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
<td align="right">380</td>
<td align="right">380</td>
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
<td align="right">15,500</td>
<td align="right">100.0%</td>
<td align="right">798,160</td>
<td align="right">100.0%</td>
<td align="right">5,049.4%</td>
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
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">441,000</td>
<td align="right">2.5%</td>
<td align="right">7,503.4%</td>
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
<td align="right">97.4%</td>
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
<td align="right">300</td>
<td align="right">31.9%</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">640</td>
<td align="right">82.1%</td>
<td align="right">640</td>
<td align="right">68.1%</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">114.3%</td>
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
<td align="right">1,629,180</td>
<td align="right">2.8%</td>
<td align="right">1,629,620</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,608,220</td>
<td align="right">97.2%</td>
<td align="right">56,608,220</td>
<td align="right">97.2%</td>
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
<td align="right">40,320</td>
<td align="right">100.0%</td>
<td align="right">40,340</td>
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
<td align="right">6,409,500</td>
<td align="right">25.6%</td>
<td align="right">10,745,360</td>
<td align="right">36.6%</td>
<td align="right">67.6%</td>
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
<td align="right">63.4%</td>
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
<td align="right">4,460</td>
<td align="right">89.9%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">13.4%</td>
<td align="right">500</td>
<td align="right">10.1%</td>
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
<td align="left">different types</td>
<td align="right">160</td>
<td align="right">5.0%</td>
<td align="right">340</td>
<td align="right">7.6%</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">3,060</td>
<td align="right">95.0%</td>
<td align="right">4,120</td>
<td align="right">92.4%</td>
<td align="right">34.6%</td>
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
<td align="right">5,660</td>
<td align="right">0.1%</td>
<td align="right">46,380</td>
<td align="right">0.5%</td>
<td align="right">719.4%</td>
</tr>
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
<td align="right">813,820</td>
<td align="right">8.4%</td>
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
<td align="right">8,867,800</td>
<td align="right">91.5%</td>
<td align="right">8,867,780</td>
<td align="right">91.2%</td>
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
<td align="right">220</td>
<td align="right">1.4%</td>
<td align="right">340</td>
<td align="right">2.1%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,640</td>
<td align="right">98.6%</td>
<td align="right">15,640</td>
<td align="right">97.9%</td>
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
<td align="right">120</td>
<td align="right">54.5%</td>
<td align="right">200</td>
<td align="right">58.8%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100</td>
<td align="right">45.5%</td>
<td align="right">140</td>
<td align="right">41.2%</td>
<td align="right">40.0%</td>
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
<td align="right">2,105,140</td>
<td align="right">81.6%</td>
<td align="right">6,115,120</td>
<td align="right">83.2%</td>
<td align="right">190.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">472,220</td>
<td align="right">18.3%</td>
<td align="right">1,227,220</td>
<td align="right">16.7%</td>
<td align="right">159.9%</td>
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
<td align="right">1,940</td>
<td align="right">81.5%</td>
<td align="right">3,060</td>
<td align="right">87.4%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">440</td>
<td align="right">18.5%</td>
<td align="right">440</td>
<td align="right">12.6%</td>
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
<td align="right">860</td>
<td align="right">44.3%</td>
<td align="right">1,640</td>
<td align="right">53.6%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">280</td>
<td align="right">14.4%</td>
<td align="right">460</td>
<td align="right">15.0%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">440</td>
<td align="right">22.7%</td>
<td align="right">600</td>
<td align="right">19.6%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">360</td>
<td align="right">18.6%</td>
<td align="right">360</td>
<td align="right">11.8%</td>
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
<td align="right">3,032,280</td>
<td align="right">1.4%</td>
<td align="right">5,847,620</td>
<td align="right">2.5%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,425,540</td>
<td align="right">3.8%</td>
<td align="right">12,240,460</td>
<td align="right">5.3%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">212,974,640</td>
<td align="right">94.9%</td>
<td align="right">212,362,280</td>
<td align="right">92.1%</td>
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
<td align="right">633,420</td>
<td align="right">0.3%</td>
<td align="right">633,420</td>
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
<td align="right">69,820</td>
<td align="right">76.6%</td>
<td align="right">122,940</td>
<td align="right">84.5%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,280</td>
<td align="right">23.4%</td>
<td align="right">22,520</td>
<td align="right">15.5%</td>
<td align="right">5.8%</td>
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
<td align="left">mutable class</td>
<td align="right">17,040</td>
<td align="right">80.1%</td>
<td align="right">18,200</td>
<td align="right">80.8%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">620</td>
<td align="right">2.9%</td>
<td align="right">660</td>
<td align="right">2.9%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,240</td>
<td align="right">15.2%</td>
<td align="right">3,240</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.6%</td>
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
<td align="right">27,161,340</td>
<td align="right">100.0%</td>
<td align="right">37,883,180</td>
<td align="right">100.0%</td>
<td align="right">39.5%</td>
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
<td align="right">2,134,920</td>
<td align="right">4.4%</td>
<td align="right">3,359,720</td>
<td align="right">6.8%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,139,000</td>
<td align="right">95.6%</td>
<td align="right">45,747,260</td>
<td align="right">93.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">41,500</td>
<td align="right">100.0%</td>
<td align="right">64,640</td>
<td align="right">100.0%</td>
<td align="right">55.8%</td>
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
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
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
<td align="right">230,280</td>
<td align="right">99.9%</td>
<td align="right">230,280</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,100</td>
<td align="right">0.1%</td>
<td align="right">78,580</td>
<td align="right">0.2%</td>
<td align="right">213.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,875,160</td>
<td align="right">3.8%</td>
<td align="right">5,094,500</td>
<td align="right">9.9%</td>
<td align="right">171.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,162,260</td>
<td align="right">96.1%</td>
<td align="right">46,344,980</td>
<td align="right">90.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">39,460</td>
<td align="right">98.9%</td>
<td align="right">100,120</td>
<td align="right">99.5%</td>
<td align="right">153.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">440</td>
<td align="right">1.1%</td>
<td align="right">480</td>
<td align="right">0.5%</td>
<td align="right">9.1%</td>
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
<td align="right">200</td>
<td align="right">41.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">31.8%</td>
<td align="right">140</td>
<td align="right">29.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">140</td>
<td align="right">31.8%</td>
<td align="right">140</td>
<td align="right">29.2%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">5,186,360</td>
<td align="right">100.0%</td>
<td align="right">5,186,360</td>
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
<td align="right">228,286,920</td>
<td align="right">42.4%</td>
<td align="right">439,589,300</td>
<td align="right">43.8%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">283,462,380</td>
<td align="right">52.7%</td>
<td align="right">516,970,380</td>
<td align="right">51.5%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">17,070,020</td>
<td align="right">3.2%</td>
<td align="right">30,546,760</td>
<td align="right">3.0%</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,505,600</td>
<td align="right">1.8%</td>
<td align="right">16,780,140</td>
<td align="right">1.7%</td>
<td align="right">76.5%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">441,000</td>
<td align="right">1.4%</td>
<td align="right">7,503.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">15,500</td>
<td align="right">0.1%</td>
<td align="right">798,160</td>
<td align="right">2.6%</td>
<td align="right">5,049.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,660</td>
<td align="right">0.0%</td>
<td align="right">46,380</td>
<td align="right">0.2%</td>
<td align="right">719.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">25,100</td>
<td align="right">0.1%</td>
<td align="right">78,580</td>
<td align="right">0.3%</td>
<td align="right">213.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,105,140</td>
<td align="right">12.4%</td>
<td align="right">6,115,120</td>
<td align="right">20.1%</td>
<td align="right">190.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,409,500</td>
<td align="right">37.7%</td>
<td align="right">10,745,360</td>
<td align="right">35.3%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,425,540</td>
<td align="right">49.5%</td>
<td align="right">12,240,460</td>
<td align="right">40.2%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8,780</td>
<td align="right">0.1%</td>
<td align="right">8,780</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">567,420</td>
<td align="right">6.0%</td>
<td align="right">2,361,420</td>
<td align="right">14.1%</td>
<td align="right">316.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">664,480</td>
<td align="right">7.0%</td>
<td align="right">1,804,600</td>
<td align="right">10.7%</td>
<td align="right">171.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">820,140</td>
<td align="right">8.6%</td>
<td align="right">1,853,440</td>
<td align="right">11.0%</td>
<td align="right">126.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,630,140</td>
<td align="right">17.1%</td>
<td align="right">3,305,360</td>
<td align="right">19.7%</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,134,920</td>
<td align="right">22.5%</td>
<td align="right">3,359,720</td>
<td align="right">20.0%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">813,500</td>
<td align="right">8.6%</td>
<td align="right">813,500</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">799,000</td>
<td align="right">8.4%</td>
<td align="right">799,000</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">706,480</td>
<td align="right">7.4%</td>
<td align="right">706,480</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">407,040</td>
<td align="right">4.3%</td>
<td align="right">407,040</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">406,760</td>
<td align="right">4.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">524,540</td>
<td align="right">3.1%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">3,300</td>
<td align="right">0.0%</td>
<td align="right">2,650.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">37,840</td>
<td align="right">0.1%</td>
<td align="right">148,800</td>
<td align="right">0.3%</td>
<td align="right">293.2%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">275,436,700</td>
<td align="right">275,436,700 / 0 !!</td>
<td align="right">476,556,200</td>
<td align="right">476,556,200 / 0 !!</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">331,388,560</td>
<td align="right">331,388,560 / 0 !!</td>
<td align="right">535,628,400</td>
<td align="right">535,628,400 / 0 !!</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">423,483,764</td>
<td align="right">423,483,764 / 0 !!</td>
<td align="right">189,618,552</td>
<td align="right">189,618,552 / 0 !!</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">435,608,214</td>
<td align="right">435,608,214 / 0 !!</td>
<td align="right">204,645,409</td>
<td align="right">204,645,409 / 0 !!</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">80,708</td>
<td align="right"></td>
<td align="right">97,304</td>
<td align="right"></td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,180,719</td>
<td align="right"></td>
<td align="right">1,395,647</td>
<td align="right"></td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,103,617</td>
<td align="right"></td>
<td align="right">1,301,905</td>
<td align="right"></td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">33,262,843</td>
<td align="right"></td>
<td align="right">34,163,175</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,137,840</td>
<td align="right"></td>
<td align="right">11,220,720</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,139,260</td>
<td align="right">23.1%</td>
<td align="right">11,222,100</td>
<td align="right">23.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">36,617,597</td>
<td align="right"></td>
<td align="right">36,782,772</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">37,076,740</td>
<td align="right">76.9%</td>
<td align="right">37,211,080</td>
<td align="right">76.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">14,810,952</td>
<td align="right"></td>
<td align="right">14,788,476</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">37,038,780</td>
<td align="right">76.8%</td>
<td align="right">37,058,980</td>
<td align="right">76.5%</td>
<td align="right">0.1%</td>
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
<td align="right">800</td>
<td align="right">1,099,860</td>
<td align="right">15,220,040</td>
<td align="right">800</td>
<td align="right">1,097,940</td>
<td align="right">15,194,320</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">3,240</td>
<td align="right">2.3%</td>
<td align="right">16,100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">360</td>
<td align="right">4.4%</td>
<td align="right">15,640</td>
<td align="right">11.2%</td>
<td align="right">4,244.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">300</td>
<td align="right">3.7%</td>
<td align="right">12,760</td>
<td align="right">9.1%</td>
<td align="right">4,153.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">4,300</td>
<td align="right">53.1%</td>
<td align="right">138,140</td>
<td align="right">98.9%</td>
<td align="right">3,112.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">8,100</td>
<td align="right"></td>
<td align="right">139,700</td>
<td align="right"></td>
<td align="right">1,624.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">4,560</td>
<td align="right">56.3%</td>
<td align="right">24,500</td>
<td align="right">17.5%</td>
<td align="right">437.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">36,368,020</td>
<td align="right"></td>
<td align="right">6,114,440</td>
<td align="right"></td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,199,397,900</td>
<td align="right">3,297.9%</td>
<td align="right">401,117,520</td>
<td align="right">6,560.2%</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,700</td>
<td align="right">45.7%</td>
<td align="right">1,420</td>
<td align="right">1.0%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">100</td>
<td align="right">1.2%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">40.0%</td>
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
<td align="right">3,780</td>
<td align="right">87.9%</td>
<td align="right">136,760</td>
<td align="right">99.0%</td>
<td align="right">3,518.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">4,300</td>
<td align="right"></td>
<td align="right">138,140</td>
<td align="right"></td>
<td align="right">3,112.6%</td>
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
<td align="right">1.4%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">180</td>
<td align="right">4.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">760</td>
<td align="right">17.7%</td>
<td align="right">1,120</td>
<td align="right">0.8%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">640</td>
<td align="right">14.9%</td>
<td align="right">15,280</td>
<td align="right">11.1%</td>
<td align="right">2,287.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">560</td>
<td align="right">13.0%</td>
<td align="right">33,860</td>
<td align="right">24.5%</td>
<td align="right">5,946.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">920</td>
<td align="right">21.4%</td>
<td align="right">41,820</td>
<td align="right">30.3%</td>
<td align="right">4,445.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">720</td>
<td align="right">16.7%</td>
<td align="right">29,600</td>
<td align="right">21.4%</td>
<td align="right">4,011.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">460</td>
<td align="right">10.7%</td>
<td align="right">14,860</td>
<td align="right">10.8%</td>
<td align="right">3,130.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">1.4%</td>
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">2,566.7%</td>
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
<td align="right">860</td>
<td align="right">20.0%</td>
<td align="right">1,120</td>
<td align="right">0.8%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">480</td>
<td align="right">11.2%</td>
<td align="right">14,340</td>
<td align="right">10.4%</td>
<td align="right">2,887.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">600</td>
<td align="right">14.0%</td>
<td align="right">22,120</td>
<td align="right">16.0%</td>
<td align="right">3,586.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">720</td>
<td align="right">16.7%</td>
<td align="right">33,300</td>
<td align="right">24.1%</td>
<td align="right">4,525.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">580</td>
<td align="right">13.5%</td>
<td align="right">47,880</td>
<td align="right">34.7%</td>
<td align="right">8,155.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">360</td>
<td align="right">8.4%</td>
<td align="right">9,540</td>
<td align="right">6.9%</td>
<td align="right">2,550.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">180</td>
<td align="right">4.2%</td>
<td align="right">8,460</td>
<td align="right">6.1%</td>
<td align="right">4,600.0%</td>
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
<td align="left">_BUILD_MAP</td>
<td align="right">38,820</td>
<td align="right">40</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">230,920</td>
<td align="right">1,320</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,193,200</td>
<td align="right">17,880</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">3,520</td>
<td align="right">40</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">686,100</td>
<td align="right">10,680</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">732,060</td>
<td align="right">18,360</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,143,160</td>
<td align="right">47,700</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,259,260</td>
<td align="right">61,800</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">858,940</td>
<td align="right">42,700</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,110,920</td>
<td align="right">65,420</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,343,380</td>
<td align="right">207,120</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">972,680</td>
<td align="right">62,320</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">554,880</td>
<td align="right">37,560</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,501,160</td>
<td align="right">112,800</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,501,160</td>
<td align="right">112,800</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">528,480</td>
<td align="right">50,480</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">50,760</td>
<td align="right">5,000</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">4,922,400</td>
<td align="right">535,860</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">386,360</td>
<td align="right">50,960</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,347,680</td>
<td align="right">188,080</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">6,926,600</td>
<td align="right">971,540</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">31,560</td>
<td align="right">4,760</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">31,560</td>
<td align="right">4,760</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,466,160</td>
<td align="right">229,860</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">34,857,560</td>
<td align="right">5,855,300</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">36,368,020</td>
<td align="right">6,114,440</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">10,504,660</td>
<td align="right">1,822,960</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">4,356,940</td>
<td align="right">780,520</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,968,940</td>
<td align="right">358,620</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">5,305,560</td>
<td align="right">969,700</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,052,160</td>
<td align="right">1,194,380</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,290,800</td>
<td align="right">656,760</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">8,496,380</td>
<td align="right">1,763,820</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,368,140</td>
<td align="right">285,020</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">22,400</td>
<td align="right">4,720</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">22,400</td>
<td align="right">4,720</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,984,980</td>
<td align="right">850,780</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,468,480</td>
<td align="right">958,620</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">19,978,300</td>
<td align="right">4,288,740</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">971,840</td>
<td align="right">213,060</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,694,280</td>
<td align="right">1,741,280</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">582,000</td>
<td align="right">132,400</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">15,549,220</td>
<td align="right">3,797,740</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">61,160</td>
<td align="right">15,320</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,764,140</td>
<td align="right">1,792,340</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,789,320</td>
<td align="right">478,540</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,675,740</td>
<td align="right">1,005,460</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">13,882,980</td>
<td align="right">3,928,740</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">6,057,200</td>
<td align="right">1,787,300</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">11,517,680</td>
<td align="right">3,421,660</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,558,400</td>
<td align="right">477,220</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">297,800</td>
<td align="right">94,100</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,200,900</td>
<td align="right">3,887,860</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,319,380</td>
<td align="right">3,929,640</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,093,280</td>
<td align="right">668,000</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">868,560</td>
<td align="right">278,140</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">507,580</td>
<td align="right">166,780</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">507,580</td>
<td align="right">166,780</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">363,660</td>
<td align="right">120,080</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,368,100</td>
<td align="right">7,177,400</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">157,497,060</td>
<td align="right">53,141,960</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,001,600</td>
<td align="right">3,045,920</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">8,067,000</td>
<td align="right">2,732,380</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,860,740</td>
<td align="right">632,100</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,844,080</td>
<td align="right">3,690,340</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">72,725,060</td>
<td align="right">24,847,220</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,773,260</td>
<td align="right">957,960</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,249,700</td>
<td align="right">1,123,460</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">150,579,820</td>
<td align="right">52,826,720</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">64,210,400</td>
<td align="right">22,561,380</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">39,664,140</td>
<td align="right">13,950,040</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">105,905,880</td>
<td align="right">37,593,340</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,139,340</td>
<td align="right">2,902,700</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">30,698,900</td>
<td align="right">10,951,740</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">722,840</td>
<td align="right">260,800</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">8,095,660</td>
<td align="right">2,939,520</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,975,000</td>
<td align="right">3,699,780</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,379,140</td>
<td align="right">2,369,160</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">696,000</td>
<td align="right">260,800</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">13,850,240</td>
<td align="right">5,197,600</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">13,790,720</td>
<td align="right">5,202,320</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,316,060</td>
<td align="right">5,410,660</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,825,220</td>
<td align="right">2,598,800</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">34,019,680</td>
<td align="right">12,994,000</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">896,040</td>
<td align="right">344,000</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">13,523,520</td>
<td align="right">5,196,500</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">13,729,420</td>
<td align="right">5,293,700</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,214,200</td>
<td align="right">5,485,820</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,294,620</td>
<td align="right">907,000</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">25,176,080</td>
<td align="right">10,022,200</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">28,098,920</td>
<td align="right">11,553,260</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">526,080</td>
<td align="right">225,040</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">725,120</td>
<td align="right">310,920</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">725,120</td>
<td align="right">310,920</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">10,042,200</td>
<td align="right">4,341,260</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,203,800</td>
<td align="right">558,760</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">85,440</td>
<td align="right">41,780</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,058,280</td>
<td align="right">1,077,060</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">169,140</td>
<td align="right">88,560</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,776,500</td>
<td align="right">993,840</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,179,240</td>
<td align="right">678,220</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">4,988,980</td>
<td align="right">2,903,080</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,786,240</td>
<td align="right">2,410,900</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">44,300</td>
<td align="right">29,280</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,355,500</td>
<td align="right">2,390,100</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">766,300</td>
<td align="right">548,540</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,960</td>
<td align="right">9,440</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,960</td>
<td align="right">9,440</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">79,840</td>
<td align="right">62,320</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">682,840</td>
<td align="right">563,960</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">107,280</td>
<td align="right">90,620</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">64,740</td>
<td align="right">71,080</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">64,740</td>
<td align="right">71,080</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">91,660</td>
<td align="right">90,500</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">809,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">288,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">189,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">40,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">35,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">33,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">31,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">24,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">21,120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">14,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">7,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">6,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,800</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,800</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,720</td>
<td align="right">4,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">3,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">8,504,540</td>
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
<td align="right">160</td>
<td align="right">9,600</td>
<td align="right">5,900.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
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
Stats gathered on: 2024-09-23
