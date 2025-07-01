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
<td align="left">BINARY_OP</td>
<td align="right">89,306</td>
<td align="right">5,138</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">75,718</td>
<td align="right">8,766</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">69,598</td>
<td align="right">8,640</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,430,957</td>
<td align="right">2,662,173</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">118,902</td>
<td align="right">219,599</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,119,304</td>
<td align="right">337,207</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">538,403</td>
<td align="right">88,599</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,592,734</td>
<td align="right">329,359</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,963,794</td>
<td align="right">779,873</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">564,615</td>
<td align="right">236,290</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,432,620</td>
<td align="right">1,077,906</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,102,784</td>
<td align="right">1,674,444</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,774,469</td>
<td align="right">1,587,819</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,855,203</td>
<td align="right">1,076,197</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,839,805</td>
<td align="right">1,653,837</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,397,966</td>
<td align="right">1,488,256</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,115,198</td>
<td align="right">5,674,271</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">624,256</td>
<td align="right">392,332</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,666,503</td>
<td align="right">1,073,519</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,409,876</td>
<td align="right">919,365</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,094</td>
<td align="right">1,370</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,453,031</td>
<td align="right">962,520</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">661,317</td>
<td align="right">472,175</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">33,033,958</td>
<td align="right">24,147,091</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,687,505</td>
<td align="right">2,751,350</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,531,613</td>
<td align="right">1,912,071</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">308,097</td>
<td align="right">234,471</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,509,111</td>
<td align="right">3,505,009</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">75,142,359</td>
<td align="right">59,360,411</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,557,014</td>
<td align="right">2,027,705</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">418,921</td>
<td align="right">334,858</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,175,587</td>
<td align="right">2,650,072</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,040,876</td>
<td align="right">7,718,720</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,279,252</td>
<td align="right">16,462,451</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,203,253</td>
<td align="right">5,386,057</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,404,263</td>
<td align="right">2,964,878</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">91,989</td>
<td align="right">80,316</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,318</td>
<td align="right">10,954</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,572,206</td>
<td align="right">1,401,096</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,760,024</td>
<td align="right">6,044,603</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,991,828</td>
<td align="right">11,618,368</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,039,746</td>
<td align="right">3,617,313</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,215,505</td>
<td align="right">9,260,073</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,376,445</td>
<td align="right">2,163,169</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">317,222</td>
<td align="right">290,664</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">398,351</td>
<td align="right">429,702</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,460,672</td>
<td align="right">2,278,658</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,439,319</td>
<td align="right">2,262,983</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,336,094</td>
<td align="right">1,240,120</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,763,056</td>
<td align="right">4,425,384</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,752,412</td>
<td align="right">6,297,068</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">458,596</td>
<td align="right">428,290</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">118,626</td>
<td align="right">110,900</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,724,878</td>
<td align="right">10,974,206</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">311,144</td>
<td align="right">292,826</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,429,941</td>
<td align="right">1,345,955</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">409,468</td>
<td align="right">385,513</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,019,711</td>
<td align="right">15,150,386</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,798,970</td>
<td align="right">14,993,363</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,035,665</td>
<td align="right">6,711,315</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">639,817</td>
<td align="right">613,259</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,234,817</td>
<td align="right">1,202,319</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,170,897</td>
<td align="right">8,986,878</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,215,822</td>
<td align="right">1,202,606</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">754,555</td>
<td align="right">749,055</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">255,119</td>
<td align="right">253,755</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">763,599</td>
<td align="right">760,621</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">225,170</td>
<td align="right">224,488</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">274,298</td>
<td align="right">273,616</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,778,696</td>
<td align="right">1,775,484</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">459,788</td>
<td align="right">459,106</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,189,792</td>
<td align="right">1,191,490</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,212,350</td>
<td align="right">5,207,870</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,215,274</td>
<td align="right">2,215,274</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,655,294</td>
<td align="right">1,655,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,400,591</td>
<td align="right">1,400,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,113,704</td>
<td align="right">1,113,704</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">918,788</td>
<td align="right">918,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">869,956</td>
<td align="right">869,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">714,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">693,933</td>
<td align="right">693,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">640,585</td>
<td align="right">640,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">468,763</td>
<td align="right">468,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">350,105</td>
<td align="right">350,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">315,049</td>
<td align="right">315,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">231,447</td>
<td align="right">231,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">200,606</td>
<td align="right">200,606</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">167,922</td>
<td align="right">167,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">130,861</td>
<td align="right">130,861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">100,303</td>
<td align="right">100,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">96,277</td>
<td align="right">96,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">59,363</td>
<td align="right">59,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">57,253</td>
<td align="right">57,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">46,471</td>
<td align="right">46,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">40,877</td>
<td align="right">40,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">34,867</td>
<td align="right">34,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">32,820</td>
<td align="right">32,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">26,506</td>
<td align="right">26,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,762</td>
<td align="right">24,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">24,522</td>
<td align="right">24,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">19,328</td>
<td align="right">19,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">18,816</td>
<td align="right">18,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">16,444</td>
<td align="right">16,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">16,376</td>
<td align="right">16,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">16,355</td>
<td align="right">16,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">14,329</td>
<td align="right">14,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">14,287</td>
<td align="right">14,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,282</td>
<td align="right">12,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,282</td>
<td align="right">12,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,266</td>
<td align="right">12,266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">10,303</td>
<td align="right">10,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,576</td>
<td align="right">9,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">6,209</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,186</td>
<td align="right">6,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,141</td>
<td align="right">6,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">4,094</td>
<td align="right">4,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,073</td>
<td align="right">4,073</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,801</td>
<td align="right">3,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,247</td>
<td align="right">2,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,115</td>
<td align="right">2,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">2,026</td>
<td align="right">2,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,026</td>
<td align="right">2,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,023</td>
<td align="right">2,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,806</td>
<td align="right">1,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,008</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">47</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">88,255</td>
<td align="right">0.5%</td>
<td align="right">4,192</td>
<td align="right">0.0%</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,182,576</td>
<td align="right">99.5%</td>
<td align="right">18,182,576</td>
<td align="right">99.9%</td>
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
<td align="right">6,293</td>
<td align="right">0.0%</td>
<td align="right">6,293</td>
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
<td align="right">232</td>
<td align="right">20.0%</td>
<td align="right">127</td>
<td align="right">12.1%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">926</td>
<td align="right">80.0%</td>
<td align="right">926</td>
<td align="right">87.9%</td>
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
<td align="left">out of range</td>
<td align="right">231</td>
<td align="right">99.6%</td>
<td align="right">126</td>
<td align="right">99.2%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.8%</td>
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
<td align="right">714,403</td>
<td align="right">100.0%</td>
<td align="right">714,403</td>
<td align="right">100.0%</td>
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
<td align="right">648,506</td>
<td align="right">2.8%</td>
<td align="right">648,506</td>
<td align="right">2.8%</td>
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
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
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
<td align="right">651,317</td>
<td align="right">2.8%</td>
<td align="right">651,317</td>
<td align="right">2.8%</td>
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
<td align="right">21,627</td>
<td align="right">100.0%</td>
<td align="right">21,627</td>
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
<td align="right">903</td>
<td align="right">50.0%</td>
<td align="right">903</td>
<td align="right">50.0%</td>
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
<td align="right">903</td>
<td align="right">100.0%</td>
<td align="right">903</td>
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
<td align="right">3,401,059</td>
<td align="right">31.3%</td>
<td align="right">2,961,863</td>
<td align="right">28.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,448,508</td>
<td align="right">68.6%</td>
<td align="right">7,279,762</td>
<td align="right">71.1%</td>
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
<td align="right">2,679</td>
<td align="right">83.6%</td>
<td align="right">2,490</td>
<td align="right">82.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">525</td>
<td align="right">16.4%</td>
<td align="right">525</td>
<td align="right">17.4%</td>
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
<td align="left">baseobject</td>
<td align="right">2,426</td>
<td align="right">90.6%</td>
<td align="right">2,237</td>
<td align="right">89.8%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">253</td>
<td align="right">9.4%</td>
<td align="right">253</td>
<td align="right">10.2%</td>
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
<td align="right">18,738</td>
<td align="right">0.5%</td>
<td align="right">18,738</td>
<td align="right">0.5%</td>
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
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
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
<td align="right">325,229</td>
<td align="right">8.4%</td>
<td align="right">325,229</td>
<td align="right">8.4%</td>
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
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">275</td>
<td align="right">4.1%</td>
<td align="right">275</td>
<td align="right">4.1%</td>
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
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">106</td>
<td align="right">38.5%</td>
<td align="right">106</td>
<td align="right">38.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">683,304</td>
<td align="right">26.9%</td>
<td align="right">287,303</td>
<td align="right">21.1%</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,852,634</td>
<td align="right">73.0%</td>
<td align="right">1,073,964</td>
<td align="right">78.8%</td>
<td align="right">-42.0%</td>
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
<td align="right">2,107</td>
<td align="right">82.0%</td>
<td align="right">1,771</td>
<td align="right">79.3%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">462</td>
<td align="right">18.0%</td>
<td align="right">462</td>
<td align="right">20.7%</td>
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
<td align="left">enumerate</td>
<td align="right">379</td>
<td align="right">18.0%</td>
<td align="right">254</td>
<td align="right">14.3%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">990</td>
<td align="right">47.0%</td>
<td align="right">842</td>
<td align="right">47.5%</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">316</td>
<td align="right">15.0%</td>
<td align="right">274</td>
<td align="right">15.5%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">400</td>
<td align="right">19.0%</td>
<td align="right">379</td>
<td align="right">21.4%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">1.0%</td>
<td align="right">22</td>
<td align="right">1.2%</td>
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
<td align="left">other</td>
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
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
<td align="right">4,007,693</td>
<td align="right">4.6%</td>
<td align="right">3,585,451</td>
<td align="right">4.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,901,969</td>
<td align="right">92.6%</td>
<td align="right">78,232,521</td>
<td align="right">92.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,323,171</td>
<td align="right">2.7%</td>
<td align="right">2,325,227</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">253,498</td>
<td align="right">0.3%</td>
<td align="right">253,498</td>
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
<td align="right">18,571</td>
<td align="right">24.5%</td>
<td align="right">18,380</td>
<td align="right">24.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">57,215</td>
<td align="right">75.5%</td>
<td align="right">57,231</td>
<td align="right">75.7%</td>
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
<td align="left">mutable class</td>
<td align="right">14,996</td>
<td align="right">80.7%</td>
<td align="right">14,807</td>
<td align="right">80.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">592</td>
<td align="right">3.2%</td>
<td align="right">591</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,643</td>
<td align="right">14.2%</td>
<td align="right">2,642</td>
<td align="right">14.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
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
<td align="right">13,791,237</td>
<td align="right">99.9%</td>
<td align="right">12,751,466</td>
<td align="right">99.9%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
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
<td align="right">4,452</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">4,872</td>
<td align="right">100.0%</td>
<td align="right">4,872</td>
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
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">16,355</td>
<td align="right">99.7%</td>
<td align="right">16,355</td>
<td align="right">99.7%</td>
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
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,348,111</td>
<td align="right">6.9%</td>
<td align="right">1,327,071</td>
<td align="right">6.8%</td>
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
<td align="right">18,284,591</td>
<td align="right">93.1%</td>
<td align="right">18,305,247</td>
<td align="right">93.2%</td>
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
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
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
<td align="right">26,736</td>
<td align="right">100.0%</td>
<td align="right">26,352</td>
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
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
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
<td align="right">91,989</td>
<td align="right">99.7%</td>
<td align="right">91,989</td>
<td align="right">99.7%</td>
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
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">126</td>
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
<td align="right">1,963,074</td>
<td align="right">9.7%</td>
<td align="right">1,789,062</td>
<td align="right">9.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,224,095</td>
<td align="right">90.1%</td>
<td align="right">18,096,150</td>
<td align="right">90.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">41,450</td>
<td align="right">0.2%</td>
<td align="right">41,450</td>
<td align="right">0.2%</td>
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
<td align="right">41,201</td>
<td align="right">99.0%</td>
<td align="right">37,921</td>
<td align="right">98.9%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">422</td>
<td align="right">1.0%</td>
<td align="right">422</td>
<td align="right">1.1%</td>
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
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
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
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">231</td>
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
<td align="right">2,073,448</td>
<td align="right">100.0%</td>
<td align="right">2,073,448</td>
<td align="right">100.0%</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">231</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">148,777,150</td>
<td align="right">42.6%</td>
<td align="right">121,056,649</td>
<td align="right">41.6%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,538,015</td>
<td align="right">3.3%</td>
<td align="right">9,717,049</td>
<td align="right">3.3%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,033,971</td>
<td align="right">52.2%</td>
<td align="right">153,467,754</td>
<td align="right">52.8%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">6,621,670</td>
<td align="right">1.9%</td>
<td align="right">6,428,757</td>
<td align="right">2.2%</td>
<td align="right">-2.9%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">88,255</td>
<td align="right">0.8%</td>
<td align="right">4,192</td>
<td align="right">0.0%</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,852,634</td>
<td align="right">17.2%</td>
<td align="right">1,073,964</td>
<td align="right">11.9%</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,401,059</td>
<td align="right">31.6%</td>
<td align="right">2,961,863</td>
<td align="right">32.7%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,007,693</td>
<td align="right">37.2%</td>
<td align="right">3,585,451</td>
<td align="right">39.6%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">6.6%</td>
<td align="right">714,403</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">648,506</td>
<td align="right">6.0%</td>
<td align="right">648,506</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">41,450</td>
<td align="right">0.4%</td>
<td align="right">41,450</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">758,695</td>
<td align="right">11.5%</td>
<td align="right">671,646</td>
<td align="right">10.4%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">856,804</td>
<td align="right">12.9%</td>
<td align="right">769,937</td>
<td align="right">12.0%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,348,111</td>
<td align="right">20.4%</td>
<td align="right">1,327,071</td>
<td align="right">20.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,288,155</td>
<td align="right">19.5%</td>
<td align="right">1,289,563</td>
<td align="right">20.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">739,363</td>
<td align="right">11.2%</td>
<td align="right">740,011</td>
<td align="right">11.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">208,806</td>
<td align="right">3.2%</td>
<td align="right">208,732</td>
<td align="right">3.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">324,298</td>
<td align="right">4.9%</td>
<td align="right">324,298</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">319,627</td>
<td align="right">4.8%</td>
<td align="right">319,627</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">282,563</td>
<td align="right">4.3%</td>
<td align="right">282,563</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">162,763</td>
<td align="right">2.5%</td>
<td align="right">162,763</td>
<td align="right">2.5%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">127</td>
<td align="right">0.0%</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">37,204</td>
<td align="right"></td>
<td align="right">52,679</td>
<td align="right"></td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">7,011,330</td>
<td align="right">3.4%</td>
<td align="right">4,338,146</td>
<td align="right">2.1%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">8,369,063</td>
<td align="right">3.8%</td>
<td align="right">5,288,772</td>
<td align="right">2.4%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">62,370,980</td>
<td align="right">28.6%</td>
<td align="right">73,180,070</td>
<td align="right">33.4%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">63,315,617</td>
<td align="right">30.5%</td>
<td align="right">72,792,231</td>
<td align="right">34.8%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">509,894</td>
<td align="right"></td>
<td align="right">558,943</td>
<td align="right"></td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">87,530,019</td>
<td align="right">42.1%</td>
<td align="right">79,309,526</td>
<td align="right">37.9%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">105,479,693</td>
<td align="right">48.4%</td>
<td align="right">95,927,379</td>
<td align="right">43.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">41,653,619</td>
<td align="right">19.1%</td>
<td align="right">44,748,071</td>
<td align="right">20.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">475,680</td>
<td align="right"></td>
<td align="right">509,130</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">49,932,869</td>
<td align="right">24.0%</td>
<td align="right">52,619,552</td>
<td align="right">25.2%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">14,541</td>
<td align="right">0.1%</td>
<td align="right">14,939</td>
<td align="right">0.1%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,730,007</td>
<td align="right"></td>
<td align="right">13,677,590</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">5,631,280</td>
<td align="right"></td>
<td align="right">5,615,700</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,554,226</td>
<td align="right">40.0%</td>
<td align="right">7,554,855</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,539,622</td>
<td align="right">39.9%</td>
<td align="right">7,539,789</td>
<td align="right">39.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,335,312</td>
<td align="right"></td>
<td align="right">11,335,166</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,337,495</td>
<td align="right">60.0%</td>
<td align="right">11,337,349</td>
<td align="right">60.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,330,919</td>
<td align="right"></td>
<td align="right">7,330,926</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">341,849</td>
<td align="right"></td>
<td align="right">341,849</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">320</td>
<td align="right">529,920</td>
<td align="right">4,206,903</td>
<td align="right">103,072</td>
<td align="right">596,496</td>
<td align="right">320</td>
<td align="right">530,235</td>
<td align="right">4,210,018</td>
<td align="right">102,315</td>
<td align="right">597,959</td>
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">86</td>
<td align="right">16.1%</td>
<td align="right">466</td>
<td align="right">24.5%</td>
<td align="right">441.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">534</td>
<td align="right"></td>
<td align="right">1,902</td>
<td align="right"></td>
<td align="right">256.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">109</td>
<td align="right">20.4%</td>
<td align="right">384</td>
<td align="right">20.2%</td>
<td align="right">252.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">339</td>
<td align="right">63.5%</td>
<td align="right">968</td>
<td align="right">50.9%</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,492,713</td>
<td align="right"></td>
<td align="right">2,948,008</td>
<td align="right"></td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">331,810,567</td>
<td align="right">22,228.7%</td>
<td align="right">460,513,488</td>
<td align="right">15,621.2%</td>
<td align="right">38.8%</td>
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
<td align="right">84</td>
<td align="right">4.4%</td>
<td align="right">84 / 0 !!</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">168</td>
<td align="right">8.8%</td>
<td align="right">168 / 0 !!</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">4.4%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">339</td>
<td align="right"></td>
<td align="right">968</td>
<td align="right"></td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">275</td>
<td align="right">81.1%</td>
<td align="right">737</td>
<td align="right">76.1%</td>
<td align="right">168.0%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">617,097</td>
<td align="right">13.7%</td>
<td align="right">1,623,348</td>
<td align="right">16.1%</td>
<td align="right">163.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">94,696</td>
<td align="right">2.1%</td>
<td align="right">214,520</td>
<td align="right">2.1%</td>
<td align="right">126.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,489,216</td>
<td align="right"></td>
<td align="right">10,104,832</td>
<td align="right"></td>
<td align="right">125.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">3,777,423</td>
<td align="right">84.1%</td>
<td align="right">8,266,964</td>
<td align="right">81.8%</td>
<td align="right">118.9%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
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
<td align="left">22</td>
<td align="right">8.0%</td>
<td align="left">43</td>
<td align="right">5.8%</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">84</td>
<td align="right">30.5%</td>
<td align="left">336</td>
<td align="right">45.6%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">106</td>
<td align="right">38.5%</td>
<td align="left">231</td>
<td align="right">31.3%</td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">7.6%</td>
<td align="left">63</td>
<td align="right">8.5%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">15.3%</td>
<td align="left">64</td>
<td align="right">8.7%</td>
<td align="right">52.4%</td>
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
<td align="left"><= 32</td>
<td align="right">43</td>
<td align="right">12.7%</td>
<td align="right">169</td>
<td align="right">17.5%</td>
<td align="right">293.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">84</td>
<td align="right">24.8%</td>
<td align="right">231</td>
<td align="right">23.9%</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">336</td>
<td align="right">34.7%</td>
<td align="right">217.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">13.0%</td>
<td align="right">126 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">106</td>
<td align="right">11.0%</td>
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
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">6.5%</td>
<td align="right">22</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">252</td>
<td align="right">26.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">294</td>
<td align="right">30.4%</td>
<td align="right">177.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">6.2%</td>
<td align="right">84</td>
<td align="right">8.7%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">85</td>
<td align="right">8.8%</td>
<td align="right">34.9%</td>
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
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,099</td>
<td align="right">105,362</td>
<td align="right">1,384.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,099</td>
<td align="right">80,725</td>
<td align="right">1,037.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">22,365</td>
<td align="right">254,289</td>
<td align="right">1,037.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">142,180</td>
<td align="right">326,199</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">135,081</td>
<td align="right">280,711</td>
<td align="right">107.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,492,713</td>
<td align="right">2,948,008</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,492,713</td>
<td align="right">2,948,008</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">189,556</td>
<td align="right">358,569</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">173,869</td>
<td align="right">321,693</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,657</td>
<td align="right">28,877</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,657</td>
<td align="right">28,877</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">15,657</td>
<td align="right">28,877</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">606,319</td>
<td align="right">1,096,830</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">135,081</td>
<td align="right">243,708</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">525,655</td>
<td align="right">910,508</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">135,767</td>
<td align="right">231,741</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,088,558</td>
<td align="right">1,772,054</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">135,081</td>
<td align="right">219,753</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">135,081</td>
<td align="right">219,753</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">135,081</td>
<td align="right">219,753</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">135,767</td>
<td align="right">219,753</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">194,444</td>
<td align="right">303,071</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,594,416</td>
<td align="right">5,576,427</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">390,574</td>
<td align="right">603,850</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">606,319</td>
<td align="right">928,084</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,539,775</td>
<td align="right">2,318,445</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">698,455</td>
<td align="right">1,050,095</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">2,278,033</td>
<td align="right">3,419,601</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">522,531</td>
<td align="right">783,664</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">981,633</td>
<td align="right">1,460,183</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,201,538</td>
<td align="right">4,729,144</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,853,101</td>
<td align="right">2,722,426</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,051,776</td>
<td align="right">5,913,730</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,531,163</td>
<td align="right">3,666,832</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">193,006</td>
<td align="right">277,069</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">277,069</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">277,069</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">193,006</td>
<td align="right">277,069</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">193,006</td>
<td align="right">277,069</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,656,089</td>
<td align="right">2,370,146</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,708,510</td>
<td align="right">8,128,612</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,447,309</td>
<td align="right">2,051,207</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,988,182</td>
<td align="right">2,793,789</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,988,182</td>
<td align="right">2,793,789</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,988,182</td>
<td align="right">2,793,789</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,988,182</td>
<td align="right">2,792,425</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">734,852</td>
<td align="right">1,031,531</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">2,255,668</td>
<td align="right">3,165,312</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">3,721,468</td>
<td align="right">5,210,939</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,988,182</td>
<td align="right">2,765,185</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">64,378,571</td>
<td align="right">89,250,261</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">248,919</td>
<td align="right">343,590</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">62,828,119</td>
<td align="right">86,538,594</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,092,541</td>
<td align="right">8,365,614</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,938,671</td>
<td align="right">5,396,095</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,655,092</td>
<td align="right">2,259,914</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">3,104,441</td>
<td align="right">4,227,614</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,250,654</td>
<td align="right">1,700,458</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">34,385,692</td>
<td align="right">46,256,031</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">25,934,797</td>
<td align="right">34,821,676</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,039,582</td>
<td align="right">9,449,976</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,283,002</td>
<td align="right">1,722,198</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">5,544,555</td>
<td align="right">7,440,638</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,699,103</td>
<td align="right">4,958,697</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,846,002</td>
<td align="right">2,465,544</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,283,002</td>
<td align="right">1,705,244</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,237,109</td>
<td align="right">12,275,655</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">10,517,504</td>
<td align="right">13,958,047</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">3,692,004</td>
<td align="right">4,878,654</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,692,004</td>
<td align="right">4,877,972</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">3,692,004</td>
<td align="right">4,877,972</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,846,002</td>
<td align="right">2,438,986</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">7,384,008</td>
<td align="right">9,753,897</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,692,004</td>
<td align="right">4,875,925</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">1,846,002</td>
<td align="right">2,436,939</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,039,981</td>
<td align="right">2,569,290</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,101,703</td>
<td align="right">2,628,419</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,117,414</td>
<td align="right">1,367,701</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">791,406</td>
<td align="right">967,742</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">31,351</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,698</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right"></td>
<td align="right">328,325</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right"></td>
<td align="right">328,325</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right"></td>
<td align="right">201,245</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">200,448</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">192,701</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">189,142</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">168,746</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">66,952</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">66,952</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">60,958</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right"></td>
<td align="right">51,521</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">42,273</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">30,306</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">27,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">27,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">26,558</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">26,558</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right"></td>
<td align="right">11,988</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">11,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">11,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">7,726</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">3,212</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">2,978</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">1,766</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">1,364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">682</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">682</td>
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
<td align="right"></td>
<td align="right">42</td>
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
Stats gathered on: 2025-07-01
