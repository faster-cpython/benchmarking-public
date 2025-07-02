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
<td align="left">EXTENDED_ARG</td>
<td align="right">1,033,851</td>
<td align="right">17,787</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">591,150</td>
<td align="right">18,732</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">178,479</td>
<td align="right">5,817</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,511,894</td>
<td align="right">97,125</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">177,114</td>
<td align="right">7,770</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,817,988</td>
<td align="right">248,199</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">739,641</td>
<td align="right">38,892</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,059,660</td>
<td align="right">57,708</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">838,047</td>
<td align="right">47,250</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">783,951</td>
<td align="right">46,830</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,170,561</td>
<td align="right">79,485</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,217,223</td>
<td align="right">90,195</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">400,722</td>
<td align="right">30,660</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,335,264</td>
<td align="right">102,858</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">401,982</td>
<td align="right">31,920</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,540,014</td>
<td align="right">125,769</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,236,500</td>
<td align="right">183,834</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">297,612</td>
<td align="right">24,948</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">297,612</td>
<td align="right">24,948</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">148,932</td>
<td align="right">12,600</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,211,742</td>
<td align="right">110,838</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,224,257</td>
<td align="right">211,323</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">850,164</td>
<td align="right">81,732</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">656,376</td>
<td align="right">69,426</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">76,734</td>
<td align="right">9,198</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">86,856</td>
<td align="right">13,020</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">111,636</td>
<td align="right">24,129</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">103,488</td>
<td align="right">24,864</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">13,167</td>
<td align="right">3,171</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,153,780</td>
<td align="right">884,121</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,509,245</td>
<td align="right">1,732,395</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">142,149</td>
<td align="right">49,287</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">150,570</td>
<td align="right">54,012</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,290,636</td>
<td align="right">1,584,282</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,378,419</td>
<td align="right">665,196</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,455</td>
<td align="right">3,759</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,532,874</td>
<td align="right">812,784</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,019,725</td>
<td align="right">8,769,852</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,296</td>
<td align="right">10,080</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">13,921,299</td>
<td align="right">9,329,817</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,792,112</td>
<td align="right">6,021,309</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">12,327,420</td>
<td align="right">8,600,550</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,161,965</td>
<td align="right">20,753,565</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">15,386,805</td>
<td align="right">11,199,048</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">131,905,494</td>
<td align="right">99,581,433</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">46,898,376</td>
<td align="right">35,484,456</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">15,610,287</td>
<td align="right">12,961,893</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">16,258,515</td>
<td align="right">13,610,121</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">9,948,939</td>
<td align="right">8,453,949</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">30,485,091</td>
<td align="right">26,013,876</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,052,217</td>
<td align="right">8,583,666</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,874,830</td>
<td align="right">8,455,734</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">34,776</td>
<td align="right">29,988</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,893,368</td>
<td align="right">13,022,982</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">83,633,466</td>
<td align="right">73,391,829</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">14,638,764</td>
<td align="right">12,970,860</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">23,208,990</td>
<td align="right">20,790,420</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,205,812</td>
<td align="right">8,465,415</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48,547,086</td>
<td align="right">44,736,552</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">8,954,904</td>
<td align="right">8,378,076</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">17,876,838</td>
<td align="right">16,785,762</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">681,492</td>
<td align="right">645,540</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,443,960</td>
<td align="right">1,370,124</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">72,149,028</td>
<td align="right">69,643,707</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">47,138,784</td>
<td align="right">45,724,539</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,553,367</td>
<td align="right">4,517,415</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">46,244,898</td>
<td align="right">46,244,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">32,208,414</td>
<td align="right">32,208,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,913,803</td>
<td align="right">12,913,803</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">12,874,638</td>
<td align="right">12,874,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">12,866,994</td>
<td align="right">12,866,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,346,744</td>
<td align="right">8,346,744</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">8,314,950</td>
<td align="right">8,314,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,987,881</td>
<td align="right">1,987,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">65,289</td>
<td align="right">65,289</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">38,262</td>
<td align="right">38,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">29,253</td>
<td align="right">29,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,675</td>
<td align="right">24,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">22,554</td>
<td align="right">22,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">22,302</td>
<td align="right">22,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,945</td>
<td align="right">21,945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,614</td>
<td align="right">19,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">19,362</td>
<td align="right">19,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">18,312</td>
<td align="right">18,312</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">18,060</td>
<td align="right">18,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,372</td>
<td align="right">15,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14,868</td>
<td align="right">14,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">13,524</td>
<td align="right">13,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">13,461</td>
<td align="right">13,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">12,453</td>
<td align="right">12,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">12,012</td>
<td align="right">12,012</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,865</td>
<td align="right">11,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">11,088</td>
<td align="right">11,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,088</td>
<td align="right">11,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">9,975</td>
<td align="right">9,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">8,862</td>
<td align="right">8,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,316</td>
<td align="right">8,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,001</td>
<td align="right">8,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,833</td>
<td align="right">7,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">7,560</td>
<td align="right">7,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">7,308</td>
<td align="right">7,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,098</td>
<td align="right">7,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">5,544</td>
<td align="right">5,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,187</td>
<td align="right">5,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,704</td>
<td align="right">4,704</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">4,536</td>
<td align="right">4,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,864</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,528</td>
<td align="right">3,528</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,297</td>
<td align="right">3,297</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,108</td>
<td align="right">3,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,856</td>
<td align="right">2,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,688</td>
<td align="right">2,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,688</td>
<td align="right">2,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">2,604</td>
<td align="right">2,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">2,121</td>
<td align="right">2,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,953</td>
<td align="right">1,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,764</td>
<td align="right">1,764</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,428</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,344</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,176</td>
<td align="right">1,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">861</td>
<td align="right">861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">588</td>
<td align="right">588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">504</td>
<td align="right">504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">504</td>
<td align="right">504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">779,982</td>
<td align="right">2.2%</td>
<td align="right">43,743</td>
<td align="right">0.1%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,140,141</td>
<td align="right">97.8%</td>
<td align="right">34,140,141</td>
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
<td align="left">Failure</td>
<td align="right">2,730</td>
<td align="right">68.8%</td>
<td align="right">1,848</td>
<td align="right">59.9%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,239</td>
<td align="right">31.2%</td>
<td align="right">1,239</td>
<td align="right">40.1%</td>
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
<td align="right">1,554</td>
<td align="right">56.9%</td>
<td align="right">966</td>
<td align="right">52.3%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">819</td>
<td align="right">30.0%</td>
<td align="right">567</td>
<td align="right">30.7%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">147</td>
<td align="right">5.4%</td>
<td align="right">105</td>
<td align="right">5.7%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">126</td>
<td align="right">4.6%</td>
<td align="right">126</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">84</td>
<td align="right">3.1%</td>
<td align="right">84</td>
<td align="right">4.5%</td>
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
<td align="right">8,001</td>
<td align="right">100.0%</td>
<td align="right">8,001</td>
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
<td align="right">9,492</td>
<td align="right">0.0%</td>
<td align="right">5,229</td>
<td align="right">0.0%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">22,470</td>
<td align="right">0.0%</td>
<td align="right">18,270</td>
<td align="right">0.0%</td>
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
<td align="right">131,602,716</td>
<td align="right">100.0%</td>
<td align="right">131,606,916</td>
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
<td align="right">11,697</td>
<td align="right">100.0%</td>
<td align="right">11,634</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">1,008</td>
<td align="right">51.6%</td>
<td align="right">1,008</td>
<td align="right">51.6%</td>
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
<td align="right">945</td>
<td align="right">100.0%</td>
<td align="right">945</td>
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
<td align="right">3,150</td>
<td align="right">0.2%</td>
<td align="right">3,150</td>
<td align="right">0.2%</td>
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
<td align="right">1,447,299</td>
<td align="right">99.7%</td>
<td align="right">1,447,299</td>
<td align="right">99.7%</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">1,260</td>
<td align="right">81.1%</td>
<td align="right">1,260</td>
<td align="right">81.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">294</td>
<td align="right">18.9%</td>
<td align="right">294</td>
<td align="right">18.9%</td>
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
<td align="right">231</td>
<td align="right">78.6%</td>
<td align="right">231</td>
<td align="right">78.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">42</td>
<td align="right">14.3%</td>
<td align="right">42</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">21</td>
<td align="right">7.1%</td>
<td align="right">21</td>
<td align="right">7.1%</td>
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
<td align="right">4,808,853</td>
<td align="right">34.7%</td>
<td align="right">242,298</td>
<td align="right">2.6%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,056,502</td>
<td align="right">65.3%</td>
<td align="right">9,056,502</td>
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
<td align="right">8,967</td>
<td align="right">98.2%</td>
<td align="right">5,733</td>
<td align="right">97.2%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">168</td>
<td align="right">1.8%</td>
<td align="right">168</td>
<td align="right">2.8%</td>
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
<td align="right">8,526</td>
<td align="right">95.1%</td>
<td align="right">5,292</td>
<td align="right">92.3%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">252</td>
<td align="right">2.8%</td>
<td align="right">252</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">189</td>
<td align="right">2.1%</td>
<td align="right">189</td>
<td align="right">3.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,790,458</td>
<td align="right">30.1%</td>
<td align="right">2,087,757</td>
<td align="right">25.7%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,783,922</td>
<td align="right">69.8%</td>
<td align="right">6,014,799</td>
<td align="right">74.2%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">7,140</td>
<td align="right">87.2%</td>
<td align="right">5,460</td>
<td align="right">83.9%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,050</td>
<td align="right">12.8%</td>
<td align="right">1,050</td>
<td align="right">16.1%</td>
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
<td align="left">seq iter</td>
<td align="right">2,478</td>
<td align="right">34.7%</td>
<td align="right">1,806</td>
<td align="right">33.1%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,179</td>
<td align="right">58.5%</td>
<td align="right">3,171</td>
<td align="right">58.1%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">336</td>
<td align="right">4.7%</td>
<td align="right">336</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">84</td>
<td align="right">1.2%</td>
<td align="right">84</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">63</td>
<td align="right">0.9%</td>
<td align="right">63</td>
<td align="right">1.2%</td>
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
<td align="left">list</td>
<td align="right">9,064,398</td>
<td align="right">9,064,398 / 0 !!</td>
<td align="right">9,064,398</td>
<td align="right">9,064,398 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">8,407,749</td>
<td align="right">8,407,749 / 0 !!</td>
<td align="right">8,407,749</td>
<td align="right">8,407,749 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">23,016</td>
<td align="right">23,016 / 0 !!</td>
<td align="right">23,016</td>
<td align="right">23,016 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">8,568</td>
<td align="right">8,568 / 0 !!</td>
<td align="right">8,568</td>
<td align="right">8,568 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,176</td>
<td align="right">1,176 / 0 !!</td>
<td align="right">1,176</td>
<td align="right">1,176 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">273</td>
<td align="right">273 / 0 !!</td>
<td align="right">273</td>
<td align="right">273 / 0 !!</td>
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
<td align="right">15,369,942</td>
<td align="right">39.2%</td>
<td align="right">11,184,411</td>
<td align="right">33.6%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,820,846</td>
<td align="right">60.7%</td>
<td align="right">22,123,122</td>
<td align="right">66.4%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,148</td>
<td align="right">0.0%</td>
<td align="right">8,148</td>
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
<td align="right">10,626</td>
<td align="right">62.9%</td>
<td align="right">8,400</td>
<td align="right">57.2%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,279</td>
<td align="right">37.1%</td>
<td align="right">6,279</td>
<td align="right">42.8%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">9,618</td>
<td align="right">90.5%</td>
<td align="right">7,392</td>
<td align="right">88.0%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">714</td>
<td align="right">6.7%</td>
<td align="right">714</td>
<td align="right">8.5%</td>
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
<td align="right">45,501,834</td>
<td align="right">99.9%</td>
<td align="right">34,780,746</td>
<td align="right">99.9%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,613</td>
<td align="right">0.0%</td>
<td align="right">11,613</td>
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
<td align="right">357</td>
<td align="right">0.0%</td>
<td align="right">357</td>
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
<td align="right">2,982</td>
<td align="right">0.0%</td>
<td align="right">2,982</td>
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
<td align="right">10,332</td>
<td align="right">100.0%</td>
<td align="right">10,332</td>
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
<td align="right">1,596</td>
<td align="right">95.0%</td>
<td align="right">1,596</td>
<td align="right">95.0%</td>
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
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">84</td>
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
<td align="right">14,658</td>
<td align="right">0.1%</td>
<td align="right">14,658</td>
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
<td align="right">12,874,638</td>
<td align="right">99.9%</td>
<td align="right">12,874,638</td>
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
<td align="right">42</td>
<td align="right">20.0%</td>
<td align="right">42</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">168</td>
<td align="right">80.0%</td>
<td align="right">168</td>
<td align="right">80.0%</td>
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
<td align="right">168</td>
<td align="right">100.0%</td>
<td align="right">168</td>
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
<td align="right">1,374,996</td>
<td align="right">14.1%</td>
<td align="right">662,340</td>
<td align="right">7.3%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,342,082</td>
<td align="right">85.8%</td>
<td align="right">8,342,082</td>
<td align="right">92.6%</td>
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
<td align="right">4,746</td>
<td align="right">0.0%</td>
<td align="right">4,746</td>
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
<td align="right">2,436</td>
<td align="right">70.7%</td>
<td align="right">1,869</td>
<td align="right">65.0%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,008</td>
<td align="right">29.3%</td>
<td align="right">1,008</td>
<td align="right">35.0%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,869</td>
<td align="right">76.7%</td>
<td align="right">1,302</td>
<td align="right">69.7%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">252</td>
<td align="right">10.3%</td>
<td align="right">252</td>
<td align="right">13.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">210</td>
<td align="right">8.6%</td>
<td align="right">210</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">105</td>
<td align="right">4.3%</td>
<td align="right">105</td>
<td align="right">5.6%</td>
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
<td align="right">231</td>
<td align="right">0.3%</td>
<td align="right">231</td>
<td align="right">0.3%</td>
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
<td align="right">86,856</td>
<td align="right">99.6%</td>
<td align="right">86,856</td>
<td align="right">99.6%</td>
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
<td align="right">105</td>
<td align="right">71.4%</td>
<td align="right">105</td>
<td align="right">71.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42</td>
<td align="right">28.6%</td>
<td align="right">42</td>
<td align="right">28.6%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
<td align="right">100.0%</td>
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
<td align="right">178,017</td>
<td align="right">0.3%</td>
<td align="right">71,463</td>
<td align="right">0.1%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">58,098,600</td>
<td align="right">81.6%</td>
<td align="right">55,505,457</td>
<td align="right">81.0%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,906,873</td>
<td align="right">18.1%</td>
<td align="right">12,906,873</td>
<td align="right">18.8%</td>
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
<td align="right">6,300</td>
<td align="right">61.5%</td>
<td align="right">4,242</td>
<td align="right">51.8%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,948</td>
<td align="right">38.5%</td>
<td align="right">3,948</td>
<td align="right">48.2%</td>
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
<td align="right">3,612</td>
<td align="right">91.5%</td>
<td align="right">3,612</td>
<td align="right">91.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">336</td>
<td align="right">8.5%</td>
<td align="right">336</td>
<td align="right">8.5%</td>
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
<td align="right">672</td>
<td align="right">0.0%</td>
<td align="right">672</td>
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
<td align="right">14,272,020</td>
<td align="right">100.0%</td>
<td align="right">14,272,020</td>
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
<td align="right">672</td>
<td align="right">100.0%</td>
<td align="right">672</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">203,784</td>
<td align="right">0.0%</td>
<td align="right">92,946</td>
<td align="right">0.0%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">46,387,530</td>
<td align="right">5.2%</td>
<td align="right">31,356,171</td>
<td align="right">4.2%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">548,317,392</td>
<td align="right">61.5%</td>
<td align="right">456,078,819</td>
<td align="right">61.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">297,313,191</td>
<td align="right">33.3%</td>
<td align="right">254,725,632</td>
<td align="right">34.3%</td>
<td align="right">-14.3%</td>
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
<td align="right">4,808,853</td>
<td align="right">10.9%</td>
<td align="right">242,298</td>
<td align="right">0.8%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">779,982</td>
<td align="right">1.8%</td>
<td align="right">43,743</td>
<td align="right">0.1%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,374,996</td>
<td align="right">3.1%</td>
<td align="right">662,340</td>
<td align="right">2.1%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,783,922</td>
<td align="right">19.9%</td>
<td align="right">6,014,799</td>
<td align="right">19.3%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">15,369,942</td>
<td align="right">34.9%</td>
<td align="right">11,184,411</td>
<td align="right">35.9%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">22,470</td>
<td align="right">0.1%</td>
<td align="right">18,270</td>
<td align="right">0.1%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,906,873</td>
<td align="right">29.3%</td>
<td align="right">12,906,873</td>
<td align="right">41.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14,658</td>
<td align="right">0.0%</td>
<td align="right">14,658</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11,613</td>
<td align="right">0.0%</td>
<td align="right">11,613</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,001</td>
<td align="right">0.0%</td>
<td align="right">8,001</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">86,898</td>
<td align="right">42.6%</td>
<td align="right">31,164</td>
<td align="right">33.5%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">91,119</td>
<td align="right">44.7%</td>
<td align="right">40,299</td>
<td align="right">43.3%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,295</td>
<td align="right">4.1%</td>
<td align="right">4,032</td>
<td align="right">4.3%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">7,371</td>
<td align="right">3.6%</td>
<td align="right">7,371</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,746</td>
<td align="right">2.3%</td>
<td align="right">4,746</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,722</td>
<td align="right">0.8%</td>
<td align="right">1,722</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,260</td>
<td align="right">0.6%</td>
<td align="right">1,260</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">777</td>
<td align="right">0.4%</td>
<td align="right">777</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">357</td>
<td align="right">0.2%</td>
<td align="right">357</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">252</td>
<td align="right">0.1%</td>
<td align="right">252</td>
<td align="right">0.3%</td>
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
<td align="right">46,245,402</td>
<td align="right">53.2%</td>
<td align="right">46,245,402</td>
<td align="right">53.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,636,344</td>
<td align="right">46.8%</td>
<td align="right">40,636,344</td>
<td align="right">46.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">46,245,402</td>
<td align="right">53.2%</td>
<td align="right">46,245,402</td>
<td align="right">53.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">28,864,899</td>
<td align="right">33.2%</td>
<td align="right">28,864,899</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">17,380,503</td>
<td align="right">20.0%</td>
<td align="right">17,380,503</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">28,863,051</td>
<td align="right">33.2%</td>
<td align="right">28,863,051</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,764</td>
<td align="right">0.0%</td>
<td align="right">1,764</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">4,368</td>
<td align="right">0.0%</td>
<td align="right">4,368</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">10,626</td>
<td align="right">0.0%</td>
<td align="right">10,626</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">28,840,518</td>
<td align="right">33.2%</td>
<td align="right">28,840,518</td>
<td align="right">33.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">3,129</td>
<td align="right">0.0%</td>
<td align="right">3,129</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">54,650,022</td>
<td align="right">62.9%</td>
<td align="right">54,650,022</td>
<td align="right">62.9%</td>
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
<td align="right">219,011,982</td>
<td align="right">13.6%</td>
<td align="right">205,035,369</td>
<td align="right">12.7%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">319,209,282</td>
<td align="right">18.0%</td>
<td align="right">299,042,604</td>
<td align="right">16.9%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,419</td>
<td align="right"></td>
<td align="right">70,946</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,019,279,439</td>
<td align="right">57.6%</td>
<td align="right">1,041,411,392</td>
<td align="right">58.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">889,858,104</td>
<td align="right">55.3%</td>
<td align="right">905,790,501</td>
<td align="right">56.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">101,388</td>
<td align="right">0.0%</td>
<td align="right">102,438</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">11,095</td>
<td align="right"></td>
<td align="right">11,011</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">65,289</td>
<td align="right">0.0%</td>
<td align="right">65,688</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">69,904</td>
<td align="right"></td>
<td align="right">70,028</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">41,893,530</td>
<td align="right">2.6%</td>
<td align="right">41,819,694</td>
<td align="right">2.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">458,132,268</td>
<td align="right">28.5%</td>
<td align="right">458,216,035</td>
<td align="right">28.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">174,382,075</td>
<td align="right"></td>
<td align="right">174,386,544</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">121,460,351</td>
<td align="right"></td>
<td align="right">121,457,896</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">423,191,793</td>
<td align="right">23.9%</td>
<td align="right">423,197,474</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">173,400,277</td>
<td align="right">73.5%</td>
<td align="right">173,401,685</td>
<td align="right">73.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">45,306,989</td>
<td align="right"></td>
<td align="right">45,306,737</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">8,399,559</td>
<td align="right">0.5%</td>
<td align="right">8,399,601</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">62,622,253</td>
<td align="right"></td>
<td align="right">62,622,504</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">62,574,266</td>
<td align="right">26.5%</td>
<td align="right">62,574,454</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">173,233,600</td>
<td align="right">73.4%</td>
<td align="right">173,233,559</td>
<td align="right">73.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">20,118</td>
<td align="right"></td>
<td align="right">20,118</td>
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
<td align="right">11,844</td>
<td align="right">24,150</td>
<td align="right">289,381,274</td>
<td align="right">33,880,371</td>
<td align="right">12,606,741</td>
<td align="right">11,844</td>
<td align="right">24,570</td>
<td align="right">289,898,408</td>
<td align="right">33,792,087</td>
<td align="right">12,709,557</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">861</td>
<td align="right">11.6%</td>
<td align="right">2,373</td>
<td align="right">19.8%</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">441</td>
<td align="right">5.9%</td>
<td align="right">1,050</td>
<td align="right">8.8%</td>
<td align="right">138.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">126</td>
<td align="right">1.7%</td>
<td align="right">42</td>
<td align="right">0.4%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">273</td>
<td align="right">3.7%</td>
<td align="right">441</td>
<td align="right">3.7%</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">7,434</td>
<td align="right"></td>
<td align="right">11,970</td>
<td align="right"></td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,132</td>
<td align="right">82.5%</td>
<td align="right">8,547</td>
<td align="right">71.4%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">32,128,404</td>
<td align="right"></td>
<td align="right">37,780,071</td>
<td align="right"></td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,434,212,711</td>
<td align="right">7,576.5%</td>
<td align="right">2,749,031,796</td>
<td align="right">7,276.4%</td>
<td align="right">12.9%</td>
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

A potential trace is abandoned because it is too short.
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
<td align="right">210</td>
<td align="right">1.8%</td>
<td align="right">210 / 0 !!</td>
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
<td align="right">861</td>
<td align="right"></td>
<td align="right">2,373</td>
<td align="right"></td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">861</td>
<td align="right">100.0%</td>
<td align="right">2,352</td>
<td align="right">99.1%</td>
<td align="right">173.2%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">86,016</td>
<td align="right">0.6%</td>
<td align="right">344,064</td>
<td align="right">1.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">294,000</td>
<td align="right">2.2%</td>
<td align="right">771,456</td>
<td align="right">2.2%</td>
<td align="right">162.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">10,848,579</td>
<td align="right">81.4%</td>
<td align="right">28,290,423</td>
<td align="right">81.4%</td>
<td align="right">160.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">13,332,480</td>
<td align="right"></td>
<td align="right">34,750,464</td>
<td align="right"></td>
<td align="right">160.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,189,901</td>
<td align="right">16.4%</td>
<td align="right">5,688,585</td>
<td align="right">16.4%</td>
<td align="right">159.8%</td>
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
<td align="left">147</td>
<td align="right">17.1%</td>
<td align="left">336</td>
<td align="right">14.3%</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">378</td>
<td align="right">43.9%</td>
<td align="left">882</td>
<td align="right">37.5%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">21</td>
<td align="right">2.4%</td>
<td align="left">399</td>
<td align="right">17.0%</td>
<td align="right">1,800.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">189</td>
<td align="right">22.0%</td>
<td align="left">609</td>
<td align="right">25.9%</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">126</td>
<td align="right">14.6%</td>
<td align="left">126</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 32</td>
<td align="right">84</td>
<td align="right">9.8%</td>
<td align="right">147</td>
<td align="right">6.2%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">441</td>
<td align="right">51.2%</td>
<td align="right">1,029</td>
<td align="right">43.4%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">2.4%</td>
<td align="right">378</td>
<td align="right">15.9%</td>
<td align="right">1,700.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">189</td>
<td align="right">22.0%</td>
<td align="right">651</td>
<td align="right">27.4%</td>
<td align="right">244.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">126</td>
<td align="right">14.6%</td>
<td align="right">126</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">42</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
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
<td align="left"><= 32</td>
<td align="right">504</td>
<td align="right">58.5%</td>
<td align="right">966</td>
<td align="right">40.7%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">42</td>
<td align="right">4.9%</td>
<td align="right">336</td>
<td align="right">14.2%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">17.1%</td>
<td align="right">588</td>
<td align="right">24.8%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">168</td>
<td align="right">19.5%</td>
<td align="right">378</td>
<td align="right">15.9%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">42</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">42</td>
<td align="right">1.8%</td>
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
<td align="left">_DEOPT</td>
<td align="right">105</td>
<td align="right">42</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">466,116</td>
<td align="right">638,778</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">466,116</td>
<td align="right">638,778</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">466,116</td>
<td align="right">638,778</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">466,116</td>
<td align="right">638,778</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">466,116</td>
<td align="right">638,778</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">554,778</td>
<td align="right">703,542</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,109,556</td>
<td align="right">1,382,220</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,109,556</td>
<td align="right">1,382,220</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">554,778</td>
<td align="right">691,110</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">14,146,713</td>
<td align="right">17,171,007</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">7,047,978</td>
<td align="right">8,510,628</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">7,555,212</td>
<td align="right">9,050,202</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,769,815</td>
<td align="right">4,506,054</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">7,510,356</td>
<td align="right">8,929,389</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">7,510,356</td>
<td align="right">8,929,389</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">7,510,356</td>
<td align="right">8,924,601</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,510,356</td>
<td align="right">8,924,601</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,955,578</td>
<td align="right">8,249,136</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">24,750,180</td>
<td align="right">29,316,735</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,808,035</td>
<td align="right">4,508,784</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,808,035</td>
<td align="right">4,508,784</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">3,769,815</td>
<td align="right">4,463,172</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,510,356</td>
<td align="right">8,850,765</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">28,696,059</td>
<td align="right">33,815,145</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,321,086</td>
<td align="right">5,089,518</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,321,086</td>
<td align="right">5,089,518</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">32,128,299</td>
<td align="right">37,780,029</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">32,128,404</td>
<td align="right">37,780,071</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,184,652</td>
<td align="right">1,391,586</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">13,911,156</td>
<td align="right">16,316,223</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">21,648,081</td>
<td align="right">25,374,951</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">14,692,608</td>
<td align="right">17,197,866</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">7,736,925</td>
<td align="right">9,043,167</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">5,033,742</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,399,689</td>
<td align="right">5,121,480</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">25,316,256</td>
<td align="right">29,375,703</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">629,874</td>
<td align="right">730,212</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">7,736,925</td>
<td align="right">8,969,331</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">76,525,743</td>
<td align="right">88,710,867</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">551,271</td>
<td align="right">638,778</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">7,182,147</td>
<td align="right">8,309,175</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">72,601,032</td>
<td align="right">83,943,426</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,399,689</td>
<td align="right">5,081,622</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,182,147</td>
<td align="right">8,283,051</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">14,915,565</td>
<td align="right">17,185,224</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,182,147</td>
<td align="right">8,273,223</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">7,182,147</td>
<td align="right">8,273,223</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,182,147</td>
<td align="right">8,273,223</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">79,056,789</td>
<td align="right">90,973,134</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">31,367,952</td>
<td align="right">36,002,610</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">20,240,304</td>
<td align="right">23,227,659</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">74,034,429</td>
<td align="right">84,516,453</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">49,601,916</td>
<td align="right">56,309,883</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">17,562,090</td>
<td align="right">19,925,493</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">15,268,680</td>
<td align="right">17,321,346</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">15,208,578</td>
<td align="right">17,214,561</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">15,208,578</td>
<td align="right">17,214,561</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">15,986,418</td>
<td align="right">18,001,767</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">72,535,617</td>
<td align="right">81,617,949</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">56,232,162</td>
<td align="right">63,218,841</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">467,448,408</td>
<td align="right">525,117,978</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">430,910,298</td>
<td align="right">484,005,459</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">15,406,587</td>
<td align="right">17,266,977</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">33,562,032</td>
<td align="right">37,537,458</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">14,940,471</td>
<td align="right">16,638,195</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">21,746,214</td>
<td align="right">24,174,948</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">14,940,471</td>
<td align="right">16,608,375</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">83,582,604</td>
<td align="right">92,799,273</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,427,824</td>
<td align="right">10,429,776</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,427,824</td>
<td align="right">10,429,776</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">34,134,450</td>
<td align="right">37,756,698</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">25,123,266</td>
<td align="right">27,771,660</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">12,727,785</td>
<td align="right">14,064,960</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">34,322,967</td>
<td align="right">37,793,994</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">42,520,779</td>
<td align="right">46,706,310</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">8,464,932</td>
<td align="right">9,185,022</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">7,698,222</td>
<td align="right">8,285,172</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">7,698,222</td>
<td align="right">8,285,172</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">36,342,495</td>
<td align="right">39,111,618</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,758,324</td>
<td align="right">8,335,152</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">7,835,058</td>
<td align="right">8,379,042</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,464,932</td>
<td align="right">9,037,350</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">8,464,932</td>
<td align="right">9,037,350</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">19,868,457</td>
<td align="right">21,157,185</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">7,835,058</td>
<td align="right">8,343,090</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">17,473,512</td>
<td align="right">18,529,812</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">16,456,125</td>
<td align="right">17,246,922</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">13,870,962</td>
<td align="right">14,241,024</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,870,962</td>
<td align="right">14,241,024</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,686,310</td>
<td align="right">12,855,654</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">96,558</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">92,862</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">83,097</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">78,624</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">78,624</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">73,836</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">73,836</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">73,836</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">73,836</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">35,952</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">35,952</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">11,991</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">9,996</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">6,216</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">4,788</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">4,788</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">3,696</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-02
