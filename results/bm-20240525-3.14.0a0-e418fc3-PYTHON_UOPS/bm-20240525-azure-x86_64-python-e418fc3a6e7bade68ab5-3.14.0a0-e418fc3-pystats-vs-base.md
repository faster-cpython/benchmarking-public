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
<td align="left">JUMP_BACKWARD</td>
<td align="right">4,917,503,151</td>
<td align="right">2,282,281</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">80,934,741</td>
<td align="right">211,834</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,123,940</td>
<td align="right">162,960</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">162,427,160</td>
<td align="right">7,254,200</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">832,090,533</td>
<td align="right">47,431,467</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">133,515,680</td>
<td align="right">8,000,960</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">233,230,359</td>
<td align="right">18,683,588</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">76,978,491</td>
<td align="right">7,569,330</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,783,304,815</td>
<td align="right">176,377,726</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">665,650,854</td>
<td align="right">68,001,202</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">189,307,277</td>
<td align="right">22,311,296</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">12,200,126</td>
<td align="right">1,470,151</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">589,480,834</td>
<td align="right">78,178,605</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,797,498</td>
<td align="right">244,537</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,382,308,235</td>
<td align="right">190,039,362</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,933,562,177</td>
<td align="right">275,139,128</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">97,500,481</td>
<td align="right">13,904,753</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">232,768,583</td>
<td align="right">33,292,163</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">448,578,453</td>
<td align="right">64,747,741</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">649,546,608</td>
<td align="right">94,788,381</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">506,699,164</td>
<td align="right">74,089,757</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">119,377,774</td>
<td align="right">17,572,653</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,081,118</td>
<td align="right">2,365,215</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">457,479,214</td>
<td align="right">72,807,650</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,193,233,953</td>
<td align="right">513,031,362</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,591,077,179</td>
<td align="right">288,576,488</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">212,920,022</td>
<td align="right">40,272,250</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,674,382,420</td>
<td align="right">326,500,800</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">515,627,939</td>
<td align="right">109,231,062</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,779,490,138</td>
<td align="right">384,500,215</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,323,584,069</td>
<td align="right">290,764,258</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,497,462,312</td>
<td align="right">353,126,753</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">427,317,632</td>
<td align="right">102,114,370</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">195,351,500</td>
<td align="right">48,007,894</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">338,196,208</td>
<td align="right">83,133,988</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">43,290,524</td>
<td align="right">10,875,612</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">131,598,850</td>
<td align="right">33,162,143</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,466,856,086</td>
<td align="right">622,341,054</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,623,519,265</td>
<td align="right">414,959,098</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">110,852,301</td>
<td align="right">30,005,081</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,388,282,224</td>
<td align="right">392,555,435</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">288,577,480</td>
<td align="right">85,233,329</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">284,106,387</td>
<td align="right">84,439,285</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">944,893,473</td>
<td align="right">284,972,893</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">211,756,570</td>
<td align="right">65,832,041</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">469,772,208</td>
<td align="right">147,364,033</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,167,499,892</td>
<td align="right">706,912,433</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,740,281,041</td>
<td align="right">5,029,459,999</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,679,726,723</td>
<td align="right">5,040,085,297</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,562,542,114</td>
<td align="right">1,913,640,778</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,441,386,475</td>
<td align="right">4,008,650,480</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,258,840,093</td>
<td align="right">444,775,943</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">279,407,459</td>
<td align="right">104,982,760</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,149,978,684</td>
<td align="right">4,981,354,937</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,022,386,997</td>
<td align="right">392,009,890</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">152,413,371</td>
<td align="right">58,440,337</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">127,709,343</td>
<td align="right">49,031,841</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">942,673,224</td>
<td align="right">366,073,479</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">699,745,292</td>
<td align="right">273,414,770</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,217,294</td>
<td align="right">32,547,068</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">839,355,294</td>
<td align="right">332,986,783</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">795,332,090</td>
<td align="right">317,629,626</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">577,115,887</td>
<td align="right">233,204,760</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">176,569,840</td>
<td align="right">72,220,826</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,152,120,651</td>
<td align="right">890,210,786</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">843,331,111</td>
<td align="right">350,121,321</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">844,000,982</td>
<td align="right">354,146,683</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">8,204,680</td>
<td align="right">3,464,680</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">99,244,044</td>
<td align="right">42,165,155</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">434,337,555</td>
<td align="right">188,505,588</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,811,619,578</td>
<td align="right">1,226,900,764</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,219,783,194</td>
<td align="right">970,822,215</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">43,642,220,831</td>
<td align="right">19,248,423,266</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">357,627,324</td>
<td align="right">158,553,839</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">155,858,911</td>
<td align="right">70,678,021</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">478,663,130</td>
<td align="right">218,119,341</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">213,147,315</td>
<td align="right">97,168,748</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">68,773,874</td>
<td align="right">31,597,939</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,182,020</td>
<td align="right">546,580</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">360,261,992</td>
<td align="right">168,844,943</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">93,948,040</td>
<td align="right">44,302,692</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,181,678,851</td>
<td align="right">587,715,779</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,188,386,462</td>
<td align="right">1,103,776,680</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">544,386,590</td>
<td align="right">277,020,613</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">399,430,651</td>
<td align="right">203,929,338</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,228,723,305</td>
<td align="right">2,676,683,010</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,891,288,309</td>
<td align="right">982,776,456</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,975,252,570</td>
<td align="right">1,031,274,064</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">18,058,151</td>
<td align="right">9,613,141</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,335,030,890</td>
<td align="right">1,253,164,526</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,143,833,001</td>
<td align="right">2,229,003,751</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">12,309,310</td>
<td align="right">6,637,213</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,270,060</td>
<td align="right">1,783,115</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">410,249,133</td>
<td align="right">225,412,995</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">253,880,120</td>
<td align="right">141,994,543</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">337,750,059</td>
<td align="right">189,470,659</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">189,520,995</td>
<td align="right">106,897,937</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">346,630,146</td>
<td align="right">195,712,973</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">664,725,681</td>
<td align="right">379,938,578</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,132,640</td>
<td align="right">8,087,860</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">437,674,145</td>
<td align="right">251,013,417</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">83,960</td>
<td align="right">49,180</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">243,756,230</td>
<td align="right">143,313,510</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">998,242,650</td>
<td align="right">591,755,746</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,044,708,336</td>
<td align="right">4,176,269,281</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">249,499,246</td>
<td align="right">148,276,008</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">660,655,404</td>
<td align="right">397,311,929</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">65,864,447</td>
<td align="right">39,945,359</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,244,747</td>
<td align="right">13,042,404</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,244,885</td>
<td align="right">13,050,164</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">86,777,996</td>
<td align="right">53,475,709</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">354,411,713</td>
<td align="right">219,184,574</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">701,374,693</td>
<td align="right">434,109,266</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,773,792</td>
<td align="right">13,054,074</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">481,704,975</td>
<td align="right">322,346,234</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,795,515,021</td>
<td align="right">3,259,638,281</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">177,018,312</td>
<td align="right">122,116,066</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,041,440</td>
<td align="right">719,420</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,831,592,660</td>
<td align="right">5,470,778,482</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">74,754,921</td>
<td align="right">52,503,061</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">139,685,160</td>
<td align="right">98,885,500</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">819,230,355</td>
<td align="right">582,633,020</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,346,002</td>
<td align="right">105,671,082</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">499,560,498</td>
<td align="right">356,445,639</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">558,370,312</td>
<td align="right">398,898,234</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,975,004</td>
<td align="right">4,407,394</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,542,754,354</td>
<td align="right">1,145,478,274</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">626,431,602</td>
<td align="right">468,876,170</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,132,684,939</td>
<td align="right">3,131,173,505</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">389,878,046</td>
<td align="right">298,693,151</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">196,418,060</td>
<td align="right">150,950,828</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,760</td>
<td align="right">22,820</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,822,253,457</td>
<td align="right">3,850,037,272</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">64,954,158</td>
<td align="right">52,179,020</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,285,461,206</td>
<td align="right">1,048,693,433</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,927,302,314</td>
<td align="right">1,586,687,107</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">208,280,762</td>
<td align="right">172,973,292</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">369,178,661</td>
<td align="right">312,669,165</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,040</td>
<td align="right">900</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">119,293,256</td>
<td align="right">104,677,244</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,866,059</td>
<td align="right">9,619,785</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,240</td>
<td align="right">2,000</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,260</td>
<td align="right">2,020</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">88,168,517</td>
<td align="right">83,092,835</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,390,968</td>
<td align="right">258,851,012</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">25,780</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,395,798,665</td>
<td align="right">1,338,557,922</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,480,880</td>
<td align="right">90,672,640</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,285,175,551</td>
<td align="right">2,376,030,380</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">94,738,413</td>
<td align="right">91,111,169</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">229,115,010</td>
<td align="right">221,668,530</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,436,296</td>
<td align="right">46,613,160</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,198,360</td>
<td align="right">90,667,500</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,187</td>
<td align="right">16,004</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">507,146</td>
<td align="right">502,660</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,988,199</td>
<td align="right">6,964,324</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,365,813</td>
<td align="right">20,302,940</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,242,115</td>
<td align="right">9,215,596</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,269,608</td>
<td align="right">228,622,190</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,912,554</td>
<td align="right">81,766,322</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,666,132</td>
<td align="right">9,651,108</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">147,280</td>
<td align="right">147,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,874,196</td>
<td align="right">1,873,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,674,167</td>
<td align="right">116,620,333</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">94,200</td>
<td align="right">94,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,917,686</td>
<td align="right">555,713,467</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,823,509</td>
<td align="right">1,822,994</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,729</td>
<td align="right">692,551</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,344,684</td>
<td align="right">233,312,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,225,776</td>
<td align="right">786,216,135</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,026,568</td>
<td align="right">402,024,605</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,852</td>
<td align="right">173,318,590</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">2,319,669,566</td>
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
<td align="right">6,951,362,371</td>
<td align="right">82.9%</td>
<td align="right">1,367,519,468</td>
<td align="right">76.4%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,435,935,558</td>
<td align="right">17.1%</td>
<td align="right">420,374,598</td>
<td align="right">23.5%</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">50,340,300</td>
<td align="right">0.6%</td>
<td align="right">29,500,920</td>
<td align="right">1.6%</td>
<td align="right">-41.4%</td>
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
<td align="right">991,665</td>
<td align="right">36.9%</td>
<td align="right">591,310</td>
<td align="right">35.2%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,695,301</td>
<td align="right">63.1%</td>
<td align="right">1,090,447</td>
<td align="right">64.8%</td>
<td align="right">-35.7%</td>
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
<td align="right">28,769</td>
<td align="right">1.7%</td>
<td align="right">5,025</td>
<td align="right">0.5%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">216,777</td>
<td align="right">12.8%</td>
<td align="right">38,089</td>
<td align="right">3.5%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">36,951</td>
<td align="right">2.2%</td>
<td align="right">8,605</td>
<td align="right">0.8%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">66,732</td>
<td align="right">3.9%</td>
<td align="right">15,971</td>
<td align="right">1.5%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">17,765</td>
<td align="right">1.0%</td>
<td align="right">4,723</td>
<td align="right">0.4%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">29,505</td>
<td align="right">1.7%</td>
<td align="right">8,843</td>
<td align="right">0.8%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">247,190</td>
<td align="right">14.6%</td>
<td align="right">81,624</td>
<td align="right">7.5%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">29,445</td>
<td align="right">1.7%</td>
<td align="right">10,463</td>
<td align="right">1.0%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">13,515</td>
<td align="right">0.8%</td>
<td align="right">5,521</td>
<td align="right">0.5%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">69,206</td>
<td align="right">4.1%</td>
<td align="right">29,872</td>
<td align="right">2.7%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66,614</td>
<td align="right">3.9%</td>
<td align="right">37,274</td>
<td align="right">3.4%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">52,680</td>
<td align="right">3.1%</td>
<td align="right">32,092</td>
<td align="right">2.9%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">15,260</td>
<td align="right">0.9%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">16,346</td>
<td align="right">1.0%</td>
<td align="right">12,504</td>
<td align="right">1.1%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,760</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">777,950</td>
<td align="right">45.9%</td>
<td align="right">781,605</td>
<td align="right">71.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,896</td>
<td align="right">0.1%</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">1,627,909,657</td>
<td align="right">26.3%</td>
<td align="right">416,450,859</td>
<td align="right">25.0%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,566,413,902</td>
<td align="right">73.7%</td>
<td align="right">1,248,873,599</td>
<td align="right">75.0%</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,045,304</td>
<td align="right">0.1%</td>
<td align="right">1,753,474</td>
<td align="right">0.1%</td>
<td align="right">-65.2%</td>
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
<td align="right">468,505</td>
<td align="right">71.5%</td>
<td align="right">148,637</td>
<td align="right">56.8%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,407</td>
<td align="right">28.5%</td>
<td align="right">113,076</td>
<td align="right">43.2%</td>
<td align="right">-39.3%</td>
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
<td align="left">list slice</td>
<td align="right">35,080</td>
<td align="right">7.5%</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">157,600</td>
<td align="right">33.6%</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,779</td>
<td align="right">25.1%</td>
<td align="right">30,974</td>
<td align="right">20.8%</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">57,381</td>
<td align="right">12.2%</td>
<td align="right">30,320</td>
<td align="right">20.4%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">74,080</td>
<td align="right">15.8%</td>
<td align="right">44,020</td>
<td align="right">29.6%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,620</td>
<td align="right">1.2%</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">4.2%</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">11,543,851,068</td>
<td align="right">97.0%</td>
<td align="right">5,364,613,276</td>
<td align="right">94.5%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,300</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">240,462,674</td>
<td align="right">2.0%</td>
<td align="right">196,080,001</td>
<td align="right">3.5%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">351,985,232</td>
<td align="right">3.0%</td>
<td align="right">308,446,538</td>
<td align="right">5.4%</td>
<td align="right">-12.4%</td>
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
<td align="right">5,072,953</td>
<td align="right">98.5%</td>
<td align="right">4,176,888</td>
<td align="right">98.2%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">78,656</td>
<td align="right">1.5%</td>
<td align="right">76,908</td>
<td align="right">1.8%</td>
<td align="right">-2.2%</td>
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
<td align="left">init not python</td>
<td align="right">700</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,960</td>
<td align="right">2.5%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,580</td>
<td align="right">12.2%</td>
<td align="right">8,440</td>
<td align="right">11.0%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">68,596</td>
<td align="right">87.2%</td>
<td align="right">67,988</td>
<td align="right">88.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,000</td>
<td align="right">3.8%</td>
<td align="right">3,000</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,903,365,951</td>
<td align="right">95.8%</td>
<td align="right">1,873,657,559</td>
<td align="right">95.0%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">214,245,699</td>
<td align="right">4.2%</td>
<td align="right">97,708,692</td>
<td align="right">5.0%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,375,843</td>
<td align="right">0.0%</td>
<td align="right">736,183</td>
<td align="right">0.0%</td>
<td align="right">-46.5%</td>
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
<td align="right">193,915</td>
<td align="right">69.9%</td>
<td align="right">130,574</td>
<td align="right">66.5%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">83,544</td>
<td align="right">30.1%</td>
<td align="right">65,665</td>
<td align="right">33.5%</td>
<td align="right">-21.4%</td>
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
<td align="right">9,880</td>
<td align="right">5.1%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,493</td>
<td align="right">1.8%</td>
<td align="right">1,544</td>
<td align="right">1.2%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">51,955</td>
<td align="right">26.8%</td>
<td align="right">25,793</td>
<td align="right">19.8%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27,500</td>
<td align="right">14.2%</td>
<td align="right">18,740</td>
<td align="right">14.4%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,280</td>
<td align="right">1.2%</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">19,106</td>
<td align="right">9.9%</td>
<td align="right">14,363</td>
<td align="right">11.0%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">34,576</td>
<td align="right">17.8%</td>
<td align="right">26,562</td>
<td align="right">20.3%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,723</td>
<td align="right">10.2%</td>
<td align="right">16,384</td>
<td align="right">12.5%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,742</td>
<td align="right">6.6%</td>
<td align="right">11,688</td>
<td align="right">9.0%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,880</td>
<td align="right">5.6%</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">-1.8%</td>
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
<td align="right">2,446,643,876</td>
<td align="right">87.5%</td>
<td align="right">381,852,930</td>
<td align="right">65.8%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">348,959,533</td>
<td align="right">12.5%</td>
<td align="right">198,071,005</td>
<td align="right">34.1%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
<td align="right">0.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">155,514</td>
<td align="right">71.7%</td>
<td align="right">100,208</td>
<td align="right">62.9%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,339</td>
<td align="right">28.3%</td>
<td align="right">59,020</td>
<td align="right">37.1%</td>
<td align="right">-3.8%</td>
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
<td align="right">27,880</td>
<td align="right">17.9%</td>
<td align="right">8,680</td>
<td align="right">8.7%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,023</td>
<td align="right">14.2%</td>
<td align="right">13,569</td>
<td align="right">13.5%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,291</td>
<td align="right">20.1%</td>
<td align="right">22,979</td>
<td align="right">22.9%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">74,320</td>
<td align="right">47.8%</td>
<td align="right">54,980</td>
<td align="right">54.9%</td>
<td align="right">-26.0%</td>
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
<td align="right">173,291,056</td>
<td align="right">4.3%</td>
<td align="right">181,251</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,324,419,483</td>
<td align="right">83.0%</td>
<td align="right">351,708,486</td>
<td align="right">82.6%</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">676,383,282</td>
<td align="right">16.9%</td>
<td align="right">74,128,896</td>
<td align="right">17.4%</td>
<td align="right">-89.0%</td>
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
<td align="right">3,318,499</td>
<td align="right">92.0%</td>
<td align="right">47,787</td>
<td align="right">33.6%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">288,439</td>
<td align="right">8.0%</td>
<td align="right">94,325</td>
<td align="right">66.4%</td>
<td align="right">-67.3%</td>
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
<td align="right">30,100</td>
<td align="right">10.4%</td>
<td align="right">1,980</td>
<td align="right">2.1%</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,740</td>
<td align="right">2.0%</td>
<td align="right">1,300</td>
<td align="right">1.4%</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">41,833</td>
<td align="right">14.5%</td>
<td align="right">9,606</td>
<td align="right">10.2%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">2,280</td>
<td align="right">0.8%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,980</td>
<td align="right">7.6%</td>
<td align="right">6,840</td>
<td align="right">7.3%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">12,240</td>
<td align="right">4.2%</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">107,402</td>
<td align="right">37.2%</td>
<td align="right">36,519</td>
<td align="right">38.7%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">28,144</td>
<td align="right">9.8%</td>
<td align="right">10,200</td>
<td align="right">10.8%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">660</td>
<td align="right">0.2%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">5,980</td>
<td align="right">2.1%</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">14,020</td>
<td align="right">4.9%</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">9,760</td>
<td align="right">3.4%</td>
<td align="right">6,480</td>
<td align="right">6.9%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">8,020</td>
<td align="right">2.8%</td>
<td align="right">5,520</td>
<td align="right">5.9%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">959,540,040</td>
<td align="right">5.3%</td>
<td align="right">248,222,630</td>
<td align="right">2.6%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,829,637,322</td>
<td align="right">15.5%</td>
<td align="right">1,224,985,421</td>
<td align="right">12.6%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,357,593,700</td>
<td align="right">84.3%</td>
<td align="right">8,481,985,718</td>
<td align="right">87.3%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">324,280</td>
<td align="right">0.0%</td>
<td align="right">323,880</td>
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
<td align="right">18,728,578</td>
<td align="right">88.4%</td>
<td align="right">5,222,292</td>
<td align="right">86.8%</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,462,449</td>
<td align="right">11.6%</td>
<td align="right">791,373</td>
<td align="right">13.2%</td>
<td align="right">-67.9%</td>
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
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">715,950</td>
<td align="right">29.1%</td>
<td align="right">45,408</td>
<td align="right">5.7%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">997,108</td>
<td align="right">40.5%</td>
<td align="right">267,030</td>
<td align="right">33.7%</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">114,994</td>
<td align="right">4.7%</td>
<td align="right">54,571</td>
<td align="right">6.9%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">144,761</td>
<td align="right">5.9%</td>
<td align="right">77,764</td>
<td align="right">9.8%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">264,456</td>
<td align="right">10.7%</td>
<td align="right">149,620</td>
<td align="right">18.9%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">19,676</td>
<td align="right">0.8%</td>
<td align="right">13,429</td>
<td align="right">1.7%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">20,540</td>
<td align="right">0.8%</td>
<td align="right">14,380</td>
<td align="right">1.8%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,440</td>
<td align="right">0.1%</td>
<td align="right">2,800</td>
<td align="right">0.4%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">22,260</td>
<td align="right">0.9%</td>
<td align="right">19,740</td>
<td align="right">2.5%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">81,372</td>
<td align="right">3.3%</td>
<td align="right">73,029</td>
<td align="right">9.2%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">28,720</td>
<td align="right">1.2%</td>
<td align="right">26,800</td>
<td align="right">3.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,132</td>
<td align="right">0.2%</td>
<td align="right">5,782</td>
<td align="right">0.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,800</td>
<td align="right">0.5%</td>
<td align="right">11,180</td>
<td align="right">1.4%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">16,620</td>
<td align="right">0.7%</td>
<td align="right">15,840</td>
<td align="right">2.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,460</td>
<td align="right">0.5%</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">10,357,587,414</td>
<td align="right">99.8%</td>
<td align="right">5,172,835,822</td>
<td align="right">99.6%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,520</td>
<td align="right">0.0%</td>
<td align="right">11,500</td>
<td align="right">0.0%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">469,721</td>
<td align="right">0.0%</td>
<td align="right">443,237</td>
<td align="right">0.0%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,361,287</td>
<td align="right">0.2%</td>
<td align="right">20,303,451</td>
<td align="right">0.4%</td>
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
<td align="right">474,247</td>
<td align="right">100.0%</td>
<td align="right">442,726</td>
<td align="right">100.0%</td>
<td align="right">-6.6%</td>
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
<td align="right">8,227</td>
<td align="right">0.0%</td>
<td align="right">8,124</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,736,063</td>
<td align="right">100.0%</td>
<td align="right">83,589,316</td>
<td align="right">100.0%</td>
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
<td align="right">7,960</td>
<td align="right">100.0%</td>
<td align="right">7,880</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">786,195,116</td>
<td align="right">81.9%</td>
<td align="right">786,185,475</td>
<td align="right">81.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,284,412</td>
<td align="right">18.1%</td>
<td align="right">173,284,230</td>
<td align="right">18.1%</td>
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
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">30,660</td>
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
<td align="right">5,480</td>
<td align="right">8.4%</td>
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="left">list</td>
<td align="right">9,980</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">150,707,957</td>
<td align="right">5.1%</td>
<td align="right">68,502,353</td>
<td align="right">3.0%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216,432,819</td>
<td align="right">7.3%</td>
<td align="right">98,647,305</td>
<td align="right">4.3%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,742,461,761</td>
<td align="right">92.6%</td>
<td align="right">2,177,848,374</td>
<td align="right">95.6%</td>
<td align="right">-20.6%</td>
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
<td align="right">2,943,542</td>
<td align="right">96.5%</td>
<td align="right">1,382,981</td>
<td align="right">95.2%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105,470</td>
<td align="right">3.5%</td>
<td align="right">70,006</td>
<td align="right">4.8%</td>
<td align="right">-33.6%</td>
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
<td align="right">34,800</td>
<td align="right">33.0%</td>
<td align="right">10,260</td>
<td align="right">14.7%</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,900</td>
<td align="right">7.5%</td>
<td align="right">4,360</td>
<td align="right">6.2%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,780</td>
<td align="right">6.4%</td>
<td align="right">3,820</td>
<td align="right">5.5%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,680</td>
<td align="right">3.5%</td>
<td align="right">2,940</td>
<td align="right">4.2%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,700</td>
<td align="right">10.1%</td>
<td align="right">8,580</td>
<td align="right">12.3%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">840</td>
<td align="right">0.8%</td>
<td align="right">760</td>
<td align="right">1.1%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,880</td>
<td align="right">13.2%</td>
<td align="right">12,920</td>
<td align="right">18.5%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,120</td>
<td align="right">4.9%</td>
<td align="right">4,800</td>
<td align="right">6.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,920</td>
<td align="right">4.7%</td>
<td align="right">4,720</td>
<td align="right">6.7%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,730</td>
<td align="right">15.9%</td>
<td align="right">16,726</td>
<td align="right">23.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">448,409,490</td>
<td align="right">33.8%</td>
<td align="right">64,684,277</td>
<td align="right">28.4%</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">878,055,414</td>
<td align="right">66.2%</td>
<td align="right">163,411,934</td>
<td align="right">71.6%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">158,740</td>
<td align="right">92.4%</td>
<td align="right">52,582</td>
<td align="right">82.9%</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,123</td>
<td align="right">7.6%</td>
<td align="right">10,882</td>
<td align="right">17.1%</td>
<td align="right">-17.1%</td>
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
<td align="right">9,640</td>
<td align="right">6.1%</td>
<td align="right">900</td>
<td align="right">1.7%</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">66,240</td>
<td align="right">41.7%</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,240</td>
<td align="right">2.0%</td>
<td align="right">800</td>
<td align="right">1.5%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">34,300</td>
<td align="right">21.6%</td>
<td align="right">10,162</td>
<td align="right">19.3%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">43,960</td>
<td align="right">27.7%</td>
<td align="right">33,100</td>
<td align="right">62.9%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,360</td>
<td align="right">0.9%</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">-16.2%</td>
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
<td align="right">141,875,306</td>
<td align="right">2.0%</td>
<td align="right">49,029,668</td>
<td align="right">1.4%</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">548,588,970</td>
<td align="right">7.9%</td>
<td align="right">273,159,467</td>
<td align="right">7.8%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,405,796,766</td>
<td align="right">92.1%</td>
<td align="right">3,216,344,495</td>
<td align="right">92.1%</td>
<td align="right">-49.8%</td>
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
<td align="right">659,867</td>
<td align="right">18.7%</td>
<td align="right">175,143</td>
<td align="right">13.6%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,875,602</td>
<td align="right">81.3%</td>
<td align="right">1,108,053</td>
<td align="right">86.4%</td>
<td align="right">-61.5%</td>
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
<td align="right">174,019</td>
<td align="right">26.4%</td>
<td align="right">4,586</td>
<td align="right">2.6%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">165,138</td>
<td align="right">25.0%</td>
<td align="right">4,725</td>
<td align="right">2.7%</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100,457</td>
<td align="right">15.2%</td>
<td align="right">27,085</td>
<td align="right">15.5%</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">27,640</td>
<td align="right">4.2%</td>
<td align="right">13,460</td>
<td align="right">7.7%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">97,764</td>
<td align="right">14.8%</td>
<td align="right">48,023</td>
<td align="right">27.4%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">28,794</td>
<td align="right">4.4%</td>
<td align="right">14,690</td>
<td align="right">8.4%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">16,561</td>
<td align="right">2.5%</td>
<td align="right">13,381</td>
<td align="right">7.6%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,740</td>
<td align="right">0.3%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,294</td>
<td align="right">7.0%</td>
<td align="right">46,273</td>
<td align="right">26.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,768,034</td>
<td align="right">0.1%</td>
<td align="right">215,373</td>
<td align="right">0.0%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,570,210,564</td>
<td align="right">99.9%</td>
<td align="right">562,205,340</td>
<td align="right">100.0%</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">2,876</td>
<td align="right">8.5%</td>
<td align="right">2,076</td>
<td align="right">7.1%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,828</td>
<td align="right">91.5%</td>
<td align="right">27,088</td>
<td align="right">92.9%</td>
<td align="right">-12.1%</td>
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
<td align="right">2,236</td>
<td align="right">77.7%</td>
<td align="right">1,436</td>
<td align="right">69.2%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">13.2%</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">9.0%</td>
<td align="right">260</td>
<td align="right">12.5%</td>
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
<td align="right">1,803,575,988</td>
<td align="right">0.8%</td>
<td align="right">674,871,752</td>
<td align="right">0.6%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">24,339,024,502</td>
<td align="right">10.5%</td>
<td align="right">9,771,433,057</td>
<td align="right">9.3%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">80,853,699,435</td>
<td align="right">35.0%</td>
<td align="right">37,352,528,351</td>
<td align="right">35.5%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">124,326,804,269</td>
<td align="right">53.7%</td>
<td align="right">57,466,377,223</td>
<td align="right">54.6%</td>
<td align="right">-53.8%</td>
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
<td align="right">676,383,282</td>
<td align="right">7.6%</td>
<td align="right">74,128,896</td>
<td align="right">2.2%</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,627,909,657</td>
<td align="right">18.3%</td>
<td align="right">416,450,859</td>
<td align="right">12.4%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,435,935,558</td>
<td align="right">16.1%</td>
<td align="right">420,374,598</td>
<td align="right">12.5%</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,829,637,322</td>
<td align="right">31.8%</td>
<td align="right">1,224,985,421</td>
<td align="right">36.3%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">216,432,819</td>
<td align="right">2.4%</td>
<td align="right">98,647,305</td>
<td align="right">2.9%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">214,245,699</td>
<td align="right">2.4%</td>
<td align="right">97,708,692</td>
<td align="right">2.9%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">548,588,970</td>
<td align="right">6.2%</td>
<td align="right">273,159,467</td>
<td align="right">8.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">348,959,533</td>
<td align="right">3.9%</td>
<td align="right">198,071,005</td>
<td align="right">5.9%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">351,985,232</td>
<td align="right">4.0%</td>
<td align="right">308,446,538</td>
<td align="right">9.2%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">448,409,490</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">173,284,230</td>
<td align="right">5.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">377,615,581</td>
<td align="right">20.1%</td>
<td align="right">73,029,760</td>
<td align="right">9.7%</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">348,607,228</td>
<td align="right">18.5%</td>
<td align="right">100,617,953</td>
<td align="right">13.4%</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">120,120,683</td>
<td align="right">6.4%</td>
<td align="right">43,286,460</td>
<td align="right">5.8%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">109,957,919</td>
<td align="right">5.8%</td>
<td align="right">40,955,345</td>
<td align="right">5.4%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">115,661,039</td>
<td align="right">6.1%</td>
<td align="right">90,678,454</td>
<td align="right">12.0%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,883,747</td>
<td align="right">4.1%</td>
<td align="right">77,874,115</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,883,747</td>
<td align="right">4.1%</td>
<td align="right">77,874,115</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">86,704,641</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">86,456,355</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">66,957,874</td>
<td align="right">3.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">39,280,727</td>
<td align="right">5.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">27,511,601</td>
<td align="right">3.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,196,593</td>
<td align="right">3.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,297,480</td>
<td align="right">0.1%</td>
<td align="right">2,651,480</td>
<td align="right">0.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">409,172,802</td>
<td align="right">4.8%</td>
<td align="right">527,046,635</td>
<td align="right">6.6%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
<td align="right">22,820</td>
<td align="right">0.0%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">83,830,747</td>
<td align="right">1.0%</td>
<td align="right">71,671,263</td>
<td align="right">0.9%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,315,042,497</td>
<td align="right">73.4%</td>
<td align="right">5,662,615,384</td>
<td align="right">70.4%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,042,211</td>
<td align="right">0.4%</td>
<td align="right">28,603,131</td>
<td align="right">0.4%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,426,560,276</td>
<td align="right">16.6%</td>
<td align="right">1,523,811,555</td>
<td align="right">19.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,820,207,334</td>
<td align="right">79.3%</td>
<td align="right">6,362,606,672</td>
<td align="right">79.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,431,886,516</td>
<td align="right">16.6%</td>
<td align="right">1,526,485,855</td>
<td align="right">19.0%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,288,629,885</td>
<td align="right">26.6%</td>
<td align="right">2,378,481,967</td>
<td align="right">29.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,288,629,885</td>
<td align="right">26.6%</td>
<td align="right">2,378,481,967</td>
<td align="right">29.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">222,078,720</td>
<td align="right">2.6%</td>
<td align="right">225,090,964</td>
<td align="right">2.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">856,743,369</td>
<td align="right">10.0%</td>
<td align="right">851,996,112</td>
<td align="right">10.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,380,932</td>
<td align="right">2.5%</td>
<td align="right">211,380,949</td>
<td align="right">2.6%</td>
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
<td align="right">65,639,130</td>
<td align="right"></td>
<td align="right">20,314,624</td>
<td align="right"></td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">73,876,420</td>
<td align="right"></td>
<td align="right">24,699,898</td>
<td align="right"></td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,220,980</td>
<td align="right"></td>
<td align="right">4,561,144</td>
<td align="right"></td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">114,020</td>
<td align="right">0.1%</td>
<td align="right">63,780</td>
<td align="right">0.0%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,282,002,104</td>
<td align="right"></td>
<td align="right">2,624,316,886</td>
<td align="right"></td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">25,500,464,970</td>
<td align="right">22.5%</td>
<td align="right">22,999,591,876</td>
<td align="right">20.8%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,578,026,250</td>
<td align="right"></td>
<td align="right">10,655,189,172</td>
<td align="right"></td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,077,834,568</td>
<td align="right">61.5%</td>
<td align="right">10,201,251,042</td>
<td align="right">60.8%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">28,307,116,546</td>
<td align="right">21.7%</td>
<td align="right">26,089,789,347</td>
<td align="right">20.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,201,237,745</td>
<td align="right">62.1%</td>
<td align="right">10,324,818,633</td>
<td align="right">61.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,255,422</td>
<td align="right"></td>
<td align="right">150,140,854</td>
<td align="right"></td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,823,920,712</td>
<td align="right"></td>
<td align="right">6,448,647,543</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,822,049,276</td>
<td align="right">37.9%</td>
<td align="right">6,446,879,786</td>
<td align="right">38.4%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,262,568,573</td>
<td align="right"></td>
<td align="right">3,109,599,816</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,210,707</td>
<td align="right">0.1%</td>
<td align="right">19,813,513</td>
<td align="right">0.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">102,234,738,635</td>
<td align="right">78.3%</td>
<td align="right">100,719,243,678</td>
<td align="right">79.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,306,620</td>
<td align="right">2.0%</td>
<td align="right">3,271,220</td>
<td align="right">2.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,192,470</td>
<td align="right">0.6%</td>
<td align="right">103,754,078</td>
<td align="right">0.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">87,787,234,402</td>
<td align="right">77.5%</td>
<td align="right">87,522,071,928</td>
<td align="right">79.2%</td>
<td align="right">-0.3%</td>
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
<td align="right">115,398,680</td>
<td align="right">16,286,709,509</td>
<td align="right">0</td>
<td align="right">18,603,040</td>
<td align="right">14,491,189,999</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,994,492</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,003,949,904</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,084</td>
<td align="right">1,084 / 0 !!</td>
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
<td align="right">1,084</td>
<td align="right">1,084 / 0 !!</td>
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
<td align="right">1,920</td>
<td align="right">1,900</td>
<td align="right">-1.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-26
