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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">422,063</td>
<td align="right">364,367</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">596,872</td>
<td align="right">515,959</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">865,153</td>
<td align="right">749,735</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">291,733</td>
<td align="right">253,111</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">878,164</td>
<td align="right">764,474</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">300,046</td>
<td align="right">261,424</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,183,772</td>
<td align="right">1,034,836</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,373,318</td>
<td align="right">1,203,661</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">158,399</td>
<td align="right">138,922</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">471,689</td>
<td align="right">413,704</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,212,018</td>
<td align="right">1,063,082</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">628,290</td>
<td align="right">551,282</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">476,026</td>
<td align="right">418,094</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">315,434</td>
<td align="right">277,049</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">315,754</td>
<td align="right">277,369</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,249,835</td>
<td align="right">1,100,899</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">612,591</td>
<td align="right">540,688</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,084,159</td>
<td align="right">2,725,294</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">503,495</td>
<td align="right">445,774</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">4,113,652</td>
<td align="right">3,661,559</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">178,339</td>
<td align="right">158,763</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">176,118</td>
<td align="right">156,807</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">182,053</td>
<td align="right">162,715</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,127,893</td>
<td align="right">1,009,127</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,157,171</td>
<td align="right">1,036,230</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,732,019</td>
<td align="right">6,064,627</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,900,747</td>
<td align="right">3,515,600</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,812,828</td>
<td align="right">5,239,231</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,049,031</td>
<td align="right">947,680</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,039,773</td>
<td align="right">939,993</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,199,472</td>
<td align="right">8,322,432</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">9,268,887</td>
<td align="right">8,416,317</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,409,845</td>
<td align="right">10,378,468</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,862,711</td>
<td align="right">2,607,048</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,482,165</td>
<td align="right">3,177,323</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,102,666</td>
<td align="right">2,831,135</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,577,301</td>
<td align="right">9,656,325</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,334,098</td>
<td align="right">1,218,299</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,476,776</td>
<td align="right">5,010,114</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,344,280</td>
<td align="right">1,230,756</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">57,670,372</td>
<td align="right">52,853,330</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,337,912</td>
<td align="right">4,913,800</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,326,547</td>
<td align="right">20,560,875</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">753,528</td>
<td align="right">693,982</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,409,793</td>
<td align="right">2,222,416</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,911,815</td>
<td align="right">6,385,684</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,586,045</td>
<td align="right">1,466,520</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,793,776</td>
<td align="right">2,586,848</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,922,201</td>
<td align="right">13,829,318</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,502,846</td>
<td align="right">2,323,946</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,100,183</td>
<td align="right">1,023,150</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">90,698</td>
<td align="right">96,883</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,314,185</td>
<td align="right">2,157,765</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">856,935</td>
<td align="right">799,212</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,179,986</td>
<td align="right">1,102,380</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">302,958</td>
<td align="right">283,596</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,373,950</td>
<td align="right">2,233,447</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,938,767</td>
<td align="right">24,412,089</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">14,416,693</td>
<td align="right">13,600,658</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">16,980,135</td>
<td align="right">16,027,637</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,805,686</td>
<td align="right">18,737,493</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,383,169</td>
<td align="right">6,052,092</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,697,728</td>
<td align="right">3,506,919</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,172,562</td>
<td align="right">3,018,442</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">682,693</td>
<td align="right">650,167</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,540,181</td>
<td align="right">6,247,840</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,791,168</td>
<td align="right">7,464,109</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">378,783</td>
<td align="right">394,193</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,272,633</td>
<td align="right">3,144,209</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,267,773</td>
<td align="right">6,139,570</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">98</td>
<td align="right">100</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,721,906</td>
<td align="right">5,608,809</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,055,170</td>
<td align="right">1,035,858</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,079</td>
<td align="right">4,994</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,678,266</td>
<td align="right">5,599,814</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,514,340</td>
<td align="right">1,532,882</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,098,589</td>
<td align="right">1,085,424</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">588,720</td>
<td align="right">594,642</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,476</td>
<td align="right">13,391</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,667,206</td>
<td align="right">11,602,046</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">360</td>
<td align="right">358</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,383,560</td>
<td align="right">2,370,395</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,699</td>
<td align="right">17,614</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,699</td>
<td align="right">17,614</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,555</td>
<td align="right">4,568</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,225</td>
<td align="right">3,232</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">468</td>
<td align="right">467</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">8,309</td>
<td align="right">8,322</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,430</td>
<td align="right">102,293</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,424</td>
<td align="right">97,320</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">204,853</td>
<td align="right">204,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,682</td>
<td align="right">516,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,849</td>
<td align="right">928,769</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,069</td>
<td align="right">35,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,052</td>
<td align="right">34,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">454,118</td>
<td align="right">454,092</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,548</td>
<td align="right">456,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,709</td>
<td align="right">1,818,682</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,022</td>
<td align="right">191,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,629</td>
<td align="right">939,628</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,280</td>
<td align="right">5,068,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,575</td>
<td align="right">4,723,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,671</td>
<td align="right">426,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,140</td>
<td align="right">105,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,431</td>
<td align="right">86,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,720</td>
<td align="right">84,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,671</td>
<td align="right">81,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,356</td>
<td align="right">77,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,588</td>
<td align="right">67,588</td>
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
<td align="right">59,114</td>
<td align="right">59,114</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,863</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,859</td>
<td align="right">55,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,010</td>
<td align="right">44,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,252</td>
<td align="right">31,252</td>
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
<td align="right">29,557</td>
<td align="right">29,557</td>
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
<td align="right">21,908</td>
<td align="right">21,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,464</td>
<td align="right">21,464</td>
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
<td align="right">17,809</td>
<td align="right">17,809</td>
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
<td align="right">14,139</td>
<td align="right">14,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,837</td>
<td align="right">12,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,380</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,488</td>
<td align="right">8,488</td>
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
<td align="right">784</td>
<td align="right">784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">504</td>
<td align="right">504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">491</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">391</td>
<td align="right">391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">207</td>
<td align="right">207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">181</td>
<td align="right">181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">153</td>
<td align="right">153</td>
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
<td align="right">27</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,169</td>
<td align="right">0.2%</td>
<td align="right">23,489</td>
<td align="right">0.3%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,293,440</td>
<td align="right">93.9%</td>
<td align="right">7,345,034</td>
<td align="right">93.2%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">515,615</td>
<td align="right">5.8%</td>
<td align="right">515,528</td>
<td align="right">6.5%</td>
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
<td align="right">607</td>
<td align="right">42.9%</td>
<td align="right">711</td>
<td align="right">46.7%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">808</td>
<td align="right">57.1%</td>
<td align="right">811</td>
<td align="right">53.3%</td>
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
<td align="left">remainder</td>
<td align="right">295</td>
<td align="right">36.5%</td>
<td align="right">298</td>
<td align="right">36.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.1%</td>
<td align="right">187</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">164</td>
<td align="right">20.3%</td>
<td align="right">164</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">87</td>
<td align="right">10.8%</td>
<td align="right">87</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">66</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">14,139</td>
<td align="right">100.0%</td>
<td align="right">14,139</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,741,293</td>
<td align="right">100.0%</td>
<td align="right">17,967,860</td>
<td align="right">100.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,992</td>
<td align="right">0.0%</td>
<td align="right">1,998</td>
<td align="right">0.0%</td>
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
<td align="right">823</td>
<td align="right">0.0%</td>
<td align="right">823</td>
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
<td align="right">3,386</td>
<td align="right">100.0%</td>
<td align="right">3,393</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">42</td>
<td align="right">23.2%</td>
<td align="right">42</td>
<td align="right">23.2%</td>
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
<td align="right">139</td>
<td align="right">100.0%</td>
<td align="right">139</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">17,931</td>
<td align="right">0.4%</td>
<td align="right">22,006</td>
<td align="right">0.5%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">595,694</td>
<td align="right">13.5%</td>
<td align="right">514,663</td>
<td align="right">12.5%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,795,393</td>
<td align="right">86.1%</td>
<td align="right">3,564,353</td>
<td align="right">86.9%</td>
<td align="right">-6.1%</td>
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
<td align="right">911</td>
<td align="right">60.5%</td>
<td align="right">1,031</td>
<td align="right">60.5%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">595</td>
<td align="right">39.5%</td>
<td align="right">673</td>
<td align="right">39.5%</td>
<td align="right">13.1%</td>
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
<td align="right">616</td>
<td align="right">67.6%</td>
<td align="right">733</td>
<td align="right">71.1%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">154</td>
<td align="right">16.9%</td>
<td align="right">157</td>
<td align="right">15.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">10.5%</td>
<td align="right">96</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">45</td>
<td align="right">4.9%</td>
<td align="right">45</td>
<td align="right">4.4%</td>
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
<td align="right">1,417,087</td>
<td align="right">100.0%</td>
<td align="right">1,282,478</td>
<td align="right">100.0%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">264</td>
<td align="right">0.0%</td>
<td align="right">264</td>
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
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">84.3%</td>
<td align="right">43</td>
<td align="right">84.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,415,350</td>
<td align="right">92.4%</td>
<td align="right">11,229,215</td>
<td align="right">92.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">939,088</td>
<td align="right">7.6%</td>
<td align="right">939,088</td>
<td align="right">7.7%</td>
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
<td align="right">53</td>
<td align="right">9.8%</td>
<td align="right">52</td>
<td align="right">9.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.2%</td>
<td align="right">488</td>
<td align="right">90.4%</td>
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
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="left">list</td>
<td align="right">1,892,096</td>
<td align="right">1,892,096 / 0 !!</td>
<td align="right">1,699,382</td>
<td align="right">1,699,382 / 0 !!</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">894,178</td>
<td align="right">894,178 / 0 !!</td>
<td align="right">836,219</td>
<td align="right">836,219 / 0 !!</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
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
<td align="right">33,912,451</td>
<td align="right">82.6%</td>
<td align="right">29,430,829</td>
<td align="right">82.0%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,720,900</td>
<td align="right">16.4%</td>
<td align="right">6,053,491</td>
<td align="right">16.9%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,019</td>
<td align="right">1.0%</td>
<td align="right">396,361</td>
<td align="right">1.1%</td>
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
<td align="right">6,549</td>
<td align="right">35.8%</td>
<td align="right">6,566</td>
<td align="right">35.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,744</td>
<td align="right">64.2%</td>
<td align="right">11,737</td>
<td align="right">64.1%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">795</td>
<td align="right">12.1%</td>
<td align="right">843</td>
<td align="right">12.8%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,418</td>
<td align="right">21.7%</td>
<td align="right">1,373</td>
<td align="right">20.9%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">10.4%</td>
<td align="right">683</td>
<td align="right">10.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,582</td>
<td align="right">24.2%</td>
<td align="right">1,585</td>
<td align="right">24.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.1%</td>
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
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
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
<td align="right">16,886,393</td>
<td align="right">100.0%</td>
<td align="right">15,388,354</td>
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
<td align="right">828</td>
<td align="right">0.0%</td>
<td align="right">829</td>
<td align="right">0.0%</td>
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
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">228</td>
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
<td align="right">2,403</td>
<td align="right">100.0%</td>
<td align="right">2,409</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">1,611,681</td>
<td align="right">100.0%</td>
<td align="right">1,400,039</td>
<td align="right">100.0%</td>
<td align="right">-13.1%</td>
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
<td align="right">4,150,464</td>
<td align="right">94.5%</td>
<td align="right">3,765,299</td>
<td align="right">94.0%</td>
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
<td align="right">79,939</td>
<td align="right">1.8%</td>
<td align="right">79,939</td>
<td align="right">2.0%</td>
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
<td align="right">160,377</td>
<td align="right">3.7%</td>
<td align="right">160,377</td>
<td align="right">4.0%</td>
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
<td align="right">3,990</td>
<td align="right">84.2%</td>
<td align="right">3,990</td>
<td align="right">84.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">746</td>
<td align="right">15.8%</td>
<td align="right">746</td>
<td align="right">15.8%</td>
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
<td align="right">747</td>
<td align="right">100.1%</td>
<td align="right">762</td>
<td align="right">102.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.1%</td>
<td align="right">344</td>
<td align="right">46.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.6%</td>
<td align="right">206</td>
<td align="right">27.6%</td>
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
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.3%</td>
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
<td align="right">1,478,980</td>
<td align="right">98.6%</td>
<td align="right">1,344,555</td>
<td align="right">98.4%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,261</td>
<td align="right">1.4%</td>
<td align="right">21,261</td>
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
<td align="left">Success</td>
<td align="right">16</td>
<td align="right">7.9%</td>
<td align="right">16</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">92.1%</td>
<td align="right">187</td>
<td align="right">92.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,875,746</td>
<td align="right">93.8%</td>
<td align="right">7,878,374</td>
<td align="right">93.0%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">587,399</td>
<td align="right">6.2%</td>
<td align="right">593,302</td>
<td align="right">7.0%</td>
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
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">31</td>
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
<td align="right">857</td>
<td align="right">64.8%</td>
<td align="right">876</td>
<td align="right">65.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">465</td>
<td align="right">35.2%</td>
<td align="right">465</td>
<td align="right">34.7%</td>
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
<td align="left">mapping</td>
<td align="right">306</td>
<td align="right">35.7%</td>
<td align="right">322</td>
<td align="right">36.8%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">142</td>
<td align="right">16.6%</td>
<td align="right">145</td>
<td align="right">16.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">27.1%</td>
<td align="right">232</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">13.0%</td>
<td align="right">111</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">2,033,184</td>
<td align="right">100.0%</td>
<td align="right">1,994,484</td>
<td align="right">100.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">12,002,535</td>
<td align="right">3.1%</td>
<td align="right">11,081,187</td>
<td align="right">3.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">145,699,091</td>
<td align="right">37.2%</td>
<td align="right">136,138,775</td>
<td align="right">37.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">232,871,356</td>
<td align="right">59.5%</td>
<td align="right">217,605,950</td>
<td align="right">59.5%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">594,579</td>
<td align="right">0.2%</td>
<td align="right">603,315</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">595,694</td>
<td align="right">6.3%</td>
<td align="right">514,663</td>
<td align="right">5.9%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,720,900</td>
<td align="right">70.9%</td>
<td align="right">6,053,491</td>
<td align="right">69.3%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">587,399</td>
<td align="right">6.2%</td>
<td align="right">593,302</td>
<td align="right">6.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,992</td>
<td align="right">0.0%</td>
<td align="right">1,998</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">828</td>
<td align="right">0.0%</td>
<td align="right">829</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,615</td>
<td align="right">5.4%</td>
<td align="right">515,528</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,088</td>
<td align="right">9.9%</td>
<td align="right">939,088</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,939</td>
<td align="right">0.8%</td>
<td align="right">79,939</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
<td align="right">14,139</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">9,206</td>
<td align="right">1.5%</td>
<td align="right">11,963</td>
<td align="right">2.0%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">8,963</td>
<td align="right">1.5%</td>
<td align="right">11,526</td>
<td align="right">1.9%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">17,930</td>
<td align="right">3.0%</td>
<td align="right">22,005</td>
<td align="right">3.6%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">337,481</td>
<td align="right">56.8%</td>
<td align="right">336,828</td>
<td align="right">55.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,494</td>
<td align="right">8.3%</td>
<td align="right">49,489</td>
<td align="right">8.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">27.0%</td>
<td align="right">160,377</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">397</td>
<td align="right">0.1%</td>
<td align="right">397</td>
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
<td align="right">142</td>
<td align="right">0.0%</td>
<td align="right">142</td>
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
<td align="right">418,745</td>
<td align="right">1.5%</td>
<td align="right">380,361</td>
<td align="right">1.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">22,869,580</td>
<td align="right">82.0%</td>
<td align="right">21,020,304</td>
<td align="right">80.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">20,099,312</td>
<td align="right">72.1%</td>
<td align="right">18,577,095</td>
<td align="right">71.3%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,368,093</td>
<td align="right">26.4%</td>
<td align="right">7,041,034</td>
<td align="right">27.0%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,368,151</td>
<td align="right">26.4%</td>
<td align="right">7,041,092</td>
<td align="right">27.0%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,795,526</td>
<td align="right">27.9%</td>
<td align="right">7,468,467</td>
<td align="right">28.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,795,526</td>
<td align="right">27.9%</td>
<td align="right">7,468,467</td>
<td align="right">28.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,713</td>
<td align="right">0.1%</td>
<td align="right">17,628</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.5%</td>
<td align="right">427,375</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
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
<td align="right">1.6%</td>
<td align="right">456,471</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.6%</td>
<td align="right">441,508</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">4,902</td>
<td align="right"></td>
<td align="right">6,807</td>
<td align="right"></td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">35,518</td>
<td align="right"></td>
<td align="right">21,719</td>
<td align="right"></td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">40,089</td>
<td align="right"></td>
<td align="right">28,212</td>
<td align="right"></td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,304,574</td>
<td align="right"></td>
<td align="right">1,150,508</td>
<td align="right"></td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,192,648</td>
<td align="right"></td>
<td align="right">8,186,019</td>
<td align="right"></td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">778,802</td>
<td align="right">0.3%</td>
<td align="right">701,784</td>
<td align="right">0.3%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">67,668,935</td>
<td align="right">31.9%</td>
<td align="right">61,828,722</td>
<td align="right">31.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">46,729,076</td>
<td align="right">19.4%</td>
<td align="right">42,775,864</td>
<td align="right">19.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">44,262,860</td>
<td align="right">20.9%</td>
<td align="right">40,617,637</td>
<td align="right">20.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">71,339,130</td>
<td align="right">29.6%</td>
<td align="right">65,728,159</td>
<td align="right">29.5%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,380,290</td>
<td align="right">2.5%</td>
<td align="right">4,958,916</td>
<td align="right">2.5%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,152,618</td>
<td align="right"></td>
<td align="right">20,438,031</td>
<td align="right"></td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,150,786</td>
<td align="right">65.4%</td>
<td align="right">20,436,355</td>
<td align="right">64.8%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,572,604</td>
<td align="right"></td>
<td align="right">8,839,340</td>
<td align="right"></td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">121,812,922</td>
<td align="right">50.6%</td>
<td align="right">113,599,624</td>
<td align="right">51.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">94,869,946</td>
<td align="right">44.7%</td>
<td align="right">88,966,221</td>
<td align="right">45.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,825,884</td>
<td align="right"></td>
<td align="right">12,074,664</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,616,541</td>
<td align="right">34.3%</td>
<td align="right">11,000,126</td>
<td align="right">34.9%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,737,743</td>
<td align="right">34.6%</td>
<td align="right">11,121,325</td>
<td align="right">35.2%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,620</td>
<td align="right">0.2%</td>
<td align="right">77,618</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,582</td>
<td align="right">0.1%</td>
<td align="right">43,581</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.1%</td>
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
<td align="right">2</td>
<td align="right">560</td>
<td align="right">22,433</td>
<td align="right">1,504</td>
<td align="right">1,341</td>
<td align="right">2</td>
<td align="right">560</td>
<td align="right">22,433</td>
<td align="right">1,504</td>
<td align="right">1,341</td>
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
<td align="right">11</td>
<td align="right">0.4%</td>
<td align="right">15</td>
<td align="right">0.5%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,990,073</td>
<td align="right"></td>
<td align="right">1,688,306</td>
<td align="right"></td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">156,404,885</td>
<td align="right">7,859.3%</td>
<td align="right">135,800,081</td>
<td align="right">8,043.6%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">80</td>
<td align="right">2.6%</td>
<td align="right">77</td>
<td align="right">2.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,491</td>
<td align="right">48.6%</td>
<td align="right">1,450</td>
<td align="right">48.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,071</td>
<td align="right"></td>
<td align="right">2,993</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,394</td>
<td align="right">45.4%</td>
<td align="right">1,360</td>
<td align="right">45.4%</td>
<td align="right">-2.4%</td>
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

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">106</td>
<td align="right">3.5%</td>
<td align="right">106</td>
<td align="right">3.5%</td>
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
<td align="right">80</td>
<td align="right"></td>
<td align="right">77</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">77</td>
<td align="right">100.0%</td>
<td align="right">-3.8%</td>
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
<td align="right">45,680</td>
<td align="right">2.1%</td>
<td align="right">47,280</td>
<td align="right">2.1%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">1,960,149</td>
<td align="right">88.6%</td>
<td align="right">2,022,973</td>
<td align="right">88.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,211,840</td>
<td align="right"></td>
<td align="right">2,277,376</td>
<td align="right"></td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">206,011</td>
<td align="right">9.3%</td>
<td align="right">207,123</td>
<td align="right">9.1%</td>
<td align="right">0.5%</td>
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
<td align="left"><= 8,192</td>
<td align="left">12</td>
<td align="right">15.0%</td>
<td align="left">10</td>
<td align="right">13.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">23</td>
<td align="right">28.7%</td>
<td align="left">23</td>
<td align="right">29.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">23</td>
<td align="right">28.7%</td>
<td align="left">18</td>
<td align="right">23.4%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">22</td>
<td align="right">27.5%</td>
<td align="left">26</td>
<td align="right">33.8%</td>
<td align="right">18.2%</td>
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
<td align="right">12</td>
<td align="right">15.0%</td>
<td align="right">10</td>
<td align="right">13.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21</td>
<td align="right">26.2%</td>
<td align="right">21</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2</td>
<td align="right">2.5%</td>
<td align="right">2</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">23</td>
<td align="right">28.7%</td>
<td align="right">18</td>
<td align="right">23.4%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">22</td>
<td align="right">27.5%</td>
<td align="right">26</td>
<td align="right">33.8%</td>
<td align="right">18.2%</td>
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
<td align="left"><= 32</td>
<td align="right">12</td>
<td align="right">15.0%</td>
<td align="right">10</td>
<td align="right">13.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">27.5%</td>
<td align="right">22</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13</td>
<td align="right">16.2%</td>
<td align="right">11</td>
<td align="right">14.3%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22</td>
<td align="right">27.5%</td>
<td align="right">19</td>
<td align="right">24.7%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">11</td>
<td align="right">13.8%</td>
<td align="right">15</td>
<td align="right">19.5%</td>
<td align="right">36.4%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">404,109</td>
<td align="right">1,278,766</td>
<td align="right">216.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,538,658</td>
<td align="right">341,403</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,337,297</td>
<td align="right">399,696</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,134,549</td>
<td align="right">341,403</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">76,839</td>
<td align="right">51,317</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">76,839</td>
<td align="right">51,317</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">76,839</td>
<td align="right">51,317</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">230,588</td>
<td align="right">154,035</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">153,749</td>
<td align="right">102,718</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">76,910</td>
<td align="right">51,401</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">614,779</td>
<td align="right">471,074</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">326,330</td>
<td align="right">254,557</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">326,330</td>
<td align="right">254,557</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">326,330</td>
<td align="right">254,557</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">211,610</td>
<td align="right">165,200</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">557,858</td>
<td align="right">444,121</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">461,030</td>
<td align="right">368,356</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">807,269</td>
<td align="right">647,271</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">1,769,222</td>
<td align="right">1,432,783</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">1,894,028</td>
<td align="right">1,534,475</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,459,200</td>
<td align="right">1,182,784</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,459,200</td>
<td align="right">1,182,784</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,422,998</td>
<td align="right">1,153,880</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,422,998</td>
<td align="right">1,153,880</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">845,207</td>
<td align="right">685,383</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">124,807</td>
<td align="right">101,692</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">730,440</td>
<td align="right">595,960</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">730,439</td>
<td align="right">595,960</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">481,019</td>
<td align="right">392,804</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,847,204</td>
<td align="right">3,360,777</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,987,566</td>
<td align="right">3,271,508</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,231,367</td>
<td align="right">1,013,122</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">384,177</td>
<td align="right">317,027</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,134,549</td>
<td align="right">937,363</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">885,119</td>
<td align="right">734,201</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,942,767</td>
<td align="right">1,620,169</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,942,767</td>
<td align="right">1,620,169</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,942,767</td>
<td align="right">1,620,169</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,942,767</td>
<td align="right">1,620,169</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,471,667</td>
<td align="right">2,063,252</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,586,610</td>
<td align="right">1,329,129</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">404,109</td>
<td align="right">341,403</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">942,918</td>
<td align="right">796,605</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">538,800</td>
<td align="right">455,196</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">134,700</td>
<td align="right">113,799</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">134,700</td>
<td align="right">113,799</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">135,582</td>
<td align="right">114,681</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,990,073</td>
<td align="right">1,688,306</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,865,266</td>
<td align="right">1,586,614</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,746,581</td>
<td align="right">2,361,262</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,749,976</td>
<td align="right">1,506,365</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,379,632</td>
<td align="right">1,198,889</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">2,525,369</td>
<td align="right">2,202,683</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">28,549,843</td>
<td align="right">24,972,974</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">25,163,864</td>
<td align="right">22,127,780</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,160,261</td>
<td align="right">1,021,512</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,480,656</td>
<td align="right">2,197,666</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">822,863</td>
<td align="right">730,012</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,010,378</td>
<td align="right">2,674,041</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">860,744</td>
<td align="right">768,052</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,220,005</td>
<td align="right">1,094,599</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">726,044</td>
<td align="right">654,253</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,209,456</td>
<td align="right">3,796,312</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">921,670</td>
<td align="right">831,406</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">921,670</td>
<td align="right">831,406</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">783,891</td>
<td align="right">716,723</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,483,977</td>
<td align="right">4,140,374</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,463,280</td>
<td align="right">3,256,923</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,463,280</td>
<td align="right">3,256,923</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">480,477</td>
<td align="right">454,968</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">488,658</td>
<td align="right">463,134</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">535,296</td>
<td align="right">514,377</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">538,532</td>
<td align="right">517,613</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">538,532</td>
<td align="right">517,613</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,102,912</td>
<td align="right">2,077,390</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,507,361</td>
<td align="right">2,481,839</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,714</td>
<td align="right">399,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,134,549</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">633,654</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,714</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">288,449</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">76,839</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
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
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
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
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right"></td>
<td align="right">1,756,732</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">216,517</td>
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
<td align="right">107</td>
<td align="right">107</td>
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
Stats gathered on: 2025-05-21
