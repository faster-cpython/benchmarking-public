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
<td align="right">33,924,979</td>
<td align="right">7,388,641</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">211,407</td>
<td align="right">372,617</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,351,465</td>
<td align="right">1,187,330</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,111,844</td>
<td align="right">3,491,475</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,898,928</td>
<td align="right">797,333</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,285,045</td>
<td align="right">1,031,336</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,689,896</td>
<td align="right">1,759,044</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,987,646</td>
<td align="right">6,751,803</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,511,373</td>
<td align="right">787,116</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,692,506</td>
<td align="right">5,125,169</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,349,157</td>
<td align="right">10,534,432</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,373,126</td>
<td align="right">750,984</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,426,478</td>
<td align="right">1,337,950</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,440,042</td>
<td align="right">3,056,915</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,918,150</td>
<td align="right">1,680,701</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,278,982</td>
<td align="right">1,952,789</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">346,266</td>
<td align="right">216,234</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,098,903</td>
<td align="right">7,000,581</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,296,253</td>
<td align="right">11,070,690</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,939,188</td>
<td align="right">11,060,167</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,509,494</td>
<td align="right">5,593,181</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">446,796</td>
<td align="right">303,219</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,924,504</td>
<td align="right">2,005,967</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,528,684</td>
<td align="right">14,572,704</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,278,150</td>
<td align="right">5,898,141</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,943,100</td>
<td align="right">9,256,627</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,518,045</td>
<td align="right">37,884,832</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,439,804</td>
<td align="right">15,220,173</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,980,792</td>
<td align="right">110,761,141</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,875,915</td>
<td align="right">37,810,259</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,209</td>
<td align="right">1,150,677</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">125,721,012</td>
<td align="right">98,759,872</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">44,317,650</td>
<td align="right">34,827,655</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,789,697</td>
<td align="right">2,197,008</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,889,436</td>
<td align="right">13,372,885</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,221,621</td>
<td align="right">14,508,125</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,035,261</td>
<td align="right">33,066,457</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">109,819,796</td>
<td align="right">89,002,312</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,707,931</td>
<td align="right">3,851,927</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,082,964</td>
<td align="right">3,350,969</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">118,090,796</td>
<td align="right">97,159,771</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,282,521</td>
<td align="right">13,472,344</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,669,072</td>
<td align="right">14,665,208</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">36,185,419</td>
<td align="right">30,036,911</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">118,505,755</td>
<td align="right">99,397,335</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">167,220,394</td>
<td align="right">140,774,922</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,518,120</td>
<td align="right">10,545,940</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,622,335</td>
<td align="right">3,912,388</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">29,947,506</td>
<td align="right">25,599,085</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,362,047</td>
<td align="right">14,865,462</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">577,135,905</td>
<td align="right">496,222,557</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,336,739</td>
<td align="right">1,152,857</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,077,295</td>
<td align="right">19,988,705</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,020,073</td>
<td align="right">1,750,354</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,192,267</td>
<td align="right">4,511,875</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,041,517</td>
<td align="right">8,746,519</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,638,175</td>
<td align="right">39,858,729</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,917,957</td>
<td align="right">8,699,072</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,312,636</td>
<td align="right">1,473,686</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">767,135</td>
<td align="right">674,458</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">130,863,898</td>
<td align="right">116,163,523</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,446,563</td>
<td align="right">8,401,650</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,204,764</td>
<td align="right">12,638,971</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,687,028</td>
<td align="right">1,508,983</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,092,660</td>
<td align="right">25,203,003</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,569,260</td>
<td align="right">5,001,599</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,245,252</td>
<td align="right">8,305,179</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,476,763</td>
<td align="right">45,540,682</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,990,107</td>
<td align="right">9,019,425</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,572,446</td>
<td align="right">5,045,621</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,408</td>
<td align="right">2,488,336</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,852,690</td>
<td align="right">9,989,690</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">162,621,943</td>
<td align="right">149,990,832</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">135,770,306</td>
<td align="right">125,572,121</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,960,751</td>
<td align="right">15,734,369</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">138,347,591</td>
<td align="right">128,387,234</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,468,896</td>
<td align="right">4,163,468</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,645,765</td>
<td align="right">6,196,939</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">85,685,554</td>
<td align="right">80,577,413</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,892,956</td>
<td align="right">70,046,566</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">712,407</td>
<td align="right">676,446</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,367,022</td>
<td align="right">4,180,210</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,942,183</td>
<td align="right">56,673,463</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,650,661</td>
<td align="right">3,521,831</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,115,634</td>
<td align="right">36,913,846</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,220</td>
<td align="right">229,166</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">523,767</td>
<td align="right">535,473</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,692,100</td>
<td align="right">1,656,052</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,498,151</td>
<td align="right">21,220,446</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">862,184</td>
<td align="right">851,305</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,044,600</td>
<td align="right">3,019,451</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,458,211</td>
<td align="right">6,482,054</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,002</td>
<td align="right">460,729</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,577,003</td>
<td align="right">4,569,949</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,480,739</td>
<td align="right">2,479,896</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,957</td>
<td align="right">21,950</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,588</td>
<td align="right">1,280,428</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">69,141</td>
<td align="right">69,134</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">640,636</td>
<td align="right">640,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,076,052</td>
<td align="right">155,087,758</td>
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
<td align="right">9,235,316</td>
<td align="right">46.0%</td>
<td align="right">8,295,454</td>
<td align="right">43.4%</td>
<td align="right">-10.2%</td>
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
<td align="right">56.6%</td>
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
<td align="right">9,347</td>
<td align="right">94.1%</td>
<td align="right">9,136</td>
<td align="right">93.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">589</td>
<td align="right">5.9%</td>
<td align="right">589</td>
<td align="right">6.1%</td>
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
<td align="right">805</td>
<td align="right">8.8%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">127</td>
<td align="right">1.4%</td>
<td align="right">129</td>
<td align="right">1.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">36.4%</td>
<td align="right">3,402</td>
<td align="right">37.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,401</td>
<td align="right">25.7%</td>
<td align="right">2,401</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">16.0%</td>
<td align="right">1,492</td>
<td align="right">16.3%</td>
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
<td align="right">2,488,336</td>
<td align="right">100.0%</td>
<td align="right">-8.9%</td>
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
<td align="right">3,643,816</td>
<td align="right">9.5%</td>
<td align="right">3,514,816</td>
<td align="right">9.2%</td>
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
<td align="right">2,366,702</td>
<td align="right">6.1%</td>
<td align="right">2,365,258</td>
<td align="right">6.2%</td>
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
<td align="right">32,466,866</td>
<td align="right">84.4%</td>
<td align="right">32,467,235</td>
<td align="right">84.7%</td>
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
<td align="right">5,612</td>
<td align="right">10.9%</td>
<td align="right">5,782</td>
<td align="right">11.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,741</td>
<td align="right">89.1%</td>
<td align="right">45,698</td>
<td align="right">88.8%</td>
<td align="right">-0.1%</td>
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
<td align="left">out of range</td>
<td align="right">2,655</td>
<td align="right">47.3%</td>
<td align="right">2,847</td>
<td align="right">49.2%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">823</td>
<td align="right">14.7%</td>
<td align="right">801</td>
<td align="right">13.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,252</td>
<td align="right">22.3%</td>
<td align="right">1,252</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.5%</td>
<td align="right">307</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.4%</td>
<td align="right">245</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.2%</td>
<td align="right">238</td>
<td align="right">4.1%</td>
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
<td align="right">1,820,425</td>
<td align="right">0.8%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">239,290,933</td>
<td align="right">99.2%</td>
<td align="right">239,374,646</td>
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
<td align="right">44,850</td>
<td align="right">0.0%</td>
<td align="right">44,846</td>
<td align="right">0.0%</td>
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
<td align="right">61,226</td>
<td align="right">99.8%</td>
<td align="right">60,121</td>
<td align="right">99.8%</td>
<td align="right">-1.8%</td>
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
<td align="right">636,750</td>
<td align="right">5.5%</td>
<td align="right">636,805</td>
<td align="right">5.5%</td>
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
<td align="right">2,666</td>
<td align="right">66.4%</td>
<td align="right">2,668</td>
<td align="right">66.4%</td>
<td align="right">0.1%</td>
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
<td align="right">102</td>
<td align="right">3.8%</td>
<td align="right">104</td>
<td align="right">3.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,804</td>
<td align="right">67.7%</td>
<td align="right">1,804</td>
<td align="right">67.6%</td>
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
<td align="right">4,361,477</td>
<td align="right">27.1%</td>
<td align="right">4,174,729</td>
<td align="right">26.2%</td>
<td align="right">-4.3%</td>
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
<td align="right">73.7%</td>
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
<td align="right">4,953</td>
<td align="right">90.4%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,447</td>
<td align="right">29.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,172</td>
<td align="right">43.3%</td>
<td align="right">2,151</td>
<td align="right">43.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">733</td>
<td align="right">14.6%</td>
<td align="right">733</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">622</td>
<td align="right">12.4%</td>
<td align="right">622</td>
<td align="right">12.6%</td>
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
<td align="right">9,686,388</td>
<td align="right">9.2%</td>
<td align="right">5,120,178</td>
<td align="right">6.1%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,516,328</td>
<td align="right">4.3%</td>
<td align="right">2,653,462</td>
<td align="right">3.2%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">91,350,872</td>
<td align="right">86.5%</td>
<td align="right">76,438,913</td>
<td align="right">90.8%</td>
<td align="right">-16.3%</td>
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
<td align="right">85,867</td>
<td align="right">94.0%</td>
<td align="right">50,704</td>
<td align="right">92.1%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,482</td>
<td align="right">6.0%</td>
<td align="right">4,355</td>
<td align="right">7.9%</td>
<td align="right">-20.6%</td>
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
<td align="right">4.3%</td>
<td align="right">106</td>
<td align="right">2.4%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">465</td>
<td align="right">8.5%</td>
<td align="right">294</td>
<td align="right">6.8%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">710</td>
<td align="right">13.0%</td>
<td align="right">496</td>
<td align="right">11.4%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.4%</td>
<td align="right">267</td>
<td align="right">6.1%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,229</td>
<td align="right">22.4%</td>
<td align="right">935</td>
<td align="right">21.5%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,547</td>
<td align="right">28.2%</td>
<td align="right">1,311</td>
<td align="right">30.1%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.6%</td>
<td align="right">469</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">5.0%</td>
<td align="right">272</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.8%</td>
<td align="right">97</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.1%</td>
<td align="right">61</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">47</td>
<td align="right">0.9%</td>
<td align="right">47</td>
<td align="right">1.1%</td>
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
<td align="right">98,745,535</td>
<td align="right">29.0%</td>
<td align="right">71,756,830</td>
<td align="right">23.2%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,620,897</td>
<td align="right">11.9%</td>
<td align="right">32,730,043</td>
<td align="right">10.6%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">200,207,603</td>
<td align="right">58.9%</td>
<td align="right">204,469,247</td>
<td align="right">66.1%</td>
<td align="right">2.1%</td>
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
<td align="right">2,264,774</td>
<td align="right">99.5%</td>
<td align="right">1,678,581</td>
<td align="right">99.4%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">10,878</td>
<td align="right">0.5%</td>
<td align="right">9,878</td>
<td align="right">0.6%</td>
<td align="right">-9.2%</td>
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
<td align="right">242</td>
<td align="right">2.4%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,856</td>
<td align="right">26.3%</td>
<td align="right">2,318</td>
<td align="right">23.5%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,294</td>
<td align="right">11.9%</td>
<td align="right">1,105</td>
<td align="right">11.2%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">636</td>
<td align="right">5.8%</td>
<td align="right">551</td>
<td align="right">5.6%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,203</td>
<td align="right">29.4%</td>
<td align="right">3,096</td>
<td align="right">31.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">9.1%</td>
<td align="right">993</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">5.9%</td>
<td align="right">645</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">1.1%</td>
<td align="right">115</td>
<td align="right">1.2%</td>
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
<td align="right">209,651,121</td>
<td align="right">100.0%</td>
<td align="right">195,606,546</td>
<td align="right">100.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,002</td>
<td align="right">0.0%</td>
<td align="right">2,998</td>
<td align="right">0.0%</td>
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
<td align="right">19,382</td>
<td align="right">100.0%</td>
<td align="right">19,379</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">10,026,604</td>
<td align="right">29.7%</td>
<td align="right">8,731,921</td>
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
<td align="right">9,609,037</td>
<td align="right">29.6%</td>
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
<td align="right">14,054,616</td>
<td align="right">41.7%</td>
<td align="right">14,064,332</td>
<td align="right">43.4%</td>
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
<td align="right">185,957</td>
<td align="right">95.2%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,146,815</td>
<td align="right">11.1%</td>
<td align="right">-22.8%</td>
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
<td align="right">88.8%</td>
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
<td align="right">3,388</td>
<td align="right">87.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">474</td>
<td align="right">12.3%</td>
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
<td align="right">255</td>
<td align="right">7.5%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,960</td>
<td align="right">85.2%</td>
<td align="right">2,960</td>
<td align="right">87.4%</td>
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
<td align="right">5,398,116</td>
<td align="right">2.9%</td>
<td align="right">3,647,929</td>
<td align="right">2.0%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,054,101</td>
<td align="right">7.5%</td>
<td align="right">12,540,086</td>
<td align="right">6.8%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,731,765</td>
<td align="right">89.6%</td>
<td align="right">169,244,875</td>
<td align="right">91.2%</td>
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
<td align="right">146,672</td>
<td align="right">58.1%</td>
<td align="right">94,915</td>
<td align="right">56.6%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105,785</td>
<td align="right">41.9%</td>
<td align="right">72,742</td>
<td align="right">43.4%</td>
<td align="right">-31.2%</td>
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
<td align="right">133,300</td>
<td align="right">90.9%</td>
<td align="right">81,543</td>
<td align="right">85.9%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,949</td>
<td align="right">6.8%</td>
<td align="right">9,949</td>
<td align="right">10.5%</td>
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
<td align="right">122,549,436</td>
<td align="right">3.6%</td>
<td align="right">91,875,649</td>
<td align="right">3.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">97,691,234</td>
<td align="right">2.9%</td>
<td align="right">80,455,026</td>
<td align="right">2.7%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,254,538,611</td>
<td align="right">37.2%</td>
<td align="right">1,079,942,172</td>
<td align="right">36.8%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,901,739,446</td>
<td align="right">56.3%</td>
<td align="right">1,679,712,362</td>
<td align="right">57.3%</td>
<td align="right">-11.7%</td>
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
<td align="right">9,686,388</td>
<td align="right">10.0%</td>
<td align="right">5,120,178</td>
<td align="right">6.4%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,261</td>
<td align="right">1.5%</td>
<td align="right">1,146,815</td>
<td align="right">1.4%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40,620,897</td>
<td align="right">41.9%</td>
<td align="right">32,730,043</td>
<td align="right">41.0%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,026,604</td>
<td align="right">10.3%</td>
<td align="right">8,731,921</td>
<td align="right">10.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,054,101</td>
<td align="right">14.5%</td>
<td align="right">12,540,086</td>
<td align="right">15.7%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,235,316</td>
<td align="right">9.5%</td>
<td align="right">8,295,454</td>
<td align="right">10.4%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,408</td>
<td align="right">2.8%</td>
<td align="right">2,488,336</td>
<td align="right">3.1%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,361,477</td>
<td align="right">4.5%</td>
<td align="right">4,174,729</td>
<td align="right">5.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,643,816</td>
<td align="right">3.8%</td>
<td align="right">3,514,816</td>
<td align="right">4.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">636,750</td>
<td align="right">0.7%</td>
<td align="right">636,805</td>
<td align="right">0.8%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,258,539</td>
<td align="right">1.8%</td>
<td align="right">1,326,578</td>
<td align="right">1.4%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,257,789</td>
<td align="right">1.8%</td>
<td align="right">1,326,884</td>
<td align="right">1.4%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">17,878,172</td>
<td align="right">14.6%</td>
<td align="right">10,990,910</td>
<td align="right">12.0%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,400,982</td>
<td align="right">3.6%</td>
<td align="right">2,805,198</td>
<td align="right">3.1%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,257,470</td>
<td align="right">11.6%</td>
<td align="right">10,122,237</td>
<td align="right">11.0%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,811,940</td>
<td align="right">39.0%</td>
<td align="right">35,158,785</td>
<td align="right">38.3%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,816</td>
<td align="right">6.3%</td>
<td align="right">5,713,302</td>
<td align="right">6.2%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,358,421</td>
<td align="right">8.5%</td>
<td align="right">9,142,453</td>
<td align="right">10.0%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,563,981</td>
<td align="right">7.8%</td>
<td align="right">9,554,066</td>
<td align="right">10.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,342,043</td>
<td align="right">1.9%</td>
<td align="right">2,340,599</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
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
<td align="right">629,182</td>
<td align="right">0.3%</td>
<td align="right">790,392</td>
<td align="right">0.4%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,557,641</td>
<td align="right">8.5%</td>
<td align="right">17,367,559</td>
<td align="right">7.9%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,691,329</td>
<td align="right">3.1%</td>
<td align="right">6,976,816</td>
<td align="right">3.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,650,024</td>
<td align="right">18.1%</td>
<td align="right">38,448,236</td>
<td align="right">17.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,651,747</td>
<td align="right">18.1%</td>
<td align="right">38,449,959</td>
<td align="right">17.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,280,929</td>
<td align="right">18.4%</td>
<td align="right">39,240,351</td>
<td align="right">17.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,280,929</td>
<td align="right">18.4%</td>
<td align="right">39,240,351</td>
<td align="right">17.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,884,048</td>
<td align="right">81.6%</td>
<td align="right">180,085,836</td>
<td align="right">82.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,029,757</td>
<td align="right">72.1%</td>
<td align="right">158,041,463</td>
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
<td align="right">1,127,051,925</td>
<td align="right">27.2%</td>
<td align="right">1,409,175,999</td>
<td align="right">32.5%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,268,561,963</td>
<td align="right">33.7%</td>
<td align="right">1,553,873,126</td>
<td align="right">39.6%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">390,146,242</td>
<td align="right">10.4%</td>
<td align="right">337,227,886</td>
<td align="right">8.6%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">706,154,039</td>
<td align="right">17.0%</td>
<td align="right">787,224,899</td>
<td align="right">18.2%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546,076,103</td>
<td align="right">13.2%</td>
<td align="right">485,062,217</td>
<td align="right">11.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,377,739,702</td>
<td align="right">36.6%</td>
<td align="right">1,252,578,348</td>
<td align="right">31.9%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,771,872,118</td>
<td align="right">42.7%</td>
<td align="right">1,650,487,564</td>
<td align="right">38.1%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">731,499,108</td>
<td align="right">19.4%</td>
<td align="right">777,728,805</td>
<td align="right">19.8%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,502,639</td>
<td align="right"></td>
<td align="right">1,595,509</td>
<td align="right"></td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">212,506,889</td>
<td align="right"></td>
<td align="right">205,345,852</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,887,867</td>
<td align="right"></td>
<td align="right">10,055,057</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,387,322</td>
<td align="right"></td>
<td align="right">8,461,613</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">156,261,461</td>
<td align="right"></td>
<td align="right">155,457,267</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">211,956,822</td>
<td align="right"></td>
<td align="right">212,539,752</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,425,946</td>
<td align="right">0.5%</td>
<td align="right">1,422,045</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">199,042,844</td>
<td align="right">70.0%</td>
<td align="right">199,586,449</td>
<td align="right">70.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">200,530,639</td>
<td align="right">70.5%</td>
<td align="right">201,070,343</td>
<td align="right">70.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,811,365</td>
<td align="right">29.5%</td>
<td align="right">83,859,166</td>
<td align="right">29.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,829,783</td>
<td align="right"></td>
<td align="right">83,860,990</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">13,427,078</td>
<td align="right">282,970,055</td>
<td align="right">18,933,312</td>
<td align="right">24,414,172</td>
<td align="right">6,279</td>
<td align="right">13,432,257</td>
<td align="right">282,850,651</td>
<td align="right">19,009,598</td>
<td align="right">24,524,107</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,044,234,226</td>
<td align="right">882.8%</td>
<td align="right">3,411,714,549</td>
<td align="right">909.4%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">231,562,934</td>
<td align="right"></td>
<td align="right">375,166,502</td>
<td align="right"></td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,714</td>
<td align="right">38.2%</td>
<td align="right">4,344</td>
<td align="right">16.8%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">15,745</td>
<td align="right">61.8%</td>
<td align="right">21,500</td>
<td align="right">83.2%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,256</td>
<td align="right">63.9%</td>
<td align="right">21,677</td>
<td align="right">83.9%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,459</td>
<td align="right"></td>
<td align="right">25,844</td>
<td align="right"></td>
<td align="right">1.5%</td>
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
<td align="right">22</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">9,693</td>
<td align="right">99.8%</td>
<td align="right">4,175</td>
<td align="right">96.1%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">9,714</td>
<td align="right"></td>
<td align="right">4,344</td>
<td align="right"></td>
<td align="right">-55.3%</td>
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
<td align="right">492</td>
<td align="right">5.1%</td>
<td align="right">303</td>
<td align="right">7.0%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,131</td>
<td align="right">21.9%</td>
<td align="right">1,027</td>
<td align="right">23.6%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,715</td>
<td align="right">48.5%</td>
<td align="right">1,741</td>
<td align="right">40.1%</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,103</td>
<td align="right">21.6%</td>
<td align="right">1,104</td>
<td align="right">25.4%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">273</td>
<td align="right">2.8%</td>
<td align="right">169</td>
<td align="right">3.9%</td>
<td align="right">-38.1%</td>
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
<td align="right">1.0%</td>
<td align="right">42 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,110</td>
<td align="right">21.7%</td>
<td align="right">565</td>
<td align="right">13.0%</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,543</td>
<td align="right">15.9%</td>
<td align="right">1,326</td>
<td align="right">30.5%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,170</td>
<td align="right">53.2%</td>
<td align="right">1,652</td>
<td align="right">38.0%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">744</td>
<td align="right">7.7%</td>
<td align="right">549</td>
<td align="right">12.6%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">126</td>
<td align="right">1.3%</td>
<td align="right">41</td>
<td align="right">0.9%</td>
<td align="right">-67.5%</td>
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
<td align="right">567,703</td>
<td align="right">1,351,573.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">248</td>
<td align="right">270,013</td>
<td align="right">108,776.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">248</td>
<td align="right">269,967</td>
<td align="right">108,757.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">6,699</td>
<td align="right">3,693,172</td>
<td align="right">55,030.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,982</td>
<td align="right">890,141</td>
<td align="right">44,811.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,932</td>
<td align="right">586,603</td>
<td align="right">30,262.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,484</td>
<td align="right">945,401</td>
<td align="right">17,139.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">30,883</td>
<td align="right">4,015,017</td>
<td align="right">12,900.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">148</td>
<td align="right">7,202</td>
<td align="right">4,766.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">148</td>
<td align="right">7,202</td>
<td align="right">4,766.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,029</td>
<td align="right">47,138</td>
<td align="right">4,481.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">57,898</td>
<td align="right">1,992,503</td>
<td align="right">3,341.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,713</td>
<td align="right">946,250</td>
<td align="right">3,314.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">102,057</td>
<td align="right">3,105,921</td>
<td align="right">2,943.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,699</td>
<td align="right">96,435</td>
<td align="right">2,507.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">149,480</td>
<td align="right">2,529,489</td>
<td align="right">1,592.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">166,784</td>
<td align="right">2,655,865</td>
<td align="right">1,492.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">206,769</td>
<td align="right">3,016,946</td>
<td align="right">1,359.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">535,808</td>
<td align="right">7,735,411</td>
<td align="right">1,343.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">46,705</td>
<td align="right">668,847</td>
<td align="right">1,332.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">292,063</td>
<td align="right">3,456,198</td>
<td align="right">1,083.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">292,063</td>
<td align="right">3,456,198</td>
<td align="right">1,083.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">101,867</td>
<td align="right">1,166,219</td>
<td align="right">1,044.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,205</td>
<td align="right">59,572</td>
<td align="right">860.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,205</td>
<td align="right">59,572</td>
<td align="right">860.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">21</td>
<td align="right">181</td>
<td align="right">761.9%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">21</td>
<td align="right">181</td>
<td align="right">761.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">919,419</td>
<td align="right">7,539,788</td>
<td align="right">720.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">24,643</td>
<td align="right">173,344</td>
<td align="right">603.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,817,637</td>
<td align="right">12,199,497</td>
<td align="right">571.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,371,778</td>
<td align="right">15,002,563</td>
<td align="right">532.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,376,533</td>
<td align="right">15,015,082</td>
<td align="right">531.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">680,257</td>
<td align="right">4,196,808</td>
<td align="right">516.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">204,011</td>
<td align="right">1,248,924</td>
<td align="right">512.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,493,160</td>
<td align="right">8,713,290</td>
<td align="right">483.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">147,548</td>
<td align="right">857,495</td>
<td align="right">481.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,267,932</td>
<td align="right">12,826,858</td>
<td align="right">465.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">218,043</td>
<td align="right">1,216,613</td>
<td align="right">458.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">424,610</td>
<td align="right">2,355,462</td>
<td align="right">454.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">54,977</td>
<td align="right">299,049</td>
<td align="right">444.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">101,682</td>
<td align="right">550,508</td>
<td align="right">441.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">701,232</td>
<td align="right">3,789,822</td>
<td align="right">440.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">942,316</td>
<td align="right">4,908,976</td>
<td align="right">420.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">125,638</td>
<td align="right">652,463</td>
<td align="right">419.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">268,013</td>
<td align="right">1,357,253</td>
<td align="right">406.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">180,863</td>
<td align="right">912,858</td>
<td align="right">404.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">617,217</td>
<td align="right">3,113,802</td>
<td align="right">404.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">617,217</td>
<td align="right">3,113,802</td>
<td align="right">404.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,480,214</td>
<td align="right">12,440,571</td>
<td align="right">401.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">231,521</td>
<td align="right">1,160,779</td>
<td align="right">401.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">125,610</td>
<td align="right">628,162</td>
<td align="right">400.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,169,332</td>
<td align="right">15,205,749</td>
<td align="right">379.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,349,189</td>
<td align="right">6,457,330</td>
<td align="right">378.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,800,215</td>
<td align="right">13,154,923</td>
<td align="right">369.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,085,351</td>
<td align="right">4,946,944</td>
<td align="right">355.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,568,558</td>
<td align="right">55,769,078</td>
<td align="right">343.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">54,901</td>
<td align="right">234,791</td>
<td align="right">327.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">54,540</td>
<td align="right">232,585</td>
<td align="right">326.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">268,850</td>
<td align="right">1,130,330</td>
<td align="right">320.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,807,776</td>
<td align="right">15,436,208</td>
<td align="right">305.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">774,096</td>
<td align="right">2,930,367</td>
<td align="right">278.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">997,615</td>
<td align="right">3,565,294</td>
<td align="right">257.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">322,605</td>
<td align="right">1,131,039</td>
<td align="right">250.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,054,548</td>
<td align="right">3,641,578</td>
<td align="right">245.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,205,003</td>
<td align="right">10,973,041</td>
<td align="right">242.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,318,570</td>
<td align="right">4,499,985</td>
<td align="right">241.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">319,786</td>
<td align="right">1,044,043</td>
<td align="right">226.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">319,786</td>
<td align="right">1,044,043</td>
<td align="right">226.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">381,356</td>
<td align="right">1,237,360</td>
<td align="right">224.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">665,922</td>
<td align="right">2,137,894</td>
<td align="right">221.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">16,317</td>
<td align="right">52,278</td>
<td align="right">220.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,871,754</td>
<td align="right">18,595,185</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,371,033</td>
<td align="right">38,816,524</td>
<td align="right">213.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,867,414</td>
<td align="right">11,842,960</td>
<td align="right">206.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">611,616</td>
<td align="right">1,849,065</td>
<td align="right">202.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">317,045</td>
<td align="right">942,657</td>
<td align="right">197.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">313,957</td>
<td align="right">923,793</td>
<td align="right">194.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,689</td>
<td align="right">519,135</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">632,053</td>
<td align="right">1,733,648</td>
<td align="right">174.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">113,836</td>
<td align="right">300,584</td>
<td align="right">164.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,763,392</td>
<td align="right">9,911,060</td>
<td align="right">163.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,444,291</td>
<td align="right">6,419,112</td>
<td align="right">162.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,450,429</td>
<td align="right">6,267,860</td>
<td align="right">155.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,229,751</td>
<td align="right">5,655,080</td>
<td align="right">153.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,751,724</td>
<td align="right">6,738,760</td>
<td align="right">144.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">471,444</td>
<td align="right">1,151,940</td>
<td align="right">144.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">78,557,635</td>
<td align="right">189,000,366</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,880,906</td>
<td align="right">11,519,760</td>
<td align="right">136.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,917,491</td>
<td align="right">11,268,269</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,412,860</td>
<td align="right">12,057,960</td>
<td align="right">122.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">486,948</td>
<td align="right">1,079,637</td>
<td align="right">121.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,481,858</td>
<td align="right">5,398,171</td>
<td align="right">117.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">929,929</td>
<td align="right">2,018,457</td>
<td align="right">117.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,909,299</td>
<td align="right">8,475,509</td>
<td align="right">116.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,465,911</td>
<td align="right">11,805,411</td>
<td align="right">116.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,242,039</td>
<td align="right">4,625,166</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,155,977</td>
<td align="right">2,374,862</td>
<td align="right">105.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,180,874</td>
<td align="right">2,291,574</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,310,902</td>
<td align="right">10,107,203</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">177,932,759</td>
<td align="right">301,015,695</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">236,443,840</td>
<td align="right">386,686,262</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">34,118,563</td>
<td align="right">55,634,430</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">231,562,934</td>
<td align="right">375,166,502</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">122,696,266</td>
<td align="right">197,590,164</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">34,988,466</td>
<td align="right">56,325,842</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">174,171,892</td>
<td align="right">274,553,888</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">44,966,392</td>
<td align="right">70,747,318</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">253,373</td>
<td align="right">396,950</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,165,568</td>
<td align="right">6,491,172</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">71,411,330</td>
<td align="right">110,845,507</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">252,680</td>
<td align="right">382,712</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">253,709</td>
<td align="right">383,741</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">35,797,261</td>
<td align="right">51,872,379</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">63,627,259</td>
<td align="right">90,846,329</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">50,666,545</td>
<td align="right">70,552,200</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">15,380,849</td>
<td align="right">21,160,295</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">49,464,468</td>
<td align="right">67,659,448</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">49,464,468</td>
<td align="right">67,659,448</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">22,162,198</td>
<td align="right">30,282,187</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">34,083,371</td>
<td align="right">46,218,523</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">139</td>
<td align="right">187</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">21,698,332</td>
<td align="right">28,915,558</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">95,467</td>
<td align="right">71,624</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">33,573,265</td>
<td align="right">40,353,479</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">35,792,582</td>
<td align="right">42,157,550</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,527,627</td>
<td align="right">63,325,806</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,584,539</td>
<td align="right">38,545,006</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">32,391,855</td>
<td align="right">36,448,848</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">33,366,496</td>
<td align="right">37,436,102</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">69,461,915</td>
<td align="right">77,632,434</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">33,500,969</td>
<td align="right">36,331,898</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">30,973,281</td>
<td align="right">33,242,001</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">20,509</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">20,509</td>
<td align="right">6.6%</td>
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
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">5,879,021</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">1,294,682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">1,201,042</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">305,428</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">277,506</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">277,506</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">160,092</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">120,897</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right"></td>
<td align="right">92,736</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">16,338</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">10,663</td>
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
<td align="right">170</td>
<td align="right">191</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
Stats gathered on: 2024-12-11