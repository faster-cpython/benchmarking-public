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
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">4,628</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">146,850</td>
<td align="right">83</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">98</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">196,240</td>
<td align="right">165</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,769</td>
<td align="right">847</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,468</td>
<td align="right">436</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,982</td>
<td align="right">374</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">192,012</td>
<td align="right">1,213</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">121</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,528,150</td>
<td align="right">412,418</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,545,861</td>
<td align="right">625,365</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,760</td>
<td align="right">21,723</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,430,835</td>
<td align="right">141,627</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,585</td>
<td align="right">10,811</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,359,765</td>
<td align="right">124,829</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,855</td>
<td align="right">3,578</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,579</td>
<td align="right">2,428,420</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">27,003,380</td>
<td align="right">2,902,391</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,044,798</td>
<td align="right">335,725</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,616</td>
<td align="right">126,302</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">87,429,968</td>
<td align="right">14,920,490</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,428</td>
<td align="right">538,366</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,874,836</td>
<td align="right">382,492</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,665,225</td>
<td align="right">763,116</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">1,833</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,706</td>
<td align="right">1,833</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,673,064</td>
<td align="right">356,656</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,327</td>
<td align="right">50,802</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,619,777</td>
<td align="right">2,045,860</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">3,727,080</td>
<td align="right">912,235</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,878</td>
<td align="right">19,924</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,943,043</td>
<td align="right">36,542,068</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,618,336</td>
<td align="right">1,528,604</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,460,941</td>
<td align="right">24,541,890</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">138,862,382</td>
<td align="right">42,599,395</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,082</td>
<td align="right">9,870</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">85,965,189</td>
<td align="right">26,740,663</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,521,072</td>
<td align="right">1,429,646</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">167,041,231</td>
<td align="right">54,058,323</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">3,517</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,480,751</td>
<td align="right">826,839</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,020,090</td>
<td align="right">724,898</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,285,249</td>
<td align="right">1,193,126</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,458,216</td>
<td align="right">2,407,208</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">152,617,549</td>
<td align="right">57,098,294</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,930,370</td>
<td align="right">1,102,469</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">767,074</td>
<td align="right">289,174</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">163,046,763</td>
<td align="right">61,798,357</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">36,377,084</td>
<td align="right">13,853,211</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,978</td>
<td align="right">9,976</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,069,631</td>
<td align="right">1,577,003</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">118,731,682</td>
<td align="right">46,793,728</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,689,915</td>
<td align="right">1,859,515</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,455</td>
<td align="right">8,515</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,590,344</td>
<td align="right">1,847,135</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">743,585</td>
<td align="right">299,418</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,324,100</td>
<td align="right">6,984,245</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,509,180</td>
<td align="right">5,065,786</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">44,396,613</td>
<td align="right">70,809,614</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,839,961</td>
<td align="right">30,283,276</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,443,808</td>
<td align="right">30,860,667</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,558,000</td>
<td align="right">2,296,969</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,335,699</td>
<td align="right">559,992</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,284,951</td>
<td align="right">958,244</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">55,140,845</td>
<td align="right">23,183,394</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,173,540</td>
<td align="right">4,711,364</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,098,056</td>
<td align="right">3,869,937</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,629</td>
<td align="right">469,374</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,007,169</td>
<td align="right">59,377,360</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,432,036</td>
<td align="right">4,132,906</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,468,855</td>
<td align="right">1,961,796</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,840,615</td>
<td align="right">4,391,687</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">892,856</td>
<td align="right">398,994</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,193,596</td>
<td align="right">8,135,334</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,515,772</td>
<td align="right">683,863</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,233,408</td>
<td align="right">6,482,756</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,931,439</td>
<td align="right">1,505,824</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,312,346</td>
<td align="right">675,463</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">266,452</td>
<td align="right">137,795</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,587</td>
<td align="right">674,714</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">640,544</td>
<td align="right">338,381</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,334,128</td>
<td align="right">730,805</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">34,176,755</td>
<td align="right">18,901,590</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">578,023,379</td>
<td align="right">319,797,850</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">414,880</td>
<td align="right">598,879</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,860,505</td>
<td align="right">6,125,151</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,953,174</td>
<td align="right">2,842,693</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,050,377</td>
<td align="right">5,800,387</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,106,789</td>
<td align="right">90,173,537</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,924,104</td>
<td align="right">5,796,102</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,219</td>
<td align="right">667,450</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,541,736</td>
<td align="right">31,153,351</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">126,112,663</td>
<td align="right">74,883,859</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">30,099,265</td>
<td align="right">18,210,971</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,274,503</td>
<td align="right">5,008,651</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,248,238</td>
<td align="right">759,116</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,859,608</td>
<td align="right">30,445,652</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,489,357</td>
<td align="right">13,146,343</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">152,862</td>
<td align="right">94,534</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,334</td>
<td align="right">933,425</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,298,779</td>
<td align="right">10,437,479</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,511,518</td>
<td align="right">969,826</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,500,874</td>
<td align="right">68,590,268</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">255,548</td>
<td align="right">167,218</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">712,414</td>
<td align="right">479,681</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,212</td>
<td align="right">6,211</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,577,095</td>
<td align="right">3,122,579</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,668,975</td>
<td align="right">12,550,665</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,431</td>
<td align="right">7,464</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,370,352</td>
<td align="right">3,171,908</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,001</td>
<td align="right">336,223</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,972,127</td>
<td align="right">7,271,162</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,929,348</td>
<td align="right">43,215,686</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,613</td>
<td align="right">17,407</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">110,133,175</td>
<td align="right">82,885,783</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,617,786</td>
<td align="right">5,018,974</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,192,761</td>
<td align="right">3,988,855</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">65,356</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">518,124</td>
<td align="right">619,392</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">211,118</td>
<td align="right">170,348</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">345,332</td>
<td align="right">278,698</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,488,727</td>
<td align="right">16,640,258</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">8,838,661</td>
<td align="right">7,214,002</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,139</td>
<td align="right">6,798</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">110,415,003</td>
<td align="right">93,478,952</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,109,666</td>
<td align="right">13,694,738</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,939,192</td>
<td align="right">14,491,775</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,829,184</td>
<td align="right">14,830,161</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,719,295</td>
<td align="right">3,333,538</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">44,242,536</td>
<td align="right">39,694,134</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,046,627</td>
<td align="right">9,031,077</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,522,459</td>
<td align="right">1,369,381</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,747</td>
<td align="right">6,619,773</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,941,901</td>
<td align="right">11,816,420</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,794,152</td>
<td align="right">1,639,721</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">84,302</td>
<td align="right">77,162</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,922</td>
<td align="right">15,619,768</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,723,407</td>
<td align="right">1,858,835</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,882,507</td>
<td align="right">2,666,419</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,395,633</td>
<td align="right">4,078,898</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,795</td>
<td align="right">5,640,681</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,272,411</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,405</td>
<td align="right">150,551</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,630</td>
<td align="right">2,818,815</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,855</td>
<td align="right">5,466,154</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,156</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,977</td>
<td align="right">21,639</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,797</td>
<td align="right">28,377</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,438</td>
<td align="right">558,894</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,085,417</td>
<td align="right">37,996,495</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,322</td>
<td align="right">38,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">53,270</td>
<td align="right">53,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,660,807</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,710</td>
<td align="right">2,973,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,792,095</td>
<td align="right">1,792,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,522,459</td>
<td align="right">1,522,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,256</td>
<td align="right">1,477,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,123</td>
<td align="right">129,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">24,139</td>
<td align="right">24,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,174</td>
<td align="right">23,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">13,810</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,078</td>
<td align="right">3,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,091</td>
<td align="right">2,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,344</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">346</td>
<td align="right">346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">289</td>
<td align="right">289</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">115</td>
<td align="right">115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">39</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">7</td>
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
<td align="right">9,088,160</td>
<td align="right">45.3%</td>
<td align="right">3,864,622</td>
<td align="right">26.2%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,976,335</td>
<td align="right">54.7%</td>
<td align="right">10,880,584</td>
<td align="right">73.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53</td>
<td align="right">0.0%</td>
<td align="right">53</td>
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
<td align="right">9,306</td>
<td align="right">94.0%</td>
<td align="right">4,726</td>
<td align="right">88.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">591</td>
<td align="right">6.0%</td>
<td align="right">590</td>
<td align="right">11.1%</td>
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
<td align="left">and different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">117</td>
<td align="right">1.3%</td>
<td align="right">35</td>
<td align="right">0.7%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">36.6%</td>
<td align="right">1,461</td>
<td align="right">30.9%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,017</td>
<td align="right">10.9%</td>
<td align="right">453</td>
<td align="right">9.6%</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">16.0%</td>
<td align="right">666</td>
<td align="right">14.1%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,349</td>
<td align="right">25.2%</td>
<td align="right">1,326</td>
<td align="right">28.1%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.5%</td>
<td align="right">148</td>
<td align="right">3.1%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">272</td>
<td align="right">2.9%</td>
<td align="right">223</td>
<td align="right">4.7%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">230</td>
<td align="right">2.5%</td>
<td align="right">215</td>
<td align="right">4.5%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">46</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">16</td>
<td align="right">0.2%</td>
<td align="right">16</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">2,732,428</td>
<td align="right">100.0%</td>
<td align="right">538,366</td>
<td align="right">100.0%</td>
<td align="right">-80.3%</td>
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
<td align="right">3,712,429</td>
<td align="right">9.6%</td>
<td align="right">3,327,929</td>
<td align="right">8.7%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,467,009</td>
<td align="right">84.2%</td>
<td align="right">32,460,415</td>
<td align="right">85.1%</td>
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
<td align="right">2,366,706</td>
<td align="right">6.1%</td>
<td align="right">2,366,643</td>
<td align="right">6.2%</td>
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
<td align="right">5,633</td>
<td align="right">11.0%</td>
<td align="right">4,454</td>
<td align="right">8.9%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,741</td>
<td align="right">89.0%</td>
<td align="right">45,663</td>
<td align="right">91.1%</td>
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
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.5%</td>
<td align="right">150</td>
<td align="right">3.4%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,252</td>
<td align="right">22.2%</td>
<td align="right">718</td>
<td align="right">16.1%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.2%</td>
<td align="right">145</td>
<td align="right">3.3%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.3%</td>
<td align="right">204</td>
<td align="right">4.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">844</td>
<td align="right">15.0%</td>
<td align="right">715</td>
<td align="right">16.1%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">92</td>
<td align="right">1.6%</td>
<td align="right">103</td>
<td align="right">2.3%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,655</td>
<td align="right">47.1%</td>
<td align="right">2,419</td>
<td align="right">54.3%</td>
<td align="right">-8.9%</td>
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
<td align="right">1,880,294</td>
<td align="right">0.8%</td>
<td align="right">1,465,202</td>
<td align="right">0.6%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">239,318,085</td>
<td align="right">99.2%</td>
<td align="right">239,765,421</td>
<td align="right">99.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,174</td>
<td align="right">0.0%</td>
<td align="right">14,177</td>
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
<td align="right">59,426</td>
<td align="right">100.0%</td>
<td align="right">51,582</td>
<td align="right">100.0%</td>
<td align="right">-13.2%</td>
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
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
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
<td align="right">336</td>
<td align="right">15.6%</td>
<td align="right">336</td>
<td align="right">15.6%</td>
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
<td align="right">64</td>
<td align="right">3.0%</td>
<td align="right">64</td>
<td align="right">3.0%</td>
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
<td align="right">1,755</td>
<td align="right">100.0%</td>
<td align="right">1,755</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,051</td>
<td align="right">0.1%</td>
<td align="right">3,976</td>
<td align="right">0.0%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">636,669</td>
<td align="right">5.5%</td>
<td align="right">335,403</td>
<td align="right">3.0%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,925,975</td>
<td align="right">94.4%</td>
<td align="right">10,920,458</td>
<td align="right">97.0%</td>
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
<td align="right">2,655</td>
<td align="right">66.3%</td>
<td align="right">1,754</td>
<td align="right">57.6%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,351</td>
<td align="right">33.7%</td>
<td align="right">1,292</td>
<td align="right">42.4%</td>
<td align="right">-4.4%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">258</td>
<td align="right">9.7%</td>
<td align="right">83</td>
<td align="right">4.7%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">92</td>
<td align="right">3.5%</td>
<td align="right">42</td>
<td align="right">2.4%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,803</td>
<td align="right">67.9%</td>
<td align="right">1,185</td>
<td align="right">67.6%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">256</td>
<td align="right">9.6%</td>
<td align="right">214</td>
<td align="right">12.2%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">160</td>
<td align="right">9.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">43</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">4,364,805</td>
<td align="right">27.1%</td>
<td align="right">3,168,257</td>
<td align="right">21.3%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,734,400</td>
<td align="right">72.9%</td>
<td align="right">11,712,448</td>
<td align="right">78.7%</td>
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
<td align="right">5,019</td>
<td align="right">90.5%</td>
<td align="right">3,145</td>
<td align="right">86.1%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">528</td>
<td align="right">9.5%</td>
<td align="right">506</td>
<td align="right">13.9%</td>
<td align="right">-4.2%</td>
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
<td align="right">622</td>
<td align="right">12.4%</td>
<td align="right">193</td>
<td align="right">6.1%</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">733</td>
<td align="right">14.6%</td>
<td align="right">342</td>
<td align="right">10.9%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,172</td>
<td align="right">43.3%</td>
<td align="right">1,432</td>
<td align="right">45.5%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,492</td>
<td align="right">29.7%</td>
<td align="right">1,178</td>
<td align="right">37.5%</td>
<td align="right">-21.0%</td>
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
<td align="right">4,650,521</td>
<td align="right">4.4%</td>
<td align="right">18,166,077</td>
<td align="right">14.9%</td>
<td align="right">290.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,834,453</td>
<td align="right">9.3%</td>
<td align="right">4,387,643</td>
<td align="right">3.6%</td>
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
<td align="right">91,784,770</td>
<td align="right">86.4%</td>
<td align="right">99,215,538</td>
<td align="right">81.5%</td>
<td align="right">8.1%</td>
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
<td align="right">88,387</td>
<td align="right">94.1%</td>
<td align="right">343,375</td>
<td align="right">99.0%</td>
<td align="right">288.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,526</td>
<td align="right">5.9%</td>
<td align="right">3,407</td>
<td align="right">1.0%</td>
<td align="right">-38.3%</td>
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
<td align="right">465</td>
<td align="right">8.4%</td>
<td align="right">143</td>
<td align="right">4.2%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.4%</td>
<td align="right">119</td>
<td align="right">3.5%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">710</td>
<td align="right">12.8%</td>
<td align="right">300</td>
<td align="right">8.8%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">234</td>
<td align="right">4.2%</td>
<td align="right">104</td>
<td align="right">3.1%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,251</td>
<td align="right">22.6%</td>
<td align="right">708</td>
<td align="right">20.8%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.5%</td>
<td align="right">340</td>
<td align="right">10.0%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,569</td>
<td align="right">28.4%</td>
<td align="right">1,216</td>
<td align="right">35.7%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">272</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.8%</td>
<td align="right">97</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.1%</td>
<td align="right">61</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">47</td>
<td align="right">0.9%</td>
<td align="right">47</td>
<td align="right">1.4%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,389</td>
<td align="right">0.0%</td>
<td align="right">30,456</td>
<td align="right">0.0%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">77,608,580</td>
<td align="right">24.8%</td>
<td align="right">96,279,302</td>
<td align="right">27.7%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">191,242,535</td>
<td align="right">61.1%</td>
<td align="right">211,415,993</td>
<td align="right">60.9%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">43,802,591</td>
<td align="right">14.0%</td>
<td align="right">39,186,555</td>
<td align="right">11.3%</td>
<td align="right">-10.5%</td>
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
<td align="right">55,663</td>
<td align="right">3.7%</td>
<td align="right">177,165</td>
<td align="right">8.9%</td>
<td align="right">218.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,453,070</td>
<td align="right">96.3%</td>
<td align="right">1,805,694</td>
<td align="right">91.1%</td>
<td align="right">24.3%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">67</td>
<td align="right">0.1%</td>
<td align="right">25</td>
<td align="right">0.0%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,294</td>
<td align="right">2.3%</td>
<td align="right">639</td>
<td align="right">0.4%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">113</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,203</td>
<td align="right">5.8%</td>
<td align="right">2,360</td>
<td align="right">1.3%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,856</td>
<td align="right">5.1%</td>
<td align="right">2,290</td>
<td align="right">1.3%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">1.8%</td>
<td align="right">925</td>
<td align="right">0.5%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">640</td>
<td align="right">1.1%</td>
<td align="right">640</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">279</td>
<td align="right">0.5%</td>
<td align="right">279</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,096</td>
<td align="right">0.0%</td>
<td align="right">11,264</td>
<td align="right">0.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">209,835,034</td>
<td align="right">100.0%</td>
<td align="right">211,971,728</td>
<td align="right">100.0%</td>
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
<td align="right">3,005</td>
<td align="right">0.0%</td>
<td align="right">2,994</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">57</td>
<td align="right">0.0%</td>
<td align="right">57</td>
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
<td align="right">19,397</td>
<td align="right">100.0%</td>
<td align="right">19,069</td>
<td align="right">100.0%</td>
<td align="right">-1.7%</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">18,086,397</td>
<td align="right">67.2%</td>
<td align="right">41,413,730</td>
<td align="right">85.2%</td>
<td align="right">129.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,814,795</td>
<td align="right">32.7%</td>
<td align="right">7,191,618</td>
<td align="right">14.8%</td>
<td align="right">-18.4%</td>
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
<td align="right">355,380</td>
<td align="right">98.6%</td>
<td align="right">795,428</td>
<td align="right">99.5%</td>
<td align="right">123.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,160</td>
<td align="right">1.4%</td>
<td align="right">3,995</td>
<td align="right">0.5%</td>
<td align="right">-22.6%</td>
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
<td align="right">3,984</td>
<td align="right">77.2%</td>
<td align="right">2,884</td>
<td align="right">72.2%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">kind 18</td>
<td align="right">636</td>
<td align="right">12.3%</td>
<td align="right">767</td>
<td align="right">19.2%</td>
<td align="right">20.6%</td>
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
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">424,857</td>
<td align="right">100.0%</td>
<td align="right">424,857</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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

### LOAD_SUPER_METHOD

<details>
<summary> specialization stats for LOAD_SUPER_METHOD family </summary>

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
<td align="right">41</td>
<td align="right">18.6%</td>
<td align="right">41</td>
<td align="right">18.6%</td>
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
<td align="right">179</td>
<td align="right">100.0%</td>
<td align="right">179</td>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
<td align="right">4,490</td>
<td align="right">29.2%</td>
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
<td align="right">10,810</td>
<td align="right">70.4%</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
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
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
<td align="right">47</td>
<td align="right">92.2%</td>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">47</td>
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
<td align="right">10,035,417</td>
<td align="right">29.8%</td>
<td align="right">5,789,516</td>
<td align="right">20.7%</td>
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
<td align="right">9,609,951</td>
<td align="right">28.5%</td>
<td align="right">7,909,029</td>
<td align="right">28.3%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,054,795</td>
<td align="right">41.7%</td>
<td align="right">14,223,825</td>
<td align="right">50.9%</td>
<td align="right">1.2%</td>
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
<td align="right">9,812</td>
<td align="right">5.0%</td>
<td align="right">5,732</td>
<td align="right">3.6%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">185,985</td>
<td align="right">95.0%</td>
<td align="right">154,262</td>
<td align="right">96.4%</td>
<td align="right">-17.1%</td>
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
<td align="right">46,208</td>
<td align="right">470.9%</td>
<td align="right">169,924</td>
<td align="right">2,964.5%</td>
<td align="right">267.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">122</td>
<td align="right">1.2%</td>
<td align="right">31</td>
<td align="right">0.5%</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">5,037</td>
<td align="right">51.3%</td>
<td align="right">2,579</td>
<td align="right">45.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">51</td>
<td align="right">0.9%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.8%</td>
<td align="right">1,450</td>
<td align="right">25.3%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.6%</td>
<td align="right">401</td>
<td align="right">7.0%</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">12</td>
<td align="right">0.2%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">311</td>
<td align="right">3.2%</td>
<td align="right">227</td>
<td align="right">4.0%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">287</td>
<td align="right">2.9%</td>
<td align="right">292</td>
<td align="right">5.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">196,240</td>
<td align="right">100.0%</td>
<td align="right">165</td>
<td align="right">100.0%</td>
<td align="right">-99.9%</td>
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
<td align="right">1,486,386</td>
<td align="right">14.0%</td>
<td align="right">931,017</td>
<td align="right">9.2%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,355</td>
<td align="right">86.0%</td>
<td align="right">9,139,207</td>
<td align="right">90.7%</td>
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
<td align="right">3,474</td>
<td align="right">88.0%</td>
<td align="right">1,978</td>
<td align="right">82.1%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">430</td>
<td align="right">17.9%</td>
<td align="right">-9.3%</td>
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
<td align="right">13</td>
<td align="right">0.4%</td>
<td align="right">57</td>
<td align="right">2.9%</td>
<td align="right">338.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,960</td>
<td align="right">85.2%</td>
<td align="right">1,465</td>
<td align="right">74.1%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">296</td>
<td align="right">15.0%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">113</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">47</td>
<td align="right">2.4%</td>
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
<td align="right">14,083,135</td>
<td align="right">7.5%</td>
<td align="right">6,334,954</td>
<td align="right">3.5%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,385,976</td>
<td align="right">2.9%</td>
<td align="right">4,769,274</td>
<td align="right">2.6%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,733,970</td>
<td align="right">89.6%</td>
<td align="right">169,339,883</td>
<td align="right">93.8%</td>
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
<td align="right">105,551</td>
<td align="right">41.9%</td>
<td align="right">93,849</td>
<td align="right">39.5%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146,282</td>
<td align="right">58.1%</td>
<td align="right">143,996</td>
<td align="right">60.5%</td>
<td align="right">-1.6%</td>
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
<td align="right">192</td>
<td align="right">0.1%</td>
<td align="right">421</td>
<td align="right">0.3%</td>
<td align="right">119.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">532</td>
<td align="right">0.4%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,948</td>
<td align="right">6.8%</td>
<td align="right">7,897</td>
<td align="right">5.5%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">905</td>
<td align="right">0.6%</td>
<td align="right">749</td>
<td align="right">0.5%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">132,933</td>
<td align="right">90.9%</td>
<td align="right">134,174</td>
<td align="right">93.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">116</td>
<td align="right">0.1%</td>
<td align="right">116</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">107</td>
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
<td align="right">296,270</td>
<td align="right">2.0%</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,605,541</td>
<td align="right">98.0%</td>
<td align="right">14,596,642</td>
<td align="right">100.0%</td>
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
<td align="right">97</td>
<td align="right">19.4%</td>
<td align="right">26</td>
<td align="right">6.4%</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">402</td>
<td align="right">80.6%</td>
<td align="right">381</td>
<td align="right">93.6%</td>
<td align="right">-5.2%</td>
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
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">3</td>
<td align="right">11.5%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">88.5%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,015,094,349</td>
<td align="right">57.2%</td>
<td align="right">947,212,824</td>
<td align="right">50.8%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,277,613,824</td>
<td align="right">36.3%</td>
<td align="right">669,399,292</td>
<td align="right">35.9%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">119,611,728</td>
<td align="right">3.4%</td>
<td align="right">172,386,874</td>
<td align="right">9.2%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">109,816,805</td>
<td align="right">3.1%</td>
<td align="right">75,836,392</td>
<td align="right">4.1%</td>
<td align="right">-30.9%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,428</td>
<td align="right">2.5%</td>
<td align="right">538,366</td>
<td align="right">0.7%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,088,160</td>
<td align="right">8.3%</td>
<td align="right">3,864,622</td>
<td align="right">5.1%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,834,453</td>
<td align="right">9.0%</td>
<td align="right">4,387,643</td>
<td align="right">5.8%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,083,135</td>
<td align="right">12.9%</td>
<td align="right">6,334,954</td>
<td align="right">8.4%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,035,417</td>
<td align="right">9.2%</td>
<td align="right">5,789,516</td>
<td align="right">7.7%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,386</td>
<td align="right">1.4%</td>
<td align="right">931,017</td>
<td align="right">1.2%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,364,805</td>
<td align="right">4.0%</td>
<td align="right">3,168,257</td>
<td align="right">4.2%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">8,814,795</td>
<td align="right">8.1%</td>
<td align="right">7,191,618</td>
<td align="right">9.6%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">43,802,591</td>
<td align="right">40.1%</td>
<td align="right">39,186,555</td>
<td align="right">52.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,712,429</td>
<td align="right">3.4%</td>
<td align="right">3,327,929</td>
<td align="right">4.4%</td>
<td align="right">-10.4%</td>
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
<td align="right">2,325,048</td>
<td align="right">1.9%</td>
<td align="right">9,082,639</td>
<td align="right">5.3%</td>
<td align="right">290.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,325,473</td>
<td align="right">1.9%</td>
<td align="right">9,083,438</td>
<td align="right">5.3%</td>
<td align="right">290.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">17,912,498</td>
<td align="right">15.0%</td>
<td align="right">41,217,120</td>
<td align="right">23.9%</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,559,448</td>
<td align="right">12.2%</td>
<td align="right">23,426,692</td>
<td align="right">13.6%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,401,538</td>
<td align="right">37.1%</td>
<td align="right">53,818,332</td>
<td align="right">31.2%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">8.0%</td>
<td align="right">7,871,867</td>
<td align="right">4.6%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,392,276</td>
<td align="right">3.7%</td>
<td align="right">4,109,853</td>
<td align="right">2.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,809</td>
<td align="right">6.4%</td>
<td align="right">7,379,798</td>
<td align="right">4.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,358,933</td>
<td align="right">8.7%</td>
<td align="right">10,258,721</td>
<td align="right">6.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,342,047</td>
<td align="right">2.0%</td>
<td align="right">2,341,984</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">628,884</td>
<td align="right">0.3%</td>
<td align="right">597,906</td>
<td align="right">0.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,690,748</td>
<td align="right">3.1%</td>
<td align="right">6,610,484</td>
<td align="right">3.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,558,143</td>
<td align="right">8.5%</td>
<td align="right">18,459,859</td>
<td align="right">8.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,250,423</td>
<td align="right">18.4%</td>
<td align="right">40,120,731</td>
<td align="right">18.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,250,423</td>
<td align="right">18.4%</td>
<td align="right">40,120,731</td>
<td align="right">18.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,619,818</td>
<td align="right">18.1%</td>
<td align="right">39,521,104</td>
<td align="right">18.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,621,539</td>
<td align="right">18.1%</td>
<td align="right">39,522,825</td>
<td align="right">18.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,914,322</td>
<td align="right">81.6%</td>
<td align="right">179,003,244</td>
<td align="right">81.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,484,683</td>
<td align="right">4.8%</td>
<td align="right">10,488,709</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,060,494</td>
<td align="right">72.1%</td>
<td align="right">158,064,950</td>
<td align="right">72.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">377</td>
<td align="right">0.0%</td>
<td align="right">377</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,496</td>
<td align="right">0.2%</td>
<td align="right">502,496</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">88</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,369,716,591</td>
<td align="right">36.3%</td>
<td align="right">901,442,011</td>
<td align="right">25.2%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546,542,387</td>
<td align="right">13.1%</td>
<td align="right">378,199,755</td>
<td align="right">9.7%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">391,101,728</td>
<td align="right">10.4%</td>
<td align="right">286,801,403</td>
<td align="right">8.0%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,773,101,594</td>
<td align="right">42.6%</td>
<td align="right">1,345,455,594</td>
<td align="right">34.7%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,284,840,707</td>
<td align="right">34.0%</td>
<td align="right">1,570,053,930</td>
<td align="right">43.8%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,133,030,694</td>
<td align="right">27.2%</td>
<td align="right">1,377,362,546</td>
<td align="right">35.5%</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">729,928,562</td>
<td align="right">19.3%</td>
<td align="right">823,493,758</td>
<td align="right">23.0%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,118</td>
<td align="right">0.0%</td>
<td align="right">68,779</td>
<td align="right">0.0%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">711,818,972</td>
<td align="right">17.1%</td>
<td align="right">779,768,852</td>
<td align="right">20.1%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">217,351,729</td>
<td align="right"></td>
<td align="right">198,854,032</td>
<td align="right"></td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,012,284</td>
<td align="right"></td>
<td align="right">3,222,242</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,280,879</td>
<td align="right"></td>
<td align="right">9,154,105</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">12,290,983</td>
<td align="right"></td>
<td align="right">12,374,459</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">160,709,370</td>
<td align="right"></td>
<td align="right">160,184,970</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,426,768</td>
<td align="right">0.5%</td>
<td align="right">1,425,341</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">203,988,927</td>
<td align="right"></td>
<td align="right">203,816,349</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">191,606,443</td>
<td align="right">67.3%</td>
<td align="right">191,474,869</td>
<td align="right">67.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">193,095,329</td>
<td align="right">67.9%</td>
<td align="right">192,968,989</td>
<td align="right">67.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">91,369,257</td>
<td align="right"></td>
<td align="right">91,347,197</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">91,409,482</td>
<td align="right">32.1%</td>
<td align="right">91,388,866</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,685</td>
<td align="right"></td>
<td align="right">3,079,685</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
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
<td align="right">6,261</td>
<td align="right">13,132,357</td>
<td align="right">262,308,991</td>
<td align="right">16,211,323</td>
<td align="right">23,995,700</td>
<td align="right">6,323</td>
<td align="right">13,098,422</td>
<td align="right">257,220,898</td>
<td align="right">16,285,127</td>
<td align="right">23,919,053</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,130,465,775</td>
<td align="right">919.4%</td>
<td align="right">5,694,421,891</td>
<td align="right">1,706.1%</td>
<td align="right">167.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,648</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,923</td>
<td align="right">38.7%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,258</td>
<td align="right">63.4%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">15,725</td>
<td align="right">61.3%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">22</td>
<td align="right">0.1%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">231,728,475</td>
<td align="right"></td>
<td align="right">333,762,577</td>
<td align="right"></td>
<td align="right">44.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">9,923</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">9,882</td>
<td align="right">99.6%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">452</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,068</td>
<td align="right">20.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,795</td>
<td align="right">48.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,334</td>
<td align="right">23.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">274</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,968</td>
<td align="right">19.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,404</td>
<td align="right">14.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,168</td>
<td align="right">52.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,216</td>
<td align="right">12.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">126</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">42</td>
<td align="right">2,814,486</td>
<td align="right">6,701,057.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">44</td>
<td align="right">1,449,338</td>
<td align="right">3,293,850.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">21</td>
<td align="right">605,894</td>
<td align="right">2,885,109.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">21</td>
<td align="right">596,134</td>
<td align="right">2,838,633.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">243</td>
<td align="right">1,298,973</td>
<td align="right">534,456.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">243</td>
<td align="right">1,291,409</td>
<td align="right">531,344.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">44</td>
<td align="right">185,567</td>
<td align="right">421,643.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,932</td>
<td align="right">2,927,844</td>
<td align="right">151,444.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,715</td>
<td align="right">5,325,094</td>
<td align="right">93,077.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,545</td>
<td align="right">2,114,026</td>
<td align="right">59,534.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">139</td>
<td align="right">68,294</td>
<td align="right">49,032.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,123</td>
<td align="right">2,818,572</td>
<td align="right">45,932.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,123</td>
<td align="right">2,818,572</td>
<td align="right">45,932.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,553,525</td>
<td align="right">502,093,561</td>
<td align="right">19,562.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,236</td>
<td align="right">3,110,662</td>
<td align="right">16,071.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,029</td>
<td align="right">154,820</td>
<td align="right">14,945.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">7,879</td>
<td align="right">1,133,360</td>
<td align="right">14,284.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,675</td>
<td align="right">481,662</td>
<td align="right">13,006.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">32,411</td>
<td align="right">2,316,787</td>
<td align="right">7,048.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,773</td>
<td align="right">1,471,863</td>
<td align="right">6,985.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,069,547</td>
<td align="right">60,294,073</td>
<td align="right">5,537.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">102,057</td>
<td align="right">5,220,367</td>
<td align="right">5,015.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,965,428</td>
<td align="right">98,223,406</td>
<td align="right">4,897.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,557,263</td>
<td align="right">115,188,157</td>
<td align="right">4,404.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">95,467</td>
<td align="right">4,146,475</td>
<td align="right">4,243.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,272,154</td>
<td align="right">97,791,499</td>
<td align="right">4,203.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,822,378</td>
<td align="right">116,851,472</td>
<td align="right">4,040.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">54,953</td>
<td align="right">2,249,015</td>
<td align="right">3,992.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">140,066</td>
<td align="right">5,034,823</td>
<td align="right">3,494.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">190,495</td>
<td align="right">6,054,210</td>
<td align="right">3,078.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">20,958</td>
<td align="right">633,073</td>
<td align="right">2,920.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">263,521</td>
<td align="right">7,205,912</td>
<td align="right">2,634.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,236</td>
<td align="right">508,358</td>
<td align="right">2,542.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">217,035</td>
<td align="right">5,534,903</td>
<td align="right">2,450.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">119,867</td>
<td align="right">2,997,784</td>
<td align="right">2,400.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">140,287</td>
<td align="right">3,399,918</td>
<td align="right">2,323.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">153,121</td>
<td align="right">3,401,825</td>
<td align="right">2,121.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60,061</td>
<td align="right">1,294,997</td>
<td align="right">2,056.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">68,516</td>
<td align="right">1,381,532</td>
<td align="right">1,916.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">655,067</td>
<td align="right">11,883,167</td>
<td align="right">1,714.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">655,067</td>
<td align="right">10,993,887</td>
<td align="right">1,578.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">179,525</td>
<td align="right">2,994,974</td>
<td align="right">1,568.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">16,317</td>
<td align="right">249,050</td>
<td align="right">1,426.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">572,216</td>
<td align="right">8,462,317</td>
<td align="right">1,378.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">194,323</td>
<td align="right">2,599,849</td>
<td align="right">1,237.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">129,682</td>
<td align="right">1,728,494</td>
<td align="right">1,232.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,512,448</td>
<td align="right">30,811,275</td>
<td align="right">1,126.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,517,203</td>
<td align="right">30,811,590</td>
<td align="right">1,124.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">110,541</td>
<td align="right">1,329,041</td>
<td align="right">1,102.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">163,464</td>
<td align="right">1,804,405</td>
<td align="right">1,003.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,877,092</td>
<td align="right">29,526,899</td>
<td align="right">926.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">974,422</td>
<td align="right">8,561,033</td>
<td align="right">778.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">399,356</td>
<td align="right">3,221,564</td>
<td align="right">706.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,029</td>
<td align="right">8,169</td>
<td align="right">693.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">145,014</td>
<td align="right">653.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">145,014</td>
<td align="right">653.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">449,267</td>
<td align="right">3,351,376</td>
<td align="right">646.0%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">3,570,434</td>
<td align="right">26,036,008</td>
<td align="right">629.2%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,007,196</td>
<td align="right">7,112,395</td>
<td align="right">606.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">346,254</td>
<td align="right">2,174,155</td>
<td align="right">527.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,149,820</td>
<td align="right">5,277,822</td>
<td align="right">359.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,580</td>
<td align="right">752,097</td>
<td align="right">318.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">15,473,163</td>
<td align="right">60,383,867</td>
<td align="right">290.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">56,735,096</td>
<td align="right">218,585,488</td>
<td align="right">285.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,371,585</td>
<td align="right">8,936,603</td>
<td align="right">276.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">740,499</td>
<td align="right">2,739,452</td>
<td align="right">269.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">470,964</td>
<td align="right">1,703,733</td>
<td align="right">261.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">925,689</td>
<td align="right">3,215,656</td>
<td align="right">247.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">164,276,176</td>
<td align="right">559,601,825</td>
<td align="right">240.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">45,103,815</td>
<td align="right">148,997,191</td>
<td align="right">230.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">656,173</td>
<td align="right">2,148,517</td>
<td align="right">227.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">185,093</td>
<td align="right">576,250</td>
<td align="right">211.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,063,745</td>
<td align="right">6,153,477</td>
<td align="right">198.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">319,648</td>
<td align="right">861,340</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">319,648</td>
<td align="right">861,340</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,761,228</td>
<td align="right">9,233,763</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">77,650,581</td>
<td align="right">180,212,154</td>
<td align="right">132.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">247,883</td>
<td align="right">564,618</td>
<td align="right">127.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">247,883</td>
<td align="right">564,618</td>
<td align="right">127.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,836,075</td>
<td align="right">9,770,410</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">984,632</td>
<td align="right">1,978,999</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">184,064</td>
<td align="right">65</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">217,781,163</td>
<td align="right">434,560,208</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">32,789,008</td>
<td align="right">2,392,628</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">316,918</td>
<td align="right">606,596</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,331,362</td>
<td align="right">10,006,780</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,964,355</td>
<td align="right">9,107,001</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">49,469,977</td>
<td align="right">88,305,129</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">30,796,402</td>
<td align="right">6,666,920</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">49,469,977</td>
<td align="right">15,988,028</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,165,522</td>
<td align="right">1,533,744</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">70,923,344</td>
<td align="right">114,028,744</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">185,017</td>
<td align="right">82,980</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">30,986,101</td>
<td align="right">46,699,763</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">21,225,089</td>
<td align="right">11,267,442</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,558,193</td>
<td align="right">18,170,291</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">33,358,830</td>
<td align="right">18,170,291</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">21,749,145</td>
<td align="right">12,598,034</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">69,972,064</td>
<td align="right">43,134,309</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">35,765,827</td>
<td align="right">23,002,776</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">647,258</td>
<td align="right">863,346</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">178,092,837</td>
<td align="right">119,552,811</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">33,996,571</td>
<td align="right">26,128,782</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">33,549,325</td>
<td align="right">26,059,392</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,435,416</td>
<td align="right">43,134,309</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">236,448,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">231,728,475</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">35,436,162</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">34,896,589</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">33,782,125</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">33,474,084</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">32,321,683</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,550,237</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,220,915</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,683,374</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,329,825</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,719,925</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,812,537</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,673,487</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,944,216</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,764,257</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,207,424</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,052,705</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,031,170</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,285,830</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,175,425</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,119,537</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">948,669</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">824,201</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">715,024</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">327,982</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">322,605</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">317,391</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">283,410</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">199,363</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">57,444</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">25,636</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,675</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">3,675</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,029</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">1,143,684,094</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">125,534,313</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">92,525,383</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">83,761,801</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">77,836,435</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">77,832,816</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">77,822,261</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">64,937,708</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">61,028,798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">44,518,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">44,500,095</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">39,115,732</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">38,859,859</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">24,697,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">24,684,843</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">20,249,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">18,168,728</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">16,070,267</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">12,544,958</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">8,905,904</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">8,539,987</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">6,813,455</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">6,813,455</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">5,746,079</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">2,507,059</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">2,447,417</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">1,341,545</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">831,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">825,343</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">707,123</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">692,250</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">692,250</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">688,974</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">622,255</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">531,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">493,778</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">480,037</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">465,769</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">444,167</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">310,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">308,114</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">304,729</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">291,908</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">216,701</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">196,075</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">190,799</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">190,799</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">153,078</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">152,596</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">146,734</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">146,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">146,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">138,774</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right"></td>
<td align="right">128,657</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">122,815</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">116,958</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">88,330</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">76,608</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">67,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">66,634</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">59,954</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">58,328</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">32,277</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">22,212</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">19,058</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">16,263</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">16,002</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">12,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">7,854</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">7,293</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">6,873</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">6,873</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">6,206</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">2,967</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">1,341</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">84</td>
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
<td align="right">191</td>
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
<td align="right">22,592</td>
<td align="right">22,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">22</td>
<td align="right">22</td>
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
<td align="right">23</td>
<td align="right">23</td>
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
Stats gathered on: 2025-01-27
