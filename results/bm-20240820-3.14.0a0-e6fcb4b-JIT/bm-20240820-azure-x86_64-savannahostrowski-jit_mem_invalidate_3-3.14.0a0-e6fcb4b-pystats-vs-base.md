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
<td align="right">2,909,462</td>
<td align="right">678,930,345</td>
<td align="right">23,235.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">183,125,612</td>
<td align="right">780,735,750</td>
<td align="right">326.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">549,250</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">200,095,054</td>
<td align="right">551,865,820</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">272,019,897</td>
<td align="right">472,716,714</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,655,280</td>
<td align="right">826,357,166</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">615,786,142</td>
<td align="right">1,020,051,862</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">722,472,588</td>
<td align="right">1,125,326,973</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,537,983</td>
<td align="right">11,248,983</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,733,827,432</td>
<td align="right">6,198,804,849</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">653,029,424</td>
<td align="right">854,531,244</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">701,218,455</td>
<td align="right">903,367,225</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">815,652,763</td>
<td align="right">1,017,173,668</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">49,557,480</td>
<td align="right">60,706,911</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,095,714</td>
<td align="right">40,518,228</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,633,791</td>
<td align="right">130,818,837</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">43,000,542</td>
<td align="right">50,914,516</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,849,720,986</td>
<td align="right">2,170,403,550</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,813,638,313</td>
<td align="right">2,426,630,857</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,999,788,838</td>
<td align="right">5,584,890,673</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,459,180</td>
<td align="right">168,169,114</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,668,303,672</td>
<td align="right">17,724,764,885</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">824,988,488</td>
<td align="right">871,334,367</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,299,732</td>
<td align="right">85,138,066</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,211,795,242</td>
<td align="right">1,266,246,248</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,626,205</td>
<td align="right">36,178,858</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">337,331,987</td>
<td align="right">352,423,366</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">673,020,400</td>
<td align="right">700,367,576</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">188,157,355</td>
<td align="right">195,701,176</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">352,854,405</td>
<td align="right">365,434,045</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,322,291</td>
<td align="right">48,945,479</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,683,284</td>
<td align="right">3,557,356</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">217,872,327</td>
<td align="right">225,244,859</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,583,465,046</td>
<td align="right">2,663,358,226</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,104,889</td>
<td align="right">106,203,349</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">759,398,097</td>
<td align="right">782,004,146</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,798,587</td>
<td align="right">20,358,719</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,114,160,401</td>
<td align="right">2,167,519,064</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,745</td>
<td align="right">94,138,301</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">536,292,465</td>
<td align="right">548,516,439</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">459,640,765</td>
<td align="right">469,122,585</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">166,159,989</td>
<td align="right">169,283,210</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,011,843</td>
<td align="right">125,072,743</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,152,214</td>
<td align="right">199,411,558</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,611,430</td>
<td align="right">54,478,224</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">226,513,310</td>
<td align="right">230,152,855</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">384,699,700</td>
<td align="right">390,863,223</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">988,954,246</td>
<td align="right">1,004,035,211</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">318,781,106</td>
<td align="right">323,568,706</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,418,362</td>
<td align="right">1,438,929</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,175,638</td>
<td align="right">125,881,504</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">894,827,921</td>
<td align="right">906,487,558</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,070,303,787</td>
<td align="right">4,121,529,535</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,582,949</td>
<td align="right">140,254,729</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">89,541,404</td>
<td align="right">90,537,783</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,087,538</td>
<td align="right">137,582,638</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,974,554</td>
<td align="right">223,358,734</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">190,044,005</td>
<td align="right">192,084,692</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,115,409</td>
<td align="right">144,620,029</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,916,962,624</td>
<td align="right">4,967,961,352</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,900,627,023</td>
<td align="right">2,929,860,279</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,763,239</td>
<td align="right">202,773,329</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">537,575,277</td>
<td align="right">542,955,678</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,399,826,873</td>
<td align="right">2,423,580,381</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">234,813,526</td>
<td align="right">237,062,202</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">762,767,785</td>
<td align="right">769,628,373</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,817,128</td>
<td align="right">135,010,189</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,050,474,973</td>
<td align="right">1,059,491,931</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,163,061</td>
<td align="right">53,610,359</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,730,793</td>
<td align="right">72,326,253</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,194,644</td>
<td align="right">118,112,864</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">271,432,063</td>
<td align="right">273,438,680</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">93,244,615</td>
<td align="right">93,927,099</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,110,476</td>
<td align="right">326,442,556</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,785,019</td>
<td align="right">9,855,347</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">395,237,789</td>
<td align="right">397,978,801</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,755,659,301</td>
<td align="right">2,774,127,478</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">365,476,410</td>
<td align="right">367,888,299</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">714,366,374</td>
<td align="right">718,783,934</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,728</td>
<td align="right">3,565,244</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,977,389,991</td>
<td align="right">4,001,115,004</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,828,927</td>
<td align="right">53,142,639</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">53,672,758</td>
<td align="right">53,360,199</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,990,635</td>
<td align="right">104,591,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">57,073,569</td>
<td align="right">57,398,768</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,266,477</td>
<td align="right">33,438,873</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,767,379,646</td>
<td align="right">3,786,439,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">492,950,412</td>
<td align="right">495,423,934</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,745,930</td>
<td align="right">48,980,989</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">473,374,602</td>
<td align="right">475,402,770</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,948,114</td>
<td align="right">71,243,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,562,273</td>
<td align="right">37,717,862</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,542,233</td>
<td align="right">8,576,791</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,226,283</td>
<td align="right">58,453,141</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,953,154</td>
<td align="right">14,896,566</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,421,572</td>
<td align="right">299,544,270</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,035,022</td>
<td align="right">83,337,524</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,291,616</td>
<td align="right">16,234,070</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">815,474,522</td>
<td align="right">818,277,958</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">164,405,782</td>
<td align="right">164,940,572</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">104,701,577</td>
<td align="right">104,973,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,018,411</td>
<td align="right">44,129,853</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,842,259,940</td>
<td align="right">1,845,951,712</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,594,235</td>
<td align="right">10,615,116</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,251</td>
<td align="right">2,898,562</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">72,107,719</td>
<td align="right">71,981,832</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,456,004</td>
<td align="right">141,663,633</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,499,373</td>
<td align="right">4,505,571</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,264,386</td>
<td align="right">11,279,881</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,530,857</td>
<td align="right">47,584,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,676</td>
<td align="right">43,495,697</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,934,664</td>
<td align="right">277,203,086</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">314,076,328</td>
<td align="right">314,333,663</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,019,797</td>
<td align="right">35,047,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,057</td>
<td align="right">268,365,009</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,112,130</td>
<td align="right">22,128,450</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,198,924</td>
<td align="right">56,235,437</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,059,119</td>
<td align="right">91,113,161</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,848,771</td>
<td align="right">8,843,582</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,311,178</td>
<td align="right">60,343,138</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,193,755</td>
<td align="right">150,254,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,269,937,486</td>
<td align="right">2,269,106,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">67,170,929</td>
<td align="right">67,194,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,165</td>
<td align="right">15,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">200,997,085</td>
<td align="right">201,062,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,390,617</td>
<td align="right">21,397,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,938,141</td>
<td align="right">356,041,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,225,017</td>
<td align="right">1,371,843,929</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">719,224</td>
<td align="right">719,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,584,887</td>
<td align="right">402,673,416</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,444,253</td>
<td align="right">198,480,595</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">493,224,734</td>
<td align="right">493,314,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">525,258</td>
<td align="right">525,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,229,934</td>
<td align="right">107,211,838</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">339,327,738</td>
<td align="right">339,279,713</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,660</td>
<td align="right">268,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224,002</td>
<td align="right">223,974</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,056,351,932</td>
<td align="right">1,056,466,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,001,650</td>
<td align="right">147,017,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">98,856,320</td>
<td align="right">98,846,005</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">298,017,155</td>
<td align="right">298,045,707</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231,625,481</td>
<td align="right">231,607,219</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,994,963</td>
<td align="right">10,994,328</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,781</td>
<td align="right">225,022,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,084,646</td>
<td align="right">21,083,596</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,398,958</td>
<td align="right">21,397,921</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">340,423,809</td>
<td align="right">340,413,596</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,772,041</td>
<td align="right">57,770,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,461,736</td>
<td align="right">82,463,847</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">246,817,263</td>
<td align="right">246,821,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,353,394</td>
<td align="right">20,353,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,116</td>
<td align="right">3,744,074</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,259</td>
<td align="right">5,830,229</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,751,430</td>
<td align="right">120,751,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,169,346</td>
<td align="right">94,169,406</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">236,562,124</td>
<td align="right">236,562,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,074</td>
<td align="right">402,104,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,062</td>
<td align="right">173,399,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,887,371</td>
<td align="right">91,887,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,355,103</td>
<td align="right">10,355,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,288</td>
<td align="right">3,465,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">658,292</td>
<td align="right">658,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
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
<td align="right">91,641</td>
<td align="right">91,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">58,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">30,129</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,806</td>
<td align="right">27,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,856</td>
<td align="right">21,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,062</td>
<td align="right">1,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">412,553,451</td>
<td align="right">4.2%</td>
<td align="right">418,714,550</td>
<td align="right">4.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,395,553,379</td>
<td align="right">95.8%</td>
<td align="right">9,395,514,567</td>
<td align="right">95.7%</td>
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
<td align="right">29,575,090</td>
<td align="right">0.3%</td>
<td align="right">29,575,090</td>
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
<td align="left">Failure</td>
<td align="right">1,121,563</td>
<td align="right">65.2%</td>
<td align="right">1,123,896</td>
<td align="right">65.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">599,776</td>
<td align="right">34.8%</td>
<td align="right">599,867</td>
<td align="right">34.8%</td>
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
<td align="right">20,360</td>
<td align="right">1.8%</td>
<td align="right">22,238</td>
<td align="right">2.0%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,875</td>
<td align="right">4.4%</td>
<td align="right">49,098</td>
<td align="right">4.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,803</td>
<td align="right">1.0%</td>
<td align="right">10,844</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,605</td>
<td align="right">0.5%</td>
<td align="right">5,620</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,919</td>
<td align="right">7.4%</td>
<td align="right">83,064</td>
<td align="right">7.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,580</td>
<td align="right">1.3%</td>
<td align="right">14,605</td>
<td align="right">1.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,247</td>
<td align="right">0.7%</td>
<td align="right">8,255</td>
<td align="right">0.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,311</td>
<td align="right">2.8%</td>
<td align="right">31,284</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,468</td>
<td align="right">0.8%</td>
<td align="right">8,473</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,728</td>
<td align="right">0.4%</td>
<td align="right">4,730</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,962</td>
<td align="right">0.3%</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,803</td>
<td align="right">0.6%</td>
<td align="right">6,805</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,350</td>
<td align="right">4.4%</td>
<td align="right">49,362</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,342</td>
<td align="right">2.8%</td>
<td align="right">31,349</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,611</td>
<td align="right">69.7%</td>
<td align="right">781,609</td>
<td align="right">69.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">657,418,254</td>
<td align="right">9.6%</td>
<td align="right">858,881,367</td>
<td align="right">12.2%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,347</td>
<td align="right">0.1%</td>
<td align="right">4,801,997</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,202,014,676</td>
<td align="right">90.4%</td>
<td align="right">6,200,485,216</td>
<td align="right">87.8%</td>
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
<td align="right">221,965</td>
<td align="right">55.0%</td>
<td align="right">270,129</td>
<td align="right">59.8%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,552</td>
<td align="right">45.0%</td>
<td align="right">181,745</td>
<td align="right">40.2%</td>
<td align="right">0.1%</td>
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
<td align="right">109,084</td>
<td align="right">49.1%</td>
<td align="right">158,166</td>
<td align="right">58.6%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">960</td>
<td align="right">0.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,326</td>
<td align="right">26.3%</td>
<td align="right">57,346</td>
<td align="right">21.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,332</td>
<td align="right">9.6%</td>
<td align="right">21,372</td>
<td align="right">7.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">12.0%</td>
<td align="right">26,640</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">4,300</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
<td align="right">151,023,689</td>
<td align="right">1.1%</td>
<td align="right">154,194,455</td>
<td align="right">1.1%</td>
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
<td align="right">640,705,632</td>
<td align="right">4.5%</td>
<td align="right">643,906,789</td>
<td align="right">4.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,489,690,188</td>
<td align="right">95.4%</td>
<td align="right">13,484,528,326</td>
<td align="right">95.4%</td>
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
<td align="right">33,002</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
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
<td align="right">3,375,183</td>
<td align="right">95.3%</td>
<td align="right">3,435,012</td>
<td align="right">95.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,608</td>
<td align="right">4.7%</td>
<td align="right">167,630</td>
<td align="right">4.7%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">156,755</td>
<td align="right">93.5%</td>
<td align="right">156,777</td>
<td align="right">93.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">0.2%</td>
<td align="right">363</td>
<td align="right">0.2%</td>
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
<td align="right">1,327,228</td>
<td align="right">0.0%</td>
<td align="right">1,277,224</td>
<td align="right">0.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">105,073,658</td>
<td align="right">1.8%</td>
<td align="right">105,627,385</td>
<td align="right">1.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,722,183,275</td>
<td align="right">98.2%</td>
<td align="right">5,722,003,028</td>
<td align="right">98.2%</td>
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
<td align="right">164,488</td>
<td align="right">67.4%</td>
<td align="right">162,451</td>
<td align="right">67.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">79,717</td>
<td align="right">32.6%</td>
<td align="right">78,808</td>
<td align="right">32.7%</td>
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
<td align="left">bool</td>
<td align="right">1,550</td>
<td align="right">0.9%</td>
<td align="right">1,461</td>
<td align="right">0.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,452</td>
<td align="right">29.5%</td>
<td align="right">46,380</td>
<td align="right">28.6%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,429</td>
<td align="right">11.8%</td>
<td align="right">19,529</td>
<td align="right">12.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,434</td>
<td align="right">10.6%</td>
<td align="right">17,471</td>
<td align="right">10.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,531</td>
<td align="right">8.8%</td>
<td align="right">14,513</td>
<td align="right">8.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,200</td>
<td align="right">7.4%</td>
<td align="right">12,192</td>
<td align="right">7.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">32,982</td>
<td align="right">20.1%</td>
<td align="right">32,995</td>
<td align="right">20.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.5%</td>
<td align="right">10,680</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.7%</td>
<td align="right">2,720</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">490</td>
<td align="right">0.3%</td>
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
<td align="right">51,965,780</td>
<td align="right">2.0%</td>
<td align="right">63,111,715</td>
<td align="right">2.5%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,776,001</td>
<td align="right">97.9%</td>
<td align="right">2,486,685,029</td>
<td align="right">97.5%</td>
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
<td align="right">2,546,180</td>
<td align="right">0.1%</td>
<td align="right">2,546,180</td>
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
<td align="right">76,741</td>
<td align="right">55.7%</td>
<td align="right">80,237</td>
<td align="right">56.8%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,139</td>
<td align="right">44.3%</td>
<td align="right">61,139</td>
<td align="right">43.2%</td>
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
<td align="right">19,502</td>
<td align="right">25.4%</td>
<td align="right">22,022</td>
<td align="right">27.4%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,470</td>
<td align="right">18.9%</td>
<td align="right">14,930</td>
<td align="right">18.6%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,572</td>
<td align="right">35.9%</td>
<td align="right">28,216</td>
<td align="right">35.2%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,197</td>
<td align="right">19.8%</td>
<td align="right">15,069</td>
<td align="right">18.8%</td>
<td align="right">-0.8%</td>
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
<td align="right">6,745,311</td>
<td align="right">0.6%</td>
<td align="right">30,801,162</td>
<td align="right">1.7%</td>
<td align="right">356.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">482,026,002</td>
<td align="right">46.0%</td>
<td align="right">856,243,174</td>
<td align="right">48.3%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">565,065,112</td>
<td align="right">53.9%</td>
<td align="right">914,034,079</td>
<td align="right">51.6%</td>
<td align="right">61.8%</td>
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
<td align="right">175,673</td>
<td align="right">46.9%</td>
<td align="right">629,522</td>
<td align="right">68.8%</td>
<td align="right">258.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,916</td>
<td align="right">53.1%</td>
<td align="right">285,632</td>
<td align="right">31.2%</td>
<td align="right">43.6%</td>
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
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">1,280</td>
<td align="right">0.4%</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,982</td>
<td align="right">52.8%</td>
<td align="right">186,022</td>
<td align="right">65.1%</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">2.5%</td>
<td align="right">7,436</td>
<td align="right">2.6%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,661</td>
<td align="right">2.3%</td>
<td align="right">5,420</td>
<td align="right">1.9%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,078</td>
<td align="right">5.6%</td>
<td align="right">11,923</td>
<td align="right">4.2%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,354</td>
<td align="right">5.7%</td>
<td align="right">11,796</td>
<td align="right">4.1%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,510</td>
<td align="right">18.4%</td>
<td align="right">36,980</td>
<td align="right">12.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,467</td>
<td align="right">1.2%</td>
<td align="right">2,487</td>
<td align="right">0.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">3.4%</td>
<td align="right">6,737</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">3.3%</td>
<td align="right">6,565</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,202</td>
<td align="right">2.6%</td>
<td align="right">5,202</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,744</td>
<td align="right">1.4%</td>
<td align="right">2,744</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">304,212,637</td>
<td align="right">1.9%</td>
<td align="right">401,132,562</td>
<td align="right">2.5%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">970,016,224</td>
<td align="right">6.0%</td>
<td align="right">1,091,674,629</td>
<td align="right">6.7%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,088,529,966</td>
<td align="right">93.9%</td>
<td align="right">15,098,167,987</td>
<td align="right">93.2%</td>
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
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">303,840</td>
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
<td align="right">863,447</td>
<td align="right">12.0%</td>
<td align="right">1,643,787</td>
<td align="right">16.7%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,353,366</td>
<td align="right">88.0%</td>
<td align="right">8,181,722</td>
<td align="right">83.3%</td>
<td align="right">28.8%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">1,500.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">159,366</td>
<td align="right">18.5%</td>
<td align="right">590,662</td>
<td align="right">35.9%</td>
<td align="right">270.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">155,979</td>
<td align="right">18.1%</td>
<td align="right">498,440</td>
<td align="right">30.3%</td>
<td align="right">219.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">0.6%</td>
<td align="right">5,545</td>
<td align="right">0.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,638</td>
<td align="right">10.4%</td>
<td align="right">91,518</td>
<td align="right">5.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,293</td>
<td align="right">2.4%</td>
<td align="right">20,614</td>
<td align="right">1.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,543</td>
<td align="right">0.3%</td>
<td align="right">2,582</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">176,740</td>
<td align="right">20.5%</td>
<td align="right">179,061</td>
<td align="right">10.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,651</td>
<td align="right">2.0%</td>
<td align="right">17,869</td>
<td align="right">1.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,300</td>
<td align="right">3.0%</td>
<td align="right">26,600</td>
<td align="right">1.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,622</td>
<td align="right">1.8%</td>
<td align="right">15,782</td>
<td align="right">1.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,509</td>
<td align="right">2.0%</td>
<td align="right">17,649</td>
<td align="right">1.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">78,398</td>
<td align="right">9.1%</td>
<td align="right">78,825</td>
<td align="right">4.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,458</td>
<td align="right">10.1%</td>
<td align="right">87,833</td>
<td align="right">5.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,759</td>
<td align="right">0.7%</td>
<td align="right">5,741</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,964</td>
<td align="right">0.3%</td>
<td align="right">2,964</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,844,647,894</td>
<td align="right">99.6%</td>
<td align="right">5,183,722,681</td>
<td align="right">99.6%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">391,983</td>
<td align="right">0.0%</td>
<td align="right">393,688</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,279,854</td>
<td align="right">0.4%</td>
<td align="right">20,281,643</td>
<td align="right">0.4%</td>
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
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">9,236</td>
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
<td align="right">465,523</td>
<td align="right">100.0%</td>
<td align="right">465,697</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">86,248,195</td>
<td align="right">100.0%</td>
<td align="right">86,122,266</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,624</td>
<td align="right">0.0%</td>
<td align="right">7,629</td>
<td align="right">0.0%</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">786,232,534</td>
<td align="right">81.9%</td>
<td align="right">786,232,566</td>
<td align="right">81.9%</td>
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
<td align="right">173,364,414</td>
<td align="right">18.1%</td>
<td align="right">173,364,414</td>
<td align="right">18.1%</td>
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
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">30,643</td>
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
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,195,653</td>
<td align="right">4.2%</td>
<td align="right">113,430,973</td>
<td align="right">4.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">160,755,132</td>
<td align="right">6.1%</td>
<td align="right">164,242,807</td>
<td align="right">6.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,455,709,347</td>
<td align="right">93.8%</td>
<td align="right">2,454,563,697</td>
<td align="right">93.6%</td>
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
<td align="right">2,176,921</td>
<td align="right">95.9%</td>
<td align="right">2,237,954</td>
<td align="right">96.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,527</td>
<td align="right">4.1%</td>
<td align="right">92,851</td>
<td align="right">4.0%</td>
<td align="right">0.4%</td>
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
<td align="right">31,964</td>
<td align="right">34.5%</td>
<td align="right">32,224</td>
<td align="right">34.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">5.5%</td>
<td align="right">5,115</td>
<td align="right">5.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,419</td>
<td align="right">6.9%</td>
<td align="right">6,439</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,772</td>
<td align="right">10.6%</td>
<td align="right">9,776</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,663</td>
<td align="right">9.4%</td>
<td align="right">8,663</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">8.1%</td>
<td align="right">7,505</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,003</td>
<td align="right">5.4%</td>
<td align="right">5,003</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">3.4%</td>
<td align="right">3,185</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">271,898,824</td>
<td align="right">23.7%</td>
<td align="right">472,546,489</td>
<td align="right">35.1%</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,328,194</td>
<td align="right">76.3%</td>
<td align="right">875,234,351</td>
<td align="right">64.9%</td>
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
<td align="right">110,604</td>
<td align="right">89.2%</td>
<td align="right">159,750</td>
<td align="right">92.3%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,369</td>
<td align="right">10.8%</td>
<td align="right">13,375</td>
<td align="right">7.7%</td>
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
<td align="right">43,420</td>
<td align="right">39.3%</td>
<td align="right">92,420</td>
<td align="right">57.9%</td>
<td align="right">112.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,580</td>
<td align="right">1.0%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,540</td>
<td align="right">1.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,661</td>
<td align="right">6.9%</td>
<td align="right">7,707</td>
<td align="right">4.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,203</td>
<td align="right">38.2%</td>
<td align="right">42,223</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,280</td>
<td align="right">12.9%</td>
<td align="right">14,280</td>
<td align="right">8.9%</td>
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
<td align="right">24,998,357</td>
<td align="right">0.4%</td>
<td align="right">28,435,232</td>
<td align="right">0.5%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">188,487,212</td>
<td align="right">3.2%</td>
<td align="right">192,383,326</td>
<td align="right">3.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,754,886,157</td>
<td align="right">96.8%</td>
<td align="right">5,759,508,735</td>
<td align="right">96.8%</td>
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
<td align="right">664,538</td>
<td align="right">72.5%</td>
<td align="right">729,456</td>
<td align="right">73.5%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">252,389</td>
<td align="right">27.5%</td>
<td align="right">263,022</td>
<td align="right">26.5%</td>
<td align="right">4.2%</td>
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
<td align="right">37,241</td>
<td align="right">14.8%</td>
<td align="right">45,566</td>
<td align="right">17.3%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,125</td>
<td align="right">6.8%</td>
<td align="right">17,645</td>
<td align="right">6.7%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,214</td>
<td align="right">33.0%</td>
<td align="right">84,608</td>
<td align="right">32.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,188</td>
<td align="right">9.6%</td>
<td align="right">24,507</td>
<td align="right">9.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,994</td>
<td align="right">2.4%</td>
<td align="right">6,048</td>
<td align="right">2.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,973</td>
<td align="right">2.8%</td>
<td align="right">6,969</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,888</td>
<td align="right">7.9%</td>
<td align="right">19,897</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">54,874</td>
<td align="right">21.7%</td>
<td align="right">54,890</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">723</td>
<td align="right">0.3%</td>
<td align="right">723</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,700</td>
<td align="right">0.0%</td>
<td align="right">195,766</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,703,445</td>
<td align="right">100.0%</td>
<td align="right">1,529,217,861</td>
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
<td align="right">30,519</td>
<td align="right">94.2%</td>
<td align="right">30,587</td>
<td align="right">94.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,863</td>
<td align="right">5.8%</td>
<td align="right">1,861</td>
<td align="right">5.7%</td>
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
<td align="right">1,216</td>
<td align="right">65.3%</td>
<td align="right">1,214</td>
<td align="right">65.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">267</td>
<td align="right">14.3%</td>
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
<td align="right">636,052,247</td>
<td align="right">0.7%</td>
<td align="right">766,833,751</td>
<td align="right">0.7%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,327,743,288</td>
<td align="right">9.5%</td>
<td align="right">10,800,335,789</td>
<td align="right">10.3%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,219,796,621</td>
<td align="right">56.5%</td>
<td align="right">59,790,392,102</td>
<td align="right">56.9%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,592,516,162</td>
<td align="right">33.3%</td>
<td align="right">33,809,392,478</td>
<td align="right">32.1%</td>
<td align="right">3.7%</td>
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
<td align="right">482,026,002</td>
<td align="right">11.7%</td>
<td align="right">856,243,174</td>
<td align="right">16.9%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">271,898,824</td>
<td align="right">6.6%</td>
<td align="right">472,546,489</td>
<td align="right">9.3%</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">657,418,254</td>
<td align="right">15.9%</td>
<td align="right">858,881,367</td>
<td align="right">17.0%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">970,016,224</td>
<td align="right">23.5%</td>
<td align="right">1,091,674,629</td>
<td align="right">21.6%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">160,755,132</td>
<td align="right">3.9%</td>
<td align="right">164,242,807</td>
<td align="right">3.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">188,487,212</td>
<td align="right">4.6%</td>
<td align="right">192,383,326</td>
<td align="right">3.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">412,553,451</td>
<td align="right">10.0%</td>
<td align="right">418,714,550</td>
<td align="right">8.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,073,658</td>
<td align="right">2.5%</td>
<td align="right">105,627,385</td>
<td align="right">2.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">640,705,632</td>
<td align="right">15.5%</td>
<td align="right">643,906,789</td>
<td align="right">12.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,364,414</td>
<td align="right">4.2%</td>
<td align="right">173,364,414</td>
<td align="right">3.4%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">67,368,390</td>
<td align="right">10.6%</td>
<td align="right">117,866,413</td>
<td align="right">15.4%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">129,872,490</td>
<td align="right">20.4%</td>
<td align="right">165,672,591</td>
<td align="right">21.6%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">37,898,202</td>
<td align="right">6.0%</td>
<td align="right">43,301,539</td>
<td align="right">5.6%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,507,967</td>
<td align="right">5.6%</td>
<td align="right">38,213,887</td>
<td align="right">5.0%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,319,016</td>
<td align="right">13.6%</td>
<td align="right">89,541,377</td>
<td align="right">11.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,516,299</td>
<td align="right">12.7%</td>
<td align="right">82,811,979</td>
<td align="right">10.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,237,369</td>
<td align="right">2.9%</td>
<td align="right">17,848,987</td>
<td align="right">2.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,852,971</td>
<td align="right">3.7%</td>
<td align="right">23,865,930</td>
<td align="right">3.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,352</td>
<td align="right">4.3%</td>
<td align="right">27,497,360</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.2%</td>
<td align="right">20,177,240</td>
<td align="right">2.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,251,407</td>
<td align="right">4.0%</td>
<td align="right">333,966,139</td>
<td align="right">4.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">852,113,378</td>
<td align="right">10.1%</td>
<td align="right">851,709,302</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,273,754,537</td>
<td align="right">27.0%</td>
<td align="right">2,272,902,483</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,273,754,537</td>
<td align="right">27.0%</td>
<td align="right">2,272,902,483</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,417,192,758</td>
<td align="right">16.8%</td>
<td align="right">1,416,744,780</td>
<td align="right">16.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,421,641,159</td>
<td align="right">16.9%</td>
<td align="right">1,421,193,181</td>
<td align="right">16.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,759,162</td>
<td align="right">1.0%</td>
<td align="right">84,733,475</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,671,132,731</td>
<td align="right">79.1%</td>
<td align="right">6,669,898,018</td>
<td align="right">79.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,158,388,402</td>
<td align="right">73.0%</td>
<td align="right">6,157,602,382</td>
<td align="right">73.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,756</td>
<td align="right">0.4%</td>
<td align="right">31,097,683</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,645,102</td>
<td align="right">3.9%</td>
<td align="right">331,644,923</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,463</td>
<td align="right">2.1%</td>
<td align="right">175,480,433</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
<td align="right">30,129</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">9,656,654</td>
<td align="right"></td>
<td align="right">6,913,826</td>
<td align="right"></td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">71,836,963</td>
<td align="right"></td>
<td align="right">66,142,004</td>
<td align="right"></td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,176,590</td>
<td align="right"></td>
<td align="right">60,228,001</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">60,708,942,459</td>
<td align="right">37.7%</td>
<td align="right">63,393,897,604</td>
<td align="right">39.7%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">44,345,341,663</td>
<td align="right">32.0%</td>
<td align="right">46,137,718,973</td>
<td align="right">33.7%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">100,182,880,628</td>
<td align="right">62.3%</td>
<td align="right">96,199,180,061</td>
<td align="right">60.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">94,032,332,119</td>
<td align="right">68.0%</td>
<td align="right">90,938,206,073</td>
<td align="right">66.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,967,530</td>
<td align="right">0.4%</td>
<td align="right">93,382,924</td>
<td align="right">0.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,540,147,645</td>
<td align="right"></td>
<td align="right">2,534,689,215</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,359,747,133</td>
<td align="right"></td>
<td align="right">4,363,682,149</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,519,615</td>
<td align="right"></td>
<td align="right">173,447,528</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,592,608,642</td>
<td align="right"></td>
<td align="right">13,594,831,211</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,638,265,680</td>
<td align="right">47.4%</td>
<td align="right">11,637,757,160</td>
<td align="right">47.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,640,151,396</td>
<td align="right"></td>
<td align="right">11,639,680,695</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,359,998</td>
<td align="right">0.1%</td>
<td align="right">15,360,503</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,784,799,743</td>
<td align="right">52.1%</td>
<td align="right">12,784,530,303</td>
<td align="right">52.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,893,127,271</td>
<td align="right">52.6%</td>
<td align="right">12,893,273,730</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,160</td>
<td align="right">1.9%</td>
<td align="right">3,382,160</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,883</td>
<td align="right">0.1%</td>
<td align="right">127,883</td>
<td align="right">0.1%</td>
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
<td align="right">0</td>
<td align="right">113,748,508</td>
<td align="right">19,546,324,589</td>
<td align="right">0</td>
<td align="right">114,882,797</td>
<td align="right">19,565,521,228</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,972,197,132</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,853,856</td>
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
<td align="right">943</td>
<td align="right">0.1%</td>
<td align="right">14,304</td>
<td align="right">0.9%</td>
<td align="right">1,416.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">172,780</td>
<td align="right">17.4%</td>
<td align="right">717,078</td>
<td align="right">45.8%</td>
<td align="right">315.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">993,527</td>
<td align="right"></td>
<td align="right">1,565,677</td>
<td align="right"></td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">10,776</td>
<td align="right">1.1%</td>
<td align="right">15,857</td>
<td align="right">1.0%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">4,420</td>
<td align="right">0.3%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,951</td>
<td align="right">0.2%</td>
<td align="right">2,666</td>
<td align="right">0.2%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">602,273</td>
<td align="right">60.6%</td>
<td align="right">740,439</td>
<td align="right">47.3%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,014,904,987</td>
<td align="right"></td>
<td align="right">8,111,721,610</td>
<td align="right"></td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">818,796</td>
<td align="right">82.4%</td>
<td align="right">845,933</td>
<td align="right">54.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,690</td>
<td align="right">5.0%</td>
<td align="right">8,412</td>
<td align="right">1.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">285,169,549,791</td>
<td align="right">3,163.3%</td>
<td align="right">279,570,668,615</td>
<td align="right">3,446.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
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
<td align="right">162,488</td>
<td align="right">94.0%</td>
<td align="right">698,538</td>
<td align="right">97.4%</td>
<td align="right">329.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">172,780</td>
<td align="right"></td>
<td align="right">717,078</td>
<td align="right"></td>
<td align="right">315.0%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,574</td>
<td align="right">1.5%</td>
<td align="right">2,517</td>
<td align="right">0.4%</td>
<td align="right">-2.2%</td>
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
<td align="right">3,637</td>
<td align="right">2.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,678</td>
<td align="right">13.1%</td>
<td align="right">46,319</td>
<td align="right">6.5%</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,799</td>
<td align="right">12.0%</td>
<td align="right">107,362</td>
<td align="right">15.0%</td>
<td align="right">416.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,690</td>
<td align="right">27.6%</td>
<td align="right">253,560</td>
<td align="right">35.4%</td>
<td align="right">431.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">39,735</td>
<td align="right">23.0%</td>
<td align="right">202,595</td>
<td align="right">28.3%</td>
<td align="right">409.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22,839</td>
<td align="right">13.2%</td>
<td align="right">81,664</td>
<td align="right">11.4%</td>
<td align="right">257.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">13,002</td>
<td align="right">7.5%</td>
<td align="right">22,238</td>
<td align="right">3.1%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,160</td>
<td align="right">1.3%</td>
<td align="right">3,100</td>
<td align="right">0.4%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">19,891</td>
<td align="right">11.5%</td>
<td align="right">29,175</td>
<td align="right">4.1%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">17,035</td>
<td align="right">9.9%</td>
<td align="right">79,961</td>
<td align="right">11.2%</td>
<td align="right">369.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">30,096</td>
<td align="right">17.4%</td>
<td align="right">126,643</td>
<td align="right">17.7%</td>
<td align="right">320.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">49,875</td>
<td align="right">28.9%</td>
<td align="right">291,393</td>
<td align="right">40.6%</td>
<td align="right">484.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,247</td>
<td align="right">16.3%</td>
<td align="right">130,460</td>
<td align="right">18.2%</td>
<td align="right">361.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,044</td>
<td align="right">7.5%</td>
<td align="right">34,846</td>
<td align="right">4.9%</td>
<td align="right">167.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,820</td>
<td align="right">2.2%</td>
<td align="right">5,600</td>
<td align="right">0.8%</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">460</td>
<td align="right">0.3%</td>
<td align="right">460</td>
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
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">440</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">143,040</td>
<td align="right">32,320</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">960,362,113</td>
<td align="right">362,751,948</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,018,060</td>
<td align="right">1,522,960</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">915,179,464</td>
<td align="right">561,245,127</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">40,727,305</td>
<td align="right">25,027,456</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">902,242,483</td>
<td align="right">599,326,445</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">603,925,083</td>
<td align="right">403,277,155</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,580,380</td>
<td align="right">3,075,760</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">874,294,691</td>
<td align="right">672,231,756</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,700,920</td>
<td align="right">2,105,460</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,864,377,913</td>
<td align="right">1,459,967,721</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,940,369,397</td>
<td align="right">1,537,263,680</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,941,520</td>
<td align="right">5,556,160</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">41,965,925</td>
<td align="right">34,051,951</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,515,109,779</td>
<td align="right">2,099,208,202</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,055,672,344</td>
<td align="right">1,720,979,638</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,348,289,257</td>
<td align="right">1,996,461,432</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,362,256,610</td>
<td align="right">2,012,694,732</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,870,920</td>
<td align="right">1,598,080</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">230,748,645</td>
<td align="right">198,391,725</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,438,850,937</td>
<td align="right">1,238,815,649</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">96,213,280</td>
<td align="right">84,059,600</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">95,373,940</td>
<td align="right">83,841,960</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,141,255,938</td>
<td align="right">1,009,575,803</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,459,867,504</td>
<td align="right">3,954,527,425</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">415,379,443</td>
<td align="right">368,959,317</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,007,167,593</td>
<td align="right">1,795,783,664</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,097,725,524</td>
<td align="right">7,252,012,548</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,342,442,171</td>
<td align="right">12,884,235,279</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,014,904,987</td>
<td align="right">8,111,721,610</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">28,138,302</td>
<td align="right">25,615,107</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">24,356,144,407</td>
<td align="right">22,213,586,237</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,683,935,230</td>
<td align="right">3,360,270,703</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,832,222,795</td>
<td align="right">2,587,631,374</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,705,324,747</td>
<td align="right">18,961,005,307</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,984,564,336</td>
<td align="right">9,173,710,364</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">142,356,961</td>
<td align="right">131,209,177</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,680,276,279</td>
<td align="right">8,971,133,118</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">55,419,048</td>
<td align="right">51,531,295</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">653,979,553</td>
<td align="right">613,424,730</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">657,378,743</td>
<td align="right">620,154,553</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">937,941</td>
<td align="right">885,355</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">211,672,846</td>
<td align="right">199,883,512</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,763,275,898</td>
<td align="right">3,561,124,713</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">71,146,582</td>
<td align="right">67,559,162</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">6,786,594</td>
<td align="right">6,449,646</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">869,665,564</td>
<td align="right">828,231,960</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,574,615</td>
<td align="right">6,271,695</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">887,427,315</td>
<td align="right">847,043,616</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">365,512</td>
<td align="right">349,143</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,708,712,708</td>
<td align="right">4,505,056,918</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">186,107,658</td>
<td align="right">178,536,614</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">376,062,883</td>
<td align="right">361,033,405</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">164,185,696</td>
<td align="right">158,114,110</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">208,859,920</td>
<td align="right">201,171,404</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">614,441</td>
<td align="right">592,842</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,781,582,692</td>
<td align="right">7,514,286,348</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">528,707,243</td>
<td align="right">510,820,293</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">301,461,125</td>
<td align="right">291,829,198</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">206,372,250</td>
<td align="right">200,307,616</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,200,135,869</td>
<td align="right">2,137,098,312</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,001,233,513</td>
<td align="right">1,945,497,755</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">247,376,738</td>
<td align="right">240,512,325</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,035,153,257</td>
<td align="right">1,007,336,572</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">467,666,039</td>
<td align="right">455,350,691</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,431,982</td>
<td align="right">109,482,448</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,394,409</td>
<td align="right">61,735,542</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,200,886</td>
<td align="right">34,316,717</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,361,182</td>
<td align="right">131,100,941</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">990,866,582</td>
<td align="right">966,871,622</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,889,180</td>
<td align="right">151,178,180</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">240,956,075</td>
<td align="right">235,294,942</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,222,222</td>
<td align="right">104,777,688</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,895,216,550</td>
<td align="right">2,829,515,871</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">257,276,665</td>
<td align="right">262,901,385</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,306,328,939</td>
<td align="right">2,259,101,362</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,156</td>
<td align="right">120,466,883</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,957,475</td>
<td align="right">13,192,435</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,081,530,132</td>
<td align="right">1,062,535,561</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">1,960,210</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,061,289</td>
<td align="right">9,888,672</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,485,946,444</td>
<td align="right">3,427,135,673</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,828,599</td>
<td align="right">663,046,790</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,580,809,710</td>
<td align="right">1,556,088,927</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,081,160</td>
<td align="right">2,049,200</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,563,944,687</td>
<td align="right">1,540,409,189</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">99,691,136</td>
<td align="right">98,201,849</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,787,736</td>
<td align="right">3,733,572</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">825,705,028</td>
<td align="right">813,961,815</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,544,129,907</td>
<td align="right">1,522,203,669</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,577,021</td>
<td align="right">74,543,996</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,548,425,850</td>
<td align="right">7,446,504,184</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">710,624,683</td>
<td align="right">701,150,205</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,219,792</td>
<td align="right">60,405,112</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,946,365,440</td>
<td align="right">1,920,532,756</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,640,957,188</td>
<td align="right">7,543,072,378</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,940,107,068</td>
<td align="right">1,915,299,830</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">534,936,352</td>
<td align="right">528,410,009</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,301,328,596</td>
<td align="right">4,250,588,989</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,338,214,565</td>
<td align="right">2,311,033,395</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">26,796,331</td>
<td align="right">26,495,798</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,104,246</td>
<td align="right">160,308,724</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,490</td>
<td align="right">1,289,130</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">159,953,595</td>
<td align="right">158,193,435</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">438,495,179</td>
<td align="right">433,706,509</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">65,250,400</td>
<td align="right">64,549,280</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,235,799,942</td>
<td align="right">2,213,728,945</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">878,182,156</td>
<td align="right">870,245,401</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,184,551,275</td>
<td align="right">3,155,796,240</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,145,554,855</td>
<td align="right">3,117,503,660</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">234,817,246</td>
<td align="right">232,762,265</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,624</td>
<td align="right">11,724</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,330,484</td>
<td align="right">8,260,124</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,296,688</td>
<td align="right">13,190,667</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,296,688</td>
<td align="right">13,190,667</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,448,118,022</td>
<td align="right">3,424,575,056</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,076,776,136</td>
<td align="right">1,070,092,529</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">107,884,360</td>
<td align="right">107,228,220</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">978,405,654</td>
<td align="right">972,690,844</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,420,956,327</td>
<td align="right">1,412,723,029</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,326,996,411</td>
<td align="right">1,319,577,767</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">391,425,102</td>
<td align="right">389,273,250</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,045,929,768</td>
<td align="right">1,040,707,696</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">569,357,290</td>
<td align="right">566,546,546</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,124,970,591</td>
<td align="right">1,119,499,547</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,577,440</td>
<td align="right">5,550,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">340,483,301</td>
<td align="right">338,900,045</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">497,898,064</td>
<td align="right">495,607,676</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">502,702,224</td>
<td align="right">500,411,396</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,303,825</td>
<td align="right">54,095,556</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,299,585</td>
<td align="right">54,091,936</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">688,538,614</td>
<td align="right">686,047,920</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">325,869,499</td>
<td align="right">324,713,058</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">197,058,566</td>
<td align="right">196,410,726</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,244,048</td>
<td align="right">280,336,375</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,702,031,262</td>
<td align="right">3,690,799,437</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,926,402</td>
<td align="right">78,699,680</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,600,625,198</td>
<td align="right">3,590,639,520</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,200</td>
<td align="right">4,247,680</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">986,762,974</td>
<td align="right">984,336,688</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,634,039</td>
<td align="right">94,415,309</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">941,936,966</td>
<td align="right">939,807,956</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,442,680</td>
<td align="right">9,422,230</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,604,135,313</td>
<td align="right">1,600,813,376</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,707,868</td>
<td align="right">85,552,008</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,343,624,645</td>
<td align="right">1,341,221,807</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,567,700</td>
<td align="right">32,624,320</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,980,819</td>
<td align="right">114,792,179</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,470,425,248</td>
<td align="right">1,468,157,991</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,176,890,175</td>
<td align="right">5,169,436,141</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">788,268,381</td>
<td align="right">787,146,186</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,639,920</td>
<td align="right">204,350,320</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,033,160,840</td>
<td align="right">3,029,342,026</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,377,842</td>
<td align="right">210,128,542</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,548,145,846</td>
<td align="right">2,545,217,539</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">25,217,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">307,134,561</td>
<td align="right">306,785,790</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">555,698,049</td>
<td align="right">555,110,532</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">106,094,463</td>
<td align="right">105,986,591</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,603,484,226</td>
<td align="right">5,597,911,678</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,894</td>
<td align="right">5,467,583</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,419,220</td>
<td align="right">125,307,780</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,153,047,242</td>
<td align="right">6,147,960,506</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,398,228</td>
<td align="right">97,318,104</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">37,843,900</td>
<td align="right">37,812,780</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">393,967,002</td>
<td align="right">393,657,262</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,974,995</td>
<td align="right">1,819,746,810</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,828</td>
<td align="right">90,249,535</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">234,896,292</td>
<td align="right">234,743,851</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,246,790,636</td>
<td align="right">1,245,993,397</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,289,081</td>
<td align="right">97,236,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,780,100</td>
<td align="right">57,752,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">162,266,588</td>
<td align="right">162,201,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,240,981</td>
<td align="right">97,203,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,260</td>
<td align="right">517,906,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">127,819,170</td>
<td align="right">127,773,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,089,903</td>
<td align="right">39,103,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">239,659,590</td>
<td align="right">239,585,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,625,940</td>
<td align="right">46,612,317</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,929</td>
<td align="right">167,877,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,007,580</td>
<td align="right">80,986,104</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">111,840,420</td>
<td align="right">111,811,717</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">102,819,372</td>
<td align="right">102,795,303</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,226,981</td>
<td align="right">68,213,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,632,540</td>
<td align="right">532,536,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,660,964,448</td>
<td align="right">1,660,707,093</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,436,734</td>
<td align="right">779,326,409</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,794,494</td>
<td align="right">780,684,169</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">732,984,238</td>
<td align="right">732,897,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">856,223,278</td>
<td align="right">856,155,314</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,852,286</td>
<td align="right">532,811,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,343,531</td>
<td align="right">1,713,239,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,620</td>
<td align="right">103,812,376</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,620</td>
<td align="right">103,812,376</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,331,855,094</td>
<td align="right">1,331,902,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">559,022,360</td>
<td align="right">559,014,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,437,280</td>
<td align="right">32,437,202</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,488,404</td>
<td align="right">228,488,364</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,950</td>
<td align="right">603,439,941</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,096,877,240</td>
<td align="right">1,096,877,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">350,232,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">51,907,580</td>
<td align="right">51,907,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">11,445,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">10,396,360</td>
<td align="right">10,396,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,825,480</td>
<td align="right">1,825,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">1,543,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,225,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">590,260</td>
<td align="right">590,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">24,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INCREMENT_RUN_COUNT</td>
<td align="right"></td>
<td align="right">10,699,352,984</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">920</td>
<td align="right">1,980</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">36,344</td>
<td align="right">65,946</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">131,353</td>
<td align="right">69,038</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,181</td>
<td align="right">16,042</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,563</td>
<td align="right">56,432</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,440</td>
<td align="right">42,420</td>
<td align="right">23.2%</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,146</td>
<td align="right">1,149</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,146</td>
<td align="right">1,149</td>
<td align="right">0.3%</td>
</tr>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-21
