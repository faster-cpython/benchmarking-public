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
<td align="left">LOAD_CONST</td>
<td align="right">10,433,847</td>
<td align="right">901,257</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,725,578</td>
<td align="right">22,930,636</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">248,372</td>
<td align="right">424,804</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,557,299</td>
<td align="right">4,321,919</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">517,730</td>
<td align="right">870,623</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">951,001</td>
<td align="right">1,598,026</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">610,486</td>
<td align="right">1,022,203</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,453,957</td>
<td align="right">5,776,415</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">790,460</td>
<td align="right">1,319,929</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">234,123</td>
<td align="right">390,551</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">176,310</td>
<td align="right">294,004</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">979,240</td>
<td align="right">1,626,265</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">905,118</td>
<td align="right">1,493,457</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">921,910</td>
<td align="right">1,509,966</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">184,622</td>
<td align="right">302,316</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,017,053</td>
<td align="right">1,664,078</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">855,712</td>
<td align="right">1,385,181</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">292,277</td>
<td align="right">470,986</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">396,862</td>
<td align="right">632,145</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">298,455</td>
<td align="right">475,054</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">199,453</td>
<td align="right">317,038</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">199,515</td>
<td align="right">317,100</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">302,380</td>
<td align="right">478,928</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">109,784</td>
<td align="right">168,660</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">330,564</td>
<td align="right">507,046</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,648,836</td>
<td align="right">7,002,047</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">118,372</td>
<td align="right">177,219</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">121,173</td>
<td align="right">180,130</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,253,763</td>
<td align="right">6,313,127</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,350,567</td>
<td align="right">1,997,317</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,321,786</td>
<td align="right">10,791,714</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">124,309</td>
<td align="right">183,178</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,593,933</td>
<td align="right">14,122,829</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,457,626</td>
<td align="right">2,104,812</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,221,470</td>
<td align="right">13,161,522</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,716,818</td>
<td align="right">6,716,703</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,011,267</td>
<td align="right">1,422,984</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,178,793</td>
<td align="right">3,061,018</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,789,492</td>
<td align="right">3,907,226</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,594,901</td>
<td align="right">3,594,625</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,073,091</td>
<td align="right">1,484,533</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,075,634</td>
<td align="right">4,252,178</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,821,625</td>
<td align="right">12,115,629</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">987,454</td>
<td align="right">1,340,550</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,829,822</td>
<td align="right">2,476,853</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">58,246,773</td>
<td align="right">78,475,570</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,385,877</td>
<td align="right">3,209,715</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,181,914</td>
<td align="right">2,887,182</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,952,255</td>
<td align="right">7,833,250</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">584,256</td>
<td align="right">760,897</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,465,276</td>
<td align="right">5,759,721</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,858,196</td>
<td align="right">23,739,303</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">683,197</td>
<td align="right">859,651</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,690,561</td>
<td align="right">8,395,064</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,299,946</td>
<td align="right">27,946,682</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">949,277</td>
<td align="right">1,183,790</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">243,631</td>
<td align="right">302,528</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,372,805</td>
<td align="right">18,958,072</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,089,606</td>
<td align="right">5,028,057</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,036,137</td>
<td align="right">1,271,472</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">14,701,615</td>
<td align="right">17,875,359</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,512,238</td>
<td align="right">7,747,740</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,205,121</td>
<td align="right">7,381,713</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,272,300</td>
<td align="right">1,507,608</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,709,568</td>
<td align="right">3,180,228</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,885,259</td>
<td align="right">3,355,852</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">107</td>
<td align="right">90</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,785,199</td>
<td align="right">7,785,143</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,059,849</td>
<td align="right">1,177,601</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,044,735</td>
<td align="right">5,574,242</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">608,065</td>
<td align="right">666,910</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">453</td>
<td align="right">487</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,806,243</td>
<td align="right">13,629,436</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">997,442</td>
<td align="right">1,056,295</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,539</td>
<td align="right">5,220</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,151,950</td>
<td align="right">3,269,702</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,937</td>
<td align="right">13,617</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">18,160</td>
<td align="right">17,840</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">18,160</td>
<td align="right">17,840</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,139</td>
<td align="right">3,153</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">101,548</td>
<td align="right">101,287</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,495</td>
<td align="right">4,504</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">95,750</td>
<td align="right">95,867</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,473</td>
<td align="right">603,892</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">449,114</td>
<td align="right">448,795</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">57,490</td>
<td align="right">57,520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,477</td>
<td align="right">21,469</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,046</td>
<td align="right">34,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,379</td>
<td align="right">61,371</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">906,968</td>
<td align="right">907,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,103</td>
<td align="right">35,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,022</td>
<td align="right">191,010</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,265</td>
<td align="right">857,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,665</td>
<td align="right">1,818,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">855,359</td>
<td align="right">855,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,647</td>
<td align="right">940,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,067,766</td>
<td align="right">5,067,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,877</td>
<td align="right">4,723,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">4,558,288</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,670</td>
<td align="right">462,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,666</td>
<td align="right">426,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">105,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,109</td>
<td align="right">105,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">87,183</td>
<td align="right">87,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,699</td>
<td align="right">84,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">77,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">67,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">55,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,466</td>
<td align="right">55,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">50,931</td>
<td align="right">50,931</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,868</td>
<td align="right">43,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,875</td>
<td align="right">42,875</td>
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
<td align="right">29,549</td>
<td align="right">29,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,767</td>
<td align="right">28,767</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">28,680</td>
<td align="right">28,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
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
<td align="right">17,706</td>
<td align="right">17,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">12,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,833</td>
<td align="right">12,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">8,485</td>
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
<td align="right">742</td>
<td align="right">742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">427</td>
<td align="right">427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">330</td>
<td align="right">330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">179</td>
<td align="right">179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">152</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">148</td>
<td align="right">148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">97</td>
<td align="right">97</td>
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
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">19</td>
<td align="right">19</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">14,530,239</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_INT</td>
<td align="right"></td>
<td align="right">4,147,168</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">141,448</td>
<td align="right">2.8%</td>
<td align="right">245,037</td>
<td align="right">3.2%</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,443,897</td>
<td align="right">69.1%</td>
<td align="right">5,759,969</td>
<td align="right">75.4%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,389,007</td>
<td align="right">27.9%</td>
<td align="right">1,618,021</td>
<td align="right">21.2%</td>
<td align="right">16.5%</td>
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
<td align="right">2,787</td>
<td align="right">21.9%</td>
<td align="right">4,741</td>
<td align="right">22.5%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,940</td>
<td align="right">78.1%</td>
<td align="right">16,326</td>
<td align="right">77.5%</td>
<td align="right">64.2%</td>
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
<td align="left">add different types</td>
<td align="right">8,131</td>
<td align="right">81.8%</td>
<td align="right">14,002</td>
<td align="right">85.8%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">522</td>
<td align="right">5.3%</td>
<td align="right">727</td>
<td align="right">4.5%</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">945</td>
<td align="right">9.5%</td>
<td align="right">1,263</td>
<td align="right">7.7%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">255</td>
<td align="right">2.6%</td>
<td align="right">247</td>
<td align="right">1.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">0.9%</td>
<td align="right">87</td>
<td align="right">0.5%</td>
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
<td align="right">12,855</td>
<td align="right">100.0%</td>
<td align="right">12,855</td>
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
<td align="right">382,830</td>
<td align="right">46.0%</td>
<td align="right">500,524</td>
<td align="right">52.7%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">448,739</td>
<td align="right">53.9%</td>
<td align="right">448,420</td>
<td align="right">47.2%</td>
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
<td align="right">117</td>
<td align="right">31.2%</td>
<td align="right">117</td>
<td align="right">31.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">258</td>
<td align="right">68.8%</td>
<td align="right">258</td>
<td align="right">68.8%</td>
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
<td align="right">257</td>
<td align="right">99.6%</td>
<td align="right">257</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">14,367,263</td>
<td align="right">100.0%</td>
<td align="right">19,777,194</td>
<td align="right">100.0%</td>
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
<td align="right">1,148</td>
<td align="right">0.0%</td>
<td align="right">1,211</td>
<td align="right">0.0%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">510</td>
<td align="right">0.0%</td>
<td align="right">510</td>
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
<td align="right">3,485</td>
<td align="right">100.0%</td>
<td align="right">3,431</td>
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
<td align="right">41</td>
<td align="right">22.9%</td>
<td align="right">41</td>
<td align="right">22.9%</td>
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
<td align="right">84,366</td>
<td align="right">2.4%</td>
<td align="right">143,189</td>
<td align="right">3.2%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">290,107</td>
<td align="right">8.4%</td>
<td align="right">467,690</td>
<td align="right">10.6%</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,095,009</td>
<td align="right">89.2%</td>
<td align="right">3,800,307</td>
<td align="right">86.1%</td>
<td align="right">22.8%</td>
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
<td align="right">1,850</td>
<td align="right">49.4%</td>
<td align="right">2,954</td>
<td align="right">49.4%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,898</td>
<td align="right">50.6%</td>
<td align="right">3,028</td>
<td align="right">50.6%</td>
<td align="right">59.5%</td>
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
<td align="right">1,693</td>
<td align="right">89.2%</td>
<td align="right">2,831</td>
<td align="right">93.5%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">110</td>
<td align="right">5.8%</td>
<td align="right">102</td>
<td align="right">3.4%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">5.0%</td>
<td align="right">95</td>
<td align="right">3.1%</td>
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
<td align="right">1,011,364</td>
<td align="right">100.0%</td>
<td align="right">1,423,081</td>
<td align="right">100.0%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">7</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,486,066</td>
<td align="right">92.4%</td>
<td align="right">12,898,116</td>
<td align="right">93.2%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">940,111</td>
<td align="right">7.6%</td>
<td align="right">940,111</td>
<td align="right">6.8%</td>
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
<td align="right">48</td>
<td align="right">9.0%</td>
<td align="right">50</td>
<td align="right">9.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">91.0%</td>
<td align="right">488</td>
<td align="right">90.7%</td>
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
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="right">4,244,320</td>
<td align="right">13.3%</td>
<td align="right">6,303,359</td>
<td align="right">14.8%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,365,083</td>
<td align="right">85.6%</td>
<td align="right">35,889,803</td>
<td align="right">84.3%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">359,550</td>
<td align="right">1.1%</td>
<td align="right">358,883</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
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
<td align="right">4,687</td>
<td align="right">29.4%</td>
<td align="right">5,124</td>
<td align="right">31.5%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,268</td>
<td align="right">70.6%</td>
<td align="right">11,145</td>
<td align="right">68.5%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,087</td>
<td align="right">23.2%</td>
<td align="right">1,398</td>
<td align="right">27.3%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,442</td>
<td align="right">30.8%</td>
<td align="right">1,495</td>
<td align="right">29.2%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">747</td>
<td align="right">15.9%</td>
<td align="right">767</td>
<td align="right">15.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.8%</td>
<td align="right">460</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">186</td>
<td align="right">4.0%</td>
<td align="right">186</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.5%</td>
<td align="right">71</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">1.0%</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">14,310,477</td>
<td align="right">100.0%</td>
<td align="right">20,839,258</td>
<td align="right">100.0%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">789</td>
<td align="right">0.0%</td>
<td align="right">827</td>
<td align="right">0.0%</td>
<td align="right">4.8%</td>
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
<td align="right">274</td>
<td align="right">0.0%</td>
<td align="right">274</td>
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
<td align="right">2,359</td>
<td align="right">100.0%</td>
<td align="right">2,335</td>
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
<td align="right">974,801</td>
<td align="right">100.0%</td>
<td align="right">1,621,826</td>
<td align="right">100.0%</td>
<td align="right">66.4%</td>
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
<td align="right">2,963,660</td>
<td align="right">93.6%</td>
<td align="right">4,140,204</td>
<td align="right">95.3%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,832</td>
<td align="right">1.9%</td>
<td align="right">59,828</td>
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
<td align="right">140,654</td>
<td align="right">4.4%</td>
<td align="right">140,654</td>
<td align="right">3.2%</td>
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
<td align="right">3,622</td>
<td align="right">86.6%</td>
<td align="right">3,618</td>
<td align="right">86.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561</td>
<td align="right">13.4%</td>
<td align="right">561</td>
<td align="right">13.4%</td>
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
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.8%</td>
<td align="right">10</td>
<td align="right">1.8%</td>
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
<td align="right">1,073,091</td>
<td align="right">98.0%</td>
<td align="right">1,484,533</td>
<td align="right">98.6%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,267</td>
<td align="right">1.9%</td>
<td align="right">21,263</td>
<td align="right">1.4%</td>
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
<td align="right">23</td>
<td align="right">11.0%</td>
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">89.0%</td>
<td align="right">187</td>
<td align="right">90.8%</td>
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
<td align="right">6,055,845</td>
<td align="right">90.9%</td>
<td align="right">9,291,080</td>
<td align="right">93.3%</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">606,814</td>
<td align="right">9.1%</td>
<td align="right">665,655</td>
<td align="right">6.7%</td>
<td align="right">9.7%</td>
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
<td align="right">803</td>
<td align="right">64.1%</td>
<td align="right">810</td>
<td align="right">64.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">450</td>
<td align="right">35.9%</td>
<td align="right">447</td>
<td align="right">35.6%</td>
<td align="right">-0.7%</td>
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
<td align="left">mapping</td>
<td align="right">313</td>
<td align="right">39.0%</td>
<td align="right">320</td>
<td align="right">39.5%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">28.9%</td>
<td align="right">232</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">147</td>
<td align="right">18.3%</td>
<td align="right">147</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">8.5%</td>
<td align="right">68</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">43</td>
<td align="right">5.4%</td>
<td align="right">43</td>
<td align="right">5.3%</td>
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
<td align="right">1,917,114</td>
<td align="right">100.0%</td>
<td align="right">2,034,895</td>
<td align="right">100.0%</td>
<td align="right">6.1%</td>
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
<td align="right">110</td>
<td align="right">100.0%</td>
<td align="right">110</td>
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
<td align="right">10,101,577</td>
<td align="right">2.9%</td>
<td align="right">14,720,643</td>
<td align="right">3.3%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">117,314,471</td>
<td align="right">34.1%</td>
<td align="right">169,241,207</td>
<td align="right">37.5%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">215,885,952</td>
<td align="right">62.8%</td>
<td align="right">265,956,812</td>
<td align="right">59.0%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">726,830</td>
<td align="right">0.2%</td>
<td align="right">888,575</td>
<td align="right">0.2%</td>
<td align="right">22.3%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">3,443,897</td>
<td align="right">34.2%</td>
<td align="right">5,759,969</td>
<td align="right">39.2%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">290,107</td>
<td align="right">2.9%</td>
<td align="right">467,690</td>
<td align="right">3.2%</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,244,320</td>
<td align="right">42.1%</td>
<td align="right">6,303,359</td>
<td align="right">42.9%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">606,814</td>
<td align="right">6.0%</td>
<td align="right">665,655</td>
<td align="right">4.5%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,148</td>
<td align="right">0.0%</td>
<td align="right">1,211</td>
<td align="right">0.0%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">448,739</td>
<td align="right">4.5%</td>
<td align="right">448,420</td>
<td align="right">3.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,267</td>
<td align="right">0.2%</td>
<td align="right">21,263</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,832</td>
<td align="right">0.6%</td>
<td align="right">59,828</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,111</td>
<td align="right">9.3%</td>
<td align="right">940,111</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.1%</td>
<td align="right">12,855</td>
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
<td align="right">141,448</td>
<td align="right">19.5%</td>
<td align="right">245,037</td>
<td align="right">27.6%</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">84,365</td>
<td align="right">11.6%</td>
<td align="right">143,188</td>
<td align="right">16.1%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">300,014</td>
<td align="right">41.3%</td>
<td align="right">299,343</td>
<td align="right">33.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,486</td>
<td align="right">6.8%</td>
<td align="right">49,490</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">19.4%</td>
<td align="right">140,654</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.4%</td>
<td align="right">9,895</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">269</td>
<td align="right">0.0%</td>
<td align="right">269</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">143</td>
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
<td align="right">302,607</td>
<td align="right">1.4%</td>
<td align="right">420,218</td>
<td align="right">1.5%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">17,288,099</td>
<td align="right">77.5%</td>
<td align="right">22,934,869</td>
<td align="right">82.0%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">15,523,675</td>
<td align="right">69.6%</td>
<td align="right">20,170,501</td>
<td align="right">72.1%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,362,644</td>
<td align="right">28.5%</td>
<td align="right">7,362,588</td>
<td align="right">26.3%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,362,700</td>
<td align="right">28.5%</td>
<td align="right">7,362,644</td>
<td align="right">26.3%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">6,789,557</td>
<td align="right">30.4%</td>
<td align="right">7,789,501</td>
<td align="right">27.9%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">6,789,557</td>
<td align="right">30.4%</td>
<td align="right">7,789,501</td>
<td align="right">27.9%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">18,171</td>
<td align="right">0.1%</td>
<td align="right">17,851</td>
<td align="right">0.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.9%</td>
<td align="right">426,857</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">2.0%</td>
<td align="right">456,471</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">2.0%</td>
<td align="right">441,507</td>
<td align="right">1.6%</td>
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
<td align="right">19,024</td>
<td align="right"></td>
<td align="right">53,563</td>
<td align="right"></td>
<td align="right">181.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">44,468</td>
<td align="right"></td>
<td align="right">85,154</td>
<td align="right"></td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">841,546</td>
<td align="right"></td>
<td align="right">1,312,162</td>
<td align="right"></td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,209,897</td>
<td align="right"></td>
<td align="right">7,822,331</td>
<td align="right"></td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">33,396,742</td>
<td align="right">11.6%</td>
<td align="right">45,032,168</td>
<td align="right">11.9%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">66,699,056</td>
<td align="right">23.1%</td>
<td align="right">89,809,570</td>
<td align="right">23.6%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">27,066,004</td>
<td align="right">10.5%</td>
<td align="right">36,113,422</td>
<td align="right">11.2%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">37,947,441</td>
<td align="right">14.7%</td>
<td align="right">50,623,352</td>
<td align="right">15.7%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,038,680</td>
<td align="right">47.4%</td>
<td align="right">16,044,429</td>
<td align="right">49.7%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,041,508</td>
<td align="right"></td>
<td align="right">16,047,217</td>
<td align="right"></td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">141,269,906</td>
<td align="right">48.9%</td>
<td align="right">183,743,296</td>
<td align="right">48.4%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">127,752,076</td>
<td align="right">49.4%</td>
<td align="right">164,979,537</td>
<td align="right">51.3%</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">47,755,956</td>
<td align="right">16.5%</td>
<td align="right">61,308,172</td>
<td align="right">16.1%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,200,004</td>
<td align="right"></td>
<td align="right">10,429,080</td>
<td align="right"></td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">25,683</td>
<td align="right"></td>
<td align="right">31,882</td>
<td align="right"></td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,059,162</td>
<td align="right"></td>
<td align="right">17,352,499</td>
<td align="right"></td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,256,186</td>
<td align="right">52.2%</td>
<td align="right">16,137,527</td>
<td align="right">50.0%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,377,287</td>
<td align="right">52.6%</td>
<td align="right">16,258,587</td>
<td align="right">50.3%</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">65,686,917</td>
<td align="right">25.4%</td>
<td align="right">70,180,036</td>
<td align="right">21.8%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,561</td>
<td align="right">0.3%</td>
<td align="right">77,526</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,540</td>
<td align="right">0.2%</td>
<td align="right">43,534</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.1%</td>
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
Stats gathered on: 2024-10-25
