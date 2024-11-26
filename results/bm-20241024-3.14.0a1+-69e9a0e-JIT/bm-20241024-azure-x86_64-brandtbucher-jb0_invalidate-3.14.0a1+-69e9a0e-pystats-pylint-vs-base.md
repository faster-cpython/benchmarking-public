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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,012,771</td>
<td align="right">53,789,643</td>
<td align="right">133.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">164,551</td>
<td align="right">109</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,690,363</td>
<td align="right">4,631</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,427</td>
<td align="right">122</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,611</td>
<td align="right">301</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,611,034</td>
<td align="right">103,908</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,343,269</td>
<td align="right">96,740</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">215,365</td>
<td align="right">9,315</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,688</td>
<td align="right">374</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,664,972</td>
<td align="right">513,121</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,932,112</td>
<td align="right">511,134</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">761,080</td>
<td align="right">1,402,986</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,651</td>
<td align="right">3,521</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">67,336</td>
<td align="right">14,305</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,198,483</td>
<td align="right">257,287</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">231,437</td>
<td align="right">53,730</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">506,822</td>
<td align="right">136,460</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">553,256</td>
<td align="right">152,106</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">223,694</td>
<td align="right">68,052</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,688,849</td>
<td align="right">2,129,406</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,947,816</td>
<td align="right">2,285,915</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,765,922</td>
<td align="right">922,072</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,532,515</td>
<td align="right">2,230,723</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">329,925</td>
<td align="right">114,338</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">284,623</td>
<td align="right">99,264</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">134,132</td>
<td align="right">47,673</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,182,959</td>
<td align="right">3,268,450</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">42,341,873</td>
<td align="right">15,597,440</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,760,062</td>
<td align="right">658,787</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,943</td>
<td align="right">108,186</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,550</td>
<td align="right">108,235</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">946,423</td>
<td align="right">372,424</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,242,403</td>
<td align="right">891,243</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,105,923</td>
<td align="right">441,636</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,606,114</td>
<td align="right">2,298,988</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,317,502</td>
<td align="right">9,930,821</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">129,241</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,913,495</td>
<td align="right">878,641</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,566,587</td>
<td align="right">730,802</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,076,730</td>
<td align="right">988,353</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,748,553</td>
<td align="right">4,306,699</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,685,373</td>
<td align="right">834,531</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,909,727</td>
<td align="right">964,376</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,125,698</td>
<td align="right">577,452</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,752,002</td>
<td align="right">11,187,902</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,082</td>
<td align="right">40,678</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">429,900</td>
<td align="right">229,420</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,569,042</td>
<td align="right">1,376,884</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">135,679,503</td>
<td align="right">75,197,031</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,306,381</td>
<td align="right">1,871,804</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,838,524</td>
<td align="right">4,486,487</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,359,776</td>
<td align="right">791,833</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,424,716</td>
<td align="right">2,006,716</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">615,739</td>
<td align="right">361,737</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,900,493</td>
<td align="right">3,498,148</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">71,391</td>
<td align="right">43,369</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,689,145</td>
<td align="right">6,511,673</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,469,923</td>
<td align="right">1,508,950</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,918,237</td>
<td align="right">19,837,678</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,977,846</td>
<td align="right">13,067,856</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">37,743,391</td>
<td align="right">23,550,409</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,484,207</td>
<td align="right">2,184,402</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">913</td>
<td align="right">577</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">13,000,485</td>
<td align="right">8,233,961</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,473,187</td>
<td align="right">1,600,693</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,368,475</td>
<td align="right">2,187,350</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,391,453</td>
<td align="right">5,453,593</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,659,499</td>
<td align="right">1,105,697</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,821</td>
<td align="right">388,759</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">868,404</td>
<td align="right">581,789</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,486,039</td>
<td align="right">15,848,505</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">965,577</td>
<td align="right">654,683</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,454,696</td>
<td align="right">993,233</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,898,071</td>
<td align="right">1,318,875</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">479,948</td>
<td align="right">333,546</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">622,316</td>
<td align="right">433,220</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,536,992</td>
<td align="right">3,162,870</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,471,373</td>
<td align="right">1,026,283</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,253,007</td>
<td align="right">8,553,401</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">11,049</td>
<td align="right">7,719</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,141,475</td>
<td align="right">814,049</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,882,219</td>
<td align="right">18,539,452</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,139,374</td>
<td align="right">830,524</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,293,273</td>
<td align="right">2,402,532</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">524</td>
<td align="right">386</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,398,620</td>
<td align="right">1,031,813</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,795,098</td>
<td align="right">2,077,805</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">422,704</td>
<td align="right">316,407</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">586,011</td>
<td align="right">441,909</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,052,411</td>
<td align="right">795,473</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,540,541</td>
<td align="right">1,168,897</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">19,529,886</td>
<td align="right">14,954,312</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,620,677</td>
<td align="right">8,184,320</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,879,475</td>
<td align="right">1,462,084</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">354,890</td>
<td align="right">276,115</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,208</td>
<td align="right">1,718</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,826,388</td>
<td align="right">1,427,108</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">855,001</td>
<td align="right">672,854</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,624</td>
<td align="right">51,999</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">31,277,658</td>
<td align="right">25,046,312</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,042,826</td>
<td align="right">3,280,760</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,391,897</td>
<td align="right">1,132,518</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">317,979</td>
<td align="right">261,229</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,143,847</td>
<td align="right">940,980</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">956,088</td>
<td align="right">796,979</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">914,342</td>
<td align="right">770,040</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,923</td>
<td align="right">15,987</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,127</td>
<td align="right">9,447</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">125,727</td>
<td align="right">107,383</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">13,516,296</td>
<td align="right">11,863,225</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,949,573</td>
<td align="right">21,311,456</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,962</td>
<td align="right">75,073</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">194,032</td>
<td align="right">175,878</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,023</td>
<td align="right">3,687</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">26,582</td>
<td align="right">24,404</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">28,950</td>
<td align="right">27,037</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,471,007</td>
<td align="right">1,383,769</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,841,256</td>
<td align="right">1,743,018</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80,285</td>
<td align="right">76,400</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">276,159</td>
<td align="right">266,460</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,447,876</td>
<td align="right">35,178,224</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">958,024</td>
<td align="right">932,225</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,125</td>
<td align="right">426,727</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">117,540</td>
<td align="right">114,962</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,009</td>
<td align="right">2,048</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">26,862,811</td>
<td align="right">27,284,324</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">804,130</td>
<td align="right">792,258</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">486,466</td>
<td align="right">479,401</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,820</td>
<td align="right">56,130</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">36,258</td>
<td align="right">35,877</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,591,452</td>
<td align="right">1,577,736</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">818,451</td>
<td align="right">811,410</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,244</td>
<td align="right">254,562</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,150,007</td>
<td align="right">11,123,357</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">41,671</td>
<td align="right">41,609</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">776,155</td>
<td align="right">776,865</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">7,729,270</td>
<td align="right">7,734,704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,450,312</td>
<td align="right">1,449,337</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">610,782</td>
<td align="right">610,444</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">580,906</td>
<td align="right">581,224</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">19,102,275</td>
<td align="right">19,095,708</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,081,272</td>
<td align="right">5,080,222</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4,605,114</td>
<td align="right">4,604,542</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,585,437</td>
<td align="right">11,585,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,702,081</td>
<td align="right">4,702,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,718,303</td>
<td align="right">11,718,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,475</td>
<td align="right">8,152,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,495,099</td>
<td align="right">6,495,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,048,062</td>
<td align="right">1,048,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">687,734</td>
<td align="right">687,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">611,589</td>
<td align="right">611,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">118,722</td>
<td align="right">118,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,284</td>
<td align="right">98,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,999</td>
<td align="right">41,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,835</td>
<td align="right">26,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,914</td>
<td align="right">22,914</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,977</td>
<td align="right">2,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,410</td>
<td align="right">2,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,149</td>
<td align="right">1,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,077</td>
<td align="right">1,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">935</td>
<td align="right">935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">525</td>
<td align="right">525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">508</td>
<td align="right">508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">217</td>
<td align="right">217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">206</td>
<td align="right">206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">53</td>
<td align="right">53</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">10</td>
<td align="right">10</td>
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
<td align="right">315,240</td>
<td align="right">5.1%</td>
<td align="right">258,677</td>
<td align="right">4.2%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,875,744</td>
<td align="right">94.9%</td>
<td align="right">5,847,713</td>
<td align="right">95.7%</td>
<td align="right">-0.5%</td>
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
<td align="right">2,300</td>
<td align="right">84.0%</td>
<td align="right">2,114</td>
<td align="right">82.8%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">439</td>
<td align="right">16.0%</td>
<td align="right">438</td>
<td align="right">17.2%</td>
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
<td align="left">remainder</td>
<td align="right">196</td>
<td align="right">8.5%</td>
<td align="right">154</td>
<td align="right">7.3%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">249</td>
<td align="right">10.8%</td>
<td align="right">205</td>
<td align="right">9.7%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">156</td>
<td align="right">6.8%</td>
<td align="right">141</td>
<td align="right">6.7%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,029</td>
<td align="right">44.7%</td>
<td align="right">953</td>
<td align="right">45.1%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">144</td>
<td align="right">6.3%</td>
<td align="right">137</td>
<td align="right">6.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">91</td>
<td align="right">4.0%</td>
<td align="right">89</td>
<td align="right">4.2%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.5%</td>
<td align="right">173</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.2%</td>
<td align="right">120</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">2.9%</td>
<td align="right">66</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">37</td>
<td align="right">1.6%</td>
<td align="right">37</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">288,746</td>
<td align="right">100.0%</td>
<td align="right">129,241</td>
<td align="right">100.0%</td>
<td align="right">-55.2%</td>
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
<td align="right">1,100,539</td>
<td align="right">9.8%</td>
<td align="right">437,072</td>
<td align="right">4.1%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,116,521</td>
<td align="right">90.0%</td>
<td align="right">10,088,496</td>
<td align="right">95.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,346</td>
<td align="right">0.1%</td>
<td align="right">15,346</td>
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
<td align="right">3,958</td>
<td align="right">69.9%</td>
<td align="right">3,139</td>
<td align="right">64.8%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,704</td>
<td align="right">30.1%</td>
<td align="right">1,703</td>
<td align="right">35.2%</td>
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
<td align="left">buffer slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">887</td>
<td align="right">22.4%</td>
<td align="right">613</td>
<td align="right">19.5%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">636</td>
<td align="right">16.1%</td>
<td align="right">443</td>
<td align="right">14.1%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">822</td>
<td align="right">20.8%</td>
<td align="right">576</td>
<td align="right">18.3%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">776</td>
<td align="right">19.6%</td>
<td align="right">718</td>
<td align="right">22.9%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">771</td>
<td align="right">19.5%</td>
<td align="right">729</td>
<td align="right">23.2%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">33</td>
<td align="right">0.8%</td>
<td align="right">33</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">21</td>
<td align="right">0.7%</td>
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
<td align="right">7,078,016</td>
<td align="right">10.4%</td>
<td align="right">6,863,497</td>
<td align="right">10.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,903,609</td>
<td align="right">89.6%</td>
<td align="right">61,055,430</td>
<td align="right">89.9%</td>
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
<td align="right">6,876</td>
<td align="right">0.0%</td>
<td align="right">6,876</td>
<td align="right">0.0%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">164,723</td>
<td align="right">100.0%</td>
<td align="right">153,430</td>
<td align="right">100.0%</td>
<td align="right">-6.9%</td>
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
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">517,467</td>
<td align="right">99.5%</td>
<td align="right">134,509</td>
<td align="right">98.2%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">559</td>
<td align="right">0.1%</td>
<td align="right">559</td>
<td align="right">0.4%</td>
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
<td align="right">2,546</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">954,120</td>
<td align="right">5.3%</td>
<td align="right">928,467</td>
<td align="right">5.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,205,292</td>
<td align="right">94.7%</td>
<td align="right">17,191,213</td>
<td align="right">94.9%</td>
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
<td align="right">2,441</td>
<td align="right">61.7%</td>
<td align="right">2,276</td>
<td align="right">60.5%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,515</td>
<td align="right">38.3%</td>
<td align="right">1,484</td>
<td align="right">39.5%</td>
<td align="right">-2.0%</td>
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
<td align="right">1,014</td>
<td align="right">41.5%</td>
<td align="right">830</td>
<td align="right">36.5%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">188</td>
<td align="right">7.7%</td>
<td align="right">207</td>
<td align="right">9.1%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">237</td>
<td align="right">9.7%</td>
<td align="right">238</td>
<td align="right">10.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">633</td>
<td align="right">25.9%</td>
<td align="right">633</td>
<td align="right">27.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">160</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.7%</td>
<td align="right">90</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">51</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">48</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">18</td>
<td align="right">0.7%</td>
<td align="right">18</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">1,134,712</td>
<td align="right">21.5%</td>
<td align="right">808,088</td>
<td align="right">16.3%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,944</td>
<td align="right">0.5%</td>
<td align="right">26,322</td>
<td align="right">0.5%</td>
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
<td align="right">4,110,971</td>
<td align="right">77.9%</td>
<td align="right">4,113,890</td>
<td align="right">83.0%</td>
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
<td align="right">6,055</td>
<td align="right">83.5%</td>
<td align="right">5,253</td>
<td align="right">81.4%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,198</td>
<td align="right">16.5%</td>
<td align="right">1,198</td>
<td align="right">18.6%</td>
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
<td align="right">1,214</td>
<td align="right">20.0%</td>
<td align="right">678</td>
<td align="right">12.9%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">512</td>
<td align="right">8.5%</td>
<td align="right">461</td>
<td align="right">8.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,171</td>
<td align="right">52.4%</td>
<td align="right">2,941</td>
<td align="right">56.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,158</td>
<td align="right">19.1%</td>
<td align="right">1,173</td>
<td align="right">22.3%</td>
<td align="right">1.3%</td>
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
<td align="right">1,386,447</td>
<td align="right">7.7%</td>
<td align="right">1,127,379</td>
<td align="right">6.7%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,567,810</td>
<td align="right">91.7%</td>
<td align="right">15,584,626</td>
<td align="right">92.6%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">107,506</td>
<td align="right">0.6%</td>
<td align="right">107,613</td>
<td align="right">0.6%</td>
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
<td align="right">4,321</td>
<td align="right">58.0%</td>
<td align="right">4,010</td>
<td align="right">56.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,133</td>
<td align="right">42.0%</td>
<td align="right">3,155</td>
<td align="right">44.0%</td>
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
<td align="left">enumerate</td>
<td align="right">815</td>
<td align="right">18.9%</td>
<td align="right">608</td>
<td align="right">15.2%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">236</td>
<td align="right">5.5%</td>
<td align="right">192</td>
<td align="right">4.8%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,000</td>
<td align="right">23.1%</td>
<td align="right">924</td>
<td align="right">23.0%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">444</td>
<td align="right">10.3%</td>
<td align="right">464</td>
<td align="right">11.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">82</td>
<td align="right">1.9%</td>
<td align="right">79</td>
<td align="right">2.0%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,186</td>
<td align="right">27.4%</td>
<td align="right">1,186</td>
<td align="right">29.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">231</td>
<td align="right">5.3%</td>
<td align="right">231</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">228</td>
<td align="right">5.3%</td>
<td align="right">228</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.4%</td>
<td align="right">61</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">25</td>
<td align="right">0.6%</td>
<td align="right">25</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,670,327</td>
<td align="right">8.0%</td>
<td align="right">4,244,349</td>
<td align="right">4.4%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,315,347</td>
<td align="right">20.7%</td>
<td align="right">16,820,169</td>
<td align="right">17.6%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">76,867,051</td>
<td align="right">71.2%</td>
<td align="right">74,664,776</td>
<td align="right">77.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">207,261</td>
<td align="right">0.2%</td>
<td align="right">207,114</td>
<td align="right">0.2%</td>
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
<td align="right">15,485</td>
<td align="right">3.1%</td>
<td align="right">11,105</td>
<td align="right">3.0%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479,849</td>
<td align="right">96.9%</td>
<td align="right">364,879</td>
<td align="right">97.0%</td>
<td align="right">-24.0%</td>
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
<td align="right">488</td>
<td align="right">3.2%</td>
<td align="right">143</td>
<td align="right">1.3%</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">66</td>
<td align="right">0.4%</td>
<td align="right">31</td>
<td align="right">0.3%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">1.1%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">205</td>
<td align="right">1.3%</td>
<td align="right">110</td>
<td align="right">1.0%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,399</td>
<td align="right">22.0%</td>
<td align="right">2,163</td>
<td align="right">19.5%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,903</td>
<td align="right">31.7%</td>
<td align="right">3,512</td>
<td align="right">31.6%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,241</td>
<td align="right">8.0%</td>
<td align="right">909</td>
<td align="right">8.2%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,583</td>
<td align="right">10.2%</td>
<td align="right">1,176</td>
<td align="right">10.6%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">343</td>
<td align="right">2.2%</td>
<td align="right">257</td>
<td align="right">2.3%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">852</td>
<td align="right">5.5%</td>
<td align="right">711</td>
<td align="right">6.4%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">835</td>
<td align="right">5.4%</td>
<td align="right">793</td>
<td align="right">7.1%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">58</td>
<td align="right">0.4%</td>
<td align="right">56</td>
<td align="right">0.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">42,725,958</td>
<td align="right">99.9%</td>
<td align="right">24,469,158</td>
<td align="right">99.9%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,039</td>
<td align="right">0.0%</td>
<td align="right">5,039</td>
<td align="right">0.0%</td>
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
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">521</td>
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
<td align="right">4,500</td>
<td align="right">0.0%</td>
<td align="right">4,500</td>
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
<td align="right">17,949</td>
<td align="right">100.0%</td>
<td align="right">17,949</td>
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
<td align="right">103</td>
<td align="right">0.0%</td>
<td align="right">103</td>
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
<td align="right">718,867</td>
<td align="right">99.9%</td>
<td align="right">718,867</td>
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
<td align="right">422</td>
<td align="right">100.0%</td>
<td align="right">422</td>
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
<td align="right">6,492,134</td>
<td align="right">54.9%</td>
<td align="right">6,492,134</td>
<td align="right">54.9%</td>
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
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
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
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
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
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
<td align="right">1,191,439</td>
<td align="right">8.5%</td>
<td align="right">251,559</td>
<td align="right">2.0%</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,960,035</td>
<td align="right">14.0%</td>
<td align="right">856,520</td>
<td align="right">6.8%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,823,060</td>
<td align="right">77.4%</td>
<td align="right">11,502,022</td>
<td align="right">91.2%</td>
<td align="right">6.3%</td>
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
<td align="right">2,518</td>
<td align="right">5.7%</td>
<td align="right">1,202</td>
<td align="right">5.5%</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,439</td>
<td align="right">94.3%</td>
<td align="right">20,626</td>
<td align="right">94.5%</td>
<td align="right">-50.2%</td>
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
<td align="right">1,383</td>
<td align="right">54.9%</td>
<td align="right">139</td>
<td align="right">11.6%</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">12</td>
<td align="right">1.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">6</td>
<td align="right">0.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">129</td>
<td align="right">5.1%</td>
<td align="right">99</td>
<td align="right">8.2%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">58</td>
<td align="right">4.8%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">270</td>
<td align="right">10.7%</td>
<td align="right">223</td>
<td align="right">18.6%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">29</td>
<td align="right">1.2%</td>
<td align="right">30</td>
<td align="right">2.5%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">401</td>
<td align="right">15.9%</td>
<td align="right">401</td>
<td align="right">33.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">9.1%</td>
<td align="right">230</td>
<td align="right">19.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">29</td>
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
<td align="right">79,520</td>
<td align="right">3.0%</td>
<td align="right">75,679</td>
<td align="right">2.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,587,628</td>
<td align="right">97.0%</td>
<td align="right">2,559,597</td>
<td align="right">97.1%</td>
<td align="right">-1.1%</td>
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
<td align="right">424</td>
<td align="right">55.4%</td>
<td align="right">381</td>
<td align="right">52.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">341</td>
<td align="right">44.6%</td>
<td align="right">340</td>
<td align="right">47.2%</td>
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
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">11.1%</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">13</td>
<td align="right">3.1%</td>
<td align="right">14</td>
<td align="right">3.7%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">56.6%</td>
<td align="right">240</td>
<td align="right">63.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.7%</td>
<td align="right">92</td>
<td align="right">24.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">26</td>
<td align="right">6.1%</td>
<td align="right">26</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">6</td>
<td align="right">1.4%</td>
<td align="right">6</td>
<td align="right">1.6%</td>
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
<td align="right">488,984</td>
<td align="right">1.2%</td>
<td align="right">126,417</td>
<td align="right">0.4%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,138,064</td>
<td align="right">2.8%</td>
<td align="right">730,183</td>
<td align="right">2.0%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,727,210</td>
<td align="right">95.9%</td>
<td align="right">35,133,377</td>
<td align="right">97.6%</td>
<td align="right">-9.3%</td>
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
<td align="right">10,363</td>
<td align="right">26.6%</td>
<td align="right">2,590</td>
<td align="right">11.0%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,651</td>
<td align="right">73.4%</td>
<td align="right">20,939</td>
<td align="right">89.0%</td>
<td align="right">-26.9%</td>
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
<td align="left">set</td>
<td align="right">7,763</td>
<td align="right">74.9%</td>
<td align="right">374</td>
<td align="right">14.4%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">121</td>
<td align="right">1.2%</td>
<td align="right">56</td>
<td align="right">2.2%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">6.4%</td>
<td align="right">392</td>
<td align="right">15.1%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">3.1%</td>
<td align="right">282</td>
<td align="right">10.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">27</td>
<td align="right">0.3%</td>
<td align="right">24</td>
<td align="right">0.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">541</td>
<td align="right">5.2%</td>
<td align="right">584</td>
<td align="right">22.5%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">871</td>
<td align="right">8.4%</td>
<td align="right">829</td>
<td align="right">32.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.5%</td>
<td align="right">49</td>
<td align="right">1.9%</td>
<td align="right">-2.0%</td>
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
<td align="right">1,139</td>
<td align="right">0.0%</td>
<td align="right">1,159</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,960,723</td>
<td align="right">100.0%</td>
<td align="right">7,936,383</td>
<td align="right">100.0%</td>
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
<td align="right">834</td>
<td align="right">95.9%</td>
<td align="right">853</td>
<td align="right">96.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36</td>
<td align="right">4.1%</td>
<td align="right">36</td>
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
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">66.7%</td>
<td align="right">24</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12</td>
<td align="right">33.3%</td>
<td align="right">12</td>
<td align="right">33.3%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">283,031,675</td>
<td align="right">32.7%</td>
<td align="right">158,056,911</td>
<td align="right">25.6%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">22,288,008</td>
<td align="right">2.6%</td>
<td align="right">15,037,604</td>
<td align="right">2.4%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">33,166,374</td>
<td align="right">3.8%</td>
<td align="right">25,560,340</td>
<td align="right">4.1%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">526,286,763</td>
<td align="right">60.9%</td>
<td align="right">418,198,704</td>
<td align="right">67.8%</td>
<td align="right">-20.5%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">1,191,439</td>
<td align="right">5.4%</td>
<td align="right">251,559</td>
<td align="right">1.7%</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">488,984</td>
<td align="right">2.2%</td>
<td align="right">126,417</td>
<td align="right">0.8%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,100,539</td>
<td align="right">5.0%</td>
<td align="right">437,072</td>
<td align="right">2.9%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">1.3%</td>
<td align="right">129,241</td>
<td align="right">0.9%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,670,327</td>
<td align="right">39.2%</td>
<td align="right">4,244,349</td>
<td align="right">28.5%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,134,712</td>
<td align="right">5.1%</td>
<td align="right">808,088</td>
<td align="right">5.4%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,386,447</td>
<td align="right">6.3%</td>
<td align="right">1,127,379</td>
<td align="right">7.6%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">315,240</td>
<td align="right">1.4%</td>
<td align="right">258,677</td>
<td align="right">1.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">954,120</td>
<td align="right">4.3%</td>
<td align="right">928,467</td>
<td align="right">6.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,492,134</td>
<td align="right">29.4%</td>
<td align="right">6,492,134</td>
<td align="right">43.6%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,959,972</td>
<td align="right">5.9%</td>
<td align="right">856,404</td>
<td align="right">3.4%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,209,252</td>
<td align="right">9.7%</td>
<td align="right">1,548,560</td>
<td align="right">6.1%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">643,793</td>
<td align="right">1.9%</td>
<td align="right">316,678</td>
<td align="right">1.2%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">753,126</td>
<td align="right">2.3%</td>
<td align="right">461,843</td>
<td align="right">1.8%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,191,748</td>
<td align="right">15.7%</td>
<td align="right">3,477,283</td>
<td align="right">13.6%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,462,192</td>
<td align="right">4.4%</td>
<td align="right">1,146,274</td>
<td align="right">4.5%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,743,883</td>
<td align="right">35.4%</td>
<td align="right">10,265,888</td>
<td align="right">40.2%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,264,917</td>
<td align="right">3.8%</td>
<td align="right">1,205,131</td>
<td align="right">4.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,078,312</td>
<td align="right">15.3%</td>
<td align="right">5,033,705</td>
<td align="right">19.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">480,556</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">410,047</td>
<td align="right">1.6%</td>
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
<td align="right">1,277,686</td>
<td align="right">1.8%</td>
<td align="right">1,278,444</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,502,262</td>
<td align="right">7.9%</td>
<td align="right">5,502,925</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,550,072</td>
<td align="right">9.4%</td>
<td align="right">6,549,757</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,551,218</td>
<td align="right">9.4%</td>
<td align="right">6,550,903</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">12,053,480</td>
<td align="right">17.4%</td>
<td align="right">12,053,828</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">12,053,480</td>
<td align="right">17.4%</td>
<td align="right">12,053,828</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">392,014</td>
<td align="right">0.6%</td>
<td align="right">392,017</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,800,327</td>
<td align="right">68.9%</td>
<td align="right">47,800,651</td>
<td align="right">68.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,342,015</td>
<td align="right">82.6%</td>
<td align="right">57,342,383</td>
<td align="right">82.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">913</td>
<td align="right">0.0%</td>
<td align="right">913</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,161,291</td>
<td align="right">1.7%</td>
<td align="right">1,161,291</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">22</td>
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
<td align="left">Mortal increfs</td>
<td align="right">480,047,710</td>
<td align="right">39.6%</td>
<td align="right">647,092,095</td>
<td align="right">50.8%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">456,547,006</td>
<td align="right">35.2%</td>
<td align="right">598,521,461</td>
<td align="right">42.6%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">147,809,318</td>
<td align="right">12.2%</td>
<td align="right">109,751,916</td>
<td align="right">8.6%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">222,811,155</td>
<td align="right">17.2%</td>
<td align="right">278,121,147</td>
<td align="right">19.8%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">363,801,389</td>
<td align="right">30.0%</td>
<td align="right">275,781,669</td>
<td align="right">21.6%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">363,383</td>
<td align="right">0.4%</td>
<td align="right">435,225</td>
<td align="right">0.5%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">149,418,507</td>
<td align="right">11.5%</td>
<td align="right">121,436,451</td>
<td align="right">8.6%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">469,300,848</td>
<td align="right">36.2%</td>
<td align="right">406,495,922</td>
<td align="right">28.9%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">220,633,019</td>
<td align="right">18.2%</td>
<td align="right">241,540,014</td>
<td align="right">19.0%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">311,459</td>
<td align="right"></td>
<td align="right">334,674</td>
<td align="right"></td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,413,091</td>
<td align="right"></td>
<td align="right">49,948,160</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,481,019</td>
<td align="right"></td>
<td align="right">1,444,600</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,766</td>
<td align="right">0.0%</td>
<td align="right">39,082</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,790,578</td>
<td align="right"></td>
<td align="right">1,777,372</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">66,710,572</td>
<td align="right"></td>
<td align="right">66,864,100</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">67,990,650</td>
<td align="right">70.7%</td>
<td align="right">68,139,877</td>
<td align="right">70.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,588,501</td>
<td align="right">70.3%</td>
<td align="right">67,665,570</td>
<td align="right">70.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,614,696</td>
<td align="right"></td>
<td align="right">28,603,337</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,133,292</td>
<td align="right">29.3%</td>
<td align="right">28,130,571</td>
<td align="right">29.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,154,430</td>
<td align="right"></td>
<td align="right">28,151,709</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,110,313</td>
<td align="right"></td>
<td align="right">1,110,313</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">98,632</td>
<td align="right">8.9%</td>
<td align="right">98,632</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">4,973</td>
<td align="right">0.4%</td>
<td align="right">4,973</td>
<td align="right">0.4%</td>
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
<td align="right">1,324</td>
<td align="right">29,513</td>
<td align="right">173,641,861</td>
<td align="right">1,390</td>
<td align="right">30,173</td>
<td align="right">178,219,999</td>
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
<td align="right">1,135</td>
<td align="right">1.0%</td>
<td align="right">5,509</td>
<td align="right">2.0%</td>
<td align="right">385.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">36,085</td>
<td align="right">32.2%</td>
<td align="right">142,862</td>
<td align="right">51.2%</td>
<td align="right">295.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">265.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">637</td>
<td align="right">0.6%</td>
<td align="right">2,008</td>
<td align="right">0.7%</td>
<td align="right">215.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">30,272</td>
<td align="right">27.0%</td>
<td align="right">82,112</td>
<td align="right">29.4%</td>
<td align="right">171.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">112,198</td>
<td align="right"></td>
<td align="right">279,240</td>
<td align="right"></td>
<td align="right">148.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">81,926</td>
<td align="right">73.0%</td>
<td align="right">197,128</td>
<td align="right">70.6%</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">966,577,709</td>
<td align="right">1,063.5%</td>
<td align="right">1,602,209,498</td>
<td align="right">1,107.7%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">90,884,524</td>
<td align="right"></td>
<td align="right">144,639,969</td>
<td align="right"></td>
<td align="right">59.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126 / 0 !!</td>
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
<td align="right">80,019</td>
<td align="right">97.7%</td>
<td align="right">193,644</td>
<td align="right">98.2%</td>
<td align="right">142.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">81,926</td>
<td align="right"></td>
<td align="right">197,128</td>
<td align="right"></td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">114.3%</td>
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
<td align="right">665</td>
<td align="right">0.3%</td>
<td align="right">665 / 0 !!</td>
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
<td align="right">11,056</td>
<td align="right">5.6%</td>
<td align="right">11,056 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">9,056</td>
<td align="right">11.1%</td>
<td align="right">15,579</td>
<td align="right">7.9%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">16,446</td>
<td align="right">20.1%</td>
<td align="right">27,674</td>
<td align="right">14.0%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">29,178</td>
<td align="right">35.6%</td>
<td align="right">72,786</td>
<td align="right">36.9%</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21,968</td>
<td align="right">26.8%</td>
<td align="right">48,347</td>
<td align="right">24.5%</td>
<td align="right">120.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,540</td>
<td align="right">5.5%</td>
<td align="right">18,330</td>
<td align="right">9.3%</td>
<td align="right">303.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">608</td>
<td align="right">0.7%</td>
<td align="right">2,998</td>
<td align="right">1.5%</td>
<td align="right">393.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">130</td>
<td align="right">0.2%</td>
<td align="right">358</td>
<td align="right">0.2%</td>
<td align="right">175.4%</td>
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
<td align="right">6,239</td>
<td align="right">7.6%</td>
<td align="right">22,747</td>
<td align="right">11.5%</td>
<td align="right">264.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">15,740</td>
<td align="right">19.2%</td>
<td align="right">18,674</td>
<td align="right">9.5%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">10,810</td>
<td align="right">13.2%</td>
<td align="right">44,732</td>
<td align="right">22.7%</td>
<td align="right">313.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">34,090</td>
<td align="right">41.6%</td>
<td align="right">71,189</td>
<td align="right">36.1%</td>
<td align="right">108.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">11,659</td>
<td align="right">14.2%</td>
<td align="right">27,773</td>
<td align="right">14.1%</td>
<td align="right">138.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,349</td>
<td align="right">1.6%</td>
<td align="right">7,915</td>
<td align="right">4.0%</td>
<td align="right">486.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">131</td>
<td align="right">0.2%</td>
<td align="right">614</td>
<td align="right">0.3%</td>
<td align="right">368.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">682</td>
<td align="right">5,152,533</td>
<td align="right">755,403.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">84</td>
<td align="right">83,186</td>
<td align="right">98,931.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">317</td>
<td align="right">135,997</td>
<td align="right">42,801.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">317</td>
<td align="right">135,997</td>
<td align="right">42,801.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">293</td>
<td align="right">99,463</td>
<td align="right">33,846.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">293</td>
<td align="right">81,903</td>
<td align="right">27,853.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">293</td>
<td align="right">81,903</td>
<td align="right">27,853.2%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">718</td>
<td align="right">194,780</td>
<td align="right">27,028.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">964</td>
<td align="right">173,721</td>
<td align="right">17,920.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">964</td>
<td align="right">173,279</td>
<td align="right">17,875.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">166,347</td>
<td align="right">8,632.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,147</td>
<td align="right">1,361,767</td>
<td align="right">7,404.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,818</td>
<td align="right">197,379</td>
<td align="right">6,904.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">116</td>
<td align="right">7,891</td>
<td align="right">6,702.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">43,179</td>
<td align="right">2,569,938</td>
<td align="right">5,851.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">43,144</td>
<td align="right">2,327,077</td>
<td align="right">5,293.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,090,880</td>
<td align="right">35,428,110</td>
<td align="right">3,147.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">150,702</td>
<td align="right">4,694,568</td>
<td align="right">3,015.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">150,702</td>
<td align="right">4,387,993</td>
<td align="right">2,811.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">345</td>
<td align="right">9,234</td>
<td align="right">2,576.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">47,892</td>
<td align="right">1,150,987</td>
<td align="right">2,303.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">26,858</td>
<td align="right">600,857</td>
<td align="right">2,137.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">26,858</td>
<td align="right">600,857</td>
<td align="right">2,137.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">221,347</td>
<td align="right">4,513,756</td>
<td align="right">1,939.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">99,024</td>
<td align="right">1,942,874</td>
<td align="right">1,862.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44</td>
<td align="right">726</td>
<td align="right">1,550.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">13,329</td>
<td align="right">198,688</td>
<td align="right">1,390.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">130</td>
<td align="right">1,810</td>
<td align="right">1,292.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,022</td>
<td align="right">13,972</td>
<td align="right">1,267.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">107,796</td>
<td align="right">1,147,973</td>
<td align="right">964.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">156,127</td>
<td align="right">1,559,708</td>
<td align="right">899.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">390,115</td>
<td align="right">3,811,093</td>
<td align="right">876.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,767</td>
<td align="right">347,661</td>
<td align="right">845.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,575</td>
<td align="right">11,973</td>
<td align="right">660.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">579,299</td>
<td align="right">4,265,031</td>
<td align="right">636.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">88,757</td>
<td align="right">642,559</td>
<td align="right">624.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,251</td>
<td align="right">523,341</td>
<td align="right">568.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,038</td>
<td align="right">236,518</td>
<td align="right">556.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">6,215</td>
<td align="right">38,087</td>
<td align="right">512.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">49,846</td>
<td align="right">304,314</td>
<td align="right">510.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">124,432</td>
<td align="right">703,628</td>
<td align="right">465.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">497,411</td>
<td align="right">2,743,940</td>
<td align="right">451.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">721,070</td>
<td align="right">3,895,998</td>
<td align="right">440.3%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,665</td>
<td align="right">67,696</td>
<td align="right">361.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">261,262</td>
<td align="right">1,112,104</td>
<td align="right">325.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">29,555</td>
<td align="right">116,793</td>
<td align="right">295.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">335,436</td>
<td align="right">1,240,572</td>
<td align="right">269.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">14,345,770</td>
<td align="right">52,511,652</td>
<td align="right">266.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">4,809,349</td>
<td align="right">17,572,752</td>
<td align="right">265.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">86,955</td>
<td align="right">314,190</td>
<td align="right">261.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">488,672</td>
<td align="right">1,680,830</td>
<td align="right">244.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">311,877</td>
<td align="right">1,041,120</td>
<td align="right">233.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,070,196</td>
<td align="right">20,141,829</td>
<td align="right">231.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">79,615</td>
<td align="right">257,349</td>
<td align="right">223.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">400,773</td>
<td align="right">1,273,268</td>
<td align="right">217.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,421,049</td>
<td align="right">17,104,315</td>
<td align="right">215.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">130,630</td>
<td align="right">215.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">129,431</td>
<td align="right">212.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">2,409,518</td>
<td align="right">7,421,357</td>
<td align="right">208.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,674,388</td>
<td align="right">5,030,187</td>
<td align="right">200.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,366,547</td>
<td align="right">6,909,491</td>
<td align="right">192.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,404,038</td>
<td align="right">4,065,200</td>
<td align="right">189.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,625,498</td>
<td align="right">7,543,590</td>
<td align="right">187.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">2,354,793</td>
<td align="right">6,742,096</td>
<td align="right">186.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">21,613</td>
<td align="right">61,638</td>
<td align="right">185.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">90,371</td>
<td align="right">254,240</td>
<td align="right">181.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,533</td>
<td align="right">290,677</td>
<td align="right">167.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,928,636</td>
<td align="right">4,553,371</td>
<td align="right">136.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,379,851</td>
<td align="right">5,529,709</td>
<td align="right">132.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,173,297</td>
<td align="right">2,524,679</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,394,684</td>
<td align="right">11,229,822</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,350,885</td>
<td align="right">2,810,338</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,442,980</td>
<td align="right">7,142,589</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,360,399</td>
<td align="right">2,782,250</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,147,516</td>
<td align="right">2,340,991</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,601,324</td>
<td align="right">3,254,395</td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,761,623</td>
<td align="right">19,695,239</td>
<td align="right">101.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,622,711</td>
<td align="right">7,246,199</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,406,733</td>
<td align="right">2,780,852</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">23,876,015</td>
<td align="right">46,982,773</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">7,717,706</td>
<td align="right">15,179,753</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,912,700</td>
<td align="right">13,235,850</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">459,596</td>
<td align="right">44,974</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">320,122</td>
<td align="right">606,737</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">49,092,671</td>
<td align="right">92,553,092</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,740,713</td>
<td align="right">5,143,058</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">186,518</td>
<td align="right">346,023</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">654,145</td>
<td align="right">1,202,391</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">120,306</td>
<td align="right">219,164</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,019,376</td>
<td align="right">5,468,054</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,148,924</td>
<td align="right">5,588,124</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">16,481,789</td>
<td align="right">28,861,020</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,439</td>
<td align="right">65,461</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,741,649</td>
<td align="right">6,470,878</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">645,844</td>
<td align="right">1,115,214</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">190</td>
<td align="right">328</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">223,903</td>
<td align="right">383,012</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">994,823</td>
<td align="right">1,680,151</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,065,348</td>
<td align="right">1,782,641</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,575,626</td>
<td align="right">2,636,001</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">520</td>
<td align="right">856</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">75,924,985</td>
<td align="right">121,583,828</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,934</td>
<td align="right">31,806</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">824</td>
<td align="right">1,314</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">90,884,524</td>
<td align="right">144,639,969</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">10,306,379</td>
<td align="right">16,245,566</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,765,938</td>
<td align="right">23,230,833</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">32,075</td>
<td align="right">50,229</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">96,179,473</td>
<td align="right">149,825,430</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">55,492,102</td>
<td align="right">86,325,764</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">341,193</td>
<td align="right">529,537</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">14,493,186</td>
<td align="right">22,431,171</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,883,145</td>
<td align="right">5,977,550</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">14,313,399</td>
<td align="right">6,720,605</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">9,351,909</td>
<td align="right">14,212,471</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,739,064</td>
<td align="right">4,127,403</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">79,905,298</td>
<td align="right">119,586,702</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,443,893</td>
<td align="right">18,478,248</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">788,019</td>
<td align="right">1,162,077</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">791,660</td>
<td align="right">1,161,764</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">465,593</td>
<td align="right">681,180</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">11,849,792</td>
<td align="right">17,333,847</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">590,379</td>
<td align="right">852,659</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">4,963</td>
<td align="right">7,141</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">1,145</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,646,902</td>
<td align="right">10,822,786</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">34,116</td>
<td align="right">47,832</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">109,033</td>
<td align="right">151,141</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,161,234</td>
<td align="right">1,578,622</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,677</td>
<td align="right">102,327</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">13,864,127</td>
<td align="right">18,422,207</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,522,634</td>
<td align="right">4,611,899</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,990,897</td>
<td align="right">5,085,556</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">61,808</td>
<td align="right">77,282</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,797,429</td>
<td align="right">3,488,927</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,283,630</td>
<td align="right">1,600,569</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,409,722</td>
<td align="right">7,941,904</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,018,724</td>
<td align="right">4,972,440</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,060,181</td>
<td align="right">7,478,181</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,664,170</td>
<td align="right">3,269,851</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,123,848</td>
<td align="right">9,848,781</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">17,837,822</td>
<td align="right">21,623,200</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">9,017</td>
<td align="right">7,112</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12,248</td>
<td align="right">14,826</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">871,701</td>
<td align="right">1,049,720</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">255,703</td>
<td align="right">307,489</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">951,307</td>
<td align="right">1,134,865</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,717,929</td>
<td align="right">5,622,791</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">34,900,246</td>
<td align="right">41,529,701</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,858,234</td>
<td align="right">5,748,974</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">6,670,452</td>
<td align="right">7,891,839</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">233</td>
<td align="right">191</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,875,227</td>
<td align="right">5,743,880</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">12,166,733</td>
<td align="right">14,158,268</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,019,602</td>
<td align="right">4,608,096</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,069,476</td>
<td align="right">1,225,571</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,139,494</td>
<td align="right">8,173,604</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">2,276,146</td>
<td align="right">2,603,239</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">134,466</td>
<td align="right">152,810</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">134,466</td>
<td align="right">152,810</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,604,783</td>
<td align="right">1,806,831</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,226,712</td>
<td align="right">2,506,904</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,382,206</td>
<td align="right">1,547,942</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,776,349</td>
<td align="right">1,987,168</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,786,773</td>
<td align="right">1,989,037</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,317,879</td>
<td align="right">1,464,281</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">561</td>
<td align="right">623</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,220,131</td>
<td align="right">1,353,759</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">416,813</td>
<td align="right">460,123</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,775,737</td>
<td align="right">7,369,228</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">39,407</td>
<td align="right">42,740</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">39,441</td>
<td align="right">42,773</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,013,341</td>
<td align="right">1,097,935</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,936,539</td>
<td align="right">12,703,013</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,956,723</td>
<td align="right">12,723,700</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">978,055</td>
<td align="right">1,040,658</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,738,248</td>
<td align="right">1,844,545</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,961,731</td>
<td align="right">2,078,002</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">488,826</td>
<td align="right">460,129</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,491,191</td>
<td align="right">4,750,260</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">9,267,017</td>
<td align="right">9,796,846</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,933,405</td>
<td align="right">6,222,817</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,796,450</td>
<td align="right">7,029,048</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,541,203</td>
<td align="right">5,719,766</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,636,216</td>
<td align="right">2,718,241</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,545</td>
<td align="right">1,264,627</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">426,849</td>
<td align="right">436,233</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,294,949</td>
<td align="right">5,185,461</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">693</td>
<td align="right">705</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">528,979</td>
<td align="right">523,545</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">187,767</td>
<td align="right">189,680</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">49,794</td>
<td align="right">50,175</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,164</td>
<td align="right">23,319</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">6,284,839</td>
<td align="right">6,297,864</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">727,440</td>
<td align="right">728,012</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">754</td>
<td align="right">754</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">401,150</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">223,862</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">165,310</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">83,089</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">78,775</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">72,305</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">36,404</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">17,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">16,130</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">13,339</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">5,314</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">2,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right"></td>
<td align="right">336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">116</td>
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
<td align="right">2</td>
<td align="right">73</td>
<td align="right">3,550.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">437</td>
<td align="right">3,762</td>
<td align="right">760.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">343</td>
<td align="right">170.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,075</td>
<td align="right">2,244</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,623</td>
<td align="right">6,409</td>
<td align="right">-3.2%</td>
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
<td align="right">15</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">15</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
