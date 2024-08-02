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
<td align="left">UNARY_INVERT</td>
<td align="right">1,700,349</td>
<td align="right">2,512,465</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,870,456</td>
<td align="right">2,432,595</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,333,471,165</td>
<td align="right">2,736,578,091</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">134,502,899</td>
<td align="right">111,397,400</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,509,658,637</td>
<td align="right">5,041,305,193</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,646,534</td>
<td align="right">8,104,137</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">53,597,983</td>
<td align="right">50,845,974</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,110,204,718</td>
<td align="right">2,985,007,468</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">8,419,765</td>
<td align="right">8,724,551</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,288,722</td>
<td align="right">88,330,170</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">44,483,661</td>
<td align="right">45,299,732</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">118,073,512</td>
<td align="right">120,149,971</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,209,286</td>
<td align="right">9,365,108</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,573,289</td>
<td align="right">82,924,447</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">172,497,745</td>
<td align="right">175,258,058</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,505,233</td>
<td align="right">7,623,842</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">346,039,191</td>
<td align="right">349,590,739</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,066,300</td>
<td align="right">82,879,854</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">24,138,201</td>
<td align="right">24,373,016</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,768,719</td>
<td align="right">202,650,957</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">45,300,817</td>
<td align="right">44,920,745</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">141,404,031</td>
<td align="right">142,394,444</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">693,453</td>
<td align="right">698,209</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,637,856</td>
<td align="right">46,957,284</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">55,609,036</td>
<td align="right">55,983,707</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">88,871,370</td>
<td align="right">89,459,674</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,419,207,791</td>
<td align="right">17,307,563,944</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">292,488,077</td>
<td align="right">294,334,179</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,177,888,244</td>
<td align="right">4,151,649,084</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">448,336,186</td>
<td align="right">451,081,901</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">396,618,619</td>
<td align="right">398,860,671</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">597,190,047</td>
<td align="right">600,487,090</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,324,009,439</td>
<td align="right">3,305,695,718</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">395,478,304</td>
<td align="right">393,344,161</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">113,244,475</td>
<td align="right">113,851,815</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,096,887,449</td>
<td align="right">1,091,154,684</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">376,319,515</td>
<td align="right">378,228,187</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,971,032,655</td>
<td align="right">1,980,990,894</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">211,967,767</td>
<td align="right">213,013,013</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,183,946</td>
<td align="right">7,218,510</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,586,154</td>
<td align="right">84,974,313</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">646,638,865</td>
<td align="right">649,598,041</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">161,458,631</td>
<td align="right">162,164,652</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">602,209,325</td>
<td align="right">604,802,039</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">116,934,854</td>
<td align="right">117,415,976</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,279,301</td>
<td align="right">42,109,749</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,253,283,044</td>
<td align="right">1,258,281,214</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">785,091,727</td>
<td align="right">788,040,979</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">852,811,607</td>
<td align="right">855,729,080</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,856,287</td>
<td align="right">9,889,205</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">230,726,548</td>
<td align="right">231,492,853</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">71,810,867</td>
<td align="right">72,046,194</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,815,163,601</td>
<td align="right">2,824,339,145</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">127,536,999</td>
<td align="right">127,949,769</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">207,585,782</td>
<td align="right">208,197,642</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,190,522,245</td>
<td align="right">2,196,857,139</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">91,701,639</td>
<td align="right">91,966,262</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,217,217</td>
<td align="right">104,485,616</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">294,394,580</td>
<td align="right">295,041,407</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">305,822,035</td>
<td align="right">306,487,764</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,110,541</td>
<td align="right">487,133,612</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,626,578,074</td>
<td align="right">1,629,929,687</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,612,524,857</td>
<td align="right">3,619,660,525</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">494,940</td>
<td align="right">495,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">532,937,032</td>
<td align="right">533,939,892</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">70,984</td>
<td align="right">70,864</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,323,639,353</td>
<td align="right">2,327,553,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,089,581</td>
<td align="right">69,205,556</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">342,304,403</td>
<td align="right">342,846,488</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">45,909,890</td>
<td align="right">45,982,160</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">73,530,109</td>
<td align="right">73,645,531</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">293,876,756</td>
<td align="right">294,335,591</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">482,490,108</td>
<td align="right">483,216,810</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,074,775,487</td>
<td align="right">1,076,369,883</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">523,864,461</td>
<td align="right">524,605,789</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">238,163</td>
<td align="right">238,482</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,899,264,299</td>
<td align="right">4,905,779,904</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">49,597,263</td>
<td align="right">49,532,506</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">42,739,186</td>
<td align="right">42,793,885</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,075,657,221</td>
<td align="right">1,074,280,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">365,803,064</td>
<td align="right">366,265,703</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,934,204,831</td>
<td align="right">3,939,170,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">123,107,864</td>
<td align="right">122,960,738</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,192,280,217</td>
<td align="right">2,194,878,674</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">199,265,105</td>
<td align="right">199,482,461</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">987,387,726</td>
<td align="right">988,414,034</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,417,007</td>
<td align="right">36,454,489</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">14,634,042</td>
<td align="right">14,649,027</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,641,810</td>
<td align="right">14,656,790</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">14,600,294</td>
<td align="right">14,615,067</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">199,795,490</td>
<td align="right">199,993,630</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">50,400,831</td>
<td align="right">50,350,954</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">218,229,056</td>
<td align="right">218,428,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,948,449</td>
<td align="right">66,003,275</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">73,426,891</td>
<td align="right">73,485,019</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60,472,849</td>
<td align="right">60,425,999</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,456,250</td>
<td align="right">78,509,048</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">287,143,499</td>
<td align="right">286,950,890</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">280,112,553</td>
<td align="right">280,299,737</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">351,405,725</td>
<td align="right">351,639,265</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,598,884</td>
<td align="right">228,725,864</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">253,235,230</td>
<td align="right">253,372,652</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">276,150,848</td>
<td align="right">276,267,353</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,110,601</td>
<td align="right">2,111,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">278,569</td>
<td align="right">278,453</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,322,422</td>
<td align="right">28,333,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,690,604,572</td>
<td align="right">4,692,459,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">193,945,286</td>
<td align="right">194,019,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">225,729,056</td>
<td align="right">225,802,269</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">271,580,160</td>
<td align="right">271,495,986</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,378,811</td>
<td align="right">11,381,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">239,774,663</td>
<td align="right">239,839,131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,833,354</td>
<td align="right">11,836,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,128,909</td>
<td align="right">2,128,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,645,269</td>
<td align="right">11,642,749</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,465,796</td>
<td align="right">19,469,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">19,005</td>
<td align="right">19,001</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154,181,054</td>
<td align="right">154,209,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">102,925,378</td>
<td align="right">102,943,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,795,484</td>
<td align="right">2,795,002</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">34,081,948</td>
<td align="right">34,087,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">300,811,764</td>
<td align="right">300,764,996</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">38,084,000</td>
<td align="right">38,089,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">358,180,078</td>
<td align="right">358,131,973</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,342,353,160</td>
<td align="right">1,342,520,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">447,845,732</td>
<td align="right">447,801,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,469,880</td>
<td align="right">4,470,307</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">481,942</td>
<td align="right">481,898</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">325,826,101</td>
<td align="right">325,796,652</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,695,180</td>
<td align="right">47,697,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,780,997</td>
<td align="right">52,783,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,864,610</td>
<td align="right">98,868,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,827,830</td>
<td align="right">105,831,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">92,070,378</td>
<td align="right">92,073,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,112,890</td>
<td align="right">91,116,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">91,119,150</td>
<td align="right">91,122,338</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,030,699</td>
<td align="right">66,028,463</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">364,479,437</td>
<td align="right">364,490,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">44,844,938</td>
<td align="right">44,846,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,269,223</td>
<td align="right">556,283,044</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,463,075</td>
<td align="right">20,462,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">171,298,757</td>
<td align="right">171,302,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,761,898</td>
<td align="right">326,755,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">150,009,588</td>
<td align="right">150,012,528</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">33,197,188</td>
<td align="right">33,197,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">34,142,148</td>
<td align="right">34,142,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,296,520</td>
<td align="right">7,296,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">354,832,036</td>
<td align="right">354,837,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">16,031,765</td>
<td align="right">16,031,546</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,431,283</td>
<td align="right">106,432,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,337,645</td>
<td align="right">1,337,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,240,054</td>
<td align="right">190,242,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,851,979</td>
<td align="right">149,850,810</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">991,727</td>
<td align="right">991,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">86,571,556</td>
<td align="right">86,572,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,145,057</td>
<td align="right">229,143,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">277,075,845</td>
<td align="right">277,074,725</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">908,289,821</td>
<td align="right">908,293,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,574,962</td>
<td align="right">402,573,918</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,385,977</td>
<td align="right">30,385,907</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,865,332</td>
<td align="right">786,863,593</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,840,339</td>
<td align="right">173,840,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,095,340</td>
<td align="right">8,095,340</td>
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
<td align="right">3,465,180</td>
<td align="right">3,465,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,005,926</td>
<td align="right">3,005,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">807,420</td>
<td align="right">807,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">541,780</td>
<td align="right">541,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">241,040</td>
<td align="right">241,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">202,660</td>
<td align="right">202,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">152,063</td>
<td align="right">152,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,680</td>
<td align="right">89,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">24,020</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">423,275,284</td>
<td align="right">23.9%</td>
<td align="right">421,141,831</td>
<td align="right">23.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,344,047,430</td>
<td align="right">76.0%</td>
<td align="right">1,345,949,491</td>
<td align="right">76.1%</td>
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
<td align="right">29,506,656</td>
<td align="right">1.7%</td>
<td align="right">29,506,657</td>
<td align="right">1.7%</td>
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
<td align="right">1,111,174</td>
<td align="right">65.0%</td>
<td align="right">1,110,591</td>
<td align="right">65.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598,502</td>
<td align="right">35.0%</td>
<td align="right">598,396</td>
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
<td align="right">39,244</td>
<td align="right">3.5%</td>
<td align="right">37,792</td>
<td align="right">3.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,702</td>
<td align="right">1.3%</td>
<td align="right">15,014</td>
<td align="right">1.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">35,139</td>
<td align="right">3.2%</td>
<td align="right">35,635</td>
<td align="right">3.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,401</td>
<td align="right">0.3%</td>
<td align="right">3,441</td>
<td align="right">0.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,728</td>
<td align="right">0.5%</td>
<td align="right">5,707</td>
<td align="right">0.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,260</td>
<td align="right">1.6%</td>
<td align="right">17,313</td>
<td align="right">1.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,971</td>
<td align="right">0.2%</td>
<td align="right">1,975</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,826</td>
<td align="right">0.5%</td>
<td align="right">5,821</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,991</td>
<td align="right">0.8%</td>
<td align="right">8,984</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,124</td>
<td align="right">0.5%</td>
<td align="right">5,121</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,865</td>
<td align="right">3.6%</td>
<td align="right">39,887</td>
<td align="right">3.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,716</td>
<td align="right">2.9%</td>
<td align="right">32,704</td>
<td align="right">2.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,841</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,369</td>
<td align="right">1.1%</td>
<td align="right">12,365</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,766</td>
<td align="right">7.5%</td>
<td align="right">83,765</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">782,348</td>
<td align="right">70.4%</td>
<td align="right">782,346</td>
<td align="right">70.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,780</td>
<td align="right">1.0%</td>
<td align="right">10,780</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,187,795,762</td>
<td align="right">79.7%</td>
<td align="right">1,187,540,996</td>
<td align="right">79.7%</td>
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
<td align="right">302,402,363</td>
<td align="right">20.3%</td>
<td align="right">302,355,673</td>
<td align="right">20.3%</td>
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
<td align="right">1,837,691</td>
<td align="right">0.1%</td>
<td align="right">1,837,691</td>
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
<td align="right">126,071</td>
<td align="right">51.0%</td>
<td align="right">126,009</td>
<td align="right">51.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">121,021</td>
<td align="right">49.0%</td>
<td align="right">121,005</td>
<td align="right">49.0%</td>
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
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">121</td>
<td align="right">0.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">34,666</td>
<td align="right">27.5%</td>
<td align="right">34,568</td>
<td align="right">27.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,761</td>
<td align="right">17.3%</td>
<td align="right">21,800</td>
<td align="right">17.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">45,200</td>
<td align="right">35.9%</td>
<td align="right">45,200</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">12.8%</td>
<td align="right">16,200</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">3.4%</td>
<td align="right">4,300</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">1,640</td>
<td align="right">1.3%</td>
<td align="right">1,640</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,320</td>
<td align="right">1.0%</td>
<td align="right">1,320</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">320,133,063</td>
<td align="right">5.7%</td>
<td align="right">321,144,828</td>
<td align="right">5.7%</td>
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
<td align="right">196,979,054</td>
<td align="right">3.5%</td>
<td align="right">197,589,895</td>
<td align="right">3.5%</td>
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
<td align="right">5,253,919,689</td>
<td align="right">94.2%</td>
<td align="right">5,269,204,049</td>
<td align="right">94.2%</td>
<td align="right">0.3%</td>
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
<td align="right">95,209</td>
<td align="right">2.2%</td>
<td align="right">95,599</td>
<td align="right">2.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,287,781</td>
<td align="right">97.8%</td>
<td align="right">4,299,237</td>
<td align="right">97.8%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">82,329</td>
<td align="right">86.5%</td>
<td align="right">82,679</td>
<td align="right">86.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,820</td>
<td align="right">12.4%</td>
<td align="right">11,860</td>
<td align="right">12.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,480</td>
<td align="right">3.7%</td>
<td align="right">3,480</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">680</td>
<td align="right">0.7%</td>
<td align="right">680</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.2%</td>
<td align="right">200</td>
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
<td align="right">104,769,475</td>
<td align="right">6.5%</td>
<td align="right">105,037,073</td>
<td align="right">6.5%</td>
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
<td align="right">1,503,967,460</td>
<td align="right">93.5%</td>
<td align="right">1,505,748,624</td>
<td align="right">93.5%</td>
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
<td align="right">772,559</td>
<td align="right">0.0%</td>
<td align="right">771,806</td>
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
<td align="left">Failure</td>
<td align="right">145,041</td>
<td align="right">65.8%</td>
<td align="right">145,125</td>
<td align="right">65.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">75,260</td>
<td align="right">34.2%</td>
<td align="right">75,224</td>
<td align="right">34.1%</td>
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
<td align="left">float long</td>
<td align="right">16,345</td>
<td align="right">11.3%</td>
<td align="right">16,412</td>
<td align="right">11.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">30,423</td>
<td align="right">21.0%</td>
<td align="right">30,527</td>
<td align="right">21.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,991</td>
<td align="right">19.3%</td>
<td align="right">27,923</td>
<td align="right">19.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,792</td>
<td align="right">8.1%</td>
<td align="right">11,770</td>
<td align="right">8.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,533</td>
<td align="right">1.1%</td>
<td align="right">1,532</td>
<td align="right">1.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,822</td>
<td align="right">1.3%</td>
<td align="right">1,823</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,852</td>
<td align="right">11.6%</td>
<td align="right">16,855</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,723</td>
<td align="right">13.6%</td>
<td align="right">19,723</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.4%</td>
<td align="right">10,680</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,000</td>
<td align="right">2.8%</td>
<td align="right">4,000</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,060</td>
<td align="right">1.4%</td>
<td align="right">2,060</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,820</td>
<td align="right">1.3%</td>
<td align="right">1,820</td>
<td align="right">1.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">387,803,060</td>
<td align="right">88.9%</td>
<td align="right">388,409,280</td>
<td align="right">88.9%</td>
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
<td align="right">48,283,719</td>
<td align="right">11.1%</td>
<td align="right">48,355,987</td>
<td align="right">11.1%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.6%</td>
<td align="right">2,517,260</td>
<td align="right">0.6%</td>
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
<td align="right">61,551</td>
<td align="right">42.9%</td>
<td align="right">61,553</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">81,880</td>
<td align="right">57.1%</td>
<td align="right">81,880</td>
<td align="right">57.1%</td>
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
<td align="right">19,759</td>
<td align="right">24.1%</td>
<td align="right">19,746</td>
<td align="right">24.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,061</td>
<td align="right">36.7%</td>
<td align="right">30,074</td>
<td align="right">36.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">22,360</td>
<td align="right">27.3%</td>
<td align="right">22,360</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,700</td>
<td align="right">11.8%</td>
<td align="right">9,700</td>
<td align="right">11.8%</td>
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
<td align="right">369,238</td>
<td align="right">0.1%</td>
<td align="right">357,420</td>
<td align="right">0.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,757,033</td>
<td align="right">18.6%</td>
<td align="right">83,096,550</td>
<td align="right">18.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">356,891,213</td>
<td align="right">81.3%</td>
<td align="right">359,684,924</td>
<td align="right">81.2%</td>
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
<td align="right">57,341</td>
<td align="right">30.9%</td>
<td align="right">57,095</td>
<td align="right">30.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">128,153</td>
<td align="right">69.1%</td>
<td align="right">128,222</td>
<td align="right">69.2%</td>
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
<td align="left">set</td>
<td align="right">19,313</td>
<td align="right">15.1%</td>
<td align="right">19,185</td>
<td align="right">15.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">518</td>
<td align="right">0.4%</td>
<td align="right">520</td>
<td align="right">0.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,723</td>
<td align="right">9.1%</td>
<td align="right">11,765</td>
<td align="right">9.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">42,180</td>
<td align="right">32.9%</td>
<td align="right">42,313</td>
<td align="right">33.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,880</td>
<td align="right">5.4%</td>
<td align="right">6,900</td>
<td align="right">5.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,300</td>
<td align="right">10.4%</td>
<td align="right">13,300</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,739</td>
<td align="right">9.2%</td>
<td align="right">11,739</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">8,580</td>
<td align="right">6.7%</td>
<td align="right">8,580</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,520</td>
<td align="right">4.3%</td>
<td align="right">5,520</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,020</td>
<td align="right">3.1%</td>
<td align="right">4,020</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">1.5%</td>
<td align="right">1,980</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,560</td>
<td align="right">1.2%</td>
<td align="right">1,560</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.2%</td>
<td align="right">280</td>
<td align="right">0.2%</td>
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
<td align="right">253,065,666</td>
<td align="right">3.1%</td>
<td align="right">237,416,774</td>
<td align="right">2.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">779,796,569</td>
<td align="right">9.5%</td>
<td align="right">765,445,358</td>
<td align="right">9.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">679,050</td>
<td align="right">0.0%</td>
<td align="right">679,361</td>
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
<td align="right">7,437,387,073</td>
<td align="right">90.4%</td>
<td align="right">7,438,194,349</td>
<td align="right">90.6%</td>
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
<td align="right">5,428,841</td>
<td align="right">87.5%</td>
<td align="right">5,133,421</td>
<td align="right">86.8%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">777,288</td>
<td align="right">12.5%</td>
<td align="right">777,887</td>
<td align="right">13.2%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">7,493</td>
<td align="right">1.0%</td>
<td align="right">7,622</td>
<td align="right">1.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,940</td>
<td align="right">2.1%</td>
<td align="right">16,140</td>
<td align="right">2.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,343</td>
<td align="right">0.4%</td>
<td align="right">3,383</td>
<td align="right">0.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">57,135</td>
<td align="right">7.4%</td>
<td align="right">57,406</td>
<td align="right">7.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">29,480</td>
<td align="right">3.8%</td>
<td align="right">29,580</td>
<td align="right">3.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">99,714</td>
<td align="right">12.8%</td>
<td align="right">100,016</td>
<td align="right">12.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">211,849</td>
<td align="right">27.3%</td>
<td align="right">211,219</td>
<td align="right">27.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,842</td>
<td align="right">1.9%</td>
<td align="right">14,866</td>
<td align="right">1.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,125</td>
<td align="right">2.6%</td>
<td align="right">20,144</td>
<td align="right">2.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">46,602</td>
<td align="right">6.0%</td>
<td align="right">46,638</td>
<td align="right">6.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160,206</td>
<td align="right">20.6%</td>
<td align="right">160,296</td>
<td align="right">20.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">74,679</td>
<td align="right">9.6%</td>
<td align="right">74,697</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,800</td>
<td align="right">2.0%</td>
<td align="right">15,800</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">15,280</td>
<td align="right">2.0%</td>
<td align="right">15,280</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,000</td>
<td align="right">0.4%</td>
<td align="right">3,000</td>
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
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">426,461</td>
<td align="right">0.0%</td>
<td align="right">430,465</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,785,769,795</td>
<td align="right">99.6%</td>
<td align="right">4,804,899,574</td>
<td align="right">99.6%</td>
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
<td align="right">20,366,364</td>
<td align="right">0.4%</td>
<td align="right">20,370,033</td>
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
<td align="right">11,760</td>
<td align="right">0.0%</td>
<td align="right">11,760</td>
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
<td align="right">523,172</td>
<td align="right">100.0%</td>
<td align="right">523,094</td>
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
<td align="right">89,250,246</td>
<td align="right">100.0%</td>
<td align="right">90,098,364</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,585</td>
<td align="right">0.0%</td>
<td align="right">9,581</td>
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
<td align="right">9,420</td>
<td align="right">100.0%</td>
<td align="right">9,420</td>
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
<td align="right">786,834,432</td>
<td align="right">81.9%</td>
<td align="right">786,832,693</td>
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
<td align="right">173,802,460</td>
<td align="right">18.1%</td>
<td align="right">173,802,168</td>
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
<td align="right">30,900</td>
<td align="right">0.0%</td>
<td align="right">30,900</td>
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
<td align="right">7,051</td>
<td align="right">10.3%</td>
<td align="right">7,046</td>
<td align="right">10.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,728</td>
<td align="right">89.7%</td>
<td align="right">61,723</td>
<td align="right">89.8%</td>
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
<td align="left">other</td>
<td align="right">16,128</td>
<td align="right">26.1%</td>
<td align="right">16,123</td>
<td align="right">26.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">53.8%</td>
<td align="right">33,180</td>
<td align="right">53.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.1%</td>
<td align="right">9,960</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">69,501,872</td>
<td align="right">3.4%</td>
<td align="right">68,458,697</td>
<td align="right">3.4%</td>
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
<td align="right">102,049,971</td>
<td align="right">5.1%</td>
<td align="right">101,031,836</td>
<td align="right">5.0%</td>
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
<td align="right">1,912,564,939</td>
<td align="right">94.9%</td>
<td align="right">1,912,396,997</td>
<td align="right">94.9%</td>
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
<td align="right">1,433,421</td>
<td align="right">93.5%</td>
<td align="right">1,413,744</td>
<td align="right">93.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100,428</td>
<td align="right">6.5%</td>
<td align="right">100,582</td>
<td align="right">6.6%</td>
<td align="right">0.2%</td>
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
<td align="right">5,240</td>
<td align="right">5.2%</td>
<td align="right">5,340</td>
<td align="right">5.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,000</td>
<td align="right">5.0%</td>
<td align="right">5,020</td>
<td align="right">5.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,580</td>
<td align="right">11.5%</td>
<td align="right">11,620</td>
<td align="right">11.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">35,468</td>
<td align="right">35.3%</td>
<td align="right">35,462</td>
<td align="right">35.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,680</td>
<td align="right">14.6%</td>
<td align="right">14,680</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,720</td>
<td align="right">8.7%</td>
<td align="right">8,720</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,780</td>
<td align="right">7.7%</td>
<td align="right">7,780</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,060</td>
<td align="right">6.0%</td>
<td align="right">6,060</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,360</td>
<td align="right">4.3%</td>
<td align="right">4,360</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">167,327,620</td>
<td align="right">71.7%</td>
<td align="right">167,968,722</td>
<td align="right">71.8%</td>
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
<td align="right">65,958,571</td>
<td align="right">28.3%</td>
<td align="right">65,956,290</td>
<td align="right">28.2%</td>
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
<td align="right">56,990</td>
<td align="right">79.0%</td>
<td align="right">57,033</td>
<td align="right">79.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,138</td>
<td align="right">21.0%</td>
<td align="right">15,140</td>
<td align="right">21.0%</td>
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
<td align="right">2,300</td>
<td align="right">4.0%</td>
<td align="right">2,320</td>
<td align="right">4.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">35,216</td>
<td align="right">61.8%</td>
<td align="right">35,236</td>
<td align="right">61.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">11,294</td>
<td align="right">19.8%</td>
<td align="right">11,297</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">11.4%</td>
<td align="right">6,480</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.6%</td>
<td align="right">900</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.4%</td>
<td align="right">800</td>
<td align="right">1.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,835,663,062</td>
<td align="right">91.9%</td>
<td align="right">2,842,864,733</td>
<td align="right">91.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">247,687,182</td>
<td align="right">8.0%</td>
<td align="right">247,885,670</td>
<td align="right">8.0%</td>
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
<td align="right">49,229,939</td>
<td align="right">1.6%</td>
<td align="right">49,230,476</td>
<td align="right">1.6%</td>
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
<td align="right">194,089</td>
<td align="right">14.5%</td>
<td align="right">194,335</td>
<td align="right">14.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,144,158</td>
<td align="right">85.5%</td>
<td align="right">1,144,101</td>
<td align="right">85.5%</td>
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
<td align="left">other</td>
<td align="right">5,165</td>
<td align="right">2.7%</td>
<td align="right">5,212</td>
<td align="right">2.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">17,803</td>
<td align="right">9.2%</td>
<td align="right">17,841</td>
<td align="right">9.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">49,460</td>
<td align="right">25.5%</td>
<td align="right">49,541</td>
<td align="right">25.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">38,904</td>
<td align="right">20.0%</td>
<td align="right">38,949</td>
<td align="right">20.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,686</td>
<td align="right">15.8%</td>
<td align="right">30,713</td>
<td align="right">15.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,743</td>
<td align="right">2.4%</td>
<td align="right">4,747</td>
<td align="right">2.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20,164</td>
<td align="right">10.4%</td>
<td align="right">20,169</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">23,183</td>
<td align="right">11.9%</td>
<td align="right">23,182</td>
<td align="right">11.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,321</td>
<td align="right">1.2%</td>
<td align="right">2,321</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,240</td>
<td align="right">0.6%</td>
<td align="right">1,240</td>
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
<td align="right">533,254,467</td>
<td align="right">99.9%</td>
<td align="right">535,165,030</td>
<td align="right">99.9%</td>
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
<td align="right">447,375</td>
<td align="right">0.1%</td>
<td align="right">447,355</td>
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
<td align="right">3,071</td>
<td align="right">8.9%</td>
<td align="right">3,075</td>
<td align="right">8.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">31,496</td>
<td align="right">91.1%</td>
<td align="right">31,468</td>
<td align="right">91.1%</td>
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
<td align="left">sequence</td>
<td align="right">2,191</td>
<td align="right">71.3%</td>
<td align="right">2,195</td>
<td align="right">71.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">16.3%</td>
<td align="right">500</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">12.4%</td>
<td align="right">380</td>
<td align="right">12.4%</td>
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
<td align="right">604,422,315</td>
<td align="right">0.6%</td>
<td align="right">588,333,016</td>
<td align="right">0.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">34,847,706,196</td>
<td align="right">35.8%</td>
<td align="right">34,434,676,017</td>
<td align="right">35.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">53,838,097,683</td>
<td align="right">55.3%</td>
<td align="right">54,028,757,802</td>
<td align="right">55.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,112,809,806</td>
<td align="right">8.3%</td>
<td align="right">8,090,979,799</td>
<td align="right">8.3%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">779,796,569</td>
<td align="right">29.2%</td>
<td align="right">765,445,358</td>
<td align="right">28.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,757,033</td>
<td align="right">3.1%</td>
<td align="right">83,096,550</td>
<td align="right">3.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">102,049,971</td>
<td align="right">3.8%</td>
<td align="right">101,031,836</td>
<td align="right">3.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">423,275,284</td>
<td align="right">15.8%</td>
<td align="right">421,141,831</td>
<td align="right">15.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">320,133,063</td>
<td align="right">12.0%</td>
<td align="right">321,144,828</td>
<td align="right">12.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,769,475</td>
<td align="right">3.9%</td>
<td align="right">105,037,073</td>
<td align="right">4.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">247,687,182</td>
<td align="right">9.3%</td>
<td align="right">247,885,670</td>
<td align="right">9.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">302,402,363</td>
<td align="right">11.3%</td>
<td align="right">302,355,673</td>
<td align="right">11.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,958,571</td>
<td align="right">2.5%</td>
<td align="right">65,956,290</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,802,460</td>
<td align="right">6.5%</td>
<td align="right">173,802,168</td>
<td align="right">6.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,373,854</td>
<td align="right">12.1%</td>
<td align="right">56,738,451</td>
<td align="right">9.6%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">26,131,211</td>
<td align="right">4.3%</td>
<td align="right">25,089,062</td>
<td align="right">4.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">105,110,594</td>
<td align="right">17.4%</td>
<td align="right">106,105,547</td>
<td align="right">18.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39,517,111</td>
<td align="right">6.5%</td>
<td align="right">39,297,004</td>
<td align="right">6.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,558,217</td>
<td align="right">15.0%</td>
<td align="right">91,049,871</td>
<td align="right">15.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">41,713,719</td>
<td align="right">6.9%</td>
<td align="right">41,828,162</td>
<td align="right">7.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,629,355</td>
<td align="right">3.9%</td>
<td align="right">23,661,451</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">23,642,857</td>
<td align="right">3.9%</td>
<td align="right">23,643,515</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,346,974</td>
<td align="right">7.2%</td>
<td align="right">43,346,085</td>
<td align="right">7.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,825,769</td>
<td align="right">4.6%</td>
<td align="right">27,825,647</td>
<td align="right">4.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">233,837,817</td>
<td align="right">3.0%</td>
<td align="right">234,867,465</td>
<td align="right">3.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,337,754,719</td>
<td align="right">17.0%</td>
<td align="right">1,340,577,468</td>
<td align="right">17.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,340,430,939</td>
<td align="right">17.1%</td>
<td align="right">1,343,253,688</td>
<td align="right">17.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,167,745,862</td>
<td align="right">78.6%</td>
<td align="right">6,176,848,597</td>
<td align="right">78.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,194,894,034</td>
<td align="right">28.0%</td>
<td align="right">2,197,532,819</td>
<td align="right">28.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,194,894,034</td>
<td align="right">28.0%</td>
<td align="right">2,197,532,819</td>
<td align="right">28.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,656,609,293</td>
<td align="right">72.0%</td>
<td align="right">5,663,236,810</td>
<td align="right">72.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">454,032,012</td>
<td align="right">5.8%</td>
<td align="right">454,131,602</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">854,463,095</td>
<td align="right">10.9%</td>
<td align="right">854,279,131</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">73,893,748</td>
<td align="right">0.9%</td>
<td align="right">73,908,840</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">34,571,937</td>
<td align="right">0.4%</td>
<td align="right">34,576,367</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">213,168,769</td>
<td align="right">2.7%</td>
<td align="right">213,166,487</td>
<td align="right">2.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
<td align="right">24,020</td>
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
<td align="right">25,001,739</td>
<td align="right"></td>
<td align="right">28,378,967</td>
<td align="right"></td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">56,826,641</td>
<td align="right"></td>
<td align="right">59,153,575</td>
<td align="right"></td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">32,040,840</td>
<td align="right"></td>
<td align="right">30,985,410</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">85,190,470,054</td>
<td align="right">78.9%</td>
<td align="right">86,089,572,184</td>
<td align="right">79.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,238,634,091</td>
<td align="right"></td>
<td align="right">2,261,849,693</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">98,042,828,276</td>
<td align="right">79.0%</td>
<td align="right">98,956,504,107</td>
<td align="right">79.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,541,430</td>
<td align="right">0.1%</td>
<td align="right">20,609,802</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,215,327</td>
<td align="right"></td>
<td align="right">162,691,028</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">22,722,785,051</td>
<td align="right">21.1%</td>
<td align="right">22,760,583,912</td>
<td align="right">20.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">26,081,678,990</td>
<td align="right">21.0%</td>
<td align="right">26,116,461,386</td>
<td align="right">20.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,341,875,808</td>
<td align="right">37.6%</td>
<td align="right">6,348,387,418</td>
<td align="right">37.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,343,747,552</td>
<td align="right"></td>
<td align="right">6,350,259,756</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,854,100,371</td>
<td align="right"></td>
<td align="right">10,861,194,660</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,528,858,750</td>
<td align="right">62.4%</td>
<td align="right">10,535,181,943</td>
<td align="right">62.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,403,255,370</td>
<td align="right">61.7%</td>
<td align="right">10,409,484,594</td>
<td align="right">61.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">105,061,950</td>
<td align="right">0.6%</td>
<td align="right">105,087,547</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,070,046,226</td>
<td align="right"></td>
<td align="right">3,070,129,383</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">6,547,500</td>
<td align="right">4.0%</td>
<td align="right">6,547,500</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">64,160</td>
<td align="right">0.0%</td>
<td align="right">64,160</td>
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
<td align="right">19,457,859</td>
<td align="right">14,699,097,292</td>
<td align="right">0</td>
<td align="right">19,448,993</td>
<td align="right">14,679,676,702</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,054,428,510</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,054,397,760</td>
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
<td align="right">46,538</td>
<td align="right">6.1%</td>
<td align="right">16,364</td>
<td align="right">1.9%</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">690</td>
<td align="right">0.1%</td>
<td align="right">833</td>
<td align="right">0.1%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,014,951,478</td>
<td align="right"></td>
<td align="right">8,312,783,272</td>
<td align="right"></td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">646,492</td>
<td align="right">85.4%</td>
<td align="right">728,382</td>
<td align="right">85.8%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">757,368</td>
<td align="right"></td>
<td align="right">848,481</td>
<td align="right"></td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">110,876</td>
<td align="right">14.6%</td>
<td align="right">120,099</td>
<td align="right">14.2%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,260</td>
<td align="right">0.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">197,693,218,625</td>
<td align="right">2,818.2%</td>
<td align="right">201,479,090,240</td>
<td align="right">2,423.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,282</td>
<td align="right">5.7%</td>
<td align="right">6,366</td>
<td align="right">5.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,429</td>
<td align="right">0.8%</td>
<td align="right">6,479</td>
<td align="right">0.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">446,649</td>
<td align="right">59.0%</td>
<td align="right">449,109</td>
<td align="right">52.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">107,336</td>
<td align="right">96.8%</td>
<td align="right">116,556</td>
<td align="right">97.0%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">110,876</td>
<td align="right"></td>
<td align="right">120,099</td>
<td align="right"></td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,320</td>
<td align="right">2.1%</td>
<td align="right">2,323</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
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
<td align="right">5,080</td>
<td align="right">4.6%</td>
<td align="right">11,932</td>
<td align="right">9.9%</td>
<td align="right">134.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,010</td>
<td align="right">18.9%</td>
<td align="right">21,388</td>
<td align="right">17.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,199</td>
<td align="right">32.6%</td>
<td align="right">37,032</td>
<td align="right">30.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,099</td>
<td align="right">24.4%</td>
<td align="right">27,996</td>
<td align="right">23.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,986</td>
<td align="right">12.6%</td>
<td align="right">14,155</td>
<td align="right">11.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,102</td>
<td align="right">5.5%</td>
<td align="right">6,176</td>
<td align="right">5.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,260</td>
<td align="right">1.1%</td>
<td align="right">1,280</td>
<td align="right">1.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
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
<td align="right">4,120</td>
<td align="right">3.7%</td>
<td align="right">10,152</td>
<td align="right">8.5%</td>
<td align="right">146.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,610</td>
<td align="right">13.2%</td>
<td align="right">17,571</td>
<td align="right">14.6%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">24,069</td>
<td align="right">21.7%</td>
<td align="right">25,290</td>
<td align="right">21.1%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,827</td>
<td align="right">32.3%</td>
<td align="right">35,334</td>
<td align="right">29.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,541</td>
<td align="right">15.8%</td>
<td align="right">17,227</td>
<td align="right">14.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,229</td>
<td align="right">7.4%</td>
<td align="right">8,024</td>
<td align="right">6.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">2.3%</td>
<td align="right">2,618</td>
<td align="right">2.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">340</td>
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
<tr>
<td align="left"><= 2</td>
<td align="right">27,717,760</td>
<td align="right">0.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">373,519,196</td>
<td align="right">5.3%</td>
<td align="right">1,109,558,722</td>
<td align="right">13.3%</td>
<td align="right">197.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">905,009,267</td>
<td align="right">12.9%</td>
<td align="right">1,131,562,527</td>
<td align="right">13.6%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,066,703,441</td>
<td align="right">15.2%</td>
<td align="right">1,116,277,807</td>
<td align="right">13.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,110,634,039</td>
<td align="right">15.8%</td>
<td align="right">1,134,937,384</td>
<td align="right">13.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">693,833,187</td>
<td align="right">9.9%</td>
<td align="right">702,538,885</td>
<td align="right">8.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">339,980,213</td>
<td align="right">4.8%</td>
<td align="right">339,533,375</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">183,074,363</td>
<td align="right">2.6%</td>
<td align="right">182,275,777</td>
<td align="right">2.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">28,721,550</td>
<td align="right">0.4%</td>
<td align="right">28,644,175</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">7,342,886</td>
<td align="right">0.1%</td>
<td align="right">7,335,284</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">19,033,982</td>
<td align="right">0.3%</td>
<td align="right">19,033,925</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">685,777</td>
<td align="right">0.0%</td>
<td align="right">685,855</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">740,529</td>
<td align="right">0.0%</td>
<td align="right">743,039</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="right">246,820</td>
<td align="right">0.0%</td>
<td align="right">246,820</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="right">43,780</td>
<td align="right">0.0%</td>
<td align="right">43,780</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="right">13,070</td>
<td align="right">0.0%</td>
<td align="right">13,071</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">1,051</td>
<td align="right">0.0%</td>
<td align="right">1,049</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="right">2,021</td>
<td align="right">0.0%</td>
<td align="right">2,001</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="right">458</td>
<td align="right">0.0%</td>
<td align="right">479</td>
<td align="right">0.0%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2,097,152</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">241</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 8,388,608</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16,777,216</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,337,780</td>
<td align="right">58,443,260</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">501,700</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,592,991</td>
<td align="right">20,745,061</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,550,717,209</td>
<td align="right">5,557,746,682</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,083,798,154</td>
<td align="right">2,539,348,037</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,931,153,324</td>
<td align="right">5,773,435,235</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,719,203,606</td>
<td align="right">5,199,848,652</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,299,637,657</td>
<td align="right">1,431,010,164</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,951</td>
<td align="right">51,291,305</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">202,104,026</td>
<td align="right">211,164,864</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,631</td>
<td align="right">104,635,925</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,009,080,574</td>
<td align="right">1,042,082,915</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,778,580</td>
<td align="right">5,895,308</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">448,517</td>
<td align="right">441,339</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,550,480</td>
<td align="right">13,753,700</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,104,245,992</td>
<td align="right">7,201,716,697</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,119,615</td>
<td align="right">10,234,995</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">278,465,258</td>
<td align="right">275,743,604</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">96,799,735</td>
<td align="right">95,893,588</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,043,855</td>
<td align="right">96,137,708</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,483,435</td>
<td align="right">4,523,689</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,680</td>
<td align="right">53,344,620</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">340,381,234</td>
<td align="right">337,800,391</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">62,369,117</td>
<td align="right">62,824,761</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,487,998,695</td>
<td align="right">6,534,787,643</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,287,382</td>
<td align="right">197,923,251</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">227,625,783</td>
<td align="right">226,122,522</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,634,343</td>
<td align="right">261,972,011</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,861,163</td>
<td align="right">263,198,831</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">34,050,600</td>
<td align="right">34,253,820</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,042,459,632</td>
<td align="right">1,047,992,292</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,805,619,526</td>
<td align="right">11,867,908,199</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,720,649,309</td>
<td align="right">5,750,493,831</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">245,585,099</td>
<td align="right">244,319,086</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">140,378,226</td>
<td align="right">139,672,603</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">168,533,509</td>
<td align="right">167,731,244</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,868,060,663</td>
<td align="right">13,927,946,474</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">188,411,410</td>
<td align="right">187,705,058</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,733,349</td>
<td align="right">133,239,936</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,733,349</td>
<td align="right">133,239,936</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">99,762,328</td>
<td align="right">100,114,202</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,180,840,008</td>
<td align="right">2,188,440,848</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">212,389,612</td>
<td align="right">211,683,026</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,346,669,877</td>
<td align="right">1,342,290,015</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">974,075,633</td>
<td align="right">977,042,499</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">62,255,217</td>
<td align="right">62,441,781</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">543,735,435</td>
<td align="right">542,126,790</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">74,029,913</td>
<td align="right">74,248,274</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">29,644,741</td>
<td align="right">29,730,954</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,399,609</td>
<td align="right">11,431,968</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,399,609</td>
<td align="right">11,431,968</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,186,346,113</td>
<td align="right">2,180,229,997</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">620,874,290</td>
<td align="right">619,297,987</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,421,720</td>
<td align="right">22,366,680</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,539,441,104</td>
<td align="right">2,545,569,276</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">572,884,310</td>
<td align="right">571,573,264</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">228,571,200</td>
<td align="right">228,072,710</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">727,122,353</td>
<td align="right">725,645,516</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,544,175,239</td>
<td align="right">1,547,250,318</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,568,712</td>
<td align="right">45,651,375</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,240,880,205</td>
<td align="right">2,237,118,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,264,306,965</td>
<td align="right">2,260,515,820</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,674,076,269</td>
<td align="right">6,662,943,117</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,868,487,824</td>
<td align="right">1,865,402,499</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">862,163,439</td>
<td align="right">860,793,301</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,788,395,414</td>
<td align="right">1,785,670,003</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,028,921</td>
<td align="right">172,273,544</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,491,361,372</td>
<td align="right">6,482,313,607</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,768,171</td>
<td align="right">22,799,839</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,826,737,639</td>
<td align="right">2,830,581,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,059,046,851</td>
<td align="right">1,057,622,234</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">233,441,807</td>
<td align="right">233,749,802</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,140,701,431</td>
<td align="right">1,142,115,219</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">948,882,067</td>
<td align="right">947,714,398</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,144,459</td>
<td align="right">485,735,296</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">364,779,925</td>
<td align="right">365,224,035</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">686,137,008</td>
<td align="right">685,304,339</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,260,019,197</td>
<td align="right">1,261,514,245</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,446,732,014</td>
<td align="right">3,450,746,230</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,240,826,777</td>
<td align="right">1,242,240,354</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,098,458,911</td>
<td align="right">2,096,123,709</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,239,283,657</td>
<td align="right">1,237,923,673</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">404,824,485</td>
<td align="right">405,268,595</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,237,700,462</td>
<td align="right">2,240,111,443</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,856,837,665</td>
<td align="right">1,854,860,086</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,102,080,954</td>
<td align="right">1,101,129,334</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,956,485,293</td>
<td align="right">1,954,859,588</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,522,019</td>
<td align="right">217,699,932</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,664,061</td>
<td align="right">87,728,439</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,655,520,606</td>
<td align="right">1,654,369,972</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,604,071,650</td>
<td align="right">3,601,596,122</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,321,148</td>
<td align="right">128,408,256</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,443,788</td>
<td align="right">129,531,216</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,199,488,889</td>
<td align="right">3,197,535,005</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">121,066,394</td>
<td align="right">120,992,816</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">758,308,578</td>
<td align="right">758,764,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">336,679,565</td>
<td align="right">336,478,850</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,415,643,635</td>
<td align="right">1,414,856,751</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,528,775</td>
<td align="right">129,600,309</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">564,617,243</td>
<td align="right">564,925,985</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,680,074</td>
<td align="right">1,366,933,842</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,918,931</td>
<td align="right">101,863,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">108,198,884</td>
<td align="right">108,255,443</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,273,587,462</td>
<td align="right">1,274,222,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">554,154,456</td>
<td align="right">554,425,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">411,158,371</td>
<td align="right">411,356,331</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">782,462,148</td>
<td align="right">782,806,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">782,999,468</td>
<td align="right">783,343,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">223,043,254</td>
<td align="right">223,137,044</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,490,990</td>
<td align="right">78,523,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,313,110,260</td>
<td align="right">1,312,573,045</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">411,235,446</td>
<td align="right">411,071,749</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,941,180</td>
<td align="right">144,886,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,039,920,527</td>
<td align="right">1,039,529,387</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">711,016,475</td>
<td align="right">711,283,450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,973,823,608</td>
<td align="right">1,974,564,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,958,947,805</td>
<td align="right">2,957,868,896</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,597,212</td>
<td align="right">93,630,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,697,876</td>
<td align="right">93,730,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">184,754,274</td>
<td align="right">184,819,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,093,655</td>
<td align="right">187,158,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,603,470,537</td>
<td align="right">9,600,164,935</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">736,256,478</td>
<td align="right">736,485,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,393,516,015</td>
<td align="right">1,393,946,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">110,579,212</td>
<td align="right">110,611,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,370,034,583</td>
<td align="right">1,369,647,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">115,514,460</td>
<td align="right">115,482,619</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,479,351</td>
<td align="right">314,565,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,647,701,204</td>
<td align="right">2,647,007,430</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">688,101,731</td>
<td align="right">688,275,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,838,180</td>
<td align="right">484,718,112</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">596,134,732</td>
<td align="right">595,989,434</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,581,134</td>
<td align="right">1,114,785,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">845,855,434</td>
<td align="right">846,008,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">651,487</td>
<td align="right">651,574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">935,678,231</td>
<td align="right">935,791,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,007,420</td>
<td align="right">2,007,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,722,160</td>
<td align="right">509,667,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,500,803</td>
<td align="right">32,503,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">149,720,273</td>
<td align="right">149,709,514</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,641,829</td>
<td align="right">1,339,737,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,953,700</td>
<td align="right">1,953,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,904,698</td>
<td align="right">229,890,908</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,720</td>
<td align="right">5,636,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,301,707,193</td>
<td align="right">3,301,534,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">789,492,229</td>
<td align="right">789,532,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">134,336,772</td>
<td align="right">134,342,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,913,281</td>
<td align="right">68,911,603</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,551,548</td>
<td align="right">1,551,514</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,271,138</td>
<td align="right">203,267,436</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,903,476</td>
<td align="right">126,901,276</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,258,119</td>
<td align="right">1,335,280,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">98,835,349</td>
<td align="right">98,833,733</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">99,793,989</td>
<td align="right">99,792,373</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,798,658</td>
<td align="right">909,811,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,169,820</td>
<td align="right">6,169,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,551,540</td>
<td align="right">1,144,564,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">331,276,814</td>
<td align="right">331,280,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,406,587</td>
<td align="right">382,410,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">144,484,164</td>
<td align="right">144,482,951</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">413,977,322</td>
<td align="right">413,980,069</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">960,536,436</td>
<td align="right">960,542,353</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">324,402,156</td>
<td align="right">324,400,311</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,292,012</td>
<td align="right">101,291,458</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92,088,060</td>
<td align="right">92,088,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">153,990,988</td>
<td align="right">153,990,395</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,335,808</td>
<td align="right">54,336,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,226,240</td>
<td align="right">8,226,210</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,821,145,626</td>
<td align="right">1,821,151,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,843,820</td>
<td align="right">61,844,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">58,673,094</td>
<td align="right">58,672,976</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,426,420</td>
<td align="right">199,426,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,673,421</td>
<td align="right">384,673,151</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,059,828</td>
<td align="right">22,059,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,625,440</td>
<td align="right">61,625,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,808,225</td>
<td align="right">9,808,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,076,164</td>
<td align="right">645,076,156</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">226,004,300</td>
<td align="right">226,004,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,653,969,851</td>
<td align="right">1,653,969,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,466,000</td>
<td align="right">588,466,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">531,150,840</td>
<td align="right">531,150,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">173,848,654</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">99,814,940</td>
<td align="right">99,814,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,405,920</td>
<td align="right">81,405,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">64,594,900</td>
<td align="right">64,594,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,499,060</td>
<td align="right">20,499,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,500</td>
<td align="right">12,693,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">4,823,420</td>
<td align="right">4,823,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,840</td>
<td align="right">3,610,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,865,500</td>
<td align="right">2,865,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,133,180</td>
<td align="right">2,133,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,640</td>
<td align="right">543,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,420</td>
<td align="right">71,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">41,100</td>
<td align="right">41,100</td>
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
<tr>
<td align="left">_GUARD_INSTR_PTR</td>
<td align="right"></td>
<td align="right">732,748,599</td>
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
<td align="left">SEND_GEN</td>
<td align="right">1,380</td>
<td align="right">118,380</td>
<td align="right">8,478.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,254</td>
<td align="right">34,475</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,758</td>
<td align="right">6,472</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
<td align="right">1,640</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,906</td>
<td align="right">1,921</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,564</td>
<td align="right">5,523</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84,297</td>
<td align="right">83,968</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">538</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">41,873</td>
<td align="right">41,962</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,578</td>
<td align="right">2,577</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,362</td>
<td align="right">30,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,340</td>
<td align="right">2,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
<td align="right">260</td>
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
<td align="right">1,082</td>
<td align="right">1,084</td>
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
<td align="right">1,082</td>
<td align="right">1,084</td>
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
<td align="right">400</td>
<td align="right">400</td>
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
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-06
