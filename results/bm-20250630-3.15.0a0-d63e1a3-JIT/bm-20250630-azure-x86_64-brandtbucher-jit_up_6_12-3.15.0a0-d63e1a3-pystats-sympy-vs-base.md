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
<td align="left">NOT_TAKEN</td>
<td align="right">473,633</td>
<td align="right">2,909,473</td>
<td align="right">514.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">187,761</td>
<td align="right">83,832</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">27,729,303</td>
<td align="right">37,974,194</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,984,689</td>
<td align="right">1,906,576</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">11,696,439</td>
<td align="right">7,472,357</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,775,686</td>
<td align="right">1,819,074</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">214,773</td>
<td align="right">145,303</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,054,715</td>
<td align="right">4,177,317</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">63,696,893</td>
<td align="right">48,935,400</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,968,518</td>
<td align="right">1,575,465</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,762,956</td>
<td align="right">2,234,190</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">2,103</td>
<td align="right">1,704</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">184,485</td>
<td align="right">149,793</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,639,882</td>
<td align="right">2,207,813</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">25,235,940</td>
<td align="right">21,496,619</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">58,683</td>
<td align="right">50,029</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">48,755,257</td>
<td align="right">41,970,590</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">16,112,023</td>
<td align="right">13,996,135</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">488,844</td>
<td align="right">433,837</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,930,596</td>
<td align="right">2,631,498</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,982,876</td>
<td align="right">10,834,523</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,503,298</td>
<td align="right">32,144,845</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">56,805,654</td>
<td align="right">51,566,398</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">9,675,877</td>
<td align="right">8,807,637</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">58,365,784</td>
<td align="right">53,144,103</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">25,599</td>
<td align="right">23,373</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,047,573</td>
<td align="right">9,175,519</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">177,173,663</td>
<td align="right">162,535,927</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">15,684</td>
<td align="right">14,424</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,466</td>
<td align="right">5,067</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,198,339</td>
<td align="right">16,964,773</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">53,210,861</td>
<td align="right">49,783,814</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,634,580</td>
<td align="right">4,354,447</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,396,039</td>
<td align="right">9,778,242</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">54,757,463</td>
<td align="right">51,622,054</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,985,055</td>
<td align="right">43,389,532</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,493,448</td>
<td align="right">14,630,612</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">24,014,559</td>
<td align="right">22,679,939</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60,902,042</td>
<td align="right">57,532,805</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">33,695,657</td>
<td align="right">32,101,692</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,529,514</td>
<td align="right">15,804,985</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">18,009,445</td>
<td align="right">17,272,909</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">38,327,233</td>
<td align="right">36,787,850</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">16,190,886</td>
<td align="right">15,558,089</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">227,393,972</td>
<td align="right">219,542,869</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">90,420,281</td>
<td align="right">87,747,707</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,694,001</td>
<td align="right">29,801,635</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,738,913</td>
<td align="right">11,408,768</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">63,448,220</td>
<td align="right">61,731,953</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,864,317</td>
<td align="right">15,460,108</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">50,950,398</td>
<td align="right">49,657,488</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,257,250</td>
<td align="right">2,200,964</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">246,505,529</td>
<td align="right">240,904,087</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">69,395,022</td>
<td align="right">67,846,080</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">62,254,160</td>
<td align="right">60,908,302</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,137,892</td>
<td align="right">11,878,865</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,290,895</td>
<td align="right">1,263,917</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,632,740</td>
<td align="right">18,244,887</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">770,109</td>
<td align="right">754,429</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">61,245,906</td>
<td align="right">60,014,421</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">743,824</td>
<td align="right">728,997</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,382,156</td>
<td align="right">7,236,399</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">10,147,100</td>
<td align="right">9,948,179</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">10,173,327</td>
<td align="right">9,974,476</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,475,709</td>
<td align="right">13,223,727</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,939,756</td>
<td align="right">21,562,724</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">464,739</td>
<td align="right">457,371</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">647,666,667</td>
<td align="right">637,443,174</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">39,400,604</td>
<td align="right">38,781,962</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">50,291,452</td>
<td align="right">49,510,975</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">41,411,946</td>
<td align="right">40,774,441</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">14,898,144</td>
<td align="right">14,668,946</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">205,849,314</td>
<td align="right">202,736,918</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,068,022</td>
<td align="right">45,471,771</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">154,953,416</td>
<td align="right">152,955,762</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">43,206,626</td>
<td align="right">42,690,233</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">182,128,565</td>
<td align="right">179,999,604</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,935,336</td>
<td align="right">21,683,390</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">148,571,715</td>
<td align="right">147,049,970</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">25,934,123</td>
<td align="right">25,669,614</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">89,530</td>
<td align="right">88,657</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">187,845,396</td>
<td align="right">186,269,135</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,096,008</td>
<td align="right">5,057,025</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">18,428,506</td>
<td align="right">18,565,267</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,098,282</td>
<td align="right">6,053,339</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,584,382</td>
<td align="right">12,492,922</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">11,697,773</td>
<td align="right">11,614,176</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,388,449</td>
<td align="right">19,525,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,865</td>
<td align="right">2,183,502</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">34,785,443</td>
<td align="right">34,605,084</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,203,683</td>
<td align="right">4,183,784</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,780,261</td>
<td align="right">3,763,845</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22,506,670</td>
<td align="right">22,416,805</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,136,379</td>
<td align="right">2,128,699</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,927,394</td>
<td align="right">75,666,753</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,892,257</td>
<td align="right">6,869,654</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">90,471</td>
<td align="right">90,198</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,825,637</td>
<td align="right">1,820,551</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">440,463</td>
<td align="right">439,242</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,456,509</td>
<td align="right">1,452,932</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,664,379</td>
<td align="right">44,559,439</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,025,473</td>
<td align="right">10,002,699</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,249,626</td>
<td align="right">1,247,392</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,930,354</td>
<td align="right">44,861,304</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,402,917</td>
<td align="right">18,383,080</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">143,099</td>
<td align="right">142,992</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">184,066</td>
<td align="right">184,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,987,178</td>
<td align="right">2,985,490</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">7,254,519</td>
<td align="right">7,250,681</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">120,324</td>
<td align="right">120,261</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">241,194</td>
<td align="right">241,068</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">241,236</td>
<td align="right">241,110</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">743,482</td>
<td align="right">743,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">743,482</td>
<td align="right">743,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">743,482</td>
<td align="right">743,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,359,201</td>
<td align="right">22,350,643</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">166,780</td>
<td align="right">166,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,741</td>
<td align="right">20,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">40,046</td>
<td align="right">40,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,783,932</td>
<td align="right">18,780,506</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,861,589</td>
<td align="right">11,859,488</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,293,437</td>
<td align="right">8,294,751</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,128,266</td>
<td align="right">8,129,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">431,906</td>
<td align="right">431,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,233,873</td>
<td align="right">1,234,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">98,298</td>
<td align="right">98,288</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">50,151</td>
<td align="right">50,147</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">191,381</td>
<td align="right">191,366</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">25,306,194</td>
<td align="right">25,304,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">81,365,171</td>
<td align="right">81,359,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">444,261</td>
<td align="right">444,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,595,413</td>
<td align="right">4,595,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">3,087,652</td>
<td align="right">3,087,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">386,563</td>
<td align="right">386,543</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">945,860</td>
<td align="right">945,816</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,080,664</td>
<td align="right">1,080,614</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,082,482</td>
<td align="right">1,082,432</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">932,378</td>
<td align="right">932,335</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,866,908</td>
<td align="right">7,866,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">272,944</td>
<td align="right">272,934</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,985</td>
<td align="right">164,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">736,364</td>
<td align="right">736,389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,260,726</td>
<td align="right">7,260,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">848,530</td>
<td align="right">848,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">736,702</td>
<td align="right">736,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,276,271</td>
<td align="right">6,276,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,433,318</td>
<td align="right">3,433,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,360,975</td>
<td align="right">7,361,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">22,225,157</td>
<td align="right">22,224,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,737,343</td>
<td align="right">1,737,361</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,477,408</td>
<td align="right">1,477,397</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,795,848</td>
<td align="right">7,795,832</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,885,749</td>
<td align="right">4,885,758</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,028,007</td>
<td align="right">1,028,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">427,533</td>
<td align="right">427,533</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">378,841</td>
<td align="right">378,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">202,050</td>
<td align="right">202,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">87,150</td>
<td align="right">87,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,450</td>
<td align="right">13,450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">6,993</td>
<td align="right">6,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,200</td>
<td align="right">4,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,793</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,667</td>
<td align="right">2,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,142</td>
<td align="right">2,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,932</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,653</td>
<td align="right">1,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,265</td>
<td align="right">1,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">231</td>
<td align="right">231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">475,965</td>
<td align="right">0.4%</td>
<td align="right">431,856</td>
<td align="right">0.4%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,902,422</td>
<td align="right">38.1%</td>
<td align="right">43,310,365</td>
<td align="right">36.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">74,058,899</td>
<td align="right">61.4%</td>
<td align="right">74,078,009</td>
<td align="right">62.8%</td>
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
<td align="right">66,418</td>
<td align="right">72.7%</td>
<td align="right">63,036</td>
<td align="right">72.4%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,883</td>
<td align="right">27.3%</td>
<td align="right">23,988</td>
<td align="right">27.6%</td>
<td align="right">-3.6%</td>
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
<td align="right">3,822</td>
<td align="right">5.8%</td>
<td align="right">2,058</td>
<td align="right">3.3%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4,045</td>
<td align="right">6.1%</td>
<td align="right">3,453</td>
<td align="right">5.5%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,966</td>
<td align="right">12.0%</td>
<td align="right">7,298</td>
<td align="right">11.6%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,153</td>
<td align="right">3.2%</td>
<td align="right">1,988</td>
<td align="right">3.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,373</td>
<td align="right">3.6%</td>
<td align="right">2,310</td>
<td align="right">3.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">2,063</td>
<td align="right">3.1%</td>
<td align="right">2,021</td>
<td align="right">3.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">4,880</td>
<td align="right">7.3%</td>
<td align="right">4,836</td>
<td align="right">7.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,177</td>
<td align="right">1.8%</td>
<td align="right">1,171</td>
<td align="right">1.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,735</td>
<td align="right">5.6%</td>
<td align="right">3,718</td>
<td align="right">5.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,991</td>
<td align="right">9.0%</td>
<td align="right">5,969</td>
<td align="right">9.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">360</td>
<td align="right">0.5%</td>
<td align="right">361</td>
<td align="right">0.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,934</td>
<td align="right">2.9%</td>
<td align="right">1,929</td>
<td align="right">3.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,421</td>
<td align="right">14.2%</td>
<td align="right">9,426</td>
<td align="right">15.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,261</td>
<td align="right">9.4%</td>
<td align="right">6,261</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">3,173</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,940</td>
<td align="right">4.4%</td>
<td align="right">2,940</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">2,355</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,253</td>
<td align="right">1.9%</td>
<td align="right">1,253</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">294</td>
<td align="right">0.4%</td>
<td align="right">294</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">198</td>
<td align="right">0.3%</td>
<td align="right">198</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">90,471</td>
<td align="right">100.0%</td>
<td align="right">90,198</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">36,936,063</td>
<td align="right">11.4%</td>
<td align="right">37,072,429</td>
<td align="right">11.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,415,273</td>
<td align="right">11.3%</td>
<td align="right">36,549,046</td>
<td align="right">11.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">286,044,285</td>
<td align="right">88.5%</td>
<td align="right">285,955,359</td>
<td align="right">88.4%</td>
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
<td align="right">793,734</td>
<td align="right">100.0%</td>
<td align="right">796,317</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">11,352</td>
<td align="right">69.1%</td>
<td align="right">11,352</td>
<td align="right">69.1%</td>
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
<td align="right">2,988</td>
<td align="right">18.2%</td>
<td align="right">2,988</td>
<td align="right">18.2%</td>
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
<td align="right">5,086</td>
<td align="right">100.0%</td>
<td align="right">5,086</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,620,456</td>
<td align="right">36.5%</td>
<td align="right">29,728,323</td>
<td align="right">35.8%</td>
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
<td align="right">433,254</td>
<td align="right">0.5%</td>
<td align="right">432,295</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">52,872,641</td>
<td align="right">62.9%</td>
<td align="right">52,871,223</td>
<td align="right">63.6%</td>
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
<td align="left">Failure</td>
<td align="right">63,646</td>
<td align="right">78.0%</td>
<td align="right">63,411</td>
<td align="right">78.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">17,918</td>
<td align="right">22.0%</td>
<td align="right">17,899</td>
<td align="right">22.0%</td>
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
<td align="left">bool</td>
<td align="right">1,790</td>
<td align="right">2.8%</td>
<td align="right">1,623</td>
<td align="right">2.6%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">292</td>
<td align="right">0.5%</td>
<td align="right">291</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">15,849</td>
<td align="right">24.9%</td>
<td align="right">15,802</td>
<td align="right">24.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,426</td>
<td align="right">22.7%</td>
<td align="right">14,401</td>
<td align="right">22.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,087</td>
<td align="right">19.0%</td>
<td align="right">12,092</td>
<td align="right">19.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,004</td>
<td align="right">15.7%</td>
<td align="right">10,004</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">8,316</td>
<td align="right">13.1%</td>
<td align="right">8,316</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">315</td>
<td align="right">0.5%</td>
<td align="right">315</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">273</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">231</td>
<td align="right">0.4%</td>
<td align="right">231</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">63</td>
<td align="right">0.1%</td>
<td align="right">63</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,682,408</td>
<td align="right">33.2%</td>
<td align="right">7,459,405</td>
<td align="right">24.1%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,523,548</td>
<td align="right">66.8%</td>
<td align="right">23,522,722</td>
<td align="right">75.9%</td>
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
<td align="right">924</td>
<td align="right">0.0%</td>
<td align="right">924</td>
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
<td align="right">12,666</td>
<td align="right">90.3%</td>
<td align="right">11,587</td>
<td align="right">89.5%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365</td>
<td align="right">9.7%</td>
<td align="right">1,365</td>
<td align="right">10.5%</td>
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
<td align="right">5,586</td>
<td align="right">44.1%</td>
<td align="right">4,719</td>
<td align="right">40.7%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,197</td>
<td align="right">9.5%</td>
<td align="right">1,071</td>
<td align="right">9.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,526</td>
<td align="right">43.6%</td>
<td align="right">5,440</td>
<td align="right">46.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">357</td>
<td align="right">2.8%</td>
<td align="right">357</td>
<td align="right">3.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,244,041</td>
<td align="right">1.0%</td>
<td align="right">832,239</td>
<td align="right">0.8%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">48,663,641</td>
<td align="right">40.8%</td>
<td align="right">41,883,165</td>
<td align="right">39.6%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">69,168,248</td>
<td align="right">58.0%</td>
<td align="right">62,993,452</td>
<td align="right">59.5%</td>
<td align="right">-8.9%</td>
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
<td align="right">37,436</td>
<td align="right">32.6%</td>
<td align="right">29,659</td>
<td align="right">28.8%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">77,536</td>
<td align="right">67.4%</td>
<td align="right">73,359</td>
<td align="right">71.2%</td>
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
<td align="left">list</td>
<td align="right">714</td>
<td align="right">0.9%</td>
<td align="right">567</td>
<td align="right">0.8%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,618</td>
<td align="right">2.1%</td>
<td align="right">1,449</td>
<td align="right">2.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">5,198</td>
<td align="right">6.7%</td>
<td align="right">4,704</td>
<td align="right">6.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,557</td>
<td align="right">9.7%</td>
<td align="right">7,027</td>
<td align="right">9.6%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51,043</td>
<td align="right">65.8%</td>
<td align="right">48,398</td>
<td align="right">66.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,306</td>
<td align="right">5.6%</td>
<td align="right">4,157</td>
<td align="right">5.7%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,828</td>
<td align="right">2.4%</td>
<td align="right">1,786</td>
<td align="right">2.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,773</td>
<td align="right">3.6%</td>
<td align="right">2,772</td>
<td align="right">3.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,344</td>
<td align="right">1.7%</td>
<td align="right">1,344</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">903</td>
<td align="right">1.2%</td>
<td align="right">903</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">84</td>
<td align="right">0.1%</td>
<td align="right">84</td>
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
<td align="right">72,787</td>
<td align="right">72,787 / 0 !!</td>
<td align="right">72,734</td>
<td align="right">72,734 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,358,518</td>
<td align="right">7,358,518 / 0 !!</td>
<td align="right">7,357,296</td>
<td align="right">7,357,296 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">166,059</td>
<td align="right">166,059 / 0 !!</td>
<td align="right">166,047</td>
<td align="right">166,047 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,946,496</td>
<td align="right">8,946,496 / 0 !!</td>
<td align="right">8,946,212</td>
<td align="right">8,946,212 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,563,532</td>
<td align="right">9,563,532 / 0 !!</td>
<td align="right">9,563,278</td>
<td align="right">9,563,278 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,175,893</td>
<td align="right">9,175,893 / 0 !!</td>
<td align="right">9,175,662</td>
<td align="right">9,175,662 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,458,998</td>
<td align="right">12,458,998 / 0 !!</td>
<td align="right">12,459,049</td>
<td align="right">12,459,049 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,174</td>
<td align="right">6,174 / 0 !!</td>
<td align="right">6,174</td>
<td align="right">6,174 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4,119</td>
<td align="right">4,119 / 0 !!</td>
<td align="right">4,119</td>
<td align="right">4,119 / 0 !!</td>
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
<td align="right">61,022,054</td>
<td align="right">18.6%</td>
<td align="right">59,791,528</td>
<td align="right">18.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">213,875,449</td>
<td align="right">65.2%</td>
<td align="right">210,053,355</td>
<td align="right">65.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,924,082</td>
<td align="right">16.1%</td>
<td align="right">52,809,783</td>
<td align="right">16.4%</td>
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
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">124,986</td>
<td align="right">10.3%</td>
<td align="right">124,600</td>
<td align="right">10.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,085,280</td>
<td align="right">89.7%</td>
<td align="right">1,083,082</td>
<td align="right">89.7%</td>
<td align="right">-0.2%</td>
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
<td align="left">builtin class method</td>
<td align="right">903</td>
<td align="right">0.7%</td>
<td align="right">861</td>
<td align="right">0.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,391</td>
<td align="right">3.5%</td>
<td align="right">4,349</td>
<td align="right">3.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,533</td>
<td align="right">7.6%</td>
<td align="right">9,453</td>
<td align="right">7.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">14,856</td>
<td align="right">11.9%</td>
<td align="right">14,773</td>
<td align="right">11.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,570</td>
<td align="right">6.1%</td>
<td align="right">7,545</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,319</td>
<td align="right">49.1%</td>
<td align="right">61,203</td>
<td align="right">49.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">12,353</td>
<td align="right">9.9%</td>
<td align="right">12,355</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,883</td>
<td align="right">7.1%</td>
<td align="right">8,883</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">588</td>
<td align="right">0.5%</td>
<td align="right">588</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">106</td>
<td align="right">0.1%</td>
<td align="right">106</td>
<td align="right">0.1%</td>
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
<td align="right">273,789,995</td>
<td align="right">99.9%</td>
<td align="right">269,188,535</td>
<td align="right">99.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">94,812</td>
<td align="right">0.0%</td>
<td align="right">94,802</td>
<td align="right">0.0%</td>
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
<td align="right">21,399</td>
<td align="right">0.0%</td>
<td align="right">21,399</td>
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
<td align="right">96,779</td>
<td align="right">100.0%</td>
<td align="right">96,774</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,409,786</td>
<td align="right">99.9%</td>
<td align="right">2,409,732</td>
<td align="right">99.9%</td>
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
<td align="right">635</td>
<td align="right">0.0%</td>
<td align="right">635</td>
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
<td align="right">630</td>
<td align="right">100.0%</td>
<td align="right">630</td>
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
<td align="right">821,109</td>
<td align="right">66.9%</td>
<td align="right">821,136</td>
<td align="right">66.9%</td>
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
<td align="right">375,973</td>
<td align="right">30.6%</td>
<td align="right">375,973</td>
<td align="right">30.6%</td>
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
<td align="right">27,421</td>
<td align="right">2.2%</td>
<td align="right">27,421</td>
<td align="right">2.2%</td>
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
<td align="right">569</td>
<td align="right">16.9%</td>
<td align="right">569</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,805</td>
<td align="right">83.1%</td>
<td align="right">2,805</td>
<td align="right">83.1%</td>
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
<td align="right">2,805</td>
<td align="right">100.0%</td>
<td align="right">2,805</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,821,423</td>
<td align="right">17.0%</td>
<td align="right">1,821,632</td>
<td align="right">17.0%</td>
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
<td align="right">377,538</td>
<td align="right">3.5%</td>
<td align="right">377,522</td>
<td align="right">3.5%</td>
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
<td align="right">8,526,730</td>
<td align="right">79.4%</td>
<td align="right">8,526,676</td>
<td align="right">79.4%</td>
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
<td align="left">Failure</td>
<td align="right">3,649</td>
<td align="right">8.4%</td>
<td align="right">3,645</td>
<td align="right">8.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,659</td>
<td align="right">91.6%</td>
<td align="right">39,658</td>
<td align="right">91.6%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,402</td>
<td align="right">38.4%</td>
<td align="right">1,398</td>
<td align="right">38.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,953</td>
<td align="right">53.5%</td>
<td align="right">1,953</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">462</td>
<td align="right">12.7%</td>
<td align="right">462</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">63</td>
<td align="right">1.7%</td>
<td align="right">63</td>
<td align="right">1.7%</td>
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
<td align="right">2,103</td>
<td align="right">100.0%</td>
<td align="right">1,704</td>
<td align="right">100.0%</td>
<td align="right">-19.0%</td>
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
<td align="right">2,756,586</td>
<td align="right">13.2%</td>
<td align="right">2,227,936</td>
<td align="right">11.0%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,084,710</td>
<td align="right">86.7%</td>
<td align="right">18,077,878</td>
<td align="right">89.0%</td>
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
<td align="left">Failure</td>
<td align="right">3,510</td>
<td align="right">55.1%</td>
<td align="right">3,394</td>
<td align="right">54.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,860</td>
<td align="right">44.9%</td>
<td align="right">2,860</td>
<td align="right">45.7%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">3,510</td>
<td align="right">100.0%</td>
<td align="right">3,394</td>
<td align="right">100.0%</td>
<td align="right">-3.3%</td>
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
<td align="right">168,747,190</td>
<td align="right">94.0%</td>
<td align="right">167,703,756</td>
<td align="right">94.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,941,076</td>
<td align="right">5.5%</td>
<td align="right">9,918,367</td>
<td align="right">5.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">668,609</td>
<td align="right">0.4%</td>
<td align="right">668,384</td>
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
<td align="left">Failure</td>
<td align="right">27,186</td>
<td align="right">28.4%</td>
<td align="right">27,134</td>
<td align="right">28.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,669</td>
<td align="right">71.6%</td>
<td align="right">68,659</td>
<td align="right">71.7%</td>
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
<td align="left">dict</td>
<td align="right">2,352</td>
<td align="right">8.7%</td>
<td align="right">2,289</td>
<td align="right">8.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,060</td>
<td align="right">11.3%</td>
<td align="right">3,101</td>
<td align="right">11.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,363</td>
<td align="right">12.4%</td>
<td align="right">3,374</td>
<td align="right">12.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">13,551</td>
<td align="right">49.8%</td>
<td align="right">13,508</td>
<td align="right">49.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,395</td>
<td align="right">5.1%</td>
<td align="right">1,397</td>
<td align="right">5.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,339</td>
<td align="right">12.3%</td>
<td align="right">3,339</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,670,389</td>
<td align="right">100.0%</td>
<td align="right">83,792,730</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,357</td>
<td align="right">0.0%</td>
<td align="right">27,346</td>
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
<td align="left">Failure</td>
<td align="right">750</td>
<td align="right">5.9%</td>
<td align="right">751</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,939</td>
<td align="right">94.1%</td>
<td align="right">11,939</td>
<td align="right">94.1%</td>
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
<td align="right">687</td>
<td align="right">91.6%</td>
<td align="right">688</td>
<td align="right">91.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">63</td>
<td align="right">8.4%</td>
<td align="right">63</td>
<td align="right">8.4%</td>
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
<td align="right">258,610,173</td>
<td align="right">5.8%</td>
<td align="right">241,733,532</td>
<td align="right">5.6%</td>
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
<td align="right">1,475,109,857</td>
<td align="right">33.1%</td>
<td align="right">1,418,679,792</td>
<td align="right">32.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,626,539,795</td>
<td align="right">59.0%</td>
<td align="right">2,569,932,652</td>
<td align="right">59.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">94,556,169</td>
<td align="right">2.1%</td>
<td align="right">94,121,350</td>
<td align="right">2.2%</td>
<td align="right">-0.5%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">11,682,408</td>
<td align="right">4.7%</td>
<td align="right">7,459,405</td>
<td align="right">3.2%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,756,586</td>
<td align="right">1.1%</td>
<td align="right">2,227,936</td>
<td align="right">1.0%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">48,663,641</td>
<td align="right">19.6%</td>
<td align="right">41,883,165</td>
<td align="right">18.1%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">45,902,422</td>
<td align="right">18.5%</td>
<td align="right">43,310,365</td>
<td align="right">18.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,620,456</td>
<td align="right">12.3%</td>
<td align="right">29,728,323</td>
<td align="right">12.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">61,022,054</td>
<td align="right">24.6%</td>
<td align="right">59,791,528</td>
<td align="right">25.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,415,273</td>
<td align="right">14.7%</td>
<td align="right">36,549,046</td>
<td align="right">15.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,941,076</td>
<td align="right">4.0%</td>
<td align="right">9,918,367</td>
<td align="right">4.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">377,538</td>
<td align="right">0.2%</td>
<td align="right">377,522</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">375,973</td>
<td align="right">0.2%</td>
<td align="right">375,973</td>
<td align="right">0.2%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,420,776</td>
<td align="right">12.1%</td>
<td align="right">11,560,305</td>
<td align="right">12.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,301,832</td>
<td align="right">3.5%</td>
<td align="right">3,289,841</td>
<td align="right">3.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,857,769</td>
<td align="right">30.5%</td>
<td align="right">28,782,934</td>
<td align="right">30.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,931,107</td>
<td align="right">13.7%</td>
<td align="right">12,907,386</td>
<td align="right">13.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,184,538</td>
<td align="right">6.5%</td>
<td align="right">6,182,418</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,820,637</td>
<td align="right">1.9%</td>
<td align="right">1,820,846</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,315,695</td>
<td align="right">7.7%</td>
<td align="right">7,315,007</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,903,172</td>
<td align="right">12.6%</td>
<td align="right">11,902,462</td>
<td align="right">12.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,105,477</td>
<td align="right">2.2%</td>
<td align="right">2,105,458</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,164,097</td>
<td align="right">5.5%</td>
<td align="right">5,164,132</td>
<td align="right">5.5%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">135,805,859</td>
<td align="right">62.5%</td>
<td align="right">135,922,096</td>
<td align="right">62.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,047,694</td>
<td align="right">0.5%</td>
<td align="right">1,047,342</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">193,803,937</td>
<td align="right">89.2%</td>
<td align="right">193,777,756</td>
<td align="right">89.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">42,025,671</td>
<td align="right">19.3%</td>
<td align="right">42,020,370</td>
<td align="right">19.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">77,475,610</td>
<td align="right">35.6%</td>
<td align="right">77,470,045</td>
<td align="right">35.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">77,483,128</td>
<td align="right">35.7%</td>
<td align="right">77,477,563</td>
<td align="right">35.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">81,529,481</td>
<td align="right">37.5%</td>
<td align="right">81,523,938</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">81,529,481</td>
<td align="right">37.5%</td>
<td align="right">81,523,938</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,923,841</td>
<td align="right">8.7%</td>
<td align="right">18,923,707</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">4,046,353</td>
<td align="right">1.9%</td>
<td align="right">4,046,375</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,359,241</td>
<td align="right">4.3%</td>
<td align="right">9,359,201</td>
<td align="right">4.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">8,736</td>
<td align="right">0.0%</td>
<td align="right">8,736</td>
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
<td align="right">997,328</td>
<td align="right"></td>
<td align="right">1,317,868</td>
<td align="right"></td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">4,399,108</td>
<td align="right"></td>
<td align="right">4,245,354</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,392,920</td>
<td align="right"></td>
<td align="right">5,559,691</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">53,652,667</td>
<td align="right">1.4%</td>
<td align="right">52,135,443</td>
<td align="right">1.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,245,967,311</td>
<td align="right">35.0%</td>
<td align="right">1,274,391,685</td>
<td align="right">35.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,375,576,954</td>
<td align="right">36.0%</td>
<td align="right">1,401,064,751</td>
<td align="right">36.6%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">80,210,872</td>
<td align="right">2.3%</td>
<td align="right">78,850,888</td>
<td align="right">2.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,221,860,308</td>
<td align="right">34.4%</td>
<td align="right">1,204,863,835</td>
<td align="right">33.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">23,547</td>
<td align="right">0.0%</td>
<td align="right">23,778</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,522,098,544</td>
<td align="right">39.8%</td>
<td align="right">1,508,036,220</td>
<td align="right">39.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">849,701</td>
<td align="right">0.2%</td>
<td align="right">857,174</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">869,561,119</td>
<td align="right">22.8%</td>
<td align="right">871,030,601</td>
<td align="right">22.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">256,185,696</td>
<td align="right"></td>
<td align="right">255,834,951</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,007,327,617</td>
<td align="right">28.3%</td>
<td align="right">1,008,650,525</td>
<td align="right">28.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">153,150,993</td>
<td align="right"></td>
<td align="right">153,192,132</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">135,553,365</td>
<td align="right">27.3%</td>
<td align="right">135,560,425</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">361,402,601</td>
<td align="right">72.7%</td>
<td align="right">361,393,642</td>
<td align="right">72.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">361,656,073</td>
<td align="right"></td>
<td align="right">361,647,117</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,186,641</td>
<td align="right"></td>
<td align="right">1,186,653</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">146,059,438</td>
<td align="right"></td>
<td align="right">146,060,858</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">134,680,117</td>
<td align="right">27.1%</td>
<td align="right">134,679,473</td>
<td align="right">27.1%</td>
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
<td align="right">153</td>
<td align="right">0.8%</td>
<td align="right">638</td>
<td align="right">1.5%</td>
<td align="right">317.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,755</td>
<td align="right">14.6%</td>
<td align="right">8,719</td>
<td align="right">21.0%</td>
<td align="right">216.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">8,855</td>
<td align="right">47.1%</td>
<td align="right">21,310</td>
<td align="right">51.4%</td>
<td align="right">140.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,811</td>
<td align="right"></td>
<td align="right">41,481</td>
<td align="right"></td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">168</td>
<td align="right">0.9%</td>
<td align="right">362</td>
<td align="right">0.9%</td>
<td align="right">115.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,626</td>
<td align="right">29.9%</td>
<td align="right">9,774</td>
<td align="right">23.6%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">42,774,999</td>
<td align="right"></td>
<td align="right">57,260,349</td>
<td align="right"></td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,507,420,746</td>
<td align="right">3,524.1%</td>
<td align="right">1,930,374,150</td>
<td align="right">3,371.2%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">1,575</td>
<td align="right">8.4%</td>
<td align="right">1,678</td>
<td align="right">4.0%</td>
<td align="right">6.5%</td>
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
<td align="right">84</td>
<td align="right">0.2%</td>
<td align="right">84 / 0 !!</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">90</td>
<td align="right">1.0%</td>
<td align="right">90 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,755</td>
<td align="right"></td>
<td align="right">8,719</td>
<td align="right"></td>
<td align="right">216.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,597</td>
<td align="right">94.3%</td>
<td align="right">7,659</td>
<td align="right">87.8%</td>
<td align="right">194.9%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">15,401,387</td>
<td align="right">70.4%</td>
<td align="right">56,519,626</td>
<td align="right">75.1%</td>
<td align="right">267.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">484,936</td>
<td align="right">2.2%</td>
<td align="right">1,694,328</td>
<td align="right">2.3%</td>
<td align="right">249.4%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">21,876,736</td>
<td align="right"></td>
<td align="right">75,239,424</td>
<td align="right"></td>
<td align="right">243.9%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">5,990,413</td>
<td align="right">27.4%</td>
<td align="right">17,025,470</td>
<td align="right">22.6%</td>
<td align="right">184.2%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">172,032</td>
<td align="right">0.8%</td>
<td align="right">344,064</td>
<td align="right">0.5%</td>
<td align="right">100.0%</td>
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
<td align="left">756</td>
<td align="right">29.1%</td>
<td align="left">1,101</td>
<td align="right">14.4%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">1,379</td>
<td align="right">53.1%</td>
<td align="left">4,283</td>
<td align="right">55.9%</td>
<td align="right">210.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">378</td>
<td align="right">14.6%</td>
<td align="left">1,939</td>
<td align="right">25.3%</td>
<td align="right">413.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">84</td>
<td align="right">3.2%</td>
<td align="left">336</td>
<td align="right">4.4%</td>
<td align="right">300.0%</td>
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
<td align="right">124</td>
<td align="right">4.5%</td>
<td align="right">294</td>
<td align="right">3.4%</td>
<td align="right">137.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">260</td>
<td align="right">9.4%</td>
<td align="right">497</td>
<td align="right">5.7%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">812</td>
<td align="right">29.5%</td>
<td align="right">964</td>
<td align="right">11.1%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,139</td>
<td align="right">41.3%</td>
<td align="right">4,525</td>
<td align="right">51.9%</td>
<td align="right">297.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">336</td>
<td align="right">12.2%</td>
<td align="right">1,527</td>
<td align="right">17.5%</td>
<td align="right">354.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">2.3%</td>
<td align="right">744</td>
<td align="right">8.5%</td>
<td align="right">1,081.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">168</td>
<td align="right">1.9%</td>
<td align="right">700.0%</td>
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
<td align="right">82</td>
<td align="right">3.0%</td>
<td align="right">252</td>
<td align="right">2.9%</td>
<td align="right">207.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">157</td>
<td align="right">5.7%</td>
<td align="right">168</td>
<td align="right">1.9%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">250</td>
<td align="right">9.1%</td>
<td align="right">197</td>
<td align="right">2.3%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,583</td>
<td align="right">57.5%</td>
<td align="right">4,381</td>
<td align="right">50.2%</td>
<td align="right">176.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">231</td>
<td align="right">8.4%</td>
<td align="right">1,647</td>
<td align="right">18.9%</td>
<td align="right">613.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">273</td>
<td align="right">9.9%</td>
<td align="right">867</td>
<td align="right">9.9%</td>
<td align="right">217.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">147</td>
<td align="right">1.7%</td>
<td align="right">600.0%</td>
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
<td align="left">_LOAD_DEREF</td>
<td align="right">42,710</td>
<td align="right">3,292,054</td>
<td align="right">7,607.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">21,355</td>
<td align="right">894,220</td>
<td align="right">4,087.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">28,056</td>
<td align="right">460,022</td>
<td align="right">1,539.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">28,056</td>
<td align="right">413,155</td>
<td align="right">1,372.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">28,119</td>
<td align="right">370,272</td>
<td align="right">1,216.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">60,010</td>
<td align="right">1,061.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">306,978</td>
<td align="right">1,045.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">68,187</td>
<td align="right">694,155</td>
<td align="right">918.0%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">133,854</td>
<td align="right">1,224,384</td>
<td align="right">814.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">18,228</td>
<td align="right">163,431</td>
<td align="right">796.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">80,262</td>
<td align="right">704,691</td>
<td align="right">778.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,311</td>
<td align="right">445,614</td>
<td align="right">751.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">185,556</td>
<td align="right">1,514,751</td>
<td align="right">716.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">65,016</td>
<td align="right">382,704</td>
<td align="right">488.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">172,620</td>
<td align="right">1,010,928</td>
<td align="right">485.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">206,514</td>
<td align="right">1,071,129</td>
<td align="right">418.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">206,514</td>
<td align="right">1,071,129</td>
<td align="right">418.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">183,183</td>
<td align="right">858,675</td>
<td align="right">368.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,067,334</td>
<td align="right">4,540,275</td>
<td align="right">325.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,067,334</td>
<td align="right">4,540,275</td>
<td align="right">325.4%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,262,548</td>
<td align="right">4,707,929</td>
<td align="right">272.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,262,548</td>
<td align="right">4,707,929</td>
<td align="right">272.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,262,548</td>
<td align="right">4,707,929</td>
<td align="right">272.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,262,548</td>
<td align="right">4,606,410</td>
<td align="right">264.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,029,769</td>
<td align="right">3,605,952</td>
<td align="right">250.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">72,800</td>
<td align="right">253,143</td>
<td align="right">247.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">2,732,741</td>
<td align="right">9,269,948</td>
<td align="right">239.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,550,207</td>
<td align="right">5,223,590</td>
<td align="right">237.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">155,064</td>
<td align="right">514,944</td>
<td align="right">232.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">4,534,185</td>
<td align="right">12,839,909</td>
<td align="right">183.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">276,885</td>
<td align="right">779,853</td>
<td align="right">181.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,605,731</td>
<td align="right">11,959,244</td>
<td align="right">159.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,896,509</td>
<td align="right">7,138,169</td>
<td align="right">146.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,039,500</td>
<td align="right">2,458,472</td>
<td align="right">136.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">21,355</td>
<td align="right">43,966</td>
<td align="right">105.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">276,885</td>
<td align="right">546,095</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,786,177</td>
<td align="right">5,044,726</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">887,312</td>
<td align="right">1,597,593</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">959,553</td>
<td align="right">1,696,277</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,552,821</td>
<td align="right">2,689,164</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,731,052</td>
<td align="right">4,626,502</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,502,153</td>
<td align="right">14,340,527</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">937,839</td>
<td align="right">1,577,711</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">937,839</td>
<td align="right">1,575,947</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,328,364</td>
<td align="right">10,526,067</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,685,167</td>
<td align="right">4,222,096</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">453,033</td>
<td align="right">711,606</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">1,893,688</td>
<td align="right">2,969,806</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">20,306,537</td>
<td align="right">31,340,686</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,467,078</td>
<td align="right">2,238,125</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,391,236</td>
<td align="right">2,115,630</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,391,236</td>
<td align="right">2,115,630</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">1,690,562</td>
<td align="right">2,570,187</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,998,198</td>
<td align="right">2,979,123</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,244,131</td>
<td align="right">3,322,025</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,414,494</td>
<td align="right">13,907,151</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,180,216</td>
<td align="right">4,523,081</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,924,761</td>
<td align="right">2,689,547</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,154,125</td>
<td align="right">9,887,341</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,684,554</td>
<td align="right">2,278,800</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">42,774,999</td>
<td align="right">57,260,349</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,802,976</td>
<td align="right">5,084,074</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">42,774,999</td>
<td align="right">57,171,568</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">23,341,264</td>
<td align="right">30,931,494</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,307,101</td>
<td align="right">1,711,013</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,231,198</td>
<td align="right">4,213,443</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">10,614,278</td>
<td align="right">13,785,197</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,093,942</td>
<td align="right">2,717,524</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,292,830</td>
<td align="right">8,019,132</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">12,771,561</td>
<td align="right">15,988,222</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,067,659</td>
<td align="right">2,582,250</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">314,577,690</td>
<td align="right">392,385,347</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,264,751</td>
<td align="right">9,049,384</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">285,938,680</td>
<td align="right">352,908,935</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">820,385</td>
<td align="right">1,007,968</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,640,769</td>
<td align="right">2,014,460</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">75,713,517</td>
<td align="right">92,800,324</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,353,680</td>
<td align="right">2,859,268</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">82,041,506</td>
<td align="right">99,461,277</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">25,430,741</td>
<td align="right">30,819,276</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">25,430,741</td>
<td align="right">30,792,102</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">33,776,508</td>
<td align="right">40,888,704</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,786,539</td>
<td align="right">4,566,878</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,640,770</td>
<td align="right">1,970,802</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,797,501</td>
<td align="right">6,934,185</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,262,548</td>
<td align="right">1,497,926</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">29,899,880</td>
<td align="right">35,433,062</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,262,548</td>
<td align="right">1,494,440</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">3,847,791</td>
<td align="right">4,528,919</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">25,006,892</td>
<td align="right">29,393,608</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,558,104</td>
<td align="right">1,822,923</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">11,584,139</td>
<td align="right">13,522,742</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">11,584,139</td>
<td align="right">13,522,742</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">7,964,827</td>
<td align="right">9,277,726</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,262,548</td>
<td align="right">1,464,700</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,466,295</td>
<td align="right">7,500,055</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,262,548</td>
<td align="right">1,462,640</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,262,548</td>
<td align="right">1,462,623</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,262,548</td>
<td align="right">1,462,623</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,262,548</td>
<td align="right">1,462,623</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,558,104</td>
<td align="right">1,800,500</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">25,006,892</td>
<td align="right">28,699,162</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">21,582,168</td>
<td align="right">24,484,865</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">28,710,292</td>
<td align="right">32,281,312</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,227,530</td>
<td align="right">11,457,215</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">25,021,325</td>
<td align="right">27,954,239</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,254,984</td>
<td align="right">19,131,558</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,787,875</td>
<td align="right">6,402,909</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">25,199,680</td>
<td align="right">27,150,793</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">39,266,507</td>
<td align="right">42,200,928</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">4,967,490</td>
<td align="right">5,219,419</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">4,967,490</td>
<td align="right">5,219,419</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">31,673,515</td>
<td align="right">32,410,134</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,489,021</td>
<td align="right">15,748,183</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">11,777,481</td>
<td align="right">11,679,623</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,462,784</td>
<td align="right">2,478,927</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">3,221,870</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">3,213,506</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">3,069,173</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">1,549,021</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">1,164,265</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">528,473</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">136,128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right"></td>
<td align="right">106,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">103,929</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">89,346</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">84,037</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">69,468</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">63,088</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">59,136</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right"></td>
<td align="right">59,002</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">55,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">39,144</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">34,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">27,216</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">25,693</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">23,436</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">22,575</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">19,858</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">14,826</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">14,826</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">12,390</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">8,610</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">8,601</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">7,836</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">7,593</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">7,368</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">5,115</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">5,083</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">4,464</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">3,456</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">3,414</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">2,499</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">2,238</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">2,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">2,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">1,938</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right"></td>
<td align="right">1,848</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">1,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">1,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">1,221</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">861</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">861</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">861</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">399</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">399</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">273</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">105</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">18</td>
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
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">63</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">351</td>
<td align="right">690</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,456</td>
<td align="right">1,891</td>
<td align="right">29.9%</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-01
