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
<td align="left">SET_ADD</td>
<td align="right">47,480</td>
<td align="right">138,376</td>
<td align="right">191.4%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,460</td>
<td align="right">72,736</td>
<td align="right">164.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">662,682</td>
<td align="right">1,418,156</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,824,039</td>
<td align="right">3,748,176</td>
<td align="right">105.5%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,892</td>
<td align="right">291,875</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">271,939,827</td>
<td align="right">40,253,198</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">202,758,495</td>
<td align="right">51,864,289</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,609,230</td>
<td align="right">41,475,067</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">647,625,869</td>
<td align="right">304,094,279</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">718,259</td>
<td align="right">1,084,931</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">496,540</td>
<td align="right">747,620</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">960</td>
<td align="right">1,400</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">85,825,755</td>
<td align="right">47,536,455</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,077,996,660</td>
<td align="right">626,905,458</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">653,283</td>
<td align="right">916,305</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">144,080</td>
<td align="right">194,569</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">171,293,313</td>
<td align="right">112,028,966</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">320</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">321,938,096</td>
<td align="right">219,383,873</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,116,660</td>
<td align="right">28,807,121</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,141,213,385</td>
<td align="right">841,301,317</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">267,712,920</td>
<td align="right">197,609,925</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,430,778</td>
<td align="right">10,468,800</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,465,648</td>
<td align="right">210,396,559</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,037,363</td>
<td align="right">11,073,939</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,126,696,117</td>
<td align="right">3,266,695,450</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">383,865,103</td>
<td align="right">315,935,441</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,553,558</td>
<td align="right">20,556,494</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">187,377,937</td>
<td align="right">155,851,333</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">427,069,602</td>
<td align="right">355,404,979</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,943,468,755</td>
<td align="right">4,122,725,456</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">732,298,911</td>
<td align="right">617,406,271</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">249,829,379</td>
<td align="right">212,028,760</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">420</td>
<td align="right">480</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">193,921,735</td>
<td align="right">166,732,319</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,263,934,697</td>
<td align="right">2,817,311,495</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,345,472</td>
<td align="right">244,940,788</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">881,128,585</td>
<td align="right">761,774,531</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,259,654,366</td>
<td align="right">1,095,716,463</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,828,488,891</td>
<td align="right">2,471,546,821</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">807,420</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">44,313,302</td>
<td align="right">49,731,001</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,065</td>
<td align="right">16,903</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,640</td>
<td align="right">101,260</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">32,011,488</td>
<td align="right">35,201,680</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,339,851,266</td>
<td align="right">17,462,227,931</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">353,498,161</td>
<td align="right">319,401,994</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">155,053,415</td>
<td align="right">169,394,885</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">404,530,723</td>
<td align="right">370,057,336</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">112,728,267</td>
<td align="right">121,868,532</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">760,667,316</td>
<td align="right">700,934,317</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">47,707,946</td>
<td align="right">51,382,436</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,659,125</td>
<td align="right">109,478,290</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">896,775,113</td>
<td align="right">829,044,560</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,636,463,593</td>
<td align="right">2,445,315,511</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,072,353,189</td>
<td align="right">4,711,260,654</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">405,837,360</td>
<td align="right">377,151,423</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">99,285,982</td>
<td align="right">105,947,291</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">70,691,089</td>
<td align="right">75,402,731</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,563,825</td>
<td align="right">32,532,180</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,004,766,175</td>
<td align="right">940,184,365</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,445,636</td>
<td align="right">4,714,700</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">335,424,140</td>
<td align="right">355,204,337</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,118,666,208</td>
<td align="right">3,878,301,694</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,423</td>
<td align="right">182,626</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">924,161,692</td>
<td align="right">876,002,482</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,817,560</td>
<td align="right">21,793,225</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,251,497</td>
<td align="right">22,232,350</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,259,836</td>
<td align="right">22,240,700</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,313,457</td>
<td align="right">144,660,466</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">657,857,952</td>
<td align="right">628,176,661</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,992,641</td>
<td align="right">153,607,195</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,917,056</td>
<td align="right">207,310,037</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,958,863</td>
<td align="right">11,411,787</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,388,304</td>
<td align="right">9,991,456</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,099</td>
<td align="right">231,514</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">480,879,278</td>
<td align="right">498,319,347</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,800</td>
<td align="right">29,840</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">119,842,159</td>
<td align="right">124,163,290</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">529,584,838</td>
<td align="right">548,178,469</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">224,006,455</td>
<td align="right">231,300,205</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">212,229,965</td>
<td align="right">219,081,822</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,222,771</td>
<td align="right">85,871,128</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,986,361</td>
<td align="right">55,661,814</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">37,870,212</td>
<td align="right">38,983,087</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,087,393,487</td>
<td align="right">1,055,611,374</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">622,320</td>
<td align="right">640,420</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,351,035</td>
<td align="right">60,038,924</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">651,352,048</td>
<td align="right">670,100,040</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">205,800,978</td>
<td align="right">211,482,473</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,980,209,236</td>
<td align="right">4,843,042,023</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,672,718</td>
<td align="right">128,069,892</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,825,143</td>
<td align="right">3,928,174</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">174,576,263</td>
<td align="right">179,052,915</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,897,778</td>
<td align="right">50,144,803</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,692,781</td>
<td align="right">1,074,347,461</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">229,691,470</td>
<td align="right">235,358,039</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,973,242,714</td>
<td align="right">2,020,231,351</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,679,100</td>
<td align="right">61,098,466</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">299,261,281</td>
<td align="right">306,315,296</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">159,693,921</td>
<td align="right">163,451,711</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,424,549</td>
<td align="right">2,477,647</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,875,877</td>
<td align="right">20,297,648</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,184,682</td>
<td align="right">495,405,165</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,958,466</td>
<td align="right">5,836,681</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">387,808,418</td>
<td align="right">395,649,739</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,082,609,880</td>
<td align="right">4,003,897,998</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">818,716,101</td>
<td align="right">834,096,058</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">51,864,980</td>
<td align="right">52,834,156</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,040</td>
<td align="right">21,420</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,400,109,033</td>
<td align="right">1,424,925,019</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,009,173</td>
<td align="right">69,185,213</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,870,862,010</td>
<td align="right">1,903,203,693</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,394,865,956</td>
<td align="right">2,353,525,262</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">772,312,434</td>
<td align="right">785,311,531</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">46,860,779</td>
<td align="right">47,594,857</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,917,496</td>
<td align="right">3,978,376</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">53,472,330</td>
<td align="right">54,288,698</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">445,425,832</td>
<td align="right">451,687,844</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">363,927,174</td>
<td align="right">368,882,497</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">476,104,958</td>
<td align="right">482,134,872</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">680,961,763</td>
<td align="right">688,982,490</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,812,890</td>
<td align="right">73,598,831</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,920</td>
<td align="right">151,513,134</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,597,924</td>
<td align="right">9,697,588</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,054,079</td>
<td align="right">91,946,395</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,442,691,780</td>
<td align="right">3,411,293,991</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">317,410,462</td>
<td align="right">320,192,410</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">190,989,498</td>
<td align="right">192,601,570</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,961</td>
<td align="right">32,070,210</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">28,350,756</td>
<td align="right">28,577,855</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,360,290</td>
<td align="right">217,035,851</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,807,143</td>
<td align="right">109,636,397</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,469,871</td>
<td align="right">83,079,284</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">147,047,000</td>
<td align="right">148,115,773</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">372,596,534</td>
<td align="right">375,234,894</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,403,545</td>
<td align="right">297,241,658</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">198,415,002</td>
<td align="right">199,598,284</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,700</td>
<td align="right">158,634</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">7,505,164</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,348,752</td>
<td align="right">20,461,155</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,027,816,271</td>
<td align="right">3,042,478,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">326,738,685</td>
<td align="right">328,277,098</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">321,566,421</td>
<td align="right">322,879,618</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">137,332,725</td>
<td align="right">136,814,533</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,192,420</td>
<td align="right">92,524,558</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">50,238,139</td>
<td align="right">50,416,827</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,930,066,524</td>
<td align="right">5,949,597,679</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,641,139</td>
<td align="right">82,899,924</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,802,810</td>
<td align="right">82,056,831</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,403,180</td>
<td align="right">173,925,977</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,504,810</td>
<td align="right">48,645,478</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">41,962,736</td>
<td align="right">41,842,530</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,760,070</td>
<td align="right">37,858,336</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,003,900</td>
<td align="right">225,536,167</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,942,081</td>
<td align="right">72,111,803</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,890,882</td>
<td align="right">232,437,078</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,767,675</td>
<td align="right">403,573,233</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,699,911</td>
<td align="right">1,374,203,642</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,244,120</td>
<td align="right">92,400,216</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,526,060</td>
<td align="right">94,683,256</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,740</td>
<td align="right">402,640,986</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,374</td>
<td align="right">190,226,691</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,956,074</td>
<td align="right">556,498,071</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,656,480</td>
<td align="right">136,537,468</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">781,974,612</td>
<td align="right">782,592,438</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,735,040</td>
<td align="right">328,966,469</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,304,680</td>
<td align="right">10,310,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,309,277</td>
<td align="right">8,307,226</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,802,902</td>
<td align="right">143,771,132</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">47,430,742</td>
<td align="right">47,439,179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,465,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,699,192</td>
<td align="right">46,700,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
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
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">391,720,734</td>
<td align="right">4.0%</td>
<td align="right">396,658,278</td>
<td align="right">4.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,428,536,387</td>
<td align="right">96.0%</td>
<td align="right">9,403,893,541</td>
<td align="right">95.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">29,506,617</td>
<td align="right">0.3%</td>
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
<td align="right">1,109,802</td>
<td align="right">65.0%</td>
<td align="right">1,128,193</td>
<td align="right">65.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,558</td>
<td align="right">35.0%</td>
<td align="right">602,643</td>
<td align="right">34.8%</td>
<td align="right">0.9%</td>
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
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">3,454</td>
<td align="right">0.3%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,503</td>
<td align="right">0.9%</td>
<td align="right">12,506</td>
<td align="right">1.1%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">28,045</td>
<td align="right">2.5%</td>
<td align="right">33,129</td>
<td align="right">2.9%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,264</td>
<td align="right">1.3%</td>
<td align="right">16,484</td>
<td align="right">1.5%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">913</td>
<td align="right">0.1%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,627</td>
<td align="right">0.5%</td>
<td align="right">6,124</td>
<td align="right">0.5%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,723</td>
<td align="right">0.4%</td>
<td align="right">5,122</td>
<td align="right">0.5%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">19,931</td>
<td align="right">1.8%</td>
<td align="right">21,308</td>
<td align="right">1.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,447</td>
<td align="right">0.6%</td>
<td align="right">6,827</td>
<td align="right">0.6%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,541</td>
<td align="right">0.5%</td>
<td align="right">5,734</td>
<td align="right">0.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">46,938</td>
<td align="right">4.2%</td>
<td align="right">48,154</td>
<td align="right">4.3%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,606</td>
<td align="right">7.4%</td>
<td align="right">83,657</td>
<td align="right">7.4%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,540</td>
<td align="right">0.9%</td>
<td align="right">9,702</td>
<td align="right">0.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,678</td>
<td align="right">4.4%</td>
<td align="right">49,494</td>
<td align="right">4.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,397</td>
<td align="right">2.9%</td>
<td align="right">32,753</td>
<td align="right">2.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,603</td>
<td align="right">70.4%</td>
<td align="right">782,370</td>
<td align="right">69.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,463</td>
<td align="right">0.7%</td>
<td align="right">7,462</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,580</td>
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
<td align="right">736,690,601</td>
<td align="right">10.7%</td>
<td align="right">621,818,570</td>
<td align="right">9.3%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,150,472,410</td>
<td align="right">89.3%</td>
<td align="right">6,088,487,164</td>
<td align="right">90.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,811,745</td>
<td align="right">0.1%</td>
<td align="right">4,813,021</td>
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
<td align="right">238,078</td>
<td align="right">56.7%</td>
<td align="right">213,755</td>
<td align="right">53.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,977</td>
<td align="right">43.3%</td>
<td align="right">186,967</td>
<td align="right">46.7%</td>
<td align="right">2.7%</td>
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
<td align="left">code complex parameters</td>
<td align="right">19,480</td>
<td align="right">8.2%</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,419</td>
<td align="right">12.8%</td>
<td align="right">21,904</td>
<td align="right">10.2%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,420</td>
<td align="right">0.7%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">4,300</td>
<td align="right">2.0%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">108,676</td>
<td align="right">45.6%</td>
<td align="right">111,949</td>
<td align="right">52.4%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,700</td>
<td align="right">23.4%</td>
<td align="right">56,160</td>
<td align="right">26.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.8%</td>
<td align="right">16,200</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">664,262,051</td>
<td align="right">4.6%</td>
<td align="right">673,907,791</td>
<td align="right">4.7%</td>
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
<td align="right">13,683,993,770</td>
<td align="right">95.3%</td>
<td align="right">13,569,553,015</td>
<td align="right">95.2%</td>
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
<td align="right">183,224,790</td>
<td align="right">1.3%</td>
<td align="right">182,716,469</td>
<td align="right">1.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
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
<td align="right">165,622</td>
<td align="right">4.0%</td>
<td align="right">177,396</td>
<td align="right">4.2%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,981,799</td>
<td align="right">96.0%</td>
<td align="right">4,036,447</td>
<td align="right">95.8%</td>
<td align="right">1.4%</td>
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
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,200</td>
<td align="right">5.6%</td>
<td align="right">11,580</td>
<td align="right">6.5%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">156,062</td>
<td align="right">94.2%</td>
<td align="right">165,236</td>
<td align="right">93.1%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,000</td>
<td align="right">1.2%</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">2.1%</td>
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
<td align="right">100,131,355</td>
<td align="right">1.6%</td>
<td align="right">106,786,603</td>
<td align="right">1.8%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,130,893,313</td>
<td align="right">98.4%</td>
<td align="right">5,754,659,537</td>
<td align="right">98.2%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,071,433</td>
<td align="right">0.0%</td>
<td align="right">1,080,009</td>
<td align="right">0.0%</td>
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
<td align="left">Success</td>
<td align="right">76,290</td>
<td align="right">33.7%</td>
<td align="right">81,575</td>
<td align="right">33.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">149,770</td>
<td align="right">66.3%</td>
<td align="right">159,122</td>
<td align="right">66.1%</td>
<td align="right">6.2%</td>
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
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">3,240</td>
<td align="right">2.0%</td>
<td align="right">237.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">1,600</td>
<td align="right">1.0%</td>
<td align="right">175.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,378</td>
<td align="right">9.6%</td>
<td align="right">16,181</td>
<td align="right">10.2%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,160</td>
<td align="right">12.8%</td>
<td align="right">20,183</td>
<td align="right">12.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,750</td>
<td align="right">28.5%</td>
<td align="right">44,614</td>
<td align="right">28.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,065</td>
<td align="right">18.1%</td>
<td align="right">27,905</td>
<td align="right">17.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.8%</td>
<td align="right">2,620</td>
<td align="right">1.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,423</td>
<td align="right">1.0%</td>
<td align="right">1,463</td>
<td align="right">0.9%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,934</td>
<td align="right">11.3%</td>
<td align="right">17,406</td>
<td align="right">10.9%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,220</td>
<td align="right">8.2%</td>
<td align="right">12,310</td>
<td align="right">7.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">920</td>
<td align="right">0.6%</td>
<td align="right">920</td>
<td align="right">0.6%</td>
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
<td align="right">205,130,775</td>
<td align="right">7.6%</td>
<td align="right">54,262,455</td>
<td align="right">2.1%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,490,739,493</td>
<td align="right">92.4%</td>
<td align="right">2,498,096,598</td>
<td align="right">97.9%</td>
<td align="right">0.3%</td>
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
<td align="right">2,546,240</td>
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
<td align="right">112,780</td>
<td align="right">64.8%</td>
<td align="right">84,980</td>
<td align="right">57.4%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,180</td>
<td align="right">35.2%</td>
<td align="right">63,094</td>
<td align="right">42.6%</td>
<td align="right">3.1%</td>
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
<td align="right">55,760</td>
<td align="right">49.4%</td>
<td align="right">18,800</td>
<td align="right">22.1%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,664</td>
<td align="right">13.9%</td>
<td align="right">19,793</td>
<td align="right">23.3%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,556</td>
<td align="right">24.4%</td>
<td align="right">32,287</td>
<td align="right">38.0%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,800</td>
<td align="right">12.2%</td>
<td align="right">14,100</td>
<td align="right">16.6%</td>
<td align="right">2.2%</td>
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
<td align="right">543,338,315</td>
<td align="right">53.2%</td>
<td align="right">554,491,777</td>
<td align="right">53.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">478,394,493</td>
<td align="right">46.8%</td>
<td align="right">484,422,429</td>
<td align="right">46.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,580,605</td>
<td align="right">0.3%</td>
<td align="right">2,601,593</td>
<td align="right">0.3%</td>
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
<td align="right">194,318</td>
<td align="right">66.8%</td>
<td align="right">213,153</td>
<td align="right">67.9%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">96,752</td>
<td align="right">33.2%</td>
<td align="right">100,883</td>
<td align="right">32.1%</td>
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
<td align="left">set</td>
<td align="right">10,024</td>
<td align="right">5.2%</td>
<td align="right">18,160</td>
<td align="right">8.5%</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">817</td>
<td align="right">0.4%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">5,240</td>
<td align="right">2.5%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,120</td>
<td align="right">2.6%</td>
<td align="right">5,980</td>
<td align="right">2.8%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,770</td>
<td align="right">17.9%</td>
<td align="right">40,133</td>
<td align="right">18.8%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,400</td>
<td align="right">1.7%</td>
<td align="right">3,800</td>
<td align="right">1.8%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">7,039</td>
<td align="right">3.3%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,164</td>
<td align="right">5.7%</td>
<td align="right">11,964</td>
<td align="right">5.6%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,500</td>
<td align="right">3.3%</td>
<td align="right">6,920</td>
<td align="right">3.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">54.0%</td>
<td align="right">105,820</td>
<td align="right">49.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,800</td>
<td align="right">2.0%</td>
<td align="right">3,800</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,440</td>
<td align="right">1.3%</td>
<td align="right">2,440</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">1,479,094,093</td>
<td align="right">8.4%</td>
<td align="right">1,034,052,271</td>
<td align="right">6.4%</td>
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
<td align="right">16,126,302,816</td>
<td align="right">91.6%</td>
<td align="right">15,084,189,364</td>
<td align="right">93.5%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">410,411,827</td>
<td align="right">2.3%</td>
<td align="right">416,591,139</td>
<td align="right">2.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">304,720</td>
<td align="right">0.0%</td>
<td align="right">303,840</td>
<td align="right">0.0%</td>
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
<td align="right">956,989</td>
<td align="right">10.3%</td>
<td align="right">887,382</td>
<td align="right">9.4%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,357,405</td>
<td align="right">89.7%</td>
<td align="right">8,556,944</td>
<td align="right">90.6%</td>
<td align="right">2.4%</td>
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
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.3%</td>
<td align="right">3,308</td>
<td align="right">0.4%</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,380</td>
<td align="right">0.6%</td>
<td align="right">7,660</td>
<td align="right">0.9%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">259,802</td>
<td align="right">27.1%</td>
<td align="right">162,663</td>
<td align="right">18.3%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,552</td>
<td align="right">0.6%</td>
<td align="right">6,772</td>
<td align="right">0.8%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,866</td>
<td align="right">9.2%</td>
<td align="right">105,758</td>
<td align="right">11.9%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,671</td>
<td align="right">1.8%</td>
<td align="right">19,143</td>
<td align="right">2.2%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,880</td>
<td align="right">0.3%</td>
<td align="right">3,080</td>
<td align="right">0.3%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">163,711</td>
<td align="right">17.1%</td>
<td align="right">172,140</td>
<td align="right">19.4%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">27,080</td>
<td align="right">2.8%</td>
<td align="right">27,940</td>
<td align="right">3.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,107</td>
<td align="right">9.3%</td>
<td align="right">91,039</td>
<td align="right">10.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,420</td>
<td align="right">1.5%</td>
<td align="right">14,700</td>
<td align="right">1.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,240</td>
<td align="right">2.1%</td>
<td align="right">20,624</td>
<td align="right">2.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">76,344</td>
<td align="right">8.0%</td>
<td align="right">77,379</td>
<td align="right">8.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,400</td>
<td align="right">1.6%</td>
<td align="right">15,484</td>
<td align="right">1.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">157,136</td>
<td align="right">16.4%</td>
<td align="right">157,432</td>
<td align="right">17.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">property</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">11,380</td>
<td align="right">0.0%</td>
<td align="right">9,860</td>
<td align="right">0.0%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,358,940,567</td>
<td align="right">99.6%</td>
<td align="right">4,959,326,310</td>
<td align="right">99.6%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">442,621</td>
<td align="right">0.0%</td>
<td align="right">422,309</td>
<td align="right">0.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,326,260</td>
<td align="right">0.4%</td>
<td align="right">20,362,830</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
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
<td align="right">465,113</td>
<td align="right">100.0%</td>
<td align="right">520,634</td>
<td align="right">100.0%</td>
<td align="right">11.9%</td>
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
<td align="right">7,544</td>
<td align="right">0.0%</td>
<td align="right">8,443</td>
<td align="right">0.0%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">84,323,830</td>
<td align="right">100.0%</td>
<td align="right">86,857,380</td>
<td align="right">100.0%</td>
<td align="right">3.0%</td>
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
<td align="right">7,521</td>
<td align="right">100.0%</td>
<td align="right">8,460</td>
<td align="right">100.0%</td>
<td align="right">12.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
<td align="right">27,720</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,365,460</td>
<td align="right">18.1%</td>
<td align="right">173,884,735</td>
<td align="right">18.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,230,852</td>
<td align="right">81.9%</td>
<td align="right">786,852,333</td>
<td align="right">81.9%</td>
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
<td align="left">Success</td>
<td align="right">5,440</td>
<td align="right">8.3%</td>
<td align="right">7,074</td>
<td align="right">10.3%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,760</td>
<td align="right">91.7%</td>
<td align="right">61,888</td>
<td align="right">89.7%</td>
<td align="right">3.6%</td>
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
<td align="right">14,240</td>
<td align="right">23.8%</td>
<td align="right">16,128</td>
<td align="right">26.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">10,080</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">2,728,540,565</td>
<td align="right">93.4%</td>
<td align="right">2,456,831,739</td>
<td align="right">92.6%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">191,242,187</td>
<td align="right">6.5%</td>
<td align="right">193,134,361</td>
<td align="right">7.3%</td>
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
<td align="right">142,248,924</td>
<td align="right">4.9%</td>
<td align="right">143,220,240</td>
<td align="right">5.4%</td>
<td align="right">0.7%</td>
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
<td align="right">91,806</td>
<td align="right">3.2%</td>
<td align="right">100,168</td>
<td align="right">3.4%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,779,911</td>
<td align="right">96.8%</td>
<td align="right">2,819,867</td>
<td align="right">96.6%</td>
<td align="right">1.4%</td>
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
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">1,540</td>
<td align="right">1.5%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">10,900</td>
<td align="right">10.9%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,200</td>
<td align="right">3.5%</td>
<td align="right">4,540</td>
<td align="right">4.5%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,760</td>
<td align="right">5.2%</td>
<td align="right">5,820</td>
<td align="right">5.8%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,400</td>
<td align="right">7.0%</td>
<td align="right">6,820</td>
<td align="right">6.8%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,040</td>
<td align="right">15.3%</td>
<td align="right">14,720</td>
<td align="right">14.7%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,960</td>
<td align="right">5.4%</td>
<td align="right">5,080</td>
<td align="right">5.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,904</td>
<td align="right">8.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,726</td>
<td align="right">10.6%</td>
<td align="right">9,884</td>
<td align="right">9.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,540</td>
<td align="right">34.4%</td>
<td align="right">31,900</td>
<td align="right">31.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,443,237</td>
<td align="right">79.1%</td>
<td align="right">881,957,275</td>
<td align="right">79.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">231,780,857</td>
<td align="right">20.9%</td>
<td align="right">232,321,539</td>
<td align="right">20.8%</td>
<td align="right">0.2%</td>
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
<td align="right">2,900</td>
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
<td align="right">13,124</td>
<td align="right">11.6%</td>
<td align="right">16,721</td>
<td align="right">14.1%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99,801</td>
<td align="right">88.4%</td>
<td align="right">101,718</td>
<td align="right">85.9%</td>
<td align="right">1.9%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">7,521</td>
<td align="right">7.5%</td>
<td align="right">8,665</td>
<td align="right">8.5%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,560</td>
<td align="right">39.6%</td>
<td align="right">40,313</td>
<td align="right">39.6%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">43,440</td>
<td align="right">42.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,480</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,340</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">239,107,860</td>
<td align="right">3.8%</td>
<td align="right">207,684,837</td>
<td align="right">3.5%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,118,826,919</td>
<td align="right">96.2%</td>
<td align="right">5,742,431,359</td>
<td align="right">96.5%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,155,343</td>
<td align="right">0.8%</td>
<td align="right">53,290,353</td>
<td align="right">0.9%</td>
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
<td align="right">228,817</td>
<td align="right">16.1%</td>
<td align="right">239,279</td>
<td align="right">16.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,196,603</td>
<td align="right">83.9%</td>
<td align="right">1,217,570</td>
<td align="right">83.6%</td>
<td align="right">1.8%</td>
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
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.6%</td>
<td align="right">2,334</td>
<td align="right">1.0%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">14,820</td>
<td align="right">6.5%</td>
<td align="right">20,816</td>
<td align="right">8.7%</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,898</td>
<td align="right">5.2%</td>
<td align="right">14,473</td>
<td align="right">6.0%</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">36,731</td>
<td align="right">16.1%</td>
<td align="right">31,873</td>
<td align="right">13.3%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,246</td>
<td align="right">5.8%</td>
<td align="right">14,726</td>
<td align="right">6.2%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,148</td>
<td align="right">2.2%</td>
<td align="right">5,381</td>
<td align="right">2.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,323</td>
<td align="right">35.5%</td>
<td align="right">84,167</td>
<td align="right">35.2%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,245</td>
<td align="right">24.1%</td>
<td align="right">56,343</td>
<td align="right">23.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">7,806</td>
<td align="right">3.4%</td>
<td align="right">7,826</td>
<td align="right">3.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">194,151</td>
<td align="right">0.0%</td>
<td align="right">199,557</td>
<td align="right">0.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,566,172,140</td>
<td align="right">100.0%</td>
<td align="right">1,536,018,433</td>
<td align="right">100.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">1,856</td>
<td align="right">5.8%</td>
<td align="right">2,093</td>
<td align="right">6.0%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,172</td>
<td align="right">94.2%</td>
<td align="right">32,944</td>
<td align="right">94.0%</td>
<td align="right">9.2%</td>
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
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">500</td>
<td align="right">23.9%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,216</td>
<td align="right">65.5%</td>
<td align="right">1,213</td>
<td align="right">58.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">380</td>
<td align="right">18.2%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,000,317,538</td>
<td align="right">9.9%</td>
<td align="right">9,304,843,576</td>
<td align="right">9.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">907,927,721</td>
<td align="right">0.8%</td>
<td align="right">837,031,242</td>
<td align="right">0.8%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">38,360,497,452</td>
<td align="right">34.4%</td>
<td align="right">35,754,928,859</td>
<td align="right">34.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">61,198,174,157</td>
<td align="right">54.9%</td>
<td align="right">57,445,827,670</td>
<td align="right">55.6%</td>
<td align="right">-6.1%</td>
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
<td align="right">1,479,094,093</td>
<td align="right">30.1%</td>
<td align="right">1,034,052,271</td>
<td align="right">24.6%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">736,690,601</td>
<td align="right">15.0%</td>
<td align="right">621,818,570</td>
<td align="right">14.8%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">239,107,860</td>
<td align="right">4.9%</td>
<td align="right">207,684,837</td>
<td align="right">4.9%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">664,262,051</td>
<td align="right">13.5%</td>
<td align="right">673,907,791</td>
<td align="right">16.0%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">391,720,734</td>
<td align="right">8.0%</td>
<td align="right">396,658,278</td>
<td align="right">9.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">478,394,493</td>
<td align="right">9.7%</td>
<td align="right">484,422,429</td>
<td align="right">11.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">191,242,187</td>
<td align="right">3.9%</td>
<td align="right">193,134,361</td>
<td align="right">4.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,365,460</td>
<td align="right">3.5%</td>
<td align="right">173,884,735</td>
<td align="right">4.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,780,857</td>
<td align="right">4.7%</td>
<td align="right">232,321,539</td>
<td align="right">5.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,130,775</td>
<td align="right">4.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">106,786,603</td>
<td align="right">2.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">170,634,972</td>
<td align="right">17.3%</td>
<td align="right">175,124,055</td>
<td align="right">20.9%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">49,803,765</td>
<td align="right">5.1%</td>
<td align="right">50,577,096</td>
<td align="right">6.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">25,169,778</td>
<td align="right">2.6%</td>
<td align="right">24,903,850</td>
<td align="right">3.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,935</td>
<td align="right">2.8%</td>
<td align="right">27,599,183</td>
<td align="right">3.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">126,596,000</td>
<td align="right">12.8%</td>
<td align="right">126,962,565</td>
<td align="right">15.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">100,345,564</td>
<td align="right">10.2%</td>
<td align="right">100,144,718</td>
<td align="right">12.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,362,100</td>
<td align="right">3.6%</td>
<td align="right">35,363,774</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">117,522,540</td>
<td align="right">11.9%</td>
<td align="right">117,527,266</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,899,813</td>
<td align="right">7.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,899,813</td>
<td align="right">7.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,664,769</td>
<td align="right">3.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,528,534</td>
<td align="right">2.9%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,096,282</td>
<td align="right">0.4%</td>
<td align="right">36,876,063</td>
<td align="right">0.4%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,872,444</td>
<td align="right">6.3%</td>
<td align="right">477,012,913</td>
<td align="right">5.6%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,775,303,610</td>
<td align="right">20.3%</td>
<td align="right">1,582,840,424</td>
<td align="right">18.6%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,779,750,110</td>
<td align="right">20.4%</td>
<td align="right">1,587,288,624</td>
<td align="right">18.6%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,640,861,467</td>
<td align="right">30.2%</td>
<td align="right">2,449,854,827</td>
<td align="right">28.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,640,861,467</td>
<td align="right">30.2%</td>
<td align="right">2,449,854,827</td>
<td align="right">28.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,800</td>
<td align="right">0.0%</td>
<td align="right">29,840</td>
<td align="right">0.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,972,083,508</td>
<td align="right">79.8%</td>
<td align="right">6,762,195,980</td>
<td align="right">79.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,038,261</td>
<td align="right">3.8%</td>
<td align="right">340,709,171</td>
<td align="right">4.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,578,342</td>
<td align="right">1.0%</td>
<td align="right">86,053,923</td>
<td align="right">1.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,111</td>
<td align="right">2.0%</td>
<td align="right">176,995,216</td>
<td align="right">2.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,091,082,677</td>
<td align="right">69.8%</td>
<td align="right">6,075,725,669</td>
<td align="right">71.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">861,111,357</td>
<td align="right">9.9%</td>
<td align="right">862,566,203</td>
<td align="right">10.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,700</td>
<td align="right">0.1%</td>
<td align="right">4,418,360</td>
<td align="right">0.1%</td>
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
<td align="left">Method cache hits</td>
<td align="right">3,230,443,123</td>
<td align="right"></td>
<td align="right">2,846,704,957</td>
<td align="right"></td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,911,832</td>
<td align="right"></td>
<td align="right">10,678,594</td>
<td align="right"></td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,878,000</td>
<td align="right"></td>
<td align="right">174,316,822</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">50,137,239,435</td>
<td align="right">35.2%</td>
<td align="right">46,790,078,522</td>
<td align="right">33.8%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">66,136,859,256</td>
<td align="right">40.1%</td>
<td align="right">62,440,437,650</td>
<td align="right">38.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,933,122</td>
<td align="right">0.1%</td>
<td align="right">15,711,348</td>
<td align="right">0.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">74,151,051</td>
<td align="right"></td>
<td align="right">76,047,698</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">65,219,439</td>
<td align="right"></td>
<td align="right">66,357,398</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,844,456,546</td>
<td align="right">52.0%</td>
<td align="right">13,014,362,078</td>
<td align="right">52.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,735,401,509</td>
<td align="right">51.5%</td>
<td align="right">12,903,350,332</td>
<td align="right">52.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,121,915</td>
<td align="right">0.4%</td>
<td align="right">95,300,398</td>
<td align="right">0.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,546,692,272</td>
<td align="right"></td>
<td align="right">13,710,589,234</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,865,518,451</td>
<td align="right">48.0%</td>
<td align="right">11,749,198,519</td>
<td align="right">47.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,867,434,592</td>
<td align="right"></td>
<td align="right">11,751,209,239</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,578,511,856</td>
<td align="right"></td>
<td align="right">4,552,630,889</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,098,248,711</td>
<td align="right">64.8%</td>
<td align="right">91,769,249,728</td>
<td align="right">66.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,920</td>
<td align="right">0.1%</td>
<td align="right">128,160</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">98,933,743,011</td>
<td align="right">59.9%</td>
<td align="right">98,830,321,759</td>
<td align="right">61.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,140</td>
<td align="right">2.1%</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
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
<td align="right">115,332,980</td>
<td align="right">19,562,596,799</td>
<td align="right">0</td>
<td align="right">116,207,087</td>
<td align="right">19,746,699,288</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,691,896</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,691,360</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">131,223</td>
<td align="right">13.3%</td>
<td align="right">137,769</td>
<td align="right">13.7%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">988,822</td>
<td align="right"></td>
<td align="right">1,005,697</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">543,379</td>
<td align="right">55.0%</td>
<td align="right">552,175</td>
<td align="right">54.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">97,919</td>
<td align="right">9.9%</td>
<td align="right">99,204</td>
<td align="right">9.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">857,599</td>
<td align="right">86.7%</td>
<td align="right">867,928</td>
<td align="right">86.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,348</td>
<td align="right">0.1%</td>
<td align="right">1,340</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,211,242,670</td>
<td align="right"></td>
<td align="right">7,239,951,641</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">262,624,110,886</td>
<td align="right">3,641.9%</td>
<td align="right">263,037,664,166</td>
<td align="right">3,633.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">13,084</td>
<td align="right">1.3%</td>
<td align="right">13,072</td>
<td align="right">1.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,130</td>
<td align="right">5.4%</td>
<td align="right">7,129</td>
<td align="right">5.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,740</td>
<td align="right">0.2%</td>
<td align="right">1,740</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">115,560</td>
<td align="right">88.1%</td>
<td align="right">122,064</td>
<td align="right">88.6%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">131,223</td>
<td align="right"></td>
<td align="right">137,769</td>
<td align="right"></td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,530</td>
<td align="right">1.9%</td>
<td align="right">2,566</td>
<td align="right">1.9%</td>
<td align="right">1.4%</td>
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
<td align="right">5,402</td>
<td align="right">4.1%</td>
<td align="right">5,599</td>
<td align="right">4.1%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,277</td>
<td align="right">13.9%</td>
<td align="right">19,015</td>
<td align="right">13.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">39,279</td>
<td align="right">29.9%</td>
<td align="right">42,068</td>
<td align="right">30.5%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">33,083</td>
<td align="right">25.2%</td>
<td align="right">35,077</td>
<td align="right">25.5%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22,827</td>
<td align="right">17.4%</td>
<td align="right">23,749</td>
<td align="right">17.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">10,155</td>
<td align="right">7.7%</td>
<td align="right">10,201</td>
<td align="right">7.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,040</td>
<td align="right">1.6%</td>
<td align="right">1,920</td>
<td align="right">1.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">-12.5%</td>
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
<td align="right">4,382</td>
<td align="right">3.3%</td>
<td align="right">4,539</td>
<td align="right">3.3%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">11,763</td>
<td align="right">9.0%</td>
<td align="right">12,188</td>
<td align="right">8.8%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">27,489</td>
<td align="right">20.9%</td>
<td align="right">29,078</td>
<td align="right">21.1%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">38,226</td>
<td align="right">29.1%</td>
<td align="right">40,798</td>
<td align="right">29.6%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">20,915</td>
<td align="right">15.9%</td>
<td align="right">22,494</td>
<td align="right">16.3%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,265</td>
<td align="right">7.1%</td>
<td align="right">9,587</td>
<td align="right">7.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,080</td>
<td align="right">2.3%</td>
<td align="right">3,020</td>
<td align="right">2.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">440</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">-18.2%</td>
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
<td align="left">_BUILD_SET</td>
<td align="right">12,100</td>
<td align="right">248,204</td>
<td align="right">1,951.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">35,740</td>
<td align="right">122,604</td>
<td align="right">243.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,333,178</td>
<td align="right">1,505,654</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,132,141</td>
<td align="right">8,204,072</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">670,094</td>
<td align="right">757,419</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">9,784,600</td>
<td align="right">8,520,220</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,362,260</td>
<td align="right">10,098,940</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">854,890</td>
<td align="right">942,227</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,517,400</td>
<td align="right">8,781,725</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,789,164</td>
<td align="right">3,874,822</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,723,584</td>
<td align="right">164,289,450</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">96,901,080</td>
<td align="right">98,727,884</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">97,177,120</td>
<td align="right">99,003,924</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">15,107,175</td>
<td align="right">15,386,106</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">308,871,701</td>
<td align="right">314,540,724</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,956,780</td>
<td align="right">3,010,084</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">46,456,136</td>
<td align="right">47,249,934</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,615</td>
<td align="right">98,888,447</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,278,715</td>
<td align="right">98,936,547</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">996,372,905</td>
<td align="right">1,013,207,024</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">205,429,367</td>
<td align="right">208,889,096</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">233,819,452</td>
<td align="right">237,369,172</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,406,242</td>
<td align="right">32,823,088</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,437,990</td>
<td align="right">238,330,889</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">68,289,453</td>
<td align="right">69,069,983</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,836,780</td>
<td align="right">4,890,064</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,147,528</td>
<td align="right">123,491,288</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,262,247</td>
<td align="right">81,010,466</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">354,962,547</td>
<td align="right">358,138,714</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">60,302,584</td>
<td align="right">59,766,083</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">499,109</td>
<td align="right">502,506</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,104,193,187</td>
<td align="right">1,111,431,386</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,359,302,658</td>
<td align="right">2,374,536,971</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">250,493,419</td>
<td align="right">252,082,974</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">254,036,449</td>
<td align="right">255,625,989</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">78,391,777</td>
<td align="right">78,880,143</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">7,415,985</td>
<td align="right">7,462,134</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">400,743,113</td>
<td align="right">403,154,086</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">437,581,435</td>
<td align="right">440,189,866</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">394,411,976</td>
<td align="right">396,726,394</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">142,918,770</td>
<td align="right">143,752,710</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,283,160</td>
<td align="right">164,218,296</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,552,619</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,935,464</td>
<td align="right">134,205,226</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,935,464</td>
<td align="right">134,205,226</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">306,495,807</td>
<td align="right">308,133,654</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">861,026,751</td>
<td align="right">865,507,005</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,520,795,172</td>
<td align="right">1,528,642,547</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">248,476,840</td>
<td align="right">247,219,427</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">516,423,535</td>
<td align="right">519,031,966</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,340,460</td>
<td align="right">322,904,023</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">35,715,889</td>
<td align="right">35,888,663</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,203,446,715</td>
<td align="right">1,197,953,400</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">572,388,893</td>
<td align="right">574,933,067</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,429,543</td>
<td align="right">35,273,610</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,411,257,775</td>
<td align="right">1,417,453,795</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,684,160</td>
<td align="right">243,610,804</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">199,370,745</td>
<td align="right">198,507,669</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,177,720,645</td>
<td align="right">2,186,965,774</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,321,502,655</td>
<td align="right">1,316,046,649</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,211,242,670</td>
<td align="right">7,239,951,641</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,380,641,165</td>
<td align="right">6,405,642,199</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">95,061,121</td>
<td align="right">95,431,511</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,957,610</td>
<td align="right">97,328,481</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,105,803,627</td>
<td align="right">3,117,401,885</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">165,841,590</td>
<td align="right">166,456,803</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,603,875,517</td>
<td align="right">1,609,690,692</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">286,553,218</td>
<td align="right">287,580,732</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">867,724,010</td>
<td align="right">870,816,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,654,681,377</td>
<td align="right">6,678,330,808</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,515,904</td>
<td align="right">45,356,380</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,362,273</td>
<td align="right">94,692,189</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,537,818,002</td>
<td align="right">1,543,145,234</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">420,265,040</td>
<td align="right">421,673,215</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,342,662,415</td>
<td align="right">1,338,217,857</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,848,498,848</td>
<td align="right">6,870,698,849</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,990,747,242</td>
<td align="right">7,013,363,677</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,214,802</td>
<td align="right">733,543,964</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,889,630</td>
<td align="right">79,140,694</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">777,782,803</td>
<td align="right">780,244,181</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,320,123</td>
<td align="right">780,781,501</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">12,452,242</td>
<td align="right">12,489,515</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">12,452,242</td>
<td align="right">12,489,515</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">461,065,261</td>
<td align="right">462,421,879</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">33,368,439</td>
<td align="right">33,464,265</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,045,820,863</td>
<td align="right">1,048,816,023</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,375,876</td>
<td align="right">675,174,781</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">143,796,320</td>
<td align="right">144,163,186</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">897,922,126</td>
<td align="right">900,107,310</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">911,831,436</td>
<td align="right">909,645,626</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">556,583,723</td>
<td align="right">557,913,773</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,488,026,328</td>
<td align="right">2,493,743,701</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,543,438,088</td>
<td align="right">2,549,155,461</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,406,009</td>
<td align="right">700,838,924</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">899,577,392</td>
<td align="right">897,668,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">389,600,993</td>
<td align="right">390,416,403</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">390,828,253</td>
<td align="right">391,643,663</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,330,192,078</td>
<td align="right">2,325,549,521</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">18,879,869,009</td>
<td align="right">18,917,340,799</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">90,117,786</td>
<td align="right">90,296,254</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">128,618,840</td>
<td align="right">128,365,290</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">165,048,399</td>
<td align="right">165,371,814</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,460,090,064</td>
<td align="right">16,491,753,774</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,631,566,436</td>
<td align="right">4,640,231,862</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,291,659,480</td>
<td align="right">6,303,010,429</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">666,422,066</td>
<td align="right">665,222,755</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">940,090,988</td>
<td align="right">941,775,053</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">99,766,740</td>
<td align="right">99,928,654</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">100,009,360</td>
<td align="right">100,171,274</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">964,564,618</td>
<td align="right">965,925,073</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">980,458,373</td>
<td align="right">981,834,312</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,419,961,269</td>
<td align="right">10,434,430,925</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,361,633,980</td>
<td align="right">1,363,505,051</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,694,870</td>
<td align="right">131,860,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,890,010</td>
<td align="right">230,175,112</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,129,747,854</td>
<td align="right">2,132,385,202</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,695,310,561</td>
<td align="right">1,693,267,555</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">657,961,978</td>
<td align="right">658,728,603</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,826,209,283</td>
<td align="right">1,828,248,511</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,715,029</td>
<td align="right">90,812,250</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,200,118</td>
<td align="right">791,037,509</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,606,524,610</td>
<td align="right">1,608,216,497</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,328,428,633</td>
<td align="right">7,320,943,624</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">320,051,172</td>
<td align="right">320,369,994</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,028,963,598</td>
<td align="right">2,027,045,286</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">817,773,639</td>
<td align="right">818,540,801</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,286,545,079</td>
<td align="right">4,290,532,164</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,265,720</td>
<td align="right">4,269,615</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">993,787,842</td>
<td align="right">992,882,228</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">4,440,180</td>
<td align="right">4,444,075</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,465,522,141</td>
<td align="right">3,468,538,760</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,483,517</td>
<td align="right">395,804,491</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,632,963,041</td>
<td align="right">3,635,772,791</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,454,909</td>
<td align="right">122,541,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,905,920</td>
<td align="right">67,952,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,749,837,072</td>
<td align="right">1,748,701,633</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,003,339,786</td>
<td align="right">2,004,629,479</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,241,443,658</td>
<td align="right">3,243,465,673</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,732,197,404</td>
<td align="right">2,733,892,215</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,274,230,884</td>
<td align="right">2,275,633,894</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,251,841,933</td>
<td align="right">1,252,598,537</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,834,643,926</td>
<td align="right">1,833,565,663</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,138,039</td>
<td align="right">239,272,617</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,807,209,210</td>
<td align="right">1,808,208,525</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,363,880,589</td>
<td align="right">14,371,672,401</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,635,939,537</td>
<td align="right">3,637,897,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,588,852</td>
<td align="right">1,683,465,739</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,967,580</td>
<td align="right">2,969,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,235,451</td>
<td align="right">10,230,492</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,452,027,810</td>
<td align="right">3,453,546,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,334,900,733</td>
<td align="right">2,335,928,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">275,515,740</td>
<td align="right">275,396,061</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,130,395,872</td>
<td align="right">1,129,917,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,353,857,797</td>
<td align="right">1,354,361,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,274,471,200</td>
<td align="right">5,276,052,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,846,161,024</td>
<td align="right">3,845,073,532</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,606,577,763</td>
<td align="right">5,608,120,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,620,666,156</td>
<td align="right">1,621,099,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,079,486,944</td>
<td align="right">2,079,987,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,105,056,143</td>
<td align="right">1,104,849,686</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,892,932,275</td>
<td align="right">2,893,405,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,988,640</td>
<td align="right">61,996,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,160</td>
<td align="right">904,573,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,171,328</td>
<td align="right">114,158,167</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,501,153,882</td>
<td align="right">1,501,323,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">384,674,450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,652,240</td>
<td align="right">4,652,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,011,312,666</td>
<td align="right">2,011,485,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">186,425,960</td>
<td align="right">186,439,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">181,204,134</td>
<td align="right">181,215,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,758,812,116</td>
<td align="right">4,759,036,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,068,449</td>
<td align="right">645,091,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">92,546,175</td>
<td align="right">92,543,353</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,697,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">41,974,727</td>
<td align="right">41,973,549</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,930,020</td>
<td align="right">1,345,953,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,466,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,579,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,764,411</td>
<td align="right">68,765,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">276,625,710</td>
<td align="right">276,628,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">539,252,120</td>
<td align="right">539,255,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,993,760</td>
<td align="right">173,994,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,892,329,967</td>
<td align="right">1,892,338,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">644,040,854</td>
<td align="right">644,037,930</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,989,520</td>
<td align="right">60,989,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,726,886</td>
<td align="right">204,727,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,743,262</td>
<td align="right">10,743,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">68,309,217</td>
<td align="right">68,309,213</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,105,100</td>
<td align="right">533,105,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">122,205,777</td>
<td align="right">122,205,773</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,965,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,279,160</td>
<td align="right">110,279,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">59,644,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">54,628,640</td>
<td align="right">54,628,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,896,560</td>
<td align="right">53,896,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,394,280</td>
<td align="right">46,394,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,651,140</td>
<td align="right">5,651,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,636,040</td>
<td align="right">5,636,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,016,240</td>
<td align="right">3,016,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,713,220</td>
<td align="right">2,713,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,799,640</td>
<td align="right">1,799,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,225,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,760</td>
<td align="right">821,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">581,940</td>
<td align="right">581,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">375,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">39,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">78,400</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,160</td>
<td align="right">1,220</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">35,560</td>
<td align="right">36,746</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,859</td>
<td align="right">45,786</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,800</td>
<td align="right">3,840</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">157,107</td>
<td align="right">157,804</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">819</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">31,680</td>
<td align="right">31,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">620</td>
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
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">420</td>
<td align="right">460</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,106</td>
<td align="right">1,104</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,106</td>
<td align="right">1,104</td>
<td align="right">-0.2%</td>
</tr>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">1,780</td>
<td align="right">1,820</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-04
