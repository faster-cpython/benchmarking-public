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
<td align="left">TO_BOOL_NONE</td>
<td align="right">380,975</td>
<td align="right">377,929</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">252</td>
<td align="right">250</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,390</td>
<td align="right">9,316</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,904</td>
<td align="right">1,889</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,936,153</td>
<td align="right">3,905,152</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,190</td>
<td align="right">4,157</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,330,853</td>
<td align="right">2,312,499</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,186,109</td>
<td align="right">3,161,021</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,763,640</td>
<td align="right">2,741,879</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,098,168</td>
<td align="right">1,089,521</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">707,644</td>
<td align="right">702,072</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">127</td>
<td align="right">126</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,898,273</td>
<td align="right">3,867,578</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,098,046</td>
<td align="right">1,089,400</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">707,648</td>
<td align="right">702,076</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">353,824</td>
<td align="right">351,038</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">396,370</td>
<td align="right">393,249</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,101,357</td>
<td align="right">1,092,685</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,188,075</td>
<td align="right">6,139,351</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,510,539</td>
<td align="right">3,482,898</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,686,754</td>
<td align="right">1,673,473</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,208,075</td>
<td align="right">1,198,563</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">604,166</td>
<td align="right">599,409</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,706,969</td>
<td align="right">16,575,424</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">6,043,323</td>
<td align="right">5,995,740</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,811,018</td>
<td align="right">14,694,402</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,277,234</td>
<td align="right">2,259,304</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,899,615</td>
<td align="right">15,774,428</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">711,495</td>
<td align="right">705,893</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,205,747</td>
<td align="right">2,188,380</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">87,766,122</td>
<td align="right">87,075,094</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,550,530</td>
<td align="right">7,491,081</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,618,852</td>
<td align="right">1,606,106</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,421,115</td>
<td align="right">3,394,179</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">504,099</td>
<td align="right">500,130</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,839,243</td>
<td align="right">13,730,282</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,887,951</td>
<td align="right">6,833,720</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,466,186</td>
<td align="right">10,383,783</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,949,490</td>
<td align="right">2,926,268</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,471,992</td>
<td align="right">10,389,548</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,718,981</td>
<td align="right">1,705,448</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,736,378</td>
<td align="right">54,305,459</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,943,635</td>
<td align="right">2,920,461</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,872,047</td>
<td align="right">23,684,113</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">141,125</td>
<td align="right">140,014</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">735,096</td>
<td align="right">729,309</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,129,647</td>
<td align="right">22,947,561</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,630,484</td>
<td align="right">6,578,287</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,825</td>
<td align="right">13,464,984</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,850,438</td>
<td align="right">1,835,871</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">168,929,803</td>
<td align="right">167,599,977</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,576,214</td>
<td align="right">1,563,806</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">51,849,291</td>
<td align="right">51,441,134</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,794,478</td>
<td align="right">1,780,352</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">355,952</td>
<td align="right">353,150</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">355,444</td>
<td align="right">352,646</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,602,937</td>
<td align="right">1,590,319</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">358,257</td>
<td align="right">355,437</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,508,859</td>
<td align="right">11,418,271</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">355,985</td>
<td align="right">353,183</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,260,719</td>
<td align="right">12,164,217</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,955,739</td>
<td align="right">11,861,638</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,378,580</td>
<td align="right">7,320,505</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,710,568</td>
<td align="right">6,657,751</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,217,385</td>
<td align="right">6,168,450</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,215,086</td>
<td align="right">14,103,206</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,470,562</td>
<td align="right">5,427,506</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,392,073</td>
<td align="right">2,373,247</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,795,297</td>
<td align="right">1,781,168</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,142,870</td>
<td align="right">1,133,876</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">399,392</td>
<td align="right">396,249</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,618,575</td>
<td align="right">5,574,360</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">405,899</td>
<td align="right">402,705</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,895,624</td>
<td align="right">6,841,363</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,411,412</td>
<td align="right">2,392,437</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,131,482</td>
<td align="right">5,091,104</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,248,943</td>
<td align="right">1,239,116</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,684,365</td>
<td align="right">1,671,115</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">963,586</td>
<td align="right">956,006</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">357,245</td>
<td align="right">354,435</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,166,579</td>
<td align="right">1,157,405</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,174,015</td>
<td align="right">1,164,783</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,232</td>
<td align="right">6,183</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">711,477</td>
<td align="right">705,883</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,733,290</td>
<td align="right">1,719,662</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">1,214,650</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,689,564</td>
<td align="right">1,676,281</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">910,607</td>
<td align="right">903,448</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">742,113</td>
<td align="right">736,282</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">744,420</td>
<td align="right">738,571</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">419,088</td>
<td align="right">415,796</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,766,363</td>
<td align="right">1,752,492</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">44,158,866</td>
<td align="right">43,812,230</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,938</td>
<td align="right">2,915</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10,988</td>
<td align="right">10,902</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">12,269</td>
<td align="right">12,173</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">702,437</td>
<td align="right">696,945</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">127</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,026</td>
<td align="right">1,018</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,623,239</td>
<td align="right">11,532,722</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,973</td>
<td align="right">7,911</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">10,118,874</td>
<td align="right">10,040,199</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,951,810</td>
<td align="right">8,882,355</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,308</td>
<td align="right">12,213</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">393</td>
<td align="right">390</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">131</td>
<td align="right">130</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,736</td>
<td align="right">6,685</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,091</td>
<td align="right">1,083</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,589</td>
<td align="right">3,563</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,400</td>
<td align="right">5,361</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">140</td>
<td align="right">139</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">281</td>
<td align="right">279</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">141</td>
<td align="right">140</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,747</td>
<td align="right">33,541</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">167</td>
<td align="right">166</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,636</td>
<td align="right">3,622</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,608</td>
<td align="right">4,594</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,134</td>
<td align="right">1,131</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">574</td>
<td align="right">573</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127,279</td>
<td align="right">127,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">124,278</td>
<td align="right">124,278</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,405</td>
<td align="right">1,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,028</td>
<td align="right">1,028</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">419</td>
<td align="right">419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">219</td>
<td align="right">219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">110</td>
<td align="right">110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">109</td>
<td align="right">109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">39</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">31</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
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
<td align="right">6,214,378</td>
<td align="right">16.4%</td>
<td align="right">6,165,459</td>
<td align="right">16.4%</td>
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
<td align="right">31,667,119</td>
<td align="right">83.6%</td>
<td align="right">31,417,849</td>
<td align="right">83.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,831</td>
<td align="right">0.0%</td>
<td align="right">1,829</td>
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
<td align="left">Failure</td>
<td align="right">2,733</td>
<td align="right">90.0%</td>
<td align="right">2,718</td>
<td align="right">90.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">303</td>
<td align="right">10.0%</td>
<td align="right">302</td>
<td align="right">10.0%</td>
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
<td align="left">xor</td>
<td align="right">242</td>
<td align="right">8.9%</td>
<td align="right">240</td>
<td align="right">8.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">334</td>
<td align="right">12.2%</td>
<td align="right">332</td>
<td align="right">12.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,727</td>
<td align="right">63.2%</td>
<td align="right">1,717</td>
<td align="right">63.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">175</td>
<td align="right">6.4%</td>
<td align="right">174</td>
<td align="right">6.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">73</td>
<td align="right">2.7%</td>
<td align="right">73</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">1.9%</td>
<td align="right">52</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47</td>
<td align="right">1.7%</td>
<td align="right">47</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">44</td>
<td align="right">1.6%</td>
<td align="right">44</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">23</td>
<td align="right">0.8%</td>
<td align="right">23</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">7</td>
<td align="right">0.3%</td>
<td align="right">7</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
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
<td align="right">1,224,275</td>
<td align="right">100.0%</td>
<td align="right">1,214,650</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">29,308,557</td>
<td align="right">83.5%</td>
<td align="right">29,077,801</td>
<td align="right">83.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,785,417</td>
<td align="right">16.5%</td>
<td align="right">5,739,909</td>
<td align="right">16.5%</td>
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
<td align="right">5,676,764</td>
<td align="right">16.2%</td>
<td align="right">5,632,115</td>
<td align="right">16.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">109,787</td>
<td align="right">100.0%</td>
<td align="right">108,925</td>
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
<td align="right">10</td>
<td align="right">50.0%</td>
<td align="right">10</td>
<td align="right">50.0%</td>
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
<td align="right">10</td>
<td align="right">100.0%</td>
<td align="right">10</td>
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
<td align="right">15,096</td>
<td align="right">0.1%</td>
<td align="right">14,977</td>
<td align="right">0.1%</td>
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
<td align="right">26,304,783</td>
<td align="right">91.6%</td>
<td align="right">26,097,698</td>
<td align="right">91.6%</td>
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
<td align="right">2,409,740</td>
<td align="right">8.4%</td>
<td align="right">2,390,773</td>
<td align="right">8.4%</td>
<td align="right">-0.8%</td>
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
<td align="right">1,525</td>
<td align="right">78.3%</td>
<td align="right">1,517</td>
<td align="right">78.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">422</td>
<td align="right">21.7%</td>
<td align="right">420</td>
<td align="right">21.7%</td>
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
<td align="left">tuple</td>
<td align="right">376</td>
<td align="right">24.7%</td>
<td align="right">373</td>
<td align="right">24.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">675</td>
<td align="right">44.3%</td>
<td align="right">671</td>
<td align="right">44.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">13.1%</td>
<td align="right">199</td>
<td align="right">13.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">175</td>
<td align="right">11.5%</td>
<td align="right">175</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.0%</td>
<td align="right">92</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
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
<td align="right">6,754,800</td>
<td align="right">88.1%</td>
<td align="right">6,701,623</td>
<td align="right">88.1%</td>
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
<td align="right">909,743</td>
<td align="right">11.9%</td>
<td align="right">902,585</td>
<td align="right">11.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">818</td>
<td align="right">94.7%</td>
<td align="right">817</td>
<td align="right">94.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46</td>
<td align="right">5.3%</td>
<td align="right">46</td>
<td align="right">5.3%</td>
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
<td align="right">268</td>
<td align="right">32.8%</td>
<td align="right">267</td>
<td align="right">32.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.6%</td>
<td align="right">479</td>
<td align="right">58.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">8.3%</td>
<td align="right">68</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3</td>
<td align="right">0.4%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
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
<td align="right">1,849,805</td>
<td align="right">43.5%</td>
<td align="right">1,835,242</td>
<td align="right">43.5%</td>
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
<td align="right">2,397,414</td>
<td align="right">56.4%</td>
<td align="right">2,379,537</td>
<td align="right">56.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">12</td>
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
<td align="right">615</td>
<td align="right">97.2%</td>
<td align="right">611</td>
<td align="right">97.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18</td>
<td align="right">2.8%</td>
<td align="right">18</td>
<td align="right">2.9%</td>
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
<td align="left">reversed list</td>
<td align="right">378</td>
<td align="right">61.5%</td>
<td align="right">375</td>
<td align="right">61.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">205</td>
<td align="right">33.3%</td>
<td align="right">204</td>
<td align="right">33.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">23</td>
<td align="right">3.7%</td>
<td align="right">23</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8</td>
<td align="right">1.3%</td>
<td align="right">8</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">119,281,375</td>
<td align="right">95.9%</td>
<td align="right">118,342,209</td>
<td align="right">95.9%</td>
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
<td align="right">5,126,681</td>
<td align="right">4.1%</td>
<td align="right">5,086,323</td>
<td align="right">4.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,976</td>
<td align="right">0.0%</td>
<td align="right">18,838</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">3,589</td>
<td align="right">75.1%</td>
<td align="right">3,570</td>
<td align="right">75.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,191</td>
<td align="right">24.9%</td>
<td align="right">1,191</td>
<td align="right">25.0%</td>
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
<td align="left">method</td>
<td align="right">2,392</td>
<td align="right">66.6%</td>
<td align="right">2,376</td>
<td align="right">66.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">184</td>
<td align="right">5.1%</td>
<td align="right">183</td>
<td align="right">5.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">267</td>
<td align="right">7.4%</td>
<td align="right">266</td>
<td align="right">7.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">22</td>
<td align="right">0.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,143</td>
<td align="right">0.0%</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
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
<td align="right">20,924,511</td>
<td align="right">100.0%</td>
<td align="right">20,759,823</td>
<td align="right">100.0%</td>
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
<td align="right">245</td>
<td align="right">0.0%</td>
<td align="right">245</td>
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
<td align="right">329</td>
<td align="right">100.0%</td>
<td align="right">328</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">382</td>
<td align="right">98.5%</td>
<td align="right">379</td>
<td align="right">98.4%</td>
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
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">3</td>
<td align="right">0.8%</td>
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
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">3</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,141,953</td>
<td align="right">7.8%</td>
<td align="right">1,132,963</td>
<td align="right">7.8%</td>
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
<td align="right">13,569,534</td>
<td align="right">92.1%</td>
<td align="right">13,462,710</td>
<td align="right">92.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,599</td>
<td align="right">0.1%</td>
<td align="right">14,487</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">742</td>
<td align="right">63.4%</td>
<td align="right">738</td>
<td align="right">63.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">429</td>
<td align="right">36.6%</td>
<td align="right">429</td>
<td align="right">36.8%</td>
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
<td align="left">split dict</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">178</td>
<td align="right">24.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">314</td>
<td align="right">42.3%</td>
<td align="right">312</td>
<td align="right">42.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">226</td>
<td align="right">30.5%</td>
<td align="right">226</td>
<td align="right">30.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">22</td>
<td align="right">3.0%</td>
<td align="right">22</td>
<td align="right">3.0%</td>
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
<td align="right">2,988,729</td>
<td align="right">96.0%</td>
<td align="right">2,965,197</td>
<td align="right">96.0%</td>
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
<td align="right">124,218</td>
<td align="right">4.0%</td>
<td align="right">124,218</td>
<td align="right">4.0%</td>
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
<td align="right">23</td>
<td align="right">38.3%</td>
<td align="right">23</td>
<td align="right">38.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37</td>
<td align="right">61.7%</td>
<td align="right">37</td>
<td align="right">61.7%</td>
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
<td align="right">36</td>
<td align="right">97.3%</td>
<td align="right">36</td>
<td align="right">97.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">2.7%</td>
<td align="right">1</td>
<td align="right">2.7%</td>
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
<td align="right">21,495,813</td>
<td align="right">73.9%</td>
<td align="right">21,326,554</td>
<td align="right">73.9%</td>
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
<td align="right">7,548,323</td>
<td align="right">25.9%</td>
<td align="right">7,488,889</td>
<td align="right">25.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,506</td>
<td align="right">0.2%</td>
<td align="right">52,123</td>
<td align="right">0.2%</td>
<td align="right">-0.7%</td>
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
<td align="right">2,101</td>
<td align="right">66.0%</td>
<td align="right">2,086</td>
<td align="right">66.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,080</td>
<td align="right">34.0%</td>
<td align="right">1,074</td>
<td align="right">34.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">1,619</td>
<td align="right">77.1%</td>
<td align="right">1,606</td>
<td align="right">77.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">158</td>
<td align="right">7.5%</td>
<td align="right">157</td>
<td align="right">7.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">229</td>
<td align="right">10.9%</td>
<td align="right">228</td>
<td align="right">10.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">70</td>
<td align="right">3.3%</td>
<td align="right">70</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">1.2%</td>
<td align="right">25</td>
<td align="right">1.2%</td>
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
<td align="right">746,336</td>
<td align="right">100.0%</td>
<td align="right">740,472</td>
<td align="right">100.0%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">26,565,053</td>
<td align="right">3.4%</td>
<td align="right">28,138,135</td>
<td align="right">3.6%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">391,037,673</td>
<td align="right">49.5%</td>
<td align="right">386,181,380</td>
<td align="right">49.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">366,692,689</td>
<td align="right">46.4%</td>
<td align="right">363,807,784</td>
<td align="right">46.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,889,890</td>
<td align="right">0.7%</td>
<td align="right">5,843,620</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
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
<td align="right">7,548,323</td>
<td align="right">23.4%</td>
<td align="right">7,488,889</td>
<td align="right">23.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,849,805</td>
<td align="right">5.7%</td>
<td align="right">1,835,242</td>
<td align="right">5.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,141,953</td>
<td align="right">3.5%</td>
<td align="right">1,132,963</td>
<td align="right">3.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,126,681</td>
<td align="right">15.9%</td>
<td align="right">5,086,323</td>
<td align="right">15.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,214,378</td>
<td align="right">19.3%</td>
<td align="right">6,165,459</td>
<td align="right">19.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,409,740</td>
<td align="right">7.5%</td>
<td align="right">2,390,773</td>
<td align="right">7.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">909,743</td>
<td align="right">2.8%</td>
<td align="right">902,585</td>
<td align="right">2.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,676,764</td>
<td align="right">17.6%</td>
<td align="right">5,632,115</td>
<td align="right">17.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">3.8%</td>
<td align="right">1,214,650</td>
<td align="right">3.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">124,218</td>
<td align="right">0.4%</td>
<td align="right">124,218</td>
<td align="right">0.4%</td>
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
<td align="right">10,830</td>
<td align="right">0.2%</td>
<td align="right">10,738</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,238</td>
<td align="right">0.4%</td>
<td align="right">26,018</td>
<td align="right">0.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,096</td>
<td align="right">0.3%</td>
<td align="right">14,977</td>
<td align="right">0.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,388</td>
<td align="right">4.6%</td>
<td align="right">271,234</td>
<td align="right">4.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,749,356</td>
<td align="right">46.7%</td>
<td align="right">2,727,726</td>
<td align="right">46.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,751,565</td>
<td align="right">46.7%</td>
<td align="right">2,729,928</td>
<td align="right">46.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,272</td>
<td align="right">0.1%</td>
<td align="right">8,207</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,252</td>
<td align="right">0.2%</td>
<td align="right">11,164</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,764</td>
<td align="right">0.4%</td>
<td align="right">25,605</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,333</td>
<td align="right">0.1%</td>
<td align="right">6,300</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
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
<td align="right">355,271</td>
<td align="right">1.5%</td>
<td align="right">352,474</td>
<td align="right">1.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,472,923</td>
<td align="right">98.3%</td>
<td align="right">23,288,131</td>
<td align="right">98.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,129,664</td>
<td align="right">96.9%</td>
<td align="right">22,947,578</td>
<td align="right">96.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">399,431</td>
<td align="right">1.7%</td>
<td align="right">396,288</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">399,465</td>
<td align="right">1.7%</td>
<td align="right">396,322</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,733</td>
<td align="right">0.1%</td>
<td align="right">14,618</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">258</td>
<td align="right">0.0%</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">Frame objects created</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">76</td>
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
<td align="right">63,410</td>
<td align="right"></td>
<td align="right">407</td>
<td align="right"></td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">131,341</td>
<td align="right"></td>
<td align="right">3,838</td>
<td align="right"></td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">68,046</td>
<td align="right"></td>
<td align="right">3,548</td>
<td align="right"></td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,735,385</td>
<td align="right"></td>
<td align="right">1,784,245</td>
<td align="right"></td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,673,917</td>
<td align="right">13.8%</td>
<td align="right">48,165,550</td>
<td align="right">13.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">63,190,968</td>
<td align="right">18.8%</td>
<td align="right">62,568,141</td>
<td align="right">18.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">66,581,438</td>
<td align="right">18.9%</td>
<td align="right">65,930,908</td>
<td align="right">18.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">73,597,713</td>
<td align="right">21.9%</td>
<td align="right">72,891,999</td>
<td align="right">21.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">195,011,832</td>
<td align="right">58.0%</td>
<td align="right">193,476,589</td>
<td align="right">58.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">368,537</td>
<td align="right"></td>
<td align="right">365,636</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">219,959</td>
<td align="right">0.7%</td>
<td align="right">218,228</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,266,630</td>
<td align="right">1.3%</td>
<td align="right">4,233,056</td>
<td align="right">1.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">232,710,368</td>
<td align="right">66.2%</td>
<td align="right">230,879,348</td>
<td align="right">66.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">3,547,447</td>
<td align="right">1.0%</td>
<td align="right">3,519,535</td>
<td align="right">1.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,196,387</td>
<td align="right">33.7%</td>
<td align="right">11,108,322</td>
<td align="right">33.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,967,513</td>
<td align="right">33.0%</td>
<td align="right">10,881,249</td>
<td align="right">33.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,088,869</td>
<td align="right"></td>
<td align="right">9,017,389</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,915</td>
<td align="right">0.0%</td>
<td align="right">8,845</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,027,339</td>
<td align="right">66.3%</td>
<td align="right">21,854,933</td>
<td align="right">66.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,025,077</td>
<td align="right"></td>
<td align="right">21,852,738</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,090,819</td>
<td align="right"></td>
<td align="right">7,098,995</td>
<td align="right"></td>
<td align="right">0.1%</td>
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
<td align="right">1,079</td>
<td align="right">5,924</td>
<td align="right">22,044,872</td>
<td align="right">1,193,828</td>
<td align="right">2,074,602</td>
<td align="right">1,071</td>
<td align="right">5,924</td>
<td align="right">21,973,519</td>
<td align="right">1,189,938</td>
<td align="right">2,065,014</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-28
