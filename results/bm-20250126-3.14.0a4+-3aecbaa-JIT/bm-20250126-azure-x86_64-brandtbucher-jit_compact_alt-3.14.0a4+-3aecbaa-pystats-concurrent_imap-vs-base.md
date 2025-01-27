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
<td align="left">CALL_TUPLE_1</td>
<td align="right">14,867</td>
<td align="right">426,672</td>
<td align="right">2,769.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">175,083</td>
<td align="right">433,301</td>
<td align="right">147.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,197</td>
<td align="right">482,520</td>
<td align="right">139.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,280,162</td>
<td align="right">600</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">928,721</td>
<td align="right">244</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">453,862</td>
<td align="right">145</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">888,701</td>
<td align="right">296</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">800,043</td>
<td align="right">344</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">504,319</td>
<td align="right">384</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,440,740</td>
<td align="right">3,687</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,116,178</td>
<td align="right">1,149</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">192,909</td>
<td align="right">501</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,368</td>
<td align="right">68</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">85,741</td>
<td align="right">248</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">535,286</td>
<td align="right">1,746</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">97,305</td>
<td align="right">567</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">92,429</td>
<td align="right">542</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,636</td>
<td align="right">752</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">695</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">208</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">1,210</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">1,211</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">703,492</td>
<td align="right">9,483</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">209,706</td>
<td align="right">3,065</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">447</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,206,567</td>
<td align="right">34,981</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,772</td>
<td align="right">16,489</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">689</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">160</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">417</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">1,374</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">1,374</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">190,077</td>
<td align="right">4,332</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,051</td>
<td align="right">832</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,159,241</td>
<td align="right">30,041</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">464</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,580,779</td>
<td align="right">44,264</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">374</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">336,341</td>
<td align="right">9,863</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">336,664</td>
<td align="right">10,186</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,411,199</td>
<td align="right">43,235</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">2,386</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,248,418</td>
<td align="right">73,278</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">655,665</td>
<td align="right">22,409</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">1</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,355,891</td>
<td align="right">247,156</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">772</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">1</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,194,197</td>
<td align="right">204,593</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">187,022</td>
<td align="right">13,415</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">932,470</td>
<td align="right">68,327</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">303,640</td>
<td align="right">22,673</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,041,239</td>
<td align="right">763,734</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,843,773</td>
<td align="right">223,899</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">574,871</td>
<td align="right">46,117</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,393,551</td>
<td align="right">1,101,834</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">735,168</td>
<td align="right">68,425</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">510,982</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,640,167</td>
<td align="right">184,933</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,741,423</td>
<td align="right">2,060,044</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,218,725</td>
<td align="right">1,457,706</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,432</td>
<td align="right">10,580</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">141,361</td>
<td align="right">17,857</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">4,783,181</td>
<td align="right">658,271</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,302,960</td>
<td align="right">909,692</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">82,978</td>
<td align="right">153,777</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,812</td>
<td align="right">18,388</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,487,711</td>
<td align="right">243,108</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,045,041</td>
<td align="right">171,900</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">9,290</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">10,930,649</td>
<td align="right">2,073,494</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,874</td>
<td align="right">8,288</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,227,207</td>
<td align="right">857,591</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">13,476</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">9,513</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,896,710</td>
<td align="right">664,659</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">58,144,745</td>
<td align="right">14,603,308</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">697,380</td>
<td align="right">176,124</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,950,937</td>
<td align="right">509,738</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,177,659</td>
<td align="right">309,042</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,724,007</td>
<td align="right">2,054,616</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">587,222</td>
<td align="right">163,387</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,480,677</td>
<td align="right">1,279,725</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,023</td>
<td align="right">55,809</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">8,783</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,999,740</td>
<td align="right">3,707,629</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,570,011</td>
<td align="right">1,772,030</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">1,425,973</td>
<td align="right">475,782</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">549,391</td>
<td align="right">183,777</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,833,937</td>
<td align="right">3,992,299</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">725,791</td>
<td align="right">1,205,130</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,355,678</td>
<td align="right">7,785,608</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,442,452</td>
<td align="right">857,560</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,978,679</td>
<td align="right">1,401,605</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,404</td>
<td align="right">17,131</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">373,727</td>
<td align="right">143,614</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">2,883,052</td>
<td align="right">1,113,787</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,869,554</td>
<td align="right">755,394</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">19,513,497</td>
<td align="right">8,586,980</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,641,008</td>
<td align="right">2,052,192</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,119</td>
<td align="right">26,380</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">941,513</td>
<td align="right">421,046</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">938,243</td>
<td align="right">420,344</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,866</td>
<td align="right">26,449</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,658</td>
<td align="right">39,882</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,147,218</td>
<td align="right">566,635</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">34,277</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,335,573</td>
<td align="right">681,232</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">1,269,503</td>
<td align="right">656,803</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,297,752</td>
<td align="right">680,855</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">168,813</td>
<td align="right">90,447</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,145,071</td>
<td align="right">4,561,071</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">298</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">13,593</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">22,523</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">276</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,125,330</td>
<td align="right">1,570,490</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,091</td>
<td align="right">4,363</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">39,842</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,913</td>
<td align="right">421,868</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,711</td>
<td align="right">16,984</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">150</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">473</td>
<td align="right">462</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">313,520</td>
<td align="right">307,447</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,226</td>
<td align="right">3,177</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">87,032</td>
<td align="right">88,156</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,550</td>
<td align="right">4,504</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,606</td>
<td align="right">1,590</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,954,657</td>
<td align="right">8,032,724</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,488</td>
<td align="right">13,386</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,711</td>
<td align="right">17,609</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286</td>
<td align="right">10,227</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">351</td>
<td align="right">349</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">17,854</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,677</td>
<td align="right">1,818,675</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,310,128</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,862</td>
<td align="right">55,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,598</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,870</td>
<td align="right">9,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">8,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">806</td>
<td align="right">806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">267</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">28</td>
<td align="right">28</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,438,300</td>
<td align="right">69.2%</td>
<td align="right">3,120</td>
<td align="right">0.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">16,166</td>
<td align="right">0.3%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,954,454</td>
<td align="right">30.5%</td>
<td align="right">2,001,100</td>
<td align="right">99.8%</td>
<td align="right">2.4%</td>
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
<td align="right">2,322</td>
<td align="right">84.5%</td>
<td align="right">449</td>
<td align="right">78.9%</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">427</td>
<td align="right">15.5%</td>
<td align="right">120</td>
<td align="right">21.1%</td>
<td align="right">-71.9%</td>
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
<td align="left">or</td>
<td align="right">611</td>
<td align="right">26.3%</td>
<td align="right">40</td>
<td align="right">8.9%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,106</td>
<td align="right">47.6%</td>
<td align="right">96</td>
<td align="right">21.4%</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">8.1%</td>
<td align="right">32</td>
<td align="right">7.1%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">295</td>
<td align="right">12.7%</td>
<td align="right">158</td>
<td align="right">35.2%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">4.7%</td>
<td align="right">109</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">14</td>
<td align="right">0.6%</td>
<td align="right">14</td>
<td align="right">3.1%</td>
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
<td align="right">13,887</td>
<td align="right">100.0%</td>
<td align="right">772</td>
<td align="right">100.0%</td>
<td align="right">-94.4%</td>
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
<td align="right">40,608</td>
<td align="right">7.2%</td>
<td align="right">8,104</td>
<td align="right">1.5%</td>
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
<td align="right">520,214</td>
<td align="right">92.7%</td>
<td align="right">530,372</td>
<td align="right">98.5%</td>
<td align="right">2.0%</td>
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
<td align="right">148</td>
<td align="right">55.6%</td>
<td align="right">66</td>
<td align="right">35.9%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">44.4%</td>
<td align="right">118</td>
<td align="right">64.1%</td>
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
<td align="right">147</td>
<td align="right">99.3%</td>
<td align="right">65</td>
<td align="right">98.5%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">1.5%</td>
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
<td align="right">20,724,540</td>
<td align="right">100.0%</td>
<td align="right">21,195,911</td>
<td align="right">100.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,186</td>
<td align="right">0.0%</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">795</td>
<td align="right">0.0%</td>
<td align="right">795</td>
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
<td align="right">3,365</td>
<td align="right">100.0%</td>
<td align="right">3,345</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">16,500</td>
<td align="right">0.4%</td>
<td align="right">4,284</td>
<td align="right">0.1%</td>
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
<td align="right">586,056</td>
<td align="right">12.9%</td>
<td align="right">162,801</td>
<td align="right">3.9%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,922,214</td>
<td align="right">86.7%</td>
<td align="right">3,984,048</td>
<td align="right">96.0%</td>
<td align="right">1.6%</td>
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
<td align="right">897</td>
<td align="right">61.1%</td>
<td align="right">316</td>
<td align="right">48.3%</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">571</td>
<td align="right">38.9%</td>
<td align="right">338</td>
<td align="right">51.7%</td>
<td align="right">-40.8%</td>
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
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">10.7%</td>
<td align="right">7</td>
<td align="right">2.2%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">602</td>
<td align="right">67.1%</td>
<td align="right">111</td>
<td align="right">35.1%</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">154</td>
<td align="right">17.2%</td>
<td align="right">153</td>
<td align="right">48.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.9%</td>
<td align="right">44</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,491,144</td>
<td align="right">100.0%</td>
<td align="right">1,527,342</td>
<td align="right">100.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">270</td>
<td align="right">0.0%</td>
<td align="right">270</td>
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
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">82.7%</td>
<td align="right">43</td>
<td align="right">82.7%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">115,483</td>
<td align="right">1.8%</td>
<td align="right">18,153</td>
<td align="right">0.4%</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,300,672</td>
<td align="right">98.2%</td>
<td align="right">4,932,561</td>
<td align="right">99.6%</td>
<td align="right">-21.7%</td>
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
<td align="right">276</td>
<td align="right">83.9%</td>
<td align="right">183</td>
<td align="right">77.9%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">53</td>
<td align="right">16.1%</td>
<td align="right">52</td>
<td align="right">22.1%</td>
<td align="right">-1.9%</td>
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
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">26</td>
<td align="right">14.2%</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">32</td>
<td align="right">17.5%</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">56</td>
<td align="right">30.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">56</td>
<td align="right">30.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">7</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
<td align="right">5,347,717</td>
<td align="right">13.3%</td>
<td align="right">242,113</td>
<td align="right">0.7%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">217,275</td>
<td align="right">0.5%</td>
<td align="right">52,991</td>
<td align="right">0.1%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,600,101</td>
<td align="right">86.1%</td>
<td align="right">36,730,238</td>
<td align="right">99.2%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">4,912</td>
<td align="right">40.7%</td>
<td align="right">1,866</td>
<td align="right">31.2%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,169</td>
<td align="right">59.3%</td>
<td align="right">4,107</td>
<td align="right">68.8%</td>
<td align="right">-42.7%</td>
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
<td align="right">1,468</td>
<td align="right">29.9%</td>
<td align="right">274</td>
<td align="right">14.7%</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.4%</td>
<td align="right">24</td>
<td align="right">1.3%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">208</td>
<td align="right">4.2%</td>
<td align="right">75</td>
<td align="right">4.0%</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.4%</td>
<td align="right">26</td>
<td align="right">1.4%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,409</td>
<td align="right">28.7%</td>
<td align="right">579</td>
<td align="right">31.0%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.4%</td>
<td align="right">196</td>
<td align="right">10.5%</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">308</td>
<td align="right">6.3%</td>
<td align="right">285</td>
<td align="right">15.3%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">1.2%</td>
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
<td align="right">15,571,348</td>
<td align="right">100.0%</td>
<td align="right">22,548,358</td>
<td align="right">100.0%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">833</td>
<td align="right">0.0%</td>
<td align="right">807</td>
<td align="right">0.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">309</td>
<td align="right">0.0%</td>
<td align="right">309</td>
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
<td align="right">2,402</td>
<td align="right">100.0%</td>
<td align="right">2,379</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">59,589</td>
<td align="right">4.0%</td>
<td align="right">10,172</td>
<td align="right">2.1%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,422,402</td>
<td align="right">95.7%</td>
<td align="right">473,654</td>
<td align="right">97.5%</td>
<td align="right">-66.7%</td>
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
<td align="right">2,374</td>
<td align="right">51.2%</td>
<td align="right">946</td>
<td align="right">41.0%</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,261</td>
<td align="right">48.8%</td>
<td align="right">1,361</td>
<td align="right">59.0%</td>
<td align="right">-39.8%</td>
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
<td align="right">138</td>
<td align="right">5.8%</td>
<td align="right">49</td>
<td align="right">5.2%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,726</td>
<td align="right">72.7%</td>
<td align="right">708</td>
<td align="right">74.8%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">kind 18</td>
<td align="right">45</td>
<td align="right">1.9%</td>
<td align="right">45</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
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
<td align="right">1,728,361</td>
<td align="right">100.0%</td>
<td align="right">1,785,115</td>
<td align="right">100.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
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
<td align="right">24</td>
<td align="right">100.0%</td>
<td align="right">24</td>
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
<td align="right">9</td>
<td align="right">22.5%</td>
<td align="right">9</td>
<td align="right">22.5%</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">31</td>
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
<td align="right">140,400</td>
<td align="right">3.1%</td>
<td align="right">30,829</td>
<td align="right">0.7%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,937</td>
<td align="right">1.8%</td>
<td align="right">38,383</td>
<td align="right">0.8%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,315,719</td>
<td align="right">95.1%</td>
<td align="right">4,525,900</td>
<td align="right">98.5%</td>
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
<td align="left">Success</td>
<td align="right">3,614</td>
<td align="right">82.9%</td>
<td align="right">1,570</td>
<td align="right">75.0%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.1%</td>
<td align="right">522</td>
<td align="right">25.0%</td>
<td align="right">-29.7%</td>
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
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">124</td>
<td align="right">23.8%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">692</td>
<td align="right">93.1%</td>
<td align="right">311</td>
<td align="right">59.6%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">205</td>
<td align="right">39.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
<td align="right">10</td>
<td align="right">1.9%</td>
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
<td align="right">21,264</td>
<td align="right">1.3%</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,556,216</td>
<td align="right">98.6%</td>
<td align="right">1,587,485</td>
<td align="right">100.0%</td>
<td align="right">2.0%</td>
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
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">53</td>
<td align="right">76.8%</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">16</td>
<td align="right">23.2%</td>
<td align="right">-5.9%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">29</td>
<td align="right">54.7%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">24</td>
<td align="right">45.3%</td>
<td align="right">-64.7%</td>
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
<td align="right">173,865</td>
<td align="right">1.7%</td>
<td align="right">432,327</td>
<td align="right">4.1%</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,840,276</td>
<td align="right">98.3%</td>
<td align="right">10,129,214</td>
<td align="right">95.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">757</td>
<td align="right">62.2%</td>
<td align="right">518</td>
<td align="right">53.2%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">461</td>
<td align="right">37.8%</td>
<td align="right">456</td>
<td align="right">46.8%</td>
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
<td align="left">sequence</td>
<td align="right">145</td>
<td align="right">19.2%</td>
<td align="right">56</td>
<td align="right">10.8%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">309</td>
<td align="right">40.8%</td>
<td align="right">141</td>
<td align="right">27.2%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">126</td>
<td align="right">16.6%</td>
<td align="right">188</td>
<td align="right">36.3%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">14.7%</td>
<td align="right">67</td>
<td align="right">12.9%</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">8.6%</td>
<td align="right">65</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
<td align="right">2,054,893</td>
<td align="right">100.0%</td>
<td align="right">2,065,027</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,267,106</td>
<td align="right">3.7%</td>
<td align="right">1,399,463</td>
<td align="right">1.6%</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">451,123</td>
<td align="right">0.1%</td>
<td align="right">99,468</td>
<td align="right">0.1%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">116,692,280</td>
<td align="right">34.8%</td>
<td align="right">30,333,466</td>
<td align="right">34.3%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">205,839,195</td>
<td align="right">61.4%</td>
<td align="right">56,591,052</td>
<td align="right">64.0%</td>
<td align="right">-72.5%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">173,865</td>
<td align="right">1.4%</td>
<td align="right">432,327</td>
<td align="right">31.3%</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,438,300</td>
<td align="right">36.3%</td>
<td align="right">3,120</td>
<td align="right">0.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,347,717</td>
<td align="right">43.7%</td>
<td align="right">242,113</td>
<td align="right">17.5%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,483</td>
<td align="right">0.9%</td>
<td align="right">18,153</td>
<td align="right">1.3%</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,608</td>
<td align="right">0.3%</td>
<td align="right">8,104</td>
<td align="right">0.6%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">586,056</td>
<td align="right">4.8%</td>
<td align="right">162,801</td>
<td align="right">11.8%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">1,422,402</td>
<td align="right">11.6%</td>
<td align="right">473,654</td>
<td align="right">34.3%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.7%</td>
<td align="right">38,383</td>
<td align="right">2.8%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,160</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">807</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">59,589</td>
<td align="right">13.2%</td>
<td align="right">10,172</td>
<td align="right">10.2%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">31.1%</td>
<td align="right">30,829</td>
<td align="right">31.0%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">207,263</td>
<td align="right">45.9%</td>
<td align="right">52,821</td>
<td align="right">53.1%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">16,499</td>
<td align="right">3.7%</td>
<td align="right">4,283</td>
<td align="right">4.3%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">8,302</td>
<td align="right">1.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">7,864</td>
<td align="right">1.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.1%</td>
<td align="right">275</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">109</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">108</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="left">Frames pushed</td>
<td align="right">23,889,659</td>
<td align="right">82.6%</td>
<td align="right">24,389,922</td>
<td align="right">82.9%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">20,955,903</td>
<td align="right">72.5%</td>
<td align="right">21,378,099</td>
<td align="right">72.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,531,577</td>
<td align="right">26.0%</td>
<td align="right">7,609,644</td>
<td align="right">25.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,531,636</td>
<td align="right">26.0%</td>
<td align="right">7,609,703</td>
<td align="right">25.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,959,015</td>
<td align="right">27.5%</td>
<td align="right">8,037,082</td>
<td align="right">27.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,959,015</td>
<td align="right">27.5%</td>
<td align="right">8,037,082</td>
<td align="right">27.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,726</td>
<td align="right">0.1%</td>
<td align="right">17,624</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">443,874</td>
<td align="right">1.5%</td>
<td align="right">444,631</td>
<td align="right">1.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.5%</td>
<td align="right">427,379</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.6%</td>
<td align="right">456,471</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.5%</td>
<td align="right">441,509</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="left">Immortal increfs</td>
<td align="right">57,011,289</td>
<td align="right">15.8%</td>
<td align="right">95,410,307</td>
<td align="right">27.5%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">50,988,457</td>
<td align="right">14.1%</td>
<td align="right">18,580,384</td>
<td align="right">5.3%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">66,594,268</td>
<td align="right">15.3%</td>
<td align="right">27,332,546</td>
<td align="right">6.7%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">128,143,685</td>
<td align="right">35.6%</td>
<td align="right">60,598,101</td>
<td align="right">17.4%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">66,579</td>
<td align="right"></td>
<td align="right">38,505</td>
<td align="right"></td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">95,774</td>
<td align="right"></td>
<td align="right">57,108</td>
<td align="right"></td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">84,045,274</td>
<td align="right">19.4%</td>
<td align="right">117,518,322</td>
<td align="right">28.7%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">124,237,908</td>
<td align="right">34.5%</td>
<td align="right">172,716,088</td>
<td align="right">49.7%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">29,490</td>
<td align="right"></td>
<td align="right">18,884</td>
<td align="right"></td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">165,909,280</td>
<td align="right">38.2%</td>
<td align="right">115,526,635</td>
<td align="right">28.2%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">117,476,387</td>
<td align="right">27.1%</td>
<td align="right">149,321,262</td>
<td align="right">36.4%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,590</td>
<td align="right">0.1%</td>
<td align="right">45,016</td>
<td align="right">0.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,389,906</td>
<td align="right"></td>
<td align="right">1,431,018</td>
<td align="right"></td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,402,877</td>
<td align="right"></td>
<td align="right">10,608,825</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,724,300</td>
<td align="right"></td>
<td align="right">18,068,392</td>
<td align="right"></td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,722,696</td>
<td align="right">51.5%</td>
<td align="right">18,066,491</td>
<td align="right">51.6%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">17,855,755</td>
<td align="right"></td>
<td align="right">18,148,205</td>
<td align="right"></td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,700</td>
<td align="right">0.2%</td>
<td align="right">78,913</td>
<td align="right">0.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,693,352</td>
<td align="right">48.5%</td>
<td align="right">16,951,416</td>
<td align="right">48.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,572,062</td>
<td align="right">48.2%</td>
<td align="right">16,827,487</td>
<td align="right">48.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,834,766</td>
<td align="right"></td>
<td align="right">9,853,982</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">10,286</td>
<td align="right">766</td>
<td align="right">702</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">10,286</td>
<td align="right">766</td>
<td align="right">702</td>
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
<td align="right">376,790,035</td>
<td align="right">1,873.6%</td>
<td align="right">1,072,731,272</td>
<td align="right">2,578.5%</td>
<td align="right">184.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">20,110,280</td>
<td align="right"></td>
<td align="right">41,602,518</td>
<td align="right"></td>
<td align="right">106.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,047</td>
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
<td align="right">259</td>
<td align="right">12.7%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">45</td>
<td align="right">2.2%</td>
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
<td align="right">1,739</td>
<td align="right">85.0%</td>
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
<td align="right">1,743</td>
<td align="right">85.1%</td>
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
<td align="right">12</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">259</td>
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
<td align="right">259</td>
<td align="right">100.0%</td>
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
<td align="right">59</td>
<td align="right">22.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">48</td>
<td align="right">18.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">45</td>
<td align="right">17.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">48</td>
<td align="right">18.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">27</td>
<td align="right">10.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">19</td>
<td align="right">7.3%</td>
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
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">70</td>
<td align="right">27.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">8.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">71</td>
<td align="right">27.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">23</td>
<td align="right">8.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">53</td>
<td align="right">20.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">19</td>
<td align="right">7.3%</td>
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
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">549,921</td>
<td align="right">62,249.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">104,847</td>
<td align="right">9,649,205</td>
<td align="right">9,103.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">76,734</td>
<td align="right">8,600.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">68,264</td>
<td align="right">7,639.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">68,264</td>
<td align="right">7,639.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,741,161</td>
<td align="right">90,499,561</td>
<td align="right">3,201.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">407,686</td>
<td align="right">9,649,205</td>
<td align="right">2,266.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">64,219</td>
<td align="right">1,213,384</td>
<td align="right">1,789.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,516,493</td>
<td align="right">34,066,473</td>
<td align="right">1,253.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,529,748</td>
<td align="right">16,600,081</td>
<td align="right">985.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,017</td>
<td align="right">1,544,250</td>
<td align="right">964.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">53,704</td>
<td align="right">509,487</td>
<td align="right">848.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">467,570</td>
<td align="right">3,228,374</td>
<td align="right">590.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">499,277</td>
<td align="right">3,392,262</td>
<td align="right">579.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">467,570</td>
<td align="right">3,145,254</td>
<td align="right">572.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">467,570</td>
<td align="right">3,145,254</td>
<td align="right">572.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,569,560</td>
<td align="right">17,181,574</td>
<td align="right">568.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">86,954</td>
<td align="right">558,058</td>
<td align="right">541.8%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">209,694</td>
<td align="right">1,220,839</td>
<td align="right">482.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,752,606</td>
<td align="right">20,814,900</td>
<td align="right">454.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">58</td>
<td align="right">319</td>
<td align="right">450.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,273,100</td>
<td align="right">6,769,186</td>
<td align="right">431.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,259,743</td>
<td align="right">6,570,014</td>
<td align="right">421.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">317,046</td>
<td align="right">1,478,415</td>
<td align="right">366.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">892,084</td>
<td align="right">3,984,733</td>
<td align="right">346.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">666,040</td>
<td align="right">2,882,170</td>
<td align="right">332.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,940,028</td>
<td align="right">27,866,339</td>
<td align="right">301.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,649,138</td>
<td align="right">6,285,588</td>
<td align="right">281.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,332,179</td>
<td align="right">4,766,675</td>
<td align="right">257.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">217,304</td>
<td align="right">761,248</td>
<td align="right">250.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,725,234</td>
<td align="right">12,843,982</td>
<td align="right">244.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">13,986,203</td>
<td align="right">46,821,525</td>
<td align="right">234.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">412,941</td>
<td align="right">1,332,820</td>
<td align="right">222.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,492,843</td>
<td align="right">4,806,465</td>
<td align="right">222.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,527,631</td>
<td align="right">13,888,870</td>
<td align="right">206.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">104,847</td>
<td align="right">316,557</td>
<td align="right">201.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">31,517,681</td>
<td align="right">94,443,889</td>
<td align="right">199.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">2,441,372</td>
<td align="right">199.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,225,957</td>
<td align="right">9,649,205</td>
<td align="right">199.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,547,333</td>
<td align="right">13,127,566</td>
<td align="right">188.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,925,623</td>
<td align="right">8,419,764</td>
<td align="right">187.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,925,623</td>
<td align="right">8,419,764</td>
<td align="right">187.8%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">2,608,577</td>
<td align="right">6,941,349</td>
<td align="right">166.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">435,058</td>
<td align="right">1,146,153</td>
<td align="right">163.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">435,058</td>
<td align="right">1,108,709</td>
<td align="right">154.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">435,058</td>
<td align="right">1,104,512</td>
<td align="right">153.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right">435,058</td>
<td align="right">1,104,512</td>
<td align="right">153.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,578,400</td>
<td align="right">6,544,273</td>
<td align="right">153.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,578,400</td>
<td align="right">6,544,273</td>
<td align="right">153.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,718,845</td>
<td align="right">19,337,725</td>
<td align="right">150.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">493,744</td>
<td align="right">1,197,895</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">607,087</td>
<td align="right">1,453,126</td>
<td align="right">139.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,286,167</td>
<td align="right">14,367,459</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,286,167</td>
<td align="right">14,367,459</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">457,425</td>
<td align="right">1,008,483</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,978,079</td>
<td align="right">89,017,838</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,333,160</td>
<td align="right">2,854,885</td>
<td align="right">114.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">85,971</td>
<td align="right">182,929</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,094,341</td>
<td align="right">18,483,876</td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">552,486</td>
<td align="right">1,106,583</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">14,768,487</td>
<td align="right">1,935,297</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">811,253</td>
<td align="right">1,498,552</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">367,339</td>
<td align="right">668,717</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">2,301,908</td>
<td align="right">4,139,096</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">86,072</td>
<td align="right">20,563</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">516,687</td>
<td align="right">908,379</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">516,687</td>
<td align="right">887,375</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,351</td>
<td align="right">121,809</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">961,309</td>
<td align="right">1,595,245</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,341,735</td>
<td align="right">2,026,018</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,941,483</td>
<td align="right">3,116,193</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">497,863</td>
<td align="right">247,769</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,309,029</td>
<td align="right">1,905,138</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">236,093</td>
<td align="right">340,214</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">236,093</td>
<td align="right">331,744</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">367,351</td>
<td align="right">506,086</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">367,351</td>
<td align="right">506,086</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">18,139,576</td>
<td align="right">24,971,036</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,799,462</td>
<td align="right">5,928,147</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,463,889</td>
<td align="right">7,816,252</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,463,889</td>
<td align="right">7,816,252</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">273,292</td>
<td align="right">307,476</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">410,028</td>
<td align="right">461,298</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">824,639</td>
<td align="right">921,969</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">436,306</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">407,686</td>
<td align="right">440,087</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,351</td>
<td align="right">434,396</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">840,518</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,565,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">20,659,530</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">20,110,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">9,665,654</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,040,767</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,096,738</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,635,561</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,621,646</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,199,485</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,188,456</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,105,157</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,695,873</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,467,947</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,030,635</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,887,126</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,881,830</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,530,931</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,495,897</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,420,273</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,293,151</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,183,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,152,176</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,069,391</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,046,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,046,447</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">685,444</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">583,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">557,963</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">557,963</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">549,250</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">435,058</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">435,058</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">411,805</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,351</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">195,089,845</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">18,483,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">14,268,022</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">14,120,474</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">13,248,835</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">13,248,816</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">5,174,379</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">5,174,377</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">5,174,165</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">4,984,090</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">4,557,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">3,785,243</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right"></td>
<td align="right">3,572,153</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">2,775,559</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">2,775,477</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">959,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">912,258</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">903,888</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">879,619</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">519,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right">469,202</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">336,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">336,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">197,485</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">197,485</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">190,552</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">178,686</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">178,686</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">135,210</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">103,931</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">103,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">101,765</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">96,706</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">96,706</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">84,030</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">74,982</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">74,982</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">49,869</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">42,150</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">41,681</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">37,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">33,393</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">33,312</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">33,215</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">29,421</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">29,417</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">29,250</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">22,444</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">20,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">20,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">16,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">16,231</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">13,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">13,115</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">12,613</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">12,613</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">12,465</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">8,345</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">8,286</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">4,172</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">625</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">261</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">224</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">139</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">59</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">28</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">15</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">3</td>
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
<td align="right">107</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-01-27
