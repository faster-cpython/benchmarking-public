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
<td align="right">267,414</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,207,143</td>
<td align="right">469,770</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,308,363</td>
<td align="right">715,050</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,167,181</td>
<td align="right">1,360,235</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,519,444</td>
<td align="right">1,027,624</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">521,115</td>
<td align="right">366,891</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,334,948</td>
<td align="right">1,660,953</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,960</td>
<td align="right">12,369</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">317,268</td>
<td align="right">255,108</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">909,695</td>
<td align="right">738,994</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">838,782</td>
<td align="right">687,372</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">764,736</td>
<td align="right">633,633</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,422,841</td>
<td align="right">5,404,047</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">481,004</td>
<td align="right">406,685</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,952,019</td>
<td align="right">6,812,853</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">26,208</td>
<td align="right">22,491</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,851,169</td>
<td align="right">1,597,384</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,755,223</td>
<td align="right">5,864,739</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,791,279</td>
<td align="right">1,568,847</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,220,447</td>
<td align="right">8,080,251</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,823,386</td>
<td align="right">3,379,656</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,635,385</td>
<td align="right">4,122,313</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">10,525,137</td>
<td align="right">9,418,813</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">25,359,304</td>
<td align="right">27,728,484</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,204,992</td>
<td align="right">2,927,414</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">455,637</td>
<td align="right">416,430</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,576,649</td>
<td align="right">1,442,543</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,819,716</td>
<td align="right">4,432,497</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">14,221,633</td>
<td align="right">13,234,003</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,294,188</td>
<td align="right">1,209,810</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,924,353</td>
<td align="right">4,606,644</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,276,077</td>
<td align="right">1,200,288</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,337,052</td>
<td align="right">3,139,022</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,186,964</td>
<td align="right">3,939,038</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,797,044</td>
<td align="right">6,401,572</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,800,527</td>
<td align="right">8,291,025</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,672,688</td>
<td align="right">4,420,563</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,574,868</td>
<td align="right">6,237,146</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,527,981</td>
<td align="right">1,451,079</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,980,070</td>
<td align="right">29,463,679</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,011,142</td>
<td align="right">1,922,289</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">47,715,381</td>
<td align="right">45,667,356</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,562,542</td>
<td align="right">17,858,601</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">50,064</td>
<td align="right">48,174</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,810,153</td>
<td align="right">5,602,547</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,830,912</td>
<td align="right">4,660,770</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">64,285,198</td>
<td align="right">62,093,891</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,810,347</td>
<td align="right">1,748,964</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,765,693</td>
<td align="right">9,448,950</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,683,486</td>
<td align="right">1,637,139</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,377,518</td>
<td align="right">2,315,232</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">83,316,761</td>
<td align="right">85,477,117</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">77,198,702</td>
<td align="right">75,264,080</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,379,430</td>
<td align="right">23,818,100</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,281,394</td>
<td align="right">14,942,790</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">2,336,901</td>
<td align="right">2,286,753</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,751,159</td>
<td align="right">2,800,992</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,003,572</td>
<td align="right">8,842,563</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,548,873</td>
<td align="right">4,471,761</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">579,330,077</td>
<td align="right">570,649,656</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">136,872,069</td>
<td align="right">138,835,718</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,957,001</td>
<td align="right">2,915,736</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,372,280</td>
<td align="right">16,144,115</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">151,795,322</td>
<td align="right">149,757,462</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">117,403,387</td>
<td align="right">115,972,960</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">75,378,822</td>
<td align="right">74,535,042</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,633,715</td>
<td align="right">2,606,436</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,840,437</td>
<td align="right">135,217,543</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,449,209</td>
<td align="right">17,270,814</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">176,209,986</td>
<td align="right">174,420,185</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,261,155</td>
<td align="right">1,248,702</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,270,584</td>
<td align="right">1,258,131</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,932,292</td>
<td align="right">12,806,166</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,173,483</td>
<td align="right">19,007,583</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">268,926</td>
<td align="right">266,658</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,925,804</td>
<td align="right">5,877,273</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,329,671</td>
<td align="right">1,319,109</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,591,054</td>
<td align="right">11,509,154</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,290,587</td>
<td align="right">9,226,857</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">27,117,824</td>
<td align="right">26,943,398</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">161,848,647</td>
<td align="right">162,697,709</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,134,268</td>
<td align="right">47,894,511</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">814,299</td>
<td align="right">810,525</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,215,983</td>
<td align="right">17,138,787</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">37,830,660</td>
<td align="right">37,937,488</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">65,777,197</td>
<td align="right">65,594,308</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">51,050,834</td>
<td align="right">50,920,739</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">87,337,306</td>
<td align="right">87,129,110</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">101,179,016</td>
<td align="right">101,366,193</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">85,630,468</td>
<td align="right">85,504,340</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">102,095,494</td>
<td align="right">101,950,426</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,599,881</td>
<td align="right">5,593,329</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,224,041</td>
<td align="right">7,216,145</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,983,148</td>
<td align="right">5,987,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,212,176</td>
<td align="right">15,205,330</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,592,490</td>
<td align="right">4,590,474</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,976,305</td>
<td align="right">16,970,740</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,605,926</td>
<td align="right">1,605,422</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,007,067</td>
<td align="right">10,006,290</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">77,715,164</td>
<td align="right">77,713,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,028,470</td>
<td align="right">84,026,370</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,988,385</td>
<td align="right">155,986,285</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,024,936</td>
<td align="right">180,022,836</td>
<td align="right">-0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,251,900</td>
<td align="right">10,251,900</td>
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
<td align="left">CALL</td>
<td align="right">386,809</td>
<td align="right">386,809</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">115,786</td>
<td align="right">115,786</td>
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
<td align="right">9,156,113</td>
<td align="right">13.2%</td>
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
<td align="right">56,516,154</td>
<td align="right">81.6%</td>
<td align="right">56,516,092</td>
<td align="right">81.7%</td>
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
<td align="right">55,452</td>
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
<td align="right">471</td>
<td align="right">0.8%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">6,069</td>
<td align="right">10.9%</td>
<td align="right">6,048</td>
<td align="right">10.9%</td>
<td align="right">-0.3%</td>
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
<td align="right">3,139,022</td>
<td align="right">100.0%</td>
<td align="right">-5.9%</td>
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
<td align="right">241,753,894</td>
<td align="right">99.0%</td>
<td align="right">241,753,860</td>
<td align="right">99.0%</td>
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
<td align="right">2,235,096</td>
<td align="right">0.9%</td>
<td align="right">2,235,096</td>
<td align="right">0.9%</td>
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
<td align="right">117,203</td>
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
<td align="right">798,111</td>
<td align="right">5.8%</td>
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
<td align="right">5,802</td>
<td align="right">46.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,801</td>
<td align="right">53.9%</td>
<td align="right">6,801</td>
<td align="right">54.0%</td>
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
<td align="left">set</td>
<td align="right">63</td>
<td align="right">1.1%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">3,399</td>
<td align="right">58.4%</td>
<td align="right">3,420</td>
<td align="right">58.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">431</td>
<td align="right">7.4%</td>
<td align="right">429</td>
<td align="right">7.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">10.9%</td>
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
<td align="right">4,402,356</td>
<td align="right">26.3%</td>
<td align="right">-5.4%</td>
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
<td align="right">73.6%</td>
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
<td align="right">15,498</td>
<td align="right">85.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,709</td>
<td align="right">14.7%</td>
<td align="right">2,709</td>
<td align="right">14.9%</td>
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
<td align="right">1,680</td>
<td align="right">10.7%</td>
<td align="right">1,638</td>
<td align="right">10.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">6,951</td>
<td align="right">44.3%</td>
<td align="right">6,825</td>
<td align="right">44.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,851</td>
<td align="right">30.9%</td>
<td align="right">4,830</td>
<td align="right">31.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,205</td>
<td align="right">14.1%</td>
<td align="right">2,205</td>
<td align="right">14.2%</td>
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
<td align="right">9,397,014</td>
<td align="right">5.9%</td>
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
<td align="right">124,189,101</td>
<td align="right">76.9%</td>
<td align="right">123,660,660</td>
<td align="right">77.4%</td>
<td align="right">-0.4%</td>
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
<td align="right">26,749,569</td>
<td align="right">16.7%</td>
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
<td align="right">15,312</td>
<td align="right">2.9%</td>
<td align="right">14,304</td>
<td align="right">2.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">512,713</td>
<td align="right">97.1%</td>
<td align="right">512,125</td>
<td align="right">97.3%</td>
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
<td align="left">ascii string</td>
<td align="right">567</td>
<td align="right">3.7%</td>
<td align="right">420</td>
<td align="right">2.9%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,486</td>
<td align="right">22.8%</td>
<td align="right">3,024</td>
<td align="right">21.1%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,326</td>
<td align="right">28.3%</td>
<td align="right">4,053</td>
<td align="right">28.3%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,134</td>
<td align="right">7.4%</td>
<td align="right">1,071</td>
<td align="right">7.5%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,281</td>
<td align="right">8.4%</td>
<td align="right">1,239</td>
<td align="right">8.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,806</td>
<td align="right">11.8%</td>
<td align="right">1,785</td>
<td align="right">12.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">987</td>
<td align="right">6.4%</td>
<td align="right">987</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">651</td>
<td align="right">4.3%</td>
<td align="right">651</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">420</td>
<td align="right">2.7%</td>
<td align="right">420</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">255</td>
<td align="right">1.7%</td>
<td align="right">255</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">210</td>
<td align="right">1.4%</td>
<td align="right">210</td>
<td align="right">1.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">47,452,242</td>
<td align="right">11.9%</td>
<td align="right">47,212,695</td>
<td align="right">11.9%</td>
<td align="right">-0.5%</td>
</tr>
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
<td align="right">132,943,335</td>
<td align="right">33.4%</td>
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
<td align="right">216,809,198</td>
<td align="right">54.5%</td>
<td align="right">216,788,018</td>
<td align="right">54.5%</td>
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
<td align="right">2,589,243</td>
<td align="right">92.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,243</td>
<td align="right">7.1%</td>
<td align="right">198,054</td>
<td align="right">7.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">3,780</td>
<td align="right">1.9%</td>
<td align="right">3,696</td>
<td align="right">1.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">8,148</td>
<td align="right">4.1%</td>
<td align="right">8,043</td>
<td align="right">4.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">5,922</td>
<td align="right">3.0%</td>
<td align="right">5,943</td>
<td align="right">3.0%</td>
<td align="right">0.4%</td>
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
<td align="right">209,641,201</td>
<td align="right">99.9%</td>
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
<td align="right">58,174</td>
<td align="right">0.0%</td>
<td align="right">58,174</td>
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
<td align="right">59,838</td>
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
<td align="right">9,967,629</td>
<td align="right">28.0%</td>
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
<td align="right">172,788</td>
<td align="right">738.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">1,625,694</td>
<td align="right">15.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">8,610</td>
<td align="right">75.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,835</td>
<td align="right">24.9%</td>
<td align="right">2,835</td>
<td align="right">24.8%</td>
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
<td align="right">378</td>
<td align="right">4.4%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,119</td>
<td align="right">83.1%</td>
<td align="right">7,119</td>
<td align="right">82.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">756</td>
<td align="right">8.8%</td>
<td align="right">756</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">252</td>
<td align="right">2.9%</td>
<td align="right">252</td>
<td align="right">2.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">165,311,879</td>
<td align="right">89.0%</td>
<td align="right">167,502,181</td>
<td align="right">89.1%</td>
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
<td align="right">5,304,180</td>
<td align="right">2.9%</td>
<td align="right">5,239,311</td>
<td align="right">2.8%</td>
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
<td align="right">15,035,605</td>
<td align="right">8.1%</td>
<td align="right">15,028,780</td>
<td align="right">8.0%</td>
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
<td align="right">122,643</td>
<td align="right">44.4%</td>
<td align="right">121,425</td>
<td align="right">44.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">153,531</td>
<td align="right">55.6%</td>
<td align="right">153,510</td>
<td align="right">55.8%</td>
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
<td align="left">set</td>
<td align="right">336</td>
<td align="right">0.2%</td>
<td align="right">315</td>
<td align="right">0.2%</td>
<td align="right">-6.2%</td>
</tr>
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
<td align="right">1,995,789,759</td>
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
<td align="right">189,904,191</td>
<td align="right">5.2%</td>
<td align="right">-1.1%</td>
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
<td align="right">1,300,525,387</td>
<td align="right">35.5%</td>
<td align="right">-0.7%</td>
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
<td align="right">179,959,032</td>
<td align="right">4.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">10,502,330</td>
<td align="right">10.0%</td>
<td align="right">9,397,014</td>
<td align="right">9.1%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,337,052</td>
<td align="right">3.2%</td>
<td align="right">3,139,022</td>
<td align="right">3.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,654,292</td>
<td align="right">4.4%</td>
<td align="right">4,402,356</td>
<td align="right">4.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,672,083</td>
<td align="right">1.6%</td>
<td align="right">1,625,694</td>
<td align="right">1.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,219,799</td>
<td align="right">8.7%</td>
<td align="right">9,156,113</td>
<td align="right">8.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,452,242</td>
<td align="right">45.0%</td>
<td align="right">47,212,695</td>
<td align="right">45.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">801,862</td>
<td align="right">0.8%</td>
<td align="right">798,111</td>
<td align="right">0.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,035,605</td>
<td align="right">14.3%</td>
<td align="right">15,028,780</td>
<td align="right">14.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,968,406</td>
<td align="right">9.5%</td>
<td align="right">9,967,629</td>
<td align="right">9.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,235,096</td>
<td align="right">2.1%</td>
<td align="right">2,235,096</td>
<td align="right">2.2%</td>
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
<td align="right">4,313,421</td>
<td align="right">2.4%</td>
<td align="right">4,281,207</td>
<td align="right">2.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">49,240,419</td>
<td align="right">27.3%</td>
<td align="right">49,008,603</td>
<td align="right">27.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,328,690</td>
<td align="right">12.9%</td>
<td align="right">23,367,120</td>
<td align="right">13.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,393,170</td>
<td align="right">7.4%</td>
<td align="right">13,375,299</td>
<td align="right">7.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,387,458</td>
<td align="right">7.4%</td>
<td align="right">13,374,270</td>
<td align="right">7.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">41,255,760</td>
<td align="right">22.9%</td>
<td align="right">41,255,760</td>
<td align="right">22.9%</td>
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
<td align="right">5.2%</td>
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
<td align="right">1,219,280</td>
<td align="right"></td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,411,630</td>
<td align="right"></td>
<td align="right">9,625,868</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">122,813,208</td>
<td align="right">4.9%</td>
<td align="right">121,380,589</td>
<td align="right">4.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">10,712,950</td>
<td align="right"></td>
<td align="right">10,824,298</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">807,253,499</td>
<td align="right">31.6%</td>
<td align="right">815,062,377</td>
<td align="right">31.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,157,251,688</td>
<td align="right">45.3%</td>
<td align="right">1,148,372,571</td>
<td align="right">44.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">855,639,941</td>
<td align="right">34.2%</td>
<td align="right">849,401,915</td>
<td align="right">34.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">900,024,032</td>
<td align="right">36.0%</td>
<td align="right">905,262,740</td>
<td align="right">36.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,548,246</td>
<td align="right">0.6%</td>
<td align="right">1,551,963</td>
<td align="right">0.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">624,200,547</td>
<td align="right">24.9%</td>
<td align="right">625,491,788</td>
<td align="right">25.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">84,682</td>
<td align="right">0.0%</td>
<td align="right">84,850</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">193,879,685</td>
<td align="right"></td>
<td align="right">193,496,817</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">82,894,384</td>
<td align="right">3.2%</td>
<td align="right">82,759,530</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,671,053</td>
<td align="right"></td>
<td align="right">155,773,919</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">114,230,737</td>
<td align="right"></td>
<td align="right">114,192,877</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">136,664,636</td>
<td align="right">54.5%</td>
<td align="right">136,705,341</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">135,031,708</td>
<td align="right">53.8%</td>
<td align="right">135,068,528</td>
<td align="right">53.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">114,115,956</td>
<td align="right">45.5%</td>
<td align="right">114,085,781</td>
<td align="right">45.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">509,006,464</td>
<td align="right">19.9%</td>
<td align="right">509,117,487</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,008,447</td>
<td align="right"></td>
<td align="right">141,038,679</td>
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
<td align="right">6,823</td>
<td align="right">11,053,122</td>
<td align="right">272,254,239</td>
<td align="right">19,816,129</td>
<td align="right">21,417,495</td>
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
<td align="right">5,271</td>
<td align="right">17.1%</td>
<td align="right">292.2%</td>
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
<td align="right">147</td>
<td align="right">0.5%</td>
<td align="right">250.0%</td>
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
<td align="right">30,828</td>
<td align="right"></td>
<td align="right">58.9%</td>
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
<td align="right">24,192</td>
<td align="right">78.5%</td>
<td align="right">43.5%</td>
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
<td align="right">1,239</td>
<td align="right">4.0%</td>
<td align="right">15.7%</td>
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
<td align="right">866,233,636</td>
<td align="right">3,061.0%</td>
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
<td align="right">28,299,056</td>
<td align="right"></td>
<td align="right">-2.0%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">105</td>
<td align="right">0.3%</td>
<td align="right">105 / 0 !!</td>
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
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">5,124</td>
<td align="right">97.2%</td>
<td align="right">306.7%</td>
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
<td align="right">5,271</td>
<td align="right"></td>
<td align="right">292.2%</td>
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
<td align="right">42</td>
<td align="right">0.8%</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">40,951,512</td>
<td align="right">79.1%</td>
<td align="right">398.0%</td>
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
<td align="right">51,781,632</td>
<td align="right"></td>
<td align="right">385.5%</td>
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
<td align="right">1,186,416</td>
<td align="right">2.3%</td>
<td align="right">375.9%</td>
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
<td align="right">9,643,704</td>
<td align="right">18.6%</td>
<td align="right">339.7%</td>
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
<td align="right">86,016</td>
<td align="right">0.2%</td>
<td align="right">86,016 / 0 !!</td>
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
<td align="left">735</td>
<td align="right">14.3%</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">609</td>
<td align="right">48.3%</td>
<td align="left">2,268</td>
<td align="right">44.3%</td>
<td align="right">272.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">315</td>
<td align="right">25.0%</td>
<td align="left">1,953</td>
<td align="right">38.1%</td>
<td align="right">520.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">168</td>
<td align="right">3.3%</td>
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
<td align="right">105</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">357</td>
<td align="right">26.6%</td>
<td align="right">924</td>
<td align="right">17.5%</td>
<td align="right">158.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">672</td>
<td align="right">50.0%</td>
<td align="right">2,898</td>
<td align="right">55.0%</td>
<td align="right">331.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">210</td>
<td align="right">15.6%</td>
<td align="right">1,071</td>
<td align="right">20.3%</td>
<td align="right">410.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">273</td>
<td align="right">5.2%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">147</td>
<td align="right">10.9%</td>
<td align="right">189</td>
<td align="right">3.6%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">651</td>
<td align="right">48.4%</td>
<td align="right">2,457</td>
<td align="right">46.6%</td>
<td align="right">277.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">441</td>
<td align="right">32.8%</td>
<td align="right">2,100</td>
<td align="right">39.8%</td>
<td align="right">376.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">378</td>
<td align="right">7.2%</td>
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
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">67,830</td>
<td align="right">405,552</td>
<td align="right">497.9%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">67,830</td>
<td align="right">405,132</td>
<td align="right">497.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">67,830</td>
<td align="right">404,859</td>
<td align="right">496.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">26,565</td>
<td align="right">157,668</td>
<td align="right">493.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">65,793</td>
<td align="right">264,264</td>
<td align="right">301.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">73,689</td>
<td align="right">281,295</td>
<td align="right">281.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">19,173</td>
<td align="right">67,368</td>
<td align="right">251.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">168,546</td>
<td align="right">578,865</td>
<td align="right">243.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">247,149</td>
<td align="right">773,052</td>
<td align="right">212.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">344,148</td>
<td align="right">923,664</td>
<td align="right">168.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">103,236</td>
<td align="right">273,903</td>
<td align="right">165.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">538,776</td>
<td align="right">1,429,260</td>
<td align="right">165.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">153,678</td>
<td align="right">348,285</td>
<td align="right">126.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">238,686</td>
<td align="right">490,622</td>
<td align="right">105.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">377,769</td>
<td align="right">773,241</td>
<td align="right">104.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">550,473</td>
<td align="right">1,063,545</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">954,996</td>
<td align="right">1,798,629</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">252,273</td>
<td align="right">474,705</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">330,498</td>
<td align="right">618,639</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">73,479</td>
<td align="right">137,193</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">170,856</td>
<td align="right">316,763</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">170,856</td>
<td align="right">316,763</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">159,873</td>
<td align="right">293,979</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,011,549</td>
<td align="right">1,819,020</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,791,385</td>
<td align="right">631,029</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">584,388</td>
<td align="right">971,607</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">484,701</td>
<td align="right">801,444</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">661,059</td>
<td align="right">1,083,243</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,385,034</td>
<td align="right">2,264,283</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">170,856</td>
<td align="right">64,049</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">817,656</td>
<td align="right">1,306,620</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,007,328</td>
<td align="right">1,489,383</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,068,942</td>
<td align="right">1,578,444</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,709</td>
<td align="right">1,449</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">1,833,720</td>
<td align="right">2,671,557</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">434,784</td>
<td align="right">632,814</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,691,949</td>
<td align="right">2,456,538</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">1,556,667</td>
<td align="right">2,197,608</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">72,975</td>
<td align="right">43,806</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">389,592</td>
<td align="right">541,002</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,824,480</td>
<td align="right">2,498,475</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">565,506</td>
<td align="right">773,702</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,111,126</td>
<td align="right">4,224,233</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,293,830</td>
<td align="right">3,100,776</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">738,906</td>
<td align="right">986,832</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">8,888,397</td>
<td align="right">11,797,044</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,871,478</td>
<td align="right">2,424,870</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">1,701,084</td>
<td align="right">2,193,366</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">640,773</td>
<td align="right">819,168</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">8,155,098</td>
<td align="right">10,282,335</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,768,325</td>
<td align="right">3,540,978</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">445,956</td>
<td align="right">332,493</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">497,445</td>
<td align="right">623,573</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,177,802</td>
<td align="right">6,184,503</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,512,837</td>
<td align="right">4,172,657</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,649,214</td>
<td align="right">2,044,392</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">9,203,964</td>
<td align="right">11,388,005</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">9,203,964</td>
<td align="right">11,388,005</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">10,280,070</td>
<td align="right">7,870,087</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">10,240,380</td>
<td align="right">7,870,087</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,121,835</td>
<td align="right">7,518,967</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,121,835</td>
<td align="right">7,504,603</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,087,275</td>
<td align="right">1,321,824</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,659,819</td>
<td align="right">2,004,765</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">7,884,996</td>
<td align="right">9,519,446</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,965,386</td>
<td align="right">5,984,180</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">14,516,250</td>
<td align="right">17,470,950</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">7,821,891</td>
<td align="right">9,359,069</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">6,628,649</td>
<td align="right">7,901,228</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">7,970,467</td>
<td align="right">9,460,353</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,823,525</td>
<td align="right">9,224,227</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,796,438</td>
<td align="right">9,156,883</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">375,900</td>
<td align="right">438,060</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">375,900</td>
<td align="right">437,283</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">375,900</td>
<td align="right">437,283</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,437,344</td>
<td align="right">2,832,984</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,546,332</td>
<td align="right">5,283,705</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,546,332</td>
<td align="right">5,283,705</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,791,665</td>
<td align="right">13,671,985</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,465,774</td>
<td align="right">7,466,949</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,112,118</td>
<td align="right">1,282,533</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,663,263</td>
<td align="right">1,917,048</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,257,878</td>
<td align="right">2,596,482</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,483,920</td>
<td align="right">5,109,426</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,639,491</td>
<td align="right">1,867,656</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,639,491</td>
<td align="right">1,867,656</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,082,711</td>
<td align="right">9,180,990</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">120,136,147</td>
<td align="right">136,421,225</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">614,208</td>
<td align="right">697,347</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">5,490,305</td>
<td align="right">4,762,358</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">148,689,559</td>
<td align="right">167,653,311</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,624,936</td>
<td align="right">4,960,326</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">12,349,134</td>
<td align="right">13,770,561</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">30,440,025</td>
<td align="right">33,905,530</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">38,063,024</td>
<td align="right">42,165,352</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">920,699</td>
<td align="right">1,009,552</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,244,523</td>
<td align="right">1,362,312</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,745,730</td>
<td align="right">1,898,652</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,192,503</td>
<td align="right">5,678,106</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">10,710,380</td>
<td align="right">9,858,135</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,192,380</td>
<td align="right">2,353,389</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,364,388</td>
<td align="right">4,641,966</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">982,926</td>
<td align="right">1,045,212</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">4,322,770</td>
<td align="right">4,596,040</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">7,295,631</td>
<td align="right">7,739,361</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">7,295,631</td>
<td align="right">7,739,361</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">43,389,578</td>
<td align="right">45,770,006</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,750,180</td>
<td align="right">3,945,396</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">4,068,858</td>
<td align="right">4,262,267</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">28,804,826</td>
<td align="right">28,033,343</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">28,873,328</td>
<td align="right">28,299,056</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,777,963</td>
<td align="right">3,824,352</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">12,445,820</td>
<td align="right">12,514,340</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,405,595</td>
<td align="right">2,401,457</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">154,224</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">126,126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">77,196</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">77,112</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">76,902</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">76,902</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">75,789</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">74,319</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">74,319</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">50,148</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">48,531</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">41,265</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">39,207</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">25,515</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">25,074</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">12,453</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">12,453</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">10,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">10,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">7,896</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">6,825</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">6,804</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">6,552</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right"></td>
<td align="right">5,565</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">3,717</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">3,717</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">3,591</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">2,268</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right"></td>
<td align="right">2,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">2,016</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">1,890</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">777</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">714</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">504</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">189</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">168</td>
<td align="right">252</td>
<td align="right">50.0%</td>
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
Stats gathered on: 2025-07-02
