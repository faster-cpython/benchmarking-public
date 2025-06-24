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
<td align="left">NOT_TAKEN</td>
<td align="right">2,719,116</td>
<td align="right">93,897</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">754,035</td>
<td align="right">207,785</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,141</td>
<td align="right">3,042</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">577,601</td>
<td align="right">271,862</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,696,346</td>
<td align="right">872,403</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">960,023</td>
<td align="right">525,462</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,314,693</td>
<td align="right">783,732</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,103,569</td>
<td align="right">5,848,905</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">25,301</td>
<td align="right">16,997</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,434</td>
<td align="right">7,106</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,696</td>
<td align="right">16,581</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,521,924</td>
<td align="right">1,076,998</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">693,509</td>
<td align="right">566,816</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,025,029</td>
<td align="right">5,755,289</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">674,809</td>
<td align="right">554,757</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,015,604</td>
<td align="right">4,222,014</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,078,674</td>
<td align="right">3,446,549</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">155,774</td>
<td align="right">135,876</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,022</td>
<td align="right">403,176</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">24,850,299</td>
<td align="right">27,881,943</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,603,678</td>
<td align="right">4,994,270</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,322,057</td>
<td align="right">3,879,141</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,525</td>
<td align="right">21,402</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,328,463</td>
<td align="right">4,910,724</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,653,725</td>
<td align="right">2,450,495</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,971,415</td>
<td align="right">9,219,734</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,532,811</td>
<td align="right">3,312,044</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,139,913</td>
<td align="right">14,330,266</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">29,693,027</td>
<td align="right">28,134,212</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,185,178</td>
<td align="right">15,353,912</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,721,556</td>
<td align="right">1,635,051</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">46,675,955</td>
<td align="right">44,364,011</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,248,121</td>
<td align="right">1,186,395</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,478,030</td>
<td align="right">2,356,180</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,450,401</td>
<td align="right">6,136,257</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,336,199</td>
<td align="right">1,272,760</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,221,869</td>
<td align="right">7,839,251</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">11,029,805</td>
<td align="right">10,537,505</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,455,214</td>
<td align="right">1,391,098</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,790,159</td>
<td align="right">3,656,056</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,623</td>
<td align="right">144,503</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,249,757</td>
<td align="right">1,207,356</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">239,464</td>
<td align="right">231,384</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,089,645</td>
<td align="right">5,887,880</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,222,459</td>
<td align="right">18,593,165</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,308,088</td>
<td align="right">1,266,708</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">83,875,742</td>
<td align="right">86,377,372</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,851,825</td>
<td align="right">17,323,660</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">113,748,961</td>
<td align="right">110,556,030</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,454,692</td>
<td align="right">9,252,716</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,433,455</td>
<td align="right">4,346,940</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">63,920,290</td>
<td align="right">62,728,050</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,088,431</td>
<td align="right">1,070,451</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">137,853,609</td>
<td align="right">140,114,847</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,478,265</td>
<td align="right">3,423,531</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,432</td>
<td align="right">232,778</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">567,362,929</td>
<td align="right">558,912,209</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,685,866</td>
<td align="right">135,663,388</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,712,158</td>
<td align="right">8,585,827</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,520,994</td>
<td align="right">4,456,449</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">641,280</td>
<td align="right">634,254</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">145,906,581</td>
<td align="right">144,420,409</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">157,445,221</td>
<td align="right">158,914,082</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">13,379,394</td>
<td align="right">13,256,364</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">98,683,761</td>
<td align="right">99,590,170</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,268,317</td>
<td align="right">1,256,777</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,277,184</td>
<td align="right">1,265,644</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,672,818</td>
<td align="right">2,695,342</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">173,327,949</td>
<td align="right">171,886,180</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">22,278,737</td>
<td align="right">22,098,571</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,395,106</td>
<td align="right">48,026,460</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">38,816,832</td>
<td align="right">38,521,253</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,820,025</td>
<td align="right">1,806,477</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,137,867</td>
<td align="right">3,115,134</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">16,975,152</td>
<td align="right">16,857,819</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,223,856</td>
<td align="right">2,209,943</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">75,027,177</td>
<td align="right">75,450,693</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">72,330,413</td>
<td align="right">71,965,998</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,330,686</td>
<td align="right">17,246,939</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,971,056</td>
<td align="right">2,956,869</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,297</td>
<td align="right">1,483,493</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,148</td>
<td align="right">2,928,260</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,311</td>
<td align="right">5,924,584</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,978,767</td>
<td align="right">4,959,834</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">85,414</td>
<td align="right">85,120</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">86,454,415</td>
<td align="right">86,160,812</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,411,596</td>
<td align="right">11,379,753</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">50,343,035</td>
<td align="right">50,241,097</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,795</td>
<td align="right">7,294,765</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,851</td>
<td align="right">5,672,099</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">88,143,395</td>
<td align="right">87,991,646</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,247,756</td>
<td align="right">64,157,470</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,795,353</td>
<td align="right">1,792,885</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">101,948,800</td>
<td align="right">101,812,514</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,256</td>
<td align="right">9,245</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">26,887,549</td>
<td align="right">26,856,504</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">346,538</td>
<td align="right">346,202</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,344,078</td>
<td align="right">15,332,706</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,578,726</td>
<td align="right">4,575,751</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,512,507</td>
<td align="right">1,511,675</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,217,117</td>
<td align="right">9,213,490</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">78,580,410</td>
<td align="right">78,573,208</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,508,888</td>
<td align="right">84,501,686</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,470,462</td>
<td align="right">4,470,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,684</td>
<td align="right">21,685</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,415,037</td>
<td align="right">17,414,457</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,654,858</td>
<td align="right">9,654,543</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,566,436</td>
<td align="right">155,562,156</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">39,012</td>
<td align="right">39,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,054,771</td>
<td align="right">180,050,491</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,366,577</td>
<td align="right">10,366,489</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,568,625</td>
<td align="right">5,568,614</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">61,068,659</td>
<td align="right">61,068,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,529,039</td>
<td align="right">39,529,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,888,516</td>
<td align="right">38,888,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,032,963</td>
<td align="right">38,032,963</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,681,604</td>
<td align="right">22,681,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,496,255</td>
<td align="right">21,496,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,823</td>
<td align="right">16,962,823</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,489,314</td>
<td align="right">16,489,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,644,824</td>
<td align="right">4,644,824</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,051,087</td>
<td align="right">3,051,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,599</td>
<td align="right">2,973,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,021</td>
<td align="right">2,687,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">2,019,477</td>
<td align="right">2,019,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,668,715</td>
<td align="right">1,668,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,668,715</td>
<td align="right">1,668,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,623,512</td>
<td align="right">1,623,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,341,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,187</td>
<td align="right">1,133,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,752</td>
<td align="right">1,091,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">893,150</td>
<td align="right">893,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,724</td>
<td align="right">833,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">744,012</td>
<td align="right">744,012</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,742</td>
<td align="right">554,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,852</td>
<td align="right">501,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,745</td>
<td align="right">296,745</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,667</td>
<td align="right">266,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">257,895</td>
<td align="right">257,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">196,240</td>
<td align="right">196,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">192,022</td>
<td align="right">192,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">170,348</td>
<td align="right">170,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,435</td>
<td align="right">158,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">152,965</td>
<td align="right">152,965</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,480</td>
<td align="right">146,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,085</td>
<td align="right">129,085</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">119,000</td>
<td align="right">119,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,863</td>
<td align="right">79,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,985</td>
<td align="right">76,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">57,746</td>
<td align="right">57,746</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">36,236</td>
<td align="right">36,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,592</td>
<td align="right">35,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,987</td>
<td align="right">28,987</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">27,626</td>
<td align="right">27,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">25,183</td>
<td align="right">25,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,473</td>
<td align="right">21,473</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">16,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">10,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,055</td>
<td align="right">3,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,074</td>
<td align="right">2,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,335</td>
<td align="right">1,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">499</td>
<td align="right">499</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">348</td>
<td align="right">348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">298</td>
<td align="right">298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">175</td>
<td align="right">175</td>
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
<td align="right">98</td>
<td align="right">98</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">74</td>
<td align="right">74</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
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
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">9</td>
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
<td align="right">9,178,492</td>
<td align="right">13.9%</td>
<td align="right">9,174,866</td>
<td align="right">13.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">53,568,795</td>
<td align="right">81.3%</td>
<td align="right">53,568,795</td>
<td align="right">81.3%</td>
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
<td align="right">3,100,261</td>
<td align="right">4.7%</td>
<td align="right">3,100,261</td>
<td align="right">4.7%</td>
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
<td align="right">36,633</td>
<td align="right">37.8%</td>
<td align="right">36,632</td>
<td align="right">37.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">60,339</td>
<td align="right">62.2%</td>
<td align="right">60,339</td>
<td align="right">62.2%</td>
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
<td align="left">floor divide</td>
<td align="right">129</td>
<td align="right">0.4%</td>
<td align="right">131</td>
<td align="right">0.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,349</td>
<td align="right">6.4%</td>
<td align="right">2,347</td>
<td align="right">6.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">9.3%</td>
<td align="right">3,402</td>
<td align="right">9.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">23,921</td>
<td align="right">65.3%</td>
<td align="right">23,921</td>
<td align="right">65.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,632</td>
<td align="right">7.2%</td>
<td align="right">2,632</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,504</td>
<td align="right">4.1%</td>
<td align="right">1,504</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">698</td>
<td align="right">1.9%</td>
<td align="right">698</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">535</td>
<td align="right">1.5%</td>
<td align="right">535</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">272</td>
<td align="right">0.7%</td>
<td align="right">272</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">254</td>
<td align="right">0.7%</td>
<td align="right">254</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">0.6%</td>
<td align="right">229</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">196</td>
<td align="right">0.5%</td>
<td align="right">196</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">92</td>
<td align="right">0.3%</td>
<td align="right">92</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">66</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">and different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
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
<td align="right">3,137,867</td>
<td align="right">100.0%</td>
<td align="right">3,115,134</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,918,971</td>
<td align="right">0.8%</td>
<td align="right">1,916,667</td>
<td align="right">0.8%</td>
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
<td align="right">1,897,756</td>
<td align="right">0.8%</td>
<td align="right">1,895,495</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">240,324,618</td>
<td align="right">99.2%</td>
<td align="right">240,326,953</td>
<td align="right">99.2%</td>
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
<td align="right">60,227</td>
<td align="right">100.0%</td>
<td align="right">60,185</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">386</td>
<td align="right">18.1%</td>
<td align="right">386</td>
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
<td align="right">1,752</td>
<td align="right">100.0%</td>
<td align="right">1,752</td>
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
<td align="right">637,377</td>
<td align="right">5.5%</td>
<td align="right">630,347</td>
<td align="right">5.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,927,081</td>
<td align="right">94.4%</td>
<td align="right">10,927,081</td>
<td align="right">94.4%</td>
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
<td align="right">8,063</td>
<td align="right">0.1%</td>
<td align="right">8,063</td>
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
<td align="right">2,689</td>
<td align="right">66.7%</td>
<td align="right">2,693</td>
<td align="right">66.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,345</td>
<td align="right">33.3%</td>
<td align="right">1,345</td>
<td align="right">33.3%</td>
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
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">22</td>
<td align="right">0.8%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">106</td>
<td align="right">3.9%</td>
<td align="right">111</td>
<td align="right">4.1%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,825</td>
<td align="right">67.9%</td>
<td align="right">1,845</td>
<td align="right">68.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.6%</td>
<td align="right">259</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">251</td>
<td align="right">9.3%</td>
<td align="right">251</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">156</td>
<td align="right">5.8%</td>
<td align="right">156</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27</td>
<td align="right">1.0%</td>
<td align="right">27</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
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
<td align="right">4,073,168</td>
<td align="right">25.8%</td>
<td align="right">3,441,222</td>
<td align="right">22.7%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,734,919</td>
<td align="right">74.2%</td>
<td align="right">11,734,919</td>
<td align="right">77.3%</td>
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
<td align="right">4,977</td>
<td align="right">90.4%</td>
<td align="right">4,798</td>
<td align="right">90.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">529</td>
<td align="right">9.6%</td>
<td align="right">529</td>
<td align="right">9.9%</td>
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
<td align="right">627</td>
<td align="right">12.6%</td>
<td align="right">584</td>
<td align="right">12.2%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,424</td>
<td align="right">28.6%</td>
<td align="right">1,355</td>
<td align="right">28.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,196</td>
<td align="right">44.1%</td>
<td align="right">2,129</td>
<td align="right">44.4%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">730</td>
<td align="right">14.7%</td>
<td align="right">730</td>
<td align="right">15.2%</td>
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
<td align="right">9,965,173</td>
<td align="right">6.2%</td>
<td align="right">9,213,695</td>
<td align="right">5.7%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">123,493,263</td>
<td align="right">76.9%</td>
<td align="right">124,715,708</td>
<td align="right">77.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,100,020</td>
<td align="right">16.9%</td>
<td align="right">27,170,729</td>
<td align="right">16.9%</td>
<td align="right">0.3%</td>
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
<td align="right">5,587</td>
<td align="right">1.1%</td>
<td align="right">5,384</td>
<td align="right">1.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">511,960</td>
<td align="right">98.9%</td>
<td align="right">513,292</td>
<td align="right">99.0%</td>
<td align="right">0.3%</td>
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
<td align="right">49</td>
<td align="right">0.9%</td>
<td align="right">69</td>
<td align="right">1.3%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.4%</td>
<td align="right">405</td>
<td align="right">7.5%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">276</td>
<td align="right">4.9%</td>
<td align="right">312</td>
<td align="right">5.8%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">108</td>
<td align="right">1.9%</td>
<td align="right">100</td>
<td align="right">1.9%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,251</td>
<td align="right">22.4%</td>
<td align="right">1,173</td>
<td align="right">21.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">794</td>
<td align="right">14.2%</td>
<td align="right">751</td>
<td align="right">13.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,809</td>
<td align="right">32.4%</td>
<td align="right">1,745</td>
<td align="right">32.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">1.1%</td>
<td align="right">59</td>
<td align="right">1.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">271</td>
<td align="right">5.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.3%</td>
<td align="right">351</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.7%</td>
<td align="right">97</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">51</td>
<td align="right">0.9%</td>
<td align="right">51</td>
<td align="right">0.9%</td>
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
<td align="left">generator</td>
<td align="right">39,247,173</td>
<td align="right">39,247,173 / 0 !!</td>
<td align="right">39,247,173</td>
<td align="right">39,247,173 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">24,403,470</td>
<td align="right">24,403,470 / 0 !!</td>
<td align="right">24,403,470</td>
<td align="right">24,403,470 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">21,178,626</td>
<td align="right">21,178,626 / 0 !!</td>
<td align="right">21,178,626</td>
<td align="right">21,178,626 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,653,369</td>
<td align="right">3,653,369 / 0 !!</td>
<td align="right">3,653,369</td>
<td align="right">3,653,369 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">218,685</td>
<td align="right">218,685 / 0 !!</td>
<td align="right">218,685</td>
<td align="right">218,685 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">149,322</td>
<td align="right">149,322 / 0 !!</td>
<td align="right">149,322</td>
<td align="right">149,322 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">52,709</td>
<td align="right">52,709 / 0 !!</td>
<td align="right">52,709</td>
<td align="right">52,709 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">33,626</td>
<td align="right">33,626 / 0 !!</td>
<td align="right">33,626</td>
<td align="right">33,626 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,730</td>
<td align="right">1,730 / 0 !!</td>
<td align="right">1,730</td>
<td align="right">1,730 / 0 !!</td>
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
<td align="right">133,978,720</td>
<td align="right">33.7%</td>
<td align="right">132,918,301</td>
<td align="right">33.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">47,809,752</td>
<td align="right">12.0%</td>
<td align="right">47,445,020</td>
<td align="right">12.0%</td>
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
<td align="right">215,209,269</td>
<td align="right">54.1%</td>
<td align="right">215,012,331</td>
<td align="right">54.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,390</td>
<td align="right">0.0%</td>
<td align="right">64,390</td>
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
<td align="right">2,530,903</td>
<td align="right">93.3%</td>
<td align="right">2,510,751</td>
<td align="right">93.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">181,666</td>
<td align="right">6.7%</td>
<td align="right">181,639</td>
<td align="right">6.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,314</td>
<td align="right">0.7%</td>
<td align="right">1,310</td>
<td align="right">0.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,081</td>
<td align="right">1.7%</td>
<td align="right">3,075</td>
<td align="right">1.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">764</td>
<td align="right">0.4%</td>
<td align="right">765</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,860</td>
<td align="right">1.6%</td>
<td align="right">2,861</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">996</td>
<td align="right">0.5%</td>
<td align="right">996</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">646</td>
<td align="right">0.4%</td>
<td align="right">646</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">0.2%</td>
<td align="right">323</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">66</td>
<td align="right">0.0%</td>
<td align="right">66</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">206,002,285</td>
<td align="right">100.0%</td>
<td align="right">207,615,392</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,813</td>
<td align="right">0.0%</td>
<td align="right">2,813</td>
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
<td align="right">13,994</td>
<td align="right">0.0%</td>
<td align="right">13,994</td>
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
<td align="right">19,339</td>
<td align="right">100.0%</td>
<td align="right">19,340</td>
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
<td align="right">50</td>
<td align="right">0.0%</td>
<td align="right">50</td>
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
<td align="right">425,102</td>
<td align="right">99.9%</td>
<td align="right">425,102</td>
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
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">209</td>
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
<td align="right">10,351,515</td>
<td align="right">30.4%</td>
<td align="right">10,351,428</td>
<td align="right">30.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,061,801</td>
<td align="right">41.3%</td>
<td align="right">14,061,801</td>
<td align="right">41.3%</td>
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
<td align="right">9,609,951</td>
<td align="right">28.2%</td>
<td align="right">9,609,951</td>
<td align="right">28.2%</td>
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
<td align="right">9,915</td>
<td align="right">5.1%</td>
<td align="right">9,914</td>
<td align="right">5.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">185,984</td>
<td align="right">94.9%</td>
<td align="right">185,984</td>
<td align="right">94.9%</td>
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
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">170,831</td>
<td align="right">1,723.0%</td>
<td align="right">170,810</td>
<td align="right">1,722.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">5,037</td>
<td align="right">50.8%</td>
<td align="right">5,037</td>
<td align="right">50.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.5%</td>
<td align="right">2,626</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.5%</td>
<td align="right">643</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">311</td>
<td align="right">3.1%</td>
<td align="right">311</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">290</td>
<td align="right">2.9%</td>
<td align="right">290</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">119</td>
<td align="right">1.2%</td>
<td align="right">119</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.9%</td>
<td align="right">94</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">196,240</td>
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
<td align="right">1,486,344</td>
<td align="right">14.0%</td>
<td align="right">1,479,543</td>
<td align="right">13.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,601</td>
<td align="right">86.0%</td>
<td align="right">9,156,601</td>
<td align="right">86.1%</td>
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
<td align="right">3,478</td>
<td align="right">88.0%</td>
<td align="right">3,475</td>
<td align="right">88.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">475</td>
<td align="right">12.0%</td>
<td align="right">475</td>
<td align="right">12.0%</td>
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
<td align="left">bytearray int</td>
<td align="right">16</td>
<td align="right">0.5%</td>
<td align="right">13</td>
<td align="right">0.4%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,962</td>
<td align="right">85.2%</td>
<td align="right">2,962</td>
<td align="right">85.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.2%</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">46</td>
<td align="right">1.3%</td>
<td align="right">46</td>
<td align="right">1.3%</td>
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
<td align="right">5,285,937</td>
<td align="right">2.8%</td>
<td align="right">4,842,667</td>
<td align="right">2.6%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">165,970,816</td>
<td align="right">88.9%</td>
<td align="right">168,680,608</td>
<td align="right">89.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,192,517</td>
<td align="right">8.1%</td>
<td align="right">15,181,083</td>
<td align="right">8.0%</td>
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
<td align="right">103,621</td>
<td align="right">41.2%</td>
<td align="right">95,262</td>
<td align="right">39.2%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">147,599</td>
<td align="right">58.8%</td>
<td align="right">147,661</td>
<td align="right">60.8%</td>
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
<td align="left">set</td>
<td align="right">118</td>
<td align="right">0.1%</td>
<td align="right">96</td>
<td align="right">0.1%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">2,186</td>
<td align="right">1.5%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">134,241</td>
<td align="right">90.9%</td>
<td align="right">134,220</td>
<td align="right">90.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,929</td>
<td align="right">6.7%</td>
<td align="right">9,929</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">880</td>
<td align="right">0.6%</td>
<td align="right">880</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">243</td>
<td align="right">0.2%</td>
<td align="right">243</td>
<td align="right">0.2%</td>
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
<td align="right">296,267</td>
<td align="right">2.0%</td>
<td align="right">296,267</td>
<td align="right">2.0%</td>
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
<td align="right">14,609,454</td>
<td align="right">98.0%</td>
<td align="right">14,609,454</td>
<td align="right">98.0%</td>
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
<td align="right">381</td>
<td align="right">79.7%</td>
<td align="right">381</td>
<td align="right">79.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">20.3%</td>
<td align="right">97</td>
<td align="right">20.3%</td>
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
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">23.7%</td>
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
<td align="right">1,976,373,842</td>
<td align="right">54.4%</td>
<td align="right">1,954,484,279</td>
<td align="right">54.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">191,346,361</td>
<td align="right">5.3%</td>
<td align="right">189,390,512</td>
<td align="right">5.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">181,017,853</td>
<td align="right">5.0%</td>
<td align="right">179,582,721</td>
<td align="right">5.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,286,311,020</td>
<td align="right">35.4%</td>
<td align="right">1,281,920,252</td>
<td align="right">35.6%</td>
<td align="right">-0.3%</td>
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
<td align="right">4,073,168</td>
<td align="right">3.9%</td>
<td align="right">3,441,222</td>
<td align="right">3.4%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,965,173</td>
<td align="right">9.6%</td>
<td align="right">9,213,695</td>
<td align="right">9.0%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">637,377</td>
<td align="right">0.6%</td>
<td align="right">630,347</td>
<td align="right">0.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,809,752</td>
<td align="right">45.9%</td>
<td align="right">47,445,020</td>
<td align="right">46.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,137,867</td>
<td align="right">3.0%</td>
<td align="right">3,115,134</td>
<td align="right">3.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,344</td>
<td align="right">1.4%</td>
<td align="right">1,479,543</td>
<td align="right">1.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,897,756</td>
<td align="right">1.8%</td>
<td align="right">1,895,495</td>
<td align="right">1.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,192,517</td>
<td align="right">14.6%</td>
<td align="right">15,181,083</td>
<td align="right">14.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,178,492</td>
<td align="right">8.8%</td>
<td align="right">9,174,866</td>
<td align="right">9.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,351,515</td>
<td align="right">9.9%</td>
<td align="right">10,351,428</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,346,663</td>
<td align="right">2.4%</td>
<td align="right">4,124,268</td>
<td align="right">2.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">49,101,037</td>
<td align="right">27.1%</td>
<td align="right">48,183,371</td>
<td align="right">26.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,418,649</td>
<td align="right">12.9%</td>
<td align="right">23,284,290</td>
<td align="right">13.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,549,279</td>
<td align="right">7.5%</td>
<td align="right">13,584,833</td>
<td align="right">7.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,550,741</td>
<td align="right">7.5%</td>
<td align="right">13,585,896</td>
<td align="right">7.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">41,882,175</td>
<td align="right">23.1%</td>
<td align="right">41,879,871</td>
<td align="right">23.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,348,805</td>
<td align="right">5.7%</td>
<td align="right">10,348,805</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">5.3%</td>
<td align="right">9,554,980</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,738</td>
<td align="right">4.2%</td>
<td align="right">7,690,738</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,342,054</td>
<td align="right">1.3%</td>
<td align="right">2,342,054</td>
<td align="right">1.3%</td>
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
<td align="right">40,157,167</td>
<td align="right">18.3%</td>
<td align="right">40,157,167</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">179,431,042</td>
<td align="right">81.7%</td>
<td align="right">179,431,042</td>
<td align="right">81.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,157,167</td>
<td align="right">18.3%</td>
<td align="right">40,157,167</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,613,776</td>
<td align="right">18.0%</td>
<td align="right">39,613,776</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">543,391</td>
<td align="right">0.2%</td>
<td align="right">543,391</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">387</td>
<td align="right">0.0%</td>
<td align="right">387</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,612,054</td>
<td align="right">18.0%</td>
<td align="right">39,612,054</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,335</td>
<td align="right">0.0%</td>
<td align="right">1,335</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,485,127</td>
<td align="right">4.8%</td>
<td align="right">10,485,127</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,516</td>
<td align="right">0.2%</td>
<td align="right">502,516</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,548,632</td>
<td align="right">8.4%</td>
<td align="right">18,548,632</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,756,687</td>
<td align="right">3.1%</td>
<td align="right">6,756,687</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,520,122</td>
<td align="right">72.2%</td>
<td align="right">158,520,122</td>
<td align="right">72.2%</td>
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
<td align="right">1,154,753</td>
<td align="right"></td>
<td align="right">1,206,222</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,702,546</td>
<td align="right"></td>
<td align="right">8,374,232</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,855,837</td>
<td align="right"></td>
<td align="right">9,579,013</td>
<td align="right"></td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">845,784,667</td>
<td align="right">34.1%</td>
<td align="right">837,203,027</td>
<td align="right">33.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">121,219,468</td>
<td align="right">4.9%</td>
<td align="right">120,034,894</td>
<td align="right">4.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,146,483,867</td>
<td align="right">44.8%</td>
<td align="right">1,136,000,606</td>
<td align="right">44.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">804,562,167</td>
<td align="right">31.4%</td>
<td align="right">811,883,431</td>
<td align="right">31.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,111</td>
<td align="right">0.0%</td>
<td align="right">62,542</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">898,044,044</td>
<td align="right">36.2%</td>
<td align="right">903,265,945</td>
<td align="right">36.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">196,863,432</td>
<td align="right"></td>
<td align="right">197,560,822</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,420,144</td>
<td align="right">0.6%</td>
<td align="right">1,424,133</td>
<td align="right">0.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">612,681,090</td>
<td align="right">24.7%</td>
<td align="right">613,785,745</td>
<td align="right">24.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">83,000,626</td>
<td align="right">3.2%</td>
<td align="right">82,867,344</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">527,429,632</td>
<td align="right">20.6%</td>
<td align="right">527,816,034</td>
<td align="right">20.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">142,573,056</td>
<td align="right"></td>
<td align="right">142,672,054</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">156,600,889</td>
<td align="right"></td>
<td align="right">156,549,419</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">108,481,350</td>
<td align="right">45.2%</td>
<td align="right">108,497,301</td>
<td align="right">45.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">108,461,707</td>
<td align="right"></td>
<td align="right">108,475,175</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">130,296,765</td>
<td align="right">54.2%</td>
<td align="right">130,285,413</td>
<td align="right">54.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">131,779,020</td>
<td align="right">54.8%</td>
<td align="right">131,772,088</td>
<td align="right">54.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,080,762</td>
<td align="right"></td>
<td align="right">3,080,762</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,135</td>
<td align="right">32.4%</td>
<td align="right">997,135</td>
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
<td align="right">6,279</td>
<td align="right">13,062,005</td>
<td align="right">263,101,360</td>
<td align="right">16,050,810</td>
<td align="right">24,032,401</td>
<td align="right">6,239</td>
<td align="right">13,122,021</td>
<td align="right">265,156,952</td>
<td align="right">16,145,863</td>
<td align="right">24,045,008</td>
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
<td align="right">939</td>
<td align="right">4.7%</td>
<td align="right">5,483</td>
<td align="right">17.5%</td>
<td align="right">483.9%</td>
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
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">313.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,270</td>
<td align="right">6.4%</td>
<td align="right">3,344</td>
<td align="right">10.7%</td>
<td align="right">163.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">148</td>
<td align="right">0.7%</td>
<td align="right">285</td>
<td align="right">0.9%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">19,961</td>
<td align="right"></td>
<td align="right">31,385</td>
<td align="right"></td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">17,604</td>
<td align="right">88.2%</td>
<td align="right">22,273</td>
<td align="right">71.0%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">822,146,029</td>
<td align="right">2,456.1%</td>
<td align="right">886,900,505</td>
<td align="right">2,682.9%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">33,473,128</td>
<td align="right"></td>
<td align="right">33,058,003</td>
<td align="right"></td>
<td align="right">-1.2%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">193</td>
<td align="right">0.6%</td>
<td align="right">193 / 0 !!</td>
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
<td align="right">64</td>
<td align="right">0.2%</td>
<td align="right">64 / 0 !!</td>
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
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">8 / 0 !!</td>
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
<td align="right">854</td>
<td align="right">90.9%</td>
<td align="right">5,385</td>
<td align="right">98.2%</td>
<td align="right">530.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">939</td>
<td align="right"></td>
<td align="right">5,483</td>
<td align="right"></td>
<td align="right">483.9%</td>
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
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3 / 0 !!</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,283,767</td>
<td align="right">16.7%</td>
<td align="right">10,821,753</td>
<td align="right">19.3%</td>
<td align="right">743.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">7,692,288</td>
<td align="right"></td>
<td align="right">55,955,456</td>
<td align="right"></td>
<td align="right">627.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">6,225,273</td>
<td align="right">80.9%</td>
<td align="right">43,894,111</td>
<td align="right">78.4%</td>
<td align="right">605.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">183,248</td>
<td align="right">2.4%</td>
<td align="right">1,239,592</td>
<td align="right">2.2%</td>
<td align="right">576.5%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
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
<td align="left">219</td>
<td align="right">25.6%</td>
<td align="left">841</td>
<td align="right">15.6%</td>
<td align="right">284.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">333</td>
<td align="right">39.0%</td>
<td align="left">2,516</td>
<td align="right">46.7%</td>
<td align="right">655.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">281</td>
<td align="right">32.9%</td>
<td align="left">1,550</td>
<td align="right">28.8%</td>
<td align="right">451.6%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">2.5%</td>
<td align="left">478</td>
<td align="right">8.9%</td>
<td align="right">2,176.2%</td>
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
<td align="left"><= 16</td>
<td align="right">25</td>
<td align="right">2.7%</td>
<td align="right">227</td>
<td align="right">4.1%</td>
<td align="right">808.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">199</td>
<td align="right">21.2%</td>
<td align="right">1,027</td>
<td align="right">18.7%</td>
<td align="right">416.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">543</td>
<td align="right">57.8%</td>
<td align="right">2,975</td>
<td align="right">54.3%</td>
<td align="right">447.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">172</td>
<td align="right">18.3%</td>
<td align="right">711</td>
<td align="right">13.0%</td>
<td align="right">313.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">541</td>
<td align="right">9.9%</td>
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
<td align="left"><= 8</td>
<td align="right">21</td>
<td align="right">2.2%</td>
<td align="right">131</td>
<td align="right">2.4%</td>
<td align="right">523.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">47</td>
<td align="right">5.0%</td>
<td align="right">175</td>
<td align="right">3.2%</td>
<td align="right">272.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">418</td>
<td align="right">44.5%</td>
<td align="right">2,722</td>
<td align="right">49.6%</td>
<td align="right">551.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">347</td>
<td align="right">37.0%</td>
<td align="right">1,715</td>
<td align="right">31.3%</td>
<td align="right">394.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">2.2%</td>
<td align="right">577</td>
<td align="right">10.5%</td>
<td align="right">2,647.6%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">64</td>
<td align="right">1.2%</td>
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
<td align="left">_ERROR_POP_N</td>
<td align="right">129</td>
<td align="right">198,723</td>
<td align="right">153,948.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">4,620</td>
<td align="right">88,367</td>
<td align="right">1,812.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">19,509</td>
<td align="right">142,539</td>
<td align="right">630.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,507</td>
<td align="right">22,440</td>
<td align="right">539.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">35,238</td>
<td align="right">161,931</td>
<td align="right">359.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">3,381</td>
<td align="right">14,921</td>
<td align="right">341.3%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">3,381</td>
<td align="right">14,921</td>
<td align="right">341.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,236</td>
<td align="right">83,781</td>
<td align="right">335.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">19,929</td>
<td align="right">84,943</td>
<td align="right">326.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">19,929</td>
<td align="right">84,943</td>
<td align="right">326.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,236</td>
<td align="right">80,962</td>
<td align="right">320.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">78,082</td>
<td align="right">305.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">78,082</td>
<td align="right">305.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">108,927</td>
<td align="right">433,336</td>
<td align="right">297.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">107,962</td>
<td align="right">422,106</td>
<td align="right">291.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">107,962</td>
<td align="right">420,571</td>
<td align="right">289.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">107,962</td>
<td align="right">420,529</td>
<td align="right">289.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">169,874</td>
<td align="right">613,018</td>
<td align="right">260.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">403,593</td>
<td align="right">1,035,539</td>
<td align="right">156.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">96,387</td>
<td align="right">216,513</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">683,355</td>
<td align="right">1,476,945</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">452,660</td>
<td align="right">961,836</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,499</td>
<td align="right">7,199</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">37,635</td>
<td align="right">75,222</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">120,897</td>
<td align="right">336</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">295,631</td>
<td align="right">4,387</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,160,108</td>
<td align="right">658,478</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">298,893</td>
<td align="right">535,005</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">771,299</td>
<td align="right">1,233,959</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,223,808</td>
<td align="right">1,948,066</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">767,648</td>
<td align="right">1,210,564</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,807,069</td>
<td align="right">2,824,888</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">1,692,778</td>
<td align="right">2,629,404</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,156,129</td>
<td align="right">3,314,151</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,333,253</td>
<td align="right">2,012,106</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,077,393</td>
<td align="right">1,623,643</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,077,393</td>
<td align="right">1,623,643</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,890,380</td>
<td align="right">2,814,966</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">295,631</td>
<td align="right">432,827</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">295,631</td>
<td align="right">432,827</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,797,020</td>
<td align="right">2,628,286</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,797,020</td>
<td align="right">2,628,286</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,411,595</td>
<td align="right">2,049,479</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,837,412</td>
<td align="right">2,661,355</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">617,130</td>
<td align="right">341,097</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,808,037</td>
<td align="right">2,597,697</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">978,512</td>
<td align="right">1,386,378</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">714,591</td>
<td align="right">1,008,194</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">3,338,611</td>
<td align="right">4,587,605</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,925,767</td>
<td align="right">6,703,983</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">2,017,548</td>
<td align="right">2,738,031</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">5,487,152</td>
<td align="right">3,564,250</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">1,060,067</td>
<td align="right">1,429,597</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">5,381,239</td>
<td align="right">7,178,564</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,430,932</td>
<td align="right">3,240,579</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,130,299</td>
<td align="right">9,458,715</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,422,133</td>
<td align="right">8,507,498</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,130,299</td>
<td align="right">9,444,123</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">4,890,320</td>
<td align="right">6,451,833</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">637,416</td>
<td align="right">839,392</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">6,234,609</td>
<td align="right">4,312,361</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">658,308</td>
<td align="right">860,073</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">731,273</td>
<td align="right">952,040</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,786,666</td>
<td align="right">3,624,265</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,826,043</td>
<td align="right">6,292,811</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">11,092,526</td>
<td align="right">8,016,861</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">11,047,692</td>
<td align="right">8,016,861</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,429,610</td>
<td align="right">1,812,228</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,637,285</td>
<td align="right">4,873,030</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,041,957</td>
<td align="right">2,572,918</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">4,917,567</td>
<td align="right">6,131,624</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">286,437</td>
<td align="right">350,553</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">2,130,893</td>
<td align="right">2,578,684</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">7,376,066</td>
<td align="right">5,851,736</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,661,603</td>
<td align="right">4,413,448</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">7,225,016</td>
<td align="right">8,658,367</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">443,192</td>
<td align="right">529,697</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">443,192</td>
<td align="right">529,697</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">795,315</td>
<td align="right">947,064</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,593,897</td>
<td align="right">3,038,823</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,891,070</td>
<td align="right">10,394,593</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">258,090</td>
<td align="right">299,470</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">1,928,506</td>
<td align="right">2,234,338</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">799,755</td>
<td align="right">917,088</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">13,529,273</td>
<td align="right">15,378,740</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">981,317</td>
<td align="right">1,115,420</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,099,391</td>
<td align="right">3,517,130</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">8,500,669</td>
<td align="right">9,569,528</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">12,027,525</td>
<td align="right">13,470,424</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">9,451,338</td>
<td align="right">10,584,884</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">10,145,589</td>
<td align="right">11,337,981</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">10,145,589</td>
<td align="right">11,337,981</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">12,228,022</td>
<td align="right">10,828,827</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,387,604</td>
<td align="right">5,997,012</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">8,538,459</td>
<td align="right">9,485,293</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">128,780,098</td>
<td align="right">142,602,487</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,932,516</td>
<td align="right">2,118,139</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">157,412,332</td>
<td align="right">171,949,552</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">13,081,351</td>
<td align="right">14,187,041</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,677,916</td>
<td align="right">9,301,891</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,230,523</td>
<td align="right">1,317,500</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">34,632,353</td>
<td align="right">37,055,852</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">366,818</td>
<td align="right">389,551</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,542,519</td>
<td align="right">13,712,883</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,363,002</td>
<td align="right">2,489,333</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">6,422,253</td>
<td align="right">6,105,179</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,377,839</td>
<td align="right">1,440,290</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">443,192</td>
<td align="right">463,090</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">38,404,210</td>
<td align="right">39,891,064</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,851</td>
<td align="right">186,652</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,310,714</td>
<td align="right">1,350,032</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">33,364,072</td>
<td align="right">32,425,944</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,378,000</td>
<td align="right">8,581,230</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">8,378,000</td>
<td align="right">8,581,230</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">45,500,653</td>
<td align="right">46,528,427</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">463,730</td>
<td align="right">471,810</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,054,038</td>
<td align="right">1,067,951</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">33,473,128</td>
<td align="right">33,058,003</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,140,091</td>
<td align="right">1,153,639</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">707,019</td>
<td align="right">711,042</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,711,031</td>
<td align="right">4,725,218</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,004,012</td>
<td align="right">4,013,696</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">23,727</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">22,165</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">17,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">17,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">14,030</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">12,888</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">10,752</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">8,304</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">7,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right"></td>
<td align="right">7,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right"></td>
<td align="right">7,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right"></td>
<td align="right">7,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">7,115</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">7,104</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">5,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">5,099</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">4,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">4,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right"></td>
<td align="right">4,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">4,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">3,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">3,328</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">2,975</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">2,879</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">2,879</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">2,548</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">2,468</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">2,123</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">1,594</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">1,234</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">832</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">697</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">365</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right"></td>
<td align="right">342</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INSERT_NULL</td>
<td align="right"></td>
<td align="right">336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">315</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">294</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">87</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">51</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">15</td>
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
<td align="right">192</td>
<td align="right">437</td>
<td align="right">127.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">7</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right"></td>
<td align="right">21</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
Stats gathered on: 2025-06-24
