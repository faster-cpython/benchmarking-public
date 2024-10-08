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
<td align="right">64,463,425</td>
<td align="right">296,695</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,556,440</td>
<td align="right">11,880</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">31,248,942</td>
<td align="right">2,020,835</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">29,507,902</td>
<td align="right">1,974,255</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,355,005</td>
<td align="right">5,590,714</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">34,431,180</td>
<td align="right">5,074,460</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,561,392</td>
<td align="right">3,942,598</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">447,020</td>
<td align="right">71,000</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">494,800</td>
<td align="right">891,360</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">227,200</td>
<td align="right">45,460</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">501,400</td>
<td align="right">104,860</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,670,920</td>
<td align="right">2,119,000</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,022,220</td>
<td align="right">1,117,320</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38,388,820</td>
<td align="right">9,009,226</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">11,940,480</td>
<td align="right">2,821,820</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,811,660</td>
<td align="right">430,000</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,928,920</td>
<td align="right">759,760</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">173,213</td>
<td align="right">47,330</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,373,020</td>
<td align="right">2,431,380</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,151,820</td>
<td align="right">344,428</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,495,660</td>
<td align="right">479,140</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">519,640</td>
<td align="right">171,700</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,652,813</td>
<td align="right">2,646,940</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">4,036,120</td>
<td align="right">1,438,160</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,505,900</td>
<td align="right">536,860</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">8,049,360</td>
<td align="right">2,963,000</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,275,440</td>
<td align="right">1,587,944</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,681,560</td>
<td align="right">1,016,450</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,828,080</td>
<td align="right">743,240</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,246,460</td>
<td align="right">933,480</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,061,900</td>
<td align="right">5,944,620</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,771,650</td>
<td align="right">2,458,513</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">56,148,250</td>
<td align="right">24,125,573</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,553,120</td>
<td align="right">1,976,200</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,251,410</td>
<td align="right">4,932,259</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,232,500</td>
<td align="right">1,442,360</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">15,642,900</td>
<td align="right">7,064,480</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">15,656,000</td>
<td align="right">7,157,240</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,624,660</td>
<td align="right">4,076,820</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,210,380</td>
<td align="right">577,840</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">156,520</td>
<td align="right">76,700</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">249,660</td>
<td align="right">123,280</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,823,940</td>
<td align="right">5,096,650</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">9,269,760</td>
<td align="right">4,837,660</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,419,040</td>
<td align="right">2,901,110</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,827,540</td>
<td align="right">2,656,560</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,429,260</td>
<td align="right">3,008,655</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">104,305,893</td>
<td align="right">58,442,431</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,087,480</td>
<td align="right">1,732,520</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">520,523,209</td>
<td align="right">299,123,763</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">752,340</td>
<td align="right">432,380</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">76,701,649</td>
<td align="right">44,535,395</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">621,360</td>
<td align="right">363,520</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">99,207,573</td>
<td align="right">60,409,918</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">29,855,012</td>
<td align="right">18,378,400</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,813,083</td>
<td align="right">1,752,929</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">18,005,060</td>
<td align="right">11,226,834</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,396,890</td>
<td align="right">3,375,505</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,771,780</td>
<td align="right">5,503,908</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,205,520</td>
<td align="right">2,680,610</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,560,770</td>
<td align="right">1,633,155</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,881,400</td>
<td align="right">6,467,200</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,706,932</td>
<td align="right">3,740,200</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">50,760,860</td>
<td align="right">33,321,275</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,164,080</td>
<td align="right">1,562,880</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">86,080</td>
<td align="right">57,020</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">40,185,293</td>
<td align="right">26,718,800</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">17,980,022</td>
<td align="right">12,104,383</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">116,893,454</td>
<td align="right">78,706,119</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">131,244,366</td>
<td align="right">88,459,958</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">6,620</td>
<td align="right">4,500</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">4,207,480</td>
<td align="right">2,862,780</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">24,937,120</td>
<td align="right">16,984,660</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">76,496,290</td>
<td align="right">52,125,896</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">173,440</td>
<td align="right">123,100</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,060</td>
<td align="right">23,520</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">84,656,762</td>
<td align="right">60,452,861</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">35,368,260</td>
<td align="right">25,350,740</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">90,194,106</td>
<td align="right">64,816,928</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">20,094,043</td>
<td align="right">14,733,410</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,757,900</td>
<td align="right">2,785,580</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,357,220</td>
<td align="right">1,753,168</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">497,220</td>
<td align="right">370,120</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">59,281,940</td>
<td align="right">44,178,601</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">9,078,080</td>
<td align="right">6,765,720</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">12,380</td>
<td align="right">9,260</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,512,240</td>
<td align="right">25,431,300</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">96,721,124</td>
<td align="right">75,694,239</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,020</td>
<td align="right">36,060</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,005,610</td>
<td align="right">8,780,155</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">100</td>
<td align="right">80</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,035,380</td>
<td align="right">8,872,880</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">6,595,200</td>
<td align="right">5,472,760</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,017,240</td>
<td align="right">2,526,780</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,028,220</td>
<td align="right">3,386,960</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,851,140</td>
<td align="right">4,096,764</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6,899,920</td>
<td align="right">5,909,540</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">76,960</td>
<td align="right">66,680</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,448,860</td>
<td align="right">2,148,320</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">7,363,800</td>
<td align="right">6,488,640</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">66,516,100</td>
<td align="right">58,929,098</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,598,020</td>
<td align="right">3,209,920</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">32,972,420</td>
<td align="right">29,429,910</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,867,720</td>
<td align="right">2,574,620</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,552,120</td>
<td align="right">1,393,820</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">36,379,040</td>
<td align="right">32,887,144</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">36,001,720</td>
<td align="right">32,740,540</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">618,180</td>
<td align="right">564,660</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,151,723</td>
<td align="right">1,052,414</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,579,900</td>
<td align="right">3,310,480</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">320</td>
<td align="right">340</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,604,643</td>
<td align="right">5,258,115</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,848,880</td>
<td align="right">10,276,200</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,620</td>
<td align="right">3,440</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,898,900</td>
<td align="right">2,768,460</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">90,320</td>
<td align="right">86,304</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">7,948,920</td>
<td align="right">7,600,260</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">940</td>
<td align="right">900</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,882,340</td>
<td align="right">1,803,400</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">105,420</td>
<td align="right">101,180</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">27,551,620</td>
<td align="right">26,476,820</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,827,220</td>
<td align="right">5,630,300</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">564,340</td>
<td align="right">545,440</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">563,380</td>
<td align="right">544,600</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,696,020</td>
<td align="right">1,656,780</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">3,262,320</td>
<td align="right">3,201,240</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,148,040</td>
<td align="right">5,056,260</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">347,300</td>
<td align="right">341,900</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">15,878,620</td>
<td align="right">15,688,480</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">75,436,886</td>
<td align="right">74,547,734</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">198,120</td>
<td align="right">195,900</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,060,440</td>
<td align="right">1,050,600</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">756,860</td>
<td align="right">750,160</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">39,721,240</td>
<td align="right">39,370,566</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,413,940</td>
<td align="right">1,405,780</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,980</td>
<td align="right">7,020</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,540</td>
<td align="right">13,500</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,540</td>
<td align="right">13,580</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">677,360</td>
<td align="right">675,940</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">108,240</td>
<td align="right">108,360</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">241,240</td>
<td align="right">241,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,365,400</td>
<td align="right">6,368,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">270,640</td>
<td align="right">270,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">475,480</td>
<td align="right">475,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">199,520</td>
<td align="right">199,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,055,460</td>
<td align="right">1,055,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,947,160</td>
<td align="right">1,947,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,821,380</td>
<td align="right">16,823,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,514,433</td>
<td align="right">37,511,750</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">608,540</td>
<td align="right">608,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,543,340</td>
<td align="right">3,543,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,413,940</td>
<td align="right">1,413,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,590,040</td>
<td align="right">1,590,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,588,980</td>
<td align="right">8,589,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">10,680,080</td>
<td align="right">10,680,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">265,920</td>
<td align="right">265,920</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">50,658,594</td>
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
<td align="right">2,233,320</td>
<td align="right">20.9%</td>
<td align="right">921,020</td>
<td align="right">9.8%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,460,220</td>
<td align="right">79.0%</td>
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
<td align="right">9,900</td>
<td align="right">75.3%</td>
<td align="right">9,220</td>
<td align="right">74.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,240</td>
<td align="right">24.7%</td>
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
<td align="left">floor divide</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">920</td>
<td align="right">9.3%</td>
<td align="right">660</td>
<td align="right">7.2%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">6.7%</td>
<td align="right">540</td>
<td align="right">5.9%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">800</td>
<td align="right">8.1%</td>
<td align="right">720</td>
<td align="right">7.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,580</td>
<td align="right">16.0%</td>
<td align="right">1,520</td>
<td align="right">16.5%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,500</td>
<td align="right">35.4%</td>
<td align="right">3,380</td>
<td align="right">36.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">900</td>
<td align="right">9.1%</td>
<td align="right">900</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">400</td>
<td align="right">4.0%</td>
<td align="right">400</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">340</td>
<td align="right">3.4%</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">260</td>
<td align="right">2.6%</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">120</td>
<td align="right">1.2%</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">60</td>
<td align="right">0.6%</td>
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
<td align="right">1,828,080</td>
<td align="right">100.0%</td>
<td align="right">743,240</td>
<td align="right">100.0%</td>
<td align="right">-59.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">227,800</td>
<td align="right">0.9%</td>
<td align="right">44,880</td>
<td align="right">0.2%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,014,320</td>
<td align="right">16.5%</td>
<td align="right">1,420,380</td>
<td align="right">6.6%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,110,206</td>
<td align="right">82.5%</td>
<td align="right">20,111,780</td>
<td align="right">93.1%</td>
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
<td align="right">12,800</td>
<td align="right">49.2%</td>
<td align="right">8,820</td>
<td align="right">47.6%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,200</td>
<td align="right">50.8%</td>
<td align="right">9,720</td>
<td align="right">52.4%</td>
<td align="right">-26.4%</td>
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
<td align="right">6,740</td>
<td align="right">52.7%</td>
<td align="right">3,740</td>
<td align="right">42.4%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">180</td>
<td align="right">1.4%</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,300</td>
<td align="right">25.8%</td>
<td align="right">2,660</td>
<td align="right">30.2%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">2,180</td>
<td align="right">17.0%</td>
<td align="right">1,880</td>
<td align="right">21.3%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">260</td>
<td align="right">2.0%</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">100</td>
<td align="right">0.8%</td>
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
<td align="right">17,437,460</td>
<td align="right">11.4%</td>
<td align="right">11,676,240</td>
<td align="right">7.7%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">134,898,526</td>
<td align="right">88.4%</td>
<td align="right">139,537,410</td>
<td align="right">92.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,100</td>
<td align="right">0.1%</td>
<td align="right">140,020</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">452,940</td>
<td align="right">100.0%</td>
<td align="right">337,240</td>
<td align="right">100.0%</td>
<td align="right">-25.5%</td>
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
<td align="right">799,220</td>
<td align="right">97.5%</td>
<td align="right">431,660</td>
<td align="right">95.5%</td>
<td align="right">-46.0%</td>
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
<td align="right">1.3%</td>
<td align="right">10,780</td>
<td align="right">2.4%</td>
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
<td align="right">28,720</td>
<td align="right">0.1%</td>
<td align="right">6,280</td>
<td align="right">0.0%</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,581,923</td>
<td align="right">11.2%</td>
<td align="right">5,236,375</td>
<td align="right">10.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,202,090</td>
<td align="right">88.7%</td>
<td align="right">44,194,015</td>
<td align="right">89.4%</td>
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
<td align="right">11,280</td>
<td align="right">48.5%</td>
<td align="right">10,320</td>
<td align="right">47.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,980</td>
<td align="right">51.5%</td>
<td align="right">11,540</td>
<td align="right">52.8%</td>
<td align="right">-3.7%</td>
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
<td align="right">3,800</td>
<td align="right">33.7%</td>
<td align="right">3,000</td>
<td align="right">29.1%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">3.0%</td>
<td align="right">360</td>
<td align="right">3.5%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,360</td>
<td align="right">38.7%</td>
<td align="right">4,160</td>
<td align="right">40.3%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">980</td>
<td align="right">8.7%</td>
<td align="right">980</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">860</td>
<td align="right">7.6%</td>
<td align="right">860</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">3.0%</td>
<td align="right">340</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">220</td>
<td align="right">2.0%</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">160</td>
<td align="right">1.4%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
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
<tr>
<td align="left">bytes</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,748,353</td>
<td align="right">38.8%</td>
<td align="right">2,436,753</td>
<td align="right">21.2%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,220</td>
<td align="right">0.2%</td>
<td align="right">31,300</td>
<td align="right">0.3%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,001,800</td>
<td align="right">60.8%</td>
<td align="right">9,002,760</td>
<td align="right">78.3%</td>
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
<td align="right">19,097</td>
<td align="right">79.8%</td>
<td align="right">17,560</td>
<td align="right">78.6%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,820</td>
<td align="right">20.2%</td>
<td align="right">4,780</td>
<td align="right">21.4%</td>
<td align="right">-0.8%</td>
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
<td align="right">3,720</td>
<td align="right">19.5%</td>
<td align="right">3,360</td>
<td align="right">19.1%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">4,140</td>
<td align="right">21.7%</td>
<td align="right">3,740</td>
<td align="right">21.3%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,480</td>
<td align="right">13.0%</td>
<td align="right">2,260</td>
<td align="right">12.9%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,757</td>
<td align="right">45.9%</td>
<td align="right">8,200</td>
<td align="right">46.7%</td>
<td align="right">-6.4%</td>
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
<td align="right">8,336,320</td>
<td align="right">10.1%</td>
<td align="right">2,403,200</td>
<td align="right">9.3%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">73,894,145</td>
<td align="right">89.5%</td>
<td align="right">23,406,874</td>
<td align="right">90.2%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">294,320</td>
<td align="right">0.4%</td>
<td align="right">102,600</td>
<td align="right">0.4%</td>
<td align="right">-65.1%</td>
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
<td align="right">23,620</td>
<td align="right">56.0%</td>
<td align="right">15,100</td>
<td align="right">50.3%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,580</td>
<td align="right">44.0%</td>
<td align="right">14,940</td>
<td align="right">49.7%</td>
<td align="right">-19.6%</td>
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
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">180</td>
<td align="right">1.2%</td>
<td align="right">800.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,240</td>
<td align="right">30.7%</td>
<td align="right">2,680</td>
<td align="right">17.7%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,020</td>
<td align="right">21.3%</td>
<td align="right">3,040</td>
<td align="right">20.1%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">2.7%</td>
<td align="right">400</td>
<td align="right">2.6%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">220</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.3%</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">900</td>
<td align="right">3.8%</td>
<td align="right">680</td>
<td align="right">4.5%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,920</td>
<td align="right">20.8%</td>
<td align="right">3,960</td>
<td align="right">26.2%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,000</td>
<td align="right">8.5%</td>
<td align="right">1,700</td>
<td align="right">11.3%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">720</td>
<td align="right">3.0%</td>
<td align="right">620</td>
<td align="right">4.1%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">520</td>
<td align="right">2.2%</td>
<td align="right">460</td>
<td align="right">3.0%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,120</td>
<td align="right">4.7%</td>
<td align="right">1,000</td>
<td align="right">6.6%</td>
<td align="right">-10.7%</td>
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
<td align="right">62,353,653</td>
<td align="right">21.4%</td>
<td align="right">30,260,669</td>
<td align="right">12.3%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">32,097,700</td>
<td align="right">11.0%</td>
<td align="right">25,063,940</td>
<td align="right">10.2%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">196,269,307</td>
<td align="right">67.4%</td>
<td align="right">190,298,154</td>
<td align="right">77.4%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">427,360</td>
<td align="right">0.1%</td>
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
<td align="right">1,497,920</td>
<td align="right">95.0%</td>
<td align="right">848,740</td>
<td align="right">91.8%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">78,900</td>
<td align="right">5.0%</td>
<td align="right">75,540</td>
<td align="right">8.2%</td>
<td align="right">-4.3%</td>
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
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">820</td>
<td align="right">1.1%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,820</td>
<td align="right">2.3%</td>
<td align="right">1,640</td>
<td align="right">2.2%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,640</td>
<td align="right">5.9%</td>
<td align="right">4,300</td>
<td align="right">5.7%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,520</td>
<td align="right">1.9%</td>
<td align="right">1,420</td>
<td align="right">1.9%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">15,940</td>
<td align="right">20.2%</td>
<td align="right">14,980</td>
<td align="right">19.8%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">400</td>
<td align="right">0.5%</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,080</td>
<td align="right">26.7%</td>
<td align="right">20,240</td>
<td align="right">26.8%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,240</td>
<td align="right">5.4%</td>
<td align="right">4,080</td>
<td align="right">5.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20,000</td>
<td align="right">25.3%</td>
<td align="right">19,460</td>
<td align="right">25.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,000</td>
<td align="right">2.5%</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">1.4%</td>
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
<td align="right">153,115,999</td>
<td align="right">99.8%</td>
<td align="right">96,583,571</td>
<td align="right">99.7%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">81,940</td>
<td align="right">0.1%</td>
<td align="right">81,920</td>
<td align="right">0.1%</td>
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
<td align="right">102,200</td>
<td align="right">0.1%</td>
<td align="right">102,180</td>
<td align="right">0.1%</td>
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
<td align="right">1,500</td>
<td align="right">0.0%</td>
<td align="right">1,500</td>
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
<td align="right">98,120</td>
<td align="right">100.0%</td>
<td align="right">98,100</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">3,809,260</td>
<td align="right">99.9%</td>
<td align="right">3,809,440</td>
<td align="right">99.9%</td>
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
<td align="right">2,140</td>
<td align="right">0.1%</td>
<td align="right">2,140</td>
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
<td align="right">8,578,840</td>
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
<td align="right">3,570,640</td>
<td align="right">7.0%</td>
<td align="right">3,182,860</td>
<td align="right">6.3%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,147,520</td>
<td align="right">29.9%</td>
<td align="right">15,000,900</td>
<td align="right">29.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,912,840</td>
<td align="right">63.0%</td>
<td align="right">32,054,980</td>
<td align="right">63.8%</td>
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
<td align="left">Failure</td>
<td align="right">14,300</td>
<td align="right">4.6%</td>
<td align="right">13,980</td>
<td align="right">4.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">298,240</td>
<td align="right">95.4%</td>
<td align="right">295,480</td>
<td align="right">95.5%</td>
<td align="right">-0.9%</td>
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
<td align="right">220</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,240</td>
<td align="right">22.7%</td>
<td align="right">3,020</td>
<td align="right">21.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,420</td>
<td align="right">9.9%</td>
<td align="right">1,340</td>
<td align="right">9.6%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">7,240</td>
<td align="right">50.6%</td>
<td align="right">7,240</td>
<td align="right">51.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">600</td>
<td align="right">4.2%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">600</td>
<td align="right">4.2%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">420</td>
<td align="right">2.9%</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">2.2%</td>
<td align="right">320</td>
<td align="right">2.3%</td>
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
<td align="right">246,000</td>
<td align="right">5.3%</td>
<td align="right">119,760</td>
<td align="right">2.7%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,394,560</td>
<td align="right">94.6%</td>
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
<td align="left">Failure</td>
<td align="right">1,600</td>
<td align="right">43.7%</td>
<td align="right">1,460</td>
<td align="right">41.5%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,060</td>
<td align="right">56.3%</td>
<td align="right">2,060</td>
<td align="right">58.5%</td>
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
<td align="right">400</td>
<td align="right">25.0%</td>
<td align="right">260</td>
<td align="right">17.8%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">800</td>
<td align="right">50.0%</td>
<td align="right">800</td>
<td align="right">54.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">160</td>
<td align="right">10.0%</td>
<td align="right">160</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">7.5%</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">120</td>
<td align="right">7.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,194,180</td>
<td align="right">8.3%</td>
<td align="right">2,039,840</td>
<td align="right">1.8%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,084,243</td>
<td align="right">0.9%</td>
<td align="right">985,834</td>
<td align="right">0.9%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">110,938,705</td>
<td align="right">90.7%</td>
<td align="right">110,849,044</td>
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
<td align="left">Success</td>
<td align="right">237,560</td>
<td align="right">91.9%</td>
<td align="right">83,760</td>
<td align="right">80.7%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20,900</td>
<td align="right">8.1%</td>
<td align="right">20,000</td>
<td align="right">19.3%</td>
<td align="right">-4.3%</td>
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
<td align="right">1,540</td>
<td align="right">7.4%</td>
<td align="right">780</td>
<td align="right">3.9%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,420</td>
<td align="right">6.8%</td>
<td align="right">1,360</td>
<td align="right">6.8%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,820</td>
<td align="right">8.7%</td>
<td align="right">1,780</td>
<td align="right">8.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,320</td>
<td align="right">6.3%</td>
<td align="right">1,300</td>
<td align="right">6.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,480</td>
<td align="right">64.5%</td>
<td align="right">13,460</td>
<td align="right">67.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,000</td>
<td align="right">4.8%</td>
<td align="right">1,000</td>
<td align="right">5.0%</td>
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
<td align="right">1,551,140</td>
<td align="right">5.0%</td>
<td align="right">7,300</td>
<td align="right">0.0%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,671,042</td>
<td align="right">95.0%</td>
<td align="right">29,676,119</td>
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
<td align="left">Failure</td>
<td align="right">1,040</td>
<td align="right">19.6%</td>
<td align="right">320</td>
<td align="right">7.0%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,260</td>
<td align="right">80.4%</td>
<td align="right">4,260</td>
<td align="right">93.0%</td>
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
<td align="right">960</td>
<td align="right">92.3%</td>
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">80</td>
<td align="right">7.7%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">106,601,593</td>
<td align="right">3.7%</td>
<td align="right">59,679,939</td>
<td align="right">3.2%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">998,384,918</td>
<td align="right">34.9%</td>
<td align="right">615,756,931</td>
<td align="right">33.3%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,676,573,361</td>
<td align="right">58.7%</td>
<td align="right">1,119,745,577</td>
<td align="right">60.6%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">75,987,276</td>
<td align="right">2.7%</td>
<td align="right">52,150,822</td>
<td align="right">2.8%</td>
<td align="right">-31.4%</td>
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
<td align="right">8,336,320</td>
<td align="right">11.1%</td>
<td align="right">2,403,200</td>
<td align="right">4.7%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">4,014,320</td>
<td align="right">5.3%</td>
<td align="right">1,420,380</td>
<td align="right">2.8%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,828,080</td>
<td align="right">2.4%</td>
<td align="right">743,240</td>
<td align="right">1.4%</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,233,320</td>
<td align="right">3.0%</td>
<td align="right">921,020</td>
<td align="right">1.8%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,748,353</td>
<td align="right">7.7%</td>
<td align="right">2,436,753</td>
<td align="right">4.7%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,097,700</td>
<td align="right">42.7%</td>
<td align="right">25,063,940</td>
<td align="right">48.8%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,570,640</td>
<td align="right">4.8%</td>
<td align="right">3,182,860</td>
<td align="right">6.2%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,581,923</td>
<td align="right">7.4%</td>
<td align="right">5,236,375</td>
<td align="right">10.2%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,578,840</td>
<td align="right">11.4%</td>
<td align="right">8,578,920</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,551,140</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">985,834</td>
<td align="right">1.9%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">8,445,260</td>
<td align="right">7.9%</td>
<td align="right">1,385,020</td>
<td align="right">2.3%</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,197,600</td>
<td align="right">3.9%</td>
<td align="right">756,220</td>
<td align="right">1.3%</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,448,560</td>
<td align="right">6.0%</td>
<td align="right">1,999,640</td>
<td align="right">3.4%</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">11,687,200</td>
<td align="right">11.0%</td>
<td align="right">4,730,260</td>
<td align="right">7.9%</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,765,720</td>
<td align="right">15.7%</td>
<td align="right">7,821,960</td>
<td align="right">13.1%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,836,800</td>
<td align="right">2.7%</td>
<td align="right">1,474,520</td>
<td align="right">2.5%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">23,128,100</td>
<td align="right">21.7%</td>
<td align="right">14,826,160</td>
<td align="right">24.8%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,511,720</td>
<td align="right">9.9%</td>
<td align="right">8,798,860</td>
<td align="right">14.7%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">15,147,460</td>
<td align="right">14.2%</td>
<td align="right">15,000,840</td>
<td align="right">25.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,718,900</td>
<td align="right">2.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">610,880</td>
<td align="right">1.0%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,975,360</td>
<td align="right">1.3%</td>
<td align="right">2,620,960</td>
<td align="right">1.8%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">8,726,580</td>
<td align="right">5.9%</td>
<td align="right">9,121,660</td>
<td align="right">6.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,720</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">37,990,273</td>
<td align="right">25.7%</td>
<td align="right">38,385,950</td>
<td align="right">25.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">37,990,273</td>
<td align="right">25.7%</td>
<td align="right">38,385,950</td>
<td align="right">25.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">109,584,653</td>
<td align="right">74.3%</td>
<td align="right">109,594,730</td>
<td align="right">74.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">780,253</td>
<td align="right">0.5%</td>
<td align="right">780,210</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">890,860</td>
<td align="right">0.6%</td>
<td align="right">890,900</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">117,397,466</td>
<td align="right">79.6%</td>
<td align="right">117,402,300</td>
<td align="right">79.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">29,263,693</td>
<td align="right">19.8%</td>
<td align="right">29,264,290</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">5,112,700</td>
<td align="right">3.5%</td>
<td align="right">5,112,800</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">29,249,293</td>
<td align="right">19.8%</td>
<td align="right">29,249,850</td>
<td align="right">19.8%</td>
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
<td align="left">Decrefs</td>
<td align="right">510,782,209</td>
<td align="right">26.7%</td>
<td align="right">1,129,824,753</td>
<td align="right">52.0%</td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">543,840,193</td>
<td align="right">31.0%</td>
<td align="right">1,201,400,738</td>
<td align="right">59.8%</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">540,277</td>
<td align="right"></td>
<td align="right">753,957</td>
<td align="right"></td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,997,066</td>
<td align="right"></td>
<td align="right">5,433,444</td>
<td align="right"></td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,485,553</td>
<td align="right"></td>
<td align="right">4,708,402</td>
<td align="right"></td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,208,053,694</td>
<td align="right">69.0%</td>
<td align="right">809,177,567</td>
<td align="right">40.2%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">1,400,520,101</td>
<td align="right">73.3%</td>
<td align="right">1,041,769,123</td>
<td align="right">48.0%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">130,746,533</td>
<td align="right"></td>
<td align="right">125,270,836</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">603,300</td>
<td align="right">0.3%</td>
<td align="right">622,581</td>
<td align="right">0.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">139,963,614</td>
<td align="right"></td>
<td align="right">141,585,883</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">152,551,250</td>
<td align="right">68.7%</td>
<td align="right">154,205,877</td>
<td align="right">69.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">151,696,590</td>
<td align="right">68.3%</td>
<td align="right">153,331,936</td>
<td align="right">68.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">63,281,209</td>
<td align="right"></td>
<td align="right">63,235,283</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,405,040</td>
<td align="right"></td>
<td align="right">4,405,600</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">69,415,250</td>
<td align="right">31.3%</td>
<td align="right">69,419,875</td>
<td align="right">31.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">69,454,530</td>
<td align="right"></td>
<td align="right">69,459,155</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">251,360</td>
<td align="right">0.1%</td>
<td align="right">251,360</td>
<td align="right">0.1%</td>
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
<td align="right">5,340</td>
<td align="right">82,520</td>
<td align="right">485,529,240</td>
<td align="right">5,380</td>
<td align="right">82,020</td>
<td align="right">483,934,406</td>
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
<td align="right">0</td>
<td align="right">320</td>
<td align="right">320 / 0 !!</td>
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
<td align="right">320</td>
<td align="right">320 / 0 !!</td>
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
