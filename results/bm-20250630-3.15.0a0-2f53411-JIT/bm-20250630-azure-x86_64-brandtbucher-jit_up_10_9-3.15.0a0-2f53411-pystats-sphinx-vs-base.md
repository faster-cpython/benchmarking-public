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
<td align="right">2,345,282</td>
<td align="right">131,376</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,220,447</td>
<td align="right">5,404,335</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,207,143</td>
<td align="right">733,572</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,308,363</td>
<td align="right">884,205</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,167,181</td>
<td align="right">1,565,972</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,823,386</td>
<td align="right">2,770,698</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,851,169</td>
<td align="right">1,424,764</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">909,695</td>
<td align="right">701,365</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,519,444</td>
<td align="right">1,216,792</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">317,268</td>
<td align="right">268,170</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,334,948</td>
<td align="right">1,977,045</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,983,148</td>
<td align="right">5,220,183</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,952,019</td>
<td align="right">6,996,518</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">481,004</td>
<td align="right">424,955</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,791,279</td>
<td align="right">1,603,287</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,672,688</td>
<td align="right">4,184,753</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">838,782</td>
<td align="right">753,270</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">25,359,304</td>
<td align="right">27,830,402</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,294,188</td>
<td align="right">1,179,948</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,635,385</td>
<td align="right">4,251,316</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,819,716</td>
<td align="right">4,420,926</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,422,841</td>
<td align="right">5,905,190</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,576,649</td>
<td align="right">1,458,797</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">764,736</td>
<td align="right">709,338</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,011,142</td>
<td align="right">1,868,989</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">10,525,137</td>
<td align="right">9,814,032</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,204,992</td>
<td align="right">2,990,078</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">14,221,633</td>
<td align="right">13,315,588</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,186,964</td>
<td align="right">3,921,818</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,800,527</td>
<td align="right">8,268,870</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,797,044</td>
<td align="right">6,392,731</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,755,223</td>
<td align="right">6,376,278</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,810,347</td>
<td align="right">1,712,991</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,980,070</td>
<td align="right">29,440,115</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,751,159</td>
<td align="right">2,624,256</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">47,715,381</td>
<td align="right">45,580,500</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,337,052</td>
<td align="right">3,188,393</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,276,077</td>
<td align="right">1,220,028</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,527,981</td>
<td align="right">1,470,021</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">521,115</td>
<td align="right">501,879</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,281,394</td>
<td align="right">14,789,385</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,683,486</td>
<td align="right">1,632,078</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,924,353</td>
<td align="right">4,775,967</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,562,542</td>
<td align="right">18,029,016</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,574,868</td>
<td align="right">6,393,113</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">83,316,761</td>
<td align="right">85,524,136</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">117,403,387</td>
<td align="right">114,300,907</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,372,280</td>
<td align="right">15,956,354</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,830,912</td>
<td align="right">4,711,506</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,003,572</td>
<td align="right">8,802,271</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,173,483</td>
<td align="right">18,748,401</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">64,285,198</td>
<td align="right">62,935,465</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,765,693</td>
<td align="right">9,582,741</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,377,518</td>
<td align="right">2,334,510</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,379,430</td>
<td align="right">23,954,768</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,810,153</td>
<td align="right">5,716,535</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">579,330,077</td>
<td align="right">570,902,826</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">136,872,069</td>
<td align="right">138,759,236</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,548,873</td>
<td align="right">4,492,824</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,449,209</td>
<td align="right">17,240,952</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,840,437</td>
<td align="right">135,300,895</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">455,637</td>
<td align="right">450,828</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">151,795,322</td>
<td align="right">150,253,403</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">2,336,901</td>
<td align="right">2,317,959</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,261,155</td>
<td align="right">1,251,327</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,270,584</td>
<td align="right">1,260,756</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">37,830,660</td>
<td align="right">37,545,165</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">176,209,986</td>
<td align="right">174,962,827</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">75,378,822</td>
<td align="right">74,888,157</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,932,292</td>
<td align="right">12,856,818</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">85,630,468</td>
<td align="right">85,172,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">27,117,824</td>
<td align="right">26,992,832</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,134,268</td>
<td align="right">47,917,524</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,591,054</td>
<td align="right">11,539,772</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">87,337,306</td>
<td align="right">86,987,170</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,290,587</td>
<td align="right">9,257,361</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">101,179,016</td>
<td align="right">101,515,521</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">65,777,197</td>
<td align="right">65,584,228</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">161,848,647</td>
<td align="right">162,309,210</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">51,050,834</td>
<td align="right">50,912,276</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,215,983</td>
<td align="right">17,169,699</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,633,715</td>
<td align="right">2,640,351</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,957,001</td>
<td align="right">2,952,192</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,925,804</td>
<td align="right">5,920,995</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">102,095,494</td>
<td align="right">102,026,530</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">77,198,702</td>
<td align="right">77,167,209</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">814,299</td>
<td align="right">814,259</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,329,671</td>
<td align="right">1,329,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">115,786</td>
<td align="right">115,783</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">386,809</td>
<td align="right">386,806</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,024,936</td>
<td align="right">180,024,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,988,385</td>
<td align="right">155,988,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,028,470</td>
<td align="right">84,028,470</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">77,715,164</td>
<td align="right">77,715,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">60,118,084</td>
<td align="right">60,118,084</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">38,929,372</td>
<td align="right">38,929,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,282,244</td>
<td align="right">38,282,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,037,722</td>
<td align="right">38,037,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">23,418,066</td>
<td align="right">23,418,066</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,362,992</td>
<td align="right">22,362,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,976,305</td>
<td align="right">16,976,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,743,237</td>
<td align="right">16,743,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,389,793</td>
<td align="right">16,389,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,212,176</td>
<td align="right">15,212,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,251,900</td>
<td align="right">10,251,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,007,067</td>
<td align="right">10,007,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,224,041</td>
<td align="right">7,224,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,599,881</td>
<td align="right">5,599,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,490,197</td>
<td align="right">5,490,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,762,634</td>
<td align="right">4,762,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,623,789</td>
<td align="right">4,623,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,592,490</td>
<td align="right">4,592,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,826,557</td>
<td align="right">3,826,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,962,124</td>
<td align="right">2,962,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,669,058</td>
<td align="right">2,669,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">2,141,685</td>
<td align="right">2,141,685</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,680,433</td>
<td align="right">1,680,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,680,433</td>
<td align="right">1,680,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,635,556</td>
<td align="right">1,635,556</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,605,926</td>
<td align="right">1,605,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,318,107</td>
<td align="right">1,318,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,134,400</td>
<td align="right">1,134,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,295</td>
<td align="right">1,133,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">970,368</td>
<td align="right">970,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">859,927</td>
<td align="right">859,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">800,260</td>
<td align="right">800,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">636,846</td>
<td align="right">636,846</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">528,898</td>
<td align="right">528,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">501,619</td>
<td align="right">501,619</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">479,872</td>
<td align="right">479,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300,198</td>
<td align="right">300,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">292,824</td>
<td align="right">292,824</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">268,926</td>
<td align="right">268,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">261,862</td>
<td align="right">261,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">250,335</td>
<td align="right">250,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">194,775</td>
<td align="right">194,775</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">194,586</td>
<td align="right">194,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">169,848</td>
<td align="right">169,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">157,941</td>
<td align="right">157,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">157,374</td>
<td align="right">157,374</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">152,838</td>
<td align="right">152,838</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">149,667</td>
<td align="right">149,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">130,851</td>
<td align="right">130,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">121,770</td>
<td align="right">121,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">114,345</td>
<td align="right">114,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">88,431</td>
<td align="right">88,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">83,055</td>
<td align="right">83,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">82,047</td>
<td align="right">82,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">66,465</td>
<td align="right">66,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">62,713</td>
<td align="right">62,713</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">50,251</td>
<td align="right">50,251</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">50,064</td>
<td align="right">50,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">48,027</td>
<td align="right">48,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">37,170</td>
<td align="right">37,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">26,691</td>
<td align="right">26,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">26,208</td>
<td align="right">26,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">25,473</td>
<td align="right">25,473</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,191</td>
<td align="right">16,191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,960</td>
<td align="right">15,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">11,554</td>
<td align="right">11,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,561</td>
<td align="right">10,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">10,019</td>
<td align="right">10,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,631</td>
<td align="right">8,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,610</td>
<td align="right">8,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,610</td>
<td align="right">8,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">6,258</td>
<td align="right">6,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">6,027</td>
<td align="right">6,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,830</td>
<td align="right">4,830</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">3,675</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,520</td>
<td align="right">2,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">2,457</td>
<td align="right">2,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,205</td>
<td align="right">2,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,079</td>
<td align="right">2,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">1,554</td>
<td align="right">1,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">777</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">294</td>
<td align="right">294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
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
<td align="right">9,219,799</td>
<td align="right">13.3%</td>
<td align="right">9,186,602</td>
<td align="right">13.3%</td>
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
<td align="right">56,516,154</td>
<td align="right">81.6%</td>
<td align="right">56,516,118</td>
<td align="right">81.6%</td>
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
<td align="right">3,473,658</td>
<td align="right">5.0%</td>
<td align="right">3,473,658</td>
<td align="right">5.0%</td>
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
<td align="right">55,496</td>
<td align="right">40.8%</td>
<td align="right">55,467</td>
<td align="right">40.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">80,392</td>
<td align="right">59.2%</td>
<td align="right">80,392</td>
<td align="right">59.2%</td>
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
<td align="left">floor divide</td>
<td align="right">494</td>
<td align="right">0.9%</td>
<td align="right">465</td>
<td align="right">0.8%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">24,108</td>
<td align="right">43.4%</td>
<td align="right">24,108</td>
<td align="right">43.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">8,966</td>
<td align="right">16.2%</td>
<td align="right">8,966</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">6,069</td>
<td align="right">10.9%</td>
<td align="right">6,069</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">4,515</td>
<td align="right">8.1%</td>
<td align="right">4,515</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,654</td>
<td align="right">6.6%</td>
<td align="right">3,654</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,352</td>
<td align="right">4.2%</td>
<td align="right">2,352</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,512</td>
<td align="right">2.7%</td>
<td align="right">1,512</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">693</td>
<td align="right">1.2%</td>
<td align="right">693</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">651</td>
<td align="right">1.2%</td>
<td align="right">651</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">630</td>
<td align="right">1.1%</td>
<td align="right">630</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">546</td>
<td align="right">1.0%</td>
<td align="right">546</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">315</td>
<td align="right">0.6%</td>
<td align="right">315</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">210</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">126</td>
<td align="right">0.2%</td>
<td align="right">126</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">84</td>
<td align="right">0.2%</td>
<td align="right">84</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">3,337,052</td>
<td align="right">100.0%</td>
<td align="right">3,188,393</td>
<td align="right">100.0%</td>
<td align="right">-4.5%</td>
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
<td align="right">2,235,096</td>
<td align="right">0.9%</td>
<td align="right">2,235,095</td>
<td align="right">0.9%</td>
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
<td align="right">241,753,894</td>
<td align="right">99.0%</td>
<td align="right">241,753,863</td>
<td align="right">99.0%</td>
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
<td align="right">1,965,490</td>
<td align="right">0.8%</td>
<td align="right">1,965,490</td>
<td align="right">0.8%</td>
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
<td align="right">117,203</td>
<td align="right">100.0%</td>
<td align="right">117,201</td>
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
<td align="right">1,344</td>
<td align="right">1,344 / 0 !!</td>
<td align="right">1,344</td>
<td align="right">1,344 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
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
<td align="right">6,785</td>
<td align="right">58.4%</td>
<td align="right">6,785</td>
<td align="right">58.4%</td>
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
<td align="right">63</td>
<td align="right">0.5%</td>
<td align="right">63</td>
<td align="right">0.5%</td>
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
<td align="right">4,832</td>
<td align="right">100.0%</td>
<td align="right">4,832</td>
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
<td align="right">801,862</td>
<td align="right">5.9%</td>
<td align="right">801,830</td>
<td align="right">5.9%</td>
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
<td align="right">12,839,184</td>
<td align="right">94.0%</td>
<td align="right">12,839,184</td>
<td align="right">94.0%</td>
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
<td align="right">11,757</td>
<td align="right">0.1%</td>
<td align="right">11,757</td>
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
<td align="right">5,825</td>
<td align="right">46.1%</td>
<td align="right">5,817</td>
<td align="right">46.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,801</td>
<td align="right">53.9%</td>
<td align="right">6,801</td>
<td align="right">53.9%</td>
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
<td align="right">431</td>
<td align="right">7.4%</td>
<td align="right">423</td>
<td align="right">7.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">3,399</td>
<td align="right">58.4%</td>
<td align="right">3,399</td>
<td align="right">58.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">777</td>
<td align="right">13.3%</td>
<td align="right">777</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">630</td>
<td align="right">10.8%</td>
<td align="right">630</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">336</td>
<td align="right">5.8%</td>
<td align="right">336</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">147</td>
<td align="right">2.5%</td>
<td align="right">147</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">63</td>
<td align="right">1.1%</td>
<td align="right">63</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21</td>
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
<td align="right">4,654,292</td>
<td align="right">27.3%</td>
<td align="right">4,166,483</td>
<td align="right">25.2%</td>
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
<td align="right">12,347,391</td>
<td align="right">72.5%</td>
<td align="right">12,347,391</td>
<td align="right">74.7%</td>
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
<td align="right">15,687</td>
<td align="right">85.3%</td>
<td align="right">15,561</td>
<td align="right">85.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,709</td>
<td align="right">14.7%</td>
<td align="right">2,709</td>
<td align="right">14.8%</td>
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
<td align="right">4,851</td>
<td align="right">30.9%</td>
<td align="right">4,767</td>
<td align="right">30.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">6,951</td>
<td align="right">44.3%</td>
<td align="right">6,909</td>
<td align="right">44.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,205</td>
<td align="right">14.1%</td>
<td align="right">2,205</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,680</td>
<td align="right">10.7%</td>
<td align="right">1,680</td>
<td align="right">10.8%</td>
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
<td align="right">10,502,330</td>
<td align="right">6.5%</td>
<td align="right">9,791,435</td>
<td align="right">6.1%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">124,189,101</td>
<td align="right">76.9%</td>
<td align="right">124,840,129</td>
<td align="right">77.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,780,628</td>
<td align="right">16.6%</td>
<td align="right">26,777,394</td>
<td align="right">16.6%</td>
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
<td align="right">15,312</td>
<td align="right">2.9%</td>
<td align="right">15,102</td>
<td align="right">2.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">512,713</td>
<td align="right">97.1%</td>
<td align="right">512,650</td>
<td align="right">97.1%</td>
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
<td align="left">ascii string</td>
<td align="right">567</td>
<td align="right">3.7%</td>
<td align="right">504</td>
<td align="right">3.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,326</td>
<td align="right">28.3%</td>
<td align="right">4,242</td>
<td align="right">28.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,134</td>
<td align="right">7.4%</td>
<td align="right">1,113</td>
<td align="right">7.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,281</td>
<td align="right">8.4%</td>
<td align="right">1,260</td>
<td align="right">8.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,486</td>
<td align="right">22.8%</td>
<td align="right">3,465</td>
<td align="right">22.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,806</td>
<td align="right">11.8%</td>
<td align="right">1,806</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">987</td>
<td align="right">6.4%</td>
<td align="right">987</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">651</td>
<td align="right">4.3%</td>
<td align="right">651</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">2.7%</td>
<td align="right">420</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">255</td>
<td align="right">1.7%</td>
<td align="right">255</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">210</td>
<td align="right">1.4%</td>
<td align="right">210</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">189</td>
<td align="right">1.2%</td>
<td align="right">189</td>
<td align="right">1.3%</td>
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
<td align="right">38,634,036</td>
<td align="right">38,634,036 / 0 !!</td>
<td align="right">38,634,036</td>
<td align="right">38,634,036 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">24,168,606</td>
<td align="right">24,168,606 / 0 !!</td>
<td align="right">24,168,606</td>
<td align="right">24,168,606 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20,927,193</td>
<td align="right">20,927,193 / 0 !!</td>
<td align="right">20,927,193</td>
<td align="right">20,927,193 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,706,416</td>
<td align="right">3,706,416 / 0 !!</td>
<td align="right">3,706,416</td>
<td align="right">3,706,416 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">216,249</td>
<td align="right">216,249 / 0 !!</td>
<td align="right">216,249</td>
<td align="right">216,249 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">151,053</td>
<td align="right">151,053 / 0 !!</td>
<td align="right">151,053</td>
<td align="right">151,053 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">52,626</td>
<td align="right">52,626 / 0 !!</td>
<td align="right">52,626</td>
<td align="right">52,626 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">44,890</td>
<td align="right">44,890 / 0 !!</td>
<td align="right">44,890</td>
<td align="right">44,890 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,743</td>
<td align="right">1,743 / 0 !!</td>
<td align="right">1,743</td>
<td align="right">1,743 / 0 !!</td>
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
<td align="right">133,145,856</td>
<td align="right">33.4%</td>
<td align="right">131,840,167</td>
<td align="right">33.3%</td>
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
<td align="right">47,452,242</td>
<td align="right">11.9%</td>
<td align="right">47,236,382</td>
<td align="right">11.9%</td>
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
<td align="right">216,809,198</td>
<td align="right">54.5%</td>
<td align="right">216,656,329</td>
<td align="right">54.7%</td>
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
<td align="right">62,727</td>
<td align="right">0.0%</td>
<td align="right">62,727</td>
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
<td align="right">2,593,170</td>
<td align="right">92.9%</td>
<td align="right">2,568,472</td>
<td align="right">92.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,243</td>
<td align="right">7.1%</td>
<td align="right">198,159</td>
<td align="right">7.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">3,780</td>
<td align="right">1.9%</td>
<td align="right">3,738</td>
<td align="right">1.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">8,148</td>
<td align="right">4.1%</td>
<td align="right">8,106</td>
<td align="right">4.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">5,922</td>
<td align="right">3.0%</td>
<td align="right">5,922</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,268</td>
<td align="right">1.1%</td>
<td align="right">2,268</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,176</td>
<td align="right">0.6%</td>
<td align="right">1,176</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,074</td>
<td align="right">0.5%</td>
<td align="right">1,074</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">504</td>
<td align="right">0.3%</td>
<td align="right">504</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">399</td>
<td align="right">0.2%</td>
<td align="right">399</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">210</td>
<td align="right">0.1%</td>
<td align="right">210</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">209,107,875</td>
<td align="right">99.9%</td>
<td align="right">210,077,668</td>
<td align="right">99.9%</td>
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
<td align="right">58,174</td>
<td align="right">0.0%</td>
<td align="right">58,173</td>
<td align="right">0.0%</td>
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
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">189</td>
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
<td align="right">111,384</td>
<td align="right">0.1%</td>
<td align="right">111,384</td>
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
<td align="left">Success</td>
<td align="right">59,838</td>
<td align="right">100.0%</td>
<td align="right">59,836</td>
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
<td align="right">1,050</td>
<td align="right">0.2%</td>
<td align="right">1,050</td>
<td align="right">0.2%</td>
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
<td align="right">450,765</td>
<td align="right">99.5%</td>
<td align="right">450,765</td>
<td align="right">99.5%</td>
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
<td align="right">1,029</td>
<td align="right">100.0%</td>
<td align="right">1,029</td>
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
<td align="right">4,620</td>
<td align="right">30.0%</td>
<td align="right">4,620</td>
<td align="right">30.0%</td>
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
<td align="right">10,561</td>
<td align="right">68.6%</td>
<td align="right">10,561</td>
<td align="right">68.6%</td>
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
<td align="right">84</td>
<td align="right">40.0%</td>
<td align="right">84</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">126</td>
<td align="right">60.0%</td>
<td align="right">126</td>
<td align="right">60.0%</td>
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
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">126</td>
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
<td align="right">9,968,406</td>
<td align="right">28.0%</td>
<td align="right">9,968,406</td>
<td align="right">28.0%</td>
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
<td align="right">16,133,668</td>
<td align="right">45.3%</td>
<td align="right">16,133,668</td>
<td align="right">45.3%</td>
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
<td align="right">9,462,432</td>
<td align="right">26.6%</td>
<td align="right">9,462,432</td>
<td align="right">26.6%</td>
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
<td align="right">192,612</td>
<td align="right">89.2%</td>
<td align="right">192,612</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">23,394</td>
<td align="right">10.8%</td>
<td align="right">23,394</td>
<td align="right">10.8%</td>
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
<td align="right">172,809</td>
<td align="right">738.7%</td>
<td align="right">172,809</td>
<td align="right">738.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">12,201</td>
<td align="right">52.2%</td>
<td align="right">12,201</td>
<td align="right">52.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,263</td>
<td align="right">18.2%</td>
<td align="right">4,263</td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,667</td>
<td align="right">11.4%</td>
<td align="right">2,667</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,512</td>
<td align="right">6.5%</td>
<td align="right">1,512</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">651</td>
<td align="right">2.8%</td>
<td align="right">651</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">378</td>
<td align="right">1.6%</td>
<td align="right">378</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">273</td>
<td align="right">1.2%</td>
<td align="right">273</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">105</td>
<td align="right">0.4%</td>
<td align="right">105</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">194,775</td>
<td align="right">100.0%</td>
<td align="right">194,775</td>
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
<td align="right">1,672,083</td>
<td align="right">15.4%</td>
<td align="right">1,620,717</td>
<td align="right">15.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,180,044</td>
<td align="right">84.5%</td>
<td align="right">9,180,044</td>
<td align="right">84.9%</td>
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
<td align="right">8,568</td>
<td align="right">75.1%</td>
<td align="right">8,526</td>
<td align="right">75.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,835</td>
<td align="right">24.9%</td>
<td align="right">2,835</td>
<td align="right">25.0%</td>
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
<td align="left">bytearray int</td>
<td align="right">336</td>
<td align="right">3.9%</td>
<td align="right">294</td>
<td align="right">3.4%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,119</td>
<td align="right">83.1%</td>
<td align="right">7,119</td>
<td align="right">83.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">756</td>
<td align="right">8.8%</td>
<td align="right">756</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">252</td>
<td align="right">2.9%</td>
<td align="right">252</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">105</td>
<td align="right">1.2%</td>
<td align="right">105</td>
<td align="right">1.2%</td>
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
<td align="right">5,304,180</td>
<td align="right">2.9%</td>
<td align="right">5,105,541</td>
<td align="right">2.7%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">165,311,879</td>
<td align="right">89.0%</td>
<td align="right">167,525,344</td>
<td align="right">89.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,035,605</td>
<td align="right">8.1%</td>
<td align="right">15,035,605</td>
<td align="right">8.0%</td>
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
<td align="right">122,643</td>
<td align="right">44.4%</td>
<td align="right">118,905</td>
<td align="right">43.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">153,531</td>
<td align="right">55.6%</td>
<td align="right">153,531</td>
<td align="right">56.4%</td>
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
<td align="left">number</td>
<td align="right">133,623</td>
<td align="right">87.0%</td>
<td align="right">133,623</td>
<td align="right">87.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,676</td>
<td align="right">7.6%</td>
<td align="right">11,676</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">4,956</td>
<td align="right">3.2%</td>
<td align="right">4,956</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,512</td>
<td align="right">1.0%</td>
<td align="right">1,512</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,281</td>
<td align="right">0.8%</td>
<td align="right">1,281</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">336</td>
<td align="right">0.2%</td>
<td align="right">336</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">147</td>
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
<td align="right">295,661</td>
<td align="right">1.9%</td>
<td align="right">295,661</td>
<td align="right">1.9%</td>
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
<td align="right">14,985,714</td>
<td align="right">98.0%</td>
<td align="right">14,985,714</td>
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
<td align="right">4,201</td>
<td align="right">92.6%</td>
<td align="right">4,201</td>
<td align="right">92.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">336</td>
<td align="right">7.4%</td>
<td align="right">336</td>
<td align="right">7.4%</td>
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
<td align="right">273</td>
<td align="right">81.2%</td>
<td align="right">273</td>
<td align="right">81.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">63</td>
<td align="right">18.8%</td>
<td align="right">63</td>
<td align="right">18.8%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,019,346,206</td>
<td align="right">54.5%</td>
<td align="right">1,995,014,704</td>
<td align="right">54.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">192,030,097</td>
<td align="right">5.2%</td>
<td align="right">190,030,838</td>
<td align="right">5.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">180,257,472</td>
<td align="right">4.9%</td>
<td align="right">178,749,920</td>
<td align="right">4.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,310,304,223</td>
<td align="right">35.4%</td>
<td align="right">1,303,324,311</td>
<td align="right">35.5%</td>
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
<td align="right">4,654,292</td>
<td align="right">4.4%</td>
<td align="right">4,166,483</td>
<td align="right">4.0%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">10,502,330</td>
<td align="right">10.0%</td>
<td align="right">9,791,435</td>
<td align="right">9.4%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,337,052</td>
<td align="right">3.2%</td>
<td align="right">3,188,393</td>
<td align="right">3.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,672,083</td>
<td align="right">1.6%</td>
<td align="right">1,620,717</td>
<td align="right">1.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,452,242</td>
<td align="right">45.0%</td>
<td align="right">47,236,382</td>
<td align="right">45.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,219,799</td>
<td align="right">8.7%</td>
<td align="right">9,186,602</td>
<td align="right">8.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">801,862</td>
<td align="right">0.8%</td>
<td align="right">801,830</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,235,096</td>
<td align="right">2.1%</td>
<td align="right">2,235,095</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,035,605</td>
<td align="right">14.3%</td>
<td align="right">15,035,605</td>
<td align="right">14.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,968,406</td>
<td align="right">9.5%</td>
<td align="right">9,968,406</td>
<td align="right">9.6%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">49,240,419</td>
<td align="right">27.3%</td>
<td align="right">48,054,514</td>
<td align="right">26.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,313,421</td>
<td align="right">2.4%</td>
<td align="right">4,213,944</td>
<td align="right">2.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,328,690</td>
<td align="right">12.9%</td>
<td align="right">23,213,106</td>
<td align="right">13.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,387,458</td>
<td align="right">7.4%</td>
<td align="right">13,385,400</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,393,170</td>
<td align="right">7.4%</td>
<td align="right">13,391,994</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">41,255,760</td>
<td align="right">22.9%</td>
<td align="right">41,255,760</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,183,383</td>
<td align="right">5.6%</td>
<td align="right">10,183,383</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,406,950</td>
<td align="right">5.2%</td>
<td align="right">9,406,950</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,587,951</td>
<td align="right">4.2%</td>
<td align="right">7,587,951</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,345,112</td>
<td align="right">1.3%</td>
<td align="right">2,345,112</td>
<td align="right">1.3%</td>
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
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,847,736</td>
<td align="right">81.7%</td>
<td align="right">178,847,736</td>
<td align="right">81.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
<td align="right">40,170,608</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,585,628</td>
<td align="right">18.1%</td>
<td align="right">39,585,628</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,980</td>
<td align="right">0.3%</td>
<td align="right">584,980</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">6,846</td>
<td align="right">0.0%</td>
<td align="right">6,846</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,553,309</td>
<td align="right">18.1%</td>
<td align="right">39,553,309</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">25,473</td>
<td align="right">0.0%</td>
<td align="right">25,473</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,614,999</td>
<td align="right">4.8%</td>
<td align="right">10,614,999</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">500,829</td>
<td align="right">0.2%</td>
<td align="right">500,829</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,307,548</td>
<td align="right">8.4%</td>
<td align="right">18,307,548</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">5,376</td>
<td align="right">0.0%</td>
<td align="right">5,376</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,770,069</td>
<td align="right">3.1%</td>
<td align="right">6,770,069</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,942,216</td>
<td align="right">72.6%</td>
<td align="right">158,942,216</td>
<td align="right">72.6%</td>
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
<td align="right">1,322,209</td>
<td align="right"></td>
<td align="right">1,217,471</td>
<td align="right"></td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">10,712,950</td>
<td align="right"></td>
<td align="right">10,285,878</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,411,630</td>
<td align="right"></td>
<td align="right">9,089,450</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">122,813,208</td>
<td align="right">4.9%</td>
<td align="right">121,250,206</td>
<td align="right">4.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,157,251,688</td>
<td align="right">45.3%</td>
<td align="right">1,145,324,208</td>
<td align="right">44.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">855,639,941</td>
<td align="right">34.2%</td>
<td align="right">846,884,102</td>
<td align="right">33.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">807,253,499</td>
<td align="right">31.6%</td>
<td align="right">814,829,236</td>
<td align="right">31.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">900,024,032</td>
<td align="right">36.0%</td>
<td align="right">904,510,863</td>
<td align="right">36.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">509,006,464</td>
<td align="right">19.9%</td>
<td align="right">508,393,768</td>
<td align="right">19.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,548,246</td>
<td align="right">0.6%</td>
<td align="right">1,549,380</td>
<td align="right">0.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">624,200,547</td>
<td align="right">24.9%</td>
<td align="right">624,654,157</td>
<td align="right">25.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,671,053</td>
<td align="right"></td>
<td align="right">155,775,749</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">82,894,384</td>
<td align="right">3.2%</td>
<td align="right">82,838,954</td>
<td align="right">3.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">84,682</td>
<td align="right">0.0%</td>
<td align="right">84,724</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">193,879,685</td>
<td align="right"></td>
<td align="right">193,963,890</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">114,230,737</td>
<td align="right"></td>
<td align="right">114,195,667</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">114,115,956</td>
<td align="right">45.5%</td>
<td align="right">114,088,881</td>
<td align="right">45.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">136,664,636</td>
<td align="right">54.5%</td>
<td align="right">136,694,756</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">135,031,708</td>
<td align="right">53.8%</td>
<td align="right">135,060,652</td>
<td align="right">53.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,008,447</td>
<td align="right"></td>
<td align="right">141,026,446</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,323,355</td>
<td align="right"></td>
<td align="right">3,323,355</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">981,855</td>
<td align="right">29.5%</td>
<td align="right">981,855</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">97,356</td>
<td align="right">2.9%</td>
<td align="right">97,356</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,323</td>
<td align="right">0.0%</td>
<td align="right">1,323</td>
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
<td align="right">6,823</td>
<td align="right">11,077,203</td>
<td align="right">258,977,982</td>
<td align="right">16,766,235</td>
<td align="right">21,496,929</td>
<td align="right">6,825</td>
<td align="right">11,049,988</td>
<td align="right">272,328,321</td>
<td align="right">19,826,809</td>
<td align="right">21,377,531</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,344</td>
<td align="right">6.9%</td>
<td align="right">2,604</td>
<td align="right">11.1%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,071</td>
<td align="right">5.5%</td>
<td align="right">1,953</td>
<td align="right">8.3%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">210</td>
<td align="right">0.9%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">19,404</td>
<td align="right"></td>
<td align="right">23,499</td>
<td align="right"></td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">779,343,363</td>
<td align="right">2,699.2%</td>
<td align="right">865,816,963</td>
<td align="right">2,803.7%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">16,863</td>
<td align="right">86.9%</td>
<td align="right">18,732</td>
<td align="right">79.7%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">28,873,328</td>
<td align="right"></td>
<td align="right">30,881,112</td>
<td align="right"></td>
<td align="right">7.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,260</td>
<td align="right">93.8%</td>
<td align="right">2,499</td>
<td align="right">96.0%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,344</td>
<td align="right"></td>
<td align="right">2,604</td>
<td align="right"></td>
<td align="right">93.8%</td>
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
<td align="right">8,223,600</td>
<td align="right">77.1%</td>
<td align="right">17,113,068</td>
<td align="right">78.9%</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">249,312</td>
<td align="right">2.3%</td>
<td align="right">515,928</td>
<td align="right">2.4%</td>
<td align="right">106.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">10,665,984</td>
<td align="right"></td>
<td align="right">21,676,032</td>
<td align="right"></td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,193,072</td>
<td align="right">20.6%</td>
<td align="right">4,047,036</td>
<td align="right">18.7%</td>
<td align="right">84.5%</td>
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
<td align="left">336</td>
<td align="right">26.7%</td>
<td align="left">693</td>
<td align="right">27.7%</td>
<td align="right">106.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">609</td>
<td align="right">48.3%</td>
<td align="left">1,113</td>
<td align="right">44.5%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">315</td>
<td align="right">25.0%</td>
<td align="left">609</td>
<td align="right">24.4%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">84</td>
<td align="right">3.4%</td>
<td align="right"></td>
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
<td align="left"><= 16</td>
<td align="right">105</td>
<td align="right">7.8%</td>
<td align="right">252</td>
<td align="right">9.7%</td>
<td align="right">140.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">357</td>
<td align="right">26.6%</td>
<td align="right">630</td>
<td align="right">24.2%</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">672</td>
<td align="right">50.0%</td>
<td align="right">1,365</td>
<td align="right">52.4%</td>
<td align="right">103.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">210</td>
<td align="right">15.6%</td>
<td align="right">294</td>
<td align="right">11.3%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">2.4%</td>
<td align="right"></td>
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
<td align="left"><= 8</td>
<td align="right">21</td>
<td align="right">1.6%</td>
<td align="right">84</td>
<td align="right">3.2%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">147</td>
<td align="right">10.9%</td>
<td align="right">315</td>
<td align="right">12.1%</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">651</td>
<td align="right">48.4%</td>
<td align="right">1,176</td>
<td align="right">45.2%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">441</td>
<td align="right">32.8%</td>
<td align="right">840</td>
<td align="right">32.3%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">84</td>
<td align="right">3.2%</td>
<td align="right"></td>
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
<td align="left">_ERROR_POP_N</td>
<td align="right">2,709</td>
<td align="right">45,402</td>
<td align="right">1,576.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">67,830</td>
<td align="right">249,585</td>
<td align="right">268.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">67,830</td>
<td align="right">249,585</td>
<td align="right">268.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">67,830</td>
<td align="right">249,585</td>
<td align="right">268.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">19,173</td>
<td align="right">64,302</td>
<td align="right">235.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">26,565</td>
<td align="right">81,963</td>
<td align="right">208.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">153,678</td>
<td align="right">473,886</td>
<td align="right">208.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">238,686</td>
<td align="right">726,495</td>
<td align="right">204.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">103,236</td>
<td align="right">311,535</td>
<td align="right">201.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">168,546</td>
<td align="right">446,334</td>
<td align="right">164.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">73,689</td>
<td align="right">167,307</td>
<td align="right">127.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">344,148</td>
<td align="right">755,370</td>
<td align="right">119.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">247,149</td>
<td align="right">539,889</td>
<td align="right">118.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">170,856</td>
<td align="right">361,011</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">170,856</td>
<td align="right">361,011</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">377,769</td>
<td align="right">782,082</td>
<td align="right">107.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">497,445</td>
<td align="right">954,933</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">72,975</td>
<td align="right">7,896</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,791,385</td>
<td align="right">584,010</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">170,856</td>
<td align="right">298,536</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">252,273</td>
<td align="right">440,265</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">159,873</td>
<td align="right">277,725</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,385,034</td>
<td align="right">2,367,078</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">538,776</td>
<td align="right">917,721</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">550,473</td>
<td align="right">934,542</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">330,498</td>
<td align="right">558,390</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">584,388</td>
<td align="right">983,178</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">661,059</td>
<td align="right">1,098,363</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">565,506</td>
<td align="right">915,642</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,011,549</td>
<td align="right">1,566,852</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">954,996</td>
<td align="right">1,472,457</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,068,942</td>
<td align="right">1,600,599</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">73,479</td>
<td align="right">106,680</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,007,328</td>
<td align="right">1,434,510</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">817,656</td>
<td align="right">1,132,215</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,691,949</td>
<td align="right">2,341,101</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">484,701</td>
<td align="right">667,653</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,871,478</td>
<td align="right">2,559,984</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">738,906</td>
<td align="right">1,004,052</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,121,835</td>
<td align="right">8,291,240</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,121,835</td>
<td align="right">8,281,664</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">434,784</td>
<td align="right">583,443</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,745,730</td>
<td align="right">2,338,728</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">640,773</td>
<td align="right">849,030</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,768,325</td>
<td align="right">3,255,588</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,405,595</td>
<td align="right">3,168,560</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,512,837</td>
<td align="right">3,827,796</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">4,322,770</td>
<td align="right">5,607,060</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">445,956</td>
<td align="right">315,000</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">4,068,858</td>
<td align="right">5,228,996</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,293,830</td>
<td align="right">2,895,039</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">8,888,397</td>
<td align="right">11,190,816</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">375,900</td>
<td align="right">473,256</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">375,900</td>
<td align="right">473,256</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,663,263</td>
<td align="right">2,089,668</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,649,214</td>
<td align="right">2,071,377</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,639,491</td>
<td align="right">2,055,417</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,639,491</td>
<td align="right">2,055,417</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,177,802</td>
<td align="right">6,124,730</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">10,280,070</td>
<td align="right">7,768,379</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">10,240,380</td>
<td align="right">7,768,379</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,437,344</td>
<td align="right">3,015,852</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">1,833,720</td>
<td align="right">2,259,684</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,111,126</td>
<td align="right">3,822,021</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">389,592</td>
<td align="right">475,104</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">8,155,098</td>
<td align="right">9,932,958</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,257,878</td>
<td align="right">2,749,887</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">7,970,467</td>
<td align="right">9,677,741</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,087,275</td>
<td align="right">1,317,099</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,659,819</td>
<td align="right">1,995,273</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,624,936</td>
<td align="right">4,505,865</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,824,480</td>
<td align="right">2,182,383</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,823,525</td>
<td align="right">9,250,710</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">1,701,084</td>
<td align="right">2,003,736</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">30,440,025</td>
<td align="right">35,817,060</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">1,556,667</td>
<td align="right">1,812,489</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,082,711</td>
<td align="right">9,333,723</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">920,699</td>
<td align="right">1,062,852</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,203,964</td>
<td align="right">10,554,537</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,203,964</td>
<td align="right">10,554,537</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">7,295,631</td>
<td align="right">8,348,319</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">7,295,631</td>
<td align="right">8,348,319</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">14,516,250</td>
<td align="right">16,591,008</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">6,628,649</td>
<td align="right">7,572,705</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">5,490,305</td>
<td align="right">4,709,880</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,465,774</td>
<td align="right">7,383,957</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,791,665</td>
<td align="right">13,427,841</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,192,503</td>
<td align="right">5,334,336</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">375,900</td>
<td align="right">424,998</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">12,349,134</td>
<td align="right">13,960,103</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">7,821,891</td>
<td align="right">8,819,664</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">148,689,559</td>
<td align="right">167,250,140</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">7,884,996</td>
<td align="right">8,829,576</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">120,136,147</td>
<td align="right">134,436,524</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,796,438</td>
<td align="right">8,707,625</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,112,118</td>
<td align="right">1,231,524</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">614,208</td>
<td align="right">678,594</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,965,386</td>
<td align="right">5,483,037</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,546,332</td>
<td align="right">5,019,903</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,546,332</td>
<td align="right">5,019,903</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">65,793</td>
<td align="right">72,051</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">43,389,578</td>
<td align="right">47,472,120</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,192,380</td>
<td align="right">2,393,681</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,244,523</td>
<td align="right">1,357,293</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,483,920</td>
<td align="right">4,808,748</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">28,873,328</td>
<td align="right">30,881,112</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">28,804,826</td>
<td align="right">30,763,659</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">38,063,024</td>
<td align="right">40,209,431</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,364,388</td>
<td align="right">4,579,302</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">982,926</td>
<td align="right">1,025,934</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,750,180</td>
<td align="right">3,900,708</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">10,710,380</td>
<td align="right">10,308,711</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">12,445,820</td>
<td align="right">12,784,863</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,777,963</td>
<td align="right">3,829,329</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">182,385</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">75,474</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">57,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">57,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">56,049</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">56,049</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">56,049</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">56,049</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">46,284</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">19,236</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">18,942</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">9,828</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">9,828</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">9,471</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">4,809</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">4,809</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">4,809</td>
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
<td align="right">21</td>
<td align="right">63</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">168</td>
<td align="right">273</td>
<td align="right">62.5%</td>
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
<td align="right">22,239</td>
<td align="right">22,239</td>
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
<td align="right">462</td>
<td align="right">462</td>
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
<td align="right">483</td>
<td align="right">483</td>
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
Stats gathered on: 2025-07-01
