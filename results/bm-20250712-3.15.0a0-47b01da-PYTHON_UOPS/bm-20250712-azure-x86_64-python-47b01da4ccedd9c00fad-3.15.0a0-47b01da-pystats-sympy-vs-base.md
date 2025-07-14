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
<td align="right">139,110,661</td>
<td align="right">3,433,705</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">15,937,971</td>
<td align="right">2,930,568</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,309,132</td>
<td align="right">6,022,578</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">37,360,752</td>
<td align="right">18,622,527</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">50,208,180</td>
<td align="right">25,182,377</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,228,602</td>
<td align="right">2,984,632</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,715,735</td>
<td align="right">16,099,815</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">82,779,302</td>
<td align="right">48,899,222</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,243,016</td>
<td align="right">3,780,551</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,553,520</td>
<td align="right">2,775,383</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,997,125</td>
<td align="right">11,596,303</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,462,760</td>
<td align="right">56,916,089</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">84,023,302</td>
<td align="right">58,477,317</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,443,115</td>
<td align="right">13,467,921</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">82,932,259</td>
<td align="right">60,852,860</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">116,491,446</td>
<td align="right">90,410,173</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,902,770</td>
<td align="right">21,927,670</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">71,475,083</td>
<td align="right">61,238,103</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">48,255,986</td>
<td align="right">41,394,409</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">73,102,842</td>
<td align="right">63,427,419</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">45,201,268</td>
<td align="right">39,364,095</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,379,553</td>
<td align="right">11,738,969</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">278,963,160</td>
<td align="right">246,484,339</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">11,423,884</td>
<td align="right">10,139,871</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,450,160</td>
<td align="right">10,166,122</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">196,528,098</td>
<td align="right">176,464,688</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">13,400,184</td>
<td align="right">12,137,932</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,920,559</td>
<td align="right">16,529,810</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">17,171,067</td>
<td align="right">15,864,184</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">699,597,557</td>
<td align="right">647,747,959</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">41,012,751</td>
<td align="right">38,079,517</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">36,271,532</td>
<td align="right">33,692,363</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">54,077,584</td>
<td align="right">50,284,800</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,579,087</td>
<td align="right">21,936,725</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">15,703,664</td>
<td align="right">14,900,165</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">18,969,292</td>
<td align="right">18,009,774</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">73,055,551</td>
<td align="right">69,382,057</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">238,933,677</td>
<td align="right">227,169,653</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">27,204,817</td>
<td align="right">25,933,487</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">45,287,562</td>
<td align="right">43,188,397</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">47,765,555</td>
<td align="right">46,049,425</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">154,161,003</td>
<td align="right">148,775,716</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">46,467,368</td>
<td align="right">44,880,504</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,776,681</td>
<td align="right">35,529,260</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,229,721</td>
<td align="right">44,924,511</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">187,380,326</td>
<td align="right">182,111,323</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,021,131</td>
<td align="right">1,969,186</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">46,957,714</td>
<td align="right">45,766,149</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">54,460,211</td>
<td align="right">53,106,712</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">9,880,841</td>
<td align="right">9,672,591</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,565,735</td>
<td align="right">18,198,421</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">63,282,136</td>
<td align="right">62,360,837</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,130,878</td>
<td align="right">11,975,545</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,667,174</td>
<td align="right">15,495,702</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,667,939</td>
<td align="right">2,639,996</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">493,896</td>
<td align="right">488,794</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">156,324,668</td>
<td align="right">154,845,435</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">24,211,755</td>
<td align="right">24,001,347</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,475,240</td>
<td align="right">10,393,698</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,019,957</td>
<td align="right">9,949,891</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,661,407</td>
<td align="right">4,634,681</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">16,256,163</td>
<td align="right">16,184,686</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">11,740,199</td>
<td align="right">11,693,247</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">76,213,664</td>
<td align="right">75,927,722</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">51,136,796</td>
<td align="right">50,950,906</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,913,562</td>
<td align="right">6,890,177</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,617,232</td>
<td align="right">12,577,631</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,690,170</td>
<td align="right">30,596,717</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,142,612</td>
<td align="right">8,121,001</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,307,831</td>
<td align="right">8,286,266</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,400,137</td>
<td align="right">7,382,405</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">55,002,173</td>
<td align="right">54,877,124</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">34,857,818</td>
<td align="right">34,786,446</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">40,001</td>
<td align="right">40,074</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">183,864</td>
<td align="right">184,177</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,097,460</td>
<td align="right">6,087,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,456,404</td>
<td align="right">1,454,542</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,637,745</td>
<td align="right">18,620,070</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">58,621</td>
<td align="right">58,676</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,338,226</td>
<td align="right">22,357,798</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">25,319,604</td>
<td align="right">25,298,146</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,730</td>
<td align="right">20,747</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">770,653</td>
<td align="right">771,145</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">166,852</td>
<td align="right">166,946</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">18,659,402</td>
<td align="right">18,651,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">19,619,589</td>
<td align="right">19,612,009</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">206,048,568</td>
<td align="right">205,973,023</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">187,813,764</td>
<td align="right">187,745,767</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">50,128</td>
<td align="right">50,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,291,172</td>
<td align="right">1,291,572</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">191,279</td>
<td align="right">191,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">98,282</td>
<td align="right">98,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,234,048</td>
<td align="right">1,234,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">386,516</td>
<td align="right">386,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,260,825</td>
<td align="right">7,261,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,276,335</td>
<td align="right">6,277,118</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,257,102</td>
<td align="right">2,257,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">272,859</td>
<td align="right">272,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,096,149</td>
<td align="right">5,096,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,737,338</td>
<td align="right">1,737,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,361,023</td>
<td align="right">7,361,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,080,583</td>
<td align="right">1,080,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,082,401</td>
<td align="right">1,082,495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,781,850</td>
<td align="right">18,780,319</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">736,359</td>
<td align="right">736,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">736,703</td>
<td align="right">736,757</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,885,600</td>
<td align="right">4,885,944</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">214,767</td>
<td align="right">214,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,595,666</td>
<td align="right">4,595,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">143,093</td>
<td align="right">143,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,989</td>
<td align="right">164,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">81,369,811</td>
<td align="right">81,365,630</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,855</td>
<td align="right">2,195,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,795,782</td>
<td align="right">7,796,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,861,730</td>
<td align="right">11,862,195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,987,145</td>
<td align="right">2,987,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">89,520</td>
<td align="right">89,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">3,087,901</td>
<td align="right">3,088,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">444,276</td>
<td align="right">444,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">431,878</td>
<td align="right">431,867</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,203,613</td>
<td align="right">4,203,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">743,265</td>
<td align="right">743,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">743,265</td>
<td align="right">743,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">743,265</td>
<td align="right">743,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">22,224,798</td>
<td align="right">22,225,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,136,285</td>
<td align="right">2,136,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">932,325</td>
<td align="right">932,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">848,545</td>
<td align="right">848,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,762,600</td>
<td align="right">2,762,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,866,520</td>
<td align="right">7,866,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">7,254,257</td>
<td align="right">7,254,210</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22,505,961</td>
<td align="right">22,506,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">743,810</td>
<td align="right">743,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,025,614</td>
<td align="right">10,025,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">945,838</td>
<td align="right">945,834</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,249,616</td>
<td align="right">1,249,621</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,825,617</td>
<td align="right">1,825,612</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,477,379</td>
<td align="right">1,477,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,028,007</td>
<td align="right">1,028,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">464,739</td>
<td align="right">464,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">440,463</td>
<td align="right">440,463</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">241,236</td>
<td align="right">241,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">241,194</td>
<td align="right">241,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">202,050</td>
<td align="right">202,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">187,761</td>
<td align="right">187,761</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">184,485</td>
<td align="right">184,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">120,324</td>
<td align="right">120,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">90,471</td>
<td align="right">90,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">87,150</td>
<td align="right">87,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">25,599</td>
<td align="right">25,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">15,684</td>
<td align="right">15,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,448</td>
<td align="right">13,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">6,993</td>
<td align="right">6,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,466</td>
<td align="right">5,466</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">2,103</td>
<td align="right">2,103</td>
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
<td align="right">1,264</td>
<td align="right">1,264</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">63,778,391</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">28,019,445</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">515,338</td>
<td align="right"></td>
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
<td align="right">46,874,956</td>
<td align="right">38.6%</td>
<td align="right">45,683,590</td>
<td align="right">38.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">74,081,674</td>
<td align="right">61.0%</td>
<td align="right">73,499,961</td>
<td align="right">61.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">475,954</td>
<td align="right">0.4%</td>
<td align="right">475,994</td>
<td align="right">0.4%</td>
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
<td align="right">66,587</td>
<td align="right">72.8%</td>
<td align="right">66,353</td>
<td align="right">72.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,840</td>
<td align="right">27.2%</td>
<td align="right">24,877</td>
<td align="right">27.3%</td>
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
<td align="left">true divide float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,159</td>
<td align="right">9.2%</td>
<td align="right">5,991</td>
<td align="right">9.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,415</td>
<td align="right">3.6%</td>
<td align="right">2,373</td>
<td align="right">3.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">358</td>
<td align="right">0.5%</td>
<td align="right">360</td>
<td align="right">0.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">197</td>
<td align="right">0.3%</td>
<td align="right">196</td>
<td align="right">0.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,948</td>
<td align="right">11.9%</td>
<td align="right">7,916</td>
<td align="right">11.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,249</td>
<td align="right">1.9%</td>
<td align="right">1,253</td>
<td align="right">1.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">4,882</td>
<td align="right">7.3%</td>
<td align="right">4,870</td>
<td align="right">7.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,933</td>
<td align="right">4.4%</td>
<td align="right">2,940</td>
<td align="right">4.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,174</td>
<td align="right">1.8%</td>
<td align="right">1,172</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,735</td>
<td align="right">5.6%</td>
<td align="right">3,739</td>
<td align="right">5.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,921</td>
<td align="right">2.9%</td>
<td align="right">1,923</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">2,062</td>
<td align="right">3.1%</td>
<td align="right">2,063</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,153</td>
<td align="right">3.2%</td>
<td align="right">2,152</td>
<td align="right">3.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4,044</td>
<td align="right">6.1%</td>
<td align="right">4,045</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,429</td>
<td align="right">14.2%</td>
<td align="right">9,431</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,261</td>
<td align="right">9.4%</td>
<td align="right">6,261</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,822</td>
<td align="right">5.7%</td>
<td align="right">3,822</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">3,173</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">2,355</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">294</td>
<td align="right">0.4%</td>
<td align="right">294</td>
<td align="right">0.4%</td>
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
<td align="right">90,471</td>
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
<td align="right">286,023,291</td>
<td align="right">88.4%</td>
<td align="right">276,034,948</td>
<td align="right">88.1%</td>
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
<td align="right">37,173,382</td>
<td align="right">11.5%</td>
<td align="right">37,164,986</td>
<td align="right">11.9%</td>
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
<td align="right">36,648,060</td>
<td align="right">11.3%</td>
<td align="right">36,639,871</td>
<td align="right">11.7%</td>
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
<td align="right">798,181</td>
<td align="right">100.0%</td>
<td align="right">798,005</td>
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
<td align="right">11,350</td>
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
<td align="right">5,084</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">52,874,062</td>
<td align="right">62.9%</td>
<td align="right">49,941,286</td>
<td align="right">61.7%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,616,619</td>
<td align="right">36.4%</td>
<td align="right">30,523,265</td>
<td align="right">37.7%</td>
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
<td align="right">432,297</td>
<td align="right">0.5%</td>
<td align="right">432,293</td>
<td align="right">0.5%</td>
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
<td align="right">63,662</td>
<td align="right">78.1%</td>
<td align="right">63,561</td>
<td align="right">78.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">17,888</td>
<td align="right">21.9%</td>
<td align="right">17,888</td>
<td align="right">22.0%</td>
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
<td align="left">bool</td>
<td align="right">1,781</td>
<td align="right">2.8%</td>
<td align="right">1,763</td>
<td align="right">2.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">293</td>
<td align="right">0.5%</td>
<td align="right">291</td>
<td align="right">0.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">15,882</td>
<td align="right">24.9%</td>
<td align="right">15,803</td>
<td align="right">24.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,004</td>
<td align="right">15.7%</td>
<td align="right">10,000</td>
<td align="right">15.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,084</td>
<td align="right">19.0%</td>
<td align="right">12,087</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,420</td>
<td align="right">22.7%</td>
<td align="right">14,419</td>
<td align="right">22.7%</td>
<td align="right">-0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,522,975</td>
<td align="right">56.7%</td>
<td align="right">6,236,436</td>
<td align="right">35.0%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,981,536</td>
<td align="right">43.3%</td>
<td align="right">11,582,298</td>
<td align="right">64.9%</td>
<td align="right">-35.6%</td>
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
<td align="right">14,224</td>
<td align="right">91.2%</td>
<td align="right">12,640</td>
<td align="right">90.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365</td>
<td align="right">8.8%</td>
<td align="right">1,365</td>
<td align="right">9.7%</td>
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
<td align="right">7,147</td>
<td align="right">50.2%</td>
<td align="right">5,564</td>
<td align="right">44.0%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,523</td>
<td align="right">38.8%</td>
<td align="right">5,522</td>
<td align="right">43.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,197</td>
<td align="right">8.4%</td>
<td align="right">1,197</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">357</td>
<td align="right">2.5%</td>
<td align="right">357</td>
<td align="right">2.8%</td>
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
<td align="right">82,678,655</td>
<td align="right">43.5%</td>
<td align="right">48,808,376</td>
<td align="right">40.9%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">106,175,591</td>
<td align="right">55.8%</td>
<td align="right">69,346,506</td>
<td align="right">58.0%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,248,754</td>
<td align="right">0.7%</td>
<td align="right">1,220,286</td>
<td align="right">1.0%</td>
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
<td align="right">86,572</td>
<td align="right">69.8%</td>
<td align="right">76,758</td>
<td align="right">67.5%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,513</td>
<td align="right">30.2%</td>
<td align="right">36,992</td>
<td align="right">32.5%</td>
<td align="right">-1.4%</td>
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
<td align="left">zip</td>
<td align="right">6,637</td>
<td align="right">7.7%</td>
<td align="right">5,196</td>
<td align="right">6.8%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">58,595</td>
<td align="right">67.7%</td>
<td align="right">50,249</td>
<td align="right">65.5%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,603</td>
<td align="right">8.8%</td>
<td align="right">7,576</td>
<td align="right">9.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,305</td>
<td align="right">5.0%</td>
<td align="right">4,305</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,773</td>
<td align="right">3.2%</td>
<td align="right">2,773</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,828</td>
<td align="right">2.1%</td>
<td align="right">1,828</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,618</td>
<td align="right">1.9%</td>
<td align="right">1,618</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,344</td>
<td align="right">1.6%</td>
<td align="right">1,344</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">903</td>
<td align="right">1.0%</td>
<td align="right">903</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">714</td>
<td align="right">0.8%</td>
<td align="right">714</td>
<td align="right">0.9%</td>
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
<td align="left">set</td>
<td align="right">7,372,167</td>
<td align="right">7,372,167 / 0 !!</td>
<td align="right">7,340,184</td>
<td align="right">7,340,184 / 0 !!</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">166,037</td>
<td align="right">166,037 / 0 !!</td>
<td align="right">166,072</td>
<td align="right">166,072 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">72,742</td>
<td align="right">72,742 / 0 !!</td>
<td align="right">72,737</td>
<td align="right">72,737 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,946,140</td>
<td align="right">8,946,140 / 0 !!</td>
<td align="right">8,946,589</td>
<td align="right">8,946,589 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,175,767</td>
<td align="right">9,175,767 / 0 !!</td>
<td align="right">9,175,708</td>
<td align="right">9,175,708 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,563,398</td>
<td align="right">9,563,398 / 0 !!</td>
<td align="right">9,563,338</td>
<td align="right">9,563,338 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,459,011</td>
<td align="right">12,459,011 / 0 !!</td>
<td align="right">12,459,061</td>
<td align="right">12,459,061 / 0 !!</td>
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
<td align="right">71,248,765</td>
<td align="right">20.1%</td>
<td align="right">61,014,307</td>
<td align="right">18.8%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">229,395,703</td>
<td align="right">64.7%</td>
<td align="right">210,419,933</td>
<td align="right">64.8%</td>
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
<td align="right">53,452,353</td>
<td align="right">15.1%</td>
<td align="right">52,926,841</td>
<td align="right">16.3%</td>
<td align="right">-1.0%</td>
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
<td align="right">127,488</td>
<td align="right">10.4%</td>
<td align="right">124,971</td>
<td align="right">10.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,095,193</td>
<td align="right">89.6%</td>
<td align="right">1,085,299</td>
<td align="right">89.7%</td>
<td align="right">-0.9%</td>
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
<td align="right">1,218</td>
<td align="right">1.0%</td>
<td align="right">903</td>
<td align="right">0.7%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">10,736</td>
<td align="right">8.4%</td>
<td align="right">9,534</td>
<td align="right">7.6%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,706</td>
<td align="right">3.7%</td>
<td align="right">4,391</td>
<td align="right">3.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">15,150</td>
<td align="right">11.9%</td>
<td align="right">14,856</td>
<td align="right">11.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,705</td>
<td align="right">48.4%</td>
<td align="right">61,308</td>
<td align="right">49.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,878</td>
<td align="right">7.0%</td>
<td align="right">8,884</td>
<td align="right">7.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,571</td>
<td align="right">5.9%</td>
<td align="right">7,568</td>
<td align="right">6.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">12,347</td>
<td align="right">9.7%</td>
<td align="right">12,351</td>
<td align="right">9.9%</td>
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
<td align="right">303,850,310</td>
<td align="right">99.9%</td>
<td align="right">272,500,034</td>
<td align="right">99.9%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">94,741</td>
<td align="right">0.0%</td>
<td align="right">94,796</td>
<td align="right">0.0%</td>
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
<td align="right">21,462</td>
<td align="right">0.0%</td>
<td align="right">21,462</td>
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
<td align="right">96,706</td>
<td align="right">100.0%</td>
<td align="right">96,691</td>
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
<td align="right">2,409,704</td>
<td align="right">99.9%</td>
<td align="right">2,409,722</td>
<td align="right">99.9%</td>
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
<td align="right">634</td>
<td align="right">0.0%</td>
<td align="right">634</td>
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
<td align="right">821,124</td>
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
<td align="right">1,822,644</td>
<td align="right">17.0%</td>
<td align="right">1,822,081</td>
<td align="right">17.0%</td>
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
<td align="right">8,525,524</td>
<td align="right">79.4%</td>
<td align="right">8,526,875</td>
<td align="right">79.4%</td>
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
<td align="right">377,497</td>
<td align="right">3.5%</td>
<td align="right">377,541</td>
<td align="right">3.5%</td>
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
<td align="right">3,643</td>
<td align="right">8.4%</td>
<td align="right">3,653</td>
<td align="right">8.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,678</td>
<td align="right">91.6%</td>
<td align="right">39,663</td>
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
<td align="right">1,396</td>
<td align="right">38.3%</td>
<td align="right">1,406</td>
<td align="right">38.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,953</td>
<td align="right">53.6%</td>
<td align="right">1,953</td>
<td align="right">53.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">462</td>
<td align="right">12.7%</td>
<td align="right">462</td>
<td align="right">12.6%</td>
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
<td align="right">2,103</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,081,780</td>
<td align="right">86.7%</td>
<td align="right">18,010,298</td>
<td align="right">86.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,756,230</td>
<td align="right">13.2%</td>
<td align="right">2,756,261</td>
<td align="right">13.3%</td>
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
<td align="right">2,860</td>
<td align="right">44.9%</td>
<td align="right">2,858</td>
<td align="right">44.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,510</td>
<td align="right">55.1%</td>
<td align="right">3,510</td>
<td align="right">55.1%</td>
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
<td align="right">3,510</td>
<td align="right">100.0%</td>
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
<td align="right">174,060,652</td>
<td align="right">94.2%</td>
<td align="right">168,504,168</td>
<td align="right">94.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">668,237</td>
<td align="right">0.4%</td>
<td align="right">668,487</td>
<td align="right">0.4%</td>
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
<td align="right">9,941,250</td>
<td align="right">5.4%</td>
<td align="right">9,941,188</td>
<td align="right">5.5%</td>
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
<td align="right">27,179</td>
<td align="right">28.4%</td>
<td align="right">27,189</td>
<td align="right">28.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,640</td>
<td align="right">71.6%</td>
<td align="right">68,647</td>
<td align="right">71.6%</td>
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
<td align="right">3,081</td>
<td align="right">11.3%</td>
<td align="right">3,111</td>
<td align="right">11.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,391</td>
<td align="right">5.1%</td>
<td align="right">1,395</td>
<td align="right">5.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,359</td>
<td align="right">12.4%</td>
<td align="right">3,368</td>
<td align="right">12.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">13,531</td>
<td align="right">49.8%</td>
<td align="right">13,498</td>
<td align="right">49.6%</td>
<td align="right">-0.2%</td>
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
<td align="left">dict</td>
<td align="right">2,352</td>
<td align="right">8.7%</td>
<td align="right">2,352</td>
<td align="right">8.7%</td>
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
<td align="right">83,897,025</td>
<td align="right">100.0%</td>
<td align="right">58,350,763</td>
<td align="right">99.9%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,319</td>
<td align="right">0.0%</td>
<td align="right">27,386</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
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
<td align="right">751</td>
<td align="right">5.9%</td>
<td align="right">753</td>
<td align="right">5.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,931</td>
<td align="right">94.1%</td>
<td align="right">11,935</td>
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
<td align="right">688</td>
<td align="right">91.6%</td>
<td align="right">690</td>
<td align="right">91.6%</td>
<td align="right">0.3%</td>
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
<td align="right">311,829,945</td>
<td align="right">6.3%</td>
<td align="right">258,311,094</td>
<td align="right">5.8%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,697,627,999</td>
<td align="right">34.4%</td>
<td align="right">1,475,358,489</td>
<td align="right">33.1%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,835,606,880</td>
<td align="right">57.4%</td>
<td align="right">2,626,237,552</td>
<td align="right">59.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">95,326,416</td>
<td align="right">1.9%</td>
<td align="right">94,763,765</td>
<td align="right">2.1%</td>
<td align="right">-0.6%</td>
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
<td align="right">82,678,655</td>
<td align="right">27.6%</td>
<td align="right">48,808,376</td>
<td align="right">19.7%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,981,536</td>
<td align="right">6.0%</td>
<td align="right">11,582,298</td>
<td align="right">4.7%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">71,248,765</td>
<td align="right">23.8%</td>
<td align="right">61,014,307</td>
<td align="right">24.6%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">46,874,956</td>
<td align="right">15.6%</td>
<td align="right">45,683,590</td>
<td align="right">18.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,616,619</td>
<td align="right">10.2%</td>
<td align="right">30,523,265</td>
<td align="right">12.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,648,060</td>
<td align="right">12.2%</td>
<td align="right">36,639,871</td>
<td align="right">14.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">377,497</td>
<td align="right">0.1%</td>
<td align="right">377,541</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,756,230</td>
<td align="right">0.9%</td>
<td align="right">2,756,261</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,941,250</td>
<td align="right">3.3%</td>
<td align="right">9,941,188</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">375,973</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,379,380</td>
<td align="right">14.0%</td>
<td align="right">12,934,187</td>
<td align="right">13.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,287,801</td>
<td align="right">3.4%</td>
<td align="right">3,301,384</td>
<td align="right">3.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,952,864</td>
<td align="right">30.4%</td>
<td align="right">28,860,331</td>
<td align="right">30.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,656,310</td>
<td align="right">12.2%</td>
<td align="right">11,648,330</td>
<td align="right">12.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,821,858</td>
<td align="right">1.9%</td>
<td align="right">1,821,295</td>
<td align="right">1.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,314,271</td>
<td align="right">7.7%</td>
<td align="right">7,315,070</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,184,678</td>
<td align="right">6.5%</td>
<td align="right">6,184,394</td>
<td align="right">6.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,905,455</td>
<td align="right">12.5%</td>
<td align="right">11,905,154</td>
<td align="right">12.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,164,123</td>
<td align="right">5.4%</td>
<td align="right">5,164,149</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,105,458</td>
<td align="right">2.2%</td>
<td align="right">2,105,463</td>
<td align="right">2.2%</td>
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
<td align="right">136,014,741</td>
<td align="right">62.5%</td>
<td align="right">135,921,896</td>
<td align="right">62.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">193,786,341</td>
<td align="right">89.1%</td>
<td align="right">193,696,731</td>
<td align="right">89.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">42,029,119</td>
<td align="right">19.3%</td>
<td align="right">42,024,124</td>
<td align="right">19.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">77,480,292</td>
<td align="right">35.6%</td>
<td align="right">77,475,905</td>
<td align="right">35.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">77,487,810</td>
<td align="right">35.6%</td>
<td align="right">77,483,423</td>
<td align="right">35.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">4,046,305</td>
<td align="right">1.9%</td>
<td align="right">4,046,513</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">81,534,115</td>
<td align="right">37.5%</td>
<td align="right">81,529,936</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">81,534,115</td>
<td align="right">37.5%</td>
<td align="right">81,529,936</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,047,506</td>
<td align="right">0.5%</td>
<td align="right">1,047,476</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,923,600</td>
<td align="right">8.7%</td>
<td align="right">18,923,920</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,359,156</td>
<td align="right">4.3%</td>
<td align="right">9,359,262</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
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
<td align="right">1,525,807</td>
<td align="right"></td>
<td align="right">2,244,603</td>
<td align="right"></td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,904,715</td>
<td align="right"></td>
<td align="right">3,539,118</td>
<td align="right"></td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,426,963</td>
<td align="right"></td>
<td align="right">5,779,960</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,315,968,721</td>
<td align="right">37.2%</td>
<td align="right">1,303,467,553</td>
<td align="right">36.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,641,653,724</td>
<td align="right">43.1%</td>
<td align="right">1,628,983,290</td>
<td align="right">42.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">23,463</td>
<td align="right">0.0%</td>
<td align="right">23,547</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">255,625,544</td>
<td align="right"></td>
<td align="right">254,840,214</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">53,758,776</td>
<td align="right">1.4%</td>
<td align="right">53,624,297</td>
<td align="right">1.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">851,142</td>
<td align="right">0.2%</td>
<td align="right">853,016</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,005,190,710</td>
<td align="right">28.4%</td>
<td align="right">1,003,469,653</td>
<td align="right">28.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">869,681,836</td>
<td align="right">22.8%</td>
<td align="right">868,675,034</td>
<td align="right">22.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">154,177,742</td>
<td align="right"></td>
<td align="right">154,017,608</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">83,405,926</td>
<td align="right">2.4%</td>
<td align="right">83,357,878</td>
<td align="right">2.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">134,717,090</td>
<td align="right">27.1%</td>
<td align="right">134,643,959</td>
<td align="right">27.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">135,591,695</td>
<td align="right">27.3%</td>
<td align="right">135,520,522</td>
<td align="right">27.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">146,103,786</td>
<td align="right"></td>
<td align="right">146,029,093</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,241,772,769</td>
<td align="right">32.6%</td>
<td align="right">1,242,018,998</td>
<td align="right">32.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,137,562,096</td>
<td align="right">32.1%</td>
<td align="right">1,137,762,039</td>
<td align="right">32.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">361,406,291</td>
<td align="right">72.7%</td>
<td align="right">361,359,417</td>
<td align="right">72.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">361,659,763</td>
<td align="right"></td>
<td align="right">361,612,890</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,186,611</td>
<td align="right"></td>
<td align="right">1,186,712</td>
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
Stats gathered on: 2025-07-14
