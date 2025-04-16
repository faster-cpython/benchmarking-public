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
<td align="left">JUMP_BACKWARD</td>
<td align="right">112</td>
<td align="right">102</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">559,902</td>
<td align="right">537,731</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">7,768,757</td>
<td align="right">7,465,686</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,693,910</td>
<td align="right">5,472,182</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,140,820</td>
<td align="right">1,096,481</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,093,320</td>
<td align="right">2,012,029</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,338,292</td>
<td align="right">1,286,548</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,724,994</td>
<td align="right">1,658,498</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">383,771</td>
<td align="right">369,013</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,121,566</td>
<td align="right">2,040,275</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,943,222</td>
<td align="right">1,869,373</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,751,088</td>
<td align="right">1,684,592</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,159,383</td>
<td align="right">2,078,092</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">392,084</td>
<td align="right">377,326</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,960,907</td>
<td align="right">1,887,481</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">812,145</td>
<td align="right">782,592</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">616,665</td>
<td align="right">594,236</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">206,653</td>
<td align="right">199,141</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">407,254</td>
<td align="right">392,462</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">609,724</td>
<td align="right">587,593</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">407,574</td>
<td align="right">392,782</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">614,091</td>
<td align="right">591,946</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">213,545</td>
<td align="right">206,169</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">642,215</td>
<td align="right">620,041</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,786,535</td>
<td align="right">8,491,600</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,515,762</td>
<td align="right">9,197,918</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">222,137</td>
<td align="right">214,758</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,493,537</td>
<td align="right">2,411,893</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">224,547</td>
<td align="right">217,219</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,451,291</td>
<td align="right">13,016,468</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">228,053</td>
<td align="right">220,685</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,689,029</td>
<td align="right">17,120,144</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,590,764</td>
<td align="right">2,509,536</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,781,458</td>
<td align="right">12,389,449</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,216,207</td>
<td align="right">15,722,558</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,251,958</td>
<td align="right">8,000,923</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,738,288</td>
<td align="right">1,686,544</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,781,598</td>
<td align="right">3,670,743</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,762,230</td>
<td align="right">4,623,212</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,055,424</td>
<td align="right">4,908,056</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,800,033</td>
<td align="right">1,747,936</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,382,353</td>
<td align="right">4,256,933</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,219,692</td>
<td align="right">5,071,961</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">84,294,256</td>
<td align="right">81,911,626</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,320</td>
<td align="right">5,470</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,426,943</td>
<td align="right">3,330,960</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,610,086</td>
<td align="right">1,565,798</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,993,862</td>
<td align="right">2,913,374</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,841,630</td>
<td align="right">3,738,540</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,279,347</td>
<td align="right">26,571,490</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,434,114</td>
<td align="right">3,345,715</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">9,305,599</td>
<td align="right">9,070,235</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">897,614</td>
<td align="right">875,492</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,749,057</td>
<td align="right">6,586,626</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,031,467</td>
<td align="right">16,627,265</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">994,755</td>
<td align="right">972,595</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,488,035</td>
<td align="right">26,875,773</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,723,456</td>
<td align="right">9,509,726</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">32,295,517</td>
<td align="right">31,587,660</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,038,460</td>
<td align="right">1,016,301</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,364,715</td>
<td align="right">1,335,683</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">348,945</td>
<td align="right">341,579</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,772,666</td>
<td align="right">5,655,862</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,473,362</td>
<td align="right">1,443,837</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20,345,274</td>
<td align="right">19,948,211</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,319,426</td>
<td align="right">19,930,072</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,692,340</td>
<td align="right">8,537,237</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,282,269</td>
<td align="right">8,134,537</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,687,599</td>
<td align="right">1,658,052</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,540,218</td>
<td align="right">3,481,146</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,717,072</td>
<td align="right">3,657,952</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,886,407</td>
<td align="right">9,732,190</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,572,286</td>
<td align="right">8,446,651</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,882,952</td>
<td align="right">1,860,824</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,267,515</td>
<td align="right">1,252,763</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,563</td>
<td align="right">4,615</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,717</td>
<td align="right">13,867</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">712,441</td>
<td align="right">705,568</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,359,995</td>
<td align="right">7,293,523</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">343</td>
<td align="right">346</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,940</td>
<td align="right">18,090</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,940</td>
<td align="right">18,090</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,225</td>
<td align="right">3,251</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">14,260,564</td>
<td align="right">14,156,975</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,101,194</td>
<td align="right">1,093,811</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,359,620</td>
<td align="right">3,344,868</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,611</td>
<td align="right">1,608</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,649</td>
<td align="right">102,805</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">605,020</td>
<td align="right">605,331</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,472</td>
<td align="right">21,465</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,907</td>
<td align="right">517,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,134</td>
<td align="right">35,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,380</td>
<td align="right">97,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,041</td>
<td align="right">34,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,677</td>
<td align="right">81,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,014</td>
<td align="right">191,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,814</td>
<td align="right">928,823</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,692</td>
<td align="right">1,818,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,258</td>
<td align="right">856,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,674</td>
<td align="right">857,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,656</td>
<td align="right">940,655</td>
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
<td align="right">4,724,457</td>
<td align="right">4,724,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,683</td>
<td align="right">462,683</td>
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
<td align="right">87,313</td>
<td align="right">87,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,720</td>
<td align="right">84,720</td>
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
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
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
<td align="right">42,905</td>
<td align="right">42,905</td>
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
<td align="right">783</td>
<td align="right">783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">491</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">484</td>
<td align="right">484</td>
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
<td align="right">246,894</td>
<td align="right">2.2%</td>
<td align="right">236,969</td>
<td align="right">2.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,320,981</td>
<td align="right">93.1%</td>
<td align="right">9,968,796</td>
<td align="right">93.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">515,850</td>
<td align="right">4.7%</td>
<td align="right">516,000</td>
<td align="right">4.8%</td>
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
<td align="right">4,916</td>
<td align="right">86.1%</td>
<td align="right">4,726</td>
<td align="right">85.5%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">795</td>
<td align="right">13.9%</td>
<td align="right">804</td>
<td align="right">14.5%</td>
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
<td align="left">subscr deque</td>
<td align="right">86</td>
<td align="right">10.8%</td>
<td align="right">89</td>
<td align="right">11.1%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">289</td>
<td align="right">36.4%</td>
<td align="right">295</td>
<td align="right">36.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.5%</td>
<td align="right">187</td>
<td align="right">23.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">164</td>
<td align="right">20.6%</td>
<td align="right">164</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.3%</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
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
<td align="right">23,972,253</td>
<td align="right">100.0%</td>
<td align="right">23,294,162</td>
<td align="right">100.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,016</td>
<td align="right">0.0%</td>
<td align="right">2,003</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">787</td>
<td align="right">0.0%</td>
<td align="right">787</td>
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
<td align="right">3,334</td>
<td align="right">100.0%</td>
<td align="right">3,399</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="right">188,293</td>
<td align="right">3.7%</td>
<td align="right">180,893</td>
<td align="right">3.6%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">612,387</td>
<td align="right">11.9%</td>
<td align="right">590,100</td>
<td align="right">11.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,347,042</td>
<td align="right">84.4%</td>
<td align="right">4,258,660</td>
<td align="right">84.6%</td>
<td align="right">-2.0%</td>
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
<td align="right">4,008</td>
<td align="right">51.3%</td>
<td align="right">3,859</td>
<td align="right">51.2%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,809</td>
<td align="right">48.7%</td>
<td align="right">3,676</td>
<td align="right">48.8%</td>
<td align="right">-3.5%</td>
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
<td align="right">3,721</td>
<td align="right">92.8%</td>
<td align="right">3,566</td>
<td align="right">92.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">148</td>
<td align="right">3.7%</td>
<td align="right">154</td>
<td align="right">4.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">2.4%</td>
<td align="right">95</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">1.1%</td>
<td align="right">44</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,738,679</td>
<td align="right">100.0%</td>
<td align="right">1,686,935</td>
<td align="right">100.0%</td>
<td align="right">-3.0%</td>
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
<td align="right">13,977,982</td>
<td align="right">93.7%</td>
<td align="right">13,800,734</td>
<td align="right">93.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">940,117</td>
<td align="right">6.3%</td>
<td align="right">940,117</td>
<td align="right">6.4%</td>
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
<td align="right">51</td>
<td align="right">9.5%</td>
<td align="right">50</td>
<td align="right">9.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.5%</td>
<td align="right">488</td>
<td align="right">90.7%</td>
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
<td align="right">9,504,055</td>
<td align="right">18.7%</td>
<td align="right">9,186,271</td>
<td align="right">18.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,991,992</td>
<td align="right">80.5%</td>
<td align="right">39,983,154</td>
<td align="right">80.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">398,562</td>
<td align="right">0.8%</td>
<td align="right">399,415</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
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
<td align="right">7,190</td>
<td align="right">37.9%</td>
<td align="right">7,050</td>
<td align="right">37.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,756</td>
<td align="right">62.1%</td>
<td align="right">11,847</td>
<td align="right">62.7%</td>
<td align="right">0.8%</td>
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
<td align="right">843</td>
<td align="right">11.7%</td>
<td align="right">783</td>
<td align="right">11.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,787</td>
<td align="right">24.9%</td>
<td align="right">1,723</td>
<td align="right">24.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,704</td>
<td align="right">23.7%</td>
<td align="right">1,694</td>
<td align="right">24.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">9.5%</td>
<td align="right">682</td>
<td align="right">9.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.4%</td>
<td align="right">460</td>
<td align="right">6.5%</td>
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
<td align="right">0.9%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.6%</td>
<td align="right">45</td>
<td align="right">0.6%</td>
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
<td align="right">25,940,749</td>
<td align="right">100.0%</td>
<td align="right">25,120,829</td>
<td align="right">100.0%</td>
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
<td align="right">856</td>
<td align="right">0.0%</td>
<td align="right">850</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">238</td>
<td align="right">0.0%</td>
<td align="right">238</td>
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
<td align="right">2,375</td>
<td align="right">100.0%</td>
<td align="right">2,407</td>
<td align="right">100.0%</td>
<td align="right">1.3%</td>
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
<td align="right">2,117,120</td>
<td align="right">100.0%</td>
<td align="right">2,035,829</td>
<td align="right">100.0%</td>
<td align="right">-3.8%</td>
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
<td align="right">5,069,695</td>
<td align="right">95.4%</td>
<td align="right">4,921,964</td>
<td align="right">95.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,943</td>
<td align="right">1.5%</td>
<td align="right">79,939</td>
<td align="right">1.5%</td>
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
<td align="right">160,377</td>
<td align="right">3.0%</td>
<td align="right">160,377</td>
<td align="right">3.1%</td>
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
<td align="right">3,994</td>
<td align="right">84.3%</td>
<td align="right">3,991</td>
<td align="right">84.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">744</td>
<td align="right">15.7%</td>
<td align="right">744</td>
<td align="right">15.7%</td>
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
<td align="right">808</td>
<td align="right">108.6%</td>
<td align="right">811</td>
<td align="right">109.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">344</td>
<td align="right">46.2%</td>
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
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">11</td>
<td align="right">1.5%</td>
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
<td align="right">1,800,033</td>
<td align="right">98.8%</td>
<td align="right">1,747,936</td>
<td align="right">98.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,265</td>
<td align="right">1.2%</td>
<td align="right">21,261</td>
<td align="right">1.2%</td>
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
<td align="right">20</td>
<td align="right">9.7%</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.3%</td>
<td align="right">187</td>
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
<td align="right">11,809,854</td>
<td align="right">94.3%</td>
<td align="right">11,404,773</td>
<td align="right">94.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">711,099</td>
<td align="right">5.7%</td>
<td align="right">704,231</td>
<td align="right">5.8%</td>
<td align="right">-1.0%</td>
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
<td align="right">886</td>
<td align="right">66.0%</td>
<td align="right">876</td>
<td align="right">65.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">456</td>
<td align="right">34.0%</td>
<td align="right">461</td>
<td align="right">34.5%</td>
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
<td align="left">mapping</td>
<td align="right">338</td>
<td align="right">38.1%</td>
<td align="right">327</td>
<td align="right">37.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">139</td>
<td align="right">15.7%</td>
<td align="right">140</td>
<td align="right">16.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.2%</td>
<td align="right">232</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.5%</td>
<td align="right">111</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">2,125,189</td>
<td align="right">100.0%</td>
<td align="right">2,110,440</td>
<td align="right">100.0%</td>
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
<td align="right">12,428,220</td>
<td align="right">2.3%</td>
<td align="right">15,412,253</td>
<td align="right">3.0%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">299,432,172</td>
<td align="right">56.0%</td>
<td align="right">289,007,008</td>
<td align="right">55.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">222,085,476</td>
<td align="right">41.5%</td>
<td align="right">216,631,880</td>
<td align="right">41.5%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">995,180</td>
<td align="right">0.2%</td>
<td align="right">978,708</td>
<td align="right">0.2%</td>
<td align="right">-1.7%</td>
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
<td align="right">612,387</td>
<td align="right">4.9%</td>
<td align="right">590,100</td>
<td align="right">4.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,504,055</td>
<td align="right">76.6%</td>
<td align="right">9,186,271</td>
<td align="right">76.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">711,099</td>
<td align="right">5.7%</td>
<td align="right">704,231</td>
<td align="right">5.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">856</td>
<td align="right">0.0%</td>
<td align="right">850</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,016</td>
<td align="right">0.0%</td>
<td align="right">2,003</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,850</td>
<td align="right">4.2%</td>
<td align="right">516,000</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,265</td>
<td align="right">0.2%</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,943</td>
<td align="right">0.6%</td>
<td align="right">79,939</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,117</td>
<td align="right">7.6%</td>
<td align="right">940,117</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
<td align="right">14,139</td>
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
<td align="right">123,373</td>
<td align="right">12.4%</td>
<td align="right">118,391</td>
<td align="right">12.1%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">123,521</td>
<td align="right">12.4%</td>
<td align="right">118,578</td>
<td align="right">12.1%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">188,292</td>
<td align="right">18.9%</td>
<td align="right">180,892</td>
<td align="right">18.5%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">338,820</td>
<td align="right">34.0%</td>
<td align="right">339,677</td>
<td align="right">34.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,698</td>
<td align="right">5.0%</td>
<td align="right">49,694</td>
<td align="right">5.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">16.1%</td>
<td align="right">160,377</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.0%</td>
<td align="right">9,895</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">397</td>
<td align="right">0.0%</td>
<td align="right">397</td>
<td align="right">0.0%</td>
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
<td align="right">152</td>
<td align="right">0.0%</td>
<td align="right">152</td>
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
<td align="right">510,577</td>
<td align="right">1.6%</td>
<td align="right">495,780</td>
<td align="right">1.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">27,283,580</td>
<td align="right">84.4%</td>
<td align="right">26,575,723</td>
<td align="right">84.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,732,194</td>
<td align="right">73.5%</td>
<td align="right">23,149,972</td>
<td align="right">73.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,149,211</td>
<td align="right">25.2%</td>
<td align="right">8,023,576</td>
<td align="right">25.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,149,269</td>
<td align="right">25.2%</td>
<td align="right">8,023,634</td>
<td align="right">25.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,576,644</td>
<td align="right">26.5%</td>
<td align="right">8,451,009</td>
<td align="right">26.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,576,644</td>
<td align="right">26.5%</td>
<td align="right">8,451,009</td>
<td align="right">26.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,954</td>
<td align="right">0.1%</td>
<td align="right">18,104</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.3%</td>
<td align="right">427,375</td>
<td align="right">1.4%</td>
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
<td align="right">1.4%</td>
<td align="right">456,471</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.4%</td>
<td align="right">441,508</td>
<td align="right">1.4%</td>
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
<td align="right">21,278</td>
<td align="right"></td>
<td align="right">8,210</td>
<td align="right"></td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">83,322</td>
<td align="right"></td>
<td align="right">36,189</td>
<td align="right"></td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">62,318</td>
<td align="right"></td>
<td align="right">28,215</td>
<td align="right"></td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,672,268</td>
<td align="right"></td>
<td align="right">1,613,174</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">11,603,693</td>
<td align="right"></td>
<td align="right">11,246,853</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,796,893</td>
<td align="right">19.7%</td>
<td align="right">54,233,048</td>
<td align="right">19.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">52,413,128</td>
<td align="right">20.9%</td>
<td align="right">50,973,943</td>
<td align="right">20.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">65,110,271</td>
<td align="right">26.0%</td>
<td align="right">63,405,194</td>
<td align="right">25.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,244,293</td>
<td align="right">66.5%</td>
<td align="right">25,589,167</td>
<td align="right">66.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,246,150</td>
<td align="right"></td>
<td align="right">25,591,396</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">6,971,839</td>
<td align="right">2.8%</td>
<td align="right">6,801,512</td>
<td align="right">2.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">73,162,680</td>
<td align="right">25.8%</td>
<td align="right">71,403,223</td>
<td align="right">25.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">153,582,546</td>
<td align="right">54.1%</td>
<td align="right">150,008,681</td>
<td align="right">54.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,724,628</td>
<td align="right"></td>
<td align="right">11,456,942</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">126,057,644</td>
<td align="right">50.3%</td>
<td align="right">123,225,887</td>
<td align="right">50.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,362,356</td>
<td align="right">0.5%</td>
<td align="right">1,332,813</td>
<td align="right">0.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,612,067</td>
<td align="right"></td>
<td align="right">14,322,622</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,081,332</td>
<td align="right">33.2%</td>
<td align="right">12,843,979</td>
<td align="right">33.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,202,428</td>
<td align="right">33.5%</td>
<td align="right">12,965,051</td>
<td align="right">33.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,565</td>
<td align="right">0.2%</td>
<td align="right">77,545</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,531</td>
<td align="right">0.1%</td>
<td align="right">43,527</td>
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">9,524</td>
<td align="right">730</td>
<td align="right">646</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">9,524</td>
<td align="right">730</td>
<td align="right">646</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-16
