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
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,877,380</td>
<td align="right">8,756,058</td>
<td align="right">125.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,321,665</td>
<td align="right">1,808</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,294,052</td>
<td align="right">21,376</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,648</td>
<td align="right">1,855</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">607,168</td>
<td align="right">5,635</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,321,415</td>
<td align="right">42,267</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,475,877</td>
<td align="right">201,767</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,860,468</td>
<td align="right">538,193</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">71,105</td>
<td align="right">2,135</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,246,984</td>
<td align="right">271,020</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,608,579</td>
<td align="right">214,553</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,063,570</td>
<td align="right">84,871</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,838,888</td>
<td align="right">199,508</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">52,556</td>
<td align="right">2,337</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,219,143</td>
<td align="right">118,278</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,180</td>
<td align="right">70,662</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,991</td>
<td align="right">13,589</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,057,626</td>
<td align="right">82,870</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,405,519</td>
<td align="right">3,031,398</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,553</td>
<td align="right">38,772</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,838,116</td>
<td align="right">1,018,219</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">16,859</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">74,150</td>
<td align="right">9,591</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">136,866,753</td>
<td align="right">21,941,719</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,779,619</td>
<td align="right">292,788</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,748,949</td>
<td align="right">995,345</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,096,618</td>
<td align="right">1,967,083</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">39,954</td>
<td align="right">7,491</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,213,020</td>
<td align="right">166,742,001</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,196,310</td>
<td align="right">256,657</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,203</td>
<td align="right">259</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">105,008,446</td>
<td align="right">22,917,613</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,204,809</td>
<td align="right">4,842,976</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">11,370,817</td>
<td align="right">3,039,803</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,116,460</td>
<td align="right">838,037</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,750</td>
<td align="right">19,946</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,856,125</td>
<td align="right">1,085,999</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,281,745</td>
<td align="right">372,030</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,210,870</td>
<td align="right">1,934,290</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">237</td>
<td align="right">78</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,415,693</td>
<td align="right">16,770,749</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,836,503</td>
<td align="right">6,004,908</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,346,133</td>
<td align="right">491,412</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,512,667</td>
<td align="right">1,020,158</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,625,614</td>
<td align="right">7,849,094</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">468,007</td>
<td align="right">199,741</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,504,356</td>
<td align="right">7,071,044</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,054,571</td>
<td align="right">452,818</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">71,172,288</td>
<td align="right">31,717,146</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">30,730</td>
<td align="right">13,706</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">123,591</td>
<td align="right">55,565</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,090,456</td>
<td align="right">62,816,879</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">120</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">539,730</td>
<td align="right">256,957</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,921,853</td>
<td align="right">5,349,037</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,255,868</td>
<td align="right">616,175</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">17,740,030</td>
<td align="right">8,704,632</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">622,694</td>
<td align="right">306,209</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,892,267</td>
<td align="right">1,435,350</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">472,845,187</td>
<td align="right">235,700,222</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,264,046</td>
<td align="right">3,177,365</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,992,349</td>
<td align="right">13,449,820</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">106,409</td>
<td align="right">55,079</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">32,807,368</td>
<td align="right">17,344,584</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,312</td>
<td align="right">395,093</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">138,823,332</td>
<td align="right">73,678,989</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">995,246</td>
<td align="right">535,706</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,048,992</td>
<td align="right">21,166,036</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">397,222</td>
<td align="right">218,821</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,602,296</td>
<td align="right">883,196</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">5,311,263</td>
<td align="right">2,974,315</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,314,336</td>
<td align="right">740,711</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">158,288,997</td>
<td align="right">90,195,405</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,920,464</td>
<td align="right">17,820,432</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,946,315</td>
<td align="right">1,130,433</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,497,264</td>
<td align="right">880,937</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,360,897</td>
<td align="right">66,704,101</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,289,630</td>
<td align="right">2,535,871</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,548</td>
<td align="right">38,962</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,424,386</td>
<td align="right">58,170,215</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,304,251</td>
<td align="right">11,639,673</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,190</td>
<td align="right">1,944</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">713,312</td>
<td align="right">984,213</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,937</td>
<td align="right">470,911</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,314</td>
<td align="right">11,691</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,741,040</td>
<td align="right">7,651,638</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">34,558,970</td>
<td align="right">22,554,891</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,477,784</td>
<td align="right">16,779,544</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,155,045</td>
<td align="right">5,386,676</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">13,250,943</td>
<td align="right">8,792,039</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,549,727</td>
<td align="right">26,938,921</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,671,877</td>
<td align="right">9,100,793</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,729</td>
<td align="right">5,244</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">385,805</td>
<td align="right">261,798</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">255,756</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,963,245</td>
<td align="right">1,357,218</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,289,652</td>
<td align="right">8,547,838</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">316</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,528,362</td>
<td align="right">10,994,804</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,949,693</td>
<td align="right">10,608,473</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,010</td>
<td align="right">12,181</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,342</td>
<td align="right">5,267</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,820,452</td>
<td align="right">2,031,845</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">529</td>
<td align="right">398</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,026,977</td>
<td align="right">6,264,764</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25,658,727</td>
<td align="right">20,185,083</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">81</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,603,489</td>
<td align="right">2,071,825</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,240,524</td>
<td align="right">37,329,257</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,583</td>
<td align="right">2,111</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">178,365</td>
<td align="right">210,654</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,026,951</td>
<td align="right">19,856,025</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,136</td>
<td align="right">548,863</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,136</td>
<td align="right">548,863</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,136</td>
<td align="right">548,863</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,448,141</td>
<td align="right">16,412,120</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,699,828</td>
<td align="right">14,230,943</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,737,018</td>
<td align="right">20,269,380</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">42,948,813</td>
<td align="right">36,675,011</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,991,681</td>
<td align="right">3,428,209</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,834,629</td>
<td align="right">38,577,582</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,068</td>
<td align="right">7,889</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,803,059</td>
<td align="right">2,450,395</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">8,505,662</td>
<td align="right">7,494,035</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,231,090</td>
<td align="right">5,513,824</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">10,366,804</td>
<td align="right">9,239,993</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,135</td>
<td align="right">74,231</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">9,688,459</td>
<td align="right">8,760,536</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">963</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,462,544</td>
<td align="right">4,144,589</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,494,793</td>
<td align="right">16,404,979</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,133</td>
<td align="right">162,125</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,593,759</td>
<td align="right">20,458,135</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">35,576,566</td>
<td align="right">33,779,004</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,040,233</td>
<td align="right">16,838,941</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,444,211</td>
<td align="right">93,047,096</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,687</td>
<td align="right">615,762</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">137,231,849</td>
<td align="right">131,572,402</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">259,523</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,125,048</td>
<td align="right">1,089,186</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,332</td>
<td align="right">161,187</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,310,958</td>
<td align="right">32,719,118</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,570</td>
<td align="right">21,594,298</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">88,122</td>
<td align="right">86,634</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">176,758</td>
<td align="right">173,782</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">176,760</td>
<td align="right">173,784</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,621,460</td>
<td align="right">1,594,930</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">43,804,714</td>
<td align="right">43,103,534</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,247</td>
<td align="right">1,233,640</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,960,187</td>
<td align="right">3,929,193</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,115</td>
<td align="right">18,058</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,726,966</td>
<td align="right">3,715,695</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,213</td>
<td align="right">24,172</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">1,443</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7,373</td>
<td align="right">7,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,595</td>
<td align="right">3,595</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,962</td>
<td align="right">2,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,385,686</td>
<td align="right">37.7%</td>
<td align="right">12,112,838</td>
<td align="right">37.4%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">23,717,192</td>
<td align="right">62.2%</td>
<td align="right">20,251,952</td>
<td align="right">62.5%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">18,557</td>
<td align="right">93.6%</td>
<td align="right">16,158</td>
<td align="right">92.7%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,269</td>
<td align="right">6.4%</td>
<td align="right">1,270</td>
<td align="right">7.3%</td>
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
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">44</td>
<td align="right">0.3%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">358</td>
<td align="right">1.9%</td>
<td align="right">270</td>
<td align="right">1.7%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,210</td>
<td align="right">6.5%</td>
<td align="right">936</td>
<td align="right">5.8%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.3%</td>
<td align="right">772</td>
<td align="right">4.8%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,290</td>
<td align="right">7.0%</td>
<td align="right">1,043</td>
<td align="right">6.5%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,330</td>
<td align="right">12.6%</td>
<td align="right">1,887</td>
<td align="right">11.7%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">2,644</td>
<td align="right">14.2%</td>
<td align="right">2,192</td>
<td align="right">13.6%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">693</td>
<td align="right">3.7%</td>
<td align="right">602</td>
<td align="right">3.7%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">571</td>
<td align="right">3.1%</td>
<td align="right">503</td>
<td align="right">3.1%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">675</td>
<td align="right">3.6%</td>
<td align="right">606</td>
<td align="right">3.8%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">973</td>
<td align="right">5.2%</td>
<td align="right">908</td>
<td align="right">5.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.9%</td>
<td align="right">1,018</td>
<td align="right">6.3%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,875</td>
<td align="right">15.5%</td>
<td align="right">2,782</td>
<td align="right">17.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">154</td>
<td align="right">1.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">210</td>
<td align="right">1.1%</td>
<td align="right">211</td>
<td align="right">1.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">2,223</td>
<td align="right">13.8%</td>
<td align="right">-0.1%</td>
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
<td align="right">7,342</td>
<td align="right">100.0%</td>
<td align="right">5,267</td>
<td align="right">100.0%</td>
<td align="right">-28.3%</td>
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
<td align="right">9,246</td>
<td align="right">0.0%</td>
<td align="right">3,471</td>
<td align="right">0.0%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,815,831</td>
<td align="right">7.9%</td>
<td align="right">2,027,564</td>
<td align="right">6.8%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,776,087</td>
<td align="right">92.1%</td>
<td align="right">27,645,431</td>
<td align="right">93.1%</td>
<td align="right">-15.7%</td>
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
<td align="right">950</td>
<td align="right">19.8%</td>
<td align="right">824</td>
<td align="right">19.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,843</td>
<td align="right">80.2%</td>
<td align="right">3,503</td>
<td align="right">81.0%</td>
<td align="right">-8.8%</td>
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
<td align="left">buffer int</td>
<td align="right">142</td>
<td align="right">3.7%</td>
<td align="right">99</td>
<td align="right">2.8%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">273</td>
<td align="right">7.1%</td>
<td align="right">205</td>
<td align="right">5.9%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">688</td>
<td align="right">17.9%</td>
<td align="right">594</td>
<td align="right">17.0%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">338</td>
<td align="right">8.8%</td>
<td align="right">315</td>
<td align="right">9.0%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,401</td>
<td align="right">62.5%</td>
<td align="right">2,289</td>
<td align="right">65.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,128</td>
<td align="right">0.0%</td>
<td align="right">6,096</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,063,358</td>
<td align="right">7.2%</td>
<td align="right">21,570,828</td>
<td align="right">7.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">297,479,404</td>
<td align="right">92.8%</td>
<td align="right">281,542,573</td>
<td align="right">92.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,447</td>
<td align="right">0.0%</td>
<td align="right">8,436</td>
<td align="right">0.0%</td>
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
<td align="right">451,767</td>
<td align="right">100.0%</td>
<td align="right">423,472</td>
<td align="right">100.0%</td>
<td align="right">-6.3%</td>
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
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,619</td>
<td align="right">64.5%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">399</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.8%</td>
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
<td align="right">19,269,480</td>
<td align="right">27.3%</td>
<td align="right">11,612,682</td>
<td align="right">19.8%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">376,230</td>
<td align="right">0.5%</td>
<td align="right">318,460</td>
<td align="right">0.5%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,022,849</td>
<td align="right">72.2%</td>
<td align="right">46,802,925</td>
<td align="right">79.6%</td>
<td align="right">-8.3%</td>
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
<td align="right">33,579</td>
<td align="right">80.3%</td>
<td align="right">25,913</td>
<td align="right">78.6%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,235</td>
<td align="right">19.7%</td>
<td align="right">7,040</td>
<td align="right">21.4%</td>
<td align="right">-14.5%</td>
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
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">51</td>
<td align="right">0.2%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,125</td>
<td align="right">9.3%</td>
<td align="right">1,695</td>
<td align="right">6.5%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">12,908</td>
<td align="right">38.4%</td>
<td align="right">9,019</td>
<td align="right">34.8%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,096</td>
<td align="right">15.2%</td>
<td align="right">3,565</td>
<td align="right">13.8%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,250</td>
<td align="right">12.7%</td>
<td align="right">3,608</td>
<td align="right">13.9%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">192</td>
<td align="right">0.6%</td>
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">139</td>
<td align="right">0.4%</td>
<td align="right">135</td>
<td align="right">0.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">22.3%</td>
<td align="right">7,390</td>
<td align="right">28.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">90</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">116</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
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
<td align="right">1,342,831</td>
<td align="right">5.4%</td>
<td align="right">489,043</td>
<td align="right">2.2%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,669</td>
<td align="right">94.6%</td>
<td align="right">22,168,792</td>
<td align="right">97.8%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">3,180</td>
<td align="right">96.3%</td>
<td align="right">2,247</td>
<td align="right">94.9%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.7%</td>
<td align="right">122</td>
<td align="right">5.1%</td>
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
<td align="right">285</td>
<td align="right">9.0%</td>
<td align="right">115</td>
<td align="right">5.1%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,394</td>
<td align="right">43.8%</td>
<td align="right">938</td>
<td align="right">41.7%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,367</td>
<td align="right">43.0%</td>
<td align="right">1,060</td>
<td align="right">47.2%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">134</td>
<td align="right">4.2%</td>
<td align="right">134</td>
<td align="right">6.0%</td>
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
<td align="right">88,660</td>
<td align="right">0.2%</td>
<td align="right">15,214</td>
<td align="right">0.0%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,236,188</td>
<td align="right">44.3%</td>
<td align="right">12,276,331</td>
<td align="right">37.5%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,579,013</td>
<td align="right">55.4%</td>
<td align="right">20,445,775</td>
<td align="right">62.4%</td>
<td align="right">-5.3%</td>
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
<td align="right">2,332</td>
<td align="right">14.3%</td>
<td align="right">968</td>
<td align="right">7.7%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,026</td>
<td align="right">85.7%</td>
<td align="right">11,664</td>
<td align="right">92.3%</td>
<td align="right">-16.8%</td>
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
<td align="right">6,587</td>
<td align="right">47.0%</td>
<td align="right">4,524</td>
<td align="right">38.8%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,431</td>
<td align="right">17.3%</td>
<td align="right">2,222</td>
<td align="right">19.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">350</td>
<td align="right">2.5%</td>
<td align="right">328</td>
<td align="right">2.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.2%</td>
<td align="right">23</td>
<td align="right">0.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.2%</td>
<td align="right">28</td>
<td align="right">0.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,115</td>
<td align="right">7.9%</td>
<td align="right">1,087</td>
<td align="right">9.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">422</td>
<td align="right">3.0%</td>
<td align="right">415</td>
<td align="right">3.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">239</td>
<td align="right">1.7%</td>
<td align="right">236</td>
<td align="right">2.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,136</td>
<td align="right">15.2%</td>
<td align="right">2,112</td>
<td align="right">18.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">693</td>
<td align="right">4.9%</td>
<td align="right">689</td>
<td align="right">5.9%</td>
<td align="right">-0.6%</td>
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
<td align="right">50,358,682</td>
<td align="right">16.4%</td>
<td align="right">16,728,533</td>
<td align="right">6.4%</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,066,794</td>
<td align="right">8.8%</td>
<td align="right">9,504,958</td>
<td align="right">3.6%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">228,906,467</td>
<td align="right">74.7%</td>
<td align="right">234,835,015</td>
<td align="right">89.9%</td>
<td align="right">2.6%</td>
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
<td align="right">522,758</td>
<td align="right">92.5%</td>
<td align="right">190,024</td>
<td align="right">86.7%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,663</td>
<td align="right">7.5%</td>
<td align="right">29,072</td>
<td align="right">13.3%</td>
<td align="right">-31.9%</td>
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
<td align="right">244</td>
<td align="right">0.6%</td>
<td align="right">571</td>
<td align="right">2.0%</td>
<td align="right">134.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.5%</td>
<td align="right">273</td>
<td align="right">0.9%</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,223</td>
<td align="right">14.6%</td>
<td align="right">1,519</td>
<td align="right">5.2%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,060</td>
<td align="right">7.2%</td>
<td align="right">1,416</td>
<td align="right">4.9%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,745</td>
<td align="right">6.4%</td>
<td align="right">2,162</td>
<td align="right">7.4%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,018</td>
<td align="right">7.1%</td>
<td align="right">2,385</td>
<td align="right">8.2%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,986</td>
<td align="right">46.8%</td>
<td align="right">16,399</td>
<td align="right">56.4%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,860</td>
<td align="right">9.0%</td>
<td align="right">3,494</td>
<td align="right">12.0%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">142</td>
<td align="right">0.3%</td>
<td align="right">142</td>
<td align="right">0.5%</td>
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
<td align="right">208,745,802</td>
<td align="right">100.0%</td>
<td align="right">95,963,482</td>
<td align="right">100.0%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,298</td>
<td align="right">0.0%</td>
<td align="right">1,846</td>
<td align="right">0.0%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,555</td>
<td align="right">0.0%</td>
<td align="right">4,535</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">13,610</td>
<td align="right">100.0%</td>
<td align="right">13,611</td>
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
<td align="right">2,265,817</td>
<td align="right">100.0%</td>
<td align="right">2,215,544</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">731,601</td>
<td align="right">72.0%</td>
<td align="right">385,218</td>
<td align="right">58.8%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
<td align="right">9,875</td>
<td align="right">1.5%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">258,773</td>
<td align="right">39.5%</td>
<td align="right">-3.8%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">165</td>
<td align="right">17.3%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">789</td>
<td align="right">82.7%</td>
<td align="right">-28.8%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">789</td>
<td align="right">100.0%</td>
<td align="right">-28.8%</td>
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
<td align="right">173,681</td>
<td align="right">2.1%</td>
<td align="right">12,540</td>
<td align="right">0.2%</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">310,707</td>
<td align="right">3.7%</td>
<td align="right">247,245</td>
<td align="right">3.1%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,897,127</td>
<td align="right">94.2%</td>
<td align="right">7,762,794</td>
<td align="right">96.7%</td>
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
<td align="left">Failure</td>
<td align="right">975</td>
<td align="right">13.8%</td>
<td align="right">714</td>
<td align="right">12.7%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,096</td>
<td align="right">86.2%</td>
<td align="right">4,919</td>
<td align="right">87.3%</td>
<td align="right">-19.3%</td>
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
<td align="right">296</td>
<td align="right">30.4%</td>
<td align="right">36</td>
<td align="right">5.0%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">158</td>
<td align="right">16.2%</td>
<td align="right">157</td>
<td align="right">22.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.1%</td>
<td align="right">518</td>
<td align="right">72.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
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
<td align="right">529</td>
<td align="right">100.0%</td>
<td align="right">398</td>
<td align="right">100.0%</td>
<td align="right">-24.8%</td>
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
<td align="right">64,016</td>
<td align="right">0.4%</td>
<td align="right">37,409</td>
<td align="right">0.3%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,740,293</td>
<td align="right">99.6%</td>
<td align="right">13,375,247</td>
<td align="right">99.7%</td>
<td align="right">-24.6%</td>
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
<td align="right">956</td>
<td align="right">62.4%</td>
<td align="right">977</td>
<td align="right">62.9%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">37.6%</td>
<td align="right">576</td>
<td align="right">37.1%</td>
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
<td align="right">956</td>
<td align="right">100.0%</td>
<td align="right">977</td>
<td align="right">100.0%</td>
<td align="right">2.2%</td>
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
<td align="right">9,820,880</td>
<td align="right">6.0%</td>
<td align="right">1,004,013</td>
<td align="right">0.7%</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">341,981</td>
<td align="right">0.2%</td>
<td align="right">247,451</td>
<td align="right">0.2%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">152,822,606</td>
<td align="right">93.8%</td>
<td align="right">149,695,840</td>
<td align="right">99.2%</td>
<td align="right">-2.0%</td>
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
<td align="right">9,590</td>
<td align="right">41.4%</td>
<td align="right">6,559</td>
<td align="right">35.9%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,573</td>
<td align="right">58.6%</td>
<td align="right">11,719</td>
<td align="right">64.1%</td>
<td align="right">-13.7%</td>
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
<td align="right">4,827</td>
<td align="right">50.3%</td>
<td align="right">2,124</td>
<td align="right">32.4%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">651</td>
<td align="right">6.8%</td>
<td align="right">435</td>
<td align="right">6.6%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,233</td>
<td align="right">12.9%</td>
<td align="right">1,038</td>
<td align="right">15.8%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,182</td>
<td align="right">12.3%</td>
<td align="right">1,264</td>
<td align="right">19.3%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">728</td>
<td align="right">7.6%</td>
<td align="right">711</td>
<td align="right">10.8%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">9.2%</td>
<td align="right">901</td>
<td align="right">13.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.9%</td>
<td align="right">84</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">6,368</td>
<td align="right">0.0%</td>
<td align="right">5,191</td>
<td align="right">0.0%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,491,434</td>
<td align="right">100.0%</td>
<td align="right">82,164,331</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">308</td>
<td align="right">11.4%</td>
<td align="right">306</td>
<td align="right">11.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.6%</td>
<td align="right">2,392</td>
<td align="right">88.7%</td>
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
<td align="right">265</td>
<td align="right">86.0%</td>
<td align="right">263</td>
<td align="right">85.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.0%</td>
<td align="right">43</td>
<td align="right">14.1%</td>
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
<td align="right">933,118,579</td>
<td align="right">31.4%</td>
<td align="right">473,129,808</td>
<td align="right">26.0%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">129,626,828</td>
<td align="right">4.4%</td>
<td align="right">73,048,774</td>
<td align="right">4.0%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">51,277,901</td>
<td align="right">1.7%</td>
<td align="right">31,925,563</td>
<td align="right">1.8%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,853,133,111</td>
<td align="right">62.5%</td>
<td align="right">1,244,832,719</td>
<td align="right">68.3%</td>
<td align="right">-32.8%</td>
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
<td align="right">173,681</td>
<td align="right">0.1%</td>
<td align="right">12,540</td>
<td align="right">0.0%</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,820,880</td>
<td align="right">7.6%</td>
<td align="right">1,004,013</td>
<td align="right">1.4%</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,358,682</td>
<td align="right">38.9%</td>
<td align="right">16,728,533</td>
<td align="right">22.9%</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,342,831</td>
<td align="right">1.0%</td>
<td align="right">489,043</td>
<td align="right">0.7%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">64,016</td>
<td align="right">0.0%</td>
<td align="right">37,409</td>
<td align="right">0.1%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,269,480</td>
<td align="right">14.9%</td>
<td align="right">11,612,682</td>
<td align="right">15.9%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,815,831</td>
<td align="right">2.2%</td>
<td align="right">2,027,564</td>
<td align="right">2.8%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,717,192</td>
<td align="right">18.3%</td>
<td align="right">20,251,952</td>
<td align="right">27.8%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,579,013</td>
<td align="right">16.7%</td>
<td align="right">20,445,775</td>
<td align="right">28.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">258,773</td>
<td align="right">0.4%</td>
<td align="right">-3.8%</td>
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
<td align="right">10,653,510</td>
<td align="right">20.8%</td>
<td align="right">724,488</td>
<td align="right">2.3%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,944,053</td>
<td align="right">5.7%</td>
<td align="right">1,107,055</td>
<td align="right">3.5%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,400,706</td>
<td align="right">16.4%</td>
<td align="right">3,881,189</td>
<td align="right">12.2%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,676,622</td>
<td align="right">9.1%</td>
<td align="right">3,621,281</td>
<td align="right">11.3%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">309,928</td>
<td align="right">0.6%</td>
<td align="right">246,860</td>
<td align="right">0.8%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,683,703</td>
<td align="right">9.1%</td>
<td align="right">3,833,574</td>
<td align="right">12.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">375,210</td>
<td align="right">0.7%</td>
<td align="right">317,492</td>
<td align="right">1.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,140,439</td>
<td align="right">21.7%</td>
<td align="right">10,575,113</td>
<td align="right">33.1%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,583</td>
<td align="right">4.1%</td>
<td align="right">2,074,336</td>
<td align="right">6.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,580</td>
<td align="right">10.0%</td>
<td align="right">5,062,863</td>
<td align="right">15.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">1,008,213</td>
<td align="right">0.5%</td>
<td align="right">831,464</td>
<td align="right">0.4%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,084,122</td>
<td align="right">19.5%</td>
<td align="right">38,361,597</td>
<td align="right">19.0%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,380,524</td>
<td align="right">35.8%</td>
<td align="right">71,955,049</td>
<td align="right">35.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,381,309</td>
<td align="right">35.8%</td>
<td align="right">71,955,834</td>
<td align="right">35.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,627,678</td>
<td align="right">46.4%</td>
<td align="right">93,191,530</td>
<td align="right">46.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,627,678</td>
<td align="right">46.4%</td>
<td align="right">93,191,530</td>
<td align="right">46.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,246,369</td>
<td align="right">10.6%</td>
<td align="right">21,235,696</td>
<td align="right">10.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,906,046</td>
<td align="right">89.3%</td>
<td align="right">180,357,105</td>
<td align="right">89.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,769,584</td>
<td align="right">53.6%</td>
<td align="right">108,280,026</td>
<td align="right">53.7%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,491,209</td>
<td align="right">8.8%</td>
<td align="right">18,074,130</td>
<td align="right">9.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,166</td>
<td align="right">4.4%</td>
<td align="right">9,243,892</td>
<td align="right">4.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">519,938,569</td>
<td align="right">10.0%</td>
<td align="right">333,790,079</td>
<td align="right">6.5%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,402,756,412</td>
<td align="right">27.0%</td>
<td align="right">963,113,862</td>
<td align="right">18.7%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,063,735,385</td>
<td align="right">39.7%</td>
<td align="right">2,617,804,635</td>
<td align="right">50.8%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">632,546,969</td>
<td align="right">10.7%</td>
<td align="right">468,576,401</td>
<td align="right">7.8%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">922,723</td>
<td align="right"></td>
<td align="right">702,547</td>
<td align="right"></td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,126,846,835</td>
<td align="right">35.9%</td>
<td align="right">2,510,413,710</td>
<td align="right">41.7%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,795,149,472</td>
<td align="right">30.3%</td>
<td align="right">1,512,318,486</td>
<td align="right">25.1%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">142,604,957</td>
<td align="right"></td>
<td align="right">124,004,773</td>
<td align="right"></td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,248,426</td>
<td align="right"></td>
<td align="right">2,539,807</td>
<td align="right"></td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,377,811,414</td>
<td align="right">23.2%</td>
<td align="right">1,528,637,672</td>
<td align="right">25.4%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,341</td>
<td align="right"></td>
<td align="right">818,857</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,347,638</td>
<td align="right">45.1%</td>
<td align="right">222,162,443</td>
<td align="right">44.3%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">233,160,234</td>
<td align="right">45.2%</td>
<td align="right">222,996,800</td>
<td align="right">44.5%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,806,724</td>
<td align="right"></td>
<td align="right">235,375,961</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">262,287,583</td>
<td align="right"></td>
<td align="right">252,349,946</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">803,987</td>
<td align="right">0.2%</td>
<td align="right">825,652</td>
<td align="right">0.2%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,169,702</td>
<td align="right"></td>
<td align="right">3,241,419</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,217,867,393</td>
<td align="right">23.4%</td>
<td align="right">1,241,889,421</td>
<td align="right">24.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">282,500,004</td>
<td align="right">54.8%</td>
<td align="right">278,151,476</td>
<td align="right">55.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">282,532,302</td>
<td align="right"></td>
<td align="right">278,184,089</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,609</td>
<td align="right">0.0%</td>
<td align="right">8,705</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">304</td>
<td align="right">0.2%</td>
<td align="right">234.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">59,204</td>
<td align="right">48.9%</td>
<td align="right">150,945</td>
<td align="right">58.0%</td>
<td align="right">155.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">58,700</td>
<td align="right">48.5%</td>
<td align="right">129,340</td>
<td align="right">49.7%</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">121,147</td>
<td align="right"></td>
<td align="right">260,177</td>
<td align="right"></td>
<td align="right">114.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">62,447</td>
<td align="right">51.5%</td>
<td align="right">130,837</td>
<td align="right">50.3%</td>
<td align="right">109.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,108</td>
<td align="right">0.9%</td>
<td align="right">2,163</td>
<td align="right">0.8%</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">283,959,167</td>
<td align="right"></td>
<td align="right">454,542,378</td>
<td align="right"></td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,301,059,956</td>
<td align="right">1,514.7%</td>
<td align="right">6,459,504,960</td>
<td align="right">1,421.1%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,352</td>
<td align="right">1.1%</td>
<td align="right">1,566</td>
<td align="right">0.6%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">407</td>
<td align="right">0.3%</td>
<td align="right">366</td>
<td align="right">0.1%</td>
<td align="right">-10.1%</td>
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
<td align="right">55,746</td>
<td align="right">95.0%</td>
<td align="right">125,998</td>
<td align="right">97.4%</td>
<td align="right">126.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">58,700</td>
<td align="right"></td>
<td align="right">129,340</td>
<td align="right"></td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">2,501</td>
<td align="right">1.9%</td>
<td align="right">2,501 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">5,115</td>
<td align="right">8.7%</td>
<td align="right">10,103</td>
<td align="right">7.8%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,575</td>
<td align="right">14.6%</td>
<td align="right">22,022</td>
<td align="right">17.0%</td>
<td align="right">156.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">23,881</td>
<td align="right">40.7%</td>
<td align="right">49,165</td>
<td align="right">38.0%</td>
<td align="right">105.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">13,945</td>
<td align="right">23.8%</td>
<td align="right">31,509</td>
<td align="right">24.4%</td>
<td align="right">126.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,424</td>
<td align="right">10.9%</td>
<td align="right">12,169</td>
<td align="right">9.4%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">760</td>
<td align="right">1.3%</td>
<td align="right">1,815</td>
<td align="right">1.4%</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">56</td>
<td align="right">0.0%</td>
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
<td align="right">3,205</td>
<td align="right">5.5%</td>
<td align="right">9,373</td>
<td align="right">7.2%</td>
<td align="right">192.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,482</td>
<td align="right">7.6%</td>
<td align="right">7,277</td>
<td align="right">5.6%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,697</td>
<td align="right">23.3%</td>
<td align="right">38,638</td>
<td align="right">29.9%</td>
<td align="right">182.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,015</td>
<td align="right">37.5%</td>
<td align="right">44,639</td>
<td align="right">34.5%</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,939</td>
<td align="right">18.6%</td>
<td align="right">22,324</td>
<td align="right">17.3%</td>
<td align="right">104.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,370</td>
<td align="right">2.3%</td>
<td align="right">3,273</td>
<td align="right">2.5%</td>
<td align="right">138.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">38</td>
<td align="right">0.1%</td>
<td align="right">474</td>
<td align="right">0.4%</td>
<td align="right">1,147.4%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,504</td>
<td align="right">1,287,180</td>
<td align="right">85,483.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">336</td>
<td align="right">174,076</td>
<td align="right">51,708.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">285</td>
<td align="right">87,929</td>
<td align="right">30,752.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,392</td>
<td align="right">288,253</td>
<td align="right">11,950.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,287</td>
<td align="right">268,391</td>
<td align="right">11,635.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">3,084</td>
<td align="right">156,440</td>
<td align="right">4,972.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">847</td>
<td align="right">32,964</td>
<td align="right">3,791.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">396</td>
<td align="right">14,670</td>
<td align="right">3,604.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">440,906</td>
<td align="right">10,580,201</td>
<td align="right">2,299.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">294,460</td>
<td align="right">7,047,825</td>
<td align="right">2,293.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">294,617</td>
<td align="right">7,048,141</td>
<td align="right">2,292.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">31,665</td>
<td align="right">646,394</td>
<td align="right">1,941.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">472,792</td>
<td align="right">9,238,726</td>
<td align="right">1,854.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,707,918</td>
<td align="right">168,909,276</td>
<td align="right">1,839.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">131,495</td>
<td align="right">2,083,691</td>
<td align="right">1,484.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,001</td>
<td align="right">309,569</td>
<td align="right">1,447.8%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,001</td>
<td align="right">309,565</td>
<td align="right">1,447.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">285,997</td>
<td align="right">4,405,852</td>
<td align="right">1,440.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">285,997</td>
<td align="right">4,384,426</td>
<td align="right">1,433.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">758,364</td>
<td align="right">10,939,928</td>
<td align="right">1,342.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4,535</td>
<td align="right">64,902</td>
<td align="right">1,331.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">325,528</td>
<td align="right">3,052,030</td>
<td align="right">837.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">24,690</td>
<td align="right">186,905</td>
<td align="right">657.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">619,484</td>
<td align="right">4,268,971</td>
<td align="right">589.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">480,451</td>
<td align="right">3,241,399</td>
<td align="right">574.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">981,130</td>
<td align="right">6,113,173</td>
<td align="right">523.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">914,259</td>
<td align="right">5,337,779</td>
<td align="right">483.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">252</td>
<td align="right">1,196</td>
<td align="right">374.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">62</td>
<td align="right">272</td>
<td align="right">338.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">17,816</td>
<td align="right">74,314</td>
<td align="right">317.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,176,257</td>
<td align="right">4,263,132</td>
<td align="right">262.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">64,502</td>
<td align="right">219,221</td>
<td align="right">239.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">552</td>
<td align="right">1,798</td>
<td align="right">225.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">334,953</td>
<td align="right">1,062,426</td>
<td align="right">217.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">334,953</td>
<td align="right">1,062,426</td>
<td align="right">217.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,286,541</td>
<td align="right">31,695,554</td>
<td align="right">208.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">35,666,007</td>
<td align="right">105,076,421</td>
<td align="right">194.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,924,962</td>
<td align="right">106,197,826</td>
<td align="right">187.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,246,592</td>
<td align="right">13,598,951</td>
<td align="right">159.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,476,107</td>
<td align="right">3,684,941</td>
<td align="right">149.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,761,323</td>
<td align="right">60,941,995</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,066,605</td>
<td align="right">29,952,394</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">10,474,310</td>
<td align="right">23,681,434</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">106,558,853</td>
<td align="right">234,368,007</td>
<td align="right">119.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,943,401</td>
<td align="right">14,993,260</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,392,018</td>
<td align="right">13,740,472</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,792,167</td>
<td align="right">8,048,289</td>
<td align="right">112.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">782,544</td>
<td align="right">1,657,778</td>
<td align="right">111.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,446,197</td>
<td align="right">21,915,396</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,857,888</td>
<td align="right">8,049,611</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">236,260</td>
<td align="right">488,891</td>
<td align="right">106.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,537,963</td>
<td align="right">5,227,077</td>
<td align="right">106.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,450,379</td>
<td align="right">7,099,942</td>
<td align="right">105.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,167,835</td>
<td align="right">73,034,976</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">157</td>
<td align="right">316</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">157</td>
<td align="right">316</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,877,307</td>
<td align="right">7,799,507</td>
<td align="right">101.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,667,811</td>
<td align="right">37,551,020</td>
<td align="right">101.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,636,936</td>
<td align="right">3,281,309</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">53,665,891</td>
<td align="right">22,495</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,048,646</td>
<td align="right">22,089,197</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">87,735,477</td>
<td align="right">172,557,223</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">8,990,465</td>
<td align="right">17,646,683</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">36,569,268</td>
<td align="right">71,192,852</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">36,470,408</td>
<td align="right">70,778,570</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">61,097,203</td>
<td align="right">118,456,649</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,776</td>
<td align="right">3,442</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,776</td>
<td align="right">3,442</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">888</td>
<td align="right">1,721</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">32,073,215</td>
<td align="right">61,570,135</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,487,025</td>
<td align="right">2,831,314</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">36,207,695</td>
<td align="right">68,324,905</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,552,527</td>
<td align="right">14,218,508</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,552,527</td>
<td align="right">14,218,508</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,032,220</td>
<td align="right">128,639</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,020,580</td>
<td align="right">11,255,904</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">532,504</td>
<td align="right">995,107</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">34,419,778</td>
<td align="right">62,957,097</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">756,263</td>
<td align="right">1,336,241</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,193,304</td>
<td align="right">7,408,373</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">7,247,977</td>
<td align="right">1,828,185</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">46,019,812</td>
<td align="right">80,334,555</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,883,401</td>
<td align="right">6,555,475</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,303,240</td>
<td align="right">29,146,587</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right">2,180</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">11,172,670</td>
<td align="right">18,752,458</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,247,090</td>
<td align="right">33,720,384</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">11,538,043</td>
<td align="right">19,119,877</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">31,327,992</td>
<td align="right">51,263,010</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">18,877,932</td>
<td align="right">30,652,992</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,484,356</td>
<td align="right">583,664</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,484,356</td>
<td align="right">583,664</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">29,442,351</td>
<td align="right">47,300,272</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">283,959,167</td>
<td align="right">454,542,378</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">21,407,552</td>
<td align="right">34,129,643</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">157,074,184</td>
<td align="right">248,075,246</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,435,024</td>
<td align="right">27,346,672</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">257,930,815</td>
<td align="right">393,078,129</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">340,761</td>
<td align="right">162,488</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">195,181</td>
<td align="right">295,681</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">315,973,051</td>
<td align="right">476,053,448</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,516</td>
<td align="right">2,281</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">77,961,489</td>
<td align="right">114,633,460</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,086,141</td>
<td align="right">23,390,627</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">10,949,492</td>
<td align="right">15,426,285</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">402,711,698</td>
<td align="right">561,278,076</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,104,327</td>
<td align="right">25,104,298</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,579,266</td>
<td align="right">21,512,394</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">889</td>
<td align="right">1,225</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,704,129</td>
<td align="right">2,339,306</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">319,226,197</td>
<td align="right">436,489,125</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">4,090</td>
<td align="right">2,664</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">27,817,550</td>
<td align="right">37,349,543</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">76,601</td>
<td align="right">102,453</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,926,787</td>
<td align="right">3,273,049</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">32,013,884</td>
<td align="right">21,511,070</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,036,761</td>
<td align="right">2,053,597</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,893,769</td>
<td align="right">7,667,742</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,746,999</td>
<td align="right">3,543,167</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,302,517</td>
<td align="right">1,662,680</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">97,161,471</td>
<td align="right">121,669,514</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,913,708</td>
<td align="right">99,786,670</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">45,685,979</td>
<td align="right">56,967,111</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,197,028</td>
<td align="right">2,739,296</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,207,475</td>
<td align="right">15,184,117</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,441,131</td>
<td align="right">9,254,296</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">1,589</td>
<td align="right">1,208</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,880,302</td>
<td align="right">15,923,300</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">12,880,302</td>
<td align="right">15,923,300</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">7,398,904</td>
<td align="right">5,655,946</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">48,927,447</td>
<td align="right">60,449,268</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">7,919,927</td>
<td align="right">9,763,804</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">37,761,894</td>
<td align="right">46,538,967</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,983,265</td>
<td align="right">6,132,362</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,983,265</td>
<td align="right">6,132,362</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,105,297</td>
<td align="right">17,868,687</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">3,474,521</td>
<td align="right">4,247,623</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">46,032,915</td>
<td align="right">55,871,185</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">4,204,088</td>
<td align="right">4,946,425</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,560,270</td>
<td align="right">13,490,824</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,659,339</td>
<td align="right">8,894,758</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">286,753</td>
<td align="right">333,959</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,312,364</td>
<td align="right">32,711,288</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">11,410,734</td>
<td align="right">13,016,143</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">172,574,808</td>
<td align="right">196,594,546</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">317,532</td>
<td align="right">359,773</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">34,517,556</td>
<td align="right">38,906,035</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,802,400</td>
<td align="right">12,059,934</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">21,075,699</td>
<td align="right">18,459,242</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">16,018,023</td>
<td align="right">14,167,694</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,486,525</td>
<td align="right">28,010,176</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">672,827</td>
<td align="right">739,183</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">672,308</td>
<td align="right">738,591</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,422,751</td>
<td align="right">15,783,558</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,210,205</td>
<td align="right">7,482,292</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">18,528,136</td>
<td align="right">20,111,139</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">30,769</td>
<td align="right">33,363</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,475,361</td>
<td align="right">5,935,181</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,518,852</td>
<td align="right">2,317,303</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">11,994,116</td>
<td align="right">11,107,907</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">40,938,696</td>
<td align="right">37,927,292</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">491,214</td>
<td align="right">526,439</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">491,214</td>
<td align="right">526,439</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">31,956,107</td>
<td align="right">29,683,008</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,196,298</td>
<td align="right">15,051,238</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,678</td>
<td align="right">809,145</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">40,080,552</td>
<td align="right">37,860,686</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">20,619,449</td>
<td align="right">19,645,436</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,409,557</td>
<td align="right">19,185,124</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">654,299</td>
<td align="right">628,815</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,384</td>
<td align="right">2,453</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,384</td>
<td align="right">2,453</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">132,989</td>
<td align="right">135,693</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">19,848,417</td>
<td align="right">20,226,225</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">57,953,915</td>
<td align="right">58,960,245</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">48,751,536</td>
<td align="right">48,052,765</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">60,760,839</td>
<td align="right">61,491,787</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,874,436</td>
<td align="right">7,818,779</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">15,714,071</td>
<td align="right">15,615,610</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">47,452,845</td>
<td align="right">47,724,510</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,413,380</td>
<td align="right">13,344,872</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,515,317</td>
<td align="right">2,515,221</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,036,151</td>
<td align="right">1,036,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">5,346</td>
<td align="right">5,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">1,839</td>
<td align="right">1,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">286</td>
<td align="right">286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">934,694</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">934,694</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">924,701</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">847,639</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">847,639</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">847,639</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">358,592</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">356,584</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">115,555</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right"></td>
<td align="right">110,413</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">21,426</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right"></td>
<td align="right">2,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">183</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">92</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">21</td>
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
<td align="right">367</td>
<td align="right">629</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,076</td>
<td align="right">18,869</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,602</td>
<td align="right">8,142</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">280</td>
<td align="right">256</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">64</td>
<td align="right">64</td>
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
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
