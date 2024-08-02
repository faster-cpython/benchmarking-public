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
<td align="right">4,629,458</td>
<td align="right">9,425,649</td>
<td align="right">103.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,954,703</td>
<td align="right">71,200,617</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,699,144</td>
<td align="right">15,027,188</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">781,974,555</td>
<td align="right">268,153,611</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,797,263</td>
<td align="right">77,483,035</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,127,877</td>
<td align="right">263,744,567</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,304,900</td>
<td align="right">12,305,220</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">284,104,594</td>
<td align="right">324,899,127</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,257,059</td>
<td align="right">37,984,683</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,451,828,166</td>
<td align="right">3,029,518,379</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,823,730</td>
<td align="right">3,402,720</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,809,021</td>
<td align="right">35,007,181</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,999,003,930</td>
<td align="right">5,469,340,543</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">411,057,002</td>
<td align="right">378,354,723</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,075,091</td>
<td align="right">50,775,551</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">294,248,476</td>
<td align="right">314,801,436</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">189,869,678</td>
<td align="right">202,591,698</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">374,291,846</td>
<td align="right">398,271,211</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,136,739</td>
<td align="right">210,900,095</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,985,633,271</td>
<td align="right">2,819,621,311</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,014,179,350</td>
<td align="right">1,066,511,599</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">199,833,536</td>
<td align="right">191,064,696</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,159,891</td>
<td align="right">420,702,287</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">388,147,268</td>
<td align="right">403,664,553</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">927,016,901</td>
<td align="right">962,593,750</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,868,743</td>
<td align="right">3,725,315</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,313,090</td>
<td align="right">8,609,923</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,985,570,799</td>
<td align="right">5,148,554,559</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">718,358</td>
<td align="right">695,592</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,897,283</td>
<td align="right">171,720,306</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">660,668,159</td>
<td align="right">679,375,185</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">272,068,973</td>
<td align="right">264,845,651</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,371,653</td>
<td align="right">2,431,386</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,143,370,805</td>
<td align="right">4,042,549,711</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,828,114,292</td>
<td align="right">2,895,239,304</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,271,385,841</td>
<td align="right">3,348,852,804</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">137,345,294</td>
<td align="right">134,178,509</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,935,680</td>
<td align="right">333,381,793</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,133,313,123</td>
<td align="right">4,223,531,698</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">384,377,280</td>
<td align="right">376,229,069</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">48,352,033</td>
<td align="right">49,340,497</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">191,248,213</td>
<td align="right">194,937,499</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,596,967</td>
<td align="right">1,397,303,455</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,091,121,637</td>
<td align="right">1,073,136,986</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,286,441</td>
<td align="right">24,672,804</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">682,405,190</td>
<td align="right">693,154,594</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">363,329,935</td>
<td align="right">358,057,717</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,799,490</td>
<td align="right">35,282,852</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">319,056,587</td>
<td align="right">323,187,656</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,093,063,472</td>
<td align="right">1,104,215,478</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,080,792,811</td>
<td align="right">4,121,724,137</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">528,151,541</td>
<td align="right">533,110,690</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">117,635,396</td>
<td align="right">118,720,894</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">156,805,927</td>
<td align="right">155,393,334</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,983,198,902</td>
<td align="right">1,999,326,570</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">483,726,876</td>
<td align="right">487,467,180</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,313,515</td>
<td align="right">139,282,731</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">42,459,540</td>
<td align="right">42,180,696</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">44,403,580</td>
<td align="right">44,112,403</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">321,357,038</td>
<td align="right">319,358,415</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,404,459,067</td>
<td align="right">2,419,158,580</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,053,065</td>
<td align="right">82,543,926</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,400</td>
<td align="right">47,120</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">352,494,237</td>
<td align="right">354,425,350</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,283,168</td>
<td align="right">124,946,077</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">818,013,238</td>
<td align="right">822,195,180</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">744,920</td>
<td align="right">748,700</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">894,099,028</td>
<td align="right">889,665,369</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">204,006,126</td>
<td align="right">203,117,918</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">300,055,107</td>
<td align="right">298,772,160</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">230,682,845</td>
<td align="right">231,651,027</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">38,626,672</td>
<td align="right">38,787,655</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,735,016</td>
<td align="right">327,447,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,105,646</td>
<td align="right">182,732,170</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">446,364,015</td>
<td align="right">444,878,464</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,898,496</td>
<td align="right">49,053,760</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">224,150,890</td>
<td align="right">224,837,742</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,456,458,700</td>
<td align="right">19,515,064,144</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,991,559</td>
<td align="right">146,570,762</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,143,396,127</td>
<td align="right">1,140,213,157</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,707,667</td>
<td align="right">58,865,716</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">207,771,166</td>
<td align="right">207,249,193</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,405,689,588</td>
<td align="right">1,402,281,477</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">196,157,757</td>
<td align="right">195,683,319</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">647,475,228</td>
<td align="right">645,917,268</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,928,906</td>
<td align="right">105,155,153</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,292,284,310</td>
<td align="right">1,294,875,692</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,438,264</td>
<td align="right">4,446,889</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,945,496,647</td>
<td align="right">4,954,924,090</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">782,226,395</td>
<td align="right">780,880,851</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,522,826</td>
<td align="right">17,551,308</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">50,238,234</td>
<td align="right">50,158,914</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">649,772,008</td>
<td align="right">650,784,572</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">161,030,001</td>
<td align="right">160,788,044</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">959,570</td>
<td align="right">960,853</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">70,869,146</td>
<td align="right">70,781,172</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">91,225,331</td>
<td align="right">91,326,055</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,931,453</td>
<td align="right">216,169,571</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">403,015,221</td>
<td align="right">402,587,409</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,088,714,540</td>
<td align="right">5,083,331,040</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">53,785,555</td>
<td align="right">53,729,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">778,887,854</td>
<td align="right">778,113,406</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">904,542,870</td>
<td align="right">905,407,331</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">269,019,525</td>
<td align="right">268,769,669</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,067,276</td>
<td align="right">475,479,932</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">147,047,036</td>
<td align="right">146,929,780</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">248,107,560</td>
<td align="right">248,305,298</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,655,712,454</td>
<td align="right">2,653,654,426</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,378,946</td>
<td align="right">10,386,401</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,526,673</td>
<td align="right">53,565,104</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">325,765,063</td>
<td align="right">325,534,137</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,058,199,806</td>
<td align="right">1,057,457,469</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,185,037</td>
<td align="right">21,199,716</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,667,233</td>
<td align="right">82,718,492</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,471,072</td>
<td align="right">83,424,949</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,466,400</td>
<td align="right">274,584,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,557,372</td>
<td align="right">9,561,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,127</td>
<td align="right">15,121</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">738,436,854</td>
<td align="right">738,151,783</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,853,228</td>
<td align="right">101,892,527</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,431,671</td>
<td align="right">8,434,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,958,762</td>
<td align="right">10,956,439</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">59,688,878</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,442,986</td>
<td align="right">485,533,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">335,648,397</td>
<td align="right">335,599,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,001,751</td>
<td align="right">68,008,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,805,676</td>
<td align="right">72,812,893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,732,516</td>
<td align="right">114,743,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,048,370</td>
<td align="right">48,052,605</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,888,662</td>
<td align="right">231,906,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,038,408</td>
<td align="right">9,039,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,824,104</td>
<td align="right">1,824,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,760,071</td>
<td align="right">37,762,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,876,696</td>
<td align="right">19,875,752</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">50,814,353</td>
<td align="right">50,816,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,609,792</td>
<td align="right">108,613,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,875,319,007</td>
<td align="right">1,875,265,347</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">7,461,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">433,162,732</td>
<td align="right">433,174,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,892,955</td>
<td align="right">82,895,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,354,876</td>
<td align="right">20,354,432</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,423</td>
<td align="right">173,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,996,850</td>
<td align="right">21,996,510</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,005,189</td>
<td align="right">22,004,850</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,562,879</td>
<td align="right">21,562,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,912,947</td>
<td align="right">149,911,253</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,054,183</td>
<td align="right">91,054,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,958,496</td>
<td align="right">5,958,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">37,854,280</td>
<td align="right">37,854,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224,225</td>
<td align="right">224,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">653,078</td>
<td align="right">653,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">86,199,613</td>
<td align="right">86,199,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,340,891</td>
<td align="right">233,340,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,403,174</td>
<td align="right">173,403,182</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,731</td>
<td align="right">402,103,743</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,003,897</td>
<td align="right">225,003,901</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,364</td>
<td align="right">190,039,365</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,708,782</td>
<td align="right">143,708,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,606,960</td>
<td align="right">136,606,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,774,580</td>
<td align="right">94,774,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,492,280</td>
<td align="right">92,492,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,874,001</td>
<td align="right">71,874,001</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,465,240</td>
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
<td align="right">623,340</td>
<td align="right">623,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,700</td>
<td align="right">157,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">144,080</td>
<td align="right">144,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,640</td>
<td align="right">91,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,860</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,460</td>
<td align="right">27,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,100</td>
<td align="right">21,100</td>
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
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">420</td>
<td align="right">420</td>
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
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
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
<td align="right">391,120,454</td>
<td align="right">4.0%</td>
<td align="right">385,849,745</td>
<td align="right">3.9%</td>
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
<td align="right">9,439,540,319</td>
<td align="right">96.0%</td>
<td align="right">9,439,136,515</td>
<td align="right">96.1%</td>
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
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">29,500,920</td>
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
<td align="right">1,111,796</td>
<td align="right">65.0%</td>
<td align="right">1,110,438</td>
<td align="right">65.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598,605</td>
<td align="right">35.0%</td>
<td align="right">598,454</td>
<td align="right">35.0%</td>
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
<td align="left">add different types</td>
<td align="right">48,670</td>
<td align="right">4.4%</td>
<td align="right">47,113</td>
<td align="right">4.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,000</td>
<td align="right">0.3%</td>
<td align="right">2,940</td>
<td align="right">0.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,629</td>
<td align="right">0.5%</td>
<td align="right">5,661</td>
<td align="right">0.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,555</td>
<td align="right">0.5%</td>
<td align="right">5,527</td>
<td align="right">0.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,728</td>
<td align="right">2.7%</td>
<td align="right">29,798</td>
<td align="right">2.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,709</td>
<td align="right">0.6%</td>
<td align="right">6,720</td>
<td align="right">0.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,783</td>
<td align="right">1.2%</td>
<td align="right">13,800</td>
<td align="right">1.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,659</td>
<td align="right">2.9%</td>
<td align="right">32,699</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">837</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,585</td>
<td align="right">7.3%</td>
<td align="right">81,662</td>
<td align="right">7.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,255</td>
<td align="right">1.8%</td>
<td align="right">20,274</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,725</td>
<td align="right">0.4%</td>
<td align="right">4,721</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,265</td>
<td align="right">0.7%</td>
<td align="right">7,261</td>
<td align="right">0.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,505</td>
<td align="right">0.9%</td>
<td align="right">10,501</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">46,763</td>
<td align="right">4.2%</td>
<td align="right">46,753</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,609</td>
<td align="right">70.3%</td>
<td align="right">781,611</td>
<td align="right">70.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,540</td>
<td align="right">0.9%</td>
<td align="right">9,540</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,152,502,134</td>
<td align="right">89.2%</td>
<td align="right">6,163,515,390</td>
<td align="right">89.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">742,823,307</td>
<td align="right">10.8%</td>
<td align="right">742,538,511</td>
<td align="right">10.8%</td>
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
<td align="right">4,808,664</td>
<td align="right">0.1%</td>
<td align="right">4,808,663</td>
<td align="right">0.1%</td>
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
<td align="right">240,024</td>
<td align="right">56.8%</td>
<td align="right">239,770</td>
<td align="right">56.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">182,187</td>
<td align="right">43.2%</td>
<td align="right">182,165</td>
<td align="right">43.2%</td>
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
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">121</td>
<td align="right">0.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">900</td>
<td align="right">0.4%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">56,000</td>
<td align="right">23.3%</td>
<td align="right">55,840</td>
<td align="right">23.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">16,220</td>
<td align="right">6.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">109,999</td>
<td align="right">45.8%</td>
<td align="right">109,869</td>
<td align="right">45.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,740</td>
<td align="right">12.8%</td>
<td align="right">30,740</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,480</td>
<td align="right">8.1%</td>
<td align="right">19,480</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
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
<td align="right">182,760,467</td>
<td align="right">1.3%</td>
<td align="right">181,737,773</td>
<td align="right">1.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,722,602,770</td>
<td align="right">95.4%</td>
<td align="right">13,753,854,036</td>
<td align="right">95.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">664,061,304</td>
<td align="right">4.6%</td>
<td align="right">663,148,383</td>
<td align="right">4.6%</td>
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
<td align="right">3,976,187</td>
<td align="right">96.0%</td>
<td align="right">3,957,002</td>
<td align="right">96.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,962</td>
<td align="right">4.0%</td>
<td align="right">166,044</td>
<td align="right">4.0%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">9,200</td>
<td align="right">5.5%</td>
<td align="right">9,220</td>
<td align="right">5.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">156,402</td>
<td align="right">94.2%</td>
<td align="right">156,464</td>
<td align="right">94.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,980</td>
<td align="right">1.8%</td>
<td align="right">2,980</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,000</td>
<td align="right">1.2%</td>
<td align="right">2,000</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">360</td>
<td align="right">0.2%</td>
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
<td align="right">105,769,986</td>
<td align="right">1.7%</td>
<td align="right">105,996,481</td>
<td align="right">1.7%</td>
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
<td align="right">1,071,545</td>
<td align="right">0.0%</td>
<td align="right">1,071,813</td>
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
<td align="right">6,136,930,247</td>
<td align="right">98.3%</td>
<td align="right">6,137,918,292</td>
<td align="right">98.3%</td>
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
<td align="right">153,510</td>
<td align="right">66.6%</td>
<td align="right">153,547</td>
<td align="right">66.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,955</td>
<td align="right">33.4%</td>
<td align="right">76,938</td>
<td align="right">33.4%</td>
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
<td align="left">tuple</td>
<td align="right">12,220</td>
<td align="right">8.0%</td>
<td align="right">12,184</td>
<td align="right">7.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,423</td>
<td align="right">0.9%</td>
<td align="right">1,426</td>
<td align="right">0.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,994</td>
<td align="right">28.7%</td>
<td align="right">44,049</td>
<td align="right">28.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,849</td>
<td align="right">11.0%</td>
<td align="right">16,857</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,081</td>
<td align="right">17.6%</td>
<td align="right">27,093</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,383</td>
<td align="right">9.4%</td>
<td align="right">14,378</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,080</td>
<td align="right">12.4%</td>
<td align="right">19,080</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,600</td>
<td align="right">2.3%</td>
<td align="right">3,600</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.8%</td>
<td align="right">2,700</td>
<td align="right">1.8%</td>
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
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">580</td>
<td align="right">0.4%</td>
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
<td align="right">206,377,028</td>
<td align="right">7.6%</td>
<td align="right">205,488,888</td>
<td align="right">7.6%</td>
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
<td align="right">2,492,193,532</td>
<td align="right">92.3%</td>
<td align="right">2,495,030,958</td>
<td align="right">92.4%</td>
<td align="right">0.1%</td>
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
<td align="right">114,039</td>
<td align="right">65.0%</td>
<td align="right">113,970</td>
<td align="right">65.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,299</td>
<td align="right">35.0%</td>
<td align="right">61,300</td>
<td align="right">35.0%</td>
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
<td align="right">15,975</td>
<td align="right">14.0%</td>
<td align="right">16,013</td>
<td align="right">14.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">55,840</td>
<td align="right">49.0%</td>
<td align="right">55,720</td>
<td align="right">48.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,800</td>
<td align="right">12.1%</td>
<td align="right">13,780</td>
<td align="right">12.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">28,424</td>
<td align="right">24.9%</td>
<td align="right">28,457</td>
<td align="right">25.0%</td>
<td align="right">0.1%</td>
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
<td align="right">544,841,693</td>
<td align="right">53.3%</td>
<td align="right">576,729,718</td>
<td align="right">54.7%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,577,311</td>
<td align="right">0.3%</td>
<td align="right">2,593,783</td>
<td align="right">0.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">477,353,010</td>
<td align="right">46.7%</td>
<td align="right">477,781,215</td>
<td align="right">45.3%</td>
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
<td align="right">194,710</td>
<td align="right">66.8%</td>
<td align="right">195,377</td>
<td align="right">66.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">96,867</td>
<td align="right">33.2%</td>
<td align="right">97,123</td>
<td align="right">33.2%</td>
<td align="right">0.3%</td>
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
<td align="right">3,800</td>
<td align="right">2.0%</td>
<td align="right">4,180</td>
<td align="right">2.1%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,560</td>
<td align="right">3.4%</td>
<td align="right">6,800</td>
<td align="right">3.5%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,031</td>
<td align="right">5.2%</td>
<td align="right">9,953</td>
<td align="right">5.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,715</td>
<td align="right">17.8%</td>
<td align="right">34,856</td>
<td align="right">17.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,120</td>
<td align="right">2.6%</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,425</td>
<td align="right">5.9%</td>
<td align="right">11,428</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.9%</td>
<td align="right">104,960</td>
<td align="right">53.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,560</td>
<td align="right">3.4%</td>
<td align="right">6,560</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,500</td>
<td align="right">2.3%</td>
<td align="right">4,500</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,660</td>
<td align="right">1.9%</td>
<td align="right">3,660</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.1%</td>
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
<td align="right">1,497,255,122</td>
<td align="right">8.5%</td>
<td align="right">1,507,843,474</td>
<td align="right">8.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">413,585,105</td>
<td align="right">2.3%</td>
<td align="right">413,014,066</td>
<td align="right">2.3%</td>
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
<td align="right">16,158,640,386</td>
<td align="right">91.5%</td>
<td align="right">16,164,178,258</td>
<td align="right">91.4%</td>
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
<td align="right">304,720</td>
<td align="right">0.0%</td>
<td align="right">304,720</td>
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
<td align="right">972,909</td>
<td align="right">10.4%</td>
<td align="right">976,363</td>
<td align="right">10.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,420,546</td>
<td align="right">89.6%</td>
<td align="right">8,409,707</td>
<td align="right">89.6%</td>
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
<td align="left">class method obj</td>
<td align="right">14,420</td>
<td align="right">1.5%</td>
<td align="right">18,380</td>
<td align="right">1.9%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,880</td>
<td align="right">0.3%</td>
<td align="right">2,900</td>
<td align="right">0.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,180</td>
<td align="right">1.6%</td>
<td align="right">15,260</td>
<td align="right">1.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,667</td>
<td align="right">7.8%</td>
<td align="right">76,029</td>
<td align="right">7.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,638</td>
<td align="right">27.1%</td>
<td align="right">262,518</td>
<td align="right">26.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,830</td>
<td align="right">0.6%</td>
<td align="right">5,814</td>
<td align="right">0.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">88,201</td>
<td align="right">9.1%</td>
<td align="right">88,425</td>
<td align="right">9.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">101,942</td>
<td align="right">10.5%</td>
<td align="right">101,813</td>
<td align="right">10.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">163,178</td>
<td align="right">16.8%</td>
<td align="right">163,221</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">157,118</td>
<td align="right">16.1%</td>
<td align="right">157,150</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,675</td>
<td align="right">1.8%</td>
<td align="right">17,673</td>
<td align="right">1.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">27,080</td>
<td align="right">2.8%</td>
<td align="right">27,080</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,300</td>
<td align="right">2.1%</td>
<td align="right">20,300</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.3%</td>
<td align="right">12,200</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
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
<td align="right">5,376,248,704</td>
<td align="right">99.6%</td>
<td align="right">5,472,277,481</td>
<td align="right">99.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">444,122</td>
<td align="right">0.0%</td>
<td align="right">445,008</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,331,301</td>
<td align="right">0.4%</td>
<td align="right">20,331,921</td>
<td align="right">0.4%</td>
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
<td align="right">11,380</td>
<td align="right">0.0%</td>
<td align="right">11,380</td>
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
<td align="right">467,697</td>
<td align="right">100.0%</td>
<td align="right">467,519</td>
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
<td align="right">7,587</td>
<td align="right">0.0%</td>
<td align="right">7,581</td>
<td align="right">0.0%</td>
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
<td align="right">84,521,257</td>
<td align="right">100.0%</td>
<td align="right">84,572,617</td>
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
<td align="right">7,540</td>
<td align="right">100.0%</td>
<td align="right">7,540</td>
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
<td align="right">786,230,789</td>
<td align="right">81.9%</td>
<td align="right">786,230,873</td>
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
<td align="right">173,365,454</td>
<td align="right">18.1%</td>
<td align="right">173,365,462</td>
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
<td align="right">27,480</td>
<td align="right">0.0%</td>
<td align="right">27,480</td>
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
<td align="right">5,440</td>
<td align="right">8.3%</td>
<td align="right">5,440</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,760</td>
<td align="right">91.7%</td>
<td align="right">59,760</td>
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
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.8%</td>
<td align="right">14,240</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
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
<td align="right">142,243,489</td>
<td align="right">4.8%</td>
<td align="right">139,320,039</td>
<td align="right">4.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,184,677</td>
<td align="right">6.5%</td>
<td align="right">187,318,408</td>
<td align="right">6.4%</td>
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
<td align="right">2,741,717,302</td>
<td align="right">93.4%</td>
<td align="right">2,741,005,695</td>
<td align="right">93.5%</td>
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
<td align="right">2,781,835</td>
<td align="right">96.8%</td>
<td align="right">2,726,662</td>
<td align="right">96.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,330</td>
<td align="right">3.2%</td>
<td align="right">91,382</td>
<td align="right">3.2%</td>
<td align="right">0.1%</td>
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
<td align="right">840</td>
<td align="right">0.9%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,730</td>
<td align="right">10.7%</td>
<td align="right">9,722</td>
<td align="right">10.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,400</td>
<td align="right">34.4%</td>
<td align="right">31,420</td>
<td align="right">34.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,040</td>
<td align="right">15.4%</td>
<td align="right">14,040</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.6%</td>
<td align="right">8,760</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.2%</td>
<td align="right">7,480</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,400</td>
<td align="right">7.0%</td>
<td align="right">6,400</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,960</td>
<td align="right">5.4%</td>
<td align="right">4,960</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,760</td>
<td align="right">5.2%</td>
<td align="right">4,760</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
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
<td align="right">877,406,122</td>
<td align="right">79.1%</td>
<td align="right">878,323,451</td>
<td align="right">79.1%</td>
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
<td align="right">231,778,581</td>
<td align="right">20.9%</td>
<td align="right">231,796,776</td>
<td align="right">20.9%</td>
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
<td align="left">Failure</td>
<td align="right">99,818</td>
<td align="right">88.3%</td>
<td align="right">99,884</td>
<td align="right">88.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,163</td>
<td align="right">11.7%</td>
<td align="right">13,160</td>
<td align="right">11.6%</td>
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
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,518</td>
<td align="right">7.5%</td>
<td align="right">7,464</td>
<td align="right">7.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,580</td>
<td align="right">39.7%</td>
<td align="right">39,660</td>
<td align="right">39.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
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
<td align="right">55,724,016</td>
<td align="right">0.9%</td>
<td align="right">27,510,343</td>
<td align="right">0.4%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">243,990,428</td>
<td align="right">3.8%</td>
<td align="right">228,987,818</td>
<td align="right">3.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,132,159,682</td>
<td align="right">96.1%</td>
<td align="right">6,120,426,446</td>
<td align="right">96.4%</td>
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
<td align="right">1,245,926</td>
<td align="right">77.7%</td>
<td align="right">713,545</td>
<td align="right">64.0%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">357,340</td>
<td align="right">22.3%</td>
<td align="right">400,678</td>
<td align="right">36.0%</td>
<td align="right">12.1%</td>
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
<td align="left">mapping</td>
<td align="right">55,241</td>
<td align="right">15.5%</td>
<td align="right">95,944</td>
<td align="right">23.9%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">14,820</td>
<td align="right">4.1%</td>
<td align="right">17,440</td>
<td align="right">4.4%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,142</td>
<td align="right">1.4%</td>
<td align="right">5,045</td>
<td align="right">1.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,906</td>
<td align="right">3.9%</td>
<td align="right">13,940</td>
<td align="right">3.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,273</td>
<td align="right">22.7%</td>
<td align="right">81,363</td>
<td align="right">20.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,487</td>
<td align="right">37.9%</td>
<td align="right">135,472</td>
<td align="right">33.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">36,732</td>
<td align="right">10.3%</td>
<td align="right">36,736</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,139</td>
<td align="right">3.4%</td>
<td align="right">12,138</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">720</td>
<td align="right">0.2%</td>
<td align="right">720</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,571,876,048</td>
<td align="right">100.0%</td>
<td align="right">1,584,139,553</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,801</td>
<td align="right">0.0%</td>
<td align="right">194,841</td>
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
<td align="left">Success</td>
<td align="right">30,648</td>
<td align="right">94.3%</td>
<td align="right">30,608</td>
<td align="right">94.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,856</td>
<td align="right">5.7%</td>
<td align="right">1,857</td>
<td align="right">5.7%</td>
<td align="right">0.1%</td>
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
<td align="right">1,216</td>
<td align="right">65.5%</td>
<td align="right">1,217</td>
<td align="right">65.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
<td align="right">14.0%</td>
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
<td align="right">913,194,531</td>
<td align="right">0.8%</td>
<td align="right">880,481,351</td>
<td align="right">0.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">38,553,019,401</td>
<td align="right">34.5%</td>
<td align="right">37,657,481,906</td>
<td align="right">34.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">61,384,361,042</td>
<td align="right">54.9%</td>
<td align="right">60,779,642,658</td>
<td align="right">55.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,052,388,648</td>
<td align="right">9.9%</td>
<td align="right">11,138,913,605</td>
<td align="right">10.1%</td>
<td align="right">0.8%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">243,990,428</td>
<td align="right">4.9%</td>
<td align="right">228,987,818</td>
<td align="right">4.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,184,677</td>
<td align="right">3.8%</td>
<td align="right">187,318,408</td>
<td align="right">3.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">391,120,454</td>
<td align="right">7.9%</td>
<td align="right">385,849,745</td>
<td align="right">7.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,497,255,122</td>
<td align="right">30.3%</td>
<td align="right">1,507,843,474</td>
<td align="right">30.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">206,377,028</td>
<td align="right">4.2%</td>
<td align="right">205,488,888</td>
<td align="right">4.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">664,061,304</td>
<td align="right">13.4%</td>
<td align="right">663,148,383</td>
<td align="right">13.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">477,353,010</td>
<td align="right">9.7%</td>
<td align="right">477,781,215</td>
<td align="right">9.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">742,823,307</td>
<td align="right">15.0%</td>
<td align="right">742,538,511</td>
<td align="right">15.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,778,581</td>
<td align="right">4.7%</td>
<td align="right">231,796,776</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,365,454</td>
<td align="right">3.5%</td>
<td align="right">173,365,462</td>
<td align="right">3.5%</td>
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
<td align="right">100,400,275</td>
<td align="right">10.1%</td>
<td align="right">106,131,817</td>
<td align="right">11.1%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">117,520,540</td>
<td align="right">11.9%</td>
<td align="right">115,127,402</td>
<td align="right">12.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">170,635,769</td>
<td align="right">17.2%</td>
<td align="right">169,143,876</td>
<td align="right">17.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">126,611,352</td>
<td align="right">12.8%</td>
<td align="right">127,536,098</td>
<td align="right">13.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">52,823,428</td>
<td align="right">5.3%</td>
<td align="right">52,848,308</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,825</td>
<td align="right">2.8%</td>
<td align="right">27,496,999</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,555,018</td>
<td align="right">3.6%</td>
<td align="right">35,554,882</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,899,192</td>
<td align="right">7.9%</td>
<td align="right">77,899,243</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,899,192</td>
<td align="right">7.9%</td>
<td align="right">77,899,243</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,414,840</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,168,977</td>
<td align="right">2.5%</td>
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
<td align="right">4,417,720</td>
<td align="right">0.1%</td>
<td align="right">5,297,800</td>
<td align="right">0.1%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">85,570,903</td>
<td align="right">1.0%</td>
<td align="right">84,864,551</td>
<td align="right">1.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,092,596,800</td>
<td align="right">69.6%</td>
<td align="right">6,129,510,185</td>
<td align="right">69.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,754,388</td>
<td align="right">9.8%</td>
<td align="right">856,949,691</td>
<td align="right">9.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,991,946,589</td>
<td align="right">79.9%</td>
<td align="right">7,002,059,482</td>
<td align="right">79.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,660,108,939</td>
<td align="right">30.4%</td>
<td align="right">2,657,673,531</td>
<td align="right">30.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,660,108,939</td>
<td align="right">30.4%</td>
<td align="right">2,657,673,531</td>
<td align="right">30.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">351,027,641</td>
<td align="right">4.0%</td>
<td align="right">351,311,843</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,799,354,551</td>
<td align="right">20.6%</td>
<td align="right">1,800,723,840</td>
<td align="right">20.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,794,907,971</td>
<td align="right">20.5%</td>
<td align="right">1,795,397,180</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">551,306,914</td>
<td align="right">6.3%</td>
<td align="right">551,364,227</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,096,558</td>
<td align="right">0.4%</td>
<td align="right">31,096,846</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,065</td>
<td align="right">2.0%</td>
<td align="right">175,480,144</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
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
<td align="left">Method cache misses</td>
<td align="right">64,114,828</td>
<td align="right"></td>
<td align="right">68,265,080</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">73,171,231</td>
<td align="right"></td>
<td align="right">77,329,541</td>
<td align="right"></td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">99,020,610,869</td>
<td align="right">59.9%</td>
<td align="right">99,455,767,633</td>
<td align="right">60.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">66,337,044,977</td>
<td align="right">40.1%</td>
<td align="right">66,106,591,612</td>
<td align="right">39.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,251,867,278</td>
<td align="right"></td>
<td align="right">3,262,334,517</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,886,454,569</td>
<td align="right"></td>
<td align="right">11,906,577,951</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,884,552,301</td>
<td align="right">48.0%</td>
<td align="right">11,904,670,499</td>
<td align="right">48.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,088,169,145</td>
<td align="right">64.6%</td>
<td align="right">92,242,338,471</td>
<td align="right">64.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,586,625,986</td>
<td align="right"></td>
<td align="right">13,605,779,637</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,774,108,070</td>
<td align="right">51.6%</td>
<td align="right">12,789,131,606</td>
<td align="right">51.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,883,912,744</td>
<td align="right">52.0%</td>
<td align="right">12,898,957,212</td>
<td align="right">52.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,042,363</td>
<td align="right"></td>
<td align="right">10,049,688</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,580,269,075</td>
<td align="right"></td>
<td align="right">4,583,468,303</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">50,379,481,680</td>
<td align="right">35.4%</td>
<td align="right">50,401,333,610</td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,370,695</td>
<td align="right">0.4%</td>
<td align="right">94,390,850</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">163,345,534</td>
<td align="right"></td>
<td align="right">163,374,950</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,433,979</td>
<td align="right">0.1%</td>
<td align="right">15,434,756</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,140</td>
<td align="right">2.1%</td>
<td align="right">3,382,140</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,920</td>
<td align="right">0.1%</td>
<td align="right">127,920</td>
<td align="right">0.1%</td>
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
<td align="right">115,218,200</td>
<td align="right">19,561,989,603</td>
<td align="right">0</td>
<td align="right">115,310,660</td>
<td align="right">19,533,436,396</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,703,212</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,600,824</td>
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
<td align="right">98,882</td>
<td align="right">10.1%</td>
<td align="right">16,634</td>
<td align="right">1.8%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,978</td>
<td align="right">1.3%</td>
<td align="right">18,739</td>
<td align="right">2.0%</td>
<td align="right">44.4%</td>
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
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,339</td>
<td align="right">0.1%</td>
<td align="right">1,068</td>
<td align="right">0.1%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">132,314</td>
<td align="right">13.5%</td>
<td align="right">148,418</td>
<td align="right">15.8%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">848,407</td>
<td align="right">86.5%</td>
<td align="right">786,938</td>
<td align="right">84.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,780</td>
<td align="right">0.2%</td>
<td align="right">1,880</td>
<td align="right">0.2%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,109</td>
<td align="right">5.4%</td>
<td align="right">7,458</td>
<td align="right">5.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">980,721</td>
<td align="right"></td>
<td align="right">936,424</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">532,531</td>
<td align="right">54.3%</td>
<td align="right">554,530</td>
<td align="right">59.2%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">262,541,413,935</td>
<td align="right">3,660.1%</td>
<td align="right">264,603,960,315</td>
<td align="right">3,689.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,172,997,961</td>
<td align="right"></td>
<td align="right">7,171,535,553</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">132,314</td>
<td align="right"></td>
<td align="right">148,418</td>
<td align="right"></td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">117,310</td>
<td align="right">88.7%</td>
<td align="right">129,063</td>
<td align="right">87.0%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,504</td>
<td align="right">1.9%</td>
<td align="right">2,447</td>
<td align="right">1.6%</td>
<td align="right">-2.3%</td>
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
<td align="right">5,778</td>
<td align="right">4.4%</td>
<td align="right">11,951</td>
<td align="right">8.1%</td>
<td align="right">106.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,445</td>
<td align="right">16.2%</td>
<td align="right">19,817</td>
<td align="right">13.4%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">37,211</td>
<td align="right">28.1%</td>
<td align="right">37,340</td>
<td align="right">25.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">32,893</td>
<td align="right">24.9%</td>
<td align="right">34,556</td>
<td align="right">23.3%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22,845</td>
<td align="right">17.3%</td>
<td align="right">27,630</td>
<td align="right">18.6%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,942</td>
<td align="right">7.5%</td>
<td align="right">14,064</td>
<td align="right">9.5%</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,040</td>
<td align="right">1.5%</td>
<td align="right">2,860</td>
<td align="right">1.9%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">25.0%</td>
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
<td align="right">4,598</td>
<td align="right">3.5%</td>
<td align="right">10,477</td>
<td align="right">7.1%</td>
<td align="right">127.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">15,006</td>
<td align="right">11.3%</td>
<td align="right">14,158</td>
<td align="right">9.5%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,650</td>
<td align="right">19.4%</td>
<td align="right">24,339</td>
<td align="right">16.4%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">38,204</td>
<td align="right">28.9%</td>
<td align="right">39,007</td>
<td align="right">26.3%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21,032</td>
<td align="right">15.9%</td>
<td align="right">24,280</td>
<td align="right">16.4%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,220</td>
<td align="right">7.0%</td>
<td align="right">12,046</td>
<td align="right">8.1%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,160</td>
<td align="right">2.4%</td>
<td align="right">4,096</td>
<td align="right">2.8%</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">440</td>
<td align="right">0.3%</td>
<td align="right">660</td>
<td align="right">0.4%</td>
<td align="right">50.0%</td>
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
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">4,440,174</td>
<td align="right">518,261,202</td>
<td align="right">11,572.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,760</td>
<td align="right">32,493,780</td>
<td align="right">3,854.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">169,340</td>
<td align="right">325.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,967,580</td>
<td align="right">12,001,620</td>
<td align="right">304.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,111,517,408</td>
<td align="right">9,655,661,995</td>
<td align="right">210.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">12,100</td>
<td align="right">35,020</td>
<td align="right">189.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">292,231,786</td>
<td align="right">835,396,072</td>
<td align="right">185.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,608,934,592</td>
<td align="right">822,266,085</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,652,240</td>
<td align="right">736,200</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,667,540</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,520,292,358</td>
<td align="right">1,992,415,698</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,119,897,558</td>
<td align="right">2,657,706,268</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">123,399,418</td>
<td align="right">151,570,626</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">62,033,400</td>
<td align="right">73,468,960</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">101,126,430</td>
<td align="right">117,328,553</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">101,370,290</td>
<td align="right">117,572,413</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,469,759,213</td>
<td align="right">2,998,167,761</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">29,132,969</td>
<td align="right">25,374,134</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">214,842,900</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,966,993</td>
<td align="right">13,261,578</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,970,533</td>
<td align="right">13,265,118</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">34,421,493</td>
<td align="right">38,074,210</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">912,366,978</td>
<td align="right">832,285,606</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">346,014,909</td>
<td align="right">375,271,550</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,831,758,076</td>
<td align="right">6,286,792,310</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,906,260</td>
<td align="right">63,986,460</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">62,940,240</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,164,022</td>
<td align="right">252,349,053</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,989,520</td>
<td align="right">57,791,360</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,159,582</td>
<td align="right">374,994,627</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">90,118,090</td>
<td align="right">86,270,773</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,732,524,100</td>
<td align="right">2,840,989,509</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">205,055,970</td>
<td align="right">197,040,353</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,486,145,053</td>
<td align="right">2,583,073,735</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,541,553,833</td>
<td align="right">2,638,412,635</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,361,720</td>
<td align="right">47,958,442</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,184,294,639</td>
<td align="right">2,111,980,848</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">304,075,590</td>
<td align="right">313,267,388</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,864,000</td>
<td align="right">55,460,722</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">18,869,416,098</td>
<td align="right">19,427,850,931</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">863,236,654</td>
<td align="right">838,345,582</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,478,599</td>
<td align="right">768,442,559</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,768,098</td>
<td align="right">94,319,443</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">68,309,099</td>
<td align="right">70,143,460</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">823,472,057</td>
<td align="right">801,640,390</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,107,171,074</td>
<td align="right">1,079,280,992</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">50,666,511</td>
<td align="right">49,452,058</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,471,899,965</td>
<td align="right">16,084,825,938</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,615,530,989</td>
<td align="right">1,578,973,843</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">319,569,424</td>
<td align="right">312,379,405</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">122,108,083</td>
<td align="right">124,543,115</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">945,777,394</td>
<td align="right">927,082,308</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">461,052,034</td>
<td align="right">470,080,500</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,763,652,548</td>
<td align="right">4,686,385,461</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,140,699</td>
<td align="right">115,974,407</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,696,767,409</td>
<td align="right">1,722,949,239</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,897,892</td>
<td align="right">2,942,112</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,631,999,780</td>
<td align="right">4,561,558,450</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">68,244,083</td>
<td align="right">69,082,393</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">230,998,564</td>
<td align="right">233,735,176</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,941,751,436</td>
<td align="right">7,023,858,138</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,011,263,844</td>
<td align="right">2,034,472,097</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,685,235,758</td>
<td align="right">1,666,442,980</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,362,260</td>
<td align="right">11,487,660</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,637,550</td>
<td align="right">90,587,369</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,274,392,563</td>
<td align="right">2,298,250,119</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,581,731</td>
<td align="right">162,899,475</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,033,066,329</td>
<td align="right">2,013,700,313</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,350,265,542</td>
<td align="right">7,419,478,691</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,310,050</td>
<td align="right">136,568,898</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,310,050</td>
<td align="right">136,568,898</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">399,462,486</td>
<td align="right">403,112,610</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">668,967,809</td>
<td align="right">663,012,598</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,295,482,228</td>
<td align="right">6,243,231,244</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,421,815,051</td>
<td align="right">10,335,621,074</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,247,619,739</td>
<td align="right">3,220,961,314</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,332,508,725</td>
<td align="right">2,351,499,117</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">143,661,030</td>
<td align="right">144,807,224</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,133,577</td>
<td align="right">6,181,544</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">35,820</td>
<td align="right">36,100</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">169,417,154</td>
<td align="right">168,097,487</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,609,963,875</td>
<td align="right">1,597,771,081</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,743,282</td>
<td align="right">10,820,630</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,414,864,189</td>
<td align="right">1,424,905,199</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">703,022,655</td>
<td align="right">707,834,333</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,647,691,069</td>
<td align="right">3,623,273,659</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,201,609,192</td>
<td align="right">1,209,602,403</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,294,990,721</td>
<td align="right">4,323,163,715</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,335,096,638</td>
<td align="right">2,350,247,447</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">46,110,207</td>
<td align="right">46,405,059</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">181,984,751</td>
<td align="right">183,139,359</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,319,665,052</td>
<td align="right">1,327,893,863</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,340,825,592</td>
<td align="right">1,349,052,063</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,515,980</td>
<td align="right">45,794,824</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,329,845,521</td>
<td align="right">6,367,211,393</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,934,767</td>
<td align="right">97,471,419</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,109,542,889</td>
<td align="right">1,115,445,152</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,849,870,235</td>
<td align="right">3,830,742,353</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">96,953,100</td>
<td align="right">97,426,340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,051,901,995</td>
<td align="right">1,047,240,438</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,753,952</td>
<td align="right">68,464,028</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,637,090,249</td>
<td align="right">3,621,950,580</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,703,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">660,617,386</td>
<td align="right">663,202,468</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">576,177,561</td>
<td align="right">578,311,912</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,189</td>
<td align="right">901,140,687</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">130,569,286</td>
<td align="right">130,970,866</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">278,533,069</td>
<td align="right">277,708,784</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,810,417,646</td>
<td align="right">1,805,094,765</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">854,899</td>
<td align="right">852,390</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,340,614</td>
<td align="right">322,249,384</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,363,182,750</td>
<td align="right">2,369,756,576</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">422,624,968</td>
<td align="right">421,550,953</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">286,803,160</td>
<td align="right">286,089,831</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">437,878,244</td>
<td align="right">438,908,415</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">516,720,184</td>
<td align="right">517,922,394</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,560,560</td>
<td align="right">64,709,037</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">674,582,396</td>
<td align="right">676,077,015</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,349,280,034</td>
<td align="right">14,380,332,031</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,992,237,606</td>
<td align="right">1,988,055,680</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">205,135,065</td>
<td align="right">204,711,337</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">238,928,212</td>
<td align="right">239,413,954</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">980,602,290</td>
<td align="right">982,497,845</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,277,568,764</td>
<td align="right">5,267,509,151</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">975,507,351</td>
<td align="right">973,661,209</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">898,328,242</td>
<td align="right">899,999,774</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">96,677,180</td>
<td align="right">96,854,320</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">143,352,484</td>
<td align="right">143,599,971</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">248,476,860</td>
<td align="right">248,049,260</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">558,993,339</td>
<td align="right">559,908,682</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,134,067,200</td>
<td align="right">1,135,924,179</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,863,614</td>
<td align="right">78,736,953</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,279,160</td>
<td align="right">110,452,260</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,635,460</td>
<td align="right">163,889,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,535,892,418</td>
<td align="right">1,533,578,097</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">390,080,189</td>
<td align="right">390,653,738</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">391,307,449</td>
<td align="right">391,880,998</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">78,842,884</td>
<td align="right">78,956,499</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,231,224</td>
<td align="right">94,102,273</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">188,200,920</td>
<td align="right">188,442,680</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,083,480,071</td>
<td align="right">2,080,828,712</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,892,349</td>
<td align="right">229,609,052</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,750,689,286</td>
<td align="right">1,752,686,876</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,254,326,800</td>
<td align="right">1,255,679,372</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,930,044</td>
<td align="right">1,347,266,240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,502,175,993</td>
<td align="right">1,503,665,827</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,119,000</td>
<td align="right">533,598,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">993,856,934</td>
<td align="right">994,723,845</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,826,353,121</td>
<td align="right">1,827,923,061</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,884,060,826</td>
<td align="right">1,885,509,201</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,014</td>
<td align="right">10,235,247</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,688,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,362,035,956</td>
<td align="right">1,362,898,691</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,867,189</td>
<td align="right">35,888,091</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">962,146,368</td>
<td align="right">961,600,075</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,615,410,513</td>
<td align="right">1,616,251,428</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">863,138,205</td>
<td align="right">862,692,722</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,468,119,616</td>
<td align="right">3,466,474,734</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,557,900</td>
<td align="right">8,553,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">908,788,823</td>
<td align="right">908,380,089</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">9,784,600</td>
<td align="right">9,780,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">501,229</td>
<td align="right">501,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">275,519,217</td>
<td align="right">275,624,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,715,054</td>
<td align="right">90,687,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,172,997,961</td>
<td align="right">7,171,535,553</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,334,236</td>
<td align="right">2,334,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">670,085</td>
<td align="right">670,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">539,252,160</td>
<td align="right">539,331,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,761,287</td>
<td align="right">778,649,024</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,356,830,267</td>
<td align="right">1,356,638,971</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">252,784,685</td>
<td align="right">252,818,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">256,327,813</td>
<td align="right">256,361,803</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,894,865,276</td>
<td align="right">2,895,119,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,651,140</td>
<td align="right">5,650,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,406,188</td>
<td align="right">32,408,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">200,315,580</td>
<td align="right">200,328,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,663,210</td>
<td align="right">731,628,612</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,836,619,417</td>
<td align="right">1,836,700,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,223,967</td>
<td align="right">778,194,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">644,043,701</td>
<td align="right">644,025,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">54,628,740</td>
<td align="right">54,627,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">397,652,482</td>
<td align="right">397,644,228</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">161,471,819</td>
<td align="right">161,468,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,469,011</td>
<td align="right">81,467,725</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,636,040</td>
<td align="right">5,635,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,993,760</td>
<td align="right">173,991,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,611,548,891</td>
<td align="right">5,611,514,593</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,789,196</td>
<td align="right">3,789,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,265,714</td>
<td align="right">4,265,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,503</td>
<td align="right">97,230,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,195,683</td>
<td align="right">98,195,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,636,622</td>
<td align="right">122,636,824</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,965,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,969</td>
<td align="right">384,637,987</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,710,819</td>
<td align="right">131,710,815</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,068,474</td>
<td align="right">645,068,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,930,900</td>
<td align="right">4,930,900</td>
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
<td align="right">3,065,760</td>
<td align="right">3,065,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,024,860</td>
<td align="right">3,024,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,800,040</td>
<td align="right">1,800,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,225,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">582,020</td>
<td align="right">582,020</td>
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
<td align="right">1,180</td>
<td align="right">1,480</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,840</td>
<td align="right">4,600</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,939</td>
<td align="right">7,723</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">680</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">31,680</td>
<td align="right">34,420</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">35,900</td>
<td align="right">36,260</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">157,142</td>
<td align="right">158,283</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">45,399</td>
<td align="right">45,630</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">820</td>
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
<td align="right">1,105</td>
<td align="right">1,107</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,105</td>
<td align="right">1,107</td>
<td align="right">0.2%</td>
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
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">1,800</td>
<td align="right">1,800</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-07-26
