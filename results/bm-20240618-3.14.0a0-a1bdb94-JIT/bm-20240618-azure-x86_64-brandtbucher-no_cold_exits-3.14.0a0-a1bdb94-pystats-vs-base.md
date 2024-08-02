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
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,205,894</td>
<td align="right">1,449,915</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,283,832</td>
<td align="right">9,601,148</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,341,632</td>
<td align="right">39,885,113</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">39,557,944</td>
<td align="right">37,817,160</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,277,652</td>
<td align="right">2,341,706</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">373,495,261</td>
<td align="right">363,820,596</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">32,001,165</td>
<td align="right">31,281,455</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">88,805,551</td>
<td align="right">87,418,490</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,865,669</td>
<td align="right">2,910,356</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">106,308,452</td>
<td align="right">104,807,448</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,743,865</td>
<td align="right">105,275,432</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">360,521,615</td>
<td align="right">355,725,547</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">71,692,161</td>
<td align="right">70,804,657</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">294,597,198</td>
<td align="right">291,538,240</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">209,364</td>
<td align="right">207,268</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">154,440</td>
<td align="right">152,920</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">627,886,470</td>
<td align="right">622,286,380</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,172,510</td>
<td align="right">97,313,078</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">329,247,763</td>
<td align="right">326,502,493</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,221,681,984</td>
<td align="right">4,188,272,837</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,155,399,688</td>
<td align="right">1,148,071,915</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">111,509,674</td>
<td align="right">110,805,288</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">323,576,833</td>
<td align="right">321,602,684</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,605,699</td>
<td align="right">78,146,873</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">865,038,468</td>
<td align="right">860,159,134</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,191,261</td>
<td align="right">65,829,513</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">952,263,774</td>
<td align="right">947,063,248</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,553,381,899</td>
<td align="right">1,545,135,053</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,977,560,489</td>
<td align="right">5,948,560,474</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">99,318,420</td>
<td align="right">98,872,660</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">738,754,029</td>
<td align="right">735,445,348</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,376,472,693</td>
<td align="right">5,352,487,902</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">129,304,944</td>
<td align="right">128,736,393</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,490,328,306</td>
<td align="right">5,466,865,860</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,717,741</td>
<td align="right">52,494,861</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">106,097,622</td>
<td align="right">105,651,862</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">274,681,115</td>
<td align="right">273,544,717</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,668,480,094</td>
<td align="right">20,583,010,959</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,274,321,458</td>
<td align="right">1,269,164,187</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">181,754,934</td>
<td align="right">181,034,849</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">199,131,653</td>
<td align="right">198,364,395</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">364,191,969</td>
<td align="right">362,839,629</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">210,213,569</td>
<td align="right">209,438,135</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">111,473,352</td>
<td align="right">111,070,435</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,735,893,621</td>
<td align="right">1,729,726,407</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,256,360,461</td>
<td align="right">2,248,716,179</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">661,571,221</td>
<td align="right">659,465,314</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,254,820,837</td>
<td align="right">1,251,109,319</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">171,591,163</td>
<td align="right">171,100,682</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,013,302</td>
<td align="right">195,462,577</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,894,185</td>
<td align="right">225,274,790</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">660,663,080</td>
<td align="right">658,851,981</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">194,167,400</td>
<td align="right">193,636,373</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">764,849,659</td>
<td align="right">762,825,442</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">415,264,790</td>
<td align="right">414,200,062</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">985,899,216</td>
<td align="right">983,416,078</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,129,608,787</td>
<td align="right">1,126,769,012</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,856,220</td>
<td align="right">90,632,460</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,861,040</td>
<td align="right">90,637,280</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,674,470,322</td>
<td align="right">2,668,000,353</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,246,855,088</td>
<td align="right">3,239,485,757</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,387,828</td>
<td align="right">17,425,664</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,793,162,185</td>
<td align="right">5,781,100,852</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,387,294</td>
<td align="right">4,396,244</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">185,531,222</td>
<td align="right">185,171,553</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">391,458,417</td>
<td align="right">390,717,376</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,276,696,890</td>
<td align="right">2,272,799,002</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,942,424,036</td>
<td align="right">3,935,760,259</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,928,461,952</td>
<td align="right">3,921,946,138</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">587,695,177</td>
<td align="right">586,751,077</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,156,552</td>
<td align="right">40,219,416</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,656,625</td>
<td align="right">13,635,881</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">283,666,420</td>
<td align="right">283,287,708</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">728,974,111</td>
<td align="right">728,022,067</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">357,931,546</td>
<td align="right">357,497,741</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,264,438,264</td>
<td align="right">3,260,605,747</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">89,990,293</td>
<td align="right">90,089,651</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,793,515</td>
<td align="right">221,552,359</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,276,620</td>
<td align="right">8,285,383</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">367,079,746</td>
<td align="right">366,698,881</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,518,577</td>
<td align="right">17,536,465</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,372,201</td>
<td align="right">474,887,192</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">289,349,744</td>
<td align="right">289,070,371</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,096,008,517</td>
<td align="right">4,092,107,676</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,682,146</td>
<td align="right">81,746,152</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,979,750</td>
<td align="right">49,016,594</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,548,057,971</td>
<td align="right">1,546,936,562</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">83,071,426</td>
<td align="right">83,015,337</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,859,466</td>
<td align="right">53,894,473</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,744,904</td>
<td align="right">58,781,432</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,336,423</td>
<td align="right">397,096,571</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">576,873,235</td>
<td align="right">576,533,383</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">707,906,121</td>
<td align="right">707,527,743</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,364,629,762</td>
<td align="right">1,363,909,446</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">128,986,475</td>
<td align="right">128,925,003</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,481</td>
<td align="right">15,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">392,818,649</td>
<td align="right">392,991,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">937,197,904</td>
<td align="right">936,804,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,187,047</td>
<td align="right">19,179,762</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,614,430</td>
<td align="right">94,647,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">785,460,416</td>
<td align="right">785,199,199</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,293,805</td>
<td align="right">216,222,427</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">473,154,679</td>
<td align="right">473,012,351</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">430,891,337</td>
<td align="right">430,766,506</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">520,562,772</td>
<td align="right">520,429,727</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,818,359</td>
<td align="right">40,809,774</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,528</td>
<td align="right">687,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,645,553</td>
<td align="right">9,643,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,126,985</td>
<td align="right">22,123,012</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">900,922,217</td>
<td align="right">900,766,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,869,877</td>
<td align="right">10,868,058</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,211,324</td>
<td align="right">9,209,804</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,914,457</td>
<td align="right">47,906,782</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,809,094</td>
<td align="right">1,808,833</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,894,812</td>
<td align="right">147,916,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,872,960</td>
<td align="right">1,873,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,745,470</td>
<td align="right">258,781,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,986,130</td>
<td align="right">67,995,241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,790,247</td>
<td align="right">72,799,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">353,471,479</td>
<td align="right">353,507,963</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">381,576,382</td>
<td align="right">381,611,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,976,624</td>
<td align="right">12,977,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,960,022</td>
<td align="right">12,961,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,967,782</td>
<td align="right">12,968,827</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,614</td>
<td align="right">214,599</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,152,236</td>
<td align="right">33,149,947</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,049,759</td>
<td align="right">133,057,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,662,773,601</td>
<td align="right">2,662,625,127</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,754,903</td>
<td align="right">1,754,819</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,670,529</td>
<td align="right">47,668,932</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,607,637</td>
<td align="right">9,607,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,280,565</td>
<td align="right">20,281,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,076,196</td>
<td align="right">231,072,782</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,382,446</td>
<td align="right">4,382,398</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,364,414</td>
<td align="right">104,363,311</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">187,856,414</td>
<td align="right">187,854,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,375,770</td>
<td align="right">1,047,383,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,218,204</td>
<td align="right">33,218,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,275,649</td>
<td align="right">148,276,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,499,187</td>
<td align="right">32,499,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,284,168</td>
<td align="right">143,283,738</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,071,417</td>
<td align="right">83,071,202</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,788,672</td>
<td align="right">278,787,957</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,122,233</td>
<td align="right">91,122,007</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,705,394</td>
<td align="right">555,706,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,039</td>
<td align="right">158,554,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,612</td>
<td align="right">46,610,644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,246</td>
<td align="right">172,973,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,306,453</td>
<td align="right">233,306,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">257,956,277</td>
<td align="right">257,956,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,012</td>
<td align="right">786,211,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,640</td>
<td align="right">173,318,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,560</td>
<td align="right">225,641,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,120</td>
<td align="right">402,022,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,527,059</td>
<td align="right">49,527,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,372</td>
<td align="right">190,039,370</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,815,341</td>
<td align="right">65,815,341</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">22,310,641</td>
<td align="right">22,310,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,056,120</td>
<td align="right">12,056,120</td>
<td align="right">0.0%</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">7,254,160</td>
<td align="right">7,254,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,760</td>
<td align="right">3,464,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">560,300</td>
<td align="right">560,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">168,940</td>
<td align="right">168,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">142,120</td>
<td align="right">142,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,600</td>
<td align="right">91,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">25,780</td>
<td align="right">25,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,580</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">17,540</td>
<td align="right">17,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,374,300,397</td>
<td align="right">95.7%</td>
<td align="right">9,368,770,263</td>
<td align="right">95.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">420,638,363</td>
<td align="right">4.3%</td>
<td align="right">420,811,304</td>
<td align="right">4.3%</td>
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
<td align="right">29,500,860</td>
<td align="right">0.3%</td>
<td align="right">29,500,860</td>
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
<td align="left">Success</td>
<td align="right">590,674</td>
<td align="right">35.1%</td>
<td align="right">590,859</td>
<td align="right">35.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,090,472</td>
<td align="right">64.9%</td>
<td align="right">1,090,469</td>
<td align="right">64.9%</td>
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
<td align="left">power</td>
<td align="right">5,507</td>
<td align="right">0.5%</td>
<td align="right">5,542</td>
<td align="right">0.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,253</td>
<td align="right">1.3%</td>
<td align="right">14,213</td>
<td align="right">1.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,021</td>
<td align="right">0.5%</td>
<td align="right">5,030</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,861</td>
<td align="right">0.8%</td>
<td align="right">8,846</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,898</td>
<td align="right">0.2%</td>
<td align="right">1,895</td>
<td align="right">0.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,422</td>
<td align="right">1.1%</td>
<td align="right">12,439</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,721</td>
<td align="right">0.4%</td>
<td align="right">4,726</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,618</td>
<td align="right">2.7%</td>
<td align="right">29,639</td>
<td align="right">2.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,604</td>
<td align="right">0.8%</td>
<td align="right">8,610</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,084</td>
<td align="right">2.9%</td>
<td align="right">32,104</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,744</td>
<td align="right">7.5%</td>
<td align="right">81,709</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,501</td>
<td align="right">1.0%</td>
<td align="right">10,505</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,937</td>
<td align="right">3.5%</td>
<td align="right">37,925</td>
<td align="right">3.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,328</td>
<td align="right">3.6%</td>
<td align="right">39,320</td>
<td align="right">3.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,613</td>
<td align="right">71.7%</td>
<td align="right">781,606</td>
<td align="right">71.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<td align="right">740,155,504</td>
<td align="right">10.9%</td>
<td align="right">736,847,822</td>
<td align="right">10.9%</td>
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
<td align="right">6,028,468,924</td>
<td align="right">89.1%</td>
<td align="right">6,014,527,070</td>
<td align="right">89.1%</td>
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
<td align="right">1,741,615</td>
<td align="right">0.0%</td>
<td align="right">1,741,464</td>
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
<td align="right">227,675</td>
<td align="right">66.9%</td>
<td align="right">226,498</td>
<td align="right">66.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">112,465</td>
<td align="right">33.1%</td>
<td align="right">112,492</td>
<td align="right">33.2%</td>
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
<td align="left">buffer slice</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">760</td>
<td align="right">0.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">121</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44,760</td>
<td align="right">19.7%</td>
<td align="right">43,880</td>
<td align="right">19.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,438</td>
<td align="right">13.4%</td>
<td align="right">30,259</td>
<td align="right">13.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">109,276</td>
<td align="right">48.0%</td>
<td align="right">109,273</td>
<td align="right">48.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.6%</td>
<td align="right">19,500</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">7.1%</td>
<td align="right">16,200</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.3%</td>
<td align="right">5,340</td>
<td align="right">2.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">160,843,153</td>
<td align="right">1.2%</td>
<td align="right">158,144,935</td>
<td align="right">1.2%</td>
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
<td align="right">677,731,586</td>
<td align="right">4.9%</td>
<td align="right">674,951,168</td>
<td align="right">4.9%</td>
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
<td align="right">13,027,766,147</td>
<td align="right">95.0%</td>
<td align="right">13,007,444,525</td>
<td align="right">95.0%</td>
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
<td align="left">Success</td>
<td align="right">3,500,259</td>
<td align="right">95.3%</td>
<td align="right">3,449,492</td>
<td align="right">95.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">174,080</td>
<td align="right">4.7%</td>
<td align="right">174,002</td>
<td align="right">4.8%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">165,700</td>
<td align="right">95.2%</td>
<td align="right">165,622</td>
<td align="right">95.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">8,040</td>
<td align="right">4.6%</td>
<td align="right">8,040</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">745,052</td>
<td align="right">0.0%</td>
<td align="right">736,275</td>
<td align="right">0.0%</td>
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
<td align="right">98,723,555</td>
<td align="right">1.6%</td>
<td align="right">97,856,123</td>
<td align="right">1.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,083,983,793</td>
<td align="right">98.4%</td>
<td align="right">6,067,483,777</td>
<td align="right">98.4%</td>
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
<td align="right">129,717</td>
<td align="right">66.9%</td>
<td align="right">129,081</td>
<td align="right">66.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">64,290</td>
<td align="right">33.1%</td>
<td align="right">64,149</td>
<td align="right">33.2%</td>
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
<td align="left">bytes</td>
<td align="right">920</td>
<td align="right">0.7%</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,381</td>
<td align="right">19.6%</td>
<td align="right">25,035</td>
<td align="right">19.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,800</td>
<td align="right">9.1%</td>
<td align="right">11,704</td>
<td align="right">9.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,740</td>
<td align="right">14.4%</td>
<td align="right">18,680</td>
<td align="right">14.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,283</td>
<td align="right">20.3%</td>
<td align="right">26,321</td>
<td align="right">20.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,368</td>
<td align="right">11.1%</td>
<td align="right">14,357</td>
<td align="right">11.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,379</td>
<td align="right">12.6%</td>
<td align="right">16,378</td>
<td align="right">12.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,580</td>
<td align="right">1.2%</td>
<td align="right">1,580</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,426</td>
<td align="right">1.1%</td>
<td align="right">1,426</td>
<td align="right">1.1%</td>
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
<td align="right">198,375,056</td>
<td align="right">7.6%</td>
<td align="right">197,824,705</td>
<td align="right">7.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,416,755,525</td>
<td align="right">92.4%</td>
<td align="right">2,412,544,892</td>
<td align="right">92.4%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">96,706</td>
<td align="right">62.2%</td>
<td align="right">96,333</td>
<td align="right">62.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,800</td>
<td align="right">37.8%</td>
<td align="right">58,799</td>
<td align="right">37.9%</td>
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
<td align="right">8,460</td>
<td align="right">8.7%</td>
<td align="right">8,340</td>
<td align="right">8.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,075</td>
<td align="right">22.8%</td>
<td align="right">21,841</td>
<td align="right">22.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,811</td>
<td align="right">13.2%</td>
<td align="right">12,792</td>
<td align="right">13.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">53,360</td>
<td align="right">55.2%</td>
<td align="right">53,360</td>
<td align="right">55.4%</td>
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
<td align="right">146,576</td>
<td align="right">0.0%</td>
<td align="right">152,695</td>
<td align="right">0.0%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">462,516,958</td>
<td align="right">49.3%</td>
<td align="right">461,360,054</td>
<td align="right">49.3%</td>
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
<td align="right">475,283,891</td>
<td align="right">50.7%</td>
<td align="right">474,804,913</td>
<td align="right">50.7%</td>
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
<td align="right">46,172</td>
<td align="right">19.7%</td>
<td align="right">46,303</td>
<td align="right">19.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">188,714</td>
<td align="right">80.3%</td>
<td align="right">188,671</td>
<td align="right">80.3%</td>
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
<td align="left">reversed list</td>
<td align="right">3,860</td>
<td align="right">2.0%</td>
<td align="right">3,760</td>
<td align="right">2.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">478</td>
<td align="right">0.3%</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">35,178</td>
<td align="right">18.6%</td>
<td align="right">35,224</td>
<td align="right">18.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,011</td>
<td align="right">5.3%</td>
<td align="right">10,020</td>
<td align="right">5.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,840</td>
<td align="right">55.6%</td>
<td align="right">104,840</td>
<td align="right">55.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,767</td>
<td align="right">5.2%</td>
<td align="right">9,767</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,500</td>
<td align="right">3.4%</td>
<td align="right">6,500</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,580</td>
<td align="right">1.9%</td>
<td align="right">3,580</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,020</td>
<td align="right">1.1%</td>
<td align="right">2,020</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
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
<td align="right">15,537,277,519</td>
<td align="right">92.5%</td>
<td align="right">15,463,143,528</td>
<td align="right">92.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,245,491,718</td>
<td align="right">7.4%</td>
<td align="right">1,242,991,776</td>
<td align="right">7.4%</td>
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
<td align="right">265,902,142</td>
<td align="right">1.6%</td>
<td align="right">265,883,103</td>
<td align="right">1.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">319,560</td>
<td align="right">0.0%</td>
<td align="right">319,560</td>
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
<td align="right">767,180</td>
<td align="right">12.2%</td>
<td align="right">765,229</td>
<td align="right">12.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,542,460</td>
<td align="right">87.8%</td>
<td align="right">5,542,176</td>
<td align="right">87.9%</td>
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
<td align="left">method</td>
<td align="right">76,753</td>
<td align="right">10.0%</td>
<td align="right">75,498</td>
<td align="right">9.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,880</td>
<td align="right">2.6%</td>
<td align="right">19,760</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,472</td>
<td align="right">1.8%</td>
<td align="right">13,435</td>
<td align="right">1.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,393</td>
<td align="right">5.9%</td>
<td align="right">45,277</td>
<td align="right">5.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,554</td>
<td align="right">0.7%</td>
<td align="right">5,544</td>
<td align="right">0.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">251,148</td>
<td align="right">32.7%</td>
<td align="right">250,871</td>
<td align="right">32.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,327</td>
<td align="right">9.6%</td>
<td align="right">73,253</td>
<td align="right">9.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">149,006</td>
<td align="right">19.4%</td>
<td align="right">148,932</td>
<td align="right">19.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">55,227</td>
<td align="right">7.2%</td>
<td align="right">55,239</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,960</td>
<td align="right">3.4%</td>
<td align="right">25,960</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,720</td>
<td align="right">1.8%</td>
<td align="right">13,720</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,120</td>
<td align="right">0.7%</td>
<td align="right">5,120</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
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
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">407,263</td>
<td align="right">0.0%</td>
<td align="right">406,029</td>
<td align="right">0.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,624,911,451</td>
<td align="right">99.6%</td>
<td align="right">5,613,645,431</td>
<td align="right">99.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,257,514</td>
<td align="right">0.4%</td>
<td align="right">20,256,586</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,620</td>
<td align="right">0.0%</td>
<td align="right">10,620</td>
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
<td align="right">430,314</td>
<td align="right">100.0%</td>
<td align="right">430,492</td>
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
<td align="right">7,881</td>
<td align="right">0.0%</td>
<td align="right">7,888</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,521,160</td>
<td align="right">100.0%</td>
<td align="right">83,584,905</td>
<td align="right">100.0%</td>
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
<td align="right">7,600</td>
<td align="right">100.0%</td>
<td align="right">7,600</td>
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
<td align="right">786,180,352</td>
<td align="right">81.9%</td>
<td align="right">786,180,399</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,300</td>
<td align="right">18.1%</td>
<td align="right">173,284,306</td>
<td align="right">18.1%</td>
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
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">99,421,182</td>
<td align="right">3.6%</td>
<td align="right">98,707,504</td>
<td align="right">3.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,671,235,135</td>
<td align="right">96.4%</td>
<td align="right">2,662,774,467</td>
<td align="right">96.4%</td>
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
<td align="right">68,867,426</td>
<td align="right">2.5%</td>
<td align="right">68,873,206</td>
<td align="right">2.5%</td>
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
<td align="right">62,262</td>
<td align="right">4.3%</td>
<td align="right">61,872</td>
<td align="right">4.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,385,147</td>
<td align="right">95.7%</td>
<td align="right">1,385,285</td>
<td align="right">95.7%</td>
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
<td align="left">property</td>
<td align="right">2,720</td>
<td align="right">4.4%</td>
<td align="right">2,580</td>
<td align="right">4.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,740</td>
<td align="right">14.0%</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,000</td>
<td align="right">20.9%</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,740</td>
<td align="right">7.6%</td>
<td align="right">4,720</td>
<td align="right">7.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,762</td>
<td align="right">15.7%</td>
<td align="right">9,772</td>
<td align="right">15.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,840</td>
<td align="right">15.8%</td>
<td align="right">9,840</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,380</td>
<td align="right">7.0%</td>
<td align="right">4,380</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
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
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">820,228,890</td>
<td align="right">78.0%</td>
<td align="right">818,380,943</td>
<td align="right">78.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,974,070</td>
<td align="right">22.0%</td>
<td align="right">230,970,658</td>
<td align="right">22.0%</td>
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
<td align="right">10,660</td>
<td align="right">10.4%</td>
<td align="right">10,663</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,466</td>
<td align="right">89.6%</td>
<td align="right">91,461</td>
<td align="right">89.6%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">7,526</td>
<td align="right">8.2%</td>
<td align="right">7,521</td>
<td align="right">8.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,200</td>
<td align="right">47.2%</td>
<td align="right">43,200</td>
<td align="right">47.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,540</td>
<td align="right">35.6%</td>
<td align="right">32,540</td>
<td align="right">35.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">920</td>
<td align="right">1.0%</td>
<td align="right">920</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">800</td>
<td align="right">0.9%</td>
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
<td align="right">273,961,660</td>
<td align="right">4.5%</td>
<td align="right">273,309,643</td>
<td align="right">4.5%</td>
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
<td align="right">5,781,792,342</td>
<td align="right">95.5%</td>
<td align="right">5,769,671,485</td>
<td align="right">95.5%</td>
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
<td align="right">49,347,209</td>
<td align="right">0.8%</td>
<td align="right">49,313,786</td>
<td align="right">0.8%</td>
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
<td align="right">172,086</td>
<td align="right">13.4%</td>
<td align="right">171,804</td>
<td align="right">13.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,107,648</td>
<td align="right">86.6%</td>
<td align="right">1,107,129</td>
<td align="right">86.6%</td>
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
<td align="right">12,900</td>
<td align="right">7.5%</td>
<td align="right">12,780</td>
<td align="right">7.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,475</td>
<td align="right">2.6%</td>
<td align="right">4,443</td>
<td align="right">2.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,246</td>
<td align="right">7.7%</td>
<td align="right">13,209</td>
<td align="right">7.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,837</td>
<td align="right">2.8%</td>
<td align="right">4,824</td>
<td align="right">2.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">48,062</td>
<td align="right">27.9%</td>
<td align="right">47,961</td>
<td align="right">27.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,833</td>
<td align="right">15.6%</td>
<td align="right">26,857</td>
<td align="right">15.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,778</td>
<td align="right">7.4%</td>
<td align="right">12,780</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,035</td>
<td align="right">26.8%</td>
<td align="right">46,030</td>
<td align="right">26.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,499,205,029</td>
<td align="right">100.0%</td>
<td align="right">1,498,661,548</td>
<td align="right">100.0%</td>
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
<td align="right">186,468</td>
<td align="right">0.0%</td>
<td align="right">186,408</td>
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
<td align="right">26,368</td>
<td align="right">93.7%</td>
<td align="right">26,416</td>
<td align="right">93.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,778</td>
<td align="right">6.3%</td>
<td align="right">1,775</td>
<td align="right">6.3%</td>
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
<td align="left">sequence</td>
<td align="right">1,138</td>
<td align="right">64.0%</td>
<td align="right">1,135</td>
<td align="right">63.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">14.6%</td>
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
<td align="right">657,926,963</td>
<td align="right">0.6%</td>
<td align="right">655,177,755</td>
<td align="right">0.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,400,008,311</td>
<td align="right">9.7%</td>
<td align="right">11,358,885,955</td>
<td align="right">9.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">41,243,685,635</td>
<td align="right">35.1%</td>
<td align="right">41,101,777,150</td>
<td align="right">35.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">64,055,147,682</td>
<td align="right">54.6%</td>
<td align="right">63,870,886,269</td>
<td align="right">54.6%</td>
<td align="right">-0.3%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">99,421,182</td>
<td align="right">2.1%</td>
<td align="right">98,707,504</td>
<td align="right">2.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">740,155,504</td>
<td align="right">15.9%</td>
<td align="right">736,847,822</td>
<td align="right">15.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">677,731,586</td>
<td align="right">14.6%</td>
<td align="right">674,951,168</td>
<td align="right">14.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">198,375,056</td>
<td align="right">4.3%</td>
<td align="right">197,824,705</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,961,660</td>
<td align="right">5.9%</td>
<td align="right">273,309,643</td>
<td align="right">5.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,245,491,718</td>
<td align="right">26.8%</td>
<td align="right">1,242,991,776</td>
<td align="right">26.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,283,891</td>
<td align="right">10.2%</td>
<td align="right">474,804,913</td>
<td align="right">10.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">420,638,363</td>
<td align="right">9.0%</td>
<td align="right">420,811,304</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">230,974,070</td>
<td align="right">5.0%</td>
<td align="right">230,970,658</td>
<td align="right">5.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,300</td>
<td align="right">3.7%</td>
<td align="right">173,284,306</td>
<td align="right">3.7%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">87,463,465</td>
<td align="right">11.9%</td>
<td align="right">85,149,382</td>
<td align="right">11.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,202,505</td>
<td align="right">3.4%</td>
<td align="right">25,210,206</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,984,086</td>
<td align="right">5.6%</td>
<td align="right">40,973,611</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,645,501</td>
<td align="right">5.9%</td>
<td align="right">43,643,580</td>
<td align="right">6.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">23,949,106</td>
<td align="right">3.3%</td>
<td align="right">23,948,547</td>
<td align="right">3.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">70,359,191</td>
<td align="right">9.6%</td>
<td align="right">70,358,344</td>
<td align="right">9.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,490,988</td>
<td align="right">3.7%</td>
<td align="right">27,491,107</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,877,747</td>
<td align="right">10.6%</td>
<td align="right">77,877,482</td>
<td align="right">10.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,877,747</td>
<td align="right">10.6%</td>
<td align="right">77,877,482</td>
<td align="right">10.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">121,604,024</td>
<td align="right">16.5%</td>
<td align="right">121,603,800</td>
<td align="right">16.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">5,650,631,335</td>
<td align="right">68.0%</td>
<td align="right">5,636,334,245</td>
<td align="right">67.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,611,408,955</td>
<td align="right">79.5%</td>
<td align="right">6,597,461,222</td>
<td align="right">79.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">370,391,935</td>
<td align="right">4.5%</td>
<td align="right">370,218,599</td>
<td align="right">4.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,800,451,664</td>
<td align="right">21.7%</td>
<td align="right">1,800,332,854</td>
<td align="right">21.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,804,885,884</td>
<td align="right">21.7%</td>
<td align="right">1,804,767,074</td>
<td align="right">21.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,665,218,606</td>
<td align="right">32.0%</td>
<td align="right">2,665,070,062</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,665,218,606</td>
<td align="right">32.0%</td>
<td align="right">2,665,070,062</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,332,722</td>
<td align="right">10.3%</td>
<td align="right">860,302,988</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,916,880</td>
<td align="right">6.3%</td>
<td align="right">526,907,665</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,577,947</td>
<td align="right">0.3%</td>
<td align="right">28,577,514</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,564,890</td>
<td align="right">0.9%</td>
<td align="right">71,565,750</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,772</td>
<td align="right">2.5%</td>
<td align="right">211,357,898</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
<td align="right">22,580</td>
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
<td align="right">6,961,154</td>
<td align="right"></td>
<td align="right">10,913,159</td>
<td align="right"></td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">26,330,994</td>
<td align="right"></td>
<td align="right">28,828,930</td>
<td align="right"></td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">21,876,349</td>
<td align="right"></td>
<td align="right">20,422,385</td>
<td align="right"></td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">50,833,521,213</td>
<td align="right">37.1%</td>
<td align="right">50,677,552,238</td>
<td align="right">37.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">68,317,721,798</td>
<td align="right">42.8%</td>
<td align="right">68,128,448,999</td>
<td align="right">42.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">104,035,884</td>
<td align="right">0.5%</td>
<td align="right">103,890,180</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">150,196,310</td>
<td align="right"></td>
<td align="right">150,000,860</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,270,792,338</td>
<td align="right">54.5%</td>
<td align="right">12,255,093,014</td>
<td align="right">54.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,394,947,160</td>
<td align="right">55.1%</td>
<td align="right">12,379,096,616</td>
<td align="right">55.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,124,531,041</td>
<td align="right"></td>
<td align="right">13,108,060,544</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">86,247,194,304</td>
<td align="right">62.9%</td>
<td align="right">86,143,039,286</td>
<td align="right">63.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,287,618,730</td>
<td align="right"></td>
<td align="right">4,282,605,126</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,632,985,075</td>
<td align="right"></td>
<td align="right">2,630,190,132</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">91,221,935,771</td>
<td align="right">57.2%</td>
<td align="right">91,131,191,906</td>
<td align="right">57.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,114,592,552</td>
<td align="right"></td>
<td align="right">10,108,218,001</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,112,755,425</td>
<td align="right">44.9%</td>
<td align="right">10,106,411,556</td>
<td align="right">44.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,118,938</td>
<td align="right">0.1%</td>
<td align="right">20,113,422</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">19,250,620</td>
<td align="right">18,435,410,107</td>
<td align="right">0</td>
<td align="right">18,574,900</td>
<td align="right">18,431,067,886</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,714,996</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,396,240</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">10,659,093,084</td>
<td align="right"></td>
<td align="right">6,959,672,086</td>
<td align="right"></td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">243,275,061,449</td>
<td align="right">2,282.3%</td>
<td align="right">239,376,148,170</td>
<td align="right">3,439.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">767</td>
<td align="right">0.1%</td>
<td align="right">776</td>
<td align="right">0.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,013</td>
<td align="right">1.1%</td>
<td align="right">11,967</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">107,434</td>
<td align="right">9.5%</td>
<td align="right">107,243</td>
<td align="right">9.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,130,734</td>
<td align="right"></td>
<td align="right">1,129,614</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,023,300</td>
<td align="right">90.5%</td>
<td align="right">1,022,371</td>
<td align="right">90.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">429,607</td>
<td align="right">38.0%</td>
<td align="right">429,399</td>
<td align="right">38.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,103</td>
<td align="right">4.0%</td>
<td align="right">45,091</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,335</td>
<td align="right">5.9%</td>
<td align="right">6,334</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,360</td>
<td align="right">0.1%</td>
<td align="right">1,360</td>
<td align="right">0.1%</td>
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
<td align="right">96,459</td>
<td align="right">89.8%</td>
<td align="right">96,270</td>
<td align="right">89.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">107,434</td>
<td align="right"></td>
<td align="right">107,243</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,307</td>
<td align="right">2.1%</td>
<td align="right">2,305</td>
<td align="right">2.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">4,499</td>
<td align="right">4.2%</td>
<td align="right">4,498</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,717</td>
<td align="right">17.4%</td>
<td align="right">18,682</td>
<td align="right">17.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">30,677</td>
<td align="right">28.6%</td>
<td align="right">30,672</td>
<td align="right">28.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">26,384</td>
<td align="right">24.6%</td>
<td align="right">26,297</td>
<td align="right">24.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">19,191</td>
<td align="right">17.9%</td>
<td align="right">19,190</td>
<td align="right">17.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,326</td>
<td align="right">5.9%</td>
<td align="right">6,264</td>
<td align="right">5.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,480</td>
<td align="right">1.4%</td>
<td align="right">1,480</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">3,639</td>
<td align="right">3.4%</td>
<td align="right">3,638</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,175</td>
<td align="right">12.3%</td>
<td align="right">13,158</td>
<td align="right">12.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,284</td>
<td align="right">19.8%</td>
<td align="right">21,276</td>
<td align="right">19.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,601</td>
<td align="right">29.4%</td>
<td align="right">31,545</td>
<td align="right">29.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,115</td>
<td align="right">15.0%</td>
<td align="right">16,073</td>
<td align="right">15.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,785</td>
<td align="right">7.2%</td>
<td align="right">7,740</td>
<td align="right">7.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,500</td>
<td align="right">2.3%</td>
<td align="right">2,480</td>
<td align="right">2.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">36,000</td>
<td align="right">17,200</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">22,284,220</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,272,159</td>
<td align="right">59,838,629</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,883,343</td>
<td align="right">88,444,964</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">92,125,963</td>
<td align="right">88,687,584</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">328,979,873</td>
<td align="right">324,854,986</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,262,149,584</td>
<td align="right">2,240,708,372</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,235,835,764</td>
<td align="right">2,217,827,912</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">115,592,388</td>
<td align="right">114,900,580</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">255,321,391</td>
<td align="right">254,193,701</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">256,548,651</td>
<td align="right">255,420,961</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">446,968</td>
<td align="right">445,008</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">182,099,683</td>
<td align="right">181,330,338</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">378,373,125</td>
<td align="right">376,940,837</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">227,932,731</td>
<td align="right">227,245,162</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,411,787,439</td>
<td align="right">6,393,054,040</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,862,326,996</td>
<td align="right">1,857,832,030</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,628,892,323</td>
<td align="right">5,615,326,394</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">7,927,760</td>
<td align="right">7,908,960</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">178,201,347</td>
<td align="right">177,870,142</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,119,911,470</td>
<td align="right">6,108,643,917</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">544,717,796</td>
<td align="right">543,866,836</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">118,413,143</td>
<td align="right">118,233,940</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">881,309,332</td>
<td align="right">880,060,483</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,922,330,567</td>
<td align="right">1,919,886,811</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,594,116</td>
<td align="right">552,895,732</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">683,725,822</td>
<td align="right">682,898,879</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">285,335,948</td>
<td align="right">284,997,534</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">186,854,814</td>
<td align="right">186,638,044</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">189,380,043</td>
<td align="right">189,163,053</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">136,770,952</td>
<td align="right">136,618,301</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,471,312</td>
<td align="right">126,336,457</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,364,700,631</td>
<td align="right">1,363,246,713</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,609,585,795</td>
<td align="right">1,607,964,641</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">959,864,551</td>
<td align="right">958,914,447</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,806,761,359</td>
<td align="right">1,805,009,411</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,670,012,718</td>
<td align="right">1,668,413,371</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">912,323,516</td>
<td align="right">911,459,662</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,322,107,766</td>
<td align="right">1,320,860,077</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">758,652,819</td>
<td align="right">757,940,012</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,128,290</td>
<td align="right">31,156,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,188,778</td>
<td align="right">134,066,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,188,778</td>
<td align="right">134,066,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,134,477</td>
<td align="right">1,818,495,912</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,213,906</td>
<td align="right">10,223,023</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,965,818,862</td>
<td align="right">6,959,672,086</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,235,452,118</td>
<td align="right">6,230,002,709</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">403,068,125</td>
<td align="right">402,727,078</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,138,755,485</td>
<td align="right">1,137,803,134</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,092,344,625</td>
<td align="right">17,078,074,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,424,307,000</td>
<td align="right">6,419,164,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,238,810,205</td>
<td align="right">1,237,857,854</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,257,468,105</td>
<td align="right">1,256,515,754</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,254,154,465</td>
<td align="right">2,252,528,793</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">996,758,110</td>
<td align="right">996,040,405</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,441,662</td>
<td align="right">78,388,155</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,975,900,969</td>
<td align="right">1,974,590,525</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">357,500,147</td>
<td align="right">357,264,175</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">123,551,092</td>
<td align="right">123,470,888</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">394,605,486</td>
<td align="right">394,349,452</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,017,039,375</td>
<td align="right">7,012,488,504</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,253,098</td>
<td align="right">89,199,355</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,925,562,932</td>
<td align="right">14,916,577,419</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,313,462,773</td>
<td align="right">1,312,674,353</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,525,746,137</td>
<td align="right">1,524,855,450</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,394,095</td>
<td align="right">93,340,476</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,833,937,036</td>
<td align="right">1,832,913,053</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,388,186</td>
<td align="right">96,334,567</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,864,497</td>
<td align="right">1,335,165,127</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">980,002,575</td>
<td align="right">979,500,386</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,089,952,511</td>
<td align="right">2,088,902,956</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,675,547,115</td>
<td align="right">3,673,785,164</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,046,642,745</td>
<td align="right">1,046,152,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,902,994,089</td>
<td align="right">2,901,689,666</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,817,916</td>
<td align="right">1,682,070,202</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,145,793</td>
<td align="right">232,245,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">647,081,601</td>
<td align="right">646,815,424</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,466,127,115</td>
<td align="right">3,464,741,536</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,160,541</td>
<td align="right">360,304,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">22,134,185</td>
<td align="right">22,125,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">150,977,155</td>
<td align="right">150,917,952</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,466,005</td>
<td align="right">48,483,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,205,101</td>
<td align="right">400,349,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">715,838,768</td>
<td align="right">715,583,307</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,172,959,355</td>
<td align="right">3,171,871,699</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,317,032</td>
<td align="right">2,316,254</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,009,143,235</td>
<td align="right">1,008,817,837</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,733,966</td>
<td align="right">133,690,875</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,912,032</td>
<td align="right">1,912,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,934,627</td>
<td align="right">342,838,981</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,075,194,297</td>
<td align="right">13,071,675,642</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">916,038,807</td>
<td align="right">915,799,643</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">625,531,853</td>
<td align="right">625,370,455</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">71,355,239</td>
<td align="right">71,373,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,035,985</td>
<td align="right">113,063,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,459,091,393</td>
<td align="right">2,458,522,942</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,236,452,769</td>
<td align="right">1,236,183,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,353,953,847</td>
<td align="right">3,353,250,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,260,422,770</td>
<td align="right">4,259,545,174</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,586,068</td>
<td align="right">91,604,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,063,901,026</td>
<td align="right">3,063,323,981</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">968,429,388</td>
<td align="right">968,253,386</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,613,150,098</td>
<td align="right">3,612,630,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,911,933</td>
<td align="right">894,040,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,166,128,181</td>
<td align="right">2,165,827,502</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,959,120</td>
<td align="right">144,940,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,735,547,521</td>
<td align="right">4,734,935,273</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,360,081,283</td>
<td align="right">4,359,544,878</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,503,376</td>
<td align="right">173,521,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,347,105</td>
<td align="right">860,258,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,105,643,091</td>
<td align="right">2,105,438,456</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,606,125,039</td>
<td align="right">1,605,975,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">320,718,297</td>
<td align="right">320,746,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">768,143,558</td>
<td align="right">768,082,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,813,956,648</td>
<td align="right">1,814,084,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,632,133,828</td>
<td align="right">9,631,463,961</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,940</td>
<td align="right">6,583,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,894,382,501</td>
<td align="right">1,894,299,178</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,011,650,854</td>
<td align="right">1,011,616,236</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,671,451</td>
<td align="right">93,668,568</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,627,782,994</td>
<td align="right">4,627,643,831</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,763,913</td>
<td align="right">229,757,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,261,673</td>
<td align="right">779,284,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,798,993</td>
<td align="right">779,821,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,401,138</td>
<td align="right">32,400,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,890,263</td>
<td align="right">4,890,171</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,214,304</td>
<td align="right">733,227,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,352,686</td>
<td align="right">280,347,810</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">143,099,660</td>
<td align="right">143,097,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,831,441,905</td>
<td align="right">2,831,403,085</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,363,042</td>
<td align="right">203,365,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,202,244</td>
<td align="right">10,202,146</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,837,170</td>
<td align="right">11,837,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,837,170</td>
<td align="right">11,837,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,571,980</td>
<td align="right">80,571,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">812,162,380</td>
<td align="right">812,156,884</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,365,716</td>
<td align="right">930,370,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">563,508,193</td>
<td align="right">563,511,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,022,596</td>
<td align="right">22,022,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,077,416,307</td>
<td align="right">1,077,420,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,364,923</td>
<td align="right">643,367,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">236,353,944</td>
<td align="right">236,353,026</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,714,274</td>
<td align="right">27,714,173</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,101,638,570</td>
<td align="right">1,101,634,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,214,116</td>
<td align="right">97,214,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,171,456</td>
<td align="right">98,171,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,838,966</td>
<td align="right">227,839,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,416,659</td>
<td align="right">330,415,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,816,460</td>
<td align="right">61,816,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,278,466,442</td>
<td align="right">1,278,464,636</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,629,686,383</td>
<td align="right">2,629,689,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,700</td>
<td align="right">213,613,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,882,931,393</td>
<td align="right">1,882,929,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,060</td>
<td align="right">3,628,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,816</td>
<td align="right">47,971,781</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,112</td>
<td align="right">35,070,096</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,692,051</td>
<td align="right">163,692,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">57,950,480</td>
<td align="right">57,950,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">58,060,120</td>
<td align="right">58,060,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,736</td>
<td align="right">101,766,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,275,676</td>
<td align="right">54,275,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,037</td>
<td align="right">384,637,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,257,052</td>
<td align="right">68,257,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">148,686,040</td>
<td align="right">148,686,073</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,198,234</td>
<td align="right">101,198,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,706,257</td>
<td align="right">909,706,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,174</td>
<td align="right">645,067,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,758</td>
<td align="right">101,193,756</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,031,031</td>
<td align="right">199,031,028</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">3,693,274,222</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,073,040</td>
<td align="right">533,073,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,980</td>
<td align="right">509,717,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,740</td>
<td align="right">230,436,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,560</td>
<td align="right">187,548,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
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
<td align="right">99,651,520</td>
<td align="right">99,651,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">66,409,000</td>
<td align="right">66,409,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,196,660</td>
<td align="right">66,196,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,794,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,140</td>
<td align="right">12,693,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,220</td>
<td align="right">8,134,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">7,891,700</td>
<td align="right">7,891,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,639,420</td>
<td align="right">5,639,420</td>
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
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,180</td>
<td align="right">3,671,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,714,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,935,140</td>
<td align="right">1,935,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,919,540</td>
<td align="right">1,919,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,881,420</td>
<td align="right">1,881,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,300</td>
<td align="right">543,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">310,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,600</td>
<td align="right">71,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
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
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">500</td>
<td align="right">480</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,530</td>
<td align="right">6,494</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">479,831</td>
<td align="right">479,056</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,398</td>
<td align="right">2,395</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,970</td>
<td align="right">40,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">33,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,100</td>
<td align="right">29,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,341</td>
<td align="right">5,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,360</td>
<td align="right">2,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">300</td>
<td align="right">300</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,087</td>
<td align="right">1,086</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,087</td>
<td align="right">1,086</td>
<td align="right">-0.1%</td>
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
<td align="right">1,880</td>
<td align="right">1,880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-06-19
