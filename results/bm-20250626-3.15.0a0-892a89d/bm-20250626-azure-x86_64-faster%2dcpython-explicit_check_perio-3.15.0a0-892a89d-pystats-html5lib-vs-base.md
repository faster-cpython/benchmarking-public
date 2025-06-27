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
<td align="left">STORE_SUBSCR</td>
<td align="right">124,277</td>
<td align="right">2,609,817</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,028</td>
<td align="right">21,588</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">12,243</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">6,846</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">219</td>
<td align="right">4,599</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">1,008</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44</td>
<td align="right">924</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">861</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">861</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">861</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">39</td>
<td align="right">819</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">756</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">693</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">672</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">651</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">630</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">420</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">336</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">210</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right">189</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">168</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">21</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127,279</td>
<td align="right">2,633,548</td>
<td align="right">1,969.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">419</td>
<td align="right">7,498</td>
<td align="right">1,689.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">574</td>
<td align="right">9,953</td>
<td align="right">1,634.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,134</td>
<td align="right">18,231</td>
<td align="right">1,507.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,608</td>
<td align="right">59,879</td>
<td align="right">1,199.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,636</td>
<td align="right">40,768</td>
<td align="right">1,021.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">462</td>
<td align="right">1,000.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">1,219</td>
<td align="right">915.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">110</td>
<td align="right">1,009</td>
<td align="right">817.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">109</td>
<td align="right">988</td>
<td align="right">806.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">167</td>
<td align="right">965</td>
<td align="right">477.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">141</td>
<td align="right">419</td>
<td align="right">197.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">281</td>
<td align="right">817</td>
<td align="right">190.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">140</td>
<td align="right">398</td>
<td align="right">184.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,400</td>
<td align="right">14,262</td>
<td align="right">164.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,589</td>
<td align="right">9,277</td>
<td align="right">158.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,736</td>
<td align="right">11,814</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">393</td>
<td align="right">627</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">131</td>
<td align="right">209</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">130</td>
<td align="right">188</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">130</td>
<td align="right">188</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">130</td>
<td align="right">188</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">42</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,951,810</td>
<td align="right">11,430,798</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">10,118,874</td>
<td align="right">12,505,805</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,974</td>
<td align="right">9,850</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,623,226</td>
<td align="right">13,988,328</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,026</td>
<td align="right">1,210</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">252</td>
<td align="right">208</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,091</td>
<td align="right">1,274</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">146</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">702,437</td>
<td align="right">781,406</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">12,269</td>
<td align="right">13,617</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10,988</td>
<td align="right">12,136</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,938</td>
<td align="right">3,232</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">380,977</td>
<td align="right">403,458</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">44,158,866</td>
<td align="right">46,174,464</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,766,363</td>
<td align="right">1,832,240</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,747</td>
<td align="right">34,958</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,390</td>
<td align="right">9,082</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">419,088</td>
<td align="right">432,584</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,308</td>
<td align="right">11,938</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,904</td>
<td align="right">1,854</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">744,420</td>
<td align="right">763,361</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">742,113</td>
<td align="right">760,670</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,190</td>
<td align="right">4,104</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,330,851</td>
<td align="right">2,292,003</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,188,075</td>
<td align="right">6,089,805</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,763,640</td>
<td align="right">2,719,978</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,098,168</td>
<td align="right">1,080,854</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">707,644</td>
<td align="right">696,500</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">127</td>
<td align="right">125</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,686,755</td>
<td align="right">1,660,252</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,898,273</td>
<td align="right">3,837,043</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,098,046</td>
<td align="right">1,080,834</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">707,648</td>
<td align="right">696,584</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">353,824</td>
<td align="right">348,292</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">396,370</td>
<td align="right">390,188</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,186,109</td>
<td align="right">3,136,654</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,101,357</td>
<td align="right">1,084,273</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">1,243,025</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,618,852</td>
<td align="right">1,594,259</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,550,531</td>
<td align="right">7,437,130</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,510,539</td>
<td align="right">3,457,897</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,706,969</td>
<td align="right">16,457,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,208,075</td>
<td align="right">1,190,071</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">604,166</td>
<td align="right">595,192</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">6,043,323</td>
<td align="right">5,953,797</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,811,018</td>
<td align="right">14,592,205</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,277,234</td>
<td align="right">2,243,854</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,899,615</td>
<td align="right">15,666,561</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">711,495</td>
<td align="right">701,111</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,689,564</td>
<td align="right">1,714,157</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">87,766,122</td>
<td align="right">86,490,182</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,205,747</td>
<td align="right">2,173,773</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">504,098</td>
<td align="right">496,860</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,421,115</td>
<td align="right">3,372,103</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,466,186</td>
<td align="right">10,317,196</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,602,937</td>
<td align="right">1,580,276</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,839,243</td>
<td align="right">13,643,940</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,887,951</td>
<td align="right">6,791,769</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">355,952</td>
<td align="right">351,007</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,949,490</td>
<td align="right">2,908,966</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">97,673</td>
<td align="right">96,335</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">711,477</td>
<td align="right">721,069</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,850,364</td>
<td align="right">1,825,767</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,232</td>
<td align="right">6,314</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,471,992</td>
<td align="right">10,336,582</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">358,257</td>
<td align="right">353,697</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,718,981</td>
<td align="right">1,697,295</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">355,444</td>
<td align="right">350,968</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,260,711</td>
<td align="right">12,106,621</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,872,047</td>
<td align="right">23,576,953</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,943,635</td>
<td align="right">2,908,027</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">355,985</td>
<td align="right">351,700</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,129,647</td>
<td align="right">22,851,329</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,733,290</td>
<td align="right">1,754,112</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,174,015</td>
<td align="right">1,187,872</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">141,125</td>
<td align="right">139,463</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">735,096</td>
<td align="right">726,462</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">55,986,726</td>
<td align="right">55,329,302</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,630,484</td>
<td align="right">6,554,089</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,825</td>
<td align="right">13,418,503</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">168,206,839</td>
<td align="right">166,358,863</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,166,653</td>
<td align="right">1,179,405</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,576,214</td>
<td align="right">1,559,358</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">51,849,291</td>
<td align="right">51,297,415</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,794,478</td>
<td align="right">1,775,746</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,210,200</td>
<td align="right">8,136,029</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,119,641</td>
<td align="right">6,065,650</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,508,859</td>
<td align="right">11,413,866</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,142,870</td>
<td align="right">1,134,162</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,131,483</td>
<td align="right">5,093,319</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,936,161</td>
<td align="right">3,906,919</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,411,412</td>
<td align="right">2,393,856</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,215,086</td>
<td align="right">14,112,642</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,710,568</td>
<td align="right">6,662,415</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,678,703</td>
<td align="right">12,590,366</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,470,562</td>
<td align="right">5,433,450</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,392,073</td>
<td align="right">2,376,540</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">357,245</td>
<td align="right">355,222</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,795,143</td>
<td align="right">1,785,928</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,618,575</td>
<td align="right">5,595,545</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">963,586</td>
<td align="right">966,946</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">405,899</td>
<td align="right">404,731</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,684,378</td>
<td align="right">1,689,137</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,895,624</td>
<td align="right">6,876,642</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">399,392</td>
<td align="right">398,566</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">910,607</td>
<td align="right">912,383</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">15,491,842</td>
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
<td align="right">1,834</td>
<td align="right">0.0%</td>
<td align="right">33,430</td>
<td align="right">0.1%</td>
<td align="right">1,722.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,116,705</td>
<td align="right">16.1%</td>
<td align="right">6,053,485</td>
<td align="right">16.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,764,789</td>
<td align="right">83.8%</td>
<td align="right">31,458,849</td>
<td align="right">83.8%</td>
<td align="right">-1.0%</td>
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
<td align="right">305</td>
<td align="right">10.3%</td>
<td align="right">4,704</td>
<td align="right">36.8%</td>
<td align="right">1,442.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,660</td>
<td align="right">89.7%</td>
<td align="right">8,070</td>
<td align="right">63.2%</td>
<td align="right">203.4%</td>
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
<td align="left">subscr string slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">126</td>
<td align="right">1.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">84</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">84</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">2.0%</td>
<td align="right">252</td>
<td align="right">3.1%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">175</td>
<td align="right">6.6%</td>
<td align="right">714</td>
<td align="right">8.8%</td>
<td align="right">308.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48</td>
<td align="right">1.8%</td>
<td align="right">168</td>
<td align="right">2.1%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">334</td>
<td align="right">12.6%</td>
<td align="right">1,089</td>
<td align="right">13.5%</td>
<td align="right">226.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,727</td>
<td align="right">64.9%</td>
<td align="right">4,967</td>
<td align="right">61.5%</td>
<td align="right">187.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">63</td>
<td align="right">0.8%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">44</td>
<td align="right">1.7%</td>
<td align="right">84</td>
<td align="right">1.0%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">242</td>
<td align="right">9.1%</td>
<td align="right">418</td>
<td align="right">5.2%</td>
<td align="right">72.7%</td>
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
<td align="right">1,243,025</td>
<td align="right">100.0%</td>
<td align="right">1.5%</td>
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
<td align="right">5,785,418</td>
<td align="right">16.5%</td>
<td align="right">5,697,710</td>
<td align="right">16.4%</td>
<td align="right">-1.5%</td>
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
<td align="right">5,600,754</td>
<td align="right">16.1%</td>
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
<td align="right">29,308,565</td>
<td align="right">83.5%</td>
<td align="right">29,057,160</td>
<td align="right">83.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5,697,710</td>
<td align="right">16.4%</td>
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
<td align="left">Success</td>
<td align="right">109,788</td>
<td align="right">100.0%</td>
<td align="right">115,187</td>
<td align="right">100.0%</td>
<td align="right">4.9%</td>
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
<td align="right">210</td>
<td align="right">50.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">210</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">15,359</td>
<td align="right">0.1%</td>
<td align="right">1.7%</td>
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
<td align="right">25,990,754</td>
<td align="right">91.5%</td>
<td align="right">-1.2%</td>
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
<td align="right">2,387,482</td>
<td align="right">8.4%</td>
<td align="right">-0.9%</td>
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
<td align="right">422</td>
<td align="right">21.7%</td>
<td align="right">2,937</td>
<td align="right">44.2%</td>
<td align="right">596.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,525</td>
<td align="right">78.3%</td>
<td align="right">3,707</td>
<td align="right">55.8%</td>
<td align="right">143.1%</td>
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
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">126</td>
<td align="right">3.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">175</td>
<td align="right">11.5%</td>
<td align="right">734</td>
<td align="right">19.8%</td>
<td align="right">319.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.0%</td>
<td align="right">251</td>
<td align="right">6.8%</td>
<td align="right">172.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">675</td>
<td align="right">44.3%</td>
<td align="right">1,486</td>
<td align="right">40.1%</td>
<td align="right">120.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">13.1%</td>
<td align="right">398</td>
<td align="right">10.7%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">376</td>
<td align="right">24.7%</td>
<td align="right">691</td>
<td align="right">18.6%</td>
<td align="right">83.8%</td>
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
<td align="right">6,674,866</td>
<td align="right">88.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">908,967</td>
<td align="right">12.0%</td>
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
<td align="right">46</td>
<td align="right">5.3%</td>
<td align="right">966</td>
<td align="right">28.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">818</td>
<td align="right">94.7%</td>
<td align="right">2,450</td>
<td align="right">71.7%</td>
<td align="right">199.5%</td>
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
<td align="right">3</td>
<td align="right">0.4%</td>
<td align="right">63</td>
<td align="right">2.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">268</td>
<td align="right">32.8%</td>
<td align="right">985</td>
<td align="right">40.2%</td>
<td align="right">267.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.6%</td>
<td align="right">1,234</td>
<td align="right">50.4%</td>
<td align="right">157.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">8.3%</td>
<td align="right">168</td>
<td align="right">6.9%</td>
<td align="right">147.1%</td>
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
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">966</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,397,454</td>
<td align="right">56.4%</td>
<td align="right">4,907,103</td>
<td align="right">72.9%</td>
<td align="right">104.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,849,731</td>
<td align="right">43.5%</td>
<td align="right">1,823,904</td>
<td align="right">27.1%</td>
<td align="right">-1.4%</td>
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
<td align="right">18</td>
<td align="right">2.8%</td>
<td align="right">378</td>
<td align="right">20.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">615</td>
<td align="right">97.2%</td>
<td align="right">1,485</td>
<td align="right">79.7%</td>
<td align="right">141.5%</td>
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
<td align="right">8</td>
<td align="right">1.3%</td>
<td align="right">168</td>
<td align="right">11.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">23</td>
<td align="right">3.7%</td>
<td align="right">63</td>
<td align="right">4.2%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">205</td>
<td align="right">33.3%</td>
<td align="right">501</td>
<td align="right">33.7%</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">378</td>
<td align="right">61.5%</td>
<td align="right">732</td>
<td align="right">49.3%</td>
<td align="right">93.7%</td>
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
<td align="left">dict keys</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">273</td>
<td align="right">273 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,989</td>
<td align="right">1,989 / 0 !!</td>
<td align="right">3,639</td>
<td align="right">3,639 / 0 !!</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">228,102</td>
<td align="right">228,102 / 0 !!</td>
<td align="right">238,721</td>
<td align="right">238,721 / 0 !!</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">598,170</td>
<td align="right">598,170 / 0 !!</td>
<td align="right">588,750</td>
<td align="right">588,750 / 0 !!</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">966,864</td>
<td align="right">966,864 / 0 !!</td>
<td align="right">954,440</td>
<td align="right">954,440 / 0 !!</td>
<td align="right">-1.3%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">26,654</td>
<td align="right">0.0%</td>
<td align="right">40.5%</td>
</tr>
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
<td align="right">117,550,594</td>
<td align="right">95.8%</td>
<td align="right">-1.5%</td>
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
<td align="right">5,068,964</td>
<td align="right">4.1%</td>
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
<td align="left">Success</td>
<td align="right">1,191</td>
<td align="right">24.9%</td>
<td align="right">15,767</td>
<td align="right">64.8%</td>
<td align="right">1,223.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,589</td>
<td align="right">75.1%</td>
<td align="right">8,567</td>
<td align="right">35.2%</td>
<td align="right">138.7%</td>
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
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">1,403</td>
<td align="right">16.4%</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">184</td>
<td align="right">5.1%</td>
<td align="right">482</td>
<td align="right">5.6%</td>
<td align="right">162.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,392</td>
<td align="right">66.6%</td>
<td align="right">5,363</td>
<td align="right">62.6%</td>
<td align="right">124.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">267</td>
<td align="right">7.4%</td>
<td align="right">545</td>
<td align="right">6.4%</td>
<td align="right">104.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">90.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">245</td>
<td align="right">0.0%</td>
<td align="right">5,145</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">1,125</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">20,773,932</td>
<td align="right">99.9%</td>
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
<td align="left">Success</td>
<td align="right">329</td>
<td align="right">100.0%</td>
<td align="right">4,808</td>
<td align="right">100.0%</td>
<td align="right">1,361.4%</td>
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
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">63</td>
<td align="right">12.1%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">396</td>
<td align="right">75.9%</td>
<td align="right">3.7%</td>
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
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">14,599</td>
<td align="right">0.1%</td>
<td align="right">20,195</td>
<td align="right">0.1%</td>
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
<td align="right">1,141,953</td>
<td align="right">7.8%</td>
<td align="right">1,128,433</td>
<td align="right">7.7%</td>
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
<td align="right">13,569,534</td>
<td align="right">92.1%</td>
<td align="right">13,410,246</td>
<td align="right">92.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">429</td>
<td align="right">36.6%</td>
<td align="right">3,969</td>
<td align="right">65.9%</td>
<td align="right">825.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">742</td>
<td align="right">63.4%</td>
<td align="right">2,054</td>
<td align="right">34.1%</td>
<td align="right">176.8%</td>
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
<td align="right">314</td>
<td align="right">42.3%</td>
<td align="right">1,091</td>
<td align="right">53.1%</td>
<td align="right">247.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">226</td>
<td align="right">30.5%</td>
<td align="right">544</td>
<td align="right">26.5%</td>
<td align="right">140.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">377</td>
<td align="right">18.4%</td>
<td align="right">109.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">22</td>
<td align="right">3.0%</td>
<td align="right">42</td>
<td align="right">2.0%</td>
<td align="right">90.9%</td>
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
<td align="right">124,218</td>
<td align="right">4.0%</td>
<td align="right">2,608,578</td>
<td align="right">47.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">2,944,965</td>
<td align="right">53.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">39.0%</td>
<td align="right">483</td>
<td align="right">39.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36</td>
<td align="right">61.0%</td>
<td align="right">756</td>
<td align="right">61.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">35</td>
<td align="right">97.2%</td>
<td align="right">735</td>
<td align="right">97.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">2.8%</td>
<td align="right">21</td>
<td align="right">2.8%</td>
<td align="right">2,000.0%</td>
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
<td align="right">52,508</td>
<td align="right">0.2%</td>
<td align="right">54,245</td>
<td align="right">0.2%</td>
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
<td align="right">7,548,323</td>
<td align="right">25.9%</td>
<td align="right">7,432,254</td>
<td align="right">25.9%</td>
<td align="right">-1.5%</td>
</tr>
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
<td align="right">21,225,027</td>
<td align="right">73.9%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,080</td>
<td align="right">33.9%</td>
<td align="right">2,804</td>
<td align="right">47.7%</td>
<td align="right">159.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,102</td>
<td align="right">66.1%</td>
<td align="right">3,070</td>
<td align="right">52.3%</td>
<td align="right">46.1%</td>
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
<td align="right">25</td>
<td align="right">1.2%</td>
<td align="right">105</td>
<td align="right">3.4%</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">70</td>
<td align="right">3.3%</td>
<td align="right">210</td>
<td align="right">6.8%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">230</td>
<td align="right">10.9%</td>
<td align="right">606</td>
<td align="right">19.7%</td>
<td align="right">163.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">158</td>
<td align="right">7.5%</td>
<td align="right">356</td>
<td align="right">11.6%</td>
<td align="right">125.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,619</td>
<td align="right">77.0%</td>
<td align="right">1,793</td>
<td align="right">58.4%</td>
<td align="right">10.7%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">765,467</td>
<td align="right">99.9%</td>
<td align="right">2.6%</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">645.2%</td>
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
<td align="right">28,262,379</td>
<td align="right">3.6%</td>
<td align="right">30,530,229</td>
<td align="right">3.8%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">446,059,317</td>
<td align="right">56.4%</td>
<td align="right">464,555,496</td>
<td align="right">57.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,889,813</td>
<td align="right">0.7%</td>
<td align="right">5,849,746</td>
<td align="right">0.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">310,805,193</td>
<td align="right">39.3%</td>
<td align="right">312,065,487</td>
<td align="right">38.4%</td>
<td align="right">0.4%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">124,218</td>
<td align="right">0.4%</td>
<td align="right">2,608,578</td>
<td align="right">7.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,548,323</td>
<td align="right">23.5%</td>
<td align="right">7,432,254</td>
<td align="right">21.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">3.8%</td>
<td align="right">1,243,025</td>
<td align="right">3.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,849,731</td>
<td align="right">5.8%</td>
<td align="right">1,823,904</td>
<td align="right">5.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,676,764</td>
<td align="right">17.7%</td>
<td align="right">5,600,754</td>
<td align="right">16.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,141,953</td>
<td align="right">3.6%</td>
<td align="right">1,128,433</td>
<td align="right">3.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,126,681</td>
<td align="right">16.0%</td>
<td align="right">5,068,964</td>
<td align="right">14.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,116,705</td>
<td align="right">19.0%</td>
<td align="right">6,053,485</td>
<td align="right">17.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,409,740</td>
<td align="right">7.5%</td>
<td align="right">2,387,482</td>
<td align="right">7.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">909,743</td>
<td align="right">2.8%</td>
<td align="right">908,967</td>
<td align="right">2.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">12,886</td>
<td align="right">0.2%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,240</td>
<td align="right">0.4%</td>
<td align="right">28,369</td>
<td align="right">0.5%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,252</td>
<td align="right">0.2%</td>
<td align="right">10,916</td>
<td align="right">0.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,096</td>
<td align="right">0.3%</td>
<td align="right">15,359</td>
<td align="right">0.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,388</td>
<td align="right">4.6%</td>
<td align="right">269,042</td>
<td align="right">4.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,751,557</td>
<td align="right">46.7%</td>
<td align="right">2,709,157</td>
<td align="right">46.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,749,362</td>
<td align="right">46.7%</td>
<td align="right">2,708,174</td>
<td align="right">46.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,764</td>
<td align="right">0.4%</td>
<td align="right">25,460</td>
<td align="right">0.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,272</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,333</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">33,010</td>
<td align="right">0.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">9,279</td>
<td align="right">0.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">672</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">1,596</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">258</td>
<td align="right">0.0%</td>
<td align="right">334</td>
<td align="right">0.0%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,733</td>
<td align="right">0.1%</td>
<td align="right">17,063</td>
<td align="right">0.1%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">355,271</td>
<td align="right">1.5%</td>
<td align="right">350,717</td>
<td align="right">1.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,472,923</td>
<td align="right">98.3%</td>
<td align="right">23,182,774</td>
<td align="right">98.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,129,664</td>
<td align="right">96.9%</td>
<td align="right">22,851,686</td>
<td align="right">96.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">399,431</td>
<td align="right">1.7%</td>
<td align="right">398,084</td>
<td align="right">1.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">399,465</td>
<td align="right">1.7%</td>
<td align="right">398,798</td>
<td align="right">1.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">398,987</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">398,987</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">509</td>
<td align="right"></td>
<td align="right">2,713</td>
<td align="right"></td>
<td align="right">433.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">21,103,705</td>
<td align="right">65.4%</td>
<td align="right">23,464,296</td>
<td align="right">67.8%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,100,179</td>
<td align="right"></td>
<td align="right">23,457,751</td>
<td align="right"></td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,547,367</td>
<td align="right">13.9%</td>
<td align="right">50,953,902</td>
<td align="right">14.5%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">92,332</td>
<td align="right"></td>
<td align="right">96,486</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">91,930</td>
<td align="right"></td>
<td align="right">96,035</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,915</td>
<td align="right">0.0%</td>
<td align="right">9,275</td>
<td align="right">0.0%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">61,357,647</td>
<td align="right">18.4%</td>
<td align="right">63,439,208</td>
<td align="right">19.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">879,748</td>
<td align="right"></td>
<td align="right">901,480</td>
<td align="right"></td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">194,485,556</td>
<td align="right">58.3%</td>
<td align="right">192,111,243</td>
<td align="right">57.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">368,537</td>
<td align="right"></td>
<td align="right">364,935</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">66,633,285</td>
<td align="right">19.1%</td>
<td align="right">66,025,889</td>
<td align="right">18.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">73,514,921</td>
<td align="right">22.0%</td>
<td align="right">72,927,053</td>
<td align="right">21.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,066,936</td>
<td align="right"></td>
<td align="right">7,018,693</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">219,959</td>
<td align="right">0.7%</td>
<td align="right">218,937</td>
<td align="right">0.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,266,630</td>
<td align="right">1.3%</td>
<td align="right">4,253,661</td>
<td align="right">1.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,761,648</td>
<td align="right"></td>
<td align="right">9,776,375</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">3,547,447</td>
<td align="right">1.0%</td>
<td align="right">3,542,401</td>
<td align="right">1.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">230,480,789</td>
<td align="right">66.0%</td>
<td align="right">230,209,030</td>
<td align="right">65.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,151,088</td>
<td align="right">34.6%</td>
<td align="right">11,146,459</td>
<td align="right">32.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,922,214</td>
<td align="right">33.9%</td>
<td align="right">10,918,247</td>
<td align="right">31.5%</td>
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
<td align="right">1,038</td>
<td align="right">296,250</td>
<td align="right">19,533,931</td>
<td align="right">1,239,936</td>
<td align="right">1,778,011</td>
<td align="right">1,021</td>
<td align="right">297,150</td>
<td align="right">20,678,227</td>
<td align="right">1,812,656</td>
<td align="right">1,421,256</td>
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
Stats gathered on: 2025-06-27
