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
<td align="left">CALL_KW</td>
<td align="right">150</td>
<td align="right">450</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,552</td>
<td align="right">3,472</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,942</td>
<td align="right">4,282</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,739,713</td>
<td align="right">2,459,211</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">38</td>
<td align="right">58</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">127</td>
<td align="right">63</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">255</td>
<td align="right">127</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,513,911</td>
<td align="right">1,254,438</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,184,729</td>
<td align="right">591,479</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,429</td>
<td align="right">1,213</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">252,133</td>
<td align="right">125,993</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">10,364</td>
<td align="right">5,180</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,574,566</td>
<td align="right">2,286,545</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">75,499</td>
<td align="right">37,739</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,735</td>
<td align="right">2,367</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">133,220</td>
<td align="right">66,596</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">345,930</td>
<td align="right">172,938</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">137,837</td>
<td align="right">68,909</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">24,957</td>
<td align="right">12,477</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">20,094</td>
<td align="right">10,046</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">20,094</td>
<td align="right">10,046</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,350</td>
<td align="right">10,174</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,658,108</td>
<td align="right">1,328,939</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">60,283</td>
<td align="right">30,139</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,753</td>
<td align="right">50,873</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,760,005</td>
<td align="right">1,379,910</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">808,152</td>
<td align="right">404,056</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">350,447</td>
<td align="right">175,215</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">509,929</td>
<td align="right">254,953</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">112,635</td>
<td align="right">56,315</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">478,445</td>
<td align="right">239,213</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">232,440</td>
<td align="right">116,216</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">441,716</td>
<td align="right">220,852</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,175,772</td>
<td align="right">1,087,857</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,157,549</td>
<td align="right">2,078,723</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">144,509</td>
<td align="right">72,253</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,356,549</td>
<td align="right">1,678,242</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,704,586</td>
<td align="right">9,352,120</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">58,879</td>
<td align="right">29,439</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,778,821</td>
<td align="right">7,889,283</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,068,438</td>
<td align="right">8,034,093</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,247,341</td>
<td align="right">623,661</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,289,709</td>
<td align="right">644,845</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">27,838,022</td>
<td align="right">13,918,851</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">972,877</td>
<td align="right">486,434</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,052,749</td>
<td align="right">526,370</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">361,725</td>
<td align="right">180,861</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,203,267</td>
<td align="right">4,601,603</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">7,774,934</td>
<td align="right">3,887,444</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,926,277</td>
<td align="right">1,463,130</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,144,947</td>
<td align="right">1,572,467</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">29,614,342</td>
<td align="right">14,807,110</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,763,310</td>
<td align="right">2,881,646</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,388,028</td>
<td align="right">694,012</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">57,460,580</td>
<td align="right">28,730,211</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">3,849,337</td>
<td align="right">1,924,665</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,327,932</td>
<td align="right">1,163,964</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,455,615</td>
<td align="right">727,807</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">8,023,424</td>
<td align="right">4,011,712</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,445,504</td>
<td align="right">2,722,752</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,297,280</td>
<td align="right">2,648,640</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,811,136</td>
<td align="right">2,405,568</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,220,608</td>
<td align="right">1,610,304</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,025,280</td>
<td align="right">1,512,640</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,700,928</td>
<td align="right">1,350,464</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,686,464</td>
<td align="right">1,343,232</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">2,572,416</td>
<td align="right">1,286,208</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,864,832</td>
<td align="right">932,416</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,528,192</td>
<td align="right">764,096</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,231,616</td>
<td align="right">615,808</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">824,064</td>
<td align="right">412,032</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">824,064</td>
<td align="right">412,032</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">823,424</td>
<td align="right">411,712</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">769,920</td>
<td align="right">384,960</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">254,336</td>
<td align="right">127,168</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">233,088</td>
<td align="right">116,544</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">147,712</td>
<td align="right">73,856</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">106,112</td>
<td align="right">53,056</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">61,184</td>
<td align="right">30,592</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">61,184</td>
<td align="right">30,592</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">61,184</td>
<td align="right">30,592</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">48,512</td>
<td align="right">24,256</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">45,184</td>
<td align="right">22,592</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,336</td>
<td align="right">7,168</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,664</td>
<td align="right">832</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,536</td>
<td align="right">768</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">768</td>
<td align="right">384</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">128</td>
<td align="right">64</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">37,679,169</td>
<td align="right">18,839,616</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,189,469</td>
<td align="right">5,094,748</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,395,352</td>
<td align="right">3,697,687</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">20,641,473</td>
<td align="right">10,320,768</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">35,951,753</td>
<td align="right">17,975,938</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,206,721</td>
<td align="right">5,603,392</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,704,194</td>
<td align="right">10,852,160</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,619,777</td>
<td align="right">4,809,920</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,847,681</td>
<td align="right">3,423,872</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">106,372,945</td>
<td align="right">53,187,008</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,914,114</td>
<td align="right">5,957,120</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,949,122</td>
<td align="right">5,474,624</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,948,743</td>
<td align="right">13,974,592</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,377,985</td>
<td align="right">1,689,024</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,024,780</td>
<td align="right">14,512,706</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">14,636,504</td>
<td align="right">7,318,419</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,472,966</td>
<td align="right">5,236,610</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,219,073</td>
<td align="right">1,109,568</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,024,513</td>
<td align="right">1,012,288</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,860,289</td>
<td align="right">930,176</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,688,834</td>
<td align="right">1,844,480</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,310,401</td>
<td align="right">655,232</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,298,113</td>
<td align="right">649,088</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,405,708</td>
<td align="right">6,703,232</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,023,169</td>
<td align="right">511,616</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">885,049</td>
<td align="right">442,552</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,537,154</td>
<td align="right">768,640</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">697,665</td>
<td align="right">348,864</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">35,801,162</td>
<td align="right">17,902,202</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,335,630</td>
<td align="right">7,668,573</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,426,567</td>
<td align="right">2,213,504</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">254,017</td>
<td align="right">127,040</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">143,784</td>
<td align="right">71,911</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">650,696</td>
<td align="right">325,444</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,196,681</td>
<td align="right">1,598,840</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">312,182</td>
<td align="right">156,145</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">206,841</td>
<td align="right">103,477</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">79,937</td>
<td align="right">40,000</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">155,010</td>
<td align="right">77,568</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">73,790</td>
<td align="right">36,925</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">138,670</td>
<td align="right">69,419</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">45,377</td>
<td align="right">22,720</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,928,109</td>
<td align="right">965,803</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">807,141</td>
<td align="right">404,374</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">211,201</td>
<td align="right">105,827</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">25,537</td>
<td align="right">12,800</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">30,354</td>
<td align="right">15,413</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">62,079</td>
<td align="right">31,543</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">12,052</td>
<td align="right">6,139</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">503,628</td>
<td align="right">257,080</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">156</td>
<td align="right">216</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">192</td>
<td align="right">127</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">169</td>
<td align="right">169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_INDEX</td>
<td align="right"></td>
<td align="right">2,274,747</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right"></td>
<td align="right">137,707</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_RANGE</td>
<td align="right"></td>
<td align="right">63</td>
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
<td align="right">5,137</td>
<td align="right">0.1%</td>
<td align="right">2,538</td>
<td align="right">0.1%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,714,616</td>
<td align="right">98.2%</td>
<td align="right">1,857,275</td>
<td align="right">98.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,509</td>
<td align="right">1.6%</td>
<td align="right">30,845</td>
<td align="right">1.6%</td>
<td align="right">-49.9%</td>
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
<td align="right">166</td>
<td align="right">25.3%</td>
<td align="right">243</td>
<td align="right">32.8%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">489</td>
<td align="right">74.7%</td>
<td align="right">497</td>
<td align="right">67.2%</td>
<td align="right">1.6%</td>
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
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">21</td>
<td align="right">4.2%</td>
<td align="right">950.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">72</td>
<td align="right">14.7%</td>
<td align="right">91</td>
<td align="right">18.3%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">295</td>
<td align="right">60.3%</td>
<td align="right">268</td>
<td align="right">53.9%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">22</td>
<td align="right">4.5%</td>
<td align="right">21</td>
<td align="right">4.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">49</td>
<td align="right">10.0%</td>
<td align="right">48</td>
<td align="right">9.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">49</td>
<td align="right">10.0%</td>
<td align="right">48</td>
<td align="right">9.7%</td>
<td align="right">-2.0%</td>
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
<td align="right">48,512</td>
<td align="right">100.0%</td>
<td align="right">24,256</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">544,812</td>
<td align="right">0.8%</td>
<td align="right">271,885</td>
<td align="right">0.8%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">535,419</td>
<td align="right">0.8%</td>
<td align="right">267,694</td>
<td align="right">0.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,161,954</td>
<td align="right">99.2%</td>
<td align="right">34,080,923</td>
<td align="right">99.2%</td>
<td align="right">-50.0%</td>
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
<td align="right">11,335</td>
<td align="right">100.0%</td>
<td align="right">8,473</td>
<td align="right">100.0%</td>
<td align="right">-25.2%</td>
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
<td align="right">75</td>
<td align="right">50.0%</td>
<td align="right">75</td>
<td align="right">16.7%</td>
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
<td align="right">75</td>
<td align="right">100.0%</td>
<td align="right">375</td>
<td align="right">100.0%</td>
<td align="right">400.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">860,376</td>
<td align="right">51.6%</td>
<td align="right">430,168</td>
<td align="right">51.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">805,672</td>
<td align="right">48.3%</td>
<td align="right">402,856</td>
<td align="right">48.3%</td>
<td align="right">-50.0%</td>
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
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">200</td>
<td align="right">13.2%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,429</td>
<td align="right">97.3%</td>
<td align="right">1,318</td>
<td align="right">86.8%</td>
<td align="right">-7.8%</td>
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
<td align="right">81</td>
<td align="right">5.7%</td>
<td align="right">59</td>
<td align="right">4.5%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">662</td>
<td align="right">46.3%</td>
<td align="right">588</td>
<td align="right">44.6%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">44</td>
<td align="right">3.1%</td>
<td align="right">43</td>
<td align="right">3.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">495</td>
<td align="right">34.6%</td>
<td align="right">484</td>
<td align="right">36.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">46</td>
<td align="right">3.2%</td>
<td align="right">45</td>
<td align="right">3.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">50</td>
<td align="right">3.5%</td>
<td align="right">49</td>
<td align="right">3.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">51</td>
<td align="right">3.6%</td>
<td align="right">50</td>
<td align="right">3.8%</td>
<td align="right">-2.0%</td>
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
<td align="right">27,126</td>
<td align="right">4.0%</td>
<td align="right">13,498</td>
<td align="right">4.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">210,721</td>
<td align="right">31.4%</td>
<td align="right">105,377</td>
<td align="right">31.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">431,848</td>
<td align="right">64.4%</td>
<td align="right">215,972</td>
<td align="right">64.4%</td>
<td align="right">-50.0%</td>
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
<td align="right">544</td>
<td align="right">54.9%</td>
<td align="right">288</td>
<td align="right">40.9%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">447</td>
<td align="right">45.1%</td>
<td align="right">417</td>
<td align="right">59.1%</td>
<td align="right">-6.7%</td>
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
<td align="right">180</td>
<td align="right">40.3%</td>
<td align="right">156</td>
<td align="right">37.4%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">267</td>
<td align="right">59.7%</td>
<td align="right">261</td>
<td align="right">62.6%</td>
<td align="right">-2.2%</td>
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
<td align="right">15,068,522</td>
<td align="right">49.6%</td>
<td align="right">7,534,122</td>
<td align="right">49.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,330,584</td>
<td align="right">50.4%</td>
<td align="right">7,665,367</td>
<td align="right">50.4%</td>
<td align="right">-50.0%</td>
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
<td align="right">4,959</td>
<td align="right">98.3%</td>
<td align="right">3,119</td>
<td align="right">97.3%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">87</td>
<td align="right">1.7%</td>
<td align="right">87</td>
<td align="right">2.7%</td>
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
<td align="left">dict items</td>
<td align="right">3,798</td>
<td align="right">76.6%</td>
<td align="right">2,064</td>
<td align="right">66.2%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">73</td>
<td align="right">1.5%</td>
<td align="right">100</td>
<td align="right">3.2%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">146</td>
<td align="right">2.9%</td>
<td align="right">102</td>
<td align="right">3.3%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">183</td>
<td align="right">3.7%</td>
<td align="right">159</td>
<td align="right">5.1%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">90</td>
<td align="right">1.8%</td>
<td align="right">88</td>
<td align="right">2.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">187</td>
<td align="right">3.8%</td>
<td align="right">183</td>
<td align="right">5.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">285</td>
<td align="right">5.7%</td>
<td align="right">279</td>
<td align="right">8.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">147</td>
<td align="right">3.0%</td>
<td align="right">144</td>
<td align="right">4.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">50</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">2,457,371</td>
<td align="right">99.9%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">391</td>
<td align="right">21.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,449</td>
<td align="right">78.8%</td>
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
<td align="left">list</td>
<td align="right">4,488,320</td>
<td align="right">4,488,320 / 0 !!</td>
<td align="right">61</td>
<td align="right">4.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">33,536</td>
<td align="right">33,536 / 0 !!</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">224,000</td>
<td align="right">224,000 / 0 !!</td>
<td align="right">14</td>
<td align="right">1.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">31,744</td>
<td align="right">31,744 / 0 !!</td>
<td align="right">4</td>
<td align="right">0.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">19,712</td>
<td align="right">19,712 / 0 !!</td>
<td align="right">3</td>
<td align="right">0.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,776</td>
<td align="right">27,776 / 0 !!</td>
<td align="right">7</td>
<td align="right">0.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,897,857</td>
<td align="right">4,897,857 / 0 !!</td>
<td align="right">2,450,098</td>
<td align="right">169,088.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">14,464</td>
<td align="right">14,464 / 0 !!</td>
<td align="right">7,389</td>
<td align="right">509.9%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,304</td>
<td align="right">2,304 / 0 !!</td>
<td align="right">1,243</td>
<td align="right">85.8%</td>
<td align="right">-46.1%</td>
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
<td align="right">8,148,206</td>
<td align="right">16.3%</td>
<td align="right">4,070,982</td>
<td align="right">16.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">352,711</td>
<td align="right">0.7%</td>
<td align="right">176,327</td>
<td align="right">0.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,342,243</td>
<td align="right">82.7%</td>
<td align="right">20,673,823</td>
<td align="right">82.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">497,533</td>
<td align="right">1.0%</td>
<td align="right">249,340</td>
<td align="right">1.0%</td>
<td align="right">-49.9%</td>
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
<td align="right">154,802</td>
<td align="right">97.0%</td>
<td align="right">80,080</td>
<td align="right">95.0%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,832</td>
<td align="right">3.0%</td>
<td align="right">4,237</td>
<td align="right">5.0%</td>
<td align="right">-12.3%</td>
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
<td align="left">class method obj</td>
<td align="right">91</td>
<td align="right">1.9%</td>
<td align="right">68</td>
<td align="right">1.6%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,917</td>
<td align="right">81.1%</td>
<td align="right">3,405</td>
<td align="right">80.4%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">755</td>
<td align="right">15.6%</td>
<td align="right">697</td>
<td align="right">16.5%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">47</td>
<td align="right">1.0%</td>
<td align="right">46</td>
<td align="right">1.1%</td>
<td align="right">-2.1%</td>
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
<td align="right">85,298,390</td>
<td align="right">100.0%</td>
<td align="right">42,648,850</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right">736</td>
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
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
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
<td align="right">820</td>
<td align="right">100.0%</td>
<td align="right">2,740</td>
<td align="right">100.0%</td>
<td align="right">234.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,849,337</td>
<td align="right">100.0%</td>
<td align="right">1,924,665</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">1,937,111</td>
<td align="right">55.5%</td>
<td align="right">967,095</td>
<td align="right">55.4%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,552,658</td>
<td align="right">44.5%</td>
<td align="right">777,743</td>
<td align="right">44.6%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">78</td>
<td align="right">0.0%</td>
<td align="right">78</td>
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
<td align="right">29,573</td>
<td align="right">100.0%</td>
<td align="right">14,878</td>
<td align="right">100.0%</td>
<td align="right">-49.7%</td>
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
<td align="right">1,247,341</td>
<td align="right">100.0%</td>
<td align="right">623,661</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19</td>
<td align="right">0.0%</td>
<td align="right">19</td>
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
<td align="right">19</td>
<td align="right">100.0%</td>
<td align="right">39</td>
<td align="right">100.0%</td>
<td align="right">105.3%</td>
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
<td align="right">2,573,514</td>
<td align="right">5.9%</td>
<td align="right">1,281,859</td>
<td align="right">5.9%</td>
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
<td align="right">38,903,426</td>
<td align="right">89.6%</td>
<td align="right">19,454,904</td>
<td align="right">89.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,926,736</td>
<td align="right">4.4%</td>
<td align="right">964,296</td>
<td align="right">4.4%</td>
<td align="right">-50.0%</td>
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
<td align="right">48,819</td>
<td align="right">98.1%</td>
<td align="right">24,843</td>
<td align="right">97.4%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">938</td>
<td align="right">1.9%</td>
<td align="right">673</td>
<td align="right">2.6%</td>
<td align="right">-28.3%</td>
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
<td align="right">24</td>
<td align="right">2.6%</td>
<td align="right">44</td>
<td align="right">6.5%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26</td>
<td align="right">2.8%</td>
<td align="right">46</td>
<td align="right">6.8%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">266</td>
<td align="right">28.4%</td>
<td align="right">158</td>
<td align="right">23.5%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">347</td>
<td align="right">37.0%</td>
<td align="right">237</td>
<td align="right">35.2%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">275</td>
<td align="right">29.3%</td>
<td align="right">188</td>
<td align="right">27.9%</td>
<td align="right">-31.6%</td>
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
<td align="right">12,517,401</td>
<td align="right">99.9%</td>
<td align="right">6,258,712</td>
<td align="right">99.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,944</td>
<td align="right">0.1%</td>
<td align="right">5,992</td>
<td align="right">0.1%</td>
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
<td align="left">Success</td>
<td align="right">60</td>
<td align="right">55.6%</td>
<td align="right">100</td>
<td align="right">68.0%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48</td>
<td align="right">44.4%</td>
<td align="right">47</td>
<td align="right">32.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">48</td>
<td align="right">100.0%</td>
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">28,651,917</td>
<td align="right">3.8%</td>
<td align="right">11,931,298</td>
<td align="right">3.1%</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">12,851,687</td>
<td align="right">1.7%</td>
<td align="right">6,418,741</td>
<td align="right">1.7%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">388,494,397</td>
<td align="right">50.9%</td>
<td align="right">194,249,550</td>
<td align="right">50.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">332,666,844</td>
<td align="right">43.6%</td>
<td align="right">168,751,076</td>
<td align="right">44.3%</td>
<td align="right">-49.3%</td>
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
<td align="right">535,419</td>
<td align="right">2.8%</td>
<td align="right">267,694</td>
<td align="right">2.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">48,512</td>
<td align="right">0.2%</td>
<td align="right">24,256</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,330,584</td>
<td align="right">78.9%</td>
<td align="right">7,665,367</td>
<td align="right">63.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">805,672</td>
<td align="right">4.1%</td>
<td align="right">402,856</td>
<td align="right">3.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">210,721</td>
<td align="right">1.1%</td>
<td align="right">105,377</td>
<td align="right">0.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,926,736</td>
<td align="right">9.9%</td>
<td align="right">964,296</td>
<td align="right">7.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">497,533</td>
<td align="right">2.6%</td>
<td align="right">249,340</td>
<td align="right">2.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">61,509</td>
<td align="right">0.3%</td>
<td align="right">30,845</td>
<td align="right">0.3%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,944</td>
<td align="right">0.1%</td>
<td align="right">5,992</td>
<td align="right">0.0%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">736</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,457,371</td>
<td align="right">20.2%</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,188</td>
<td align="right">0.3%</td>
<td align="right">18,752</td>
<td align="right">0.3%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">515,144</td>
<td align="right">4.0%</td>
<td align="right">254,048</td>
<td align="right">4.0%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">241,569</td>
<td align="right">1.9%</td>
<td align="right">119,951</td>
<td align="right">1.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">985,009</td>
<td align="right">7.7%</td>
<td align="right">491,362</td>
<td align="right">7.7%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">296,589</td>
<td align="right">2.3%</td>
<td align="right">148,071</td>
<td align="right">2.3%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,218,748</td>
<td align="right">9.5%</td>
<td align="right">608,800</td>
<td align="right">9.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,891,357</td>
<td align="right">45.8%</td>
<td align="right">2,945,140</td>
<td align="right">45.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,802,275</td>
<td align="right">14.0%</td>
<td align="right">900,978</td>
<td align="right">14.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,552,658</td>
<td align="right">12.1%</td>
<td align="right">777,743</td>
<td align="right">12.1%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">211,544</td>
<td align="right">1.6%</td>
<td align="right">105,998</td>
<td align="right">1.7%</td>
<td align="right">-49.9%</td>
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
<td align="right">2,561,231</td>
<td align="right">6.6%</td>
<td align="right">1,279,866</td>
<td align="right">6.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,591,445</td>
<td align="right">9.3%</td>
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,591,445</td>
<td align="right">9.3%</td>
<td align="right">1,795,007</td>
<td align="right">9.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,574,631</td>
<td align="right">11.9%</td>
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,574,631</td>
<td align="right">11.9%</td>
<td align="right">2,286,609</td>
<td align="right">11.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">61,184</td>
<td align="right">0.2%</td>
<td align="right">30,592</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">854,785</td>
<td align="right">2.2%</td>
<td align="right">427,393</td>
<td align="right">2.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">27,948,743</td>
<td align="right">72.5%</td>
<td align="right">13,974,592</td>
<td align="right">72.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">983,186</td>
<td align="right">2.6%</td>
<td align="right">491,602</td>
<td align="right">2.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">33,949,858</td>
<td align="right">88.1%</td>
<td align="right">16,975,857</td>
<td align="right">88.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">67,137</td>
<td align="right">0.2%</td>
<td align="right">33,600</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache hits</td>
<td align="right">9,993,671</td>
<td align="right"></td>
<td align="right">4,988,447</td>
<td align="right"></td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">170,618,210</td>
<td align="right">34.9%</td>
<td align="right">85,184,453</td>
<td align="right">34.9%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">235,298,861</td>
<td align="right">42.7%</td>
<td align="right">117,495,018</td>
<td align="right">42.7%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">26,731,875</td>
<td align="right">36.4%</td>
<td align="right">13,348,418</td>
<td align="right">36.4%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">26,792,291</td>
<td align="right">36.5%</td>
<td align="right">13,378,626</td>
<td align="right">36.5%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">49,356,338</td>
<td align="right"></td>
<td align="right">24,649,513</td>
<td align="right"></td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">13,112,099</td>
<td align="right">2.7%</td>
<td align="right">6,552,017</td>
<td align="right">2.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">7,079,340</td>
<td align="right">1.3%</td>
<td align="right">3,538,646</td>
<td align="right">1.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,600,326</td>
<td align="right"></td>
<td align="right">23,298,699</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">60,288</td>
<td align="right">0.1%</td>
<td align="right">30,144</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">121,472</td>
<td align="right"></td>
<td align="right">60,736</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">186,865,711</td>
<td align="right">38.2%</td>
<td align="right">93,435,790</td>
<td align="right">38.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,604,007</td>
<td align="right">63.5%</td>
<td align="right">23,303,100</td>
<td align="right">63.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">28,991,406</td>
<td align="right"></td>
<td align="right">14,497,741</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">188,359,765</td>
<td align="right">34.2%</td>
<td align="right">94,220,984</td>
<td align="right">34.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">118,340,755</td>
<td align="right">24.2%</td>
<td align="right">59,220,124</td>
<td align="right">24.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">120,105,095</td>
<td align="right">21.8%</td>
<td align="right">60,140,621</td>
<td align="right">21.8%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">528,438</td>
<td align="right"></td>
<td align="right">277,166</td>
<td align="right"></td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">592,025</td>
<td align="right"></td>
<td align="right">337,650</td>
<td align="right"></td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">63,920</td>
<td align="right"></td>
<td align="right">60,838</td>
<td align="right"></td>
<td align="right">-4.8%</td>
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
<td align="right">129</td>
<td align="right">160,180</td>
<td align="right">1,407,820</td>
<td align="right">100,242</td>
<td align="right">188,488</td>
<td align="right">65</td>
<td align="right">92,248</td>
<td align="right">740,065</td>
<td align="right">40,392</td>
<td align="right">104,440</td>
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
Stats gathered on: 2025-06-16
