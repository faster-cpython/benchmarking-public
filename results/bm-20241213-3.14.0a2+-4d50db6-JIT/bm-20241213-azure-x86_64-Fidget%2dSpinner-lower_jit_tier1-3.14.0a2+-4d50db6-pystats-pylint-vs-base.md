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
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">67,008</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,039,311</td>
<td align="right">2,295,953</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,255,323</td>
<td align="right">27,130,003</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,694,442</td>
<td align="right">3,942,418</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">209,178</td>
<td align="right">195,231</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,117,695</td>
<td align="right">2,023,470</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,687,466</td>
<td align="right">27,702,551</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,463,185</td>
<td align="right">2,391,938</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,952,337</td>
<td align="right">2,006,355</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,673,379</td>
<td align="right">4,799,289</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">11,291,473</td>
<td align="right">11,040,070</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,775,976</td>
<td align="right">3,845,034</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">17,545,904</td>
<td align="right">17,857,713</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,655,597</td>
<td align="right">11,856,133</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">350,940</td>
<td align="right">356,472</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,746,742</td>
<td align="right">1,722,550</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">136,390</td>
<td align="right">138,145</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">84,218</td>
<td align="right">85,255</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,388,954</td>
<td align="right">6,465,031</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,536,405</td>
<td align="right">3,495,306</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">6,730,393</td>
<td align="right">6,660,700</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,836,446</td>
<td align="right">5,776,052</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,612,826</td>
<td align="right">9,708,169</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">644,223</td>
<td align="right">649,755</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,636,186</td>
<td align="right">29,882,667</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,548,270</td>
<td align="right">1,536,174</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">26,252,664</td>
<td align="right">26,101,438</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,079,894</td>
<td align="right">1,073,864</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">14,672,136</td>
<td align="right">14,593,171</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,537,893</td>
<td align="right">3,519,137</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,495,045</td>
<td align="right">4,517,926</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,358,101</td>
<td align="right">9,312,712</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,449,498</td>
<td align="right">42,263,893</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,370,693</td>
<td align="right">2,380,998</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,849,720</td>
<td align="right">2,837,413</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">42,641,272</td>
<td align="right">42,488,646</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">14,623,602</td>
<td align="right">14,571,733</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,535,468</td>
<td align="right">3,524,540</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,251,152</td>
<td align="right">31,165,187</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,931,076</td>
<td align="right">2,923,052</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,910,117</td>
<td align="right">8,885,925</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">29,137,175</td>
<td align="right">29,061,239</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,539,346</td>
<td align="right">4,528,418</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,472,795</td>
<td align="right">2,467,158</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,582,694</td>
<td align="right">11,556,590</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,926,217</td>
<td align="right">2,920,187</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">172,945,085</td>
<td align="right">172,606,498</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,063,579</td>
<td align="right">1,065,653</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,580,371</td>
<td align="right">7,565,734</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,575,196</td>
<td align="right">2,579,985</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,066,196</td>
<td align="right">4,059,127</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">38,935,959</td>
<td align="right">39,003,521</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">916,494</td>
<td align="right">917,978</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,785,796</td>
<td align="right">4,793,422</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,987,044</td>
<td align="right">1,990,062</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,329,901</td>
<td align="right">15,308,455</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2,746,834</td>
<td align="right">2,749,723</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,712,490</td>
<td align="right">9,703,171</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,431,299</td>
<td align="right">16,416,557</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">967,093</td>
<td align="right">966,283</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">53,112,737</td>
<td align="right">53,070,683</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,530,049</td>
<td align="right">5,525,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,115,171</td>
<td align="right">1,114,361</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">45,734,971</td>
<td align="right">45,765,465</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,453,437</td>
<td align="right">29,433,848</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,329,017</td>
<td align="right">9,324,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,769,602</td>
<td align="right">6,772,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,025,979</td>
<td align="right">4,027,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,887,562</td>
<td align="right">8,890,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">581,573</td>
<td align="right">581,713</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,697,721</td>
<td align="right">4,698,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,699,356</td>
<td align="right">6,698,287</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,991,118</td>
<td align="right">3,991,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">50,226</td>
<td align="right">50,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,185,650</td>
<td align="right">46,188,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">7,992,190</td>
<td align="right">7,992,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">703,476</td>
<td align="right">703,472</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,562,842</td>
<td align="right">1,562,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">959,409</td>
<td align="right">959,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,705,203</td>
<td align="right">11,705,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,220,139</td>
<td align="right">11,220,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,019,622</td>
<td align="right">10,019,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,862</td>
<td align="right">8,152,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,096,790</td>
<td align="right">8,096,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,927,483</td>
<td align="right">6,927,483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,493,721</td>
<td align="right">6,493,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,643,637</td>
<td align="right">5,643,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,334,244</td>
<td align="right">5,334,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,314,516</td>
<td align="right">4,314,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,856,186</td>
<td align="right">2,856,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,649,464</td>
<td align="right">2,649,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,614,040</td>
<td align="right">2,614,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,992,685</td>
<td align="right">1,992,685</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,984,106</td>
<td align="right">1,984,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,943,842</td>
<td align="right">1,943,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,927,679</td>
<td align="right">1,927,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,806,040</td>
<td align="right">1,806,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,798,476</td>
<td align="right">1,798,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,705,703</td>
<td align="right">1,705,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,640,801</td>
<td align="right">1,640,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,623,478</td>
<td align="right">1,623,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,499,290</td>
<td align="right">1,499,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,424,440</td>
<td align="right">1,424,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,392,003</td>
<td align="right">1,392,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,149,140</td>
<td align="right">1,149,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,045,209</td>
<td align="right">1,045,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">998,492</td>
<td align="right">998,492</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">974,095</td>
<td align="right">974,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">849,921</td>
<td align="right">849,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">822,990</td>
<td align="right">822,990</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">735,102</td>
<td align="right">735,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">690,206</td>
<td align="right">690,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">667,298</td>
<td align="right">667,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">663,236</td>
<td align="right">663,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">657,616</td>
<td align="right">657,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">615,300</td>
<td align="right">615,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">615,300</td>
<td align="right">615,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,464</td>
<td align="right">582,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">579,568</td>
<td align="right">579,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">555,828</td>
<td align="right">555,828</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">514,769</td>
<td align="right">514,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">465,880</td>
<td align="right">465,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">446,275</td>
<td align="right">446,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">438,777</td>
<td align="right">438,777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,669</td>
<td align="right">353,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">307,447</td>
<td align="right">307,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">296,835</td>
<td align="right">296,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">281,324</td>
<td align="right">281,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,898</td>
<td align="right">280,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">266,985</td>
<td align="right">266,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">258,617</td>
<td align="right">258,617</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">253,967</td>
<td align="right">253,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">225,567</td>
<td align="right">225,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,604</td>
<td align="right">165,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,174</td>
<td align="right">163,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">127,254</td>
<td align="right">127,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,560</td>
<td align="right">122,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,792</td>
<td align="right">108,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,224</td>
<td align="right">98,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84,680</td>
<td align="right">84,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84,380</td>
<td align="right">84,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">82,708</td>
<td align="right">82,708</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,258</td>
<td align="right">76,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,426</td>
<td align="right">72,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">63,916</td>
<td align="right">63,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,564</td>
<td align="right">55,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">43,007</td>
<td align="right">43,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">42,343</td>
<td align="right">42,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,479</td>
<td align="right">31,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">23,350</td>
<td align="right">23,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,679</td>
<td align="right">19,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,968</td>
<td align="right">18,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">10,977</td>
<td align="right">10,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,657</td>
<td align="right">5,657</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">5,547</td>
<td align="right">5,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,039</td>
<td align="right">3,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,949</td>
<td align="right">2,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,428</td>
<td align="right">2,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,305</td>
<td align="right">1,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,133</td>
<td align="right">1,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,081</td>
<td align="right">1,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">954</td>
<td align="right">954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">777</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">723</td>
<td align="right">723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">589</td>
<td align="right">589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">235</td>
<td align="right">235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">214</td>
<td align="right">214</td>
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
<td align="right">33</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
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
<td align="right">732,284</td>
<td align="right">10.8%</td>
<td align="right">732,284</td>
<td align="right">10.8%</td>
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
<td align="right">6,066,088</td>
<td align="right">89.2%</td>
<td align="right">6,066,088</td>
<td align="right">89.2%</td>
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
<td align="right">480</td>
<td align="right">17.0%</td>
<td align="right">480</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,338</td>
<td align="right">83.0%</td>
<td align="right">2,338</td>
<td align="right">83.0%</td>
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
<td align="left">add other</td>
<td align="right">998</td>
<td align="right">42.7%</td>
<td align="right">998</td>
<td align="right">42.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">232</td>
<td align="right">9.9%</td>
<td align="right">232</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">210</td>
<td align="right">9.0%</td>
<td align="right">210</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.4%</td>
<td align="right">173</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">156</td>
<td align="right">6.7%</td>
<td align="right">156</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">148</td>
<td align="right">6.3%</td>
<td align="right">148</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">2.8%</td>
<td align="right">66</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">1.5%</td>
<td align="right">36</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.4%</td>
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
<td align="right">446,275</td>
<td align="right">100.0%</td>
<td align="right">446,275</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,806</td>
<td align="right">0.5%</td>
<td align="right">58,396</td>
<td align="right">0.4%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,945,055</td>
<td align="right">14.2%</td>
<td align="right">1,989,331</td>
<td align="right">14.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,644,816</td>
<td align="right">85.2%</td>
<td align="right">11,606,056</td>
<td align="right">84.9%</td>
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
<td align="right">2,599</td>
<td align="right">30.7%</td>
<td align="right">12,301</td>
<td align="right">44.1%</td>
<td align="right">373.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,856</td>
<td align="right">69.3%</td>
<td align="right">15,598</td>
<td align="right">55.9%</td>
<td align="right">166.4%</td>
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
<td align="right">2,690</td>
<td align="right">45.9%</td>
<td align="right">12,434</td>
<td align="right">79.7%</td>
<td align="right">362.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">780</td>
<td align="right">5.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">845</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">782</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">690</td>
<td align="right">11.8%</td>
<td align="right">690</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">32</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">13</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,363,616</td>
<td align="right">88.3%</td>
<td align="right">61,625,108</td>
<td align="right">88.3%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,763,503</td>
<td align="right">11.4%</td>
<td align="right">7,905,557</td>
<td align="right">11.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">246,709</td>
<td align="right">0.4%</td>
<td align="right">246,709</td>
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
<td align="right">166,116</td>
<td align="right">99.8%</td>
<td align="right">1,570,886</td>
<td align="right">100.0%</td>
<td align="right">845.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">308</td>
<td align="right">0.2%</td>
<td align="right">308</td>
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
<td align="left">out of versions</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">62</td>
<td align="right">20.1%</td>
<td align="right">62</td>
<td align="right">20.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">6.8%</td>
<td align="right">21</td>
<td align="right">6.8%</td>
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
<td align="right">573,498</td>
<td align="right">99.6%</td>
<td align="right">571,820</td>
<td align="right">99.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">568</td>
<td align="right">0.1%</td>
<td align="right">568</td>
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
<td align="right">12,659</td>
<td align="right">100.0%</td>
<td align="right">19,203</td>
<td align="right">100.0%</td>
<td align="right">51.7%</td>
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
<td align="right">1,059,525</td>
<td align="right">5.8%</td>
<td align="right">1,061,599</td>
<td align="right">5.8%</td>
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
<td align="right">17,217,799</td>
<td align="right">94.2%</td>
<td align="right">17,217,802</td>
<td align="right">94.2%</td>
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
<td align="right">3,370</td>
<td align="right">0.0%</td>
<td align="right">3,370</td>
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
<td align="right">1,538</td>
<td align="right">37.3%</td>
<td align="right">1,538</td>
<td align="right">37.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,583</td>
<td align="right">62.7%</td>
<td align="right">2,583</td>
<td align="right">62.7%</td>
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
<td align="left">different types</td>
<td align="right">1,109</td>
<td align="right">42.9%</td>
<td align="right">1,109</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">653</td>
<td align="right">25.3%</td>
<td align="right">653</td>
<td align="right">25.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">244</td>
<td align="right">9.4%</td>
<td align="right">244</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">194</td>
<td align="right">7.5%</td>
<td align="right">194</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">177</td>
<td align="right">6.9%</td>
<td align="right">177</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
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
<td align="right">2,465,849</td>
<td align="right">37.3%</td>
<td align="right">2,460,212</td>
<td align="right">37.3%</td>
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
<td align="right">4,103,558</td>
<td align="right">62.1%</td>
<td align="right">4,103,558</td>
<td align="right">62.2%</td>
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
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,561</td>
<td align="right">0.4%</td>
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
<td align="right">1,225</td>
<td align="right">16.4%</td>
<td align="right">1,225</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,232</td>
<td align="right">83.6%</td>
<td align="right">6,232</td>
<td align="right">83.6%</td>
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
<td align="right">3,249</td>
<td align="right">52.1%</td>
<td align="right">3,249</td>
<td align="right">52.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">529</td>
<td align="right">8.5%</td>
<td align="right">529</td>
<td align="right">8.5%</td>
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
<td align="right">224,860</td>
<td align="right">0.8%</td>
<td align="right">214,984</td>
<td align="right">0.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,865,853</td>
<td align="right">84.2%</td>
<td align="right">22,739,229</td>
<td align="right">84.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,056,407</td>
<td align="right">14.9%</td>
<td align="right">4,041,986</td>
<td align="right">15.0%</td>
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
<td align="right">5,371</td>
<td align="right">38.3%</td>
<td align="right">33,829</td>
<td align="right">67.9%</td>
<td align="right">529.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,656</td>
<td align="right">61.7%</td>
<td align="right">16,029</td>
<td align="right">32.1%</td>
<td align="right">85.2%</td>
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
<td align="right">4,243</td>
<td align="right">49.0%</td>
<td align="right">11,635</td>
<td align="right">72.6%</td>
<td align="right">174.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,208</td>
<td align="right">14.0%</td>
<td align="right">1,189</td>
<td align="right">7.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,408</td>
<td align="right">16.3%</td>
<td align="right">1,408</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">604</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">306</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">276</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">253</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">97</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">44</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">17</td>
<td align="right">0.2%</td>
<td align="right">17</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
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
<td align="right">33,897,539</td>
<td align="right">27.1%</td>
<td align="right">34,760,408</td>
<td align="right">27.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">81,356,004</td>
<td align="right">65.2%</td>
<td align="right">83,410,702</td>
<td align="right">65.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,532,791</td>
<td align="right">7.6%</td>
<td align="right">9,532,791</td>
<td align="right">7.5%</td>
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
<td align="right">207,304</td>
<td align="right">0.2%</td>
<td align="right">207,304</td>
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
<td align="right">699,050</td>
<td align="right">97.7%</td>
<td align="right">3,683,981</td>
<td align="right">99.6%</td>
<td align="right">427.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,262</td>
<td align="right">2.3%</td>
<td align="right">16,262</td>
<td align="right">0.4%</td>
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
<td align="left">mutable class</td>
<td align="right">5,310</td>
<td align="right">32.7%</td>
<td align="right">5,310</td>
<td align="right">32.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,652</td>
<td align="right">22.5%</td>
<td align="right">3,652</td>
<td align="right">22.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,573</td>
<td align="right">9.7%</td>
<td align="right">1,573</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,339</td>
<td align="right">8.2%</td>
<td align="right">1,339</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">989</td>
<td align="right">6.1%</td>
<td align="right">989</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">5.1%</td>
<td align="right">836</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">392</td>
<td align="right">2.4%</td>
<td align="right">392</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">318</td>
<td align="right">2.0%</td>
<td align="right">318</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.4%</td>
<td align="right">235</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">204</td>
<td align="right">1.3%</td>
<td align="right">204</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">102</td>
<td align="right">0.6%</td>
<td align="right">102</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">64</td>
<td align="right">0.4%</td>
<td align="right">64</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">55,696,339</td>
<td align="right">99.9%</td>
<td align="right">55,525,524</td>
<td align="right">99.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,289</td>
<td align="right">0.0%</td>
<td align="right">5,289</td>
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
<td align="right">550</td>
<td align="right">0.0%</td>
<td align="right">550</td>
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
<td align="right">9,762</td>
<td align="right">0.0%</td>
<td align="right">9,762</td>
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
<td align="right">18,196</td>
<td align="right">100.0%</td>
<td align="right">18,196</td>
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
<td align="right">138</td>
<td align="right">0.0%</td>
<td align="right">138</td>
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
<td align="right">721,432</td>
<td align="right">99.9%</td>
<td align="right">721,432</td>
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
<td align="right">451</td>
<td align="right">100.0%</td>
<td align="right">451</td>
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
<td align="right">6,490,756</td>
<td align="right">54.9%</td>
<td align="right">6,490,756</td>
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
<td align="right">5,334,244</td>
<td align="right">45.1%</td>
<td align="right">5,334,244</td>
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
<td align="right">1,384,384</td>
<td align="right">9.9%</td>
<td align="right">1,384,384</td>
<td align="right">9.9%</td>
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
<td align="right">10,785,395</td>
<td align="right">77.1%</td>
<td align="right">10,785,395</td>
<td align="right">77.1%</td>
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
<td align="right">1,804,693</td>
<td align="right">12.9%</td>
<td align="right">1,804,693</td>
<td align="right">12.9%</td>
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
<td align="right">38,357</td>
<td align="right">92.2%</td>
<td align="right">38,357</td>
<td align="right">92.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,247</td>
<td align="right">7.8%</td>
<td align="right">3,247</td>
<td align="right">7.8%</td>
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
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">606</td>
<td align="right">18.7%</td>
<td align="right">606</td>
<td align="right">18.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">284</td>
<td align="right">8.7%</td>
<td align="right">284</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">129</td>
<td align="right">4.0%</td>
<td align="right">129</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">39</td>
<td align="right">1.2%</td>
<td align="right">39</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">83,907</td>
<td align="right">3.1%</td>
<td align="right">83,907</td>
<td align="right">3.1%</td>
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
<td align="right">2,586,183</td>
<td align="right">96.8%</td>
<td align="right">2,586,183</td>
<td align="right">96.8%</td>
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
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430</td>
<td align="right">55.6%</td>
<td align="right">430</td>
<td align="right">55.6%</td>
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
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">8</td>
<td align="right">1.9%</td>
<td align="right">8</td>
<td align="right">1.9%</td>
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
<td align="right">3,032,011</td>
<td align="right">7.1%</td>
<td align="right">2,976,726</td>
<td align="right">7.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,046,741</td>
<td align="right">91.5%</td>
<td align="right">38,812,646</td>
<td align="right">91.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">565,574</td>
<td align="right">1.3%</td>
<td align="right">565,644</td>
<td align="right">1.3%</td>
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
<td align="right">64,233</td>
<td align="right">88.2%</td>
<td align="right">153,412</td>
<td align="right">94.7%</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,596</td>
<td align="right">11.8%</td>
<td align="right">8,666</td>
<td align="right">5.3%</td>
<td align="right">0.8%</td>
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
<td align="right">5,830</td>
<td align="right">67.8%</td>
<td align="right">5,900</td>
<td align="right">68.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">804</td>
<td align="right">9.4%</td>
<td align="right">804</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">7.7%</td>
<td align="right">665</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">564</td>
<td align="right">6.6%</td>
<td align="right">564</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">345</td>
<td align="right">4.0%</td>
<td align="right">345</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">317</td>
<td align="right">3.7%</td>
<td align="right">317</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,966,898</td>
<td align="right">90.4%</td>
<td align="right">7,962,551</td>
<td align="right">90.4%</td>
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
<td align="right">848,870</td>
<td align="right">9.6%</td>
<td align="right">848,870</td>
<td align="right">9.6%</td>
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
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">246</td>
<td align="right">23.4%</td>
<td align="right">246</td>
<td align="right">23.4%</td>
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
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">24</td>
<td align="right">9.8%</td>
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
<td align="right">47,399,588</td>
<td align="right">4.4%</td>
<td align="right">48,333,184</td>
<td align="right">4.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">405,875,629</td>
<td align="right">37.5%</td>
<td align="right">408,560,577</td>
<td align="right">37.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">30,044,385</td>
<td align="right">2.8%</td>
<td align="right">30,183,254</td>
<td align="right">2.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">600,274,874</td>
<td align="right">55.4%</td>
<td align="right">599,206,701</td>
<td align="right">55.2%</td>
<td align="right">-0.2%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,945,055</td>
<td align="right">6.5%</td>
<td align="right">1,989,331</td>
<td align="right">6.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,056,407</td>
<td align="right">13.6%</td>
<td align="right">4,041,986</td>
<td align="right">13.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,465,849</td>
<td align="right">8.3%</td>
<td align="right">2,460,212</td>
<td align="right">8.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,059,525</td>
<td align="right">3.5%</td>
<td align="right">1,061,599</td>
<td align="right">3.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">565,574</td>
<td align="right">1.9%</td>
<td align="right">565,644</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,532,791</td>
<td align="right">31.9%</td>
<td align="right">9,532,791</td>
<td align="right">31.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,490,756</td>
<td align="right">21.7%</td>
<td align="right">6,490,756</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,384,384</td>
<td align="right">4.6%</td>
<td align="right">1,384,384</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">848,870</td>
<td align="right">2.8%</td>
<td align="right">848,870</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">732,284</td>
<td align="right">2.5%</td>
<td align="right">732,284</td>
<td align="right">2.4%</td>
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
<td align="right">1,190,216</td>
<td align="right">2.5%</td>
<td align="right">1,270,838</td>
<td align="right">2.6%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,113,135</td>
<td align="right">34.0%</td>
<td align="right">16,904,160</td>
<td align="right">35.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,147,413</td>
<td align="right">6.6%</td>
<td align="right">3,278,287</td>
<td align="right">6.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">930,820</td>
<td align="right">2.0%</td>
<td align="right">907,498</td>
<td align="right">1.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,618,447</td>
<td align="right">5.5%</td>
<td align="right">2,569,947</td>
<td align="right">5.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,769,689</td>
<td align="right">12.2%</td>
<td align="right">5,709,980</td>
<td align="right">11.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,049,071</td>
<td align="right">17.0%</td>
<td align="right">7,981,516</td>
<td align="right">16.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">5,591,273</td>
<td align="right">11.8%</td>
<td align="right">5,637,741</td>
<td align="right">11.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,804,610</td>
<td align="right">3.8%</td>
<td align="right">1,804,610</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">533,301</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">535,945</td>
<td align="right">1.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">388,604</td>
<td align="right">0.6%</td>
<td align="right">364,079</td>
<td align="right">0.5%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,091,352</td>
<td align="right">1.6%</td>
<td align="right">1,103,104</td>
<td align="right">1.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,557,450</td>
<td align="right">9.5%</td>
<td align="right">6,532,925</td>
<td align="right">9.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,558,556</td>
<td align="right">9.5%</td>
<td align="right">6,534,031</td>
<td align="right">9.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,914,555</td>
<td align="right">17.2%</td>
<td align="right">11,893,983</td>
<td align="right">17.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,914,555</td>
<td align="right">17.2%</td>
<td align="right">11,893,983</td>
<td align="right">17.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,355,999</td>
<td align="right">7.7%</td>
<td align="right">5,359,952</td>
<td align="right">7.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,322,610</td>
<td align="right">82.8%</td>
<td align="right">57,348,720</td>
<td align="right">82.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,794,238</td>
<td align="right">69.0%</td>
<td align="right">47,794,244</td>
<td align="right">69.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">453,513</td>
<td align="right">0.7%</td>
<td align="right">453,513</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,161,561</td>
<td align="right">1.7%</td>
<td align="right">1,161,561</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="right">212,233</td>
<td align="right"></td>
<td align="right">264,448</td>
<td align="right"></td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,882,871</td>
<td align="right"></td>
<td align="right">1,942,583</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,471,241</td>
<td align="right"></td>
<td align="right">53,393,973</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">326,174,052</td>
<td align="right">26.8%</td>
<td align="right">329,221,014</td>
<td align="right">27.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">202,200,925</td>
<td align="right">18.4%</td>
<td align="right">201,091,530</td>
<td align="right">18.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,672,652</td>
<td align="right"></td>
<td align="right">1,680,302</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,706,530</td>
<td align="right"></td>
<td align="right">28,805,589</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">424,485,940</td>
<td align="right">38.6%</td>
<td align="right">425,919,331</td>
<td align="right">38.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">181,722,668</td>
<td align="right">14.9%</td>
<td align="right">181,169,936</td>
<td align="right">14.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">65,996,765</td>
<td align="right"></td>
<td align="right">65,819,881</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">351,374,553</td>
<td align="right">32.0%</td>
<td align="right">352,304,885</td>
<td align="right">32.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,021,766</td>
<td align="right">70.2%</td>
<td align="right">66,849,398</td>
<td align="right">70.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">67,374,321</td>
<td align="right">70.6%</td>
<td align="right">67,202,025</td>
<td align="right">70.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">530,896,144</td>
<td align="right">43.6%</td>
<td align="right">530,044,766</td>
<td align="right">43.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">177,591,831</td>
<td align="right">14.6%</td>
<td align="right">177,487,420</td>
<td align="right">14.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,672</td>
<td align="right">0.0%</td>
<td align="right">38,693</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">120,579,261</td>
<td align="right">11.0%</td>
<td align="right">120,609,955</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">313,883</td>
<td align="right">0.3%</td>
<td align="right">313,934</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,067,358</td>
<td align="right">29.4%</td>
<td align="right">28,067,365</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,093,469</td>
<td align="right"></td>
<td align="right">28,093,476</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,109,982</td>
<td align="right"></td>
<td align="right">1,109,982</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">99,233</td>
<td align="right">8.9%</td>
<td align="right">99,233</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">5,006</td>
<td align="right">0.5%</td>
<td align="right">5,006</td>
<td align="right">0.5%</td>
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
<td align="right">1,326</td>
<td align="right">28,085</td>
<td align="right">72,453,606</td>
<td align="right">11,391,322</td>
<td align="right">1,938,699</td>
<td align="right">1,326</td>
<td align="right">28,085</td>
<td align="right">72,452,585</td>
<td align="right">11,390,815</td>
<td align="right">1,938,893</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">65</td>
<td align="right">1.6%</td>
<td align="right">85</td>
<td align="right">2.1%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,127</td>
<td align="right">28.1%</td>
<td align="right">1,157</td>
<td align="right">28.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,805</td>
<td align="right">69.8%</td>
<td align="right">2,878</td>
<td align="right">70.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">29,309,414</td>
<td align="right"></td>
<td align="right">29,947,978</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">379,911,496</td>
<td align="right">1,296.2%</td>
<td align="right">386,051,723</td>
<td align="right">1,289.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,017</td>
<td align="right"></td>
<td align="right">4,079</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,212</td>
<td align="right">30.2%</td>
<td align="right">1,201</td>
<td align="right">29.4%</td>
<td align="right">-0.9%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">21 / 0 !!</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,741</td>
<td align="right">97.7%</td>
<td align="right">2,835</td>
<td align="right">98.5%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,805</td>
<td align="right"></td>
<td align="right">2,878</td>
<td align="right"></td>
<td align="right">2.6%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">257</td>
<td align="right">9.2%</td>
<td align="right">281</td>
<td align="right">9.8%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">659</td>
<td align="right">23.5%</td>
<td align="right">636</td>
<td align="right">22.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">846</td>
<td align="right">30.2%</td>
<td align="right">878</td>
<td align="right">30.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">765</td>
<td align="right">27.3%</td>
<td align="right">764</td>
<td align="right">26.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">214</td>
<td align="right">7.6%</td>
<td align="right">234</td>
<td align="right">8.1%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">64</td>
<td align="right">2.3%</td>
<td align="right">85</td>
<td align="right">3.0%</td>
<td align="right">32.8%</td>
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
<td align="right">230</td>
<td align="right">8.2%</td>
<td align="right">255</td>
<td align="right">8.9%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">534</td>
<td align="right">19.0%</td>
<td align="right">508</td>
<td align="right">17.7%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">355</td>
<td align="right">12.7%</td>
<td align="right">394</td>
<td align="right">13.7%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">932</td>
<td align="right">33.2%</td>
<td align="right">925</td>
<td align="right">32.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">627</td>
<td align="right">22.4%</td>
<td align="right">648</td>
<td align="right">22.5%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">63</td>
<td align="right">2.2%</td>
<td align="right">105</td>
<td align="right">3.6%</td>
<td align="right">66.7%</td>
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
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,393</td>
<td align="right">20,340</td>
<td align="right">218.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,265</td>
<td align="right">228</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">15,378</td>
<td align="right">27,685</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">29,882</td>
<td align="right">53,613</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">497,282</td>
<td align="right">855,409</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">229,700</td>
<td align="right">64,712</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">533,296</td>
<td align="right">175,946</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,196</td>
<td align="right">4,956</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">553,750</td>
<td align="right">201,063</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">1,003,325</td>
<td align="right">1,503,687</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,672</td>
<td align="right">2,598</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,265,631</td>
<td align="right">1,746,764</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,416,635</td>
<td align="right">3,246,088</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">42,366</td>
<td align="right">56,313</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,081,984</td>
<td align="right">1,546,097</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,253,752</td>
<td align="right">940,709</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">415,419</td>
<td align="right">314,421</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,332,782</td>
<td align="right">2,652,905</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">708,416</td>
<td align="right">800,628</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">734,309</td>
<td align="right">826,521</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">574,648</td>
<td align="right">645,898</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">489,934</td>
<td align="right">541,803</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">265,158</td>
<td align="right">238,905</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">358,038</td>
<td align="right">390,635</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,465,213</td>
<td align="right">2,685,599</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">817</td>
<td align="right">749</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">820,384</td>
<td align="right">886,401</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,025,891</td>
<td align="right">1,104,859</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">475,197</td>
<td align="right">507,454</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,795,477</td>
<td align="right">2,606,845</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">555,304</td>
<td align="right">588,552</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">321,129</td>
<td align="right">339,885</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">472,628</td>
<td align="right">445,046</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">109,134</td>
<td align="right">115,164</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">250,566</td>
<td align="right">237,346</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">253,197</td>
<td align="right">239,954</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,457,311</td>
<td align="right">1,529,297</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,747,176</td>
<td align="right">1,828,589</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">129,798</td>
<td align="right">135,828</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">957,946</td>
<td align="right">997,776</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">34,206,435</td>
<td align="right">35,473,674</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,810,016</td>
<td align="right">2,906,779</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">13,710,330</td>
<td align="right">13,277,865</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">327,682</td>
<td align="right">336,525</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,854,003</td>
<td align="right">25,517,434</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">23,617,416</td>
<td align="right">24,215,175</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,350,807</td>
<td align="right">2,292,691</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">365,196</td>
<td align="right">373,798</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">29,309,414</td>
<td align="right">29,947,978</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">858,621</td>
<td align="right">840,094</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,332,033</td>
<td align="right">4,241,782</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,013,484</td>
<td align="right">4,089,974</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">34,196,923</td>
<td align="right">34,839,243</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,740,869</td>
<td align="right">1,770,074</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">485,468</td>
<td align="right">493,492</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,033,487</td>
<td align="right">3,082,115</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">578,778</td>
<td align="right">570,410</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">574,998</td>
<td align="right">566,715</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">126,099</td>
<td align="right">127,902</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,061,340</td>
<td align="right">1,075,977</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,636,327</td>
<td align="right">4,698,714</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">564,186</td>
<td align="right">556,705</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,219,370</td>
<td align="right">5,287,757</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,697,229</td>
<td align="right">20,966,038</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,493,273</td>
<td align="right">6,575,475</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,863,552</td>
<td align="right">4,923,946</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">65,806</td>
<td align="right">66,616</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">13,970,494</td>
<td align="right">14,140,180</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">229,304</td>
<td align="right">226,604</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">7,582,175</td>
<td align="right">7,664,530</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">410,256</td>
<td align="right">414,351</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,484,528</td>
<td align="right">5,538,808</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,087,548</td>
<td align="right">4,127,023</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,898,783</td>
<td align="right">1,916,127</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,483,139</td>
<td align="right">1,495,920</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,766,204</td>
<td align="right">7,833,073</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,632,446</td>
<td align="right">6,687,284</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,631,931</td>
<td align="right">6,685,567</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">390,477</td>
<td align="right">387,366</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,287,353</td>
<td align="right">4,320,259</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">528,755</td>
<td align="right">531,339</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,716,286</td>
<td align="right">3,730,274</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,715,192</td>
<td align="right">5,735,142</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,957,307</td>
<td align="right">2,967,305</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">353,154</td>
<td align="right">354,226</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,967,700</td>
<td align="right">3,978,595</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,457,118</td>
<td align="right">1,460,539</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">280,771</td>
<td align="right">280,288</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,714,577</td>
<td align="right">4,706,951</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,319,689</td>
<td align="right">4,326,270</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,084,274</td>
<td align="right">2,081,163</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">934,583</td>
<td align="right">935,870</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,700,380</td>
<td align="right">1,698,306</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,834,195</td>
<td align="right">1,832,121</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,047,213</td>
<td align="right">1,048,246</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,887,509</td>
<td align="right">4,891,265</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">266,388</td>
<td align="right">266,186</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,448,646</td>
<td align="right">1,449,718</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,636,566</td>
<td align="right">1,635,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,889,096</td>
<td align="right">2,890,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,323,283</td>
<td align="right">3,323,714</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,541,564</td>
<td align="right">2,541,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,227,755</td>
<td align="right">2,227,755</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,290</td>
<td align="right">1,207,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,164,555</td>
<td align="right">1,164,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,041,083</td>
<td align="right">1,041,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">975,423</td>
<td align="right">975,423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">651,252</td>
<td align="right">651,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">635,166</td>
<td align="right">635,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">592,788</td>
<td align="right">592,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">572,124</td>
<td align="right">572,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">374,208</td>
<td align="right">374,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">258,598</td>
<td align="right">258,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">229,313</td>
<td align="right">229,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">226,784</td>
<td align="right">226,784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">207,135</td>
<td align="right">207,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">173,254</td>
<td align="right">173,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">170,545</td>
<td align="right">170,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">139,200</td>
<td align="right">139,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,793</td>
<td align="right">128,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">124,919</td>
<td align="right">124,919</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">63,042</td>
<td align="right">63,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">39,816</td>
<td align="right">39,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">35,973</td>
<td align="right">35,973</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">33,075</td>
<td align="right">33,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">27,237</td>
<td align="right">27,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,712</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">121</td>
<td align="right">121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">121</td>
<td align="right">121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">115</td>
<td align="right">115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">115</td>
<td align="right">115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35</td>
<td align="right">35</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">35</td>
<td align="right">35</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">24,192</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">12,096</td>
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
<td align="right">61</td>
<td align="right">167</td>
<td align="right">173.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">448</td>
<td align="right">448</td>
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
<td align="right">37</td>
<td align="right">37</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
Stats gathered on: 2024-12-13
