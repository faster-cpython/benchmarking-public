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
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">36,925</td>
<td align="right">297</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">180,861</td>
<td align="right">26,945</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">208,095</td>
<td align="right">33,672</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">598,818</td>
<td align="right">103,741</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">72,253</td>
<td align="right">21,009</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">220,852</td>
<td align="right">65,008</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">50,873</td>
<td align="right">16,930</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">116,216</td>
<td align="right">39,034</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">12,800</td>
<td align="right">4,367</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">254,953</td>
<td align="right">92,167</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">450,365</td>
<td align="right">163,487</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">151,713</td>
<td align="right">59,720</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">31,543</td>
<td align="right">14,383</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">404,056</td>
<td align="right">226,178</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">560,553</td>
<td align="right">316,122</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">40,000</td>
<td align="right">22,975</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">105,827</td>
<td align="right">62,225</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">275,790</td>
<td align="right">164,834</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">591,479</td>
<td align="right">382,140</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">5,180</td>
<td align="right">3,353</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,196,700</td>
<td align="right">782,152</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">125,993</td>
<td align="right">83,920</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">781,097</td>
<td align="right">527,452</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,676,016</td>
<td align="right">1,135,021</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,301,606</td>
<td align="right">909,868</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">575,630</td>
<td align="right">414,941</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">330,139</td>
<td align="right">420,614</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">73,856</td>
<td align="right">53,731</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">257,080</td>
<td align="right">189,059</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">127,040</td>
<td align="right">94,633</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,970,603</td>
<td align="right">6,048,516</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,087,857</td>
<td align="right">862,779</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,168</td>
<td align="right">5,688</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,945,688</td>
<td align="right">1,545,208</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">103,477</td>
<td align="right">83,484</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,612,935</td>
<td align="right">2,923,255</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,622,877</td>
<td align="right">2,937,827</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">404,374</td>
<td align="right">334,954</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,469,218</td>
<td align="right">6,190,314</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,005,507</td>
<td align="right">3,328,928</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,768,859</td>
<td align="right">1,480,283</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,598,840</td>
<td align="right">1,338,134</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,196,464</td>
<td align="right">3,523,622</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">43,901,127</td>
<td align="right">37,001,825</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">511,616</td>
<td align="right">432,505</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">4,908,981</td>
<td align="right">4,158,331</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">56,315</td>
<td align="right">47,882</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,302,083</td>
<td align="right">2,831,563</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,254,438</td>
<td align="right">1,076,153</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,049,173</td>
<td align="right">4,366,821</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">10,174</td>
<td align="right">8,809</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,654,795</td>
<td align="right">6,690,195</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">10,977,036</td>
<td align="right">9,595,798</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,573,503</td>
<td align="right">13,617,939</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,810,727</td>
<td align="right">3,358,521</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">939,214</td>
<td align="right">828,258</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">71,911</td>
<td align="right">63,478</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,603,679</td>
<td align="right">2,312,093</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,078,723</td>
<td align="right">1,869,145</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,722,752</td>
<td align="right">2,483,922</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">15,413</td>
<td align="right">14,111</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,911,759</td>
<td align="right">10,937,635</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,936,664</td>
<td align="right">12,808,047</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,262,793</td>
<td align="right">2,095,599</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,120,307</td>
<td align="right">14,937,805</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,659,904</td>
<td align="right">3,402,347</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,556,700</td>
<td align="right">6,125,141</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">11,212,956</td>
<td align="right">10,512,517</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">486,434</td>
<td align="right">456,612</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,146,115</td>
<td align="right">3,919,336</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,749,089</td>
<td align="right">1,654,563</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">825,245</td>
<td align="right">782,886</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">965,803</td>
<td align="right">917,224</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,174,309</td>
<td align="right">5,432,216</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,957,994</td>
<td align="right">3,772,342</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">411,712</td>
<td align="right">396,844</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,350,464</td>
<td align="right">1,307,972</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">694,012</td>
<td align="right">674,019</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">37,739</td>
<td align="right">36,689</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">156,145</td>
<td align="right">152,070</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">655,232</td>
<td align="right">638,207</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,317,626</td>
<td align="right">8,106,301</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">175,215</td>
<td align="right">170,910</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">53,056</td>
<td align="right">51,786</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">932,416</td>
<td align="right">912,280</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">764,096</td>
<td align="right">749,228</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,409,475</td>
<td align="right">12,175,938</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,463,130</td>
<td align="right">1,445,631</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,572,467</td>
<td align="right">1,555,137</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">21,463,040</td>
<td align="right">21,228,808</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,033,799</td>
<td align="right">1,022,852</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">325,444</td>
<td align="right">322,504</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,107,405</td>
<td align="right">1,099,611</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">239,213</td>
<td align="right">237,659</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,405,568</td>
<td align="right">2,390,533</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,206,006</td>
<td align="right">7,208,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,011,712</td>
<td align="right">4,011,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,881,646</td>
<td align="right">2,881,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,286,545</td>
<td align="right">2,286,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,924,665</td>
<td align="right">1,924,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,512,640</td>
<td align="right">1,512,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,379,910</td>
<td align="right">1,379,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,286,208</td>
<td align="right">1,286,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,163,964</td>
<td align="right">1,163,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">727,807</td>
<td align="right">727,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">615,808</td>
<td align="right">615,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">412,032</td>
<td align="right">412,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">412,032</td>
<td align="right">412,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">384,960</td>
<td align="right">384,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">172,938</td>
<td align="right">172,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">127,168</td>
<td align="right">127,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">116,544</td>
<td align="right">116,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">77,568</td>
<td align="right">77,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">69,419</td>
<td align="right">69,419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">68,909</td>
<td align="right">68,909</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">66,596</td>
<td align="right">66,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">30,592</td>
<td align="right">30,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">30,592</td>
<td align="right">30,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">30,592</td>
<td align="right">30,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">30,139</td>
<td align="right">30,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">29,439</td>
<td align="right">29,439</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">24,256</td>
<td align="right">24,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">22,720</td>
<td align="right">22,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">12,477</td>
<td align="right">12,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">10,046</td>
<td align="right">10,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">10,046</td>
<td align="right">10,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">6,139</td>
<td align="right">6,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,282</td>
<td align="right">4,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,472</td>
<td align="right">3,472</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,367</td>
<td align="right">2,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,213</td>
<td align="right">1,213</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">832</td>
<td align="right">832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">768</td>
<td align="right">768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">450</td>
<td align="right">450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">384</td>
<td align="right">384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">216</td>
<td align="right">216</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">169</td>
<td align="right">169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">58</td>
<td align="right">58</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14</td>
<td align="right">14</td>
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
<td align="right">30,845</td>
<td align="right">1.6%</td>
<td align="right">13,771</td>
<td align="right">0.7%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,857,275</td>
<td align="right">98.2%</td>
<td align="right">1,857,275</td>
<td align="right">99.1%</td>
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
<td align="right">2,538</td>
<td align="right">0.1%</td>
<td align="right">2,538</td>
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
<td align="right">497</td>
<td align="right">67.2%</td>
<td align="right">411</td>
<td align="right">62.8%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">243</td>
<td align="right">32.8%</td>
<td align="right">243</td>
<td align="right">37.2%</td>
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
<td align="right">48</td>
<td align="right">9.7%</td>
<td align="right">5</td>
<td align="right">1.2%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">48</td>
<td align="right">9.7%</td>
<td align="right">5</td>
<td align="right">1.2%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">268</td>
<td align="right">53.9%</td>
<td align="right">268</td>
<td align="right">65.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">91</td>
<td align="right">18.3%</td>
<td align="right">91</td>
<td align="right">22.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">4.2%</td>
<td align="right">21</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">21</td>
<td align="right">4.2%</td>
<td align="right">21</td>
<td align="right">5.1%</td>
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
<td align="right">24,256</td>
<td align="right">100.0%</td>
<td align="right">24,256</td>
<td align="right">100.0%</td>
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
<td align="right">266,267</td>
<td align="right">0.8%</td>
<td align="right">227,332</td>
<td align="right">0.7%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">262,182</td>
<td align="right">0.8%</td>
<td align="right">223,984</td>
<td align="right">0.7%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,086,435</td>
<td align="right">99.2%</td>
<td align="right">34,134,671</td>
<td align="right">99.3%</td>
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
<td align="left">Success</td>
<td align="right">8,367</td>
<td align="right">100.0%</td>
<td align="right">7,630</td>
<td align="right">100.0%</td>
<td align="right">-8.8%</td>
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
<td align="right">75</td>
<td align="right">16.7%</td>
<td align="right">75</td>
<td align="right">16.7%</td>
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
<td align="right">375</td>
<td align="right">100.0%</td>
<td align="right">375</td>
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
<td align="right">402,856</td>
<td align="right">48.3%</td>
<td align="right">333,546</td>
<td align="right">43.9%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">430,168</td>
<td align="right">51.5%</td>
<td align="right">424,591</td>
<td align="right">55.9%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,318</td>
<td align="right">86.8%</td>
<td align="right">1,208</td>
<td align="right">85.8%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">13.2%</td>
<td align="right">200</td>
<td align="right">14.2%</td>
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
<td align="left">string</td>
<td align="right">49</td>
<td align="right">3.7%</td>
<td align="right">5</td>
<td align="right">0.4%</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">588</td>
<td align="right">44.6%</td>
<td align="right">522</td>
<td align="right">43.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">484</td>
<td align="right">36.7%</td>
<td align="right">484</td>
<td align="right">40.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59</td>
<td align="right">4.5%</td>
<td align="right">59</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">50</td>
<td align="right">3.8%</td>
<td align="right">50</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">45</td>
<td align="right">3.4%</td>
<td align="right">45</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">43</td>
<td align="right">3.3%</td>
<td align="right">43</td>
<td align="right">3.6%</td>
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
<td align="right">105,377</td>
<td align="right">31.4%</td>
<td align="right">61,776</td>
<td align="right">21.2%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">215,972</td>
<td align="right">64.4%</td>
<td align="right">215,972</td>
<td align="right">74.0%</td>
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
<td align="right">13,498</td>
<td align="right">4.0%</td>
<td align="right">13,498</td>
<td align="right">4.6%</td>
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
<td align="right">417</td>
<td align="right">59.1%</td>
<td align="right">416</td>
<td align="right">59.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">288</td>
<td align="right">40.9%</td>
<td align="right">288</td>
<td align="right">40.9%</td>
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
<td align="right">261</td>
<td align="right">62.6%</td>
<td align="right">260</td>
<td align="right">62.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">156</td>
<td align="right">37.4%</td>
<td align="right">156</td>
<td align="right">37.5%</td>
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
<td align="right">4,194,066</td>
<td align="right">47.2%</td>
<td align="right">3,521,472</td>
<td align="right">43.6%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,681,735</td>
<td align="right">52.7%</td>
<td align="right">4,553,266</td>
<td align="right">56.4%</td>
<td align="right">-2.7%</td>
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
<td align="right">2,311</td>
<td align="right">96.4%</td>
<td align="right">2,063</td>
<td align="right">96.0%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">87</td>
<td align="right">3.6%</td>
<td align="right">87</td>
<td align="right">4.0%</td>
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
<td align="left">enumerate</td>
<td align="right">144</td>
<td align="right">6.2%</td>
<td align="right">58</td>
<td align="right">2.8%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">49</td>
<td align="right">2.1%</td>
<td align="right">28</td>
<td align="right">1.4%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,256</td>
<td align="right">54.3%</td>
<td align="right">1,144</td>
<td align="right">55.5%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">279</td>
<td align="right">12.1%</td>
<td align="right">258</td>
<td align="right">12.5%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">102</td>
<td align="right">4.4%</td>
<td align="right">98</td>
<td align="right">4.8%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">2.2%</td>
<td align="right">49</td>
<td align="right">2.4%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">159</td>
<td align="right">6.9%</td>
<td align="right">158</td>
<td align="right">7.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">183</td>
<td align="right">7.9%</td>
<td align="right">182</td>
<td align="right">8.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">88</td>
<td align="right">3.8%</td>
<td align="right">88</td>
<td align="right">4.3%</td>
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
<td align="left">other</td>
<td align="right">2,448,960</td>
<td align="right">2,448,960 / 0 !!</td>
<td align="right">2,448,960</td>
<td align="right">2,448,960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,244,160</td>
<td align="right">2,244,160 / 0 !!</td>
<td align="right">2,244,160</td>
<td align="right">2,244,160 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">112,000</td>
<td align="right">112,000 / 0 !!</td>
<td align="right">112,000</td>
<td align="right">112,000 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">16,768</td>
<td align="right">16,768 / 0 !!</td>
<td align="right">16,768</td>
<td align="right">16,768 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">15,872</td>
<td align="right">15,872 / 0 !!</td>
<td align="right">15,872</td>
<td align="right">15,872 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">13,888</td>
<td align="right">13,888 / 0 !!</td>
<td align="right">13,888</td>
<td align="right">13,888 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,856</td>
<td align="right">9,856 / 0 !!</td>
<td align="right">9,856</td>
<td align="right">9,856 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,232</td>
<td align="right">7,232 / 0 !!</td>
<td align="right">7,232</td>
<td align="right">7,232 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,152</td>
<td align="right">1,152 / 0 !!</td>
<td align="right">1,152</td>
<td align="right">1,152 / 0 !!</td>
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
<td align="right">249,340</td>
<td align="right">1.0%</td>
<td align="right">181,407</td>
<td align="right">0.8%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,016,458</td>
<td align="right">16.2%</td>
<td align="right">3,147,248</td>
<td align="right">13.9%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">176,327</td>
<td align="right">0.7%</td>
<td align="right">160,157</td>
<td align="right">0.7%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,542,776</td>
<td align="right">82.8%</td>
<td align="right">19,292,523</td>
<td align="right">85.3%</td>
<td align="right">-6.1%</td>
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
<td align="right">79,048</td>
<td align="right">94.9%</td>
<td align="right">62,713</td>
<td align="right">93.8%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,237</td>
<td align="right">5.1%</td>
<td align="right">4,149</td>
<td align="right">6.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">697</td>
<td align="right">16.5%</td>
<td align="right">675</td>
<td align="right">16.3%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,405</td>
<td align="right">80.4%</td>
<td align="right">3,339</td>
<td align="right">80.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.6%</td>
<td align="right">68</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">46</td>
<td align="right">1.1%</td>
<td align="right">46</td>
<td align="right">1.1%</td>
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
<td align="right">33,103,666</td>
<td align="right">100.0%</td>
<td align="right">31,487,560</td>
<td align="right">100.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right">736</td>
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
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
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
<td align="right">2,740</td>
<td align="right">100.0%</td>
<td align="right">2,740</td>
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
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">1,924,665</td>
<td align="right">100.0%</td>
<td align="right">1,924,665</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">7</td>
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
<td align="right">775,517</td>
<td align="right">44.4%</td>
<td align="right">733,775</td>
<td align="right">42.8%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">969,279</td>
<td align="right">55.5%</td>
<td align="right">979,118</td>
<td align="right">57.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">78</td>
<td align="right">0.0%</td>
<td align="right">78</td>
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
<td align="right">14,836</td>
<td align="right">100.0%</td>
<td align="right">14,076</td>
<td align="right">100.0%</td>
<td align="right">-5.1%</td>
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
<td align="right">19</td>
<td align="right">0.0%</td>
<td align="right">19</td>
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
<td align="right">623,661</td>
<td align="right">100.0%</td>
<td align="right">623,661</td>
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
<td align="right">39</td>
<td align="right">100.0%</td>
<td align="right">39</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,281,859</td>
<td align="right">7.1%</td>
<td align="right">988,971</td>
<td align="right">5.9%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,815,789</td>
<td align="right">87.6%</td>
<td align="right">14,828,702</td>
<td align="right">88.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">964,296</td>
<td align="right">5.3%</td>
<td align="right">915,719</td>
<td align="right">5.5%</td>
<td align="right">-5.0%</td>
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
<td align="right">24,843</td>
<td align="right">97.4%</td>
<td align="right">19,316</td>
<td align="right">96.6%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">673</td>
<td align="right">2.6%</td>
<td align="right">671</td>
<td align="right">3.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">188</td>
<td align="right">27.9%</td>
<td align="right">186</td>
<td align="right">27.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">237</td>
<td align="right">35.2%</td>
<td align="right">237</td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">158</td>
<td align="right">23.5%</td>
<td align="right">158</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">46</td>
<td align="right">6.8%</td>
<td align="right">46</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">44</td>
<td align="right">6.5%</td>
<td align="right">44</td>
<td align="right">6.6%</td>
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
<td align="right">5,992</td>
<td align="right">0.1%</td>
<td align="right">5,992</td>
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
<td align="right">6,258,712</td>
<td align="right">99.9%</td>
<td align="right">6,258,712</td>
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
<td align="right">100</td>
<td align="right">68.0%</td>
<td align="right">100</td>
<td align="right">68.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">32.0%</td>
<td align="right">47</td>
<td align="right">32.0%</td>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">47</td>
<td align="right">100.0%</td>
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
<td align="right">6,356,352</td>
<td align="right">2.0%</td>
<td align="right">5,113,638</td>
<td align="right">1.8%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,957,972</td>
<td align="right">3.1%</td>
<td align="right">8,852,696</td>
<td align="right">3.1%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">133,667,061</td>
<td align="right">41.8%</td>
<td align="right">119,988,263</td>
<td align="right">41.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">169,781,410</td>
<td align="right">53.1%</td>
<td align="right">153,447,191</td>
<td align="right">53.4%</td>
<td align="right">-9.6%</td>
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
<td align="right">30,845</td>
<td align="right">0.5%</td>
<td align="right">13,771</td>
<td align="right">0.3%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">105,377</td>
<td align="right">1.7%</td>
<td align="right">61,776</td>
<td align="right">1.2%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">249,340</td>
<td align="right">4.0%</td>
<td align="right">181,407</td>
<td align="right">3.4%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">402,856</td>
<td align="right">6.5%</td>
<td align="right">333,546</td>
<td align="right">6.3%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,194,066</td>
<td align="right">67.2%</td>
<td align="right">3,521,472</td>
<td align="right">66.7%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,182</td>
<td align="right">4.2%</td>
<td align="right">223,984</td>
<td align="right">4.2%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">964,296</td>
<td align="right">15.5%</td>
<td align="right">915,719</td>
<td align="right">17.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">24,256</td>
<td align="right">0.4%</td>
<td align="right">24,256</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">5,992</td>
<td align="right">0.1%</td>
<td align="right">5,992</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right">736</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">482,455</td>
<td align="right">7.6%</td>
<td align="right">245,682</td>
<td align="right">4.8%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">119,951</td>
<td align="right">1.9%</td>
<td align="right">65,120</td>
<td align="right">1.3%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">254,048</td>
<td align="right">4.0%</td>
<td align="right">185,541</td>
<td align="right">3.6%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,899,523</td>
<td align="right">45.6%</td>
<td align="right">2,284,180</td>
<td align="right">44.7%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,453</td>
<td align="right">2.2%</td>
<td align="right">113,388</td>
<td align="right">2.2%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">900,978</td>
<td align="right">14.2%</td>
<td align="right">731,428</td>
<td align="right">14.3%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">105,998</td>
<td align="right">1.7%</td>
<td align="right">96,128</td>
<td align="right">1.9%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">775,517</td>
<td align="right">12.2%</td>
<td align="right">733,775</td>
<td align="right">14.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">608,800</td>
<td align="right">9.6%</td>
<td align="right">591,706</td>
<td align="right">11.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">18,752</td>
<td align="right">0.3%</td>
<td align="right">18,752</td>
<td align="right">0.4%</td>
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
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">16,975,857</td>
<td align="right">88.1%</td>
<td align="right">16,975,857</td>
<td align="right">88.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">491,602</td>
<td align="right">2.6%</td>
<td align="right">491,602</td>
<td align="right">2.6%</td>
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
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
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
<td align="right">427,393</td>
<td align="right">2.2%</td>
<td align="right">427,393</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">33,600</td>
<td align="right">0.2%</td>
<td align="right">33,600</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,279,866</td>
<td align="right">6.6%</td>
<td align="right">1,279,866</td>
<td align="right">6.6%</td>
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
<td align="right">30,592</td>
<td align="right">0.2%</td>
<td align="right">30,592</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">13,974,592</td>
<td align="right">72.5%</td>
<td align="right">13,974,592</td>
<td align="right">72.5%</td>
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
<td align="right">87</td>
<td align="right">0.0%</td>
<td align="right">314</td>
<td align="right">0.0%</td>
<td align="right">260.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,571,001</td>
<td align="right">2.2%</td>
<td align="right">4,359,571</td>
<td align="right">1.8%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">3,538,730</td>
<td align="right">1.3%</td>
<td align="right">3,100,173</td>
<td align="right">1.1%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">84,090,370</td>
<td align="right">33.9%</td>
<td align="right">75,228,452</td>
<td align="right">30.5%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">15,192</td>
<td align="right"></td>
<td align="right">16,496</td>
<td align="right"></td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">98,169,801</td>
<td align="right">39.6%</td>
<td align="right">105,642,820</td>
<td align="right">42.9%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">108,292,092</td>
<td align="right">38.8%</td>
<td align="right">101,943,316</td>
<td align="right">36.8%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">107,080,919</td>
<td align="right">38.4%</td>
<td align="right">112,014,493</td>
<td align="right">40.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">30,444</td>
<td align="right">0.1%</td>
<td align="right">31,615</td>
<td align="right">0.1%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,948,479</td>
<td align="right"></td>
<td align="right">4,857,928</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">60,078,248</td>
<td align="right">24.2%</td>
<td align="right">61,147,041</td>
<td align="right">24.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">275,245</td>
<td align="right"></td>
<td align="right">278,154</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">260,449</td>
<td align="right"></td>
<td align="right">262,187</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">60,000,676</td>
<td align="right">21.5%</td>
<td align="right">60,280,611</td>
<td align="right">21.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,514,710</td>
<td align="right"></td>
<td align="right">14,498,987</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">24,695,159</td>
<td align="right"></td>
<td align="right">24,675,916</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,395,720</td>
<td align="right">36.5%</td>
<td align="right">13,397,336</td>
<td align="right">36.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,365,189</td>
<td align="right">36.4%</td>
<td align="right">13,365,407</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,298,927</td>
<td align="right"></td>
<td align="right">23,298,703</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">23,303,329</td>
<td align="right">63.5%</td>
<td align="right">23,303,226</td>
<td align="right">63.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">60,736</td>
<td align="right"></td>
<td align="right">60,736</td>
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
<td align="right">65</td>
<td align="right">92,344</td>
<td align="right">727,516</td>
<td align="right">44,105</td>
<td align="right">100,824</td>
<td align="right">65</td>
<td align="right">81,584</td>
<td align="right">683,820</td>
<td align="right">53,967</td>
<td align="right">90,361</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">67</td>
<td align="right">1.1%</td>
<td align="right">6,600.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">44</td>
<td align="right">2.5%</td>
<td align="right">284</td>
<td align="right">4.7%</td>
<td align="right">545.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">407</td>
<td align="right">23.4%</td>
<td align="right">2,177</td>
<td align="right">36.2%</td>
<td align="right">434.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,743</td>
<td align="right"></td>
<td align="right">6,006</td>
<td align="right"></td>
<td align="right">244.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">509</td>
<td align="right">29.2%</td>
<td align="right">1,582</td>
<td align="right">26.3%</td>
<td align="right">210.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">827</td>
<td align="right">47.4%</td>
<td align="right">2,036</td>
<td align="right">33.9%</td>
<td align="right">146.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,509,528</td>
<td align="right"></td>
<td align="right">10,979,483</td>
<td align="right"></td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">166,310,139</td>
<td align="right">2,554.9%</td>
<td align="right">252,105,533</td>
<td align="right">2,296.2%</td>
<td align="right">51.6%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">211</td>
<td align="right">3.5%</td>
<td align="right">211 / 0 !!</td>
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
<td align="right">407</td>
<td align="right"></td>
<td align="right">2,177</td>
<td align="right"></td>
<td align="right">434.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">407</td>
<td align="right">100.0%</td>
<td align="right">1,897</td>
<td align="right">87.1%</td>
<td align="right">366.1%</td>
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
<td align="right">43</td>
<td align="right">2.0%</td>
<td align="right">43 / 0 !!</td>
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
<td align="right">2,062,440</td>
<td align="right">71.5%</td>
<td align="right">18,233,484</td>
<td align="right">81.7%</td>
<td align="right">784.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,883,584</td>
<td align="right"></td>
<td align="right">22,306,816</td>
<td align="right"></td>
<td align="right">673.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">60,728</td>
<td align="right">2.1%</td>
<td align="right">456,304</td>
<td align="right">2.0%</td>
<td align="right">651.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">760,416</td>
<td align="right">26.4%</td>
<td align="right">3,617,028</td>
<td align="right">16.2%</td>
<td align="right">375.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">4,096</td>
<td align="right">0.0%</td>
<td align="right">4,096 / 0 !!</td>
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
<td align="left">231</td>
<td align="right">56.8%</td>
<td align="left">594</td>
<td align="right">31.3%</td>
<td align="right">157.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">130</td>
<td align="right">31.9%</td>
<td align="left">434</td>
<td align="right">22.9%</td>
<td align="right">233.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">23</td>
<td align="right">5.7%</td>
<td align="left">619</td>
<td align="right">32.6%</td>
<td align="right">2,591.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">22</td>
<td align="right">5.4%</td>
<td align="left">162</td>
<td align="right">8.5%</td>
<td align="right">636.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1</td>
<td align="right">0.2%</td>
<td align="left">88</td>
<td align="right">4.6%</td>
<td align="right">8,700.0%</td>
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
<td align="left"><= 8</td>
<td align="right">84</td>
<td align="right">20.6%</td>
<td align="right">112</td>
<td align="right">5.1%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">63</td>
<td align="right">15.5%</td>
<td align="right">259</td>
<td align="right">11.9%</td>
<td align="right">311.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">84</td>
<td align="right">20.6%</td>
<td align="right">287</td>
<td align="right">13.2%</td>
<td align="right">241.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">88</td>
<td align="right">21.6%</td>
<td align="right">497</td>
<td align="right">22.8%</td>
<td align="right">464.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">64</td>
<td align="right">15.7%</td>
<td align="right">327</td>
<td align="right">15.0%</td>
<td align="right">410.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">23</td>
<td align="right">5.7%</td>
<td align="right">576</td>
<td align="right">26.5%</td>
<td align="right">2,404.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">119</td>
<td align="right">5.5%</td>
<td align="right">11,800.0%</td>
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
<td align="right">84</td>
<td align="right">20.6%</td>
<td align="right">175</td>
<td align="right">8.0%</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">105</td>
<td align="right">25.8%</td>
<td align="right">309</td>
<td align="right">14.2%</td>
<td align="right">194.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">108</td>
<td align="right">26.5%</td>
<td align="right">492</td>
<td align="right">22.6%</td>
<td align="right">355.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">86</td>
<td align="right">21.1%</td>
<td align="right">374</td>
<td align="right">17.2%</td>
<td align="right">334.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23</td>
<td align="right">5.7%</td>
<td align="right">432</td>
<td align="right">19.8%</td>
<td align="right">1,778.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">114</td>
<td align="right">5.2%</td>
<td align="right">114 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,184</td>
<td align="right">511,276</td>
<td align="right">23,310.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">62,626</td>
<td align="right">1,486,381</td>
<td align="right">2,273.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">24,843</td>
<td align="right">521,474</td>
<td align="right">1,999.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">24,843</td>
<td align="right">519,920</td>
<td align="right">1,992.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">27,165</td>
<td align="right">463,331</td>
<td align="right">1,605.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">27,165</td>
<td align="right">389,280</td>
<td align="right">1,333.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">166,245</td>
<td align="right">1,699,867</td>
<td align="right">922.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">37,783</td>
<td align="right">295,340</td>
<td align="right">681.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">44,961</td>
<td align="right">336,547</td>
<td align="right">648.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">122,075</td>
<td align="right">695,373</td>
<td align="right">469.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">27,165</td>
<td align="right">145,864</td>
<td align="right">437.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">27,165</td>
<td align="right">145,864</td>
<td align="right">437.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">75,621</td>
<td align="right">364,197</td>
<td align="right">381.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,163</td>
<td align="right">9,957</td>
<td align="right">360.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">139,578</td>
<td align="right">632,395</td>
<td align="right">353.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">84,292</td>
<td align="right">328,723</td>
<td align="right">290.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,082,521</td>
<td align="right">4,050,153</td>
<td align="right">274.1%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">84,292</td>
<td align="right">287,206</td>
<td align="right">240.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">84,292</td>
<td align="right">287,206</td>
<td align="right">240.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">414,348</td>
<td align="right">1,393,122</td>
<td align="right">236.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">73,458</td>
<td align="right">234,147</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">513,117</td>
<td align="right">1,571,302</td>
<td align="right">206.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">149,079</td>
<td align="right">402,724</td>
<td align="right">170.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">340,847</td>
<td align="right">916,603</td>
<td align="right">168.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">368,685</td>
<td align="right">977,054</td>
<td align="right">165.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">191,493</td>
<td align="right">486,496</td>
<td align="right">154.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">73,074</td>
<td align="right">184,030</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">73,074</td>
<td align="right">184,030</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">646,912</td>
<td align="right">1,606,174</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">841,328</td>
<td align="right">1,958,332</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">157,374</td>
<td align="right">360,131</td>
<td align="right">128.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">402,567</td>
<td align="right">779,904</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">326,423</td>
<td align="right">617,379</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">730,289</td>
<td align="right">79,368</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">491,349</td>
<td align="right">57,807</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">354,251</td>
<td align="right">45,138</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">112,413</td>
<td align="right">21,938</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,882,796</td>
<td align="right">3,390,116</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,882,796</td>
<td align="right">3,390,116</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,882,796</td>
<td align="right">3,390,116</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">286,968</td>
<td align="right">506,771</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,415,073</td>
<td align="right">6,017,463</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,988,074</td>
<td align="right">3,393,390</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,509,528</td>
<td align="right">10,979,483</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,509,528</td>
<td align="right">10,979,463</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">7,340,409</td>
<td align="right">12,120,630</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">514,980</td>
<td align="right">831,016</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,855,631</td>
<td align="right">2,989,181</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">655,225</td>
<td align="right">265,150</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">548,926</td>
<td align="right">872,651</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">542,570</td>
<td align="right">854,244</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,514,111</td>
<td align="right">2,349,232</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">318,275</td>
<td align="right">492,698</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,358,852</td>
<td align="right">2,086,423</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">31,881,309</td>
<td align="right">46,611,965</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,469,117</td>
<td align="right">2,145,696</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">23,496,670</td>
<td align="right">33,697,862</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,341,192</td>
<td align="right">1,889,594</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">830,881</td>
<td align="right">1,141,147</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,909,950</td>
<td align="right">8,114,571</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">255,602</td>
<td align="right">339,927</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,236,754</td>
<td align="right">4,304,022</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">782,811</td>
<td align="right">524,904</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">917,677</td>
<td align="right">1,214,610</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,614,926</td>
<td align="right">7,411,462</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,664,138</td>
<td align="right">2,186,671</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,792,665</td>
<td align="right">2,263,185</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,371,840</td>
<td align="right">4,247,053</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,792,665</td>
<td align="right">2,239,569</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">947,016</td>
<td align="right">1,173,642</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,560,761</td>
<td align="right">1,927,789</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">860,323</td>
<td align="right">1,041,370</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">911,894</td>
<td align="right">1,097,546</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,594,154</td>
<td align="right">4,294,593</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,471,301</td>
<td align="right">4,143,895</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">219,606</td>
<td align="right">261,942</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">259,881</td>
<td align="right">213,112</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">259,881</td>
<td align="right">213,112</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,751,154</td>
<td align="right">6,754,894</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,565,117</td>
<td align="right">1,798,654</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,161,079</td>
<td align="right">1,328,273</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">403,921</td>
<td align="right">450,054</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">222,098</td>
<td align="right">202,363</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">800,100</td>
<td align="right">865,970</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">232,892</td>
<td align="right">251,335</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">926,938</td>
<td align="right">853,831</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">785,059</td>
<td align="right">827,418</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,100,041</td>
<td align="right">4,311,976</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,852,514</td>
<td align="right">2,947,040</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,852,514</td>
<td align="right">2,947,040</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">800,100</td>
<td align="right">809,299</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">840,468</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">484,075</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right"></td>
<td align="right">402,292</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right"></td>
<td align="right">390,235</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">326,594</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">238,830</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">225,078</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">209,578</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">159,586</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">157,209</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right">155,844</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">153,916</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">116,881</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">113,049</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">95,582</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">77,182</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">74,733</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">69,310</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">51,244</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">48,972</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right"></td>
<td align="right">43,601</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">42,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">42,073</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">36,628</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">33,943</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">33,943</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">31,143</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">29,822</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">28,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">28,259</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">23,021</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_THIRD_NULL</td>
<td align="right"></td>
<td align="right">21,357</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">20,136</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">20,125</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">19,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">19,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">19,782</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">17,330</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">17,213</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">17,074</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">17,025</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">17,025</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">15,035</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">14,911</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">14,911</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">14,868</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">14,868</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right"></td>
<td align="right">8,639</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">8,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">8,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">8,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">4,305</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">1,827</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">1,827</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">1,554</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">1,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">1,365</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">1,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">1,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">1,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">1,050</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">1,050</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right"></td>
<td align="right">151</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right">105</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-24
