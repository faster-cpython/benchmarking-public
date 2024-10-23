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
<td align="right">761,108</td>
<td align="right">2,161,097</td>
<td align="right">183.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,015,485</td>
<td align="right">53,278,592</td>
<td align="right">131.5%</td>
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
<td align="right">4,634</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,427</td>
<td align="right">123</td>
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
<td align="right">2,611,035</td>
<td align="right">102,060</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,343,269</td>
<td align="right">96,732</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">215,365</td>
<td align="right">9,318</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,688</td>
<td align="right">373</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,664,972</td>
<td align="right">565,238</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,932,111</td>
<td align="right">517,984</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,651</td>
<td align="right">3,521</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,198,483</td>
<td align="right">257,339</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">67,336</td>
<td align="right">15,318</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">231,441</td>
<td align="right">53,726</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">506,822</td>
<td align="right">138,925</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">553,256</td>
<td align="right">152,276</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">223,694</td>
<td align="right">68,049</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,182,964</td>
<td align="right">2,914,961</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,688,858</td>
<td align="right">2,131,199</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,765,924</td>
<td align="right">938,533</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">329,925</td>
<td align="right">114,992</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">284,623</td>
<td align="right">99,266</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,532,514</td>
<td align="right">2,278,531</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">133,914</td>
<td align="right">46,967</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,760,062</td>
<td align="right">654,206</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,947,824</td>
<td align="right">2,595,784</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,943</td>
<td align="right">108,188</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">42,340,626</td>
<td align="right">16,313,249</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,550</td>
<td align="right">108,237</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">946,424</td>
<td align="right">371,736</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,242,446</td>
<td align="right">895,262</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,105,920</td>
<td align="right">445,027</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,606,123</td>
<td align="right">2,303,862</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">129,242</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,566,610</td>
<td align="right">733,439</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,316,853</td>
<td align="right">10,916,906</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,913,496</td>
<td align="right">905,117</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,076,734</td>
<td align="right">996,232</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,748,562</td>
<td align="right">4,301,820</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,685,373</td>
<td align="right">836,393</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,125,696</td>
<td align="right">584,410</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,751,996</td>
<td align="right">11,377,847</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,909,498</td>
<td align="right">1,002,443</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,082</td>
<td align="right">40,738</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">429,901</td>
<td align="right">230,765</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,569,043</td>
<td align="right">1,382,164</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">135,678,411</td>
<td align="right">77,118,683</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,838,526</td>
<td align="right">4,481,285</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,391,476</td>
<td align="right">4,877,624</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,424,712</td>
<td align="right">2,008,787</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">615,739</td>
<td align="right">362,194</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,900,494</td>
<td align="right">3,500,098</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">13,001,177</td>
<td align="right">7,722,750</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">71,392</td>
<td align="right">43,371</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,689,083</td>
<td align="right">6,559,550</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,977,848</td>
<td align="right">13,122,988</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,484,211</td>
<td align="right">2,185,003</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">913</td>
<td align="right">577</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">37,743,557</td>
<td align="right">23,909,215</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,918,275</td>
<td align="right">20,372,566</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,306,505</td>
<td align="right">2,130,628</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,473,188</td>
<td align="right">1,612,426</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,659,501</td>
<td align="right">1,105,936</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,821</td>
<td align="right">389,014</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">868,405</td>
<td align="right">583,511</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">965,578</td>
<td align="right">654,672</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,471,269</td>
<td align="right">1,677,700</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,454,712</td>
<td align="right">1,004,451</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">479,948</td>
<td align="right">333,543</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,485,985</td>
<td align="right">16,355,992</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">622,317</td>
<td align="right">433,689</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,471,374</td>
<td align="right">1,026,427</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,537,000</td>
<td align="right">3,165,879</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,898,071</td>
<td align="right">1,325,199</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">11,046</td>
<td align="right">7,716</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,252,957</td>
<td align="right">8,600,275</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,141,477</td>
<td align="right">821,876</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,882,135</td>
<td align="right">18,800,553</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,293,280</td>
<td align="right">2,408,432</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">524</td>
<td align="right">386</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,398,626</td>
<td align="right">1,032,567</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,139,332</td>
<td align="right">842,232</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,632</td>
<td align="right">49,008</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,795,100</td>
<td align="right">2,088,103</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">422,704</td>
<td align="right">316,405</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">586,011</td>
<td align="right">442,047</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,052,423</td>
<td align="right">801,675</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,540,667</td>
<td align="right">1,181,289</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,368,819</td>
<td align="right">2,603,835</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,879,472</td>
<td align="right">1,462,203</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">354,890</td>
<td align="right">276,116</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,208</td>
<td align="right">1,718</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">854,998</td>
<td align="right">675,106</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">31,278,095</td>
<td align="right">25,353,526</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">19,529,850</td>
<td align="right">15,894,907</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,391,897</td>
<td align="right">1,133,207</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">317,979</td>
<td align="right">261,585</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,042,833</td>
<td align="right">3,339,967</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">956,088</td>
<td align="right">797,641</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,620,623</td>
<td align="right">8,876,963</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">914,346</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,143,854</td>
<td align="right">995,074</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">13,516,315</td>
<td align="right">11,857,463</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,948,829</td>
<td align="right">21,361,058</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,962</td>
<td align="right">75,854</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">26,582</td>
<td align="right">24,336</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,023</td>
<td align="right">3,687</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">194,032</td>
<td align="right">177,859</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">28,952</td>
<td align="right">31,097</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,359,779</td>
<td align="right">1,450,825</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,471,007</td>
<td align="right">1,383,862</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">818,060</td>
<td align="right">862,992</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80,285</td>
<td align="right">76,400</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">36,258</td>
<td align="right">37,845</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">276,159</td>
<td align="right">265,818</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,448,428</td>
<td align="right">35,370,978</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,841,899</td>
<td align="right">1,791,045</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,125</td>
<td align="right">426,934</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">117,540</td>
<td align="right">114,966</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">957,909</td>
<td align="right">937,653</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,009</td>
<td align="right">2,048</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">486,468</td>
<td align="right">477,835</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">26,862,805</td>
<td align="right">27,284,436</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">804,130</td>
<td align="right">792,464</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,820</td>
<td align="right">56,130</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,591,452</td>
<td align="right">1,578,149</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,826,389</td>
<td align="right">1,839,998</td>
<td align="right">0.7%</td>
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
<td align="right">11,123,062</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">7,729,370</td>
<td align="right">7,740,899</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">41,671</td>
<td align="right">41,609</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">776,157</td>
<td align="right">775,299</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,450,312</td>
<td align="right">1,448,825</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">610,782</td>
<td align="right">611,382</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,081,277</td>
<td align="right">5,077,112</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4,605,120</td>
<td align="right">4,606,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">580,906</td>
<td align="right">581,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,702,081</td>
<td align="right">4,702,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">19,102,275</td>
<td align="right">19,100,733</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,585,434</td>
<td align="right">11,585,172</td>
<td align="right">-0.0%</td>
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
<td align="right">259,012</td>
<td align="right">4.2%</td>
<td align="right">-17.8%</td>
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
<td align="right">2,135</td>
<td align="right">83.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">439</td>
<td align="right">16.0%</td>
<td align="right">438</td>
<td align="right">17.0%</td>
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
<td align="right">7.2%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">91</td>
<td align="right">4.0%</td>
<td align="right">110</td>
<td align="right">5.2%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">249</td>
<td align="right">10.8%</td>
<td align="right">205</td>
<td align="right">9.6%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">156</td>
<td align="right">6.8%</td>
<td align="right">141</td>
<td align="right">6.6%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,029</td>
<td align="right">44.7%</td>
<td align="right">953</td>
<td align="right">44.6%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">144</td>
<td align="right">6.3%</td>
<td align="right">137</td>
<td align="right">6.4%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.5%</td>
<td align="right">173</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.2%</td>
<td align="right">120</td>
<td align="right">5.6%</td>
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
<td align="right">1.7%</td>
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
<td align="right">129,242</td>
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
<td align="right">1,100,536</td>
<td align="right">9.8%</td>
<td align="right">440,473</td>
<td align="right">4.2%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,116,515</td>
<td align="right">90.0%</td>
<td align="right">10,088,490</td>
<td align="right">95.6%</td>
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
<td align="right">3,129</td>
<td align="right">64.8%</td>
<td align="right">-20.9%</td>
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
<td align="right">19.6%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">636</td>
<td align="right">16.1%</td>
<td align="right">443</td>
<td align="right">14.2%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">822</td>
<td align="right">20.8%</td>
<td align="right">586</td>
<td align="right">18.7%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">776</td>
<td align="right">19.6%</td>
<td align="right">698</td>
<td align="right">22.3%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">771</td>
<td align="right">19.5%</td>
<td align="right">729</td>
<td align="right">23.3%</td>
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
<td align="right">7,078,032</td>
<td align="right">10.4%</td>
<td align="right">7,020,196</td>
<td align="right">10.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,903,682</td>
<td align="right">89.6%</td>
<td align="right">60,929,379</td>
<td align="right">89.6%</td>
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
<td align="right">164,719</td>
<td align="right">100.0%</td>
<td align="right">157,180</td>
<td align="right">100.0%</td>
<td align="right">-4.6%</td>
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
<td align="right">517,255</td>
<td align="right">99.5%</td>
<td align="right">173,743</td>
<td align="right">98.6%</td>
<td align="right">-66.4%</td>
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
<td align="right">0.3%</td>
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
<td align="right">954,006</td>
<td align="right">5.3%</td>
<td align="right">933,886</td>
<td align="right">5.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,205,289</td>
<td align="right">94.7%</td>
<td align="right">17,191,216</td>
<td align="right">94.8%</td>
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
<td align="right">2,440</td>
<td align="right">61.7%</td>
<td align="right">2,285</td>
<td align="right">60.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,515</td>
<td align="right">38.3%</td>
<td align="right">1,484</td>
<td align="right">39.4%</td>
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
<td align="right">1,013</td>
<td align="right">41.5%</td>
<td align="right">838</td>
<td align="right">36.7%</td>
<td align="right">-17.3%</td>
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
<td align="right">10.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">633</td>
<td align="right">25.9%</td>
<td align="right">634</td>
<td align="right">27.7%</td>
<td align="right">0.2%</td>
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
<td align="right">3.9%</td>
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
<td align="right">1,134,714</td>
<td align="right">21.5%</td>
<td align="right">815,967</td>
<td align="right">16.4%</td>
<td align="right">-28.1%</td>
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
<td align="right">82.9%</td>
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
<td align="right">5,201</td>
<td align="right">81.3%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,198</td>
<td align="right">16.5%</td>
<td align="right">1,198</td>
<td align="right">18.7%</td>
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
<td align="right">13.0%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">512</td>
<td align="right">8.5%</td>
<td align="right">461</td>
<td align="right">8.9%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,171</td>
<td align="right">52.4%</td>
<td align="right">2,969</td>
<td align="right">57.1%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,158</td>
<td align="right">19.1%</td>
<td align="right">1,093</td>
<td align="right">21.0%</td>
<td align="right">-5.6%</td>
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
<td align="right">1,128,084</td>
<td align="right">6.7%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,567,824</td>
<td align="right">91.7%</td>
<td align="right">15,697,339</td>
<td align="right">92.7%</td>
<td align="right">-5.3%</td>
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
<td align="right">108,252</td>
<td align="right">0.6%</td>
<td align="right">0.7%</td>
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
<td align="right">3,994</td>
<td align="right">55.8%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,133</td>
<td align="right">42.0%</td>
<td align="right">3,168</td>
<td align="right">44.2%</td>
<td align="right">1.1%</td>
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
<td align="right">23.1%</td>
<td align="right">-7.6%</td>
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
<td align="right">1,190</td>
<td align="right">29.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">444</td>
<td align="right">10.3%</td>
<td align="right">444</td>
<td align="right">11.1%</td>
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
<td align="right">8,670,336</td>
<td align="right">8.0%</td>
<td align="right">4,239,464</td>
<td align="right">4.3%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,314,212</td>
<td align="right">20.7%</td>
<td align="right">19,033,004</td>
<td align="right">19.1%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">76,867,209</td>
<td align="right">71.2%</td>
<td align="right">76,221,936</td>
<td align="right">76.6%</td>
<td align="right">-0.8%</td>
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
<td align="right">11,081</td>
<td align="right">2.7%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479,833</td>
<td align="right">96.9%</td>
<td align="right">406,472</td>
<td align="right">97.3%</td>
<td align="right">-15.3%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">1.1%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">22</td>
<td align="right">0.2%</td>
<td align="right">-47.6%</td>
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
<td align="left">class attr simple</td>
<td align="right">1,241</td>
<td align="right">8.0%</td>
<td align="right">841</td>
<td align="right">7.6%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,903</td>
<td align="right">31.7%</td>
<td align="right">3,501</td>
<td align="right">31.6%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,583</td>
<td align="right">10.2%</td>
<td align="right">1,167</td>
<td align="right">10.5%</td>
<td align="right">-26.3%</td>
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
<td align="right">774</td>
<td align="right">7.0%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">835</td>
<td align="right">5.4%</td>
<td align="right">793</td>
<td align="right">7.2%</td>
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
<td align="right">42,725,954</td>
<td align="right">99.9%</td>
<td align="right">24,714,802</td>
<td align="right">99.9%</td>
<td align="right">-42.2%</td>
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
<td align="right">251,615</td>
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
<td align="right">1,116,110</td>
<td align="right">8.8%</td>
<td align="right">-43.1%</td>
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
<td align="right">11,354,488</td>
<td align="right">89.2%</td>
<td align="right">4.9%</td>
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
<td align="right">1,198</td>
<td align="right">4.5%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,439</td>
<td align="right">94.3%</td>
<td align="right">25,496</td>
<td align="right">95.5%</td>
<td align="right">-38.5%</td>
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
<td align="right">8.3%</td>
<td align="right">-23.3%</td>
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
<td align="left">not in keys</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">54</td>
<td align="right">4.5%</td>
<td align="right">12.5%</td>
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
<td align="right">33.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">9.1%</td>
<td align="right">230</td>
<td align="right">19.2%</td>
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
<td align="right">128,878</td>
<td align="right">0.4%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,138,062</td>
<td align="right">2.8%</td>
<td align="right">1,250,078</td>
<td align="right">3.4%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,726,745</td>
<td align="right">95.9%</td>
<td align="right">35,243,818</td>
<td align="right">96.2%</td>
<td align="right">-9.0%</td>
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
<td align="right">2,586</td>
<td align="right">7.8%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,651</td>
<td align="right">73.4%</td>
<td align="right">30,759</td>
<td align="right">92.2%</td>
<td align="right">7.4%</td>
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
<td align="right">370</td>
<td align="right">14.3%</td>
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
<td align="right">15.2%</td>
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
<td align="right">22.6%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">871</td>
<td align="right">8.4%</td>
<td align="right">829</td>
<td align="right">32.1%</td>
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
<td align="right">7,960,257</td>
<td align="right">100.0%</td>
<td align="right">7,934,533</td>
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
<td align="right">283,032,988</td>
<td align="right">32.7%</td>
<td align="right">160,210,841</td>
<td align="right">25.6%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">22,287,901</td>
<td align="right">2.6%</td>
<td align="right">15,052,934</td>
<td align="right">2.4%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">526,289,351</td>
<td align="right">60.9%</td>
<td align="right">422,221,378</td>
<td align="right">67.4%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">33,165,068</td>
<td align="right">3.8%</td>
<td align="right">28,749,702</td>
<td align="right">4.6%</td>
<td align="right">-13.3%</td>
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
<td align="right">251,615</td>
<td align="right">1.7%</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">488,984</td>
<td align="right">2.2%</td>
<td align="right">128,878</td>
<td align="right">0.9%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,100,536</td>
<td align="right">5.0%</td>
<td align="right">440,473</td>
<td align="right">3.0%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">1.3%</td>
<td align="right">129,242</td>
<td align="right">0.9%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,670,336</td>
<td align="right">39.2%</td>
<td align="right">4,239,464</td>
<td align="right">28.4%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,134,714</td>
<td align="right">5.1%</td>
<td align="right">815,967</td>
<td align="right">5.5%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,386,447</td>
<td align="right">6.3%</td>
<td align="right">1,128,084</td>
<td align="right">7.6%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">315,240</td>
<td align="right">1.4%</td>
<td align="right">259,012</td>
<td align="right">1.7%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">954,006</td>
<td align="right">4.3%</td>
<td align="right">933,886</td>
<td align="right">6.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,492,134</td>
<td align="right">29.4%</td>
<td align="right">6,492,134</td>
<td align="right">43.5%</td>
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
<td align="right">643,792</td>
<td align="right">1.9%</td>
<td align="right">320,499</td>
<td align="right">1.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,209,932</td>
<td align="right">9.7%</td>
<td align="right">1,807,842</td>
<td align="right">6.3%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,959,972</td>
<td align="right">5.9%</td>
<td align="right">1,115,994</td>
<td align="right">3.9%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">753,124</td>
<td align="right">2.3%</td>
<td align="right">968,778</td>
<td align="right">3.4%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,191,059</td>
<td align="right">15.7%</td>
<td align="right">4,163,733</td>
<td align="right">14.5%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,743,114</td>
<td align="right">35.4%</td>
<td align="right">11,150,016</td>
<td align="right">38.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,462,199</td>
<td align="right">4.4%</td>
<td align="right">1,525,956</td>
<td align="right">5.3%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,265,471</td>
<td align="right">3.8%</td>
<td align="right">1,238,991</td>
<td align="right">4.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,077,660</td>
<td align="right">15.3%</td>
<td align="right">5,100,695</td>
<td align="right">17.7%</td>
<td align="right">0.5%</td>
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
<td align="right">1.4%</td>
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
<td align="right">1,277,688</td>
<td align="right">1.8%</td>
<td align="right">1,276,213</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,502,264</td>
<td align="right">7.9%</td>
<td align="right">5,501,637</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">12,053,479</td>
<td align="right">17.4%</td>
<td align="right">12,052,686</td>
<td align="right">17.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">12,053,479</td>
<td align="right">17.4%</td>
<td align="right">12,052,686</td>
<td align="right">17.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,550,069</td>
<td align="right">9.4%</td>
<td align="right">6,549,903</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,551,215</td>
<td align="right">9.4%</td>
<td align="right">6,551,049</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">392,011</td>
<td align="right">0.6%</td>
<td align="right">392,014</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,800,321</td>
<td align="right">68.9%</td>
<td align="right">47,800,496</td>
<td align="right">68.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,342,012</td>
<td align="right">82.6%</td>
<td align="right">57,341,953</td>
<td align="right">82.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">480,082,197</td>
<td align="right">39.6%</td>
<td align="right">640,134,842</td>
<td align="right">50.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">363,399</td>
<td align="right">0.4%</td>
<td align="right">476,956</td>
<td align="right">0.5%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">456,579,889</td>
<td align="right">35.2%</td>
<td align="right">591,560,934</td>
<td align="right">42.3%</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">147,808,955</td>
<td align="right">12.2%</td>
<td align="right">110,448,523</td>
<td align="right">8.7%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">222,830,594</td>
<td align="right">17.2%</td>
<td align="right">277,016,681</td>
<td align="right">19.8%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">363,804,494</td>
<td align="right">30.0%</td>
<td align="right">277,715,953</td>
<td align="right">21.9%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">149,418,139</td>
<td align="right">11.5%</td>
<td align="right">121,745,982</td>
<td align="right">8.7%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">469,305,820</td>
<td align="right">36.2%</td>
<td align="right">408,494,668</td>
<td align="right">29.2%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">220,651,058</td>
<td align="right">18.2%</td>
<td align="right">240,637,517</td>
<td align="right">19.0%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,385,220</td>
<td align="right"></td>
<td align="right">48,711,567</td>
<td align="right"></td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">310,114</td>
<td align="right"></td>
<td align="right">331,788</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,507,360</td>
<td align="right"></td>
<td align="right">1,423,200</td>
<td align="right"></td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,815,639</td>
<td align="right"></td>
<td align="right">1,753,113</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,766</td>
<td align="right">0.0%</td>
<td align="right">39,575</td>
<td align="right">0.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">66,709,799</td>
<td align="right"></td>
<td align="right">66,921,480</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">67,990,192</td>
<td align="right">70.7%</td>
<td align="right">68,198,814</td>
<td align="right">70.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,615,609</td>
<td align="right"></td>
<td align="right">28,537,025</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,588,027</td>
<td align="right">70.3%</td>
<td align="right">67,682,283</td>
<td align="right">70.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,133,289</td>
<td align="right">29.3%</td>
<td align="right">28,131,598</td>
<td align="right">29.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,154,427</td>
<td align="right"></td>
<td align="right">28,152,736</td>
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
<td align="right">173,642,103</td>
<td align="right">1,379</td>
<td align="right">30,226</td>
<td align="right">177,776,162</td>
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
<td align="right">7,740</td>
<td align="right">2.2%</td>
<td align="right">581.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">36,087</td>
<td align="right">32.2%</td>
<td align="right">173,393</td>
<td align="right">48.9%</td>
<td align="right">380.5%</td>
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
<td align="right">2,551</td>
<td align="right">0.7%</td>
<td align="right">300.5%</td>
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
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">252.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">81,950</td>
<td align="right">73.0%</td>
<td align="right">265,031</td>
<td align="right">74.8%</td>
<td align="right">223.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">112,235</td>
<td align="right"></td>
<td align="right">354,323</td>
<td align="right"></td>
<td align="right">215.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">30,285</td>
<td align="right">27.0%</td>
<td align="right">89,292</td>
<td align="right">25.2%</td>
<td align="right">194.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">966,587,437</td>
<td align="right">1,063.4%</td>
<td align="right">1,571,595,969</td>
<td align="right">1,117.3%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">90,892,513</td>
<td align="right"></td>
<td align="right">140,656,953</td>
<td align="right"></td>
<td align="right">54.8%</td>
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
<td align="right">80,044</td>
<td align="right">97.7%</td>
<td align="right">260,346</td>
<td align="right">98.2%</td>
<td align="right">225.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">81,950</td>
<td align="right"></td>
<td align="right">265,031</td>
<td align="right"></td>
<td align="right">223.4%</td>
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
<td align="right">742</td>
<td align="right">0.3%</td>
<td align="right">742 / 0 !!</td>
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
<td align="right">18,548</td>
<td align="right">7.0%</td>
<td align="right">18,548 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">9,062</td>
<td align="right">11.1%</td>
<td align="right">19,590</td>
<td align="right">7.4%</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">16,446</td>
<td align="right">20.1%</td>
<td align="right">35,795</td>
<td align="right">13.5%</td>
<td align="right">117.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">29,188</td>
<td align="right">35.6%</td>
<td align="right">97,438</td>
<td align="right">36.8%</td>
<td align="right">233.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21,975</td>
<td align="right">26.8%</td>
<td align="right">64,871</td>
<td align="right">24.5%</td>
<td align="right">195.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,541</td>
<td align="right">5.5%</td>
<td align="right">24,056</td>
<td align="right">9.1%</td>
<td align="right">429.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">608</td>
<td align="right">0.7%</td>
<td align="right">3,882</td>
<td align="right">1.5%</td>
<td align="right">538.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">130</td>
<td align="right">0.2%</td>
<td align="right">851</td>
<td align="right">0.3%</td>
<td align="right">554.6%</td>
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
<td align="right">6,241</td>
<td align="right">7.6%</td>
<td align="right">32,740</td>
<td align="right">12.4%</td>
<td align="right">424.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">15,747</td>
<td align="right">19.2%</td>
<td align="right">25,805</td>
<td align="right">9.7%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">10,806</td>
<td align="right">13.2%</td>
<td align="right">58,101</td>
<td align="right">21.9%</td>
<td align="right">437.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">34,107</td>
<td align="right">41.6%</td>
<td align="right">94,795</td>
<td align="right">35.8%</td>
<td align="right">177.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">11,662</td>
<td align="right">14.2%</td>
<td align="right">37,171</td>
<td align="right">14.0%</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,349</td>
<td align="right">1.6%</td>
<td align="right">10,539</td>
<td align="right">4.0%</td>
<td align="right">681.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">131</td>
<td align="right">0.2%</td>
<td align="right">1,195</td>
<td align="right">0.5%</td>
<td align="right">812.2%</td>
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
<td align="right">5,100,416</td>
<td align="right">747,761.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">84</td>
<td align="right">82,991</td>
<td align="right">98,698.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">317</td>
<td align="right">136,210</td>
<td align="right">42,868.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">317</td>
<td align="right">136,210</td>
<td align="right">42,868.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">293</td>
<td align="right">99,817</td>
<td align="right">33,967.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">293</td>
<td align="right">82,257</td>
<td align="right">27,974.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">293</td>
<td align="right">82,257</td>
<td align="right">27,974.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">718</td>
<td align="right">194,525</td>
<td align="right">26,992.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">964</td>
<td align="right">173,719</td>
<td align="right">17,920.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">964</td>
<td align="right">173,277</td>
<td align="right">17,874.8%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">166,347</td>
<td align="right">8,632.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,818</td>
<td align="right">197,209</td>
<td align="right">6,898.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,147</td>
<td align="right">1,254,525</td>
<td align="right">6,813.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">116</td>
<td align="right">7,891</td>
<td align="right">6,702.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">43,178</td>
<td align="right">2,571,743</td>
<td align="right">5,856.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">43,143</td>
<td align="right">2,328,929</td>
<td align="right">5,298.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,022</td>
<td align="right">48,773</td>
<td align="right">4,672.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,090,880</td>
<td align="right">34,853,932</td>
<td align="right">3,095.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">150,694</td>
<td align="right">4,515,898</td>
<td align="right">2,896.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">150,694</td>
<td align="right">4,190,180</td>
<td align="right">2,680.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">345</td>
<td align="right">8,453</td>
<td align="right">2,350.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">47,892</td>
<td align="right">1,155,568</td>
<td align="right">2,312.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">26,857</td>
<td align="right">601,545</td>
<td align="right">2,139.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">26,857</td>
<td align="right">601,545</td>
<td align="right">2,139.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">221,348</td>
<td align="right">4,466,731</td>
<td align="right">1,918.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">99,022</td>
<td align="right">1,926,413</td>
<td align="right">1,845.4%</td>
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
<td align="right">198,686</td>
<td align="right">1,390.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">130</td>
<td align="right">1,810</td>
<td align="right">1,292.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">390,116</td>
<td align="right">3,804,243</td>
<td align="right">875.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,766</td>
<td align="right">347,672</td>
<td align="right">845.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">156,117</td>
<td align="right">1,440,423</td>
<td align="right">822.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">106,664</td>
<td align="right">980,685</td>
<td align="right">819.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,575</td>
<td align="right">11,766</td>
<td align="right">647.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">579,299</td>
<td align="right">4,265,028</td>
<td align="right">636.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">88,755</td>
<td align="right">642,320</td>
<td align="right">623.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,250</td>
<td align="right">523,197</td>
<td align="right">568.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,037</td>
<td align="right">235,173</td>
<td align="right">552.6%</td>
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
<td align="right">303,857</td>
<td align="right">509.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">124,432</td>
<td align="right">697,304</td>
<td align="right">460.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">497,411</td>
<td align="right">2,743,948</td>
<td align="right">451.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">721,064</td>
<td align="right">3,956,382</td>
<td align="right">448.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,665</td>
<td align="right">66,683</td>
<td align="right">354.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">261,262</td>
<td align="right">1,110,242</td>
<td align="right">325.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">29,555</td>
<td align="right">116,700</td>
<td align="right">294.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">2,409,437</td>
<td align="right">9,513,575</td>
<td align="right">294.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">335,433</td>
<td align="right">1,230,552</td>
<td align="right">266.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">86,956</td>
<td align="right">313,765</td>
<td align="right">260.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">2,354,642</td>
<td align="right">8,487,802</td>
<td align="right">260.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">14,346,835</td>
<td align="right">51,249,583</td>
<td align="right">257.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">4,809,046</td>
<td align="right">17,056,282</td>
<td align="right">254.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">488,671</td>
<td align="right">1,675,550</td>
<td align="right">242.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,404,044</td>
<td align="right">4,733,883</td>
<td align="right">237.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">311,877</td>
<td align="right">1,037,242</td>
<td align="right">232.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">79,610</td>
<td align="right">257,353</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">130,839</td>
<td align="right">215.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">400,772</td>
<td align="right">1,261,535</td>
<td align="right">214.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">129,640</td>
<td align="right">212.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,421,059</td>
<td align="right">16,795,879</td>
<td align="right">209.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,069,935</td>
<td align="right">18,565,078</td>
<td align="right">205.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,673,920</td>
<td align="right">5,033,539</td>
<td align="right">200.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,366,538</td>
<td align="right">6,907,698</td>
<td align="right">191.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,625,489</td>
<td align="right">7,541,143</td>
<td align="right">187.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">21,613</td>
<td align="right">61,169</td>
<td align="right">183.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">90,371</td>
<td align="right">252,536</td>
<td align="right">179.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,928,590</td>
<td align="right">5,162,258</td>
<td align="right">167.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,533</td>
<td align="right">288,428</td>
<td align="right">165.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,622,645</td>
<td align="right">8,002,478</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,379,706</td>
<td align="right">5,131,070</td>
<td align="right">115.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,173,254</td>
<td align="right">2,520,660</td>
<td align="right">114.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,350,905</td>
<td align="right">2,815,356</td>
<td align="right">108.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,443,027</td>
<td align="right">7,095,712</td>
<td align="right">106.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,360,395</td>
<td align="right">2,772,378</td>
<td align="right">103.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">645,840</td>
<td align="right">1,315,671</td>
<td align="right">103.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,601,305</td>
<td align="right">3,260,157</td>
<td align="right">103.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,761,633</td>
<td align="right">19,532,971</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,406,722</td>
<td align="right">2,777,846</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,393,528</td>
<td align="right">10,545,346</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">7,717,679</td>
<td align="right">14,988,043</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">23,875,599</td>
<td align="right">46,288,059</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">459,596</td>
<td align="right">39,682</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">320,121</td>
<td align="right">605,015</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">49,094,932</td>
<td align="right">92,698,942</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,913,048</td>
<td align="right">13,038,479</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,740,712</td>
<td align="right">5,141,108</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">186,518</td>
<td align="right">346,022</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">654,141</td>
<td align="right">1,195,433</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">120,247</td>
<td align="right">214,446</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,438</td>
<td align="right">65,459</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">16,481,627</td>
<td align="right">28,755,481</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">207</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,148,919</td>
<td align="right">5,468,615</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">994,821</td>
<td align="right">1,722,582</td>
<td align="right">73.2%</td>
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
<td align="right">382,350</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,741,644</td>
<td align="right">6,377,824</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,147,498</td>
<td align="right">1,928,587</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,575,619</td>
<td align="right">2,628,119</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,065,346</td>
<td align="right">1,772,343</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">520</td>
<td align="right">856</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,761,380</td>
<td align="right">23,719,975</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">824</td>
<td align="right">1,314</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,934</td>
<td align="right">31,600</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">75,934,132</td>
<td align="right">119,210,370</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">341,192</td>
<td align="right">529,140</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">90,892,513</td>
<td align="right">140,656,953</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">14,314,668</td>
<td align="right">6,579,240</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">55,491,232</td>
<td align="right">84,728,789</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,883,104</td>
<td align="right">5,905,331</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,019,385</td>
<td align="right">4,570,510</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">96,186,533</td>
<td align="right">145,036,659</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">32,075</td>
<td align="right">48,248</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">590,379</td>
<td align="right">879,101</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">791,654</td>
<td align="right">1,161,010</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">9,351,960</td>
<td align="right">13,709,652</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">465,593</td>
<td align="right">680,526</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">787,893</td>
<td align="right">1,150,206</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">79,903,768</td>
<td align="right">116,120,456</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">4,963</td>
<td align="right">7,209</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,442,726</td>
<td align="right">17,794,223</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">11,848,625</td>
<td align="right">16,623,537</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,646,404</td>
<td align="right">10,712,775</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">10,310,482</td>
<td align="right">14,433,501</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">34,116</td>
<td align="right">47,419</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,161,234</td>
<td align="right">1,578,506</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,677</td>
<td align="right">102,622</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">13,864,152</td>
<td align="right">18,785,587</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">109,147</td>
<td align="right">145,716</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,522,173</td>
<td align="right">4,558,942</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">14,493,141</td>
<td align="right">18,752,001</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">6,670,450</td>
<td align="right">8,607,782</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,219,668</td>
<td align="right">874,309</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">61,808</td>
<td align="right">77,282</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,797,432</td>
<td align="right">3,485,526</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,409,692</td>
<td align="right">7,929,369</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,060,185</td>
<td align="right">7,476,110</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,717,464</td>
<td align="right">5,817,393</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,990,930</td>
<td align="right">4,906,704</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,018,262</td>
<td align="right">4,929,846</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,663,711</td>
<td align="right">3,261,340</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12,248</td>
<td align="right">14,822</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">871,701</td>
<td align="right">1,049,717</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">255,703</td>
<td align="right">307,711</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,122,856</td>
<td align="right">9,709,246</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">34,899,269</td>
<td align="right">41,348,639</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,858,224</td>
<td align="right">5,743,077</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">233</td>
<td align="right">191</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,875,213</td>
<td align="right">5,738,922</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,294,020</td>
<td align="right">4,379,706</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">951,280</td>
<td align="right">1,113,399</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">12,166,138</td>
<td align="right">14,056,818</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">488,774</td>
<td align="right">412,835</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,739,064</td>
<td align="right">3,155,230</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,069,476</td>
<td align="right">1,225,574</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,019,578</td>
<td align="right">4,593,588</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,776,354</td>
<td align="right">1,522,774</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">2,275,682</td>
<td align="right">2,593,508</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,138,913</td>
<td align="right">8,135,868</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,283,606</td>
<td align="right">1,460,936</td>
<td align="right">13.8%</td>
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
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">17,837,897</td>
<td align="right">20,167,376</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">9,017</td>
<td align="right">10,167</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,226,701</td>
<td align="right">2,497,536</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,317,879</td>
<td align="right">1,464,284</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">561</td>
<td align="right">623</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">416,813</td>
<td align="right">460,122</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,604,776</td>
<td align="right">1,752,744</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,775,703</td>
<td align="right">7,361,968</td>
<td align="right">8.7%</td>
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
<td align="right">1,097,600</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,786,766</td>
<td align="right">1,935,083</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">978,055</td>
<td align="right">1,039,719</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,738,248</td>
<td align="right">1,844,547</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,961,727</td>
<td align="right">2,078,002</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,936,066</td>
<td align="right">12,641,912</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,956,250</td>
<td align="right">12,659,027</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,382,210</td>
<td align="right">1,462,960</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,491,191</td>
<td align="right">4,749,548</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">693</td>
<td align="right">732</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">9,266,541</td>
<td align="right">9,743,006</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,933,399</td>
<td align="right">6,211,895</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,795,972</td>
<td align="right">7,020,996</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">49,794</td>
<td align="right">48,207</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,541,194</td>
<td align="right">5,715,170</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,636,085</td>
<td align="right">2,712,305</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">426,849</td>
<td align="right">436,875</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,545</td>
<td align="right">1,264,627</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">528,879</td>
<td align="right">517,350</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">187,765</td>
<td align="right">185,620</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,164</td>
<td align="right">23,322</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">6,284,834</td>
<td align="right">6,308,233</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">727,434</td>
<td align="right">725,557</td>
<td align="right">-0.3%</td>
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
<td align="right">400,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">223,858</td>
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
<td align="right">82,894</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">78,774</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">72,304</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">36,344</td>
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
<td align="right">13,948</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">5,315</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">4,176</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">2,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">1,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right"></td>
<td align="right">336</td>
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
<td align="right">91</td>
<td align="right">4,450.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">437</td>
<td align="right">5,045</td>
<td align="right">1,054.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">125</td>
<td align="right">921</td>
<td align="right">636.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,075</td>
<td align="right">2,687</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,633</td>
<td align="right">8,383</td>
<td align="right">26.4%</td>
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
Stats gathered on: 2024-10-23
