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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">543</td>
<td align="right">5,491,087</td>
<td align="right">1,011,149.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">14,867</td>
<td align="right">426,672</td>
<td align="right">2,769.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">168,817</td>
<td align="right">4,723,599</td>
<td align="right">2,698.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">115,813</td>
<td align="right">939,629</td>
<td align="right">711.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">184,009</td>
<td align="right">593,697</td>
<td align="right">222.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,177,748</td>
<td align="right">6,578,694</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">805,892</td>
<td align="right">1,184,851</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">889,844</td>
<td align="right">1,235,403</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,791,240</td>
<td align="right">3,851,427</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,110,823</td>
<td align="right">1,428,934</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,637</td>
<td align="right">12,515</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,537,514</td>
<td align="right">3,145,991</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,683,179</td>
<td align="right">2,062,138</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">689,975</td>
<td align="right">590,294</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,761,441</td>
<td align="right">8,834,615</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">735,596</td>
<td align="right">668,473</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,492,184</td>
<td align="right">1,357,960</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">501,374</td>
<td align="right">456,426</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,166,582</td>
<td align="right">4,706,676</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,017,494</td>
<td align="right">1,838,458</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,854,873</td>
<td align="right">6,249,204</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,019,494</td>
<td align="right">929,442</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,621,526</td>
<td align="right">2,851,625</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,045,743</td>
<td align="right">1,866,707</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,859,745</td>
<td align="right">1,697,655</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,028,001</td>
<td align="right">938,540</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,500,573</td>
<td align="right">1,370,211</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,695,543</td>
<td align="right">1,548,774</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,083,564</td>
<td align="right">1,904,528</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,189,361</td>
<td align="right">1,087,346</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,891,438</td>
<td align="right">1,729,291</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">786,088</td>
<td align="right">718,710</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">524,149</td>
<td align="right">479,500</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">524,472</td>
<td align="right">479,823</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">263,106</td>
<td align="right">240,756</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">817,043</td>
<td align="right">749,913</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,663,953</td>
<td align="right">1,528,742</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">284,017</td>
<td align="right">261,296</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">280,949</td>
<td align="right">258,475</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,455,096</td>
<td align="right">3,180,923</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">286,831</td>
<td align="right">264,380</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,992,564</td>
<td align="right">6,451,876</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,785,266</td>
<td align="right">2,997,508</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,236,708</td>
<td align="right">10,382,722</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,399,715</td>
<td align="right">8,685,796</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,793,347</td>
<td align="right">5,356,937</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,274,442</td>
<td align="right">5,822,604</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,264,764</td>
<td align="right">13,248,969</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,973,503</td>
<td align="right">1,835,206</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,203,640</td>
<td align="right">3,918,758</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,269,991</td>
<td align="right">3,998,977</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,799,267</td>
<td align="right">12,539,659</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">30,144,365</td>
<td align="right">28,254,764</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">100,932</td>
<td align="right">94,653</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,917,313</td>
<td align="right">3,674,380</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,809,994</td>
<td align="right">3,575,615</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">16,206,522</td>
<td align="right">15,214,025</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80,191,808</td>
<td align="right">75,332,553</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,825,906</td>
<td align="right">24,280,556</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,373,575</td>
<td align="right">16,363,305</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,170,430</td>
<td align="right">1,103,330</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">386,042</td>
<td align="right">364,091</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,193,752</td>
<td align="right">3,014,648</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,471,710</td>
<td align="right">1,389,448</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,214,169</td>
<td align="right">1,147,092</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,353,204</td>
<td align="right">5,648,701</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,475,412</td>
<td align="right">14,683,381</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,974,399</td>
<td align="right">15,173,847</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,750,949</td>
<td align="right">2,618,316</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,820,314</td>
<td align="right">7,453,374</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">673,632</td>
<td align="right">644,997</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,111,653</td>
<td align="right">1,066,850</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,551,218</td>
<td align="right">9,170,798</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">336</td>
<td align="right">349</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">113</td>
<td align="right">109</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,698,910</td>
<td align="right">21,948,530</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,190,976</td>
<td align="right">7,981,648</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">505</td>
<td align="right">494</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,370</td>
<td align="right">205,200</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,629,135</td>
<td align="right">5,707,768</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,860</td>
<td align="right">456,711</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,652</td>
<td align="right">1,639</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,213</td>
<td align="right">5,180</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">362,120</td>
<td align="right">364,150</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,235</td>
<td align="right">3,245</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">77,853</td>
<td align="right">78,064</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,611</td>
<td align="right">13,578</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,389,694</td>
<td align="right">6,376,528</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,834</td>
<td align="right">17,801</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,834</td>
<td align="right">17,801</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">129,869</td>
<td align="right">130,109</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,592</td>
<td align="right">4,599</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">204,645</td>
<td align="right">204,868</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,281</td>
<td align="right">97,369</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,996</td>
<td align="right">40,959</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,398</td>
<td align="right">46,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,042</td>
<td align="right">34,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">68,013</td>
<td align="right">68,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">545,090</td>
<td align="right">545,272</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,472</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,491</td>
<td align="right">102,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,752</td>
<td align="right">928,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,014</td>
<td align="right">191,027</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,658</td>
<td align="right">81,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,672</td>
<td align="right">1,818,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">105,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">87,032</td>
<td align="right">87,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,432</td>
<td align="right">86,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">84,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">77,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">67,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,119</td>
<td align="right">59,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,866</td>
<td align="right">55,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,862</td>
<td align="right">55,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,904</td>
<td align="right">42,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,133</td>
<td align="right">35,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,559</td>
<td align="right">29,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">17,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">14,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286</td>
<td align="right">10,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,870</td>
<td align="right">9,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">8,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">806</td>
<td align="right">806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">267</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
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
<td align="right">12,204,170</td>
<td align="right">99.3%</td>
<td align="right">11,196,479</td>
<td align="right">99.3%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,276</td>
<td align="right">0.1%</td>
<td align="right">12,983</td>
<td align="right">0.1%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">67,329</td>
<td align="right">0.5%</td>
<td align="right">67,344</td>
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
<td align="right">378</td>
<td align="right">41.0%</td>
<td align="right">392</td>
<td align="right">41.6%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">543</td>
<td align="right">59.0%</td>
<td align="right">550</td>
<td align="right">58.4%</td>
<td align="right">1.3%</td>
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
<td align="left">remainder</td>
<td align="right">288</td>
<td align="right">53.0%</td>
<td align="right">295</td>
<td align="right">53.6%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">34.4%</td>
<td align="right">187</td>
<td align="right">34.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">12.2%</td>
<td align="right">66</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
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
<td align="right">14,143</td>
<td align="right">100.0%</td>
<td align="right">14,143</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">708,068</td>
<td align="right">94.5%</td>
<td align="right">663,120</td>
<td align="right">94.2%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,730</td>
<td align="right">5.4%</td>
<td align="right">40,697</td>
<td align="right">5.8%</td>
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
<td align="right">148</td>
<td align="right">55.6%</td>
<td align="right">144</td>
<td align="right">55.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">44.4%</td>
<td align="right">118</td>
<td align="right">45.0%</td>
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
<td align="left">buffer int</td>
<td align="right">147</td>
<td align="right">99.3%</td>
<td align="right">143</td>
<td align="right">99.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">0.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,364,994</td>
<td align="right">100.0%</td>
<td align="right">27,304,140</td>
<td align="right">100.0%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,058</td>
<td align="right">0.0%</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">796</td>
<td align="right">0.0%</td>
<td align="right">796</td>
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
<td align="right">3,330</td>
<td align="right">100.0%</td>
<td align="right">3,355</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">1,018,317</td>
<td align="right">16.7%</td>
<td align="right">928,283</td>
<td align="right">16.2%</td>
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
<td align="right">5,049,107</td>
<td align="right">83.0%</td>
<td align="right">4,780,829</td>
<td align="right">83.5%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,535</td>
<td align="right">0.2%</td>
<td align="right">14,018</td>
<td align="right">0.2%</td>
<td align="right">3.6%</td>
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
<td align="right">507</td>
<td align="right">35.7%</td>
<td align="right">522</td>
<td align="right">36.9%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">915</td>
<td align="right">64.3%</td>
<td align="right">891</td>
<td align="right">63.1%</td>
<td align="right">-2.6%</td>
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
<td align="right">627</td>
<td align="right">68.5%</td>
<td align="right">596</td>
<td align="right">66.9%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">147</td>
<td align="right">16.1%</td>
<td align="right">154</td>
<td align="right">17.3%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">10.5%</td>
<td align="right">96</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.8%</td>
<td align="right">44</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,148,553</td>
<td align="right">100.0%</td>
<td align="right">1,991,961</td>
<td align="right">100.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">270</td>
<td align="right">0.0%</td>
<td align="right">270</td>
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
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">9</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">82.7%</td>
<td align="right">43</td>
<td align="right">82.7%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">115,485</td>
<td align="right">1.6%</td>
<td align="right">939,093</td>
<td align="right">7.6%</td>
<td align="right">713.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,979,217</td>
<td align="right">98.4%</td>
<td align="right">11,380,403</td>
<td align="right">92.4%</td>
<td align="right">63.1%</td>
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
<td align="right">276</td>
<td align="right">84.1%</td>
<td align="right">488</td>
<td align="right">91.0%</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">15.9%</td>
<td align="right">48</td>
<td align="right">9.0%</td>
<td align="right">-7.7%</td>
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
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">182.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">182.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,388,286</td>
<td align="right">16.5%</td>
<td align="right">8,674,482</td>
<td align="right">16.2%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,089,026</td>
<td align="right">82.8%</td>
<td align="right">44,572,403</td>
<td align="right">83.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">384,654</td>
<td align="right">0.7%</td>
<td align="right">388,685</td>
<td align="right">0.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">6,954</td>
<td align="right">37.8%</td>
<td align="right">6,791</td>
<td align="right">37.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,435</td>
<td align="right">62.2%</td>
<td align="right">11,565</td>
<td align="right">63.0%</td>
<td align="right">1.1%</td>
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
<td align="right">800</td>
<td align="right">11.5%</td>
<td align="right">754</td>
<td align="right">11.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,874</td>
<td align="right">26.9%</td>
<td align="right">1,768</td>
<td align="right">26.0%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,439</td>
<td align="right">20.7%</td>
<td align="right">1,432</td>
<td align="right">21.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">683</td>
<td align="right">9.8%</td>
<td align="right">681</td>
<td align="right">10.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.6%</td>
<td align="right">460</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.6%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
<td align="right">22,363,850</td>
<td align="right">100.0%</td>
<td align="right">21,550,132</td>
<td align="right">100.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">867</td>
<td align="right">0.0%</td>
<td align="right">863</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">243</td>
<td align="right">0.0%</td>
<td align="right">243</td>
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
<td align="right">2,374</td>
<td align="right">100.0%</td>
<td align="right">2,388</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">2,761,425</td>
<td align="right">100.0%</td>
<td align="right">2,515,258</td>
<td align="right">100.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,193,994</td>
<td align="right">96.5%</td>
<td align="right">5,746,117</td>
<td align="right">96.3%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,937</td>
<td align="right">1.2%</td>
<td align="right">79,939</td>
<td align="right">1.3%</td>
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
<td align="right">140,400</td>
<td align="right">2.2%</td>
<td align="right">140,400</td>
<td align="right">2.4%</td>
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
<td align="right">3,614</td>
<td align="right">82.9%</td>
<td align="right">3,616</td>
<td align="right">83.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.1%</td>
<td align="right">743</td>
<td align="right">17.0%</td>
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
<td align="right">738</td>
<td align="right">99.3%</td>
<td align="right">752</td>
<td align="right">101.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">344</td>
<td align="right">46.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,213,546</td>
<td align="right">99.0%</td>
<td align="right">2,052,872</td>
<td align="right">99.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,264</td>
<td align="right">1.0%</td>
<td align="right">21,266</td>
<td align="right">1.0%</td>
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
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">187</td>
<td align="right">90.8%</td>
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
<td align="left">py simple</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">182,806</td>
<td align="right">1.2%</td>
<td align="right">592,383</td>
<td align="right">4.1%</td>
<td align="right">224.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,006,240</td>
<td align="right">98.8%</td>
<td align="right">13,782,129</td>
<td align="right">95.9%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">750</td>
<td align="right">62.3%</td>
<td align="right">859</td>
<td align="right">65.4%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">453</td>
<td align="right">37.7%</td>
<td align="right">455</td>
<td align="right">34.6%</td>
<td align="right">0.4%</td>
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
<td align="right">126</td>
<td align="right">16.8%</td>
<td align="right">232</td>
<td align="right">27.0%</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">145</td>
<td align="right">19.3%</td>
<td align="right">147</td>
<td align="right">17.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">301</td>
<td align="right">40.1%</td>
<td align="right">302</td>
<td align="right">35.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">14.8%</td>
<td align="right">111</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.9%</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
<td align="right">2,242,729</td>
<td align="right">100.0%</td>
<td align="right">2,197,847</td>
<td align="right">100.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">10,953,858</td>
<td align="right">2.5%</td>
<td align="right">11,383,403</td>
<td align="right">2.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">263,846,954</td>
<td align="right">59.5%</td>
<td align="right">258,967,703</td>
<td align="right">58.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">552,013</td>
<td align="right">0.1%</td>
<td align="right">557,236</td>
<td align="right">0.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">167,826,523</td>
<td align="right">37.9%</td>
<td align="right">169,110,908</td>
<td align="right">38.4%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">115,485</td>
<td align="right">1.1%</td>
<td align="right">939,093</td>
<td align="right">8.3%</td>
<td align="right">713.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">182,806</td>
<td align="right">1.7%</td>
<td align="right">592,383</td>
<td align="right">5.2%</td>
<td align="right">224.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,018,317</td>
<td align="right">9.3%</td>
<td align="right">928,283</td>
<td align="right">8.2%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,388,286</td>
<td align="right">85.9%</td>
<td align="right">8,674,482</td>
<td align="right">76.4%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,058</td>
<td align="right">0.0%</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,730</td>
<td align="right">0.4%</td>
<td align="right">40,697</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">67,329</td>
<td align="right">0.6%</td>
<td align="right">67,344</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">21,266</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.7%</td>
<td align="right">79,939</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">6,006</td>
<td align="right">1.1%</td>
<td align="right">6,408</td>
<td align="right">1.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,270</td>
<td align="right">1.1%</td>
<td align="right">6,575</td>
<td align="right">1.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">13,534</td>
<td align="right">2.5%</td>
<td align="right">14,017</td>
<td align="right">2.5%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">315,236</td>
<td align="right">57.1%</td>
<td align="right">319,269</td>
<td align="right">57.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,386</td>
<td align="right">10.8%</td>
<td align="right">59,384</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">25.4%</td>
<td align="right">140,400</td>
<td align="right">25.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.8%</td>
<td align="right">9,895</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">631,716</td>
<td align="right">1.7%</td>
<td align="right">587,038</td>
<td align="right">1.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">32,906,146</td>
<td align="right">86.8%</td>
<td align="right">30,764,729</td>
<td align="right">86.0%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">28,375,829</td>
<td align="right">74.8%</td>
<td align="right">26,614,832</td>
<td align="right">74.4%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">9,128,138</td>
<td align="right">24.1%</td>
<td align="right">8,747,718</td>
<td align="right">24.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">9,128,197</td>
<td align="right">24.1%</td>
<td align="right">8,747,777</td>
<td align="right">24.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,555,576</td>
<td align="right">25.2%</td>
<td align="right">9,175,156</td>
<td align="right">25.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,555,576</td>
<td align="right">25.2%</td>
<td align="right">9,175,156</td>
<td align="right">25.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,849</td>
<td align="right">0.0%</td>
<td align="right">17,816</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.1%</td>
<td align="right">427,379</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.2%</td>
<td align="right">456,471</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.2%</td>
<td align="right">441,509</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">146,900</td>
<td align="right"></td>
<td align="right">115,200</td>
<td align="right"></td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">204,907</td>
<td align="right"></td>
<td align="right">160,817</td>
<td align="right"></td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">58,305</td>
<td align="right"></td>
<td align="right">45,885</td>
<td align="right"></td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">163,402,439</td>
<td align="right">33.8%</td>
<td align="right">138,429,695</td>
<td align="right">30.9%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">150,590,585</td>
<td align="right">25.7%</td>
<td align="right">128,914,974</td>
<td align="right">23.8%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">76,486,834</td>
<td align="right">15.8%</td>
<td align="right">67,565,908</td>
<td align="right">15.1%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">114,437,134</td>
<td align="right">19.6%</td>
<td align="right">104,780,258</td>
<td align="right">19.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,141,216</td>
<td align="right"></td>
<td align="right">1,962,066</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">14,544,072</td>
<td align="right"></td>
<td align="right">13,393,189</td>
<td align="right"></td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">27,471,830</td>
<td align="right">60.5%</td>
<td align="right">25,728,640</td>
<td align="right">60.1%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">27,473,423</td>
<td align="right"></td>
<td align="right">25,730,509</td>
<td align="right"></td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">13,917,591</td>
<td align="right"></td>
<td align="right">13,079,556</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">19,752,533</td>
<td align="right"></td>
<td align="right">18,723,415</td>
<td align="right"></td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">94,107,523</td>
<td align="right">16.1%</td>
<td align="right">89,364,001</td>
<td align="right">16.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">17,811,351</td>
<td align="right">39.2%</td>
<td align="right">16,939,310</td>
<td align="right">39.6%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">17,932,658</td>
<td align="right">39.5%</td>
<td align="right">17,060,590</td>
<td align="right">39.9%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">225,829,273</td>
<td align="right">38.6%</td>
<td align="right">219,389,786</td>
<td align="right">40.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">71,232,184</td>
<td align="right">14.7%</td>
<td align="right">70,481,355</td>
<td align="right">15.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">172,246,381</td>
<td align="right">35.6%</td>
<td align="right">171,428,134</td>
<td align="right">38.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,711</td>
<td align="right">0.2%</td>
<td align="right">77,687</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,596</td>
<td align="right">0.1%</td>
<td align="right">43,593</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,987</td>
<td align="right">85.2%</td>
<td align="right">703</td>
<td align="right">33.0%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">22,675,319</td>
<td align="right"></td>
<td align="right">16,281,963</td>
<td align="right"></td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">501,133,538</td>
<td align="right">2,210.0%</td>
<td align="right">390,928,222</td>
<td align="right">2,401.0%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">88</td>
<td align="right">3.8%</td>
<td align="right">79</td>
<td align="right">3.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">287</td>
<td align="right">12.3%</td>
<td align="right">258</td>
<td align="right">12.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,331</td>
<td align="right"></td>
<td align="right">2,131</td>
<td align="right"></td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,956</td>
<td align="right">83.9%</td>
<td align="right">1,794</td>
<td align="right">84.2%</td>
<td align="right">-8.3%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">287</td>
<td align="right"></td>
<td align="right">258</td>
<td align="right"></td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">287</td>
<td align="right">100.0%</td>
<td align="right">258</td>
<td align="right">100.0%</td>
<td align="right">-10.1%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">501,512</td>
<td align="right">12.5%</td>
<td align="right">456,416</td>
<td align="right">12.5%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">2,840,827</td>
<td align="right">70.8%</td>
<td align="right">2,589,020</td>
<td align="right">70.8%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,009,984</td>
<td align="right"></td>
<td align="right">3,657,728</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">667,645</td>
<td align="right">16.6%</td>
<td align="right">612,292</td>
<td align="right">16.7%</td>
<td align="right">-8.3%</td>
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
<td align="left">92</td>
<td align="right">32.1%</td>
<td align="left">80</td>
<td align="right">31.0%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">69</td>
<td align="right">24.0%</td>
<td align="left">60</td>
<td align="right">23.3%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">60</td>
<td align="right">20.9%</td>
<td align="left">56</td>
<td align="right">21.7%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">51</td>
<td align="right">17.8%</td>
<td align="left">48</td>
<td align="right">18.6%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">15</td>
<td align="right">5.2%</td>
<td align="left">14</td>
<td align="right">5.4%</td>
<td align="right">-6.7%</td>
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
<td align="right">71</td>
<td align="right">24.7%</td>
<td align="right">64</td>
<td align="right">24.8%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21</td>
<td align="right">7.3%</td>
<td align="right">16</td>
<td align="right">6.2%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">49</td>
<td align="right">17.1%</td>
<td align="right">46</td>
<td align="right">17.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">53</td>
<td align="right">18.5%</td>
<td align="right">46</td>
<td align="right">17.8%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">59</td>
<td align="right">20.6%</td>
<td align="right">56</td>
<td align="right">21.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">19</td>
<td align="right">6.6%</td>
<td align="right">16</td>
<td align="right">6.2%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">15</td>
<td align="right">5.2%</td>
<td align="right">14</td>
<td align="right">5.4%</td>
<td align="right">-6.7%</td>
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
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">90</td>
<td align="right">31.4%</td>
<td align="right">80</td>
<td align="right">31.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">101</td>
<td align="right">35.2%</td>
<td align="right">91</td>
<td align="right">35.3%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">29</td>
<td align="right">10.1%</td>
<td align="right">26</td>
<td align="right">10.1%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">31</td>
<td align="right">10.8%</td>
<td align="right">31</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">34</td>
<td align="right">11.8%</td>
<td align="right">30</td>
<td align="right">11.6%</td>
<td align="right">-11.8%</td>
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
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">824,637</td>
<td align="right">1,029</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,394,447</td>
<td align="right">155,216</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,267,506</td>
<td align="right">1,014,597</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,620,657</td>
<td align="right">1,362,618</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">583,305</td>
<td align="right">155,323</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">579,186</td>
<td align="right">155,323</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,746,115</td>
<td align="right">2,874,649</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,746,115</td>
<td align="right">2,874,649</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,656,746</td>
<td align="right">756,793</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">811,253</td>
<td align="right">403,567</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">11,166,851</td>
<td align="right">5,684,930</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,806,683</td>
<td align="right">10,503,879</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,226,915</td>
<td align="right">780,675</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,835,660</td>
<td align="right">13,984,059</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,430,855</td>
<td align="right">961,959</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">46,069,019</td>
<td align="right">32,581,133</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">22,675,319</td>
<td align="right">16,281,963</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">23,319,648</td>
<td align="right">16,900,062</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,202,091</td>
<td align="right">1,616,067</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">4,387,872</td>
<td align="right">3,259,342</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,325,727</td>
<td align="right">1,729,526</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">58,044,506</td>
<td align="right">43,951,592</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,404,807</td>
<td align="right">1,844,676</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">10,526,759</td>
<td align="right">8,445,958</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,367,569</td>
<td align="right">5,122,710</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">18,797,889</td>
<td align="right">15,170,027</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,907,552</td>
<td align="right">3,157,883</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,741,316</td>
<td align="right">3,045,749</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,963,860</td>
<td align="right">2,461,013</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,963,860</td>
<td align="right">2,461,013</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,449,681</td>
<td align="right">2,868,900</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">6,578,829</td>
<td align="right">5,611,518</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,000,249</td>
<td align="right">7,869,806</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">203,058</td>
<td align="right">180,402</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">203,058</td>
<td align="right">180,402</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">850,824</td>
<td align="right">760,962</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">431,835</td>
<td align="right">386,676</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">431,835</td>
<td align="right">386,676</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">660,612</td>
<td align="right">592,950</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">660,623</td>
<td align="right">592,960</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">660,623</td>
<td align="right">592,960</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">233,628</td>
<td align="right">210,738</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,618,571</td>
<td align="right">1,460,120</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,151,661</td>
<td align="right">1,038,972</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">13,968,577</td>
<td align="right">12,602,823</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">638,320</td>
<td align="right">576,391</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">400,277</td>
<td align="right">361,597</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,588,368</td>
<td align="right">2,339,843</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,281,647</td>
<td align="right">2,062,799</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">3,546,519</td>
<td align="right">3,211,774</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">171,389</td>
<td align="right">155,216</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">3,312,968</td>
<td align="right">3,001,117</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">582,932</td>
<td align="right">528,205</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,063,020</td>
<td align="right">963,539</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,263,237</td>
<td align="right">2,051,871</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">240,043</td>
<td align="right">217,666</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">720,131</td>
<td align="right">653,000</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,601,322</td>
<td align="right">1,453,708</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,757,548</td>
<td align="right">2,505,732</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">847,904</td>
<td align="right">773,160</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,130,034</td>
<td align="right">5,591,959</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">4,738,815</td>
<td align="right">4,333,200</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,738,815</td>
<td align="right">4,333,200</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,155,883</td>
<td align="right">3,804,995</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">7,198,332</td>
<td align="right">6,592,595</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,644,276</td>
<td align="right">8,839,644</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">3,194,102</td>
<td align="right">2,932,239</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,120,687</td>
<td align="right">2,867,718</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">5,817,589</td>
<td align="right">5,346,645</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">4,969,685</td>
<td align="right">4,573,485</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,555,065</td>
<td align="right">1,438,523</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,077,294</td>
<td align="right">1,922,598</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,281,767</td>
<td align="right">1,193,608</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,664,953</td>
<td align="right">2,483,107</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">127,773</td>
<td align="right">120,159</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,192,716</td>
<td align="right">8,654,014</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">954,515</td>
<td align="right">899,509</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">11,765,042</td>
<td align="right">11,159,305</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,634,065</td>
<td align="right">1,553,108</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,904,690</td>
<td align="right">7,513,225</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,904,690</td>
<td align="right">7,513,225</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,537,709</td>
<td align="right">1,466,530</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,415,860</td>
<td align="right">3,263,752</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,771,392</td>
<td align="right">2,655,584</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">644,329</td>
<td align="right">618,099</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">647,565</td>
<td align="right">621,335</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">614,913</td>
<td align="right">592,258</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">614,913</td>
<td align="right">592,258</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">706,959</td>
<td align="right">683,169</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">706,959</td>
<td align="right">683,169</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">583,215</td>
<td align="right">567,048</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,765,232</td>
<td align="right">1,724,038</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">531,177</td>
<td align="right">519,710</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">531,177</td>
<td align="right">519,710</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">531,177</td>
<td align="right">519,710</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,635,008</td>
<td align="right">5,567,346</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,962,198</td>
<td align="right">5,904,221</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,404</td>
<td align="right">399,551</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,404</td>
<td align="right">399,551</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,404</td>
<td align="right">399,551</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,601,911</td>
<td align="right">2,585,738</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,566,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">411,805</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">107</td>
<td align="right">107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right"></td>
<td align="right">1,122</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-04
