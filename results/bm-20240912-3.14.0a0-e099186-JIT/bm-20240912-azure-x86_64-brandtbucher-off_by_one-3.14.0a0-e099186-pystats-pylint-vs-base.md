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
<td align="left">CALL_TYPE_1</td>
<td align="right">536,860</td>
<td align="right">1,469,880</td>
<td align="right">173.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">57,020</td>
<td align="right">85,080</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,901,110</td>
<td align="right">3,528,652</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">432,380</td>
<td align="right">356,690</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">7,600,260</td>
<td align="right">6,289,860</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,503,908</td>
<td align="right">6,443,236</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">25,431,300</td>
<td align="right">28,950,920</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,104,383</td>
<td align="right">13,044,167</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,785,580</td>
<td align="right">2,958,220</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,587,944</td>
<td align="right">1,514,184</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">296,695</td>
<td align="right">283,126</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">50,658,594</td>
<td align="right">48,969,789</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">88,459,958</td>
<td align="right">90,537,877</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">44,178,601</td>
<td align="right">45,210,270</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">44,535,395</td>
<td align="right">45,467,231</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">52,125,896</td>
<td align="right">53,206,533</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">71,000</td>
<td align="right">69,620</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,009,226</td>
<td align="right">9,174,324</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">33,321,275</td>
<td align="right">33,927,924</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,974,255</td>
<td align="right">2,004,991</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,020,835</td>
<td align="right">2,051,271</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">299,123,763</td>
<td align="right">303,266,258</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,500</td>
<td align="right">4,440</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">64,816,928</td>
<td align="right">65,563,174</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,942,598</td>
<td align="right">3,897,840</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,880</td>
<td align="right">11,760</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,074,460</td>
<td align="right">5,029,540</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">750,160</td>
<td align="right">756,720</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,117,320</td>
<td align="right">1,107,880</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,472,760</td>
<td align="right">5,511,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">577,840</td>
<td align="right">574,240</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">25,350,740</td>
<td align="right">25,508,300</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,440</td>
<td align="right">3,420</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">32,740,540</td>
<td align="right">32,583,924</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">933,480</td>
<td align="right">929,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">9,260</td>
<td align="right">9,220</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,590,714</td>
<td align="right">5,613,526</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">29,429,910</td>
<td align="right">29,318,516</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">23,520</td>
<td align="right">23,440</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,700</td>
<td align="right">171,140</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,330</td>
<td align="right">47,177</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,526,780</td>
<td align="right">2,519,232</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,500</td>
<td align="right">13,540</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,733,410</td>
<td align="right">14,697,044</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">66,680</td>
<td align="right">66,520</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,887,144</td>
<td align="right">32,808,572</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,768,460</td>
<td align="right">2,774,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">101,180</td>
<td align="right">101,400</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">16,984,660</td>
<td align="right">17,019,820</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">891,360</td>
<td align="right">889,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,276,200</td>
<td align="right">10,296,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,096,650</td>
<td align="right">5,086,620</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">430,000</td>
<td align="right">429,220</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">743,240</td>
<td align="right">741,980</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">36,060</td>
<td align="right">36,000</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60,452,861</td>
<td align="right">60,353,961</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,821,820</td>
<td align="right">2,817,280</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">24,125,573</td>
<td align="right">24,087,104</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,052,414</td>
<td align="right">1,050,746</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,431,380</td>
<td align="right">2,427,560</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">76,700</td>
<td align="right">76,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,706,119</td>
<td align="right">78,610,554</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,562,880</td>
<td align="right">1,561,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,633,155</td>
<td align="right">1,634,871</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,458,513</td>
<td align="right">2,456,006</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">363,520</td>
<td align="right">363,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,148,320</td>
<td align="right">2,146,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">123,100</td>
<td align="right">122,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,944,620</td>
<td align="right">5,938,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">104,860</td>
<td align="right">104,760</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,076,820</td>
<td align="right">4,080,680</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,976,200</td>
<td align="right">1,974,420</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">344,428</td>
<td align="right">344,736</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,119,000</td>
<td align="right">2,117,120</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,780,155</td>
<td align="right">8,772,391</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">45,460</td>
<td align="right">45,420</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,574,620</td>
<td align="right">2,572,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,438,160</td>
<td align="right">1,439,380</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,862,780</td>
<td align="right">2,860,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,375,505</td>
<td align="right">3,378,271</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,442,360</td>
<td align="right">1,441,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,258,115</td>
<td align="right">5,254,166</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">123,280</td>
<td align="right">123,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">86,304</td>
<td align="right">86,252</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,656,560</td>
<td align="right">2,655,040</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,909,540</td>
<td align="right">5,906,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,837,660</td>
<td align="right">4,840,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,378,400</td>
<td align="right">18,368,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,008,655</td>
<td align="right">3,007,104</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,963,000</td>
<td align="right">2,961,500</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,740,200</td>
<td align="right">3,738,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,680,610</td>
<td align="right">2,679,492</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,157,240</td>
<td align="right">7,154,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">58,929,098</td>
<td align="right">58,949,951</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,732,520</td>
<td align="right">1,731,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,405,780</td>
<td align="right">1,406,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">564,660</td>
<td align="right">564,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,226,834</td>
<td align="right">11,223,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,932,259</td>
<td align="right">4,930,789</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,209,920</td>
<td align="right">3,208,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,467,200</td>
<td align="right">6,468,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">479,140</td>
<td align="right">479,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">26,718,800</td>
<td align="right">26,712,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,646,940</td>
<td align="right">2,646,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">341,900</td>
<td align="right">341,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,753,168</td>
<td align="right">1,752,776</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,752,929</td>
<td align="right">1,752,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,310,480</td>
<td align="right">3,309,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">195,900</td>
<td align="right">195,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">6,765,720</td>
<td align="right">6,764,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">15,688,480</td>
<td align="right">15,691,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,393,820</td>
<td align="right">1,393,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,386,960</td>
<td align="right">3,386,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,872,880</td>
<td align="right">8,871,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">39,370,566</td>
<td align="right">39,375,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,442,431</td>
<td align="right">58,449,397</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">26,476,820</td>
<td align="right">26,474,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,016,450</td>
<td align="right">1,016,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,096,764</td>
<td align="right">4,096,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">7,064,480</td>
<td align="right">7,065,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">544,600</td>
<td align="right">544,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">545,440</td>
<td align="right">545,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,656,780</td>
<td align="right">1,656,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,803,400</td>
<td align="right">1,803,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,630,300</td>
<td align="right">5,629,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,488,640</td>
<td align="right">6,488,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">370,120</td>
<td align="right">370,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">759,760</td>
<td align="right">759,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">75,694,239</td>
<td align="right">75,690,702</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">675,940</td>
<td align="right">675,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,056,260</td>
<td align="right">5,056,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">3,201,240</td>
<td align="right">3,201,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">60,409,918</td>
<td align="right">60,409,016</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,368,320</td>
<td align="right">6,368,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,511,750</td>
<td align="right">37,511,857</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">74,547,734</td>
<td align="right">74,547,712</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,823,340</td>
<td align="right">16,823,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">10,680,120</td>
<td align="right">10,680,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,589,060</td>
<td align="right">8,589,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,543,520</td>
<td align="right">3,543,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,947,400</td>
<td align="right">1,947,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,590,080</td>
<td align="right">1,590,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,413,980</td>
<td align="right">1,413,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,055,620</td>
<td align="right">1,055,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,050,600</td>
<td align="right">1,050,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">608,500</td>
<td align="right">608,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">475,640</td>
<td align="right">475,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">270,540</td>
<td align="right">270,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">265,920</td>
<td align="right">265,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">241,120</td>
<td align="right">241,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">199,480</td>
<td align="right">199,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">179,300</td>
<td align="right">179,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,060</td>
<td align="right">157,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">108,360</td>
<td align="right">108,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,340</td>
<td align="right">91,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">73,400</td>
<td align="right">73,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60,500</td>
<td align="right">60,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">25,800</td>
<td align="right">25,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">23,260</td>
<td align="right">23,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20,540</td>
<td align="right">20,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,580</td>
<td align="right">13,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,720</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">10,200</td>
<td align="right">10,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">7,020</td>
<td align="right">7,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">4,720</td>
<td align="right">4,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,580</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,220</td>
<td align="right">4,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">340</td>
<td align="right">340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
<td align="right">921,020</td>
<td align="right">9.8%</td>
<td align="right">917,000</td>
<td align="right">9.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,460,620</td>
<td align="right">90.1%</td>
<td align="right">8,460,620</td>
<td align="right">90.1%</td>
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
<td align="right">9,220</td>
<td align="right">74.0%</td>
<td align="right">9,200</td>
<td align="right">74.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,240</td>
<td align="right">26.0%</td>
<td align="right">3,240</td>
<td align="right">26.0%</td>
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
<td align="left">and int</td>
<td align="right">1,520</td>
<td align="right">16.5%</td>
<td align="right">1,500</td>
<td align="right">16.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,380</td>
<td align="right">36.7%</td>
<td align="right">3,380</td>
<td align="right">36.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">900</td>
<td align="right">9.8%</td>
<td align="right">900</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">720</td>
<td align="right">7.8%</td>
<td align="right">720</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">660</td>
<td align="right">7.2%</td>
<td align="right">660</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">540</td>
<td align="right">5.9%</td>
<td align="right">540</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">400</td>
<td align="right">4.3%</td>
<td align="right">400</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">743,240</td>
<td align="right">100.0%</td>
<td align="right">741,980</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,420,380</td>
<td align="right">6.6%</td>
<td align="right">1,421,600</td>
<td align="right">6.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,111,780</td>
<td align="right">93.1%</td>
<td align="right">20,111,834</td>
<td align="right">93.1%</td>
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
<td align="right">44,880</td>
<td align="right">0.2%</td>
<td align="right">44,880</td>
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
<td align="left">Success</td>
<td align="right">9,720</td>
<td align="right">52.4%</td>
<td align="right">9,720</td>
<td align="right">52.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,820</td>
<td align="right">47.6%</td>
<td align="right">8,820</td>
<td align="right">47.6%</td>
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
<td align="right">3,740</td>
<td align="right">42.4%</td>
<td align="right">3,740</td>
<td align="right">42.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,660</td>
<td align="right">30.2%</td>
<td align="right">2,660</td>
<td align="right">30.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,880</td>
<td align="right">21.3%</td>
<td align="right">1,880</td>
<td align="right">21.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">11,676,240</td>
<td align="right">7.7%</td>
<td align="right">12,440,560</td>
<td align="right">8.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">139,537,410</td>
<td align="right">92.1%</td>
<td align="right">138,196,756</td>
<td align="right">91.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,020</td>
<td align="right">0.1%</td>
<td align="right">140,020</td>
<td align="right">0.1%</td>
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
<td align="right">337,240</td>
<td align="right">100.0%</td>
<td align="right">353,540</td>
<td align="right">100.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="left">init not simple</td>
<td align="right">480</td>
<td align="right">2,400.0%</td>
<td align="right">480</td>
<td align="right">2,400.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">300</td>
<td align="right">1,500.0%</td>
<td align="right">300</td>
<td align="right">1,500.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">431,660</td>
<td align="right">95.5%</td>
<td align="right">530,720</td>
<td align="right">96.3%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,780</td>
<td align="right">2.4%</td>
<td align="right">10,780</td>
<td align="right">2.0%</td>
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
<td align="right">6,280</td>
<td align="right">0.0%</td>
<td align="right">5,220</td>
<td align="right">0.0%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,236,375</td>
<td align="right">10.6%</td>
<td align="right">5,232,486</td>
<td align="right">10.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,194,015</td>
<td align="right">89.4%</td>
<td align="right">44,194,031</td>
<td align="right">89.4%</td>
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
<td align="right">10,320</td>
<td align="right">47.2%</td>
<td align="right">10,260</td>
<td align="right">47.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,540</td>
<td align="right">52.8%</td>
<td align="right">11,520</td>
<td align="right">52.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">3,000</td>
<td align="right">29.1%</td>
<td align="right">2,940</td>
<td align="right">28.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,160</td>
<td align="right">40.3%</td>
<td align="right">4,160</td>
<td align="right">40.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">980</td>
<td align="right">9.5%</td>
<td align="right">980</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">860</td>
<td align="right">8.3%</td>
<td align="right">860</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">360</td>
<td align="right">3.5%</td>
<td align="right">360</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">3.3%</td>
<td align="right">340</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">2,436,753</td>
<td align="right">21.2%</td>
<td align="right">2,434,246</td>
<td align="right">21.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,002,760</td>
<td align="right">78.3%</td>
<td align="right">9,002,760</td>
<td align="right">78.4%</td>
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
<td align="right">31,300</td>
<td align="right">0.3%</td>
<td align="right">31,300</td>
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
<td align="right">4,780</td>
<td align="right">21.4%</td>
<td align="right">4,780</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">17,560</td>
<td align="right">78.6%</td>
<td align="right">17,560</td>
<td align="right">78.6%</td>
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
<td align="right">8,200</td>
<td align="right">46.7%</td>
<td align="right">8,200</td>
<td align="right">46.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3,740</td>
<td align="right">21.3%</td>
<td align="right">3,740</td>
<td align="right">21.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,360</td>
<td align="right">19.1%</td>
<td align="right">3,360</td>
<td align="right">19.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,260</td>
<td align="right">12.9%</td>
<td align="right">2,260</td>
<td align="right">12.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">102,600</td>
<td align="right">0.4%</td>
<td align="right">100,920</td>
<td align="right">0.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,403,200</td>
<td align="right">9.3%</td>
<td align="right">2,399,580</td>
<td align="right">9.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,406,874</td>
<td align="right">90.2%</td>
<td align="right">23,428,646</td>
<td align="right">90.3%</td>
<td align="right">0.1%</td>
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
<td align="right">15,100</td>
<td align="right">50.3%</td>
<td align="right">14,920</td>
<td align="right">50.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,940</td>
<td align="right">49.7%</td>
<td align="right">14,880</td>
<td align="right">49.9%</td>
<td align="right">-0.4%</td>
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
<td align="left">seq iter</td>
<td align="right">180</td>
<td align="right">1.2%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">460</td>
<td align="right">3.0%</td>
<td align="right">440</td>
<td align="right">2.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,680</td>
<td align="right">17.7%</td>
<td align="right">2,700</td>
<td align="right">18.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">3,960</td>
<td align="right">26.2%</td>
<td align="right">3,940</td>
<td align="right">26.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,040</td>
<td align="right">20.1%</td>
<td align="right">3,040</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,700</td>
<td align="right">11.3%</td>
<td align="right">1,700</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,000</td>
<td align="right">6.6%</td>
<td align="right">1,000</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">680</td>
<td align="right">4.5%</td>
<td align="right">680</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">620</td>
<td align="right">4.1%</td>
<td align="right">620</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">400</td>
<td align="right">2.6%</td>
<td align="right">400</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">100</td>
<td align="right">0.7%</td>
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
<td align="right">25,063,940</td>
<td align="right">10.2%</td>
<td align="right">28,558,220</td>
<td align="right">11.4%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,260,669</td>
<td align="right">12.3%</td>
<td align="right">30,098,263</td>
<td align="right">12.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">190,298,154</td>
<td align="right">77.4%</td>
<td align="right">190,511,826</td>
<td align="right">76.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">427,380</td>
<td align="right">0.2%</td>
<td align="right">427,380</td>
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
<td align="left">Success</td>
<td align="right">848,740</td>
<td align="right">91.8%</td>
<td align="right">870,220</td>
<td align="right">91.9%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">75,540</td>
<td align="right">8.2%</td>
<td align="right">76,300</td>
<td align="right">8.1%</td>
<td align="right">1.0%</td>
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
<td align="right">14,980</td>
<td align="right">19.8%</td>
<td align="right">15,240</td>
<td align="right">20.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,460</td>
<td align="right">25.8%</td>
<td align="right">19,720</td>
<td align="right">25.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,240</td>
<td align="right">26.8%</td>
<td align="right">20,480</td>
<td align="right">26.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,300</td>
<td align="right">5.7%</td>
<td align="right">4,300</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,080</td>
<td align="right">5.4%</td>
<td align="right">4,080</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,640</td>
<td align="right">2.2%</td>
<td align="right">1,640</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,420</td>
<td align="right">1.9%</td>
<td align="right">1,420</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">1.5%</td>
<td align="right">1,140</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">820</td>
<td align="right">1.1%</td>
<td align="right">820</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">96,583,571</td>
<td align="right">99.7%</td>
<td align="right">98,596,084</td>
<td align="right">99.7%</td>
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
<td align="right">102,180</td>
<td align="right">0.1%</td>
<td align="right">102,180</td>
<td align="right">0.1%</td>
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
<td align="right">1,500</td>
<td align="right">0.0%</td>
<td align="right">1,500</td>
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
<td align="right">81,920</td>
<td align="right">0.1%</td>
<td align="right">81,920</td>
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
<td align="left">Success</td>
<td align="right">98,100</td>
<td align="right">100.0%</td>
<td align="right">98,100</td>
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
<td align="right">2,140</td>
<td align="right">0.1%</td>
<td align="right">2,140</td>
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
<td align="right">3,809,440</td>
<td align="right">99.9%</td>
<td align="right">3,809,440</td>
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
<td align="right">2,080</td>
<td align="right">100.0%</td>
<td align="right">2,080</td>
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
<td align="right">8,578,920</td>
<td align="right">55.4%</td>
<td align="right">8,578,920</td>
<td align="right">55.4%</td>
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
<td align="right">6,899,920</td>
<td align="right">44.5%</td>
<td align="right">6,899,920</td>
<td align="right">44.5%</td>
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
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,260</td>
<td align="right">91.3%</td>
<td align="right">9,260</td>
<td align="right">91.3%</td>
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
<td align="right">6,780</td>
<td align="right">73.2%</td>
<td align="right">6,780</td>
<td align="right">73.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">24.4%</td>
<td align="right">2,260</td>
<td align="right">24.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.4%</td>
<td align="right">220</td>
<td align="right">2.4%</td>
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
<td align="right">3,182,860</td>
<td align="right">6.3%</td>
<td align="right">3,181,920</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,054,980</td>
<td align="right">63.8%</td>
<td align="right">32,054,960</td>
<td align="right">63.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,000,900</td>
<td align="right">29.8%</td>
<td align="right">15,000,900</td>
<td align="right">29.8%</td>
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
<td align="right">295,480</td>
<td align="right">95.5%</td>
<td align="right">295,480</td>
<td align="right">95.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,980</td>
<td align="right">4.5%</td>
<td align="right">13,980</td>
<td align="right">4.5%</td>
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
<td align="left">not managed dict</td>
<td align="right">7,240</td>
<td align="right">51.8%</td>
<td align="right">7,240</td>
<td align="right">51.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,020</td>
<td align="right">21.6%</td>
<td align="right">3,020</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,340</td>
<td align="right">9.6%</td>
<td align="right">1,340</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">1.1%</td>
<td align="right">160</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">4,720</td>
<td align="right">100.0%</td>
<td align="right">4,720</td>
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
<td align="right">119,760</td>
<td align="right">2.7%</td>
<td align="right">119,680</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,394,840</td>
<td align="right">97.3%</td>
<td align="right">4,394,840</td>
<td align="right">97.3%</td>
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
<td align="right">2,060</td>
<td align="right">58.5%</td>
<td align="right">2,060</td>
<td align="right">58.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,460</td>
<td align="right">41.5%</td>
<td align="right">1,460</td>
<td align="right">41.5%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">800</td>
<td align="right">54.8%</td>
<td align="right">800</td>
<td align="right">54.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">260</td>
<td align="right">17.8%</td>
<td align="right">260</td>
<td align="right">17.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">160</td>
<td align="right">11.0%</td>
<td align="right">160</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">120</td>
<td align="right">8.2%</td>
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
<td align="right">985,834</td>
<td align="right">0.9%</td>
<td align="right">984,166</td>
<td align="right">0.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,039,840</td>
<td align="right">1.8%</td>
<td align="right">2,036,800</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">110,849,044</td>
<td align="right">97.3%</td>
<td align="right">110,846,509</td>
<td align="right">97.3%</td>
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
<td align="right">20,000</td>
<td align="right">19.3%</td>
<td align="right">19,980</td>
<td align="right">19.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">83,760</td>
<td align="right">80.7%</td>
<td align="right">83,700</td>
<td align="right">80.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,000</td>
<td align="right">5.0%</td>
<td align="right">980</td>
<td align="right">4.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,460</td>
<td align="right">67.3%</td>
<td align="right">13,460</td>
<td align="right">67.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,780</td>
<td align="right">8.9%</td>
<td align="right">1,780</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,360</td>
<td align="right">6.8%</td>
<td align="right">1,360</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,300</td>
<td align="right">6.5%</td>
<td align="right">1,300</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">780</td>
<td align="right">3.9%</td>
<td align="right">780</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,300</td>
<td align="right">0.0%</td>
<td align="right">7,180</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,676,119</td>
<td align="right">100.0%</td>
<td align="right">29,669,743</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">4,260</td>
<td align="right">93.0%</td>
<td align="right">4,260</td>
<td align="right">93.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">320</td>
<td align="right">7.0%</td>
<td align="right">320</td>
<td align="right">7.0%</td>
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
<td align="left">sequence</td>
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">80</td>
<td align="right">25.0%</td>
<td align="right">80</td>
<td align="right">25.0%</td>
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
<td align="right">52,150,822</td>
<td align="right">2.8%</td>
<td align="right">55,653,278</td>
<td align="right">3.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">615,756,931</td>
<td align="right">33.3%</td>
<td align="right">623,615,075</td>
<td align="right">33.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">59,679,939</td>
<td align="right">3.2%</td>
<td align="right">60,375,132</td>
<td align="right">3.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,119,745,577</td>
<td align="right">60.6%</td>
<td align="right">1,122,029,086</td>
<td align="right">60.3%</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">25,063,940</td>
<td align="right">48.8%</td>
<td align="right">28,558,220</td>
<td align="right">52.1%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">921,020</td>
<td align="right">1.8%</td>
<td align="right">917,000</td>
<td align="right">1.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">743,240</td>
<td align="right">1.4%</td>
<td align="right">741,980</td>
<td align="right">1.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">985,834</td>
<td align="right">1.9%</td>
<td align="right">984,166</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,403,200</td>
<td align="right">4.7%</td>
<td align="right">2,399,580</td>
<td align="right">4.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,436,753</td>
<td align="right">4.7%</td>
<td align="right">2,434,246</td>
<td align="right">4.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,420,380</td>
<td align="right">2.8%</td>
<td align="right">1,421,600</td>
<td align="right">2.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,236,375</td>
<td align="right">10.2%</td>
<td align="right">5,232,486</td>
<td align="right">9.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,182,860</td>
<td align="right">6.2%</td>
<td align="right">3,181,920</td>
<td align="right">5.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,578,920</td>
<td align="right">16.7%</td>
<td align="right">8,578,920</td>
<td align="right">15.6%</td>
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
<td align="right">1,474,520</td>
<td align="right">2.5%</td>
<td align="right">2,044,240</td>
<td align="right">3.4%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,798,860</td>
<td align="right">14.7%</td>
<td align="right">9,019,120</td>
<td align="right">14.9%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">610,880</td>
<td align="right">1.0%</td>
<td align="right">625,100</td>
<td align="right">1.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">4,730,260</td>
<td align="right">7.9%</td>
<td align="right">4,688,460</td>
<td align="right">7.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">14,826,160</td>
<td align="right">24.8%</td>
<td align="right">14,731,740</td>
<td align="right">24.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,821,960</td>
<td align="right">13.1%</td>
<td align="right">7,797,680</td>
<td align="right">12.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,385,020</td>
<td align="right">2.3%</td>
<td align="right">1,382,240</td>
<td align="right">2.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,999,640</td>
<td align="right">3.4%</td>
<td align="right">1,998,260</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">756,220</td>
<td align="right">1.3%</td>
<td align="right">755,760</td>
<td align="right">1.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">15,000,840</td>
<td align="right">25.1%</td>
<td align="right">15,000,840</td>
<td align="right">24.8%</td>
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
<td align="left">Frame objects created</td>
<td align="right">2,620,960</td>
<td align="right">1.8%</td>
<td align="right">2,619,240</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9,121,660</td>
<td align="right">6.2%</td>
<td align="right">9,120,000</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">38,385,950</td>
<td align="right">25.9%</td>
<td align="right">38,384,317</td>
<td align="right">25.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">38,385,950</td>
<td align="right">25.9%</td>
<td align="right">38,384,317</td>
<td align="right">25.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">780,210</td>
<td align="right">0.5%</td>
<td align="right">780,237</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">29,249,850</td>
<td align="right">19.8%</td>
<td align="right">29,249,877</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">29,264,290</td>
<td align="right">19.8%</td>
<td align="right">29,264,317</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">109,594,730</td>
<td align="right">74.1%</td>
<td align="right">109,594,677</td>
<td align="right">74.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">117,402,300</td>
<td align="right">79.3%</td>
<td align="right">117,402,354</td>
<td align="right">79.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,720</td>
<td align="right">0.0%</td>
<td align="right">3,720</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">890,900</td>
<td align="right">0.6%</td>
<td align="right">890,900</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">5,112,800</td>
<td align="right">3.5%</td>
<td align="right">5,112,800</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="left">Method cache misses</td>
<td align="right">4,708,402</td>
<td align="right"></td>
<td align="right">4,515,699</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,433,444</td>
<td align="right"></td>
<td align="right">5,233,792</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">809,177,567</td>
<td align="right">809,177,567 / 0 !!</td>
<td align="right">820,308,970</td>
<td align="right">820,308,970 / 0 !!</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">63,235,283</td>
<td align="right"></td>
<td align="right">62,511,835</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">753,957</td>
<td align="right"></td>
<td align="right">747,099</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">1,041,769,123</td>
<td align="right">1,041,769,123 / 0 !!</td>
<td align="right">1,050,512,497</td>
<td align="right">1,050,512,497 / 0 !!</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">125,270,836</td>
<td align="right"></td>
<td align="right">126,154,007</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">1,201,400,738</td>
<td align="right">1,201,400,738 / 0 !!</td>
<td align="right">1,193,692,239</td>
<td align="right">1,193,692,239 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">1,129,824,753</td>
<td align="right">1,129,824,753 / 0 !!</td>
<td align="right">1,124,502,003</td>
<td align="right">1,124,502,003 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">622,581</td>
<td align="right">0.3%</td>
<td align="right">622,925</td>
<td align="right">0.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">251,360</td>
<td align="right">0.1%</td>
<td align="right">251,340</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,585,883</td>
<td align="right"></td>
<td align="right">141,575,151</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">153,331,936</td>
<td align="right">68.6%</td>
<td align="right">153,325,794</td>
<td align="right">68.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">154,205,877</td>
<td align="right">69.0%</td>
<td align="right">154,200,059</td>
<td align="right">69.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">69,419,875</td>
<td align="right">31.0%</td>
<td align="right">69,419,791</td>
<td align="right">31.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">69,459,155</td>
<td align="right"></td>
<td align="right">69,459,071</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,405,600</td>
<td align="right"></td>
<td align="right">4,405,600</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">436,500</td>
<td align="right">9.9%</td>
<td align="right">436,500</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">39,240</td>
<td align="right">0.9%</td>
<td align="right">39,240</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
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
<td align="right">5,380</td>
<td align="right">82,020</td>
<td align="right">483,934,406</td>
<td align="right">5,380</td>
<td align="right">81,920</td>
<td align="right">483,926,564</td>
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
<td align="right">0.3%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">900</td>
<td align="right">1.3%</td>
<td align="right">940</td>
<td align="right">1.4%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">215,199,188</td>
<td align="right"></td>
<td align="right">221,490,206</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">33,179</td>
<td align="right">49.6%</td>
<td align="right">33,945</td>
<td align="right">50.4%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">32,598</td>
<td align="right">48.7%</td>
<td align="right">32,225</td>
<td align="right">47.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">33,780</td>
<td align="right">50.4%</td>
<td align="right">33,420</td>
<td align="right">49.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">66,959</td>
<td align="right"></td>
<td align="right">67,365</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,482,094,193</td>
<td align="right">1,153.4%</td>
<td align="right">2,471,693,171</td>
<td align="right">1,115.9%</td>
<td align="right">-0.4%</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">520</td>
<td align="right">1.6%</td>
<td align="right">520</td>
<td align="right">1.5%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">220</td>
<td align="right">0.7%</td>
<td align="right">260</td>
<td align="right">0.8%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">33,179</td>
<td align="right"></td>
<td align="right">33,945</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">32,499</td>
<td align="right">98.0%</td>
<td align="right">33,245</td>
<td align="right">97.9%</td>
<td align="right">2.3%</td>
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
<td align="right">720</td>
<td align="right">2.2%</td>
<td align="right">620</td>
<td align="right">1.8%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,718</td>
<td align="right">20.2%</td>
<td align="right">6,940</td>
<td align="right">20.4%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,180</td>
<td align="right">12.6%</td>
<td align="right">4,220</td>
<td align="right">12.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,861</td>
<td align="right">32.7%</td>
<td align="right">11,480</td>
<td align="right">33.8%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,040</td>
<td align="right">24.2%</td>
<td align="right">8,005</td>
<td align="right">23.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,400</td>
<td align="right">7.2%</td>
<td align="right">2,400</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">240</td>
<td align="right">0.7%</td>
<td align="right">260</td>
<td align="right">0.8%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">4,478</td>
<td align="right">13.5%</td>
<td align="right">4,440</td>
<td align="right">13.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,360</td>
<td align="right">13.1%</td>
<td align="right">4,520</td>
<td align="right">13.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">6,540</td>
<td align="right">19.7%</td>
<td align="right">6,900</td>
<td align="right">20.3%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">11,861</td>
<td align="right">35.7%</td>
<td align="right">12,045</td>
<td align="right">35.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,520</td>
<td align="right">13.6%</td>
<td align="right">4,560</td>
<td align="right">13.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">700</td>
<td align="right">2.1%</td>
<td align="right">740</td>
<td align="right">2.2%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">371,320</td>
<td align="right">1,669,940</td>
<td align="right">349.7%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,390,620</td>
<td align="right">3,400</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">969,060</td>
<td align="right">36,040</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,649,560</td>
<td align="right">717,560</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,268,792</td>
<td align="right">2,329,464</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,235,230</td>
<td align="right">3,209,048</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">325,540</td>
<td align="right">401,430</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">27,608,006</td>
<td align="right">33,301,772</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,696,850</td>
<td align="right">4,673,548</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">972,320</td>
<td align="right">799,680</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">972,320</td>
<td align="right">799,680</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,880,136</td>
<td align="right">4,936,196</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4,970,560</td>
<td align="right">5,704,140</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,019,800</td>
<td align="right">1,169,620</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">6,143,094</td>
<td align="right">5,350,334</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">18,502,852</td>
<td align="right">16,344,440</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">180</td>
<td align="right">200</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">20,008,412</td>
<td align="right">17,786,500</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">14,939,059</td>
<td align="right">13,294,698</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">35,080,000</td>
<td align="right">31,681,800</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">17,840,349</td>
<td align="right">16,185,838</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,704,675</td>
<td align="right">7,029,144</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">7,128,004</td>
<td align="right">7,690,712</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">16,121,455</td>
<td align="right">14,904,212</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">6,270,984</td>
<td align="right">6,679,732</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">35,573,770</td>
<td align="right">33,526,797</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">7,740</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,612,465</td>
<td align="right">8,147,536</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,080</td>
<td align="right">3,860</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">3,605,760</td>
<td align="right">3,425,680</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">130,720</td>
<td align="right">124,260</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">10,211,405</td>
<td align="right">9,718,936</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,256,660</td>
<td align="right">3,413,256</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,257,100</td>
<td align="right">3,413,696</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,077,738</td>
<td align="right">24,944,681</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">1,122,440</td>
<td align="right">1,079,220</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">183,294,975</td>
<td align="right">189,936,033</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">45,090,028</td>
<td align="right">43,458,470</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">572,720</td>
<td align="right">552,480</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">3,511,010</td>
<td align="right">3,621,324</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">2,040</td>
<td align="right">2,100</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">215,199,188</td>
<td align="right">221,490,206</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">425,280</td>
<td align="right">437,500</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">1,399,940</td>
<td align="right">1,439,700</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">30,937,142</td>
<td align="right">30,063,260</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">4,092,158</td>
<td align="right">4,206,416</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,687,576</td>
<td align="right">2,761,336</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,135,760</td>
<td align="right">3,051,560</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,793,845</td>
<td align="right">12,466,976</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">98,392,232</td>
<td align="right">96,315,652</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,021,505</td>
<td align="right">19,624,653</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,252,961</td>
<td align="right">4,331,340</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">28,042,029</td>
<td align="right">28,557,498</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">162,419,803</td>
<td align="right">159,525,518</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">2,280</td>
<td align="right">2,320</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,360,541</td>
<td align="right">23,956,318</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,240</td>
<td align="right">10,400</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,560</td>
<td align="right">2,600</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">496,220</td>
<td align="right">503,788</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">190,620</td>
<td align="right">187,780</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">5,400</td>
<td align="right">5,480</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,760,075</td>
<td align="right">26,375,773</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">304,620</td>
<td align="right">300,260</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,420</td>
<td align="right">1,440</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,716,281</td>
<td align="right">6,806,920</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">29,711,245</td>
<td align="right">29,317,073</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">707,700</td>
<td align="right">717,040</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">376,280</td>
<td align="right">381,220</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,016</td>
<td align="right">4,068</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,100</td>
<td align="right">3,140</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">367,040</td>
<td align="right">371,440</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">45,098,044</td>
<td align="right">45,631,001</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">6,452,474</td>
<td align="right">6,526,750</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">98,456,658</td>
<td align="right">97,391,067</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">9,680</td>
<td align="right">9,780</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,200</td>
<td align="right">4,240</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">2,100</td>
<td align="right">2,120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">2,100</td>
<td align="right">2,120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">2,100</td>
<td align="right">2,120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">19,185,328</td>
<td align="right">19,009,236</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">138,456,853</td>
<td align="right">139,652,819</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">9,540</td>
<td align="right">9,620</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">293,300</td>
<td align="right">295,560</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">300,620</td>
<td align="right">302,740</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">5,020,538</td>
<td align="right">5,054,600</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">9,960</td>
<td align="right">10,020</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">214,748,956</td>
<td align="right">216,038,091</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">29,380,194</td>
<td align="right">29,215,096</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">32,425,752</td>
<td align="right">32,251,680</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">9,072,496</td>
<td align="right">9,119,208</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">7,953,220</td>
<td align="right">7,918,060</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">4,660</td>
<td align="right">4,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">7,217,830</td>
<td align="right">7,186,880</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,244,620</td>
<td align="right">1,239,544</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">34,219,383</td>
<td align="right">34,350,711</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">377,400</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,225,720</td>
<td align="right">2,233,520</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">12,631,022</td>
<td align="right">12,674,820</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">990,380</td>
<td align="right">993,740</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">53,440</td>
<td align="right">53,620</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,312,500</td>
<td align="right">1,316,520</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">39,200</td>
<td align="right">39,080</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">20,545,776</td>
<td align="right">20,488,244</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,156,700</td>
<td align="right">6,172,760</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">86,920</td>
<td align="right">87,140</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">269,520</td>
<td align="right">270,200</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">392,220</td>
<td align="right">393,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">50,380</td>
<td align="right">50,500</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">965,580</td>
<td align="right">967,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,643,550</td>
<td align="right">2,637,840</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,647,264</td>
<td align="right">5,635,092</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">18,800</td>
<td align="right">18,840</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">18,800</td>
<td align="right">18,840</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">589,640</td>
<td align="right">590,820</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">589,640</td>
<td align="right">590,820</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">94,180</td>
<td align="right">94,360</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">927,760</td>
<td align="right">926,080</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,343,300</td>
<td align="right">1,345,720</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">33,440</td>
<td align="right">33,500</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,769,434</td>
<td align="right">25,814,728</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">197,220</td>
<td align="right">197,560</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">123,600</td>
<td align="right">123,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">347,940</td>
<td align="right">348,500</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">347,940</td>
<td align="right">348,500</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,546,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">79,260</td>
<td align="right">79,380</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">92,780</td>
<td align="right">92,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">21,373,226</td>
<td align="right">21,405,332</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">79,900</td>
<td align="right">80,020</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">241,640</td>
<td align="right">242,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">125,880</td>
<td align="right">126,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">127,340</td>
<td align="right">127,520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">258,560</td>
<td align="right">258,920</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">158,880</td>
<td align="right">159,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,021,370</td>
<td align="right">2,018,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">27,538,724</td>
<td align="right">27,501,612</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">60,980</td>
<td align="right">60,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">9,527,529</td>
<td align="right">9,538,892</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,085,040</td>
<td align="right">1,086,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">34,000,039</td>
<td align="right">33,961,434</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">42,735,200</td>
<td align="right">42,689,663</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">42,655,100</td>
<td align="right">42,616,563</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,982,380</td>
<td align="right">3,985,780</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,550,780</td>
<td align="right">4,546,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">21,237,095</td>
<td align="right">21,220,450</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,047,484</td>
<td align="right">4,044,432</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">641,780</td>
<td align="right">642,260</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,526,070</td>
<td align="right">1,527,208</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">8,118,940</td>
<td align="right">8,124,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">2,171,420</td>
<td align="right">2,172,940</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,577,120</td>
<td align="right">2,578,900</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">602,612</td>
<td align="right">603,004</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">126,240</td>
<td align="right">126,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,432,100</td>
<td align="right">4,429,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">8,682,840</td>
<td align="right">8,688,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,162,540</td>
<td align="right">2,163,780</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,382,200</td>
<td align="right">1,382,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">2,313,680</td>
<td align="right">2,314,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">6,778,566</td>
<td align="right">6,782,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,316,434</td>
<td align="right">3,314,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">3,414,820</td>
<td align="right">3,413,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,067,164</td>
<td align="right">5,064,692</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,468,430</td>
<td align="right">13,474,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">755,256</td>
<td align="right">755,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,354,800</td>
<td align="right">1,355,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,773,540</td>
<td align="right">2,772,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">875,440</td>
<td align="right">875,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,060,416</td>
<td align="right">1,060,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">807,712</td>
<td align="right">807,404</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,354,922</td>
<td align="right">1,355,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">396,780</td>
<td align="right">396,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">6,320,096</td>
<td align="right">6,321,602</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">30,985,364</td>
<td align="right">30,978,012</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">181,780</td>
<td align="right">181,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">55,379,669</td>
<td align="right">55,368,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,499,040</td>
<td align="right">7,500,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,224,800</td>
<td align="right">4,225,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,455,120</td>
<td align="right">7,456,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">127,340</td>
<td align="right">127,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,923,030</td>
<td align="right">4,923,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">6,104,500</td>
<td align="right">6,105,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,016,520</td>
<td align="right">1,016,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">529,580</td>
<td align="right">529,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">8,586,080</td>
<td align="right">8,585,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">30,466,584</td>
<td align="right">30,469,442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">38,436,462</td>
<td align="right">38,439,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,665,330</td>
<td align="right">1,665,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,085,400</td>
<td align="right">3,085,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">12,607,147</td>
<td align="right">12,606,578</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,169,160</td>
<td align="right">2,169,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">24,961,964</td>
<td align="right">24,962,172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">41,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">26,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">13,380</td>
<td align="right">13,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">9,900</td>
<td align="right">9,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">9,160</td>
<td align="right">9,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">5,980</td>
<td align="right">5,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">40</td>
<td align="right"></td>
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
<td align="right">1,020</td>
<td align="right">1,860</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">3,480</td>
<td align="right">3,320</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">460</td>
<td align="right">480</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right">40</td>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">320</td>
<td align="right">320</td>
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
Stats gathered on: 2024-10-21
