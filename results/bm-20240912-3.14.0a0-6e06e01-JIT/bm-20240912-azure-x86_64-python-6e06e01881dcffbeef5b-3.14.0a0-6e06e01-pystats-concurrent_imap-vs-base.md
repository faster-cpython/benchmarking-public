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
<td align="left">FOR_ITER_GEN</td>
<td align="right">6,347,440</td>
<td align="right">12,720</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">6,464,820</td>
<td align="right">42,620</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">583,120</td>
<td align="right">7,760</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,305,260</td>
<td align="right">36,380</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">482,600</td>
<td align="right">18,238</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">759,605</td>
<td align="right">34,158</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,683,140</td>
<td align="right">1,087,956</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">564,260</td>
<td align="right">57,240</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">112,600</td>
<td align="right">14,600</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">112,600</td>
<td align="right">14,600</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,169,585</td>
<td align="right">161,544</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">637,599</td>
<td align="right">128,192</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">126,780</td>
<td align="right">28,640</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,965,204</td>
<td align="right">2,403,521</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,006,260</td>
<td align="right">293,776</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,669,231</td>
<td align="right">548,736</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,052,827</td>
<td align="right">384,045</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">969,509</td>
<td align="right">387,818</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,800</td>
<td align="right">1,240</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,220</td>
<td align="right">14,080</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,820,686</td>
<td align="right">2,249,027</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,481,442</td>
<td align="right">731,079</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">26,735,128</td>
<td align="right">13,254,718</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,727,814</td>
<td align="right">1,863,986</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,133,406</td>
<td align="right">1,071,147</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,355,636</td>
<td align="right">3,780,306</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">625,957</td>
<td align="right">328,196</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">135,985</td>
<td align="right">72,080</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,686,345</td>
<td align="right">2,506,339</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,112,421</td>
<td align="right">600,724</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">11,045,035</td>
<td align="right">6,063,306</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,384,911</td>
<td align="right">13,017,456</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,820,212</td>
<td align="right">1,024,340</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,279,492</td>
<td align="right">2,432,496</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,036,773</td>
<td align="right">1,769,043</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,033,553</td>
<td align="right">9,472,567</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,779,879</td>
<td align="right">4,042,062</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,382,488</td>
<td align="right">826,860</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,367,447</td>
<td align="right">1,433,020</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">35,884,317</td>
<td align="right">22,353,594</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,255,967</td>
<td align="right">2,722,569</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,589,279</td>
<td align="right">2,300,459</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,741,767</td>
<td align="right">1,117,856</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,759,317</td>
<td align="right">1,151,083</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,758,669</td>
<td align="right">6,400,366</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,797,272</td>
<td align="right">3,828,982</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,701,226</td>
<td align="right">9,933,598</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,324,885</td>
<td align="right">4,296,375</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">98,759,869</td>
<td align="right">68,290,436</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,164,588</td>
<td align="right">1,504,503</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">17,043,442</td>
<td align="right">11,852,330</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,663,302</td>
<td align="right">2,561,560</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">9,103,923</td>
<td align="right">6,414,376</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,578,226</td>
<td align="right">9,584,238</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">8,096,469</td>
<td align="right">5,734,662</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">43,340</td>
<td align="right">31,181</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,999,594</td>
<td align="right">1,453,036</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,819,452</td>
<td align="right">6,696,420</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,175,035</td>
<td align="right">3,216,893</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,520,371</td>
<td align="right">22,801,687</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">818,169</td>
<td align="right">652,089</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">331,009</td>
<td align="right">264,101</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,469,869</td>
<td align="right">1,174,140</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,026,752</td>
<td align="right">13,710,475</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,671,130</td>
<td align="right">6,202,216</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">240,436</td>
<td align="right">196,911</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">409,420</td>
<td align="right">345,096</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">33,420</td>
<td align="right">28,460</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">9,075,267</td>
<td align="right">7,730,624</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">33,740</td>
<td align="right">28,780</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">278,096</td>
<td align="right">239,447</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3,840</td>
<td align="right">3,420</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">282,740</td>
<td align="right">255,383</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,949,568</td>
<td align="right">18,964,094</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,137,745</td>
<td align="right">1,029,918</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,165,778</td>
<td align="right">4,678,850</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,183,207</td>
<td align="right">1,072,489</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,995,119</td>
<td align="right">6,344,041</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">236,186</td>
<td align="right">214,269</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">472,480</td>
<td align="right">428,646</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,669,737</td>
<td align="right">1,515,103</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,673,618</td>
<td align="right">1,519,025</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,503,847</td>
<td align="right">1,371,802</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">754,850</td>
<td align="right">688,597</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,769,938</td>
<td align="right">1,615,305</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">252,831</td>
<td align="right">230,873</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">514,071</td>
<td align="right">470,196</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,819,998</td>
<td align="right">1,665,365</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">264,085</td>
<td align="right">242,127</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,877,997</td>
<td align="right">1,722,883</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">32,999</td>
<td align="right">30,333</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">578,411</td>
<td align="right">534,519</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">341,540</td>
<td align="right">319,127</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">43,979</td>
<td align="right">41,313</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,301,215</td>
<td align="right">1,227,812</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">49,739</td>
<td align="right">47,073</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">49,739</td>
<td align="right">47,073</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">829,566</td>
<td align="right">807,493</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,350,533</td>
<td align="right">9,107,503</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">936</td>
<td align="right">928</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">46,976</td>
<td align="right">46,585</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">18,900</td>
<td align="right">18,860</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">39,080</td>
<td align="right">39,040</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">63,720</td>
<td align="right">63,680</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">134,965</td>
<td align="right">134,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,924</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">138,220</td>
<td align="right">138,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">17,880</td>
<td align="right">17,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">31,298</td>
<td align="right">31,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">93,080</td>
<td align="right">93,084</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,414,020</td>
<td align="right">2,414,004</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,913,660</td>
<td align="right">6,913,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">138,460</td>
<td align="right">138,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">114,880</td>
<td align="right">114,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">99,760</td>
<td align="right">99,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">97,980</td>
<td align="right">97,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">96,380</td>
<td align="right">96,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">89,520</td>
<td align="right">89,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">86,400</td>
<td align="right">86,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">78,220</td>
<td align="right">78,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,280</td>
<td align="right">75,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">75,280</td>
<td align="right">75,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">55,680</td>
<td align="right">55,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,600</td>
<td align="right">41,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">39,160</td>
<td align="right">39,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,160</td>
<td align="right">28,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,820</td>
<td align="right">19,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">17,280</td>
<td align="right">17,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,900</td>
<td align="right">11,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">11,520</td>
<td align="right">11,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,140</td>
<td align="right">9,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,940</td>
<td align="right">5,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,780</td>
<td align="right">5,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,760</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,160</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">920</td>
<td align="right">920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">620</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">520</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">10,351,264</td>
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
<td align="right">6,988,070</td>
<td align="right">77.0%</td>
<td align="right">6,337,201</td>
<td align="right">75.7%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,076,367</td>
<td align="right">22.9%</td>
<td align="right">2,029,743</td>
<td align="right">24.2%</td>
<td align="right">-2.2%</td>
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
<td align="right">6,430</td>
<td align="right">91.2%</td>
<td align="right">6,220</td>
<td align="right">90.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">619</td>
<td align="right">8.8%</td>
<td align="right">620</td>
<td align="right">9.1%</td>
<td align="right">0.2%</td>
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
<td align="right">779</td>
<td align="right">12.1%</td>
<td align="right">720</td>
<td align="right">11.6%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,710</td>
<td align="right">26.6%</td>
<td align="right">1,652</td>
<td align="right">26.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,201</td>
<td align="right">49.8%</td>
<td align="right">3,108</td>
<td align="right">50.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">640</td>
<td align="right">10.0%</td>
<td align="right">640</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">100</td>
<td align="right">1.6%</td>
<td align="right">100</td>
<td align="right">1.6%</td>
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
<td align="right">19,820</td>
<td align="right">100.0%</td>
<td align="right">19,820</td>
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
<td align="right">636,479</td>
<td align="right">45.9%</td>
<td align="right">127,253</td>
<td align="right">15.3%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">749,240</td>
<td align="right">54.0%</td>
<td align="right">705,406</td>
<td align="right">84.6%</td>
<td align="right">-5.9%</td>
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
<td align="right">880</td>
<td align="right">78.6%</td>
<td align="right">699</td>
<td align="right">74.4%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">21.4%</td>
<td align="right">240</td>
<td align="right">25.6%</td>
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
<td align="left">buffer int</td>
<td align="right">880</td>
<td align="right">100.0%</td>
<td align="right">699</td>
<td align="right">100.0%</td>
<td align="right">-20.6%</td>
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
<td align="right">1,600</td>
<td align="right">0.0%</td>
<td align="right">1,180</td>
<td align="right">0.0%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,488,692</td>
<td align="right">99.9%</td>
<td align="right">24,922,818</td>
<td align="right">99.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,624</td>
<td align="right">0.1%</td>
<td align="right">13,631</td>
<td align="right">0.1%</td>
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
<td align="right">13,920</td>
<td align="right">100.0%</td>
<td align="right">13,921</td>
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
<td align="right">620</td>
<td align="right">50.0%</td>
<td align="right">620</td>
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
<td align="right">575,627</td>
<td align="right">9.9%</td>
<td align="right">531,699</td>
<td align="right">9.6%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,203,041</td>
<td align="right">89.9%</td>
<td align="right">5,019,745</td>
<td align="right">90.3%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,355</td>
<td align="right">0.1%</td>
<td align="right">6,414</td>
<td align="right">0.1%</td>
<td align="right">0.9%</td>
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
<td align="right">1,344</td>
<td align="right">46.8%</td>
<td align="right">1,380</td>
<td align="right">47.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,529</td>
<td align="right">53.2%</td>
<td align="right">1,532</td>
<td align="right">52.6%</td>
<td align="right">0.2%</td>
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
<td align="right">175</td>
<td align="right">13.0%</td>
<td align="right">200</td>
<td align="right">14.5%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">809</td>
<td align="right">60.2%</td>
<td align="right">820</td>
<td align="right">59.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">360</td>
<td align="right">26.8%</td>
<td align="right">360</td>
<td align="right">26.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,742,387</td>
<td align="right">100.0%</td>
<td align="right">1,631,669</td>
<td align="right">100.0%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">1,302,940</td>
<td align="right">7.1%</td>
<td align="right">34,820</td>
<td align="right">0.4%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,102,469</td>
<td align="right">92.9%</td>
<td align="right">8,799,199</td>
<td align="right">99.6%</td>
<td align="right">-48.6%</td>
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
<td align="right">1,700</td>
<td align="right">73.3%</td>
<td align="right">940</td>
<td align="right">60.3%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">26.7%</td>
<td align="right">620</td>
<td align="right">39.7%</td>
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
<td align="right">520</td>
<td align="right">30.6%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">520</td>
<td align="right">30.6%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">400</td>
<td align="right">23.5%</td>
<td align="right">280</td>
<td align="right">29.8%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">260</td>
<td align="right">15.3%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
<td align="right">-15.4%</td>
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
<td align="right">7,639,880</td>
<td align="right">13.3%</td>
<td align="right">6,171,446</td>
<td align="right">11.7%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">49,339,837</td>
<td align="right">85.6%</td>
<td align="right">46,167,142</td>
<td align="right">87.2%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">596,526</td>
<td align="right">1.0%</td>
<td align="right">564,326</td>
<td align="right">1.1%</td>
<td align="right">-5.4%</td>
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
<td align="right">14,291</td>
<td align="right">34.0%</td>
<td align="right">13,808</td>
<td align="right">33.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,779</td>
<td align="right">66.0%</td>
<td align="right">27,186</td>
<td align="right">66.3%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">2,436</td>
<td align="right">17.0%</td>
<td align="right">2,140</td>
<td align="right">15.5%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,537</td>
<td align="right">24.7%</td>
<td align="right">3,448</td>
<td align="right">25.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,619</td>
<td align="right">32.3%</td>
<td align="right">4,530</td>
<td align="right">32.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">700</td>
<td align="right">4.9%</td>
<td align="right">700</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">560</td>
<td align="right">3.9%</td>
<td align="right">560</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">25,840,728</td>
<td align="right">99.9%</td>
<td align="right">20,401,555</td>
<td align="right">99.9%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,476</td>
<td align="right">0.0%</td>
<td align="right">5,340</td>
<td align="right">0.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
<td align="right">8,322</td>
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
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
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
<td align="right">9,598</td>
<td align="right">100.0%</td>
<td align="right">9,600</td>
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
<td align="right">1,763,138</td>
<td align="right">100.0%</td>
<td align="right">1,608,545</td>
<td align="right">100.0%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
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
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">280</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,101,495</td>
<td align="right">93.9%</td>
<td align="right">3,882,116</td>
<td align="right">93.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">86,860</td>
<td align="right">2.0%</td>
<td align="right">86,864</td>
<td align="right">2.1%</td>
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
<td align="right">171,520</td>
<td align="right">3.9%</td>
<td align="right">171,520</td>
<td align="right">4.1%</td>
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
<td align="right">7,360</td>
<td align="right">79.1%</td>
<td align="right">7,360</td>
<td align="right">79.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,940</td>
<td align="right">20.9%</td>
<td align="right">1,940</td>
<td align="right">20.9%</td>
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
<td align="left">property</td>
<td align="right">1,180</td>
<td align="right">60.8%</td>
<td align="right">1,180</td>
<td align="right">60.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">560</td>
<td align="right">28.9%</td>
<td align="right">560</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">10.3%</td>
<td align="right">200</td>
<td align="right">10.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,759,317</td>
<td align="right">98.3%</td>
<td align="right">1,652,523</td>
<td align="right">98.1%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,359</td>
<td align="right">1.7%</td>
<td align="right">30,360</td>
<td align="right">1.8%</td>
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
<td align="right">279</td>
<td align="right">29.7%</td>
<td align="right">280</td>
<td align="right">29.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">660</td>
<td align="right">70.3%</td>
<td align="right">660</td>
<td align="right">70.2%</td>
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
<td align="left">py simple</td>
<td align="right">440</td>
<td align="right">66.7%</td>
<td align="right">440</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">33.3%</td>
<td align="right">220</td>
<td align="right">33.3%</td>
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
<td align="right">1,047,262</td>
<td align="right">8.2%</td>
<td align="right">378,904</td>
<td align="right">3.4%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,720,077</td>
<td align="right">91.8%</td>
<td align="right">10,801,169</td>
<td align="right">96.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
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
<td align="right">2,904</td>
<td align="right">52.2%</td>
<td align="right">2,480</td>
<td align="right">48.2%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,661</td>
<td align="right">47.8%</td>
<td align="right">2,661</td>
<td align="right">51.8%</td>
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
<td align="right">740</td>
<td align="right">25.5%</td>
<td align="right">440</td>
<td align="right">17.7%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">420</td>
<td align="right">14.5%</td>
<td align="right">380</td>
<td align="right">15.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,084</td>
<td align="right">37.3%</td>
<td align="right">1,000</td>
<td align="right">40.3%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">440</td>
<td align="right">15.2%</td>
<td align="right">440</td>
<td align="right">17.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">7.6%</td>
<td align="right">220</td>
<td align="right">8.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,302,991</td>
<td align="right">100.0%</td>
<td align="right">3,214,492</td>
<td align="right">100.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="right">440</td>
<td align="right">100.0%</td>
<td align="right">440</td>
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
<td align="right">201,019,597</td>
<td align="right">35.6%</td>
<td align="right">123,099,405</td>
<td align="right">32.8%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">345,209,021</td>
<td align="right">61.1%</td>
<td align="right">237,090,258</td>
<td align="right">63.3%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">18,432,188</td>
<td align="right">3.3%</td>
<td align="right">13,821,251</td>
<td align="right">3.7%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">781,757</td>
<td align="right">0.1%</td>
<td align="right">749,060</td>
<td align="right">0.2%</td>
<td align="right">-4.2%</td>
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
<td align="right">1,302,940</td>
<td align="right">7.1%</td>
<td align="right">34,820</td>
<td align="right">0.3%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">636,479</td>
<td align="right">3.5%</td>
<td align="right">127,253</td>
<td align="right">0.9%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,047,262</td>
<td align="right">5.7%</td>
<td align="right">378,904</td>
<td align="right">2.8%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,639,880</td>
<td align="right">41.6%</td>
<td align="right">6,171,446</td>
<td align="right">44.9%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,988,070</td>
<td align="right">38.1%</td>
<td align="right">6,337,201</td>
<td align="right">46.1%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">575,627</td>
<td align="right">3.1%</td>
<td align="right">531,699</td>
<td align="right">3.9%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,624</td>
<td align="right">0.1%</td>
<td align="right">13,631</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86,860</td>
<td align="right">0.5%</td>
<td align="right">86,864</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">30,359</td>
<td align="right">0.2%</td>
<td align="right">30,360</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,820</td>
<td align="right">0.1%</td>
<td align="right">19,820</td>
<td align="right">0.1%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">860</td>
<td align="right">0.1%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">521,144</td>
<td align="right">66.7%</td>
<td align="right">488,953</td>
<td align="right">65.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,136</td>
<td align="right">0.7%</td>
<td align="right">5,000</td>
<td align="right">0.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,335</td>
<td align="right">0.8%</td>
<td align="right">6,394</td>
<td align="right">0.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">61,902</td>
<td align="right">7.9%</td>
<td align="right">61,893</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,520</td>
<td align="right">21.9%</td>
<td align="right">171,520</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.6%</td>
<td align="right">12,380</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
<td align="right">0.0%</td>
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
<td align="right">626,584</td>
<td align="right">1.7%</td>
<td align="right">582,022</td>
<td align="right">1.7%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">29,051,877</td>
<td align="right">80.9%</td>
<td align="right">27,489,044</td>
<td align="right">80.0%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">49,855</td>
<td align="right">0.1%</td>
<td align="right">47,191</td>
<td align="right">0.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">26,552,844</td>
<td align="right">73.9%</td>
<td align="right">25,233,041</td>
<td align="right">73.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,770,493</td>
<td align="right">24.4%</td>
<td align="right">8,527,463</td>
<td align="right">24.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,771,193</td>
<td align="right">24.4%</td>
<td align="right">8,528,163</td>
<td align="right">24.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,356,313</td>
<td align="right">26.1%</td>
<td align="right">9,113,283</td>
<td align="right">26.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,356,313</td>
<td align="right">26.1%</td>
<td align="right">9,113,283</td>
<td align="right">26.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">585,120</td>
<td align="right">1.6%</td>
<td align="right">585,120</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">625,920</td>
<td align="right">1.7%</td>
<td align="right">625,920</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">535,340</td>
<td align="right">1.5%</td>
<td align="right">535,340</td>
<td align="right">1.6%</td>
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
<td align="right">28,713</td>
<td align="right"></td>
<td align="right">2,341,391</td>
<td align="right"></td>
<td align="right">8,054.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">45,535</td>
<td align="right"></td>
<td align="right">242,237</td>
<td align="right"></td>
<td align="right">432.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">65,621,693</td>
<td align="right">65,621,693 / 0 !!</td>
<td align="right">150,037,590</td>
<td align="right">150,037,590 / 0 !!</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">81,661,627</td>
<td align="right">81,661,627 / 0 !!</td>
<td align="right">148,999,060</td>
<td align="right">148,999,060 / 0 !!</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">214,370,526</td>
<td align="right">214,370,526 / 0 !!</td>
<td align="right">154,630,878</td>
<td align="right">154,630,878 / 0 !!</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">12,258,900</td>
<td align="right"></td>
<td align="right">9,460,868</td>
<td align="right"></td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">235,731,939</td>
<td align="right">235,731,939 / 0 !!</td>
<td align="right">191,637,687</td>
<td align="right">191,637,687 / 0 !!</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,549</td>
<td align="right"></td>
<td align="right">60,373</td>
<td align="right"></td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,845,094</td>
<td align="right"></td>
<td align="right">8,932,533</td>
<td align="right"></td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,222,542</td>
<td align="right"></td>
<td align="right">1,134,792</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,111,361</td>
<td align="right">46.6%</td>
<td align="right">18,174,483</td>
<td align="right">46.1%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,124,205</td>
<td align="right"></td>
<td align="right">18,187,391</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">23,345,355</td>
<td align="right"></td>
<td align="right">22,585,423</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">21,607,704</td>
<td align="right">52.7%</td>
<td align="right">20,958,456</td>
<td align="right">53.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">21,912,788</td>
<td align="right">53.4%</td>
<td align="right">21,264,670</td>
<td align="right">53.9%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">131,969</td>
<td align="right">0.3%</td>
<td align="right">133,115</td>
<td align="right">0.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">173,115</td>
<td align="right">0.4%</td>
<td align="right">173,099</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">930,680</td>
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">930,400</td>
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
<td align="right">12</td>
<td align="right">12 / 0 !!</td>
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
<td align="right">12</td>
<td align="right">12 / 0 !!</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
