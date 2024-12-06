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
<td align="right">34,136,988</td>
<td align="right">13,253,272</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">475,689</td>
<td align="right">222,307</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,899,432</td>
<td align="right">935,808</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">212,519</td>
<td align="right">319,907</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,042,921</td>
<td align="right">5,117,906</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">575,946</td>
<td align="right">309,891</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,378,482</td>
<td align="right">8,170,105</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,950,617</td>
<td align="right">5,806,908</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,587,561</td>
<td align="right">3,515,181</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,939,188</td>
<td align="right">11,106,815</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,689,896</td>
<td align="right">2,469,063</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,879,606</td>
<td align="right">1,956,681</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,437,994</td>
<td align="right">13,221,285</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,931,791</td>
<td align="right">2,015,663</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,285,045</td>
<td align="right">1,577,202</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,194,061</td>
<td align="right">7,761,786</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,643,196</td>
<td align="right">6,078,406</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,411,918</td>
<td align="right">1,702,635</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,397,224</td>
<td align="right">3,137,264</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,485,457</td>
<td align="right">14,701,091</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,273,677</td>
<td align="right">6,026,639</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,276,340</td>
<td align="right">2,398,288</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,937,216</td>
<td align="right">2,222,607</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,511,373</td>
<td align="right">1,148,682</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,359,778</td>
<td align="right">1,035,279</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,542,196</td>
<td align="right">40,915,122</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,294,494</td>
<td align="right">13,468,399</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,735,844</td>
<td align="right">107,434,871</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,875,915</td>
<td align="right">41,332,977</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,439,608</td>
<td align="right">17,100,947</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">36,348,131</td>
<td align="right">31,270,724</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">126,071,261</td>
<td align="right">108,590,986</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">117,931,785</td>
<td align="right">102,007,050</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,041,516</td>
<td align="right">8,746,509</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,089,436</td>
<td align="right">35,875,205</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,303,102</td>
<td align="right">14,324,071</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">166,997,878</td>
<td align="right">147,109,966</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,192,771</td>
<td align="right">4,601,566</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">44,401,691</td>
<td align="right">39,379,519</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,193,621</td>
<td align="right">16,221,104</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,850,892</td>
<td align="right">15,044,822</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">118,682,115</td>
<td align="right">106,076,173</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,917,975</td>
<td align="right">8,875,908</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,689,931</td>
<td align="right">4,200,070</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,212,080</td>
<td align="right">12,797,065</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">578,083,160</td>
<td align="right">522,402,484</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,321,330</td>
<td align="right">15,683,165</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,508,344</td>
<td align="right">41,416,301</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,490,100</td>
<td align="right">11,397,020</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,590,467</td>
<td align="right">4,194,932</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">110,170,194</td>
<td align="right">100,793,749</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">130,533,128</td>
<td align="right">119,672,634</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,941,861</td>
<td align="right">11,875,553</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,131,930</td>
<td align="right">21,236,847</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,313,748</td>
<td align="right">1,421,136</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30,252,658</td>
<td align="right">27,925,223</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,092,276</td>
<td align="right">25,955,349</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,960,751</td>
<td align="right">15,707,219</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,245,046</td>
<td align="right">8,578,493</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,669,072</td>
<td align="right">16,467,704</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,780,126</td>
<td align="right">3,526,681</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,433,585</td>
<td align="right">8,840,842</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,069,504</td>
<td align="right">3,825,672</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,840,659</td>
<td align="right">10,204,344</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,408</td>
<td align="right">2,574,638</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">163,080,510</td>
<td align="right">153,996,776</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,209</td>
<td align="right">1,411,862</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,557,886</td>
<td align="right">5,290,223</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">138,866,789</td>
<td align="right">132,244,779</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,491,038</td>
<td align="right">48,179,117</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">85,960,130</td>
<td align="right">82,450,927</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,335,698</td>
<td align="right">1,282,115</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,002,207</td>
<td align="right">131,417,870</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,889,821</td>
<td align="right">71,462,765</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,115,634</td>
<td align="right">36,890,662</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,020,073</td>
<td align="right">1,958,522</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,370,508</td>
<td align="right">4,251,802</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,972,107</td>
<td align="right">9,723,778</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,928,722</td>
<td align="right">57,592,783</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,569,260</td>
<td align="right">5,466,717</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,693,213</td>
<td align="right">1,663,423</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,332</td>
<td align="right">232,252</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,468,896</td>
<td align="right">4,399,405</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">712,407</td>
<td align="right">707,619</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">523,767</td>
<td align="right">526,434</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,498,151</td>
<td align="right">21,430,038</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">862,184</td>
<td align="right">859,643</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,673,028</td>
<td align="right">1,669,451</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,458,211</td>
<td align="right">6,445,737</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,617,765</td>
<td align="right">6,610,611</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,577,115</td>
<td align="right">4,573,035</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">640,661</td>
<td align="right">640,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">767,159</td>
<td align="right">767,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,076,052</td>
<td align="right">155,078,719</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,528,154</td>
<td align="right">39,528,154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">38,864,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,584</td>
<td align="right">22,677,584</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,757</td>
<td align="right">7,308,757</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,833</td>
<td align="right">5,948,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,863</td>
<td align="right">5,682,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,953,051</td>
<td align="right">4,953,051</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,521,083</td>
<td align="right">4,521,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,044,600</td>
<td align="right">3,044,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,717</td>
<td align="right">2,973,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,655</td>
<td align="right">2,941,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,008</td>
<td align="right">2,687,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,480,739</td>
<td align="right">2,480,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,794,144</td>
<td align="right">1,794,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,522,465</td>
<td align="right">1,522,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,522,465</td>
<td align="right">1,522,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,515,800</td>
<td align="right">1,515,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,262</td>
<td align="right">1,477,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,341,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,334,130</td>
<td align="right">1,334,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,588</td>
<td align="right">1,280,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,248,245</td>
<td align="right">1,248,245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,223</td>
<td align="right">1,133,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,638</td>
<td align="right">1,091,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,644</td>
<td align="right">833,644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">743,593</td>
<td align="right">743,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,787</td>
<td align="right">501,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,002</td>
<td align="right">462,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">345,342</td>
<td align="right">345,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,769</td>
<td align="right">296,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,454</td>
<td align="right">266,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">255,554</td>
<td align="right">255,554</td>
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
<td align="right">192,013</td>
<td align="right">192,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,405</td>
<td align="right">158,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">152,946</td>
<td align="right">152,946</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,588</td>
<td align="right">149,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,469</td>
<td align="right">146,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,127</td>
<td align="right">129,127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">117,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">84,308</td>
<td align="right">84,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,875</td>
<td align="right">79,875</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,982</td>
<td align="right">76,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">69,137</td>
<td align="right">69,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,860</td>
<td align="right">35,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,107</td>
<td align="right">32,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,799</td>
<td align="right">28,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,977</td>
<td align="right">25,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">24,145</td>
<td align="right">24,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,613</td>
<td align="right">23,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,212</td>
<td align="right">23,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,953</td>
<td align="right">21,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,479</td>
<td align="right">21,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">16,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">10,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,427</td>
<td align="right">10,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
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
<td align="left">UNARY_INVERT</td>
<td align="right">8,138</td>
<td align="right">8,138</td>
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
<td align="right">3,081</td>
<td align="right">3,081</td>
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
<td align="right">2,091</td>
<td align="right">2,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,344</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">346</td>
<td align="right">346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">302</td>
<td align="right">302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">259</td>
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
<td align="right">115</td>
<td align="right">115</td>
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
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">7</td>
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
<td align="right">9,235,108</td>
<td align="right">46.0%</td>
<td align="right">8,568,707</td>
<td align="right">44.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,829,404</td>
<td align="right">53.9%</td>
<td align="right">10,829,404</td>
<td align="right">55.8%</td>
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
<td align="right">9,349</td>
<td align="right">94.1%</td>
<td align="right">9,197</td>
<td align="right">94.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">589</td>
<td align="right">5.9%</td>
<td align="right">589</td>
<td align="right">6.0%</td>
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
<td align="left">or</td>
<td align="right">1,017</td>
<td align="right">10.9%</td>
<td align="right">868</td>
<td align="right">9.4%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">129</td>
<td align="right">1.4%</td>
<td align="right">126</td>
<td align="right">1.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">36.4%</td>
<td align="right">3,403</td>
<td align="right">37.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,401</td>
<td align="right">25.7%</td>
<td align="right">2,401</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">16.0%</td>
<td align="right">1,492</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.7%</td>
<td align="right">251</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">230</td>
<td align="right">2.5%</td>
<td align="right">230</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.4%</td>
<td align="right">229</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">16</td>
<td align="right">0.2%</td>
<td align="right">16</td>
<td align="right">0.2%</td>
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
<td align="right">2,732,408</td>
<td align="right">100.0%</td>
<td align="right">2,574,638</td>
<td align="right">100.0%</td>
<td align="right">-5.8%</td>
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
<td align="right">3,773,239</td>
<td align="right">9.8%</td>
<td align="right">3,519,857</td>
<td align="right">9.2%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,466,866</td>
<td align="right">84.1%</td>
<td align="right">32,466,866</td>
<td align="right">84.6%</td>
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
<td align="right">2,366,702</td>
<td align="right">6.1%</td>
<td align="right">2,366,702</td>
<td align="right">6.2%</td>
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
<td align="right">5,654</td>
<td align="right">11.0%</td>
<td align="right">5,591</td>
<td align="right">10.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,741</td>
<td align="right">89.0%</td>
<td align="right">45,741</td>
<td align="right">89.1%</td>
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
<td align="left">list slice</td>
<td align="right">865</td>
<td align="right">15.3%</td>
<td align="right">802</td>
<td align="right">14.3%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,655</td>
<td align="right">47.0%</td>
<td align="right">2,655</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,252</td>
<td align="right">22.1%</td>
<td align="right">1,252</td>
<td align="right">22.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.4%</td>
<td align="right">307</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.3%</td>
<td align="right">245</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.2%</td>
<td align="right">238</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">92</td>
<td align="right">1.6%</td>
<td align="right">92</td>
<td align="right">1.6%</td>
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
<td align="right">1,880,305</td>
<td align="right">0.8%</td>
<td align="right">1,877,596</td>
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
<td align="right">239,290,957</td>
<td align="right">99.2%</td>
<td align="right">239,293,591</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44,849</td>
<td align="right">0.0%</td>
<td align="right">44,849</td>
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
<td align="right">61,223</td>
<td align="right">99.8%</td>
<td align="right">61,181</td>
<td align="right">99.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">98</td>
<td align="right">0.2%</td>
<td align="right">98</td>
<td align="right">0.2%</td>
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
<td align="left">init not simple</td>
<td align="right">424</td>
<td align="right">432.7%</td>
<td align="right">424</td>
<td align="right">432.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">98</td>
<td align="right">100.0%</td>
<td align="right">98</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">98</td>
<td align="right">100.0%</td>
<td align="right">98</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24.5%</td>
<td align="right">24</td>
<td align="right">24.5%</td>
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
<td align="right">336</td>
<td align="right">15.6%</td>
<td align="right">336</td>
<td align="right">15.6%</td>
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
<td align="right">636,773</td>
<td align="right">5.5%</td>
<td align="right">636,740</td>
<td align="right">5.5%</td>
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
<td align="right">10,925,791</td>
<td align="right">94.4%</td>
<td align="right">10,925,791</td>
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
<td align="right">8,049</td>
<td align="right">0.1%</td>
<td align="right">8,049</td>
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
<td align="right">2,668</td>
<td align="right">66.4%</td>
<td align="right">2,665</td>
<td align="right">66.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,351</td>
<td align="right">33.6%</td>
<td align="right">1,351</td>
<td align="right">33.6%</td>
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
<td align="left">big int</td>
<td align="right">104</td>
<td align="right">3.9%</td>
<td align="right">101</td>
<td align="right">3.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,804</td>
<td align="right">67.6%</td>
<td align="right">1,804</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">258</td>
<td align="right">9.7%</td>
<td align="right">258</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">256</td>
<td align="right">9.6%</td>
<td align="right">256</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">23</td>
<td align="right">0.9%</td>
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
<tr>
<td align="left">float long</td>
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
<td align="right">4,364,963</td>
<td align="right">27.1%</td>
<td align="right">4,246,299</td>
<td align="right">26.6%</td>
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
<td align="right">11,731,432</td>
<td align="right">72.9%</td>
<td align="right">11,731,432</td>
<td align="right">73.4%</td>
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
<td align="right">5,017</td>
<td align="right">90.5%</td>
<td align="right">4,975</td>
<td align="right">90.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">528</td>
<td align="right">9.5%</td>
<td align="right">528</td>
<td align="right">9.6%</td>
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
<td align="right">1,490</td>
<td align="right">29.7%</td>
<td align="right">1,469</td>
<td align="right">29.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,172</td>
<td align="right">43.3%</td>
<td align="right">2,151</td>
<td align="right">43.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">733</td>
<td align="right">14.6%</td>
<td align="right">733</td>
<td align="right">14.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">622</td>
<td align="right">12.4%</td>
<td align="right">622</td>
<td align="right">12.5%</td>
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
<td align="right">9,944,436</td>
<td align="right">9.4%</td>
<td align="right">5,801,741</td>
<td align="right">6.5%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,649,797</td>
<td align="right">4.4%</td>
<td align="right">3,249,710</td>
<td align="right">3.6%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">91,697,076</td>
<td align="right">86.3%</td>
<td align="right">80,309,386</td>
<td align="right">89.9%</td>
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
<td align="right">88,373</td>
<td align="right">94.1%</td>
<td align="right">61,959</td>
<td align="right">93.2%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,545</td>
<td align="right">5.9%</td>
<td align="right">4,531</td>
<td align="right">6.8%</td>
<td align="right">-18.3%</td>
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
<td align="left">ascii string</td>
<td align="right">234</td>
<td align="right">4.2%</td>
<td align="right">128</td>
<td align="right">2.8%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">465</td>
<td align="right">8.4%</td>
<td align="right">316</td>
<td align="right">7.0%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">710</td>
<td align="right">12.8%</td>
<td align="right">540</td>
<td align="right">11.9%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,250</td>
<td align="right">22.5%</td>
<td align="right">977</td>
<td align="right">21.6%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,589</td>
<td align="right">28.7%</td>
<td align="right">1,315</td>
<td align="right">29.0%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.3%</td>
<td align="right">309</td>
<td align="right">6.8%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.5%</td>
<td align="right">469</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">272</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.7%</td>
<td align="right">97</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.1%</td>
<td align="right">61</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">47</td>
<td align="right">0.8%</td>
<td align="right">47</td>
<td align="right">1.0%</td>
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
<td align="right">98,697,635</td>
<td align="right">29.0%</td>
<td align="right">79,771,197</td>
<td align="right">25.0%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,675,076</td>
<td align="right">12.0%</td>
<td align="right">35,517,721</td>
<td align="right">11.1%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">200,254,277</td>
<td align="right">58.9%</td>
<td align="right">203,711,232</td>
<td align="right">63.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,389</td>
<td align="right">0.0%</td>
<td align="right">64,389</td>
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
<td align="right">2,263,844</td>
<td align="right">99.5%</td>
<td align="right">1,850,440</td>
<td align="right">99.4%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">10,878</td>
<td align="right">0.5%</td>
<td align="right">10,288</td>
<td align="right">0.6%</td>
<td align="right">-5.4%</td>
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
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">3.0%</td>
<td align="right">239</td>
<td align="right">2.3%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">636</td>
<td align="right">5.8%</td>
<td align="right">572</td>
<td align="right">5.6%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,294</td>
<td align="right">11.9%</td>
<td align="right">1,168</td>
<td align="right">11.4%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,856</td>
<td align="right">26.3%</td>
<td align="right">2,625</td>
<td align="right">25.5%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,203</td>
<td align="right">29.4%</td>
<td align="right">3,118</td>
<td align="right">30.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">9.1%</td>
<td align="right">993</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">5.9%</td>
<td align="right">645</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">1.1%</td>
<td align="right">115</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">71</td>
<td align="right">0.7%</td>
<td align="right">71</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">68</td>
<td align="right">0.6%</td>
<td align="right">68</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
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
<tr>
<td align="left">expected error</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">209,879,887</td>
<td align="right">100.0%</td>
<td align="right">202,868,494</td>
<td align="right">100.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,001</td>
<td align="right">0.0%</td>
<td align="right">3,001</td>
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
<td align="right">57</td>
<td align="right">0.0%</td>
<td align="right">57</td>
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
<td align="right">12,141</td>
<td align="right">0.0%</td>
<td align="right">12,141</td>
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
<td align="right">19,379</td>
<td align="right">100.0%</td>
<td align="right">19,379</td>
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
<td align="right">424,859</td>
<td align="right">99.9%</td>
<td align="right">424,859</td>
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
<td align="right">10,026,603</td>
<td align="right">29.7%</td>
<td align="right">8,731,911</td>
<td align="right">26.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,618,952</td>
<td align="right">28.5%</td>
<td align="right">9,616,191</td>
<td align="right">29.7%</td>
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
<td align="right">14,054,616</td>
<td align="right">41.7%</td>
<td align="right">14,057,315</td>
<td align="right">43.4%</td>
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
<td align="right">9,764</td>
<td align="right">5.0%</td>
<td align="right">9,449</td>
<td align="right">4.8%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,156</td>
<td align="right">95.0%</td>
<td align="right">186,094</td>
<td align="right">95.2%</td>
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
<td align="right">5,037</td>
<td align="right">51.6%</td>
<td align="right">4,722</td>
<td align="right">50.0%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.9%</td>
<td align="right">2,626</td>
<td align="right">27.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">989</td>
<td align="right">10.1%</td>
<td align="right">989</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.6%</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.2%</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">53</td>
<td align="right">0.5%</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">9</td>
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
<tr>
<td align="left">not managed dict</td>
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
<td align="right">1,486,261</td>
<td align="right">14.0%</td>
<td align="right">1,407,935</td>
<td align="right">13.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,354</td>
<td align="right">86.0%</td>
<td align="right">9,156,354</td>
<td align="right">86.6%</td>
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
<td align="right">3,474</td>
<td align="right">88.0%</td>
<td align="right">3,453</td>
<td align="right">87.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">474</td>
<td align="right">12.1%</td>
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
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">320</td>
<td align="right">9.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,960</td>
<td align="right">85.2%</td>
<td align="right">2,960</td>
<td align="right">85.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">13</td>
<td align="right">0.4%</td>
<td align="right">13</td>
<td align="right">0.4%</td>
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
<td align="right">5,385,126</td>
<td align="right">2.9%</td>
<td align="right">3,759,744</td>
<td align="right">2.0%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,061,827</td>
<td align="right">7.5%</td>
<td align="right">12,699,206</td>
<td align="right">6.8%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,734,020</td>
<td align="right">89.6%</td>
<td align="right">169,177,143</td>
<td align="right">91.1%</td>
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
<td align="right">146,262</td>
<td align="right">58.1%</td>
<td align="right">93,889</td>
<td align="right">55.6%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105,535</td>
<td align="right">41.9%</td>
<td align="right">74,864</td>
<td align="right">44.4%</td>
<td align="right">-29.1%</td>
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
<td align="left">number</td>
<td align="right">132,890</td>
<td align="right">90.9%</td>
<td align="right">80,517</td>
<td align="right">85.8%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,949</td>
<td align="right">6.8%</td>
<td align="right">9,949</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">2,081</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">905</td>
<td align="right">0.6%</td>
<td align="right">905</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">214</td>
<td align="right">0.1%</td>
<td align="right">214</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">116</td>
<td align="right">0.1%</td>
<td align="right">116</td>
<td align="right">0.1%</td>
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
<td align="right">296,270</td>
<td align="right">2.0%</td>
<td align="right">296,270</td>
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
<td align="right">14,605,532</td>
<td align="right">98.0%</td>
<td align="right">14,605,532</td>
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
<td align="right">402</td>
<td align="right">80.6%</td>
<td align="right">402</td>
<td align="right">80.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">19.4%</td>
<td align="right">97</td>
<td align="right">19.4%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">122,622,077</td>
<td align="right">3.6%</td>
<td align="right">100,663,851</td>
<td align="right">3.3%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">98,143,597</td>
<td align="right">2.9%</td>
<td align="right">84,800,778</td>
<td align="right">2.8%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,256,284,316</td>
<td align="right">37.2%</td>
<td align="right">1,142,720,588</td>
<td align="right">37.1%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,903,834,775</td>
<td align="right">56.3%</td>
<td align="right">1,750,866,038</td>
<td align="right">56.9%</td>
<td align="right">-8.0%</td>
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
<td align="right">9,944,436</td>
<td align="right">10.2%</td>
<td align="right">5,801,741</td>
<td align="right">6.9%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,026,603</td>
<td align="right">10.3%</td>
<td align="right">8,731,911</td>
<td align="right">10.4%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40,675,076</td>
<td align="right">41.7%</td>
<td align="right">35,517,721</td>
<td align="right">42.2%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,061,827</td>
<td align="right">14.4%</td>
<td align="right">12,699,206</td>
<td align="right">15.1%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,235,108</td>
<td align="right">9.5%</td>
<td align="right">8,568,707</td>
<td align="right">10.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,773,239</td>
<td align="right">3.9%</td>
<td align="right">3,519,857</td>
<td align="right">4.2%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,408</td>
<td align="right">2.8%</td>
<td align="right">2,574,638</td>
<td align="right">3.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,261</td>
<td align="right">1.5%</td>
<td align="right">1,407,935</td>
<td align="right">1.7%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,364,963</td>
<td align="right">4.5%</td>
<td align="right">4,246,299</td>
<td align="right">5.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">636,773</td>
<td align="right">0.7%</td>
<td align="right">636,740</td>
<td align="right">0.8%</td>
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
<td align="right">4,391,585</td>
<td align="right">3.6%</td>
<td align="right">2,842,310</td>
<td align="right">2.8%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,324,675</td>
<td align="right">1.9%</td>
<td align="right">1,624,569</td>
<td align="right">1.6%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,325,122</td>
<td align="right">1.9%</td>
<td align="right">1,625,141</td>
<td align="right">1.6%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,728,060</td>
<td align="right">38.9%</td>
<td align="right">37,166,326</td>
<td align="right">36.9%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">17,911,766</td>
<td align="right">14.6%</td>
<td align="right">14,394,770</td>
<td align="right">14.3%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,240,033</td>
<td align="right">11.6%</td>
<td align="right">11,649,092</td>
<td align="right">11.6%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,358,421</td>
<td align="right">8.4%</td>
<td align="right">9,112,617</td>
<td align="right">9.1%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,862</td>
<td align="right">6.3%</td>
<td align="right">6,813,477</td>
<td align="right">6.8%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,563,981</td>
<td align="right">7.8%</td>
<td align="right">9,561,220</td>
<td align="right">9.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,342,043</td>
<td align="right">1.9%</td>
<td align="right">2,342,043</td>
<td align="right">2.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">630,294</td>
<td align="right">0.3%</td>
<td align="right">737,682</td>
<td align="right">0.3%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,557,641</td>
<td align="right">8.5%</td>
<td align="right">17,335,336</td>
<td align="right">7.9%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,693,553</td>
<td align="right">3.1%</td>
<td align="right">6,905,647</td>
<td align="right">3.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,650,024</td>
<td align="right">18.1%</td>
<td align="right">38,425,052</td>
<td align="right">17.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,651,747</td>
<td align="right">18.1%</td>
<td align="right">38,426,775</td>
<td align="right">17.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,282,041</td>
<td align="right">18.4%</td>
<td align="right">39,164,457</td>
<td align="right">17.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,282,041</td>
<td align="right">18.4%</td>
<td align="right">39,164,457</td>
<td align="right">17.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,884,048</td>
<td align="right">81.6%</td>
<td align="right">180,109,020</td>
<td align="right">82.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,029,757</td>
<td align="right">72.1%</td>
<td align="right">158,032,424</td>
<td align="right">72.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">379</td>
<td align="right">0.0%</td>
<td align="right">379</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,484,681</td>
<td align="right">4.8%</td>
<td align="right">10,484,681</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,497</td>
<td align="right">0.2%</td>
<td align="right">502,497</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">88</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">1,126,853,294</td>
<td align="right">27.1%</td>
<td align="right">1,329,168,947</td>
<td align="right">31.0%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,268,826,075</td>
<td align="right">33.7%</td>
<td align="right">1,470,709,995</td>
<td align="right">37.8%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">391,196,817</td>
<td align="right">10.4%</td>
<td align="right">354,094,917</td>
<td align="right">9.1%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,672,125</td>
<td align="right"></td>
<td align="right">1,523,560</td>
<td align="right"></td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">706,548,250</td>
<td align="right">17.0%</td>
<td align="right">765,142,750</td>
<td align="right">17.8%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546,550,688</td>
<td align="right">13.2%</td>
<td align="right">505,211,770</td>
<td align="right">11.8%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">11,116,359</td>
<td align="right"></td>
<td align="right">10,387,507</td>
<td align="right"></td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,446,236</td>
<td align="right"></td>
<td align="right">8,866,156</td>
<td align="right"></td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,378,793,968</td>
<td align="right">36.6%</td>
<td align="right">1,298,103,989</td>
<td align="right">33.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,773,301,927</td>
<td align="right">42.7%</td>
<td align="right">1,692,718,954</td>
<td align="right">39.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">731,568,880</td>
<td align="right">19.4%</td>
<td align="right">763,068,992</td>
<td align="right">19.6%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">211,400,009</td>
<td align="right"></td>
<td align="right">206,366,201</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">211,905,818</td>
<td align="right"></td>
<td align="right">212,372,192</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,426,222</td>
<td align="right">0.5%</td>
<td align="right">1,423,449</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">199,035,921</td>
<td align="right">70.0%</td>
<td align="right">199,415,059</td>
<td align="right">70.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">200,523,992</td>
<td align="right">70.5%</td>
<td align="right">200,900,357</td>
<td align="right">70.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">156,092,031</td>
<td align="right"></td>
<td align="right">155,824,057</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,824,193</td>
<td align="right"></td>
<td align="right">83,875,035</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,815,439</td>
<td align="right">29.5%</td>
<td align="right">83,862,561</td>
<td align="right">29.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,849</td>
<td align="right">0.0%</td>
<td align="right">61,849</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,690</td>
<td align="right"></td>
<td align="right">3,079,690</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">997,148</td>
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
<td align="right">6,302</td>
<td align="right">13,383,975</td>
<td align="right">281,875,688</td>
<td align="right">18,924,729</td>
<td align="right">24,398,246</td>
<td align="right">6,280</td>
<td align="right">13,441,871</td>
<td align="right">282,759,583</td>
<td align="right">19,011,922</td>
<td align="right">24,546,689</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">22</td>
<td align="right">0.1%</td>
<td align="right">64</td>
<td align="right">0.3%</td>
<td align="right">190.9%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,036,880,783</td>
<td align="right">878.4%</td>
<td align="right">3,012,380,943</td>
<td align="right">886.7%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">231,889,939</td>
<td align="right"></td>
<td align="right">339,716,274</td>
<td align="right"></td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,927</td>
<td align="right">38.7%</td>
<td align="right">6,474</td>
<td align="right">25.4%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">15,723</td>
<td align="right">61.3%</td>
<td align="right">19,050</td>
<td align="right">74.6%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,255</td>
<td align="right">63.4%</td>
<td align="right">19,463</td>
<td align="right">76.3%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,650</td>
<td align="right"></td>
<td align="right">25,524</td>
<td align="right"></td>
<td align="right">-0.5%</td>
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
<td align="right">9,885</td>
<td align="right">99.6%</td>
<td align="right">6,261</td>
<td align="right">96.7%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">9,927</td>
<td align="right"></td>
<td align="right">6,474</td>
<td align="right"></td>
<td align="right">-34.8%</td>
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
<td align="right">450</td>
<td align="right">4.5%</td>
<td align="right">533</td>
<td align="right">8.2%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,071</td>
<td align="right">20.9%</td>
<td align="right">1,581</td>
<td align="right">24.4%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,861</td>
<td align="right">49.0%</td>
<td align="right">2,678</td>
<td align="right">41.4%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,272</td>
<td align="right">22.9%</td>
<td align="right">1,448</td>
<td align="right">22.4%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">273</td>
<td align="right">2.8%</td>
<td align="right">234</td>
<td align="right">3.6%</td>
<td align="right">-14.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.6%</td>
<td align="right">42 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,028</td>
<td align="right">20.4%</td>
<td align="right">1,240</td>
<td align="right">19.2%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,544</td>
<td align="right">15.6%</td>
<td align="right">1,564</td>
<td align="right">24.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,443</td>
<td align="right">54.8%</td>
<td align="right">2,673</td>
<td align="right">41.3%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">744</td>
<td align="right">7.5%</td>
<td align="right">721</td>
<td align="right">11.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">126</td>
<td align="right">1.3%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">-83.3%</td>
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
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">42</td>
<td align="right">102,585</td>
<td align="right">244,150.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,213</td>
<td align="right">630,680</td>
<td align="right">28,398.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">248</td>
<td align="right">61,799</td>
<td align="right">24,819.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">248</td>
<td align="right">61,799</td>
<td align="right">24,819.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">7,938</td>
<td align="right">1,074,246</td>
<td align="right">13,433.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,715</td>
<td align="right">672,083</td>
<td align="right">11,660.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">36</td>
<td align="right">4,116</td>
<td align="right">11,333.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">36</td>
<td align="right">4,116</td>
<td align="right">11,333.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">32,411</td>
<td align="right">2,733,123</td>
<td align="right">8,332.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,932</td>
<td align="right">121,485</td>
<td align="right">6,188.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,426</td>
<td align="right">936,554</td>
<td align="right">4,485.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">153,953</td>
<td align="right">2,400,991</td>
<td align="right">1,459.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">575,087</td>
<td align="right">7,624,307</td>
<td align="right">1,225.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">102,057</td>
<td align="right">1,303,425</td>
<td align="right">1,177.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">57,285</td>
<td align="right">675,302</td>
<td align="right">1,078.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">186,188</td>
<td align="right">2,165,219</td>
<td align="right">1,062.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">163,298</td>
<td align="right">1,741,082</td>
<td align="right">966.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60,053</td>
<td align="right">384,552</td>
<td align="right">540.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">246,304</td>
<td align="right">1,506,264</td>
<td align="right">511.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">246,304</td>
<td align="right">1,506,264</td>
<td align="right">511.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">988,342</td>
<td align="right">5,913,357</td>
<td align="right">498.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,531,473</td>
<td align="right">11,724,246</td>
<td align="right">363.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,536,228</td>
<td align="right">11,736,185</td>
<td align="right">362.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,188,414</td>
<td align="right">5,348,355</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,961,016</td>
<td align="right">8,583,026</td>
<td align="right">337.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,074,613</td>
<td align="right">4,583,816</td>
<td align="right">326.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,588,511</td>
<td align="right">6,767,324</td>
<td align="right">326.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,820,054</td>
<td align="right">11,715,708</td>
<td align="right">315.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,011,730</td>
<td align="right">8,073,451</td>
<td align="right">301.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">646,597</td>
<td align="right">2,541,680</td>
<td align="right">293.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">424,610</td>
<td align="right">1,645,443</td>
<td align="right">287.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">54,977</td>
<td align="right">212,747</td>
<td align="right">287.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">216,989</td>
<td align="right">809,732</td>
<td align="right">273.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,630,713</td>
<td align="right">9,767,620</td>
<td align="right">271.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">220,794</td>
<td align="right">802,829</td>
<td align="right">263.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,353,786</td>
<td align="right">44,781,705</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,002,045</td>
<td align="right">3,567,756</td>
<td align="right">256.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">968,347</td>
<td align="right">3,401,612</td>
<td align="right">251.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">718,801</td>
<td align="right">2,524,871</td>
<td align="right">251.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">657,934</td>
<td align="right">2,296,099</td>
<td align="right">249.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">657,934</td>
<td align="right">2,296,099</td>
<td align="right">249.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">997,822</td>
<td align="right">3,436,174</td>
<td align="right">244.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">25,643</td>
<td align="right">84,892</td>
<td align="right">231.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,768,479</td>
<td align="right">9,029,880</td>
<td align="right">226.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,706,622</td>
<td align="right">11,933,738</td>
<td align="right">222.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">179,416</td>
<td align="right">574,951</td>
<td align="right">220.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">124,223</td>
<td align="right">390,278</td>
<td align="right">214.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">339,429</td>
<td align="right">1,054,038</td>
<td align="right">210.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">119,867</td>
<td align="right">368,196</td>
<td align="right">207.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">123,257</td>
<td align="right">376,639</td>
<td align="right">205.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">124,286</td>
<td align="right">377,668</td>
<td align="right">203.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">140,198</td>
<td align="right">407,861</td>
<td align="right">190.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">140,058</td>
<td align="right">403,737</td>
<td align="right">188.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,255,213</td>
<td align="right">3,433,427</td>
<td align="right">173.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">827,160</td>
<td align="right">2,216,543</td>
<td align="right">168.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,593,585</td>
<td align="right">32,481,480</td>
<td align="right">157.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,216,238</td>
<td align="right">5,629,455</td>
<td align="right">154.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">631,549</td>
<td align="right">1,595,173</td>
<td align="right">152.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">283,410</td>
<td align="right">689,085</td>
<td align="right">143.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,671,885</td>
<td align="right">13,734,852</td>
<td align="right">142.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">650,160</td>
<td align="right">1,573,085</td>
<td align="right">142.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,600,988</td>
<td align="right">8,677,247</td>
<td align="right">141.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,855,681</td>
<td align="right">9,201,384</td>
<td align="right">138.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">322,605</td>
<td align="right">763,437</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">317,433</td>
<td align="right">746,922</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,122,612</td>
<td align="right">2,588,681</td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">717,926</td>
<td align="right">1,651,814</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">263,521</td>
<td align="right">598,598</td>
<td align="right">127.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">470,940</td>
<td align="right">1,062,145</td>
<td align="right">125.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">194,323</td>
<td align="right">438,155</td>
<td align="right">125.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">399,356</td>
<td align="right">889,217</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,093,362</td>
<td align="right">4,510,160</td>
<td align="right">115.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,668,166</td>
<td align="right">10,025,242</td>
<td align="right">114.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">317,045</td>
<td align="right">678,680</td>
<td align="right">114.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,651,251</td>
<td align="right">7,793,946</td>
<td align="right">113.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">319,786</td>
<td align="right">682,477</td>
<td align="right">113.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">319,786</td>
<td align="right">682,477</td>
<td align="right">113.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,348,156</td>
<td align="right">4,912,946</td>
<td align="right">109.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">78,293,471</td>
<td align="right">163,203,314</td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">110,350</td>
<td align="right">229,014</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,826,104</td>
<td align="right">5,636,345</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,094,520</td>
<td align="right">4,166,900</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">54,901</td>
<td align="right">108,255</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,554,087</td>
<td align="right">4,911,740</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,155,959</td>
<td align="right">2,198,026</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,830,719</td>
<td align="right">8,974,337</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,023,437</td>
<td align="right">9,310,632</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,326,069</td>
<td align="right">9,570,669</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,320,589</td>
<td align="right">9,476,871</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">944,489</td>
<td align="right">1,653,772</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,194,334</td>
<td align="right">1,881,739</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">327,957</td>
<td align="right">503,524</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">178,210,511</td>
<td align="right">273,113,559</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">236,558,105</td>
<td align="right">349,741,516</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,165,605</td>
<td align="right">6,151,854</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">231,889,939</td>
<td align="right">339,716,274</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">45,089,376</td>
<td align="right">65,461,796</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,689</td>
<td align="right">258,015</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">122,045,845</td>
<td align="right">174,374,347</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">70,964,902</td>
<td align="right">100,096,103</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">173,372,101</td>
<td align="right">243,689,137</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">34,884,288</td>
<td align="right">46,294,794</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">21,840,286</td>
<td align="right">28,648,213</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">35,326,548</td>
<td align="right">46,283,765</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">50,262,617</td>
<td align="right">65,331,455</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">16,317</td>
<td align="right">21,105</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">21,307,552</td>
<td align="right">27,502,618</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">63,573,019</td>
<td align="right">81,705,779</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">33,768,165</td>
<td align="right">43,144,618</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">15,510,680</td>
<td align="right">19,602,723</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">49,513,684</td>
<td align="right">60,450,722</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">49,513,684</td>
<td align="right">60,450,722</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">34,002,756</td>
<td align="right">40,783,701</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">95,467</td>
<td align="right">107,941</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">35,773,115</td>
<td align="right">40,202,544</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,441,240</td>
<td align="right">60,644,846</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">33,535,658</td>
<td align="right">37,245,121</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">69,983,448</td>
<td align="right">76,918,443</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">32,262,834</td>
<td align="right">34,671,776</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,570,264</td>
<td align="right">35,882,290</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">129,682</td>
<td align="right">136,836</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">68,540</td>
<td align="right">72,117</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">33,349,470</td>
<td align="right">35,079,461</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">33,486,307</td>
<td align="right">35,120,962</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">30,986,742</td>
<td align="right">32,322,681</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">20,958</td>
<td align="right">20,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,205</td>
<td align="right">6,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,205</td>
<td align="right">6,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,699</td>
<td align="right">3,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,699</td>
<td align="right">3,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">3,699</td>
<td align="right">3,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,565</td>
<td align="right">3,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">139</td>
<td align="right">139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">5,832,373</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">1,294,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">1,230,579</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">87,738</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">69,491</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">68,051</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">68,051</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">37,632</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">10,290</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">2,499</td>
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
<td align="right">191</td>
<td align="right">170</td>
<td align="right">-11.0%</td>
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
<td align="right">23</td>
<td align="right">23</td>
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
<td align="right">24</td>
<td align="right">24</td>
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
Stats gathered on: 2024-12-06
