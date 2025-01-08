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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">544,396</td>
<td align="right">650,632</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,109,771</td>
<td align="right">1,322,267</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">373,880</td>
<td align="right">444,720</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,121,386</td>
<td align="right">1,332,513</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">625,401</td>
<td align="right">741,808</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,517,299</td>
<td align="right">1,796,547</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,911,419</td>
<td align="right">4,622,761</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,545,548</td>
<td align="right">1,824,796</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">594,821</td>
<td align="right">701,131</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">396,696</td>
<td align="right">467,511</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">397,019</td>
<td align="right">467,834</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,191,692</td>
<td align="right">1,402,418</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,583,369</td>
<td align="right">1,862,617</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">782,766</td>
<td align="right">920,333</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,315,292</td>
<td align="right">6,248,377</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,310,060</td>
<td align="right">1,535,120</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">625,791</td>
<td align="right">732,074</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">855,863</td>
<td align="right">997,544</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">217,202</td>
<td align="right">252,622</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">937,853</td>
<td align="right">1,089,332</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">220,267</td>
<td align="right">255,705</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,362,094</td>
<td align="right">1,580,062</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">223,083</td>
<td align="right">258,519</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,389,541</td>
<td align="right">1,609,350</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,978,451</td>
<td align="right">10,389,599</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,916,562</td>
<td align="right">2,211,416</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,025,801</td>
<td align="right">8,100,751</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,559,085</td>
<td align="right">5,245,816</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,626,363</td>
<td align="right">14,525,874</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,227,945</td>
<td align="right">1,411,484</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,603,053</td>
<td align="right">2,991,999</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,622,746</td>
<td align="right">12,173,678</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,811,621</td>
<td align="right">7,797,895</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,869,911</td>
<td align="right">10,149,507</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,492,036</td>
<td align="right">6,271,050</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,124,860</td>
<td align="right">2,419,410</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,246,629</td>
<td align="right">2,555,872</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,051,004</td>
<td align="right">5,737,229</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,754,540</td>
<td align="right">3,118,881</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,261,384</td>
<td align="right">5,934,777</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">62,798,327</td>
<td align="right">70,710,338</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,733,759</td>
<td align="right">1,950,729</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,667,167</td>
<td align="right">1,869,436</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">24,486,547</td>
<td align="right">27,445,150</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,240,937</td>
<td align="right">3,622,267</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,559,419</td>
<td align="right">3,974,739</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,113,250</td>
<td align="right">14,641,497</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,478,915</td>
<td align="right">15,020,809</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">348,752</td>
<td align="right">386,895</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,546,282</td>
<td align="right">23,892,343</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,341,887</td>
<td align="right">2,596,788</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">979,229</td>
<td align="right">1,085,481</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,683,830</td>
<td align="right">2,967,224</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,023,701</td>
<td align="right">1,129,943</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,559,180</td>
<td align="right">12,753,679</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,578,828</td>
<td align="right">3,925,693</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,256,694</td>
<td align="right">1,377,278</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,644,443</td>
<td align="right">5,064,784</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,800,697</td>
<td align="right">7,378,574</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,283,543</td>
<td align="right">20,914,196</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,020,282</td>
<td align="right">1,100,155</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,604</td>
<td align="right">62,460</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">779,352</td>
<td align="right">836,040</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">97,775</td>
<td align="right">104,738</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,467,601</td>
<td align="right">9,069,745</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">615,748</td>
<td align="right">657,457</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,289,636</td>
<td align="right">8,816,701</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">739,016</td>
<td align="right">781,410</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,297,036</td>
<td align="right">3,475,766</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">179,500</td>
<td align="right">187,028</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">359</td>
<td align="right">344</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">466</td>
<td align="right">484</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">95,296</td>
<td align="right">98,757</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,028</td>
<td align="right">5,194</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,616,303</td>
<td align="right">1,658,697</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">213,851</td>
<td align="right">218,072</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">395,687</td>
<td align="right">388,535</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">156,289</td>
<td align="right">159,035</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,426</td>
<td align="right">13,592</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,649</td>
<td align="right">17,815</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,649</td>
<td align="right">17,815</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">553,557</td>
<td align="right">557,741</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,207</td>
<td align="right">3,222</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,809</td>
<td align="right">40,972</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,535</td>
<td align="right">102,751</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,003</td>
<td align="right">201,357</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,547</td>
<td align="right">4,552</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,229</td>
<td align="right">97,329</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">20,695</td>
<td align="right">20,715</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,385</td>
<td align="right">46,410</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">775,640</td>
<td align="right">775,344</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,058</td>
<td align="right">34,049</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,131</td>
<td align="right">35,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,471</td>
<td align="right">21,468</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,713</td>
<td align="right">928,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,030</td>
<td align="right">191,021</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,882</td>
<td align="right">452,862</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,661</td>
<td align="right">81,658</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,813</td>
<td align="right">115,809</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">168,815</td>
<td align="right">168,813</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,671</td>
<td align="right">1,818,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">105,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">87,032</td>
<td align="right">87,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,432</td>
<td align="right">86,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">84,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">77,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">67,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,119</td>
<td align="right">59,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,866</td>
<td align="right">55,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,862</td>
<td align="right">55,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">29,563</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">17,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">14,867</td>
<td align="right">14,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">13,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286</td>
<td align="right">10,286</td>
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
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">415</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">154</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">5,310,749</td>
<td align="right">75.1%</td>
<td align="right">6,243,815</td>
<td align="right">77.2%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,223</td>
<td align="right">0.4%</td>
<td align="right">27,757</td>
<td align="right">0.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,728,022</td>
<td align="right">24.4%</td>
<td align="right">1,814,198</td>
<td align="right">22.4%</td>
<td align="right">5.0%</td>
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
<td align="right">700</td>
<td align="right">13.6%</td>
<td align="right">636</td>
<td align="right">12.5%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,435</td>
<td align="right">86.4%</td>
<td align="right">4,454</td>
<td align="right">87.5%</td>
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
<td align="left">or</td>
<td align="right">711</td>
<td align="right">16.0%</td>
<td align="right">787</td>
<td align="right">17.7%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,283</td>
<td align="right">28.9%</td>
<td align="right">1,404</td>
<td align="right">31.5%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,022</td>
<td align="right">45.6%</td>
<td align="right">1,848</td>
<td align="right">41.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">296</td>
<td align="right">6.7%</td>
<td align="right">292</td>
<td align="right">6.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">2.5%</td>
<td align="right">109</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">14</td>
<td align="right">0.3%</td>
<td align="right">14</td>
<td align="right">0.3%</td>
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
<td align="right">13,887</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">580,574</td>
<td align="right">93.4%</td>
<td align="right">651,414</td>
<td align="right">94.1%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,545</td>
<td align="right">6.5%</td>
<td align="right">40,711</td>
<td align="right">5.9%</td>
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
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">55.3%</td>
<td align="right">143</td>
<td align="right">54.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">44.7%</td>
<td align="right">118</td>
<td align="right">45.2%</td>
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
<td align="right">145</td>
<td align="right">99.3%</td>
<td align="right">142</td>
<td align="right">99.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,678</td>
<td align="right">100.0%</td>
<td align="right">26,760,328</td>
<td align="right">100.0%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,169</td>
<td align="right">0.0%</td>
<td align="right">1,226</td>
<td align="right">0.0%</td>
<td align="right">4.9%</td>
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
<td align="right">3,379</td>
<td align="right">100.0%</td>
<td align="right">3,327</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">623,748</td>
<td align="right">12.6%</td>
<td align="right">740,188</td>
<td align="right">13.5%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,284,062</td>
<td align="right">86.5%</td>
<td align="right">4,709,545</td>
<td align="right">85.8%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">42,846</td>
<td align="right">0.9%</td>
<td align="right">39,526</td>
<td align="right">0.7%</td>
<td align="right">-7.7%</td>
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
<td align="right">1,063</td>
<td align="right">43.4%</td>
<td align="right">1,000</td>
<td align="right">42.5%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,389</td>
<td align="right">56.6%</td>
<td align="right">1,355</td>
<td align="right">57.5%</td>
<td align="right">-2.4%</td>
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
<td align="right">1,093</td>
<td align="right">78.7%</td>
<td align="right">1,063</td>
<td align="right">78.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">155</td>
<td align="right">11.2%</td>
<td align="right">151</td>
<td align="right">11.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">6.9%</td>
<td align="right">96</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">3.2%</td>
<td align="right">44</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,702,355</td>
<td align="right">100.0%</td>
<td align="right">1,950,293</td>
<td align="right">100.0%</td>
<td align="right">14.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,561,648</td>
<td align="right">98.3%</td>
<td align="right">6,781,364</td>
<td align="right">98.3%</td>
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
<td align="right">115,484</td>
<td align="right">1.7%</td>
<td align="right">115,483</td>
<td align="right">1.7%</td>
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
<td align="right">53</td>
<td align="right">16.1%</td>
<td align="right">50</td>
<td align="right">15.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">276</td>
<td align="right">83.9%</td>
<td align="right">276</td>
<td align="right">84.7%</td>
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
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">7,014,562</td>
<td align="right">15.2%</td>
<td align="right">8,089,410</td>
<td align="right">15.6%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,769,249</td>
<td align="right">84.0%</td>
<td align="right">43,403,708</td>
<td align="right">83.6%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">383,331</td>
<td align="right">0.8%</td>
<td align="right">384,245</td>
<td align="right">0.7%</td>
<td align="right">0.2%</td>
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
<td align="right">6,685</td>
<td align="right">36.7%</td>
<td align="right">6,871</td>
<td align="right">37.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,510</td>
<td align="right">63.3%</td>
<td align="right">11,450</td>
<td align="right">62.5%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,656</td>
<td align="right">24.8%</td>
<td align="right">1,810</td>
<td align="right">26.3%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,337</td>
<td align="right">20.0%</td>
<td align="right">1,334</td>
<td align="right">19.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">864</td>
<td align="right">12.9%</td>
<td align="right">864</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">10.2%</td>
<td align="right">682</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.9%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">23</td>
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
<td align="right">17,887,438</td>
<td align="right">100.0%</td>
<td align="right">20,460,342</td>
<td align="right">100.0%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">818</td>
<td align="right">0.0%</td>
<td align="right">852</td>
<td align="right">0.0%</td>
<td align="right">4.2%</td>
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
<td align="right">2,398</td>
<td align="right">100.0%</td>
<td align="right">2,379</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">2,060,267</td>
<td align="right">100.0%</td>
<td align="right">2,449,886</td>
<td align="right">100.0%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">4,919,193</td>
<td align="right">95.7%</td>
<td align="right">5,627,599</td>
<td align="right">96.2%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,938</td>
<td align="right">1.6%</td>
<td align="right">79,937</td>
<td align="right">1.4%</td>
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
<td align="right">140,400</td>
<td align="right">2.7%</td>
<td align="right">140,400</td>
<td align="right">2.4%</td>
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
<td align="right">3,616</td>
<td align="right">83.0%</td>
<td align="right">3,614</td>
<td align="right">82.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.0%</td>
<td align="right">743</td>
<td align="right">17.1%</td>
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
<td align="right">771</td>
<td align="right">103.8%</td>
<td align="right">775</td>
<td align="right">104.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
<td align="right">1,768,314</td>
<td align="right">98.8%</td>
<td align="right">2,015,830</td>
<td align="right">98.9%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,265</td>
<td align="right">1.2%</td>
<td align="right">21,264</td>
<td align="right">1.0%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
<td align="right">187</td>
<td align="right">91.7%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,497,891</td>
<td align="right">98.5%</td>
<td align="right">13,447,406</td>
<td align="right">98.6%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,275</td>
<td align="right">1.5%</td>
<td align="right">185,820</td>
<td align="right">1.4%</td>
<td align="right">4.2%</td>
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
<td align="left">Success</td>
<td align="right">461</td>
<td align="right">37.6%</td>
<td align="right">453</td>
<td align="right">37.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">764</td>
<td align="right">62.4%</td>
<td align="right">755</td>
<td align="right">62.5%</td>
<td align="right">-1.2%</td>
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
<td align="right">140</td>
<td align="right">18.3%</td>
<td align="right">134</td>
<td align="right">17.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">321</td>
<td align="right">42.0%</td>
<td align="right">318</td>
<td align="right">42.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">126</td>
<td align="right">16.5%</td>
<td align="right">126</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">14.5%</td>
<td align="right">111</td>
<td align="right">14.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">8.5%</td>
<td align="right">65</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,115,196</td>
<td align="right">100.0%</td>
<td align="right">2,186,111</td>
<td align="right">100.0%</td>
<td align="right">3.4%</td>
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
<td align="right">13,428,111</td>
<td align="right">3.8%</td>
<td align="right">15,560,254</td>
<td align="right">3.9%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">126,449,484</td>
<td align="right">35.6%</td>
<td align="right">142,419,843</td>
<td align="right">35.9%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">214,285,646</td>
<td align="right">60.4%</td>
<td align="right">238,187,937</td>
<td align="right">60.0%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">599,008</td>
<td align="right">0.2%</td>
<td align="right">593,124</td>
<td align="right">0.1%</td>
<td align="right">-1.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">623,748</td>
<td align="right">4.7%</td>
<td align="right">740,188</td>
<td align="right">4.8%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,310,749</td>
<td align="right">39.6%</td>
<td align="right">6,243,815</td>
<td align="right">40.2%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,014,562</td>
<td align="right">52.3%</td>
<td align="right">8,089,410</td>
<td align="right">52.1%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,169</td>
<td align="right">0.0%</td>
<td align="right">1,226</td>
<td align="right">0.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">178,275</td>
<td align="right">1.3%</td>
<td align="right">185,820</td>
<td align="right">1.2%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,545</td>
<td align="right">0.3%</td>
<td align="right">40,711</td>
<td align="right">0.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,265</td>
<td align="right">0.2%</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,938</td>
<td align="right">0.6%</td>
<td align="right">79,937</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,484</td>
<td align="right">0.9%</td>
<td align="right">115,483</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right">13,887</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">31,223</td>
<td align="right">5.2%</td>
<td align="right">27,757</td>
<td align="right">4.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">42,845</td>
<td align="right">7.2%</td>
<td align="right">39,525</td>
<td align="right">6.7%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">313,680</td>
<td align="right">52.4%</td>
<td align="right">314,608</td>
<td align="right">53.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,591</td>
<td align="right">9.9%</td>
<td align="right">59,577</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">23.4%</td>
<td align="right">140,400</td>
<td align="right">23.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">153</td>
<td align="right">0.0%</td>
<td align="right">153</td>
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
<td align="right">504,217</td>
<td align="right">1.6%</td>
<td align="right">575,061</td>
<td align="right">1.6%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">26,784,193</td>
<td align="right">84.2%</td>
<td align="right">30,186,262</td>
<td align="right">85.7%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,337,493</td>
<td align="right">73.4%</td>
<td align="right">26,137,418</td>
<td align="right">74.2%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,044,521</td>
<td align="right">25.3%</td>
<td align="right">8,646,665</td>
<td align="right">24.6%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,044,580</td>
<td align="right">25.3%</td>
<td align="right">8,646,724</td>
<td align="right">24.6%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,471,959</td>
<td align="right">26.6%</td>
<td align="right">9,074,103</td>
<td align="right">25.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,471,959</td>
<td align="right">26.6%</td>
<td align="right">9,074,103</td>
<td align="right">25.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,664</td>
<td align="right">0.1%</td>
<td align="right">17,830</td>
<td align="right">0.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.3%</td>
<td align="right">427,379</td>
<td align="right">1.2%</td>
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
<td align="right">1.4%</td>
<td align="right">456,471</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.4%</td>
<td align="right">441,509</td>
<td align="right">1.3%</td>
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
<td align="left">Method cache misses</td>
<td align="right">32,576</td>
<td align="right"></td>
<td align="right">24,642</td>
<td align="right"></td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,631,296</td>
<td align="right"></td>
<td align="right">1,914,658</td>
<td align="right"></td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">11,278,589</td>
<td align="right"></td>
<td align="right">13,164,877</td>
<td align="right"></td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">846,968</td>
<td align="right"></td>
<td align="right">988,074</td>
<td align="right"></td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">879,273</td>
<td align="right"></td>
<td align="right">1,012,424</td>
<td align="right"></td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">73,794,589</td>
<td align="right">15.3%</td>
<td align="right">84,096,641</td>
<td align="right">15.6%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">55,930,982</td>
<td align="right">13.9%</td>
<td align="right">63,597,374</td>
<td align="right">14.2%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">67,127,859</td>
<td align="right">16.7%</td>
<td align="right">75,852,018</td>
<td align="right">16.9%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,771,368</td>
<td align="right"></td>
<td align="right">22,239,914</td>
<td align="right"></td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,769,729</td>
<td align="right">52.0%</td>
<td align="right">22,238,029</td>
<td align="right">52.7%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">96,034,920</td>
<td align="right">19.9%</td>
<td align="right">107,691,882</td>
<td align="right">20.0%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">182,918,547</td>
<td align="right">37.9%</td>
<td align="right">205,076,553</td>
<td align="right">38.0%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">139,416,829</td>
<td align="right">34.7%</td>
<td align="right">155,414,597</td>
<td align="right">34.6%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,706,695</td>
<td align="right"></td>
<td align="right">11,911,568</td>
<td align="right"></td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">138,914,648</td>
<td align="right">34.6%</td>
<td align="right">154,400,919</td>
<td align="right">34.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">19,606,227</td>
<td align="right"></td>
<td align="right">21,587,629</td>
<td align="right"></td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">129,611,170</td>
<td align="right">26.9%</td>
<td align="right">142,678,527</td>
<td align="right">26.4%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">18,111,367</td>
<td align="right">47.7%</td>
<td align="right">19,845,014</td>
<td align="right">47.0%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">18,232,693</td>
<td align="right">48.0%</td>
<td align="right">19,966,343</td>
<td align="right">47.3%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,611</td>
<td align="right">0.1%</td>
<td align="right">43,607</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,715</td>
<td align="right">0.2%</td>
<td align="right">77,722</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">11,083</td>
<td align="right">773</td>
<td align="right">784</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">11,083</td>
<td align="right">773</td>
<td align="right">784</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">59</td>
<td align="right">2.9%</td>
<td align="right">72</td>
<td align="right">3.3%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">246</td>
<td align="right">12.0%</td>
<td align="right">279</td>
<td align="right">12.8%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">391,958,668</td>
<td align="right">1,939.0%</td>
<td align="right">432,299,093</td>
<td align="right">2,037.9%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,053</td>
<td align="right"></td>
<td align="right">2,177</td>
<td align="right"></td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,620</td>
<td align="right">78.9%</td>
<td align="right">1,716</td>
<td align="right">78.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">20,214,891</td>
<td align="right"></td>
<td align="right">21,212,651</td>
<td align="right"></td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,748</td>
<td align="right">85.1%</td>
<td align="right">1,826</td>
<td align="right">83.9%</td>
<td align="right">4.5%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">246</td>
<td align="right"></td>
<td align="right">279</td>
<td align="right"></td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">246</td>
<td align="right">100.0%</td>
<td align="right">279</td>
<td align="right">100.0%</td>
<td align="right">13.4%</td>
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
<td align="right">61</td>
<td align="right">24.8%</td>
<td align="right">70</td>
<td align="right">25.1%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13</td>
<td align="right">5.3%</td>
<td align="right">15</td>
<td align="right">5.4%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">25</td>
<td align="right">10.2%</td>
<td align="right">31</td>
<td align="right">11.1%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">44</td>
<td align="right">17.9%</td>
<td align="right">49</td>
<td align="right">17.6%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">47</td>
<td align="right">19.1%</td>
<td align="right">58</td>
<td align="right">20.8%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">25</td>
<td align="right">10.2%</td>
<td align="right">25</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">31</td>
<td align="right">12.6%</td>
<td align="right">31</td>
<td align="right">11.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">72</td>
<td align="right">29.3%</td>
<td align="right">83</td>
<td align="right">29.7%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">68</td>
<td align="right">27.6%</td>
<td align="right">79</td>
<td align="right">28.3%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">29</td>
<td align="right">10.4%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">49</td>
<td align="right">19.9%</td>
<td align="right">55</td>
<td align="right">19.7%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">31</td>
<td align="right">12.6%</td>
<td align="right">31</td>
<td align="right">11.1%</td>
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
<td align="left">_BUILD_LIST</td>
<td align="right">502,790</td>
<td align="right">637,208</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">110,857</td>
<td align="right">139,359</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">110,786</td>
<td align="right">139,268</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,305,644</td>
<td align="right">1,633,302</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">87,257</td>
<td align="right">108,911</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,345,994</td>
<td align="right">2,924,337</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">266,897</td>
<td align="right">331,534</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">130,857</td>
<td align="right">162,095</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">130,857</td>
<td align="right">162,095</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">394,697</td>
<td align="right">488,465</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">559,688</td>
<td align="right">692,386</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,098,254</td>
<td align="right">1,357,320</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">286,898</td>
<td align="right">354,277</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">286,898</td>
<td align="right">354,277</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">442,950</td>
<td align="right">546,473</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">442,950</td>
<td align="right">546,473</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">442,939</td>
<td align="right">546,459</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,722,526</td>
<td align="right">2,117,661</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">740,810</td>
<td align="right">908,159</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,606,088</td>
<td align="right">1,957,388</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,844,402</td>
<td align="right">2,242,894</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">519,168</td>
<td align="right">629,539</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,500,306</td>
<td align="right">4,232,621</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,500,306</td>
<td align="right">4,232,621</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,105,609</td>
<td align="right">3,744,156</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,419,324</td>
<td align="right">2,908,516</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,221,067</td>
<td align="right">2,669,367</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,293,413</td>
<td align="right">2,736,879</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">97,299</td>
<td align="right">78,700</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">292,704</td>
<td align="right">236,884</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,774,182</td>
<td align="right">2,111,135</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,775,009</td>
<td align="right">4,476,032</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,860,911</td>
<td align="right">5,752,987</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,747,109</td>
<td align="right">6,794,048</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,720,661</td>
<td align="right">2,032,829</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,513,940</td>
<td align="right">1,788,590</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">5,304,170</td>
<td align="right">6,247,589</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,785,002</td>
<td align="right">5,618,050</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">75</td>
<td align="right">62</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,316,987</td>
<td align="right">1,538,710</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,931,303</td>
<td align="right">3,419,175</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">9,472,692</td>
<td align="right">11,024,555</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,851,910</td>
<td align="right">7,945,612</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,079,226</td>
<td align="right">1,250,455</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,882,449</td>
<td align="right">10,252,805</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,110,969</td>
<td align="right">2,433,657</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,205,377</td>
<td align="right">2,539,146</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,494,089</td>
<td align="right">4,015,894</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,093,266</td>
<td align="right">3,525,279</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,026,717</td>
<td align="right">1,169,613</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">971,497</td>
<td align="right">1,104,193</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,594,953</td>
<td align="right">14,249,321</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,009,993</td>
<td align="right">1,142,018</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,563,463</td>
<td align="right">1,747,929</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">761,067</td>
<td align="right">849,283</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,449,017</td>
<td align="right">1,614,675</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,760,512</td>
<td align="right">27,410,553</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,088,336</td>
<td align="right">2,309,722</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">34,072,723</td>
<td align="right">37,637,678</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">10,313,819</td>
<td align="right">11,360,758</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,914,908</td>
<td align="right">3,195,383</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,378,819</td>
<td align="right">1,509,398</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,283,658</td>
<td align="right">1,400,356</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">10,128,102</td>
<td align="right">11,025,157</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">605,800</td>
<td align="right">655,950</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">605,800</td>
<td align="right">655,950</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,702,038</td>
<td align="right">9,421,626</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">8,439,535</td>
<td align="right">9,124,763</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">8,439,535</td>
<td align="right">9,124,763</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,231,022</td>
<td align="right">1,327,546</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,851,465</td>
<td align="right">7,378,390</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,851,465</td>
<td align="right">7,378,390</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,922,031</td>
<td align="right">3,137,947</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,301,093</td>
<td align="right">2,449,541</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,301,093</td>
<td align="right">2,449,541</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">576,622</td>
<td align="right">613,412</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">577,318</td>
<td align="right">614,129</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">580,554</td>
<td align="right">617,365</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,099,283</td>
<td align="right">1,164,569</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,205,167</td>
<td align="right">16,099,420</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,586,307</td>
<td align="right">1,679,433</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">542,692</td>
<td align="right">573,936</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">542,692</td>
<td align="right">573,936</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">18,528,461</td>
<td align="right">19,563,205</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">518,542</td>
<td align="right">547,038</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">522,661</td>
<td align="right">551,157</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">522,557</td>
<td align="right">551,019</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,639,224</td>
<td align="right">2,779,378</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,554,914</td>
<td align="right">8,991,622</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">20,792,209</td>
<td align="right">21,826,780</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">20,214,891</td>
<td align="right">21,212,651</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">490,638</td>
<td align="right">512,313</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">490,638</td>
<td align="right">512,313</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">490,638</td>
<td align="right">512,313</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,340,168</td>
<td align="right">5,541,987</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,933,164</td>
<td align="right">5,108,173</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,945,770</td>
<td align="right">5,058,328</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,333,844</td>
<td align="right">1,362,326</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,009,649</td>
<td align="right">5,113,169</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,541,308</td>
<td align="right">2,569,790</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,381</td>
<td align="right">403,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,381</td>
<td align="right">403,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,381</td>
<td align="right">403,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">824,638</td>
<td align="right">824,639</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,566,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
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
<td align="right">214</td>
<td align="right">214</td>
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
Stats gathered on: 2025-01-08
