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
<td align="left">DELETE_NAME</td>
<td align="right">25</td>
<td align="right">725</td>
<td align="right">2,800.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,999</td>
<td align="right">1,553,607</td>
<td align="right">2,625.7%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">3,696</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,356</td>
<td align="right">92,129</td>
<td align="right">1,620.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">50,315</td>
<td align="right">1,202.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,695</td>
<td align="right">324,285</td>
<td align="right">862.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,629</td>
<td align="right">106,206</td>
<td align="right">741.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">23,410</td>
<td align="right">559.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,205</td>
<td align="right">1,578,176</td>
<td align="right">548.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,513</td>
<td align="right">14,163</td>
<td align="right">463.6%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">5,959</td>
<td align="right">455.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,803</td>
<td align="right">23,354</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,354</td>
<td align="right">333,538</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">232,167</td>
<td align="right">115,623</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">74,319</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,762</td>
<td align="right">2,332,004</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,646</td>
<td align="right">12,021,399</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,577</td>
<td align="right">120,759</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,656</td>
<td align="right">560,145</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,776</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,276</td>
<td align="right">11,838,586</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,138</td>
<td align="right">3,463,048</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">4,130,887</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,096,778</td>
<td align="right">10,781,196</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,675</td>
<td align="right">13,524,168</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,633,176</td>
<td align="right">80,093,138</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,298</td>
<td align="right">15,620,812</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,895,879</td>
<td align="right">344,895,923</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,676,297</td>
<td align="right">68,949,206</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,711</td>
<td align="right">64,101,079</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,669</td>
<td align="right">80,217</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,450</td>
<td align="right">68,996,222</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,977,965</td>
<td align="right">83,917,186</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,158,613</td>
<td align="right">61,257,524</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,504,950</td>
<td align="right">21,169,845</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,332,926</td>
<td align="right">65,311,448</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,831,719</td>
<td align="right">21,445,471</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,831,699</td>
<td align="right">21,445,450</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,005,056</td>
<td align="right">1,002,308,296</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,430,335</td>
<td align="right">5,574,769</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,657,040</td>
<td align="right">1,698,224</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,674,410</td>
<td align="right">817,502,325</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,359</td>
<td align="right">6,279,015</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,295,476</td>
<td align="right">177,313,351</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,369,793</td>
<td align="right">204,603,902</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,627</td>
<td align="right">73,792</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,505,122,187</td>
<td align="right">1,481,483,867</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,709</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">794,274,608</td>
<td align="right">806,647,113</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,590,077</td>
<td align="right">155,981,844</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,853,028</td>
<td align="right">1,607,348,555</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,831,602</td>
<td align="right">784,689,849</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,991,480</td>
<td align="right">190,607,135</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,448,641</td>
<td align="right">1,556,750,976</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,270,784</td>
<td align="right">395,736,720</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,286,629</td>
<td align="right">264,813,153</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">675,483,419</td>
<td align="right">683,991,268</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,011,786</td>
<td align="right">473,853,091</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">317,963,779</td>
<td align="right">314,009,773</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,533,349</td>
<td align="right">1,260,297,864</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,542,447</td>
<td align="right">789,787,145</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,342,054</td>
<td align="right">1,200,443,302</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,486,155</td>
<td align="right">6,559,537</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,556,996</td>
<td align="right">67,807,487</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,491,623</td>
<td align="right">1,388,305,468</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,320,194</td>
<td align="right">67,017,228</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,517</td>
<td align="right">454,419,303</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">113,987,469</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,307,865</td>
<td align="right">1,640,895,753</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,214,120</td>
<td align="right">2,513,121,763</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">335,025,632</td>
<td align="right">331,919,722</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,903,605</td>
<td align="right">2,694,542,866</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,041,819</td>
<td align="right">2,508,631,009</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,713,051</td>
<td align="right">632,106,243</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,682,683</td>
<td align="right">121,628,838</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,988</td>
<td align="right">130,184,901</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">532,592,468</td>
<td align="right">536,988,114</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">541,071,933</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,037,394</td>
<td align="right">4,788,255,446</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,414,536</td>
<td align="right">854,579,457</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,261,327</td>
<td align="right">367,346,836</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,148,118</td>
<td align="right">1,599,539,806</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,361,229</td>
<td align="right">61,875,640</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,499,103</td>
<td align="right">2,712,848,410</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,554,441</td>
<td align="right">254,694,575</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,542,628</td>
<td align="right">91,188,625</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,573,884</td>
<td align="right">350,062,254</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,837,589,773</td>
<td align="right">5,796,410,179</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,796</td>
<td align="right">337,891,671</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,760,686</td>
<td align="right">1,235,414,174</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,097,001</td>
<td align="right">155,082,588</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,329,052</td>
<td align="right">268,997,485</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,098,503</td>
<td align="right">269,426,340</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,483,022,408</td>
<td align="right">3,462,011,366</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,412,649</td>
<td align="right">2,331,222,770</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,036,923</td>
<td align="right">164,952,766</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,390</td>
<td align="right">501,632,612</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,287,092</td>
<td align="right">72,684,414</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,320,801</td>
<td align="right">114,688,895</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,378,545,632</td>
<td align="right">3,396,844,885</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,745,287</td>
<td align="right">668,240,781</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,822,948</td>
<td align="right">148,592,599</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,612,177</td>
<td align="right">353,784,441</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,123,406,426</td>
<td align="right">2,112,538,475</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,120,236</td>
<td align="right">7,247,295,011</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,055,873,108</td>
<td align="right">1,050,890,171</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,228,647</td>
<td align="right">1,035,553,625</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">98,038,429</td>
<td align="right">98,473,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,427,979</td>
<td align="right">98,863,849</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,214,899</td>
<td align="right">75,535,359</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,357,687,784</td>
<td align="right">5,380,049,434</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,193,176</td>
<td align="right">1,107,578,370</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,160,655</td>
<td align="right">1,090,747,955</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,102,972,045</td>
<td align="right">2,111,399,481</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,172,469</td>
<td align="right">534,055,848</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,594,119</td>
<td align="right">508,587,362</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,250,666</td>
<td align="right">1,536,222,976</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">252,181,924</td>
<td align="right">253,155,739</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">1,049,376,789</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,567,322</td>
<td align="right">376,161,405</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,657,601</td>
<td align="right">347,922,661</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,543,274</td>
<td align="right">28,440,970</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,569</td>
<td align="right">241,651,856</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">129,310,545</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,732</td>
<td align="right">243,701,950</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,514,133</td>
<td align="right">591,478,649</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,501,658</td>
<td align="right">70,736,808</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,454,208</td>
<td align="right">1,748,629,243</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,495,721</td>
<td align="right">843,257,184</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,887,094,996</td>
<td align="right">3,899,838,552</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,139,801,838</td>
<td align="right">2,146,671,736</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,385,171,015</td>
<td align="right">13,342,528,328</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,108,262,207</td>
<td align="right">10,076,471,104</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,932</td>
<td align="right">3,100,397</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,300</td>
<td align="right">72,491,372</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,239,556,495</td>
<td align="right">6,258,088,614</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,112,284</td>
<td align="right">386,251,629</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,805,232</td>
<td align="right">234,488,450</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,942,740</td>
<td align="right">418,720,038</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,225,012</td>
<td align="right">190,775,511</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,951,274</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">41,858,530</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,955,195</td>
<td align="right">564,543,132</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,487,807</td>
<td align="right">190,023,836</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,514</td>
<td align="right">699,148,443</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,053,972</td>
<td align="right">942,147,717</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">282,063,449</td>
<td align="right">282,660,556</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,368,853</td>
<td align="right">116,609,055</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">74,637,453</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,350,920</td>
<td align="right">2,260,890,499</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,127,782</td>
<td align="right">2,424,762,124</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,191,500</td>
<td align="right">1,355,707,068</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,870,921</td>
<td align="right">9,887,601</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,789,898,009</td>
<td align="right">5,780,498,395</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,899,417</td>
<td align="right">56,813,975</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">354,001,130</td>
<td align="right">354,527,562</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,767</td>
<td align="right">77,784,311</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,786,271</td>
<td align="right">71,683,831</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,673,726</td>
<td align="right">691,574,270</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,159,887</td>
<td align="right">484,537,798</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,163,900,491</td>
<td align="right">3,167,832,369</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">942,993,805</td>
<td align="right">941,988,172</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,808,607</td>
<td align="right">154,644,570</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,077,469</td>
<td align="right">1,253,349,275</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,671,684,261</td>
<td align="right">10,660,903,837</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,139,212</td>
<td align="right">8,539,436,598</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,616,071</td>
<td align="right">22,595,294</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,124,562</td>
<td align="right">289,863,216</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,954,695</td>
<td align="right">35,928,065</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,294,555</td>
<td align="right">415,998,227</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,613,882</td>
<td align="right">433,845,934</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,433,413,502</td>
<td align="right">3,431,650,985</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,135,782</td>
<td align="right">3,216,757,776</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,232</td>
<td align="right">158,464,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,146</td>
<td align="right">188,626,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,342,992</td>
<td align="right">7,345,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,484,231,646</td>
<td align="right">33,497,147,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,871</td>
<td align="right">127,610,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,651,748</td>
<td align="right">302,554,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,636,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,154,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,978,638</td>
<td align="right">88,969,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,410</td>
<td align="right">62,354,019</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">112,726,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right"></td>
<td align="right">80</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,228,030,626</td>
<td align="right">87.0%</td>
<td align="right">16,121,768,449</td>
<td align="right">87.0%</td>
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
<td align="right">71,483,732</td>
<td align="right">0.4%</td>
<td align="right">71,951,404</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,343,482,505</td>
<td align="right">12.6%</td>
<td align="right">2,329,992,592</td>
<td align="right">12.6%</td>
<td align="right">-0.6%</td>
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
<td align="right">912,880</td>
<td align="right">40.1%</td>
<td align="right">1,072,561</td>
<td align="right">41.5%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365,754</td>
<td align="right">59.9%</td>
<td align="right">1,513,296</td>
<td align="right">58.5%</td>
<td align="right">10.8%</td>
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
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">343</td>
<td align="right">0.0%</td>
<td align="right">697.7%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">279.6%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">8,485</td>
<td align="right">0.8%</td>
<td align="right">263.2%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">1,207</td>
<td align="right">0.1%</td>
<td align="right">246.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">626</td>
<td align="right">0.1%</td>
<td align="right">1,418</td>
<td align="right">0.1%</td>
<td align="right">126.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,167</td>
<td align="right">0.9%</td>
<td align="right">17,983</td>
<td align="right">1.7%</td>
<td align="right">120.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,060</td>
<td align="right">0.8%</td>
<td align="right">15,498</td>
<td align="right">1.4%</td>
<td align="right">119.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">754</td>
<td align="right">0.1%</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">4,257</td>
<td align="right">0.4%</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">900</td>
<td align="right">0.1%</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">2,756</td>
<td align="right">0.3%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">4,915</td>
<td align="right">0.5%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.3%</td>
<td align="right">5,634</td>
<td align="right">0.5%</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,905</td>
<td align="right">3.9%</td>
<td align="right">62,154</td>
<td align="right">5.8%</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,095</td>
<td align="right">0.1%</td>
<td align="right">1,759</td>
<td align="right">0.2%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">13,113</td>
<td align="right">1.2%</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,830</td>
<td align="right">4.7%</td>
<td align="right">63,122</td>
<td align="right">5.9%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">64,451</td>
<td align="right">6.0%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">11,049</td>
<td align="right">1.0%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,453</td>
<td align="right">4.8%</td>
<td align="right">56,717</td>
<td align="right">5.3%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,509</td>
<td align="right">2.6%</td>
<td align="right">29,812</td>
<td align="right">2.8%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,989</td>
<td align="right">3.7%</td>
<td align="right">41,991</td>
<td align="right">3.9%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">14,054</td>
<td align="right">1.3%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">3,765</td>
<td align="right">0.4%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">22,731</td>
<td align="right">2.1%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">25,632</td>
<td align="right">2.4%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">78,865</td>
<td align="right">8.6%</td>
<td align="right">87,196</td>
<td align="right">8.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">126,579</td>
<td align="right">11.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,199</td>
<td align="right">8.1%</td>
<td align="right">71,163</td>
<td align="right">6.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">88,203</td>
<td align="right">8.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,941</td>
<td align="right">11.8%</td>
<td align="right">109,867</td>
<td align="right">10.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">114,008</td>
<td align="right">10.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">545,503,600</td>
<td align="right">100.0%</td>
<td align="right">541,071,933</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,691,750</td>
<td align="right">1.6%</td>
<td align="right">185,673,841</td>
<td align="right">1.7%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">182,052,462</td>
<td align="right">1.6%</td>
<td align="right">188,244,360</td>
<td align="right">1.7%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,101,393,944</td>
<td align="right">98.4%</td>
<td align="right">11,056,783,111</td>
<td align="right">98.3%</td>
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
<td align="right">3,603,771</td>
<td align="right">100.0%</td>
<td align="right">4,148,529</td>
<td align="right">100.0%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">166</td>
<td align="right">0.0%</td>
<td align="right">13.7%</td>
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
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">352.8%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">254.7%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">166</td>
<td align="right">100.0%</td>
<td align="right">13.7%</td>
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
<td align="right">574,328</td>
<td align="right">96.6%</td>
<td align="right">685,046</td>
<td align="right">91.8%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">581,624</td>
<td align="right">97.9%</td>
<td align="right">640,338</td>
<td align="right">85.8%</td>
<td align="right">10.1%</td>
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
<td align="right">19,925</td>
<td align="right">100.0%</td>
<td align="right">61,498</td>
<td align="right">100.0%</td>
<td align="right">208.6%</td>
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
<td align="right">1,273,878</td>
<td align="right">0.0%</td>
<td align="right">1,332,667</td>
<td align="right">0.0%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">510,368,810</td>
<td align="right">10.2%</td>
<td align="right">508,251,809</td>
<td align="right">10.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,505,613,399</td>
<td align="right">89.8%</td>
<td align="right">4,507,491,114</td>
<td align="right">89.8%</td>
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
<td align="right">41,449</td>
<td align="right">16.6%</td>
<td align="right">90,012</td>
<td align="right">25.0%</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">207,585</td>
<td align="right">83.4%</td>
<td align="right">270,204</td>
<td align="right">75.0%</td>
<td align="right">30.2%</td>
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
<td align="right">934</td>
<td align="right">0.4%</td>
<td align="right">3,151</td>
<td align="right">1.2%</td>
<td align="right">237.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.1%</td>
<td align="right">514</td>
<td align="right">0.2%</td>
<td align="right">162.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,763</td>
<td align="right">3.7%</td>
<td align="right">19,230</td>
<td align="right">7.1%</td>
<td align="right">147.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">2,842</td>
<td align="right">1.1%</td>
<td align="right">114.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,480</td>
<td align="right">5.0%</td>
<td align="right">20,663</td>
<td align="right">7.6%</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,875</td>
<td align="right">0.9%</td>
<td align="right">2,845</td>
<td align="right">1.1%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,413</td>
<td align="right">21.9%</td>
<td align="right">64,639</td>
<td align="right">23.9%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,307</td>
<td align="right">5.4%</td>
<td align="right">14,692</td>
<td align="right">5.4%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,399</td>
<td align="right">11.3%</td>
<td align="right">27,744</td>
<td align="right">10.3%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.7%</td>
<td align="right">9,009</td>
<td align="right">3.3%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,831</td>
<td align="right">3.3%</td>
<td align="right">7,623</td>
<td align="right">2.8%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,415</td>
<td align="right">43.6%</td>
<td align="right">97,252</td>
<td align="right">36.0%</td>
<td align="right">7.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,403,375</td>
<td align="right">0.1%</td>
<td align="right">1,369,433</td>
<td align="right">0.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">153,529,717</td>
<td align="right">6.6%</td>
<td align="right">155,846,852</td>
<td align="right">6.7%</td>
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
<td align="right">2,186,664,715</td>
<td align="right">93.4%</td>
<td align="right">2,181,105,744</td>
<td align="right">93.3%</td>
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
<td align="left">Failure</td>
<td align="right">58,250</td>
<td align="right">67.1%</td>
<td align="right">119,302</td>
<td align="right">74.2%</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,585</td>
<td align="right">32.9%</td>
<td align="right">41,415</td>
<td align="right">25.8%</td>
<td align="right">44.9%</td>
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
<td align="right">10,993</td>
<td align="right">18.9%</td>
<td align="right">31,287</td>
<td align="right">26.2%</td>
<td align="right">184.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,773</td>
<td align="right">37.4%</td>
<td align="right">42,067</td>
<td align="right">35.3%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,944</td>
<td align="right">18.8%</td>
<td align="right">19,756</td>
<td align="right">16.6%</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,540</td>
<td align="right">25.0%</td>
<td align="right">26,192</td>
<td align="right">22.0%</td>
<td align="right">80.1%</td>
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
<td align="right">1,504,679,551</td>
<td align="right">29.3%</td>
<td align="right">1,480,904,465</td>
<td align="right">28.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,009,337</td>
<td align="right">3.2%</td>
<td align="right">162,066,014</td>
<td align="right">3.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,470,123,652</td>
<td align="right">67.5%</td>
<td align="right">3,485,619,801</td>
<td align="right">68.0%</td>
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
<td align="right">437,244</td>
<td align="right">12.4%</td>
<td align="right">519,788</td>
<td align="right">14.3%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,728</td>
<td align="right">87.6%</td>
<td align="right">3,117,044</td>
<td align="right">85.7%</td>
<td align="right">0.6%</td>
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
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">1,159</td>
<td align="right">0.2%</td>
<td align="right">345.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">2,124</td>
<td align="right">0.4%</td>
<td align="right">298.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,282</td>
<td align="right">1.0%</td>
<td align="right">8,625</td>
<td align="right">1.7%</td>
<td align="right">101.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">11,801</td>
<td align="right">2.3%</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">5,583</td>
<td align="right">1.1%</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">2,065</td>
<td align="right">0.4%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,542</td>
<td align="right">2.4%</td>
<td align="right">17,148</td>
<td align="right">3.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,420</td>
<td align="right">0.8%</td>
<td align="right">5,499</td>
<td align="right">1.1%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,704</td>
<td align="right">7.9%</td>
<td align="right">46,751</td>
<td align="right">9.0%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">24,379</td>
<td align="right">4.7%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">70,961</td>
<td align="right">16.2%</td>
<td align="right">94,378</td>
<td align="right">18.2%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,016</td>
<td align="right">4.1%</td>
<td align="right">23,445</td>
<td align="right">4.5%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">12,435</td>
<td align="right">2.4%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,675</td>
<td align="right">19.1%</td>
<td align="right">89,063</td>
<td align="right">17.1%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">171,565</td>
<td align="right">39.2%</td>
<td align="right">175,073</td>
<td align="right">33.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">enumerate</td>
<td align="right">5,508,979</td>
<td align="right">5,508,979 / 0 !!</td>
<td align="right">5,653,422</td>
<td align="right">5,653,422 / 0 !!</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,107,651</td>
<td align="right">12,107,651 / 0 !!</td>
<td align="right">12,372,104</td>
<td align="right">12,372,104 / 0 !!</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,369,952</td>
<td align="right">119,369,952 / 0 !!</td>
<td align="right">117,059,061</td>
<td align="right">117,059,061 / 0 !!</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,932,891</td>
<td align="right">34,932,891 / 0 !!</td>
<td align="right">34,399,735</td>
<td align="right">34,399,735 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,958,975</td>
<td align="right">341,958,975 / 0 !!</td>
<td align="right">336,986,978</td>
<td align="right">336,986,978 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,254,976</td>
<td align="right">171,254,976 / 0 !!</td>
<td align="right">173,286,448</td>
<td align="right">173,286,448 / 0 !!</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,823,200</td>
<td align="right">2,823,200 / 0 !!</td>
<td align="right">2,799,054</td>
<td align="right">2,799,054 / 0 !!</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,453,731</td>
<td align="right">304,453,731 / 0 !!</td>
<td align="right">305,699,109</td>
<td align="right">305,699,109 / 0 !!</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,923,169</td>
<td align="right">101,923,169 / 0 !!</td>
<td align="right">101,677,715</td>
<td align="right">101,677,715 / 0 !!</td>
<td align="right">-0.2%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,436,011</td>
<td align="right">0.0%</td>
<td align="right">1,386,949</td>
<td align="right">0.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">799,901,759</td>
<td align="right">5.9%</td>
<td align="right">814,701,502</td>
<td align="right">6.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">860,555,125</td>
<td align="right">6.3%</td>
<td align="right">869,368,729</td>
<td align="right">6.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,981,906,576</td>
<td align="right">87.8%</td>
<td align="right">11,999,088,448</td>
<td align="right">87.7%</td>
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
<td align="right">505,630</td>
<td align="right">3.0%</td>
<td align="right">837,919</td>
<td align="right">4.7%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,315,555</td>
<td align="right">97.0%</td>
<td align="right">17,011,184</td>
<td align="right">95.3%</td>
<td align="right">4.3%</td>
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
<td align="right">1,885</td>
<td align="right">0.4%</td>
<td align="right">21,886</td>
<td align="right">2.6%</td>
<td align="right">1,061.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">328.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">192.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">3,171</td>
<td align="right">0.4%</td>
<td align="right">187.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,193</td>
<td align="right">10.5%</td>
<td align="right">145,417</td>
<td align="right">17.4%</td>
<td align="right">173.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,310</td>
<td align="right">1.1%</td>
<td align="right">13,506</td>
<td align="right">1.6%</td>
<td align="right">154.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,721</td>
<td align="right">0.3%</td>
<td align="right">4,327</td>
<td align="right">0.5%</td>
<td align="right">151.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">9,020</td>
<td align="right">1.1%</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,154</td>
<td align="right">1.6%</td>
<td align="right">16,247</td>
<td align="right">1.9%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,801</td>
<td align="right">3.1%</td>
<td align="right">30,993</td>
<td align="right">3.7%</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">5,081</td>
<td align="right">0.6%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,421</td>
<td align="right">4.8%</td>
<td align="right">42,681</td>
<td align="right">5.1%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">91,783</td>
<td align="right">11.0%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">73,633</td>
<td align="right">14.6%</td>
<td align="right">112,969</td>
<td align="right">13.5%</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
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
<td align="right">51,816</td>
<td align="right">0.0%</td>
<td align="right">303,522</td>
<td align="right">0.0%</td>
<td align="right">485.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">5,094</td>
<td align="right">0.0%</td>
<td align="right">270.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,452</td>
<td align="right">0.2%</td>
<td align="right">15,099,664</td>
<td align="right">0.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,216,083,589</td>
<td align="right">99.8%</td>
<td align="right">9,192,951,542</td>
<td align="right">99.8%</td>
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
<td align="right">134,597</td>
<td align="right">100.0%</td>
<td align="right">526,091</td>
<td align="right">100.0%</td>
<td align="right">290.9%</td>
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
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">6,993</td>
<td align="right">0.0%</td>
<td align="right">3,344.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,155,643</td>
<td align="right">100.0%</td>
<td align="right">67,201,476</td>
<td align="right">100.0%</td>
<td align="right">4.7%</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">7,170</td>
<td align="right">100.0%</td>
<td align="right">210.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">27,421</td>
<td align="right">0.0%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,499,422</td>
<td align="right">82.2%</td>
<td align="right">591,451,228</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,951</td>
<td align="right">17.8%</td>
<td align="right">129,260,570</td>
<td align="right">17.9%</td>
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
<td align="left">Success</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">591.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
<td align="right">33.5%</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">197.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
<td align="right">182.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">2.5%</td>
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
<td align="right">114,207,228</td>
<td align="right">5.7%</td>
<td align="right">125,541,491</td>
<td align="right">6.2%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,870</td>
<td align="right">3.3%</td>
<td align="right">68,781,423</td>
<td align="right">3.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,768,429</td>
<td align="right">90.9%</td>
<td align="right">1,827,706,251</td>
<td align="right">90.4%</td>
<td align="right">0.8%</td>
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
<td align="right">44,915</td>
<td align="right">2.0%</td>
<td align="right">104,454</td>
<td align="right">4.0%</td>
<td align="right">132.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,193,780</td>
<td align="right">98.0%</td>
<td align="right">2,474,903</td>
<td align="right">96.0%</td>
<td align="right">12.8%</td>
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
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">7,044</td>
<td align="right">6.7%</td>
<td align="right">843.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">468.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">1,823</td>
<td align="right">1.7%</td>
<td align="right">402.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,340</td>
<td align="right">7.4%</td>
<td align="right">11,043</td>
<td align="right">10.6%</td>
<td align="right">230.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">190.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">251</td>
<td align="right">0.2%</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">3,088</td>
<td align="right">3.0%</td>
<td align="right">133.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">43,626</td>
<td align="right">41.8%</td>
<td align="right">122.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">7,974</td>
<td align="right">7.6%</td>
<td align="right">113.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">14,124</td>
<td align="right">13.5%</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">9,321</td>
<td align="right">8.9%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">248,234</td>
<td align="right">552.7%</td>
<td align="right">319,820</td>
<td align="right">306.2%</td>
<td align="right">28.8%</td>
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
<td align="right">112,724,902</td>
<td align="right">100.0%</td>
<td align="right">112,726,125</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,526,859</td>
<td align="right">56.7%</td>
<td align="right">914,603,226</td>
<td align="right">56.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">700,605,612</td>
<td align="right">43.3%</td>
<td align="right">698,908,385</td>
<td align="right">43.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">15,210</td>
<td align="right">6.3%</td>
<td align="right">636.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">181,878</td>
<td align="right">98.9%</td>
<td align="right">224,888</td>
<td align="right">93.7%</td>
<td align="right">23.6%</td>
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
<td align="right">17,164</td>
<td align="right">9.4%</td>
<td align="right">45,076</td>
<td align="right">20.0%</td>
<td align="right">162.6%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">147.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">3,060</td>
<td align="right">1.4%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">8,875</td>
<td align="right">3.9%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">4,465</td>
<td align="right">2.0%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">23,849</td>
<td align="right">10.6%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">53,621</td>
<td align="right">23.8%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">85,774</td>
<td align="right">38.1%</td>
<td align="right">-0.9%</td>
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
<td align="right">110,663,160</td>
<td align="right">2.2%</td>
<td align="right">113,803,616</td>
<td align="right">2.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">255,907,359</td>
<td align="right">5.0%</td>
<td align="right">253,823,668</td>
<td align="right">5.0%</td>
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
<td align="right">4,725,965,587</td>
<td align="right">92.8%</td>
<td align="right">4,739,716,925</td>
<td align="right">92.8%</td>
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
<td align="left">Success</td>
<td align="right">2,136,471</td>
<td align="right">78.2%</td>
<td align="right">2,365,812</td>
<td align="right">78.5%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,941</td>
<td align="right">21.8%</td>
<td align="right">646,550</td>
<td align="right">21.5%</td>
<td align="right">8.3%</td>
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
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,047</td>
<td align="right">1.7%</td>
<td align="right">19,929</td>
<td align="right">3.1%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,303</td>
<td align="right">2.7%</td>
<td align="right">23,797</td>
<td align="right">3.7%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,721</td>
<td align="right">1.6%</td>
<td align="right">11,872</td>
<td align="right">1.8%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,557</td>
<td align="right">14.0%</td>
<td align="right">95,787</td>
<td align="right">14.8%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">81,581</td>
<td align="right">12.6%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">20,936</td>
<td align="right">3.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">126,706</td>
<td align="right">21.2%</td>
<td align="right">133,144</td>
<td align="right">20.6%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,846</td>
<td align="right">43.2%</td>
<td align="right">257,442</td>
<td align="right">39.8%</td>
<td align="right">-0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,318</td>
<td align="right">0.1%</td>
<td align="right">1,658,491</td>
<td align="right">0.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,237,457,096</td>
<td align="right">99.9%</td>
<td align="right">1,242,777,928</td>
<td align="right">99.9%</td>
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
<td align="left">Success</td>
<td align="right">9,889</td>
<td align="right">91.5%</td>
<td align="right">37,233</td>
<td align="right">93.6%</td>
<td align="right">276.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">913</td>
<td align="right">8.5%</td>
<td align="right">2,540</td>
<td align="right">6.4%</td>
<td align="right">178.2%</td>
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
<td align="right">99</td>
<td align="right">10.8%</td>
<td align="right">378</td>
<td align="right">14.9%</td>
<td align="right">281.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">678</td>
<td align="right">74.3%</td>
<td align="right">1,846</td>
<td align="right">72.7%</td>
<td align="right">172.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.9%</td>
<td align="right">316</td>
<td align="right">12.4%</td>
<td align="right">132.4%</td>
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
<td align="right">1,506,459,842</td>
<td align="right">0.7%</td>
<td align="right">1,534,817,073</td>
<td align="right">0.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,238,131,438</td>
<td align="right">3.9%</td>
<td align="right">8,210,491,547</td>
<td align="right">3.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,542,598,940</td>
<td align="right">37.3%</td>
<td align="right">78,477,036,813</td>
<td align="right">37.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,096,913,279</td>
<td align="right">58.0%</td>
<td align="right">122,089,752,167</td>
<td align="right">58.1%</td>
<td align="right">-0.0%</td>
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
<td align="left">CALL</td>
<td align="right">178,691,750</td>
<td align="right">2.4%</td>
<td align="right">185,673,841</td>
<td align="right">2.5%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">799,901,759</td>
<td align="right">10.9%</td>
<td align="right">814,701,502</td>
<td align="right">11.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,504,679,551</td>
<td align="right">20.6%</td>
<td align="right">1,480,904,465</td>
<td align="right">20.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,529,717</td>
<td align="right">2.1%</td>
<td align="right">155,846,852</td>
<td align="right">2.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,907,359</td>
<td align="right">3.5%</td>
<td align="right">253,823,668</td>
<td align="right">3.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">7.5%</td>
<td align="right">541,071,933</td>
<td align="right">7.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,343,482,505</td>
<td align="right">32.0%</td>
<td align="right">2,329,992,592</td>
<td align="right">31.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,368,810</td>
<td align="right">7.0%</td>
<td align="right">508,251,809</td>
<td align="right">7.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">1.8%</td>
<td align="right">129,260,570</td>
<td align="right">1.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,612</td>
<td align="right">9.6%</td>
<td align="right">698,908,385</td>
<td align="right">9.6%</td>
<td align="right">-0.2%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,666</td>
<td align="right">6.2%</td>
<td align="right">105,769,620</td>
<td align="right">6.9%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,362,220</td>
<td align="right">3.3%</td>
<td align="right">52,115,413</td>
<td align="right">3.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,667,061</td>
<td align="right">5.4%</td>
<td align="right">84,766,312</td>
<td align="right">5.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,824,339</td>
<td align="right">5.5%</td>
<td align="right">84,211,320</td>
<td align="right">5.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,923,885</td>
<td align="right">5.4%</td>
<td align="right">80,913,375</td>
<td align="right">5.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,008,057</td>
<td align="right">5.4%</td>
<td align="right">81,070,391</td>
<td align="right">5.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,459,315</td>
<td align="right">24.3%</td>
<td align="right">369,438,128</td>
<td align="right">24.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,472,369</td>
<td align="right">3.6%</td>
<td align="right">54,850,180</td>
<td align="right">3.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,889,293</td>
<td align="right">6.0%</td>
<td align="right">89,366,252</td>
<td align="right">5.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,664,476</td>
<td align="right">17.6%</td>
<td align="right">265,857,242</td>
<td align="right">17.3%</td>
<td align="right">0.5%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">1,202.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,894,382</td>
<td align="right">15.0%</td>
<td align="right">1,015,528,836</td>
<td align="right">15.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,171,703</td>
<td align="right">15.1%</td>
<td align="right">1,019,803,073</td>
<td align="right">15.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,698,141</td>
<td align="right">1.1%</td>
<td align="right">71,569,989</td>
<td align="right">1.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">4,223,922</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,590,748</td>
<td align="right">0.4%</td>
<td align="right">23,814,897</td>
<td align="right">0.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,635,737</td>
<td align="right">23.8%</td>
<td align="right">1,604,224,827</td>
<td align="right">23.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,635,737</td>
<td align="right">23.8%</td>
<td align="right">1,604,224,827</td>
<td align="right">23.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">131,916,029</td>
<td align="right">2.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,414,735,744</td>
<td align="right">81.0%</td>
<td align="right">5,437,708,436</td>
<td align="right">81.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,093,551,511</td>
<td align="right">76.2%</td>
<td align="right">5,099,607,968</td>
<td align="right">76.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,476,902</td>
<td align="right">3.9%</td>
<td align="right">259,753,431</td>
<td align="right">3.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,464,034</td>
<td align="right">8.7%</td>
<td align="right">584,421,754</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,667,846</td>
<td align="right">4.1%</td>
<td align="right">275,670,294</td>
<td align="right">4.1%</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,037,334</td>
<td align="right"></td>
<td align="right">58,852,143</td>
<td align="right"></td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,482</td>
<td align="right">1.9%</td>
<td align="right">3,639,155</td>
<td align="right">2.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">60,961,175</td>
<td align="right"></td>
<td align="right">65,104,701</td>
<td align="right"></td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,262</td>
<td align="right">0.0%</td>
<td align="right">6,599,518</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,725,961</td>
<td align="right"></td>
<td align="right">6,944,375</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,364,955,120</td>
<td align="right"></td>
<td align="right">2,411,926,286</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,611,785</td>
<td align="right"></td>
<td align="right">177,717,882</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,266,610</td>
<td align="right">0.4%</td>
<td align="right">71,700,800</td>
<td align="right">0.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,569,929,868</td>
<td align="right">70.9%</td>
<td align="right">13,495,024,131</td>
<td align="right">70.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,570,042,925</td>
<td align="right"></td>
<td align="right">13,496,735,235</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,952,872,473</td>
<td align="right">25.1%</td>
<td align="right">23,067,147,765</td>
<td align="right">25.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,383</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,446,675,186</td>
<td align="right"></td>
<td align="right">2,435,545,446</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,558,831,830</td>
<td align="right">29.1%</td>
<td align="right">5,580,242,152</td>
<td align="right">29.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,481,199,958</td>
<td align="right">28.7%</td>
<td align="right">5,501,941,834</td>
<td align="right">28.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,748,924,229</td>
<td align="right">29.2%</td>
<td align="right">31,642,995,748</td>
<td align="right">29.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,156,567,035</td>
<td align="right"></td>
<td align="right">6,139,545,205</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,067,042,731</td>
<td align="right">42.6%</td>
<td align="right">39,131,543,013</td>
<td align="right">42.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,906,384,699</td>
<td align="right">22.9%</td>
<td align="right">24,941,348,949</td>
<td align="right">23.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,544,994</td>
<td align="right">5.1%</td>
<td align="right">4,647,714,125</td>
<td align="right">5.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,137,337,210</td>
<td align="right">46.1%</td>
<td align="right">50,176,490,628</td>
<td align="right">46.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,942,599,100</td>
<td align="right">27.2%</td>
<td align="right">24,932,214,731</td>
<td align="right">27.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,312,142</td>
<td align="right">1.7%</td>
<td align="right">1,860,848,469</td>
<td align="right">1.7%</td>
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
<td align="right">364,847</td>
<td align="right">102,017,796</td>
<td align="right">9,534,047,281</td>
<td align="right">758,771,873</td>
<td align="right">763,945,882</td>
<td align="right">367,208</td>
<td align="right">94,657,058</td>
<td align="right">9,775,164,693</td>
<td align="right">817,629,757</td>
<td align="right">755,947,779</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,058,112</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,194,488</td>
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
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">41</td>
<td align="right">901</td>
<td align="right">2,097.6%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">34</td>
<td align="right">714</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,239</td>
<td align="right">-1.6%</td>
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
<td align="right">2,397</td>
<td align="right">2,337</td>
<td align="right">-2.5%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-26
