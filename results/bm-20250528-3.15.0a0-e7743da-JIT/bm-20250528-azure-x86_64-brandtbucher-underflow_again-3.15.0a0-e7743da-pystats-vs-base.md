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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">5,694,716</td>
<td align="right">1,386,916</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">23,304,832</td>
<td align="right">6,571,732</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,030,372</td>
<td align="right">3,650,078</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">29,331,002</td>
<td align="right">12,381,142</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">50,776,628</td>
<td align="right">22,079,990</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,324,677</td>
<td align="right">6,697,497</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">53,588,827</td>
<td align="right">28,140,712</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">9,526,061</td>
<td align="right">5,187,345</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,851,191</td>
<td align="right">1,580,701</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">486,224,020</td>
<td align="right">339,879,534</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,375,236</td>
<td align="right">23,343,157</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">153,671,508</td>
<td align="right">108,143,960</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,065,889</td>
<td align="right">12,400,977</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,065,909</td>
<td align="right">12,400,998</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">6,495</td>
<td align="right">8,235</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,904,293</td>
<td align="right">12,426,102</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">51,635,298</td>
<td align="right">40,045,663</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,285,044</td>
<td align="right">4,128,400</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">365,751,045</td>
<td align="right">286,701,314</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">16,597,327</td>
<td align="right">13,046,455</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">98,083,062</td>
<td align="right">77,725,694</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">796,008,458</td>
<td align="right">633,696,293</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,948,398</td>
<td align="right">3,541,968</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">145,138,451</td>
<td align="right">117,606,737</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">31,319,438</td>
<td align="right">25,509,100</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">175,186,557</td>
<td align="right">143,078,346</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">119,084,811</td>
<td align="right">99,619,812</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">44,929,453</td>
<td align="right">37,613,505</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">62,750,871</td>
<td align="right">53,058,406</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">27,766,519</td>
<td align="right">23,507,987</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,085,654</td>
<td align="right">933,214</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">156,744,095</td>
<td align="right">135,704,518</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">492,604,214</td>
<td align="right">427,210,416</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,447,761</td>
<td align="right">10,818,995</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">220,887,142</td>
<td align="right">192,052,600</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">494,044,205</td>
<td align="right">429,916,785</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">274,808,044</td>
<td align="right">239,265,448</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">202,055,534</td>
<td align="right">176,881,743</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,804,540</td>
<td align="right">83,998,811</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">810,624,515</td>
<td align="right">713,794,458</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">185,756,907</td>
<td align="right">163,618,573</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">156,853,674</td>
<td align="right">138,416,775</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">325,509,564</td>
<td align="right">287,308,198</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">741,626,136</td>
<td align="right">658,402,413</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">374,072,664</td>
<td align="right">332,485,831</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">361,058,648</td>
<td align="right">321,118,402</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">423,211,359</td>
<td align="right">376,756,889</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,220,702</td>
<td align="right">1,983,737</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">237,304,302</td>
<td align="right">213,901,893</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">396,237,821</td>
<td align="right">357,240,917</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">110,010,413</td>
<td align="right">99,313,226</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">135,630,819</td>
<td align="right">122,621,113</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">633,380,698</td>
<td align="right">574,380,371</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,601,641,805</td>
<td align="right">3,267,359,990</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">185,419,090</td>
<td align="right">168,878,032</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,560,534</td>
<td align="right">15,998,303</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,965,533,560</td>
<td align="right">2,706,016,232</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">62,985,590</td>
<td align="right">57,475,553</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,926,884</td>
<td align="right">9,079,233</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,304,343</td>
<td align="right">26,814,447</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,323,135</td>
<td align="right">92,769,094</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,333,806,012</td>
<td align="right">1,226,165,784</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">50,620,623</td>
<td align="right">46,585,798</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">476,157,520</td>
<td align="right">439,573,558</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">188,551,916</td>
<td align="right">174,232,543</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">996,982,352</td>
<td align="right">921,707,433</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">975,868,561</td>
<td align="right">903,278,170</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,802,479,723</td>
<td align="right">13,701,956,120</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">317,789,656</td>
<td align="right">294,627,672</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">56,449,811</td>
<td align="right">60,561,873</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">66,528,405</td>
<td align="right">61,702,008</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">75,094,302</td>
<td align="right">69,774,988</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,353,714,151</td>
<td align="right">2,191,225,132</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,386</td>
<td align="right">1,176,076</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,400,079,144</td>
<td align="right">3,181,127,531</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">178,449,429</td>
<td align="right">167,000,975</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">75,612,871</td>
<td align="right">70,832,846</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">615,203,630</td>
<td align="right">577,067,821</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,861,662,562</td>
<td align="right">1,746,900,328</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">109,438,121</td>
<td align="right">102,814,357</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">350,491,346</td>
<td align="right">329,981,305</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">742,745,694</td>
<td align="right">700,739,193</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,409,247,022</td>
<td align="right">4,167,617,093</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,838,749,365</td>
<td align="right">1,738,567,356</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">38,751,194</td>
<td align="right">36,655,464</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">266,156,566</td>
<td align="right">251,883,233</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">357,703,146</td>
<td align="right">338,585,085</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,973,066</td>
<td align="right">32,193,336</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,764,347,339</td>
<td align="right">3,568,853,412</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,847,800,800</td>
<td align="right">1,752,846,048</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">604,032,675</td>
<td align="right">572,994,270</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,950,630</td>
<td align="right">185,891,959</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">109,066,769</td>
<td align="right">103,479,344</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">736,111,721</td>
<td align="right">699,051,974</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,993,331,525</td>
<td align="right">3,795,612,412</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">346,964,049</td>
<td align="right">330,041,284</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">133,549,177</td>
<td align="right">127,333,765</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,921,243,677</td>
<td align="right">1,833,723,813</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,356</td>
<td align="right">1,296</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,241,535</td>
<td align="right">3,108,117</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">348,373,683</td>
<td align="right">334,292,211</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">66,380,047</td>
<td align="right">63,779,441</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,668,296,807</td>
<td align="right">4,488,601,337</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">31,971</td>
<td align="right">30,755</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">102,933,608</td>
<td align="right">99,052,626</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">846,151,136</td>
<td align="right">814,598,889</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">164,452,987</td>
<td align="right">158,358,628</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">867,731,089</td>
<td align="right">836,805,129</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">68,498,826</td>
<td align="right">66,058,026</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">148,375,149</td>
<td align="right">143,116,530</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">187,184,693</td>
<td align="right">180,615,290</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">146,094,435</td>
<td align="right">141,013,959</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">166,191,032</td>
<td align="right">160,513,786</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">984,390,505</td>
<td align="right">953,743,815</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">421,435,873</td>
<td align="right">408,333,511</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,319,969</td>
<td align="right">42,025,753</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,522,077</td>
<td align="right">454,996,240</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">179,170,442</td>
<td align="right">174,128,873</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">113,727,890</td>
<td align="right">110,682,483</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">443,170,229</td>
<td align="right">432,794,044</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,426</td>
<td align="right">3,346</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">129,431,922</td>
<td align="right">126,423,113</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,153</td>
<td align="right">12,871</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">503,864,244</td>
<td align="right">493,143,234</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,443,064</td>
<td align="right">13,193,694</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">596,356,056</td>
<td align="right">585,748,016</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,545,875</td>
<td align="right">5,448,715</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,310,331,619</td>
<td align="right">2,271,304,681</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">262,727,380</td>
<td align="right">258,309,910</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,472,065,523</td>
<td align="right">1,449,286,059</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">252,365</td>
<td align="right">248,626</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">118,262,816</td>
<td align="right">116,762,967</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">66,884,069</td>
<td align="right">66,070,411</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">219,584,203</td>
<td align="right">216,992,346</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">91,262,042</td>
<td align="right">90,190,070</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">164,932,386</td>
<td align="right">163,263,880</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,466,393</td>
<td align="right">4,422,326</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">287,808,666</td>
<td align="right">290,644,288</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">128,955,681</td>
<td align="right">127,808,369</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">166,602,714</td>
<td align="right">165,372,801</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">192,680,214</td>
<td align="right">191,267,873</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">276,267</td>
<td align="right">274,327</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">3,844</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,212,331</td>
<td align="right">50,977,059</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">53,803,093</td>
<td align="right">53,560,753</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">94,059,746</td>
<td align="right">93,645,722</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">163,586,585</td>
<td align="right">162,879,159</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,268</td>
<td align="right">57,028</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,185</td>
<td align="right">115,129,700</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,315,267</td>
<td align="right">64,121,776</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,110,729,248</td>
<td align="right">1,107,853,971</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,630,172</td>
<td align="right">57,749,851</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,164,522</td>
<td align="right">417,317,979</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,365,793</td>
<td align="right">70,229,315</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,089,900</td>
<td align="right">5,081,228</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,690,033</td>
<td align="right">76,596,523</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,961,273</td>
<td align="right">27,930,884</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">239,386,399</td>
<td align="right">239,590,521</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,753,233</td>
<td align="right">123,659,561</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">821,805,815</td>
<td align="right">822,374,411</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,456</td>
<td align="right">5,459</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">266,546,444</td>
<td align="right">266,434,229</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">733,591,995</td>
<td align="right">733,326,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">441,342</td>
<td align="right">441,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,027</td>
<td align="right">3,047,597</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,763,054</td>
<td align="right">14,761,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,721,848</td>
<td align="right">1,721,718</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,965,411</td>
<td align="right">41,966,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,633</td>
<td align="right">9,742,533</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">8,709,159</td>
<td align="right">8,709,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,505</td>
<td align="right">25,720,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,098</td>
<td align="right">35,549,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,539</td>
<td align="right">591,619,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,141</td>
<td align="right">302,246,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,732</td>
<td align="right">128,851,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
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
<td align="left">GET_ANEXT</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">2,597,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,575</td>
<td align="right">98,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right">72,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right">69,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,850</td>
<td align="right">53,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,984</td>
<td align="right">13,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,641</td>
<td align="right">2,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">25</td>
<td align="right">25</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,213,747</td>
<td align="right">0.3%</td>
<td align="right">46,961,798</td>
<td align="right">0.3%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">996,560,354</td>
<td align="right">5.9%</td>
<td align="right">921,361,014</td>
<td align="right">5.5%</td>
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
<td align="right">15,953,848,401</td>
<td align="right">93.8%</td>
<td align="right">15,858,816,148</td>
<td align="right">94.2%</td>
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
<td align="right">403,462</td>
<td align="right">28.7%</td>
<td align="right">328,764</td>
<td align="right">26.7%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,003,442</td>
<td align="right">71.3%</td>
<td align="right">903,550</td>
<td align="right">73.3%</td>
<td align="right">-10.0%</td>
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
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">72,758</td>
<td align="right">18.0%</td>
<td align="right">24,883</td>
<td align="right">7.6%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,552</td>
<td align="right">2.9%</td>
<td align="right">6,172</td>
<td align="right">1.9%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,293</td>
<td align="right">2.1%</td>
<td align="right">5,934</td>
<td align="right">1.8%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">18,005</td>
<td align="right">4.5%</td>
<td align="right">13,155</td>
<td align="right">4.0%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">37,617</td>
<td align="right">9.3%</td>
<td align="right">28,536</td>
<td align="right">8.7%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,004</td>
<td align="right">5.2%</td>
<td align="right">18,429</td>
<td align="right">5.6%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,075</td>
<td align="right">5.2%</td>
<td align="right">18,854</td>
<td align="right">5.7%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,120</td>
<td align="right">0.5%</td>
<td align="right">2,000</td>
<td align="right">0.6%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">107</td>
<td align="right">0.0%</td>
<td align="right">110</td>
<td align="right">0.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,477</td>
<td align="right">1.6%</td>
<td align="right">6,374</td>
<td align="right">1.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,016</td>
<td align="right">1.7%</td>
<td align="right">6,945</td>
<td align="right">2.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">330</td>
<td align="right">0.1%</td>
<td align="right">332</td>
<td align="right">0.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,830</td>
<td align="right">4.9%</td>
<td align="right">19,723</td>
<td align="right">6.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">625</td>
<td align="right">0.2%</td>
<td align="right">628</td>
<td align="right">0.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">7.1%</td>
<td align="right">28,612</td>
<td align="right">8.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,469</td>
<td align="right">4.6%</td>
<td align="right">18,467</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">63,003</td>
<td align="right">15.6%</td>
<td align="right">63,001</td>
<td align="right">19.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">6.4%</td>
<td align="right">25,838</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">4.1%</td>
<td align="right">16,343</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.5%</td>
<td align="right">6,194</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.8%</td>
<td align="right">3,130</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2,935</td>
<td align="right">0.7%</td>
<td align="right">2,935</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">2,767</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">2,343</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">1,996</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,814</td>
<td align="right">0.4%</td>
<td align="right">1,814</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,364</td>
<td align="right">0.3%</td>
<td align="right">1,364</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">289</td>
<td align="right">0.1%</td>
<td align="right">289</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">179,170,442</td>
<td align="right">100.0%</td>
<td align="right">174,128,873</td>
<td align="right">100.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">8,620,254,152</td>
<td align="right">98.4%</td>
<td align="right">8,308,043,586</td>
<td align="right">98.3%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">143,353,894</td>
<td align="right">1.6%</td>
<td align="right">145,728,006</td>
<td align="right">1.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,724,875</td>
<td align="right">1.6%</td>
<td align="right">143,053,801</td>
<td align="right">1.7%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">2,881,238</td>
<td align="right">100.0%</td>
<td align="right">2,922,685</td>
<td align="right">100.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
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
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">594</td>
<td align="right">406.8%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">247</td>
<td align="right">169.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
<td align="right">100.0%</td>
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
<td align="right">576,076</td>
<td align="right">96.6%</td>
<td align="right">576,076</td>
<td align="right">96.6%</td>
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
<td align="right">583,374</td>
<td align="right">97.8%</td>
<td align="right">583,374</td>
<td align="right">97.8%</td>
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
<td align="right">20,451</td>
<td align="right">100.0%</td>
<td align="right">20,169</td>
<td align="right">100.0%</td>
<td align="right">-1.4%</td>
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
<td align="right">91,149,524</td>
<td align="right">2.0%</td>
<td align="right">90,078,997</td>
<td align="right">2.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,036,555</td>
<td align="right">0.0%</td>
<td align="right">1,024,498</td>
<td align="right">0.0%</td>
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
<td align="right">4,407,777,517</td>
<td align="right">97.9%</td>
<td align="right">4,392,658,689</td>
<td align="right">98.0%</td>
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
<td align="right">94,107</td>
<td align="right">71.4%</td>
<td align="right">92,879</td>
<td align="right">71.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,748</td>
<td align="right">28.6%</td>
<td align="right">37,336</td>
<td align="right">28.7%</td>
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
<td align="left">list</td>
<td align="right">838</td>
<td align="right">0.9%</td>
<td align="right">718</td>
<td align="right">0.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">31,820</td>
<td align="right">33.8%</td>
<td align="right">31,097</td>
<td align="right">33.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,400</td>
<td align="right">10.0%</td>
<td align="right">9,239</td>
<td align="right">9.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,080</td>
<td align="right">4.3%</td>
<td align="right">4,018</td>
<td align="right">4.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,883</td>
<td align="right">2.0%</td>
<td align="right">1,870</td>
<td align="right">2.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,640</td>
<td align="right">8.1%</td>
<td align="right">7,597</td>
<td align="right">8.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,095</td>
<td align="right">24.5%</td>
<td align="right">23,007</td>
<td align="right">24.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,854</td>
<td align="right">6.2%</td>
<td align="right">5,836</td>
<td align="right">6.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">8.1%</td>
<td align="right">7,648</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,323</td>
<td align="right">1.4%</td>
<td align="right">1,323</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">154</td>
<td align="right">0.2%</td>
<td align="right">154</td>
<td align="right">0.2%</td>
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
<td align="right">75,572,193</td>
<td align="right">3.9%</td>
<td align="right">70,794,915</td>
<td align="right">3.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,842,155,797</td>
<td align="right">96.0%</td>
<td align="right">1,812,724,588</td>
<td align="right">96.2%</td>
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
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,959</td>
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
<td align="right">38,360</td>
<td align="right">57.3%</td>
<td align="right">35,733</td>
<td align="right">55.7%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,541</td>
<td align="right">42.7%</td>
<td align="right">28,421</td>
<td align="right">44.3%</td>
<td align="right">-0.4%</td>
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
<td align="right">11,267</td>
<td align="right">29.4%</td>
<td align="right">10,206</td>
<td align="right">28.6%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">7,772</td>
<td align="right">20.3%</td>
<td align="right">7,243</td>
<td align="right">20.3%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,094</td>
<td align="right">23.7%</td>
<td align="right">8,520</td>
<td align="right">23.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,227</td>
<td align="right">26.7%</td>
<td align="right">9,764</td>
<td align="right">27.3%</td>
<td align="right">-4.5%</td>
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
<td align="right">44,183,392</td>
<td align="right">3.0%</td>
<td align="right">29,073,831</td>
<td align="right">2.1%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,212,156,703</td>
<td align="right">83.5%</td>
<td align="right">1,143,698,981</td>
<td align="right">84.2%</td>
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
<td align="right">195,838,916</td>
<td align="right">13.5%</td>
<td align="right">185,781,980</td>
<td align="right">13.7%</td>
<td align="right">-5.1%</td>
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
<td align="right">838,952</td>
<td align="right">88.8%</td>
<td align="right">553,874</td>
<td align="right">84.1%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,271</td>
<td align="right">11.2%</td>
<td align="right">104,534</td>
<td align="right">15.9%</td>
<td align="right">-1.6%</td>
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
<td align="right">956</td>
<td align="right">0.9%</td>
<td align="right">716</td>
<td align="right">0.7%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,762</td>
<td align="right">4.5%</td>
<td align="right">3,581</td>
<td align="right">3.4%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,619</td>
<td align="right">1.5%</td>
<td align="right">1,919</td>
<td align="right">1.8%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,140</td>
<td align="right">3.0%</td>
<td align="right">2,720</td>
<td align="right">2.6%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,665</td>
<td align="right">5.3%</td>
<td align="right">5,025</td>
<td align="right">4.8%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,779</td>
<td align="right">12.0%</td>
<td align="right">12,504</td>
<td align="right">12.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">50,153</td>
<td align="right">47.2%</td>
<td align="right">50,961</td>
<td align="right">48.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,885</td>
<td align="right">10.2%</td>
<td align="right">10,724</td>
<td align="right">10.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,167</td>
<td align="right">3.9%</td>
<td align="right">4,216</td>
<td align="right">4.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,211</td>
<td align="right">4.0%</td>
<td align="right">4,234</td>
<td align="right">4.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,567</td>
<td align="right">3.4%</td>
<td align="right">3,567</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,497</td>
<td align="right">3.3%</td>
<td align="right">3,497</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">90</td>
<td align="right">0.1%</td>
<td align="right">90</td>
<td align="right">0.1%</td>
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
<td align="right">85,275,392</td>
<td align="right">85,275,392 / 0 !!</td>
<td align="right">64,903,560</td>
<td align="right">64,903,560 / 0 !!</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,049,799</td>
<td align="right">4,049,799 / 0 !!</td>
<td align="right">3,273,085</td>
<td align="right">3,273,085 / 0 !!</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120,862,094</td>
<td align="right">120,862,094 / 0 !!</td>
<td align="right">104,415,159</td>
<td align="right">104,415,159 / 0 !!</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">249,102,797</td>
<td align="right">249,102,797 / 0 !!</td>
<td align="right">223,077,656</td>
<td align="right">223,077,656 / 0 !!</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,604,985</td>
<td align="right">2,604,985 / 0 !!</td>
<td align="right">2,496,625</td>
<td align="right">2,496,625 / 0 !!</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111,977,360</td>
<td align="right">111,977,360 / 0 !!</td>
<td align="right">108,779,368</td>
<td align="right">108,779,368 / 0 !!</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,055,082</td>
<td align="right">12,055,082 / 0 !!</td>
<td align="right">11,900,335</td>
<td align="right">11,900,335 / 0 !!</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,680,084</td>
<td align="right">341,680,084 / 0 !!</td>
<td align="right">341,628,503</td>
<td align="right">341,628,503 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,651,422</td>
<td align="right">34,651,422 / 0 !!</td>
<td align="right">34,649,602</td>
<td align="right">34,649,602 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
<td align="right">492,011,975</td>
<td align="right">4.7%</td>
<td align="right">358,107,297</td>
<td align="right">3.6%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">491,195,869</td>
<td align="right">4.7%</td>
<td align="right">426,171,250</td>
<td align="right">4.3%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,540,465,683</td>
<td align="right">90.6%</td>
<td align="right">9,145,069,733</td>
<td align="right">92.1%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,389</td>
<td align="right">0.0%</td>
<td align="right">1,262,389</td>
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
<td align="right">9,402,241</td>
<td align="right">95.6%</td>
<td align="right">6,905,629</td>
<td align="right">94.3%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">433,291</td>
<td align="right">4.4%</td>
<td align="right">419,494</td>
<td align="right">5.7%</td>
<td align="right">-3.2%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">19,539</td>
<td align="right">4.5%</td>
<td align="right">13,301</td>
<td align="right">3.2%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,391</td>
<td align="right">1.5%</td>
<td align="right">4,814</td>
<td align="right">1.1%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,667</td>
<td align="right">0.4%</td>
<td align="right">1,502</td>
<td align="right">0.4%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">35,999</td>
<td align="right">8.3%</td>
<td align="right">33,156</td>
<td align="right">7.9%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40,786</td>
<td align="right">9.4%</td>
<td align="right">38,336</td>
<td align="right">9.1%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">4,383</td>
<td align="right">1.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,334</td>
<td align="right">3.5%</td>
<td align="right">15,133</td>
<td align="right">3.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47,866</td>
<td align="right">11.0%</td>
<td align="right">47,317</td>
<td align="right">11.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,886</td>
<td align="right">1.1%</td>
<td align="right">4,838</td>
<td align="right">1.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">2,379</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,647</td>
<td align="right">0.4%</td>
<td align="right">1,647</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">703</td>
<td align="right">0.2%</td>
<td align="right">703</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,381</td>
<td align="right">0.0%</td>
<td align="right">1,721</td>
<td align="right">0.0%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,281,824,311</td>
<td align="right">99.7%</td>
<td align="right">4,131,128,022</td>
<td align="right">99.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,425</td>
<td align="right">0.0%</td>
<td align="right">46,245</td>
<td align="right">0.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,435</td>
<td align="right">0.3%</td>
<td align="right">14,623,292</td>
<td align="right">0.4%</td>
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
<td align="right">140,330</td>
<td align="right">100.0%</td>
<td align="right">138,602</td>
<td align="right">100.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">65,058,340</td>
<td align="right">100.0%</td>
<td align="right">64,410,705</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">216</td>
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
<td align="right">2,425</td>
<td align="right">100.0%</td>
<td align="right">2,425</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">591,604,828</td>
<td align="right">82.1%</td>
<td align="right">591,604,835</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
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
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">82,596,182</td>
<td align="right">4.5%</td>
<td align="right">51,233,481</td>
<td align="right">2.9%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,552,829</td>
<td align="right">2.8%</td>
<td align="right">39,970,196</td>
<td align="right">2.3%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,699,932,209</td>
<td align="right">92.7%</td>
<td align="right">1,670,844,647</td>
<td align="right">94.8%</td>
<td align="right">-1.7%</td>
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
<td align="right">1,599,666</td>
<td align="right">97.5%</td>
<td align="right">1,007,950</td>
<td align="right">96.8%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40,336</td>
<td align="right">2.5%</td>
<td align="right">33,674</td>
<td align="right">3.2%</td>
<td align="right">-16.5%</td>
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
<td align="right">15,813</td>
<td align="right">39.2%</td>
<td align="right">9,773</td>
<td align="right">29.0%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">704</td>
<td align="right">1.7%</td>
<td align="right">504</td>
<td align="right">1.5%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,519</td>
<td align="right">3.8%</td>
<td align="right">1,419</td>
<td align="right">4.2%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,207</td>
<td align="right">17.9%</td>
<td align="right">6,847</td>
<td align="right">20.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,650</td>
<td align="right">11.5%</td>
<td align="right">4,734</td>
<td align="right">14.1%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,446</td>
<td align="right">8.5%</td>
<td align="right">3,422</td>
<td align="right">10.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">241,128</td>
<td align="right">597.8%</td>
<td align="right">241,868</td>
<td align="right">718.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,781</td>
<td align="right">9.4%</td>
<td align="right">3,781</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">365</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
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
<td align="right">1,085,654</td>
<td align="right">100.0%</td>
<td align="right">933,214</td>
<td align="right">100.0%</td>
<td align="right">-14.0%</td>
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
<td align="right">101,286,071</td>
<td align="right">10.9%</td>
<td align="right">92,736,134</td>
<td align="right">10.3%</td>
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
<td align="right">828,043,016</td>
<td align="right">89.1%</td>
<td align="right">803,894,986</td>
<td align="right">89.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
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
<td align="right">34,903</td>
<td align="right">94.1%</td>
<td align="right">30,919</td>
<td align="right">93.8%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,181</td>
<td align="right">5.9%</td>
<td align="right">2,041</td>
<td align="right">6.2%</td>
<td align="right">-6.4%</td>
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
<td align="right">2,511</td>
<td align="right">7.2%</td>
<td align="right">1,930</td>
<td align="right">6.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">30.0%</td>
<td align="right">9,040</td>
<td align="right">29.2%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">301</td>
<td align="right">1.0%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,566</td>
<td align="right">47.5%</td>
<td align="right">14,787</td>
<td align="right">47.8%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,563</td>
<td align="right">4.5%</td>
<td align="right">1,423</td>
<td align="right">4.6%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.5%</td>
<td align="right">3,323</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">47</td>
<td align="right">0.1%</td>
<td align="right">47</td>
<td align="right">0.2%</td>
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
<td align="right">60,712,178</td>
<td align="right">1.9%</td>
<td align="right">55,362,246</td>
<td align="right">1.9%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,948,205,070</td>
<td align="right">93.9%</td>
<td align="right">2,803,558,757</td>
<td align="right">93.9%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,986,143</td>
<td align="right">4.1%</td>
<td align="right">126,075,589</td>
<td align="right">4.2%</td>
<td align="right">-2.3%</td>
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
<td align="right">394,166</td>
<td align="right">24.8%</td>
<td align="right">296,658</td>
<td align="right">21.3%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,195,500</td>
<td align="right">75.2%</td>
<td align="right">1,093,896</td>
<td align="right">78.7%</td>
<td align="right">-8.5%</td>
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
<td align="right">54,384</td>
<td align="right">13.8%</td>
<td align="right">31,730</td>
<td align="right">10.7%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">206,224</td>
<td align="right">52.3%</td>
<td align="right">136,071</td>
<td align="right">45.9%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">26,677</td>
<td align="right">6.8%</td>
<td align="right">23,728</td>
<td align="right">8.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,430</td>
<td align="right">2.6%</td>
<td align="right">10,028</td>
<td align="right">3.4%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">70,981</td>
<td align="right">18.0%</td>
<td align="right">69,625</td>
<td align="right">23.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,840</td>
<td align="right">2.2%</td>
<td align="right">8,844</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,067</td>
<td align="right">2.6%</td>
<td align="right">10,069</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,677</td>
<td align="right">1.2%</td>
<td align="right">4,677</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.4%</td>
<td align="right">1,420</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.0%</td>
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
<td align="right">1,251,635</td>
<td align="right">0.1%</td>
<td align="right">1,165,598</td>
<td align="right">0.1%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">915,486,128</td>
<td align="right">99.9%</td>
<td align="right">891,020,901</td>
<td align="right">99.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,040</td>
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
<td align="left">Success</td>
<td align="right">10,001</td>
<td align="right">92.7%</td>
<td align="right">9,701</td>
<td align="right">92.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">790</td>
<td align="right">7.3%</td>
<td align="right">777</td>
<td align="right">7.4%</td>
<td align="right">-1.6%</td>
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
<td align="right">556</td>
<td align="right">70.4%</td>
<td align="right">543</td>
<td align="right">69.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.2%</td>
<td align="right">136</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.4%</td>
<td align="right">98</td>
<td align="right">12.6%</td>
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
<td align="right">878,304,020</td>
<td align="right">1.0%</td>
<td align="right">689,683,696</td>
<td align="right">0.8%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,954,248,096</td>
<td align="right">3.3%</td>
<td align="right">2,705,102,615</td>
<td align="right">3.2%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">52,923,574,850</td>
<td align="right">59.2%</td>
<td align="right">49,462,450,408</td>
<td align="right">59.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,696,320,072</td>
<td align="right">36.6%</td>
<td align="right">30,870,797,111</td>
<td align="right">36.9%</td>
<td align="right">-5.6%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">491,195,869</td>
<td align="right">18.9%</td>
<td align="right">426,171,250</td>
<td align="right">17.6%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,286,071</td>
<td align="right">3.9%</td>
<td align="right">92,736,134</td>
<td align="right">3.8%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">996,560,354</td>
<td align="right">38.4%</td>
<td align="right">921,361,014</td>
<td align="right">38.1%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">75,572,193</td>
<td align="right">2.9%</td>
<td align="right">70,794,915</td>
<td align="right">2.9%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,838,916</td>
<td align="right">7.5%</td>
<td align="right">185,781,980</td>
<td align="right">7.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">179,170,442</td>
<td align="right">6.9%</td>
<td align="right">174,128,873</td>
<td align="right">7.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">128,986,143</td>
<td align="right">5.0%</td>
<td align="right">126,075,589</td>
<td align="right">5.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140,724,875</td>
<td align="right">5.4%</td>
<td align="right">143,053,801</td>
<td align="right">5.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">91,149,524</td>
<td align="right">3.5%</td>
<td align="right">90,078,997</td>
<td align="right">3.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">5.0%</td>
<td align="right">128,816,934</td>
<td align="right">5.3%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">63,600,567</td>
<td align="right">7.2%</td>
<td align="right">32,239,727</td>
<td align="right">4.7%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">59,549,214</td>
<td align="right">6.8%</td>
<td align="right">30,489,217</td>
<td align="right">4.4%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">174,364,503</td>
<td align="right">19.8%</td>
<td align="right">123,348,942</td>
<td align="right">17.9%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">70,162,933</td>
<td align="right">8.0%</td>
<td align="right">50,168,028</td>
<td align="right">7.3%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">137,614,666</td>
<td align="right">15.7%</td>
<td align="right">109,194,333</td>
<td align="right">15.8%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">49,548,253</td>
<td align="right">5.6%</td>
<td align="right">55,644,505</td>
<td align="right">8.1%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">28,461,740</td>
<td align="right">3.2%</td>
<td align="right">25,421,457</td>
<td align="right">3.7%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,557,208</td>
<td align="right">3.0%</td>
<td align="right">25,352,826</td>
<td align="right">3.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,725,131</td>
<td align="right">2.8%</td>
<td align="right">24,727,548</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">22,073,155</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,872,939</td>
<td align="right">3.0%</td>
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
<td align="left">Frame objects created</td>
<td align="right">63,727,983</td>
<td align="right">1.1%</td>
<td align="right">57,678,023</td>
<td align="right">1.0%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,208,861</td>
<td align="right">0.4%</td>
<td align="right">22,210,353</td>
<td align="right">0.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,335,438,811</td>
<td align="right">74.6%</td>
<td align="right">4,161,704,698</td>
<td align="right">74.1%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">4,480,568,477</td>
<td align="right">77.1%</td>
<td align="right">4,306,109,322</td>
<td align="right">76.7%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">228,782,109</td>
<td align="right">3.9%</td>
<td align="right">221,263,318</td>
<td align="right">3.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">886,644,493</td>
<td align="right">15.3%</td>
<td align="right">863,466,060</td>
<td align="right">15.4%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">890,919,550</td>
<td align="right">15.3%</td>
<td align="right">867,739,957</td>
<td align="right">15.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">232,557,982</td>
<td align="right">4.0%</td>
<td align="right">227,745,766</td>
<td align="right">4.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,475,190,486</td>
<td align="right">25.4%</td>
<td align="right">1,451,842,223</td>
<td align="right">25.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,475,190,486</td>
<td align="right">25.4%</td>
<td align="right">1,451,842,223</td>
<td align="right">25.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">3,844</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,270,936</td>
<td align="right">10.1%</td>
<td align="right">584,102,266</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,271,193</td>
<td align="right">0.1%</td>
<td align="right">4,270,053</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,901</td>
<td align="right">2.3%</td>
<td align="right">132,513,901</td>
<td align="right">2.4%</td>
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
<td align="right">37,731,918</td>
<td align="right"></td>
<td align="right">21,744,550</td>
<td align="right"></td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">41,445,328</td>
<td align="right"></td>
<td align="right">24,534,411</td>
<td align="right"></td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,976,184</td>
<td align="right"></td>
<td align="right">2,835,804</td>
<td align="right"></td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">219,028</td>
<td align="right">0.1%</td>
<td align="right">157,628</td>
<td align="right">0.1%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,799,545,017</td>
<td align="right"></td>
<td align="right">1,540,273,797</td>
<td align="right"></td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,153,770,990</td>
<td align="right">1.2%</td>
<td align="right">1,078,629,890</td>
<td align="right">1.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,779,125,944</td>
<td align="right"></td>
<td align="right">1,665,503,394</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">29,135,016,687</td>
<td align="right">29.6%</td>
<td align="right">27,645,318,543</td>
<td align="right">29.0%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,759,979,773</td>
<td align="right">3.4%</td>
<td align="right">2,619,549,007</td>
<td align="right">3.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">22,837,721,598</td>
<td align="right">27.8%</td>
<td align="right">21,881,126,024</td>
<td align="right">27.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,657,728,361</td>
<td align="right">26.4%</td>
<td align="right">4,491,275,662</td>
<td align="right">26.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,217,793,071</td>
<td align="right"></td>
<td align="right">5,032,912,737</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,734,950,757</td>
<td align="right">26.9%</td>
<td align="right">4,567,971,956</td>
<td align="right">26.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,653,072</td>
<td align="right"></td>
<td align="right">162,711,605</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,980,455,124</td>
<td align="right">26.8%</td>
<td align="right">21,226,611,522</td>
<td align="right">26.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">34,517,953,375</td>
<td align="right">42.0%</td>
<td align="right">33,356,214,390</td>
<td align="right">42.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,264,982</td>
<td align="right">0.0%</td>
<td align="right">6,076,469</td>
<td align="right">0.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,580,085,117</td>
<td align="right">24.0%</td>
<td align="right">22,891,221,078</td>
<td align="right">24.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">44,521,676,281</td>
<td align="right">45.2%</td>
<td align="right">43,600,855,708</td>
<td align="right">45.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,899,985,445</td>
<td align="right"></td>
<td align="right">12,723,519,279</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,899,839,861</td>
<td align="right">73.1%</td>
<td align="right">12,723,408,861</td>
<td align="right">73.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">70,957,414</td>
<td align="right">0.4%</td>
<td align="right">70,619,825</td>
<td align="right">0.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,405,116</td>
<td align="right">2.0%</td>
<td align="right">3,405,116</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
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
<td align="right">353,083</td>
<td align="right">69,904,835</td>
<td align="right">8,973,122,872</td>
<td align="right">727,424,721</td>
<td align="right">718,903,523</td>
<td align="right">338,881</td>
<td align="right">30,236,260</td>
<td align="right">8,340,401,858</td>
<td align="right">705,356,276</td>
<td align="right">663,632,206</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,454,908</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,445,188</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">225</td>
<td align="right">0.1%</td>
<td align="right">257.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,676</td>
<td align="right">0.4%</td>
<td align="right">3,792</td>
<td align="right">1.0%</td>
<td align="right">126.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">202,136</td>
<td align="right">50.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,947</td>
<td align="right">0.5%</td>
<td align="right">709</td>
<td align="right">0.2%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">261</td>
<td align="right">1.0%</td>
<td align="right">341</td>
<td align="right">1.2%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">122,057</td>
<td align="right">30.6%</td>
<td align="right">156,931</td>
<td align="right">41.0%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">431</td>
<td align="right">0.1%</td>
<td align="right">534</td>
<td align="right">0.1%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">50</td>
<td align="right">0.0%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,463,571,032</td>
<td align="right"></td>
<td align="right">4,058,389,701</td>
<td align="right"></td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">398,393</td>
<td align="right"></td>
<td align="right">382,475</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">27,041</td>
<td align="right">6.8%</td>
<td align="right">27,673</td>
<td align="right">7.2%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">219,590,687,082</td>
<td align="right">6,340.0%</td>
<td align="right">224,408,031,789</td>
<td align="right">5,529.5%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,117</td>
<td align="right">11.8%</td>
<td align="right">47,643</td>
<td align="right">12.5%</td>
<td align="right">1.1%</td>
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
<td align="right">22,153</td>
<td align="right">81.9%</td>
<td align="right">23,833</td>
<td align="right">86.1%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">27,041</td>
<td align="right"></td>
<td align="right">27,673</td>
<td align="right"></td>
<td align="right">2.3%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">18,313,216</td>
<td align="right">6.7%</td>
<td align="right">1,921,024</td>
<td align="right">0.5%</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">220,147,934</td>
<td align="right">80.9%</td>
<td align="right">297,443,285</td>
<td align="right">84.2%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">272,183,296</td>
<td align="right"></td>
<td align="right">353,292,288</td>
<td align="right"></td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">5,769,648</td>
<td align="right">2.1%</td>
<td align="right">7,415,848</td>
<td align="right">2.1%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">46,265,714</td>
<td align="right">17.0%</td>
<td align="right">48,433,155</td>
<td align="right">13.7%</td>
<td align="right">4.7%</td>
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
<td align="left">5,562</td>
<td align="right">25.1%</td>
<td align="left">5,044</td>
<td align="right">21.2%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,019</td>
<td align="right">31.7%</td>
<td align="left">6,390</td>
<td align="right">26.8%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">6,280</td>
<td align="right">28.3%</td>
<td align="left">6,653</td>
<td align="right">27.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,247</td>
<td align="right">10.1%</td>
<td align="left">3,726</td>
<td align="right">15.6%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">965</td>
<td align="right">4.4%</td>
<td align="left">1,858</td>
<td align="right">7.8%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">80</td>
<td align="right">0.4%</td>
<td align="left">162</td>
<td align="right">0.7%</td>
<td align="right">102.5%</td>
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
<td align="left"><= 8</td>
<td align="right">1,298</td>
<td align="right">4.8%</td>
<td align="right">1,257</td>
<td align="right">4.5%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">896</td>
<td align="right">3.3%</td>
<td align="right">1,550</td>
<td align="right">5.6%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,320</td>
<td align="right">16.0%</td>
<td align="right">3,196</td>
<td align="right">11.5%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,192</td>
<td align="right">30.3%</td>
<td align="right">6,391</td>
<td align="right">23.1%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,224</td>
<td align="right">19.3%</td>
<td align="right">6,450</td>
<td align="right">23.3%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,168</td>
<td align="right">19.1%</td>
<td align="right">5,288</td>
<td align="right">19.1%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,676</td>
<td align="right">6.2%</td>
<td align="right">2,990</td>
<td align="right">10.8%</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">267</td>
<td align="right">1.0%</td>
<td align="right">551</td>
<td align="right">2.0%</td>
<td align="right">106.4%</td>
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
<td align="left"><= 4</td>
<td align="right">731</td>
<td align="right">2.7%</td>
<td align="right">731</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">891</td>
<td align="right">3.3%</td>
<td align="right">772</td>
<td align="right">2.8%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,650</td>
<td align="right">9.8%</td>
<td align="right">2,742</td>
<td align="right">9.9%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,380</td>
<td align="right">27.3%</td>
<td align="right">5,652</td>
<td align="right">20.4%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,181</td>
<td align="right">22.9%</td>
<td align="right">6,674</td>
<td align="right">24.1%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,463</td>
<td align="right">9.1%</td>
<td align="right">4,263</td>
<td align="right">15.4%</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,675</td>
<td align="right">6.2%</td>
<td align="right">2,475</td>
<td align="right">8.9%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">182</td>
<td align="right">0.7%</td>
<td align="right">524</td>
<td align="right">1.9%</td>
<td align="right">187.9%</td>
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
<td align="left">_DELETE_SUBSCR</td>
<td align="right">179,903</td>
<td align="right">9,355,909</td>
<td align="right">5,100.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">677,888</td>
<td align="right">6,775,646</td>
<td align="right">899.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,953,793</td>
<td align="right">23,044,698</td>
<td align="right">189.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,560,502</td>
<td align="right">801,235</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,783,149</td>
<td align="right">11,555,068</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">101,585,388</td>
<td align="right">142,274,374</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,585,388</td>
<td align="right">142,274,374</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">101,740,528</td>
<td align="right">142,361,554</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,983,993</td>
<td align="right">2,735,848</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">39,831,068</td>
<td align="right">26,699,585</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,433,550</td>
<td align="right">1,000,330</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,324,005</td>
<td align="right">2,410,985</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right">10,476,300</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">34,521,547</td>
<td align="right">42,859,399</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,176,916</td>
<td align="right">1,666,116</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">474,795</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,399,783</td>
<td align="right">65,461,945</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,713,427</td>
<td align="right">5,313,558</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">52,258,341</td>
<td align="right">41,804,380</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">440,121,418</td>
<td align="right">521,336,996</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">170,042,198</td>
<td align="right">139,002,539</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">57,567,413</td>
<td align="right">47,544,927</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,428,874,103</td>
<td align="right">4,023,740,362</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,463,571,032</td>
<td align="right">4,058,389,701</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">247,851,902</td>
<td align="right">208,447,012</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">49,132,694</td>
<td align="right">56,775,449</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">50,000,356</td>
<td align="right">57,255,603</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">118,803,098</td>
<td align="right">135,819,687</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">75,010,522</td>
<td align="right">85,627,040</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">211,745,927</td>
<td align="right">182,052,909</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">169,970,805</td>
<td align="right">147,944,522</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">98,098,601</td>
<td align="right">86,317,948</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">5,303,275</td>
<td align="right">5,929,555</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">5,303,275</td>
<td align="right">5,929,555</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">121,884,246</td>
<td align="right">107,715,963</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">608,464,989</td>
<td align="right">678,885,594</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">196,728,502</td>
<td align="right">174,489,687</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">153,039,303</td>
<td align="right">170,091,310</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,583,956</td>
<td align="right">6,190,168</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">5,852,494,984</td>
<td align="right">6,432,432,057</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">192,648,203</td>
<td align="right">174,410,768</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,306,073</td>
<td align="right">41,631,320</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,605,753</td>
<td align="right">52,811,067</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,331,269</td>
<td align="right">691,890,012</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">591,130,589</td>
<td align="right">633,885,152</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,718,540</td>
<td align="right">5,322,540</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">81,255,858</td>
<td align="right">75,772,378</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">197,253,092</td>
<td align="right">209,228,854</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,165,756,879</td>
<td align="right">1,235,951,451</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">433,020,859</td>
<td align="right">458,790,716</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,409,132</td>
<td align="right">1,331,572</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">489,688,795</td>
<td align="right">516,040,471</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">489,802,035</td>
<td align="right">516,040,471</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">50,147,000</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,266,418,901</td>
<td align="right">1,331,878,940</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">90,282,923</td>
<td align="right">94,919,477</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">144,386</td>
<td align="right">151,800</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">2,706,669,192</td>
<td align="right">2,844,859,065</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">27,042,203</td>
<td align="right">25,684,224</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,329,303,582</td>
<td align="right">1,395,487,174</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,329,483,214</td>
<td align="right">1,395,665,506</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">4,435,758</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">30,495,173</td>
<td align="right">31,792,369</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">78,980,963</td>
<td align="right">82,081,437</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,319,706,163</td>
<td align="right">1,269,039,213</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">884,793,676</td>
<td align="right">918,018,921</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">40,460,443</td>
<td align="right">41,966,317</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">30,021,049</td>
<td align="right">28,913,482</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,737,325,890</td>
<td align="right">2,637,993,376</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,315,657,439</td>
<td align="right">1,268,697,169</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,223,810,183</td>
<td align="right">1,266,745,722</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">609,257,681</td>
<td align="right">630,534,934</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">222,018</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">96,571,866</td>
<td align="right">99,768,685</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,104,317</td>
<td align="right">38,331,197</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">294,820,200</td>
<td align="right">304,302,812</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">433,516,421</td>
<td align="right">447,330,835</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">322,789,526</td>
<td align="right">333,046,843</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">65,207,763</td>
<td align="right">63,170,629</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">602,897,187</td>
<td align="right">584,184,172</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,993</td>
<td align="right">432,804,348</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,755,849</td>
<td align="right">141,485,922</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,463,129,475</td>
<td align="right">1,505,654,929</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">404,684,245</td>
<td align="right">416,431,754</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,199,132,886</td>
<td align="right">1,233,804,422</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,452,835,418</td>
<td align="right">3,552,395,724</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,227,614,467</td>
<td align="right">1,262,896,273</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,534,526</td>
<td align="right">44,761,406</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,991,793</td>
<td align="right">8,212,325</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">41,116,362</td>
<td align="right">40,044,434</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,222,983,427</td>
<td align="right">1,192,154,142</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">341,036,296</td>
<td align="right">332,454,196</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">568,620,157</td>
<td align="right">582,798,864</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">39,440,814,914</td>
<td align="right">40,396,734,278</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">424,614,758</td>
<td align="right">414,426,435</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">160,398,151</td>
<td align="right">156,618,572</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">121,790,865</td>
<td align="right">118,957,599</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">148,987,967</td>
<td align="right">145,810,437</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">383,450,243</td>
<td align="right">391,616,039</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">147,055,567</td>
<td align="right">150,001,868</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">24,643,554</td>
<td align="right">24,172,498</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,105,399,123</td>
<td align="right">9,276,505,978</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,073,171</td>
<td align="right">595,897,907</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,731,038,613</td>
<td align="right">1,700,143,122</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">165,936,688</td>
<td align="right">168,874,480</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">161,981,135</td>
<td align="right">159,115,101</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,141,584,372</td>
<td align="right">2,178,952,617</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,754,931,293</td>
<td align="right">1,785,370,636</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">208,827,224</td>
<td align="right">212,168,316</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">29,719,286</td>
<td align="right">29,249,309</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,782,792,530</td>
<td align="right">1,810,094,609</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">363,341,794</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">39,279,673</td>
<td align="right">39,823,175</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">262,313,214</td>
<td align="right">258,768,974</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">424,469,708</td>
<td align="right">418,815,015</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">784,278,016</td>
<td align="right">774,051,138</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">796,826,107</td>
<td align="right">786,599,105</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">796,826,107</td>
<td align="right">786,599,105</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">768,857,570</td>
<td align="right">778,432,689</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">52,782,630</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">52,782,630</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,808,674,834</td>
<td align="right">1,829,364,968</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,691,619</td>
<td align="right">116,353,839</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">577,035,507</td>
<td align="right">582,982,849</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">532,683,636</td>
<td align="right">527,193,780</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,839,840,845</td>
<td align="right">5,785,370,027</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">90,810,039</td>
<td align="right">91,620,951</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,909,803,319</td>
<td align="right">1,926,789,946</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">34,996,829,071</td>
<td align="right">35,305,078,687</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,283,792,869</td>
<td align="right">1,272,505,315</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,217,714,843</td>
<td align="right">1,207,054,352</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">451,080,786</td>
<td align="right">447,423,467</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,989,390,753</td>
<td align="right">1,974,012,346</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">452,206,029</td>
<td align="right">448,863,185</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,061,195,789</td>
<td align="right">1,054,289,808</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">469,041,941</td>
<td align="right">466,034,239</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,388,923,952</td>
<td align="right">2,374,042,356</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">921,766,149</td>
<td align="right">916,027,674</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,721,384,970</td>
<td align="right">3,743,619,592</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,877,166</td>
<td align="right">157,791,733</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">310,730,342</td>
<td align="right">308,998,462</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">84,643,314</td>
<td align="right">84,172,258</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,077</td>
<td align="right">144,384,137</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,438,787,850</td>
<td align="right">7,477,712,548</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">12,783,849</td>
<td align="right">12,719,353</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,257,371,505</td>
<td align="right">2,268,635,373</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">73,405,480</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,813,318</td>
<td align="right">46,024,379</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">358,521,878</td>
<td align="right">356,888,517</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">49,249,153</td>
<td align="right">49,440,563</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">731,839,989</td>
<td align="right">729,271,170</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,863,923,843</td>
<td align="right">2,854,134,141</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,041,856</td>
<td align="right">19,977,344</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,031,907,323</td>
<td align="right">3,023,731,138</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,777</td>
<td align="right">131,295,539</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,208,676</td>
<td align="right">4,200,888</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">694,097,677</td>
<td align="right">692,909,622</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">923,235,880</td>
<td align="right">921,727,154</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">923,250,740</td>
<td align="right">921,742,014</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,556,350,669</td>
<td align="right">2,552,266,822</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,148,998,666</td>
<td align="right">1,150,700,606</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,065,964,786</td>
<td align="right">1,064,444,341</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">706,244,570</td>
<td align="right">707,215,865</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,676,876</td>
<td align="right">34,629,286</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">3,873,776,427</td>
<td align="right">3,879,006,404</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,868,714</td>
<td align="right">1,344,191,804</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">462,143,821</td>
<td align="right">462,613,391</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,741,736</td>
<td align="right">976,637,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,838,776</td>
<td align="right">55,878,108</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">423,331,251</td>
<td align="right">423,621,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">601,196,603</td>
<td align="right">601,553,432</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">444,620,696</td>
<td align="right">444,882,430</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">444,620,696</td>
<td align="right">444,882,430</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,278,515,434</td>
<td align="right">2,279,764,606</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">46,575,594</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,050,990</td>
<td align="right">48,033,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,113,750,711</td>
<td align="right">1,113,343,738</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right">30,887,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right">30,887,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,793,678,934</td>
<td align="right">2,792,922,713</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,992,273,267</td>
<td align="right">1,991,849,132</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,655,710</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,655,710</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,062,952</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,507</td>
<td align="right">1,545,287</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,504,834,956</td>
<td align="right">2,504,483,513</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,282,834</td>
<td align="right">416,261,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">983,244,017</td>
<td align="right">983,270,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,547,967</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,547,967</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,253,140</td>
<td align="right">3,253,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,700,112</td>
<td align="right">6,700,092</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,554</td>
<td align="right">40,025,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,440</td>
<td align="right">47,940,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,487</td>
<td align="right">70,350,508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,487</td>
<td align="right">70,350,508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">263,905,156</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,143,550</td>
<td align="right">469,143,530</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,178,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,999,760</td>
<td align="right">59,999,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">3,709,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,106,080</td>
<td align="right">3,106,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,034,740</td>
<td align="right">3,034,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,678,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">918,506</td>
<td align="right">918,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">356,340</td>
<td align="right">356,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">117,983</td>
<td align="right">117,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,053</td>
<td align="right">20,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLER_INSTR_PTR</td>
<td align="right"></td>
<td align="right">764,097,341</td>
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
<td align="left">CALL</td>
<td align="right">1,810</td>
<td align="right">2,514</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,367</td>
<td align="right">23,591</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">161</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">161</td>
<td align="right">59.4%</td>
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
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
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
<td align="right">2,420</td>
<td align="right">2,420</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-29
