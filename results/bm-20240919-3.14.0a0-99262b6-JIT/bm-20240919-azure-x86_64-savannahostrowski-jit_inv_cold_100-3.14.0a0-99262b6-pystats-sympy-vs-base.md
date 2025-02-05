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
<td align="right">427,404</td>
<td align="right">95,124,340</td>
<td align="right">22,156.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">76,340</td>
<td align="right">1,282,380</td>
<td align="right">1,579.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">188,093</td>
<td align="right">3,082,585</td>
<td align="right">1,538.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,923,052</td>
<td align="right">17,998,274</td>
<td align="right">835.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">244,880</td>
<td align="right">2,031,383</td>
<td align="right">729.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,513,480</td>
<td align="right">21,424,435</td>
<td align="right">509.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">101,060</td>
<td align="right">499,420</td>
<td align="right">394.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">117,080</td>
<td align="right">537,360</td>
<td align="right">359.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,445,353</td>
<td align="right">13,960,339</td>
<td align="right">305.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,530,841</td>
<td align="right">41,632,760</td>
<td align="right">295.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">232,488</td>
<td align="right">851,597</td>
<td align="right">266.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,841,547</td>
<td align="right">9,955,694</td>
<td align="right">250.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,312,577</td>
<td align="right">11,294,094</td>
<td align="right">240.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,153,476</td>
<td align="right">88,963,514</td>
<td align="right">227.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,645,420</td>
<td align="right">11,779,578</td>
<td align="right">223.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,077,184</td>
<td align="right">12,962,746</td>
<td align="right">217.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,844,106</td>
<td align="right">12,978,654</td>
<td align="right">167.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,870,528</td>
<td align="right">5,005,143</td>
<td align="right">167.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,400,114</td>
<td align="right">19,666,572</td>
<td align="right">165.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,615,519</td>
<td align="right">8,821,544</td>
<td align="right">144.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,679,250</td>
<td align="right">3,786,970</td>
<td align="right">125.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,776,678</td>
<td align="right">90,939,411</td>
<td align="right">117.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,695,252</td>
<td align="right">92,895,615</td>
<td align="right">107.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">42,025</td>
<td align="right">1,280</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,352,447</td>
<td align="right">4,475,774</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,040,161</td>
<td align="right">19,046,979</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">3,600</td>
<td align="right">6,680</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,304,964</td>
<td align="right">28,675,770</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">21,653,091</td>
<td align="right">37,641,211</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,450,322</td>
<td align="right">2,495,086</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">839,122</td>
<td align="right">1,442,371</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">51,053,393</td>
<td align="right">82,955,366</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">27,197,823</td>
<td align="right">44,180,709</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,209,805</td>
<td align="right">21,075,300</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,673,221</td>
<td align="right">35,936,988</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,444,234</td>
<td align="right">50,119,456</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,578,920</td>
<td align="right">29,141,491</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,004,728</td>
<td align="right">26,560,848</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">23,539,457</td>
<td align="right">36,200,596</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">300</td>
<td align="right">140</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,092,696</td>
<td align="right">62,997,760</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">54,927,206</td>
<td align="right">79,741,678</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,040</td>
<td align="right">1,120</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">42,249,967</td>
<td align="right">61,287,412</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,207,031</td>
<td align="right">56,666,391</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,624,918</td>
<td align="right">15,322,092</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,829,485</td>
<td align="right">48,718,027</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">50,195</td>
<td align="right">28,279</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">51,948,574</td>
<td align="right">73,932,668</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,711,842</td>
<td align="right">200,212,419</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,028,536</td>
<td align="right">601,036</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">197,137,370</td>
<td align="right">274,927,343</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">122,240,129</td>
<td align="right">168,476,622</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,845,701</td>
<td align="right">5,296,198</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">168,659,700</td>
<td align="right">231,172,090</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">592,069,273</td>
<td align="right">807,799,962</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,746,288</td>
<td align="right">6,445,185</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">12,329,043</td>
<td align="right">16,622,183</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">320</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,040,767</td>
<td align="right">56,082,575</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,055,634</td>
<td align="right">20,884,882</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,118,686</td>
<td align="right">785,440</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92,651,886</td>
<td align="right">119,547,175</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">121,676,366</td>
<td align="right">156,445,041</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,565,370</td>
<td align="right">21,282,897</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,928,381</td>
<td align="right">30,673,726</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,657,148</td>
<td align="right">39,143,863</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">19,019,779</td>
<td align="right">13,773,066</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">532,256</td>
<td align="right">385,476</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">519,360</td>
<td align="right">376,320</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">22,532</td>
<td align="right">16,594</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,031,413</td>
<td align="right">2,549,152</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">170,566,445</td>
<td align="right">212,307,879</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,628,608</td>
<td align="right">2,025,080</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,756,348</td>
<td align="right">79,443,279</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,500,369</td>
<td align="right">221,393,656</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">14,521,230</td>
<td align="right">17,780,774</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">49,711,588</td>
<td align="right">60,421,804</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,832,465</td>
<td align="right">29,502,207</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22,979,053</td>
<td align="right">27,086,612</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">940</td>
<td align="right">780</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">20,030,798</td>
<td align="right">23,391,547</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">7,231,342</td>
<td align="right">8,434,551</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,311,684</td>
<td align="right">33,756,471</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">906,786</td>
<td align="right">776,880</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">906,786</td>
<td align="right">776,880</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">906,786</td>
<td align="right">776,880</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,541,183</td>
<td align="right">16,586,944</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,355,034</td>
<td align="right">25,301,364</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">32,968,571</td>
<td align="right">37,203,615</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">19,732,052</td>
<td align="right">22,189,298</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">769,105</td>
<td align="right">863,340</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,045,882</td>
<td align="right">5,656,276</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,450,429</td>
<td align="right">2,719,047</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,095,804</td>
<td align="right">3,429,503</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">56,057,835</td>
<td align="right">61,894,944</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">25,268,629</td>
<td align="right">27,832,968</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">119,118</td>
<td align="right">108,240</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,480</td>
<td align="right">10,480</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,340,218</td>
<td align="right">1,233,368</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,334,570</td>
<td align="right">5,747,414</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">543,623</td>
<td align="right">506,597</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,760</td>
<td align="right">4,440</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,847,174</td>
<td align="right">5,168,685</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,252</td>
<td align="right">112,534</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,135,857</td>
<td align="right">8,586,194</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">23,354,943</td>
<td align="right">22,144,736</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">227,530</td>
<td align="right">216,153</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">530,776</td>
<td align="right">504,243</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,389,209</td>
<td align="right">1,320,323</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,958,574</td>
<td align="right">8,579,780</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">21,734,297</td>
<td align="right">22,551,652</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">178,051,609</td>
<td align="right">171,372,618</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,845</td>
<td align="right">38,369</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">887,858</td>
<td align="right">854,986</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,656,361</td>
<td align="right">12,230,701</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">442,840</td>
<td align="right">429,660</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">411,945</td>
<td align="right">399,703</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">126,510,001</td>
<td align="right">123,440,518</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">210,314</td>
<td align="right">205,228</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,188,035</td>
<td align="right">13,503,442</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,881</td>
<td align="right">95,918</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,349,304</td>
<td align="right">1,320,203</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,591,860</td>
<td align="right">1,561,288</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,207,211</td>
<td align="right">8,063,101</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">28,013,260</td>
<td align="right">27,545,095</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,182,023</td>
<td align="right">1,162,351</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">54,774,137</td>
<td align="right">55,602,974</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,784,229</td>
<td align="right">1,758,011</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">867,466</td>
<td align="right">855,314</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,518,232</td>
<td align="right">1,538,977</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,970,049</td>
<td align="right">14,136,497</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,027,509</td>
<td align="right">5,074,199</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,572,593</td>
<td align="right">1,559,753</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,515,169</td>
<td align="right">1,502,960</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,582,457</td>
<td align="right">2,562,354</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">233,080</td>
<td align="right">231,480</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,098,350</td>
<td align="right">2,084,853</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">140,940</td>
<td align="right">140,140</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">282,560</td>
<td align="right">280,960</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">282,600</td>
<td align="right">281,000</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">9,430,794</td>
<td align="right">9,382,423</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,491,645</td>
<td align="right">7,475,026</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,205</td>
<td align="right">1,203</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">142,545</td>
<td align="right">142,347</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,010</td>
<td align="right">4,006</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,719,401</td>
<td align="right">5,715,185</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">181,994</td>
<td align="right">181,908</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,608,620</td>
<td align="right">8,612,104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,781</td>
<td align="right">532,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,770</td>
<td align="right">12,766</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47,579</td>
<td align="right">47,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,696</td>
<td align="right">262,632</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">165,210</td>
<td align="right">165,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">139,180</td>
<td align="right">139,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">72,160</td>
<td align="right">72,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">63,800</td>
<td align="right">63,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">19,260</td>
<td align="right">19,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,100</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,840</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">29,256,631</td>
<td align="right">60.8%</td>
<td align="right">33,701,725</td>
<td align="right">67.6%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,837,125</td>
<td align="right">39.1%</td>
<td align="right">16,063,482</td>
<td align="right">32.2%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">6,764</td>
<td align="right">12.3%</td>
<td align="right">6,722</td>
<td align="right">12.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48,289</td>
<td align="right">87.7%</td>
<td align="right">48,024</td>
<td align="right">87.7%</td>
<td align="right">-0.5%</td>
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
<td align="left">true divide float</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">226</td>
<td align="right">0.5%</td>
<td align="right">183</td>
<td align="right">0.4%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,192</td>
<td align="right">2.5%</td>
<td align="right">1,085</td>
<td align="right">2.3%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,840</td>
<td align="right">12.1%</td>
<td align="right">6,315</td>
<td align="right">13.1%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,868</td>
<td align="right">5.9%</td>
<td align="right">2,661</td>
<td align="right">5.5%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">584</td>
<td align="right">1.2%</td>
<td align="right">543</td>
<td align="right">1.1%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">280</td>
<td align="right">0.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,524</td>
<td align="right">5.2%</td>
<td align="right">2,363</td>
<td align="right">4.9%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,829</td>
<td align="right">7.9%</td>
<td align="right">3,636</td>
<td align="right">7.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">377</td>
<td align="right">0.8%</td>
<td align="right">358</td>
<td align="right">0.7%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,120</td>
<td align="right">4.4%</td>
<td align="right">2,216</td>
<td align="right">4.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,816</td>
<td align="right">3.8%</td>
<td align="right">1,740</td>
<td align="right">3.6%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,051</td>
<td align="right">4.2%</td>
<td align="right">1,996</td>
<td align="right">4.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,848</td>
<td align="right">8.0%</td>
<td align="right">3,756</td>
<td align="right">7.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,744</td>
<td align="right">14.0%</td>
<td align="right">6,887</td>
<td align="right">14.3%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,116</td>
<td align="right">2.3%</td>
<td align="right">1,132</td>
<td align="right">2.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,700</td>
<td align="right">7.7%</td>
<td align="right">3,660</td>
<td align="right">7.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,150</td>
<td align="right">18.9%</td>
<td align="right">9,210</td>
<td align="right">19.2%</td>
<td align="right">0.7%</td>
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
<td align="right">532,781</td>
<td align="right">100.0%</td>
<td align="right">532,976</td>
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
<td align="right">3,495,644</td>
<td align="right">7.6%</td>
<td align="right">21,402,384</td>
<td align="right">37.0%</td>
<td align="right">512.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,923</td>
<td align="right">0.0%</td>
<td align="right">10,097</td>
<td align="right">0.0%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,674,431</td>
<td align="right">92.4%</td>
<td align="right">36,430,505</td>
<td align="right">63.0%</td>
<td align="right">-14.6%</td>
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
<td align="right">10,355</td>
<td align="right">57.3%</td>
<td align="right">14,576</td>
<td align="right">65.7%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,721</td>
<td align="right">42.7%</td>
<td align="right">7,615</td>
<td align="right">34.3%</td>
<td align="right">-1.4%</td>
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
<td align="right">7,171</td>
<td align="right">69.3%</td>
<td align="right">11,553</td>
<td align="right">79.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,960</td>
<td align="right">18.9%</td>
<td align="right">1,740</td>
<td align="right">11.9%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,200</td>
<td align="right">11.6%</td>
<td align="right">1,260</td>
<td align="right">8.6%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,800</td>
<td align="right">0.0%</td>
<td align="right">23,560</td>
<td align="right">0.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">384,884,199</td>
<td align="right">92.7%</td>
<td align="right">363,847,934</td>
<td align="right">92.2%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,132,999</td>
<td align="right">7.3%</td>
<td align="right">30,431,908</td>
<td align="right">7.7%</td>
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
<td align="right">167,601</td>
<td align="right">0.0%</td>
<td align="right">167,564</td>
<td align="right">0.0%</td>
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
<td align="right">667,107</td>
<td align="right">100.0%</td>
<td align="right">672,711</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
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
<td align="right">3,580</td>
<td align="right">21.9%</td>
<td align="right">3,180</td>
<td align="right">19.9%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,988</td>
<td align="right">48.9%</td>
<td align="right">7,986</td>
<td align="right">50.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">22,600,467</td>
<td align="right">25.3%</td>
<td align="right">35,860,501</td>
<td align="right">36.7%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">66,065,887</td>
<td align="right">74.1%</td>
<td align="right">61,325,445</td>
<td align="right">62.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">465,603</td>
<td align="right">0.5%</td>
<td align="right">492,406</td>
<td align="right">0.5%</td>
<td align="right">5.8%</td>
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
<td align="right">63,131</td>
<td align="right">77.6%</td>
<td align="right">66,839</td>
<td align="right">78.1%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,203</td>
<td align="right">22.4%</td>
<td align="right">18,714</td>
<td align="right">21.9%</td>
<td align="right">2.8%</td>
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
<td align="left">bool</td>
<td align="right">427</td>
<td align="right">0.7%</td>
<td align="right">2,090</td>
<td align="right">3.1%</td>
<td align="right">389.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,887</td>
<td align="right">20.4%</td>
<td align="right">14,315</td>
<td align="right">21.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16,229</td>
<td align="right">25.7%</td>
<td align="right">17,837</td>
<td align="right">26.7%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">260</td>
<td align="right">0.4%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">320</td>
<td align="right">0.5%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,154</td>
<td align="right">19.3%</td>
<td align="right">11,503</td>
<td align="right">17.2%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,914</td>
<td align="right">15.7%</td>
<td align="right">9,794</td>
<td align="right">14.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,320</td>
<td align="right">16.3%</td>
<td align="right">10,200</td>
<td align="right">15.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
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
<td align="right">1,911,918</td>
<td align="right">6.0%</td>
<td align="right">17,983,423</td>
<td align="right">39.0%</td>
<td align="right">840.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,685,649</td>
<td align="right">93.9%</td>
<td align="right">28,061,080</td>
<td align="right">60.9%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">9,894</td>
<td align="right">88.9%</td>
<td align="right">13,611</td>
<td align="right">91.7%</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">11.1%</td>
<td align="right">1,240</td>
<td align="right">8.3%</td>
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
<td align="right">3,554</td>
<td align="right">35.9%</td>
<td align="right">7,030</td>
<td align="right">51.6%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,120</td>
<td align="right">51.7%</td>
<td align="right">5,361</td>
<td align="right">39.4%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">940</td>
<td align="right">9.5%</td>
<td align="right">940</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">280</td>
<td align="right">2.8%</td>
<td align="right">280</td>
<td align="right">2.1%</td>
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
<td align="right">118,252</td>
<td align="right">0.2%</td>
<td align="right">1,485,114</td>
<td align="right">1.0%</td>
<td align="right">1,155.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,106,614</td>
<td align="right">55.0%</td>
<td align="right">88,863,768</td>
<td align="right">58.8%</td>
<td align="right">227.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,984,317</td>
<td align="right">44.6%</td>
<td align="right">60,566,523</td>
<td align="right">40.1%</td>
<td align="right">175.5%</td>
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
<td align="right">14,127</td>
<td align="right">28.9%</td>
<td align="right">39,921</td>
<td align="right">31.3%</td>
<td align="right">182.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,838</td>
<td align="right">71.1%</td>
<td align="right">87,726</td>
<td align="right">68.7%</td>
<td align="right">151.8%</td>
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
<td align="right">16,512</td>
<td align="right">47.4%</td>
<td align="right">62,482</td>
<td align="right">71.2%</td>
<td align="right">278.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">3,998</td>
<td align="right">11.5%</td>
<td align="right">8,582</td>
<td align="right">9.8%</td>
<td align="right">114.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,720</td>
<td align="right">13.5%</td>
<td align="right">7,062</td>
<td align="right">8.1%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">720</td>
<td align="right">0.8%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,468</td>
<td align="right">10.0%</td>
<td align="right">3,555</td>
<td align="right">4.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,840</td>
<td align="right">5.3%</td>
<td align="right">1,800</td>
<td align="right">2.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,400</td>
<td align="right">4.0%</td>
<td align="right">1,425</td>
<td align="right">1.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,960</td>
<td align="right">5.6%</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
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
<td align="right">33,219,908</td>
<td align="right">8.6%</td>
<td align="right">52,135,784</td>
<td align="right">12.8%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,500</td>
<td align="right">0.0%</td>
<td align="right">15,440</td>
<td align="right">0.0%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">64,541,292</td>
<td align="right">16.8%</td>
<td align="right">79,227,370</td>
<td align="right">19.4%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">286,796,580</td>
<td align="right">74.5%</td>
<td align="right">276,202,445</td>
<td align="right">67.7%</td>
<td align="right">-3.7%</td>
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
<td align="right">710,854</td>
<td align="right">85.4%</td>
<td align="right">1,067,809</td>
<td align="right">89.7%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">121,921</td>
<td align="right">14.6%</td>
<td align="right">122,792</td>
<td align="right">10.3%</td>
<td align="right">0.7%</td>
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
<td align="left">builtin class method</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">1,174</td>
<td align="right">1.0%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">480</td>
<td align="right">0.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">5,054</td>
<td align="right">4.1%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,913</td>
<td align="right">7.3%</td>
<td align="right">8,575</td>
<td align="right">7.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,744</td>
<td align="right">6.4%</td>
<td align="right">7,975</td>
<td align="right">6.5%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">59</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">14,880</td>
<td align="right">12.2%</td>
<td align="right">15,080</td>
<td align="right">12.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">11,726</td>
<td align="right">9.6%</td>
<td align="right">11,769</td>
<td align="right">9.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,270</td>
<td align="right">7.6%</td>
<td align="right">9,296</td>
<td align="right">7.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">59,468</td>
<td align="right">48.8%</td>
<td align="right">59,522</td>
<td align="right">48.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
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
<td align="right">265,092,591</td>
<td align="right">99.9%</td>
<td align="right">332,477,216</td>
<td align="right">99.9%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">90,141</td>
<td align="right">0.0%</td>
<td align="right">90,088</td>
<td align="right">0.0%</td>
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
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">20,380</td>
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
<td align="right">92,013</td>
<td align="right">100.0%</td>
<td align="right">91,980</td>
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
<td align="right">2,996,172</td>
<td align="right">100.0%</td>
<td align="right">2,934,733</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">605</td>
<td align="right">0.0%</td>
<td align="right">603</td>
<td align="right">0.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">999,176</td>
<td align="right">67.8%</td>
<td align="right">576,336</td>
<td align="right">55.9%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,640</td>
<td align="right">2.1%</td>
<td align="right">24,700</td>
<td align="right">2.4%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
<td align="right">427,060</td>
<td align="right">41.4%</td>
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
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">500</td>
<td align="right">16.2%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,060</td>
<td align="right">83.2%</td>
<td align="right">2,580</td>
<td align="right">83.8%</td>
<td align="right">-15.7%</td>
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
<td align="right">3,060</td>
<td align="right">100.0%</td>
<td align="right">2,580</td>
<td align="right">100.0%</td>
<td align="right">-15.7%</td>
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
<td align="right">426,445</td>
<td align="right">3.6%</td>
<td align="right">2,077,738</td>
<td align="right">16.4%</td>
<td align="right">387.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,154,207</td>
<td align="right">93.0%</td>
<td align="right">10,180,893</td>
<td align="right">80.4%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">403,137</td>
<td align="right">3.4%</td>
<td align="right">390,937</td>
<td align="right">3.1%</td>
<td align="right">-3.0%</td>
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
<td align="right">12,979</td>
<td align="right">77.8%</td>
<td align="right">44,184</td>
<td align="right">92.3%</td>
<td align="right">240.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,708</td>
<td align="right">22.2%</td>
<td align="right">3,666</td>
<td align="right">7.7%</td>
<td align="right">-1.1%</td>
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
<td align="right">1,448</td>
<td align="right">39.1%</td>
<td align="right">1,406</td>
<td align="right">38.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">1,960</td>
<td align="right">53.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
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
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">780</td>
<td align="right">100.0%</td>
<td align="right">-17.0%</td>
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
<td align="right">182,535</td>
<td align="right">0.8%</td>
<td align="right">3,076,491</td>
<td align="right">15.1%</td>
<td align="right">1,585.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,620,605</td>
<td align="right">99.2%</td>
<td align="right">17,294,793</td>
<td align="right">84.9%</td>
<td align="right">-23.5%</td>
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
<td align="right">2,836</td>
<td align="right">51.0%</td>
<td align="right">3,374</td>
<td align="right">55.4%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,722</td>
<td align="right">49.0%</td>
<td align="right">2,720</td>
<td align="right">44.6%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,836</td>
<td align="right">100.0%</td>
<td align="right">3,374</td>
<td align="right">100.0%</td>
<td align="right">19.0%</td>
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
<td align="right">440,100</td>
<td align="right">0.2%</td>
<td align="right">680,682</td>
<td align="right">0.3%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,580,958</td>
<td align="right">6.0%</td>
<td align="right">12,150,511</td>
<td align="right">5.9%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">196,734,800</td>
<td align="right">93.8%</td>
<td align="right">193,704,920</td>
<td align="right">93.8%</td>
<td align="right">-1.5%</td>
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
<td align="right">22,753</td>
<td align="right">27.6%</td>
<td align="right">27,479</td>
<td align="right">29.9%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,760</td>
<td align="right">72.4%</td>
<td align="right">64,386</td>
<td align="right">70.1%</td>
<td align="right">7.7%</td>
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
<td align="right">1,633</td>
<td align="right">7.2%</td>
<td align="right">3,791</td>
<td align="right">13.8%</td>
<td align="right">132.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,801</td>
<td align="right">47.5%</td>
<td align="right">13,677</td>
<td align="right">49.8%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,437</td>
<td align="right">6.3%</td>
<td align="right">1,306</td>
<td align="right">4.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,502</td>
<td align="right">15.4%</td>
<td align="right">3,355</td>
<td align="right">12.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,080</td>
<td align="right">9.1%</td>
<td align="right">2,050</td>
<td align="right">7.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">3,260</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,672</td>
<td align="right">0.0%</td>
<td align="right">26,227</td>
<td align="right">0.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">105,946,580</td>
<td align="right">100.0%</td>
<td align="right">104,686,570</td>
<td align="right">100.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">777</td>
<td align="right">6.4%</td>
<td align="right">758</td>
<td align="right">6.2%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,396</td>
<td align="right">93.6%</td>
<td align="right">11,384</td>
<td align="right">93.8%</td>
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
<td align="left">sequence</td>
<td align="right">717</td>
<td align="right">92.3%</td>
<td align="right">698</td>
<td align="right">92.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">60</td>
<td align="right">7.7%</td>
<td align="right">60</td>
<td align="right">7.9%</td>
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
<td align="right">164,062,731</td>
<td align="right">4.4%</td>
<td align="right">294,696,244</td>
<td align="right">5.8%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">64,874,150</td>
<td align="right">1.7%</td>
<td align="right">87,737,391</td>
<td align="right">1.7%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,194,883,299</td>
<td align="right">32.0%</td>
<td align="right">1,596,246,597</td>
<td align="right">31.7%</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,312,918,068</td>
<td align="right">61.9%</td>
<td align="right">3,061,965,415</td>
<td align="right">60.7%</td>
<td align="right">32.4%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">1,911,918</td>
<td align="right">1.2%</td>
<td align="right">17,983,423</td>
<td align="right">6.1%</td>
<td align="right">840.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,495,644</td>
<td align="right">2.1%</td>
<td align="right">21,402,384</td>
<td align="right">7.3%</td>
<td align="right">512.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,106,614</td>
<td align="right">16.6%</td>
<td align="right">88,863,768</td>
<td align="right">30.2%</td>
<td align="right">227.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,600,467</td>
<td align="right">13.8%</td>
<td align="right">35,860,501</td>
<td align="right">12.2%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,541,292</td>
<td align="right">39.5%</td>
<td align="right">79,227,370</td>
<td align="right">27.0%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,256,631</td>
<td align="right">17.9%</td>
<td align="right">33,701,725</td>
<td align="right">11.5%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,580,958</td>
<td align="right">7.7%</td>
<td align="right">12,150,511</td>
<td align="right">4.1%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
<td align="right">427,060</td>
<td align="right">0.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,781</td>
<td align="right">0.3%</td>
<td align="right">532,976</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">403,137</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3,076,491</td>
<td align="right">1.0%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">425,465</td>
<td align="right">0.7%</td>
<td align="right">2,077,238</td>
<td align="right">2.4%</td>
<td align="right">388.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,545,630</td>
<td align="right">14.7%</td>
<td align="right">16,315,655</td>
<td align="right">18.5%</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">14,018,175</td>
<td align="right">21.6%</td>
<td align="right">23,730,676</td>
<td align="right">26.9%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,408,457</td>
<td align="right">8.3%</td>
<td align="right">8,121,339</td>
<td align="right">9.2%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,163,454</td>
<td align="right">9.5%</td>
<td align="right">7,024,024</td>
<td align="right">8.0%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,729,150</td>
<td align="right">22.7%</td>
<td align="right">14,162,055</td>
<td align="right">16.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,671,225</td>
<td align="right">5.7%</td>
<td align="right">3,549,545</td>
<td align="right">4.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,661,166</td>
<td align="right">4.1%</td>
<td align="right">2,625,466</td>
<td align="right">3.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,512,248</td>
<td align="right">10.0%</td>
<td align="right">6,463,817</td>
<td align="right">7.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">464,003</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">760,349</td>
<td align="right">0.9%</td>
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
<td align="right">1,367,271</td>
<td align="right">0.5%</td>
<td align="right">1,111,391</td>
<td align="right">0.4%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">146,233,871</td>
<td align="right">53.6%</td>
<td align="right">138,836,105</td>
<td align="right">52.9%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">29,491,487</td>
<td align="right">10.8%</td>
<td align="right">28,357,824</td>
<td align="right">10.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">243,179,611</td>
<td align="right">89.1%</td>
<td align="right">234,225,629</td>
<td align="right">89.2%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">126,753,534</td>
<td align="right">46.4%</td>
<td align="right">123,616,428</td>
<td align="right">47.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">126,753,534</td>
<td align="right">46.4%</td>
<td align="right">123,616,428</td>
<td align="right">47.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">52,808,953</td>
<td align="right">19.3%</td>
<td align="right">51,665,030</td>
<td align="right">19.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">23,783,689</td>
<td align="right">8.7%</td>
<td align="right">23,273,271</td>
<td align="right">8.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">97,254,747</td>
<td align="right">35.6%</td>
<td align="right">95,251,304</td>
<td align="right">36.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">97,262,047</td>
<td align="right">35.6%</td>
<td align="right">95,258,604</td>
<td align="right">36.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,824,994</td>
<td align="right">4.3%</td>
<td align="right">11,717,171</td>
<td align="right">4.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">6,960</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,051,798</td>
<td align="right">0.2%</td>
<td align="right">1,662,505</td>
<td align="right">0.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">2,667,383,842</td>
<td align="right">2,667,383,842 / 0 !!</td>
<td align="right">1,719,011,593</td>
<td align="right">1,719,011,593 / 0 !!</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">2,756,639,053</td>
<td align="right">2,756,639,053 / 0 !!</td>
<td align="right">1,862,956,768</td>
<td align="right">1,862,956,768 / 0 !!</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,790,685,137</td>
<td align="right">1,790,685,137 / 0 !!</td>
<td align="right">2,270,933,368</td>
<td align="right">2,270,933,368 / 0 !!</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">2,275,838,518</td>
<td align="right">2,275,838,518 / 0 !!</td>
<td align="right">2,689,381,164</td>
<td align="right">2,689,381,164 / 0 !!</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">4,259,727</td>
<td align="right"></td>
<td align="right">3,844,559</td>
<td align="right"></td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,334,842</td>
<td align="right"></td>
<td align="right">4,863,503</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,078,677</td>
<td align="right"></td>
<td align="right">1,021,947</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,393,032</td>
<td align="right"></td>
<td align="right">1,335,057</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">193,081,034</td>
<td align="right"></td>
<td align="right">185,748,811</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,831,852</td>
<td align="right">44.4%</td>
<td align="right">282,181,454</td>
<td align="right">43.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,908,110</td>
<td align="right">44.6%</td>
<td align="right">283,868,099</td>
<td align="right">44.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">306,828,638</td>
<td align="right"></td>
<td align="right">297,714,031</td>
<td align="right"></td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">337,262,612</td>
<td align="right"></td>
<td align="right">331,279,056</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">24,140</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">364,493,016</td>
<td align="right">55.4%</td>
<td align="right">360,496,594</td>
<td align="right">55.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">364,731,848</td>
<td align="right"></td>
<td align="right">360,735,434</td>
<td align="right"></td>
<td align="right">-1.1%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">244</td>
<td align="right">0.3%</td>
<td align="right">30,931</td>
<td align="right">4.1%</td>
<td align="right">12,576.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">32,098</td>
<td align="right">36.2%</td>
<td align="right">703,486</td>
<td align="right">92.4%</td>
<td align="right">2,091.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">3,686</td>
<td align="right">0.5%</td>
<td align="right">1,216.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">88,785</td>
<td align="right"></td>
<td align="right">761,583</td>
<td align="right"></td>
<td align="right">757.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,162</td>
<td align="right">2.4%</td>
<td align="right">14,646</td>
<td align="right">1.9%</td>
<td align="right">577.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">52,522</td>
<td align="right">59.2%</td>
<td align="right">212,885</td>
<td align="right">28.0%</td>
<td align="right">305.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">371,879,582</td>
<td align="right"></td>
<td align="right">108,977,188</td>
<td align="right"></td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">311</td>
<td align="right">1.0%</td>
<td align="right">95</td>
<td align="right">0.0%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,318,198,507</td>
<td align="right">1,430.1%</td>
<td align="right">1,790,381,123</td>
<td align="right">1,642.9%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">56,687</td>
<td align="right">63.8%</td>
<td align="right">58,097</td>
<td align="right">7.6%</td>
<td align="right">2.5%</td>
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
<td align="right">30,483</td>
<td align="right">95.0%</td>
<td align="right">700,543</td>
<td align="right">99.6%</td>
<td align="right">2,198.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">32,098</td>
<td align="right"></td>
<td align="right">703,486</td>
<td align="right"></td>
<td align="right">2,091.7%</td>
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
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
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
<td align="right">543</td>
<td align="right">1.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,078</td>
<td align="right">12.7%</td>
<td align="right">11,483</td>
<td align="right">1.6%</td>
<td align="right">181.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,355</td>
<td align="right">13.6%</td>
<td align="right">84,087</td>
<td align="right">12.0%</td>
<td align="right">1,830.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,364</td>
<td align="right">38.5%</td>
<td align="right">420,742</td>
<td align="right">59.8%</td>
<td align="right">3,303.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,831</td>
<td align="right">24.4%</td>
<td align="right">140,129</td>
<td align="right">19.9%</td>
<td align="right">1,689.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,787</td>
<td align="right">8.7%</td>
<td align="right">46,105</td>
<td align="right">6.6%</td>
<td align="right">1,554.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">940</td>
<td align="right">0.1%</td>
<td align="right">571.4%</td>
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
<td align="right">4,100</td>
<td align="right">12.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,390</td>
<td align="right">7.4%</td>
<td align="right">31,573</td>
<td align="right">4.5%</td>
<td align="right">1,221.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,210</td>
<td align="right">25.6%</td>
<td align="right">167,666</td>
<td align="right">23.8%</td>
<td align="right">1,942.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,021</td>
<td align="right">31.2%</td>
<td align="right">389,633</td>
<td align="right">55.4%</td>
<td align="right">3,788.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,202</td>
<td align="right">16.2%</td>
<td align="right">86,772</td>
<td align="right">12.3%</td>
<td align="right">1,568.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">520</td>
<td align="right">1.6%</td>
<td align="right">24,879</td>
<td align="right">3.5%</td>
<td align="right">4,684.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
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
<td align="left">_DEOPT</td>
<td align="right">114,228</td>
<td align="right">355,974</td>
<td align="right">211.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">4,427,666</td>
<td align="right">7,584</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,837,284</td>
<td align="right">3,308</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">21,610,003</td>
<td align="right">89,177</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">31,960</td>
<td align="right">180</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">852,368</td>
<td align="right">6,620</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,560</td>
<td align="right">160</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">4,520,345</td>
<td align="right">38,185</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,014,168</td>
<td align="right">26,043</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">860,265</td>
<td align="right">9,360</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">7,559,766</td>
<td align="right">97,580</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,239,824</td>
<td align="right">67,172</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">9,740,226</td>
<td align="right">228,196</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,884,316</td>
<td align="right">76,796</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,295,280</td>
<td align="right">67,307</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">658,680</td>
<td align="right">19,895</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">658,680</td>
<td align="right">19,895</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">446,180</td>
<td align="right">14,220</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">49,740</td>
<td align="right">1,625</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">418,540</td>
<td align="right">16,500</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">413,620</td>
<td align="right">17,575</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">413,620</td>
<td align="right">17,575</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">17,935,911</td>
<td align="right">869,248</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">14,864</td>
<td align="right">772</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,570,783</td>
<td align="right">329,141</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">56,660,985</td>
<td align="right">3,388,853</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">20,425,277</td>
<td align="right">1,238,105</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">903,610</td>
<td align="right">57,603</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">346,862</td>
<td align="right">23,318</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,466,590</td>
<td align="right">106,939</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">9,482,743</td>
<td align="right">738,511</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">268,475</td>
<td align="right">21,398</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">10,198,648</td>
<td align="right">833,572</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">20,243,808</td>
<td align="right">1,720,740</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">20,883,579</td>
<td align="right">1,787,027</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">711,396</td>
<td align="right">63,592</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">14,735,972</td>
<td align="right">1,371,516</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">74,598,485</td>
<td align="right">7,094,542</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,985,169</td>
<td align="right">398,893</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">13,194,560</td>
<td align="right">1,381,547</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,991,490</td>
<td align="right">1,715,526</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,991,490</td>
<td align="right">1,715,526</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,087,880</td>
<td align="right">1,657,923</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,487,855</td>
<td align="right">1,639,161</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,093,959</td>
<td align="right">3,216,659</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">12,534,303</td>
<td align="right">1,558,907</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">20,970,134</td>
<td align="right">2,744,415</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,116,981</td>
<td align="right">830,068</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">5,928,840</td>
<td align="right">830,068</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">27,914,505</td>
<td align="right">4,083,067</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">16,043,252</td>
<td align="right">2,373,931</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">18,112,442</td>
<td align="right">2,888,862</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">6,420</td>
<td align="right">1,080</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">6,088,210</td>
<td align="right">1,062,256</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">78,305,059</td>
<td align="right">13,814,596</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">44,950,112</td>
<td align="right">7,974,385</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">617,260</td>
<td align="right">112,655</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">538,311,471</td>
<td align="right">98,425,732</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">460,528</td>
<td align="right">85,670</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">62,358,688</td>
<td align="right">11,980,590</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">42,540,905</td>
<td align="right">8,737,616</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">26,666,584</td>
<td align="right">5,503,303</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">8,160</td>
<td align="right">1,740</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,857,175</td>
<td align="right">3,239,702</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,452,781</td>
<td align="right">2,397,349</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,185,439</td>
<td align="right">1,190,899</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,188,673</td>
<td align="right">1,437,723</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">26,455,702</td>
<td align="right">6,333,976</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">57,851,068</td>
<td align="right">13,920,091</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">4,318,031</td>
<td align="right">1,044,757</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">25,420,293</td>
<td align="right">6,153,546</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">67,463,934</td>
<td align="right">16,616,740</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,753,886</td>
<td align="right">7,581,084</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">54,710,316</td>
<td align="right">13,556,754</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">7,744,560</td>
<td align="right">1,944,532</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">42,254,169</td>
<td align="right">10,664,578</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,751,098</td>
<td align="right">1,453,568</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">36,667,374</td>
<td align="right">9,521,489</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">44,982,644</td>
<td align="right">11,688,112</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">47,680</td>
<td align="right">12,414</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">50,094,874</td>
<td align="right">13,059,640</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">45,141,952</td>
<td align="right">11,770,404</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,227,612</td>
<td align="right">601,610</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">271,160</td>
<td align="right">73,235</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">144,312,051</td>
<td align="right">40,226,140</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">219,553,188</td>
<td align="right">61,827,851</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">344,578,352</td>
<td align="right">97,689,141</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">371,879,582</td>
<td align="right">108,977,188</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3,900</td>
<td align="right">1,160</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">19,953,789</td>
<td align="right">6,176,989</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">54,629,468</td>
<td align="right">17,081,058</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">110,233,693</td>
<td align="right">34,795,006</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,934,980</td>
<td align="right">2,203,738</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">23,146,222</td>
<td align="right">7,417,211</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">107,564,636</td>
<td align="right">35,252,684</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,702,186</td>
<td align="right">5,846,336</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">52,784,281</td>
<td align="right">17,457,462</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">64,359,835</td>
<td align="right">21,507,439</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">17,976,025</td>
<td align="right">6,047,926</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">341,652</td>
<td align="right">115,014</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">51,641,612</td>
<td align="right">17,415,050</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,894,640</td>
<td align="right">642,542</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">338,572</td>
<td align="right">115,014</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,890,816</td>
<td align="right">642,542</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">944,019</td>
<td align="right">322,111</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">231,558,951</td>
<td align="right">79,030,487</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">30,242,544</td>
<td align="right">10,329,898</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">41,330,332</td>
<td align="right">14,434,385</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">5,287,226</td>
<td align="right">1,920,267</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">83,909,870</td>
<td align="right">31,434,059</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">115,071,804</td>
<td align="right">43,443,446</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">36,260</td>
<td align="right">13,841</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">59,177,469</td>
<td align="right">22,735,219</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">57,322,574</td>
<td align="right">22,602,716</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,915,842</td>
<td align="right">10,858,838</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">63,336,691</td>
<td align="right">26,221,881</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,825,016</td>
<td align="right">2,020,501</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">97,588</td>
<td align="right">42,732</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">18,702,431</td>
<td align="right">8,532,827</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,150,708</td>
<td align="right">1,438,578</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,266,749</td>
<td align="right">199,966,410</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,592,803</td>
<td align="right">8,650,921</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">24,307,347</td>
<td align="right">11,359,630</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">35,851,332</td>
<td align="right">16,781,623</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">52,806,875</td>
<td align="right">25,314,010</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">14,371</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">60,109,213</td>
<td align="right">29,726,800</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">16,858,386</td>
<td align="right">8,529,439</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">18,427,055</td>
<td align="right">9,645,779</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,932,982</td>
<td align="right">1,023,250</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">26,032,251</td>
<td align="right">13,897,334</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,381,048</td>
<td align="right">7,727,767</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">11,920</td>
<td align="right">6,500</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,977,371</td>
<td align="right">6,406,700</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">25,115,358</td>
<td align="right">14,845,601</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">32,216,681</td>
<td align="right">19,451,720</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,770,758</td>
<td align="right">22,248,837</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">24,156,838</td>
<td align="right">14,619,446</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,528,291</td>
<td align="right">9,555,663</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">134,315,902</td>
<td align="right">83,536,252</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">15,276,582</td>
<td align="right">9,662,329</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,540</td>
<td align="right">1,625</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">980</td>
<td align="right">629</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">268,440</td>
<td align="right">178,138</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,682,226</td>
<td align="right">6,500,878</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,682,226</td>
<td align="right">6,500,878</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,488,242</td>
<td align="right">1,008,110</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">12,406,998</td>
<td align="right">8,527,150</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,562,481</td>
<td align="right">7,591,420</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">8,731,106</td>
<td align="right">6,341,926</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">9,961,935</td>
<td align="right">7,404,667</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">10,789,229</td>
<td align="right">8,077,110</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">10,789,229</td>
<td align="right">8,077,110</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,908,025</td>
<td align="right">2,298,066</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,833,838</td>
<td align="right">1,585,327</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">854,560</td>
<td align="right">738,947</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,056</td>
<td align="right">169,440</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">67,180</td>
<td align="right">62,260</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">189,120</td>
<td align="right">176,790</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">968,386</td>
<td align="right">920,874</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,317,420</td>
<td align="right">1,267,434</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">82,653</td>
<td align="right">80,273</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">5,760</td>
<td align="right">5,640</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,000</td>
<td align="right">39,680</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,000</td>
<td align="right">39,680</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">61,720</td>
<td align="right">61,600</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,680</td>
<td align="right">13,670</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">1,201,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">990,791</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">441,663</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">441,663</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">106,660</td>
<td align="right">106,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">39,280</td>
<td align="right">39,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">36,660</td>
<td align="right">36,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">11,040</td>
<td align="right">11,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">7,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">3,824</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">3,824</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">3,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">3,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">3,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">122,897,279</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">920</td>
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
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">560</td>
<td align="right">2,700.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">60</td>
<td align="right">900</td>
<td align="right">1,400.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">7,080</td>
<td align="right">34,904</td>
<td align="right">393.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,945</td>
<td align="right">13,255</td>
<td align="right">236.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">480</td>
<td align="right">328</td>
<td align="right">-31.7%</td>
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
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
