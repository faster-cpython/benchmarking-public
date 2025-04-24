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
<td align="right">462,294</td>
<td align="right">563,711</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">945,604</td>
<td align="right">1,148,407</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">650,080</td>
<td align="right">787,787</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">959,421</td>
<td align="right">1,161,624</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">318,849</td>
<td align="right">385,905</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,292,980</td>
<td align="right">1,561,197</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">327,162</td>
<td align="right">394,218</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,321,226</td>
<td align="right">1,589,443</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">668,021</td>
<td align="right">801,323</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">342,107</td>
<td align="right">409,995</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">342,427</td>
<td align="right">410,315</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,021,311</td>
<td align="right">1,223,487</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">682,077</td>
<td align="right">817,035</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,359,043</td>
<td align="right">1,627,260</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">512,341</td>
<td align="right">612,865</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">171,838</td>
<td align="right">205,384</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">516,701</td>
<td align="right">617,288</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,383,903</td>
<td align="right">4,024,338</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">543,728</td>
<td align="right">645,124</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">4,522,666</td>
<td align="right">5,328,897</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">189,676</td>
<td align="right">223,204</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,840,954</td>
<td align="right">6,860,601</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,236,974</td>
<td align="right">1,451,598</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,037,049</td>
<td align="right">10,593,686</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,841,501</td>
<td align="right">8,019,849</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">195,599</td>
<td align="right">229,094</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">192,315</td>
<td align="right">224,968</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,657,914</td>
<td align="right">3,109,009</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,266,294</td>
<td align="right">1,480,755</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,062,084</td>
<td align="right">11,706,017</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,169,879</td>
<td align="right">4,844,380</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,135,673</td>
<td align="right">1,317,382</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">9,474,047</td>
<td align="right">10,988,119</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,775,081</td>
<td align="right">13,631,526</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,672,136</td>
<td align="right">1,933,399</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,819,186</td>
<td align="right">5,559,786</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">57,196,127</td>
<td align="right">65,775,426</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,307,008</td>
<td align="right">3,801,628</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,156,901</td>
<td align="right">1,328,457</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">104,138</td>
<td align="right">88,783</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,539,998</td>
<td align="right">2,909,619</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,471,144</td>
<td align="right">7,406,982</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,701,901</td>
<td align="right">4,235,636</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,818,572</td>
<td align="right">6,655,311</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,415,209</td>
<td align="right">1,616,740</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,877,616</td>
<td align="right">2,131,590</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,158,532</td>
<td align="right">26,259,531</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,550,246</td>
<td align="right">15,355,022</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,683,418</td>
<td align="right">1,906,714</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,559,133</td>
<td align="right">2,878,832</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">835,814</td>
<td align="right">938,397</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,793,220</td>
<td align="right">13,229,573</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,438,517</td>
<td align="right">2,732,082</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,652,632</td>
<td align="right">2,967,647</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,153,963</td>
<td align="right">1,288,878</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">897,154</td>
<td align="right">998,538</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,438,597</td>
<td align="right">6,035,598</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,464,722</td>
<td align="right">2,734,486</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,234,147</td>
<td align="right">1,367,842</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">940,852</td>
<td align="right">1,042,239</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">316,485</td>
<td align="right">349,970</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,831,597</td>
<td align="right">28,534,324</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,259,872</td>
<td align="right">18,929,120</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,467,374</td>
<td align="right">3,799,865</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,884,104</td>
<td align="right">21,781,811</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,375,808</td>
<td align="right">6,883,608</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,019,222</td>
<td align="right">8,593,709</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">723,185</td>
<td align="right">774,778</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,379,880</td>
<td align="right">3,601,287</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">739,264</td>
<td align="right">693,190</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">656,930</td>
<td align="right">690,433</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,712,626</td>
<td align="right">4,896,438</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,424,493</td>
<td align="right">6,671,415</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">381,672</td>
<td align="right">369,438</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,541,623</td>
<td align="right">4,686,407</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">496</td>
<td align="right">481</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">602,548</td>
<td align="right">587,183</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,075</td>
<td align="right">4,981</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,125,552</td>
<td align="right">1,143,686</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">341</td>
<td align="right">345</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,343,470</td>
<td align="right">11,476,157</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,626</td>
<td align="right">1,610</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,002,837</td>
<td align="right">2,020,971</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,472</td>
<td align="right">13,378</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,238</td>
<td align="right">3,258</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,588</td>
<td align="right">4,614</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,695</td>
<td align="right">17,601</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,695</td>
<td align="right">17,601</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">205,059</td>
<td align="right">204,742</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,404</td>
<td align="right">102,250</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,380</td>
<td align="right">97,260</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">108,868</td>
<td align="right">108,784</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,421</td>
<td align="right">46,391</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">16,571</td>
<td align="right">16,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,790</td>
<td align="right">456,716</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,814</td>
<td align="right">928,724</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,673</td>
<td align="right">81,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,042</td>
<td align="right">34,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,131</td>
<td align="right">35,130</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,699</td>
<td align="right">1,818,666</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,622</td>
<td align="right">939,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,015</td>
<td align="right">191,016</td>
<td align="right">0.0%</td>
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
<td align="right">59,116</td>
<td align="right">59,116</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">107</td>
<td align="right">107</td>
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
<td align="right">18,953</td>
<td align="right">0.2%</td>
<td align="right">15,140</td>
<td align="right">0.1%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,950,559</td>
<td align="right">98.6%</td>
<td align="right">10,608,861</td>
<td align="right">98.8%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">107,917</td>
<td align="right">1.2%</td>
<td align="right">107,826</td>
<td align="right">1.0%</td>
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
<td align="right">624</td>
<td align="right">47.5%</td>
<td align="right">553</td>
<td align="right">44.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">690</td>
<td align="right">52.5%</td>
<td align="right">696</td>
<td align="right">55.7%</td>
<td align="right">0.9%</td>
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
<td align="right">85</td>
<td align="right">12.3%</td>
<td align="right">88</td>
<td align="right">12.6%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">291</td>
<td align="right">42.2%</td>
<td align="right">294</td>
<td align="right">42.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">27.1%</td>
<td align="right">187</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">9.6%</td>
<td align="right">66</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">58</td>
<td align="right">8.4%</td>
<td align="right">58</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.3%</td>
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
<td align="right">20,978,945</td>
<td align="right">100.0%</td>
<td align="right">24,079,025</td>
<td align="right">100.0%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,032</td>
<td align="right">0.0%</td>
<td align="right">2,013</td>
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
<td align="right">3,343</td>
<td align="right">100.0%</td>
<td align="right">3,388</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">648,875</td>
<td align="right">14.0%</td>
<td align="right">786,613</td>
<td align="right">15.2%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,537</td>
<td align="right">0.4%</td>
<td align="right">15,664</td>
<td align="right">0.3%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,956,014</td>
<td align="right">85.5%</td>
<td align="right">4,361,677</td>
<td align="right">84.4%</td>
<td align="right">10.3%</td>
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
<td align="right">605</td>
<td align="right">39.1%</td>
<td align="right">557</td>
<td align="right">38.2%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">941</td>
<td align="right">60.9%</td>
<td align="right">902</td>
<td align="right">61.8%</td>
<td align="right">-4.1%</td>
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
<td align="right">652</td>
<td align="right">69.3%</td>
<td align="right">610</td>
<td align="right">67.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">150</td>
<td align="right">15.9%</td>
<td align="right">153</td>
<td align="right">17.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">10.1%</td>
<td align="right">95</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">4.7%</td>
<td align="right">44</td>
<td align="right">4.9%</td>
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
<td align="right">1,510,894</td>
<td align="right">100.0%</td>
<td align="right">1,747,656</td>
<td align="right">100.0%</td>
<td align="right">15.7%</td>
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
<td align="right">11,612,745</td>
<td align="right">92.5%</td>
<td align="right">11,960,254</td>
<td align="right">92.7%</td>
<td align="right">3.0%</td>
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
<td align="right">7.5%</td>
<td align="right">939,088</td>
<td align="right">7.3%</td>
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
<td align="right">46</td>
<td align="right">8.6%</td>
<td align="right">53</td>
<td align="right">9.8%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">91.4%</td>
<td align="right">488</td>
<td align="right">90.2%</td>
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
<td align="right">6,830,378</td>
<td align="right">15.9%</td>
<td align="right">8,008,395</td>
<td align="right">16.7%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,677,678</td>
<td align="right">83.1%</td>
<td align="right">39,649,265</td>
<td align="right">82.5%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,812</td>
<td align="right">0.9%</td>
<td align="right">397,073</td>
<td align="right">0.8%</td>
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
<td align="right">6,603</td>
<td align="right">36.0%</td>
<td align="right">6,873</td>
<td align="right">36.8%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,747</td>
<td align="right">64.0%</td>
<td align="right">11,782</td>
<td align="right">63.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,496</td>
<td align="right">22.7%</td>
<td align="right">1,634</td>
<td align="right">23.8%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">815</td>
<td align="right">12.3%</td>
<td align="right">855</td>
<td align="right">12.4%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">10.3%</td>
<td align="right">682</td>
<td align="right">9.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,506</td>
<td align="right">22.8%</td>
<td align="right">1,506</td>
<td align="right">21.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
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
<td align="right">0.7%</td>
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
<td align="right">17,593,415</td>
<td align="right">100.0%</td>
<td align="right">20,286,599</td>
<td align="right">100.0%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">863</td>
<td align="right">0.0%</td>
<td align="right">859</td>
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
<td align="right">2,381</td>
<td align="right">100.0%</td>
<td align="right">2,405</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">1,759,266</td>
<td align="right">100.0%</td>
<td align="right">2,130,943</td>
<td align="right">100.0%</td>
<td align="right">21.1%</td>
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
<td align="right">4,419,353</td>
<td align="right">94.8%</td>
<td align="right">5,093,926</td>
<td align="right">95.5%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,940</td>
<td align="right">1.7%</td>
<td align="right">79,942</td>
<td align="right">1.5%</td>
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
<td align="right">3.4%</td>
<td align="right">160,377</td>
<td align="right">3.0%</td>
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
<td align="right">3,993</td>
<td align="right">84.3%</td>
<td align="right">3,994</td>
<td align="right">84.3%</td>
<td align="right">0.0%</td>
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
<td align="right">764</td>
<td align="right">102.7%</td>
<td align="right">825</td>
<td align="right">110.9%</td>
<td align="right">8.0%</td>
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
<td align="right">1,572,371</td>
<td align="right">98.7%</td>
<td align="right">1,809,034</td>
<td align="right">98.8%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,262</td>
<td align="right">1.3%</td>
<td align="right">21,264</td>
<td align="right">1.2%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">20</td>
<td align="right">9.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
<td align="right">187</td>
<td align="right">90.3%</td>
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
<td align="right">10,020,734</td>
<td align="right">94.3%</td>
<td align="right">11,874,777</td>
<td align="right">95.3%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">601,235</td>
<td align="right">5.7%</td>
<td align="right">585,872</td>
<td align="right">4.7%</td>
<td align="right">-2.6%</td>
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
<td align="left">Success</td>
<td align="right">453</td>
<td align="right">34.5%</td>
<td align="right">463</td>
<td align="right">35.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">860</td>
<td align="right">65.5%</td>
<td align="right">848</td>
<td align="right">64.7%</td>
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
<td align="left">mapping</td>
<td align="right">318</td>
<td align="right">37.0%</td>
<td align="right">304</td>
<td align="right">35.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">133</td>
<td align="right">15.5%</td>
<td align="right">135</td>
<td align="right">15.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">27.0%</td>
<td align="right">232</td>
<td align="right">27.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.9%</td>
<td align="right">111</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">44</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">22</td>
<td align="right">2.6%</td>
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
<td align="right">2,060,267</td>
<td align="right">100.0%</td>
<td align="right">2,127,233</td>
<td align="right">100.0%</td>
<td align="right">3.3%</td>
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
<td align="right">9,268,438</td>
<td align="right">2.4%</td>
<td align="right">10,569,103</td>
<td align="right">2.5%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">157,405,265</td>
<td align="right">40.9%</td>
<td align="right">176,309,962</td>
<td align="right">41.0%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">217,244,074</td>
<td align="right">56.5%</td>
<td align="right">242,614,973</td>
<td align="right">56.4%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">596,735</td>
<td align="right">0.2%</td>
<td align="right">589,311</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">648,875</td>
<td align="right">7.0%</td>
<td align="right">786,613</td>
<td align="right">7.5%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,830,378</td>
<td align="right">73.9%</td>
<td align="right">8,008,395</td>
<td align="right">75.9%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">601,235</td>
<td align="right">6.5%</td>
<td align="right">585,872</td>
<td align="right">5.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,032</td>
<td align="right">0.0%</td>
<td align="right">2,013</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">863</td>
<td align="right">0.0%</td>
<td align="right">859</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">107,917</td>
<td align="right">1.2%</td>
<td align="right">107,826</td>
<td align="right">1.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,262</td>
<td align="right">0.2%</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,940</td>
<td align="right">0.9%</td>
<td align="right">79,942</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,088</td>
<td align="right">10.2%</td>
<td align="right">939,088</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.2%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">9,655</td>
<td align="right">1.6%</td>
<td align="right">7,707</td>
<td align="right">1.3%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">9,298</td>
<td align="right">1.6%</td>
<td align="right">7,433</td>
<td align="right">1.3%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,536</td>
<td align="right">3.1%</td>
<td align="right">15,663</td>
<td align="right">2.7%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,698</td>
<td align="right">8.3%</td>
<td align="right">49,507</td>
<td align="right">8.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">338,070</td>
<td align="right">56.7%</td>
<td align="right">337,522</td>
<td align="right">57.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">26.9%</td>
<td align="right">160,377</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
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
<td align="right">445,436</td>
<td align="right">1.5%</td>
<td align="right">513,331</td>
<td align="right">1.6%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">24,160,423</td>
<td align="right">82.8%</td>
<td align="right">27,399,370</td>
<td align="right">84.5%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">21,162,101</td>
<td align="right">72.5%</td>
<td align="right">23,826,561</td>
<td align="right">73.5%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,596,147</td>
<td align="right">26.0%</td>
<td align="right">8,170,634</td>
<td align="right">25.2%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,596,205</td>
<td align="right">26.0%</td>
<td align="right">8,170,692</td>
<td align="right">25.2%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,023,580</td>
<td align="right">27.5%</td>
<td align="right">8,598,067</td>
<td align="right">26.5%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,023,580</td>
<td align="right">27.5%</td>
<td align="right">8,598,067</td>
<td align="right">26.5%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,709</td>
<td align="right">0.1%</td>
<td align="right">17,615</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.5%</td>
<td align="right">427,375</td>
<td align="right">1.3%</td>
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
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.5%</td>
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
<td align="left">Method cache collisions</td>
<td align="right">69,675</td>
<td align="right"></td>
<td align="right">27,378</td>
<td align="right"></td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,412,130</td>
<td align="right"></td>
<td align="right">1,681,960</td>
<td align="right"></td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,729,508</td>
<td align="right"></td>
<td align="right">11,558,187</td>
<td align="right"></td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">211,337</td>
<td align="right"></td>
<td align="right">172,126</td>
<td align="right"></td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">832,818</td>
<td align="right">0.3%</td>
<td align="right">967,665</td>
<td align="right">0.3%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,342,600</td>
<td align="right"></td>
<td align="right">9,626,187</td>
<td align="right"></td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,272,273</td>
<td align="right">2.3%</td>
<td align="right">6,014,919</td>
<td align="right">2.3%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">53,270,289</td>
<td align="right">20.2%</td>
<td align="right">60,414,975</td>
<td align="right">20.4%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">81,338,868</td>
<td align="right">35.1%</td>
<td align="right">91,887,534</td>
<td align="right">35.3%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">49,115,877</td>
<td align="right">21.2%</td>
<td align="right">55,467,398</td>
<td align="right">21.3%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">23,347,911</td>
<td align="right">65.8%</td>
<td align="right">26,350,952</td>
<td align="right">66.6%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,350,203</td>
<td align="right"></td>
<td align="right">26,352,871</td>
<td align="right"></td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">81,630,030</td>
<td align="right">31.0%</td>
<td align="right">91,790,989</td>
<td align="right">31.1%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">127,656,968</td>
<td align="right">48.5%</td>
<td align="right">142,406,504</td>
<td align="right">48.2%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">95,885,096</td>
<td align="right">41.4%</td>
<td align="right">106,602,883</td>
<td align="right">41.0%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,343,566</td>
<td align="right"></td>
<td align="right">14,658,837</td>
<td align="right"></td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,040,805</td>
<td align="right">33.9%</td>
<td align="right">13,119,914</td>
<td align="right">33.1%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,162,002</td>
<td align="right">34.2%</td>
<td align="right">13,241,099</td>
<td align="right">33.4%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,585</td>
<td align="right">0.1%</td>
<td align="right">43,574</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,744,629</td>
<td align="right"></td>
<td align="right">1,744,417</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,612</td>
<td align="right">0.2%</td>
<td align="right">77,611</td>
<td align="right">0.2%</td>
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
<td align="right">2,540,459</td>
<td align="right"></td>
<td align="right">3,040,273</td>
<td align="right"></td>
<td align="right">19.7%</td>
</tr>
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
<td align="right">9</td>
<td align="right">0.3%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">226,760,794</td>
<td align="right">8,926.0%</td>
<td align="right">258,627,705</td>
<td align="right">8,506.7%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">90</td>
<td align="right">2.9%</td>
<td align="right">83</td>
<td align="right">2.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,500</td>
<td align="right">48.4%</td>
<td align="right">1,562</td>
<td align="right">48.8%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,294</td>
<td align="right">41.8%</td>
<td align="right">1,341</td>
<td align="right">41.9%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,096</td>
<td align="right"></td>
<td align="right">3,198</td>
<td align="right"></td>
<td align="right">3.3%</td>
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
<td align="right">212</td>
<td align="right">6.8%</td>
<td align="right">212</td>
<td align="right">6.6%</td>
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
<td align="right">90</td>
<td align="right"></td>
<td align="right">83</td>
<td align="right"></td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">90</td>
<td align="right">100.0%</td>
<td align="right">83</td>
<td align="right">100.0%</td>
<td align="right">-7.8%</td>
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
<td align="right">2,192,873</td>
<td align="right">88.9%</td>
<td align="right">1,961,218</td>
<td align="right">88.2%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,465,792</td>
<td align="right"></td>
<td align="right">2,224,128</td>
<td align="right"></td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">49,976</td>
<td align="right">2.0%</td>
<td align="right">45,160</td>
<td align="right">2.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">222,943</td>
<td align="right">9.0%</td>
<td align="right">217,750</td>
<td align="right">9.8%</td>
<td align="right">-2.3%</td>
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
<td align="left">16</td>
<td align="right">17.8%</td>
<td align="left">14</td>
<td align="right">16.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">22</td>
<td align="right">24.4%</td>
<td align="left">22</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">31</td>
<td align="right">34.4%</td>
<td align="left">29</td>
<td align="right">34.9%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">23.3%</td>
<td align="left">18</td>
<td align="right">21.7%</td>
<td align="right">-14.3%</td>
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
<td align="right">16</td>
<td align="right">17.8%</td>
<td align="right">14</td>
<td align="right">16.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21</td>
<td align="right">23.3%</td>
<td align="right">21</td>
<td align="right">25.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2</td>
<td align="right">2.2%</td>
<td align="right">2</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">30</td>
<td align="right">33.3%</td>
<td align="right">28</td>
<td align="right">33.7%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">23.3%</td>
<td align="right">18</td>
<td align="right">21.7%</td>
<td align="right">-14.3%</td>
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
<td align="right">16</td>
<td align="right">17.8%</td>
<td align="right">14</td>
<td align="right">16.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">24.4%</td>
<td align="right">22</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">17</td>
<td align="right">18.9%</td>
<td align="right">15</td>
<td align="right">18.1%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">24</td>
<td align="right">26.7%</td>
<td align="right">23</td>
<td align="right">27.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">11</td>
<td align="right">12.2%</td>
<td align="right">9</td>
<td align="right">10.8%</td>
<td align="right">-18.2%</td>
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
<td align="right">442,486</td>
<td align="right">2,519,790</td>
<td align="right">469.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">442,486</td>
<td align="right">979,628</td>
<td align="right">121.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">76,946</td>
<td align="right">125,799</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">76,946</td>
<td align="right">125,799</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">77,041</td>
<td align="right">125,903</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">77,041</td>
<td align="right">125,903</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">77,041</td>
<td align="right">125,903</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,052,214</td>
<td align="right">953,632</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,898,267</td>
<td align="right">1,357,199</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,244,910</td>
<td align="right">6,103,846</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">653,348</td>
<td align="right">907,945</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">351,868</td>
<td align="right">474,263</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">351,868</td>
<td align="right">474,263</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">596,473</td>
<td align="right">797,648</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">499,361</td>
<td align="right">656,243</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">1,910,237</td>
<td align="right">2,489,576</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">2,047,766</td>
<td align="right">2,663,889</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">519,527</td>
<td align="right">671,849</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,585,158</td>
<td align="right">2,045,906</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,585,158</td>
<td align="right">2,045,906</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">794,354</td>
<td align="right">1,020,209</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,333,945</td>
<td align="right">1,707,554</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">412,436</td>
<td align="right">522,757</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">137,531</td>
<td align="right">174,316</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,236,842</td>
<td align="right">1,566,158</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,182,380</td>
<td align="right">2,706,541</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,946,008</td>
<td align="right">2,407,526</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,946,008</td>
<td align="right">2,407,526</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,032,465</td>
<td align="right">1,273,872</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">148,375</td>
<td align="right">182,862</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">638,619</td>
<td align="right">785,187</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,864,948</td>
<td align="right">2,277,679</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,113,617</td>
<td align="right">3,790,091</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,274,860</td>
<td align="right">1,549,569</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,644,528</td>
<td align="right">1,973,844</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,333,566</td>
<td align="right">1,598,472</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">5,984,329</td>
<td align="right">7,165,275</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,540,459</td>
<td align="right">3,040,273</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,402,928</td>
<td align="right">2,865,957</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">3,367,331</td>
<td align="right">4,007,100</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,202,042</td>
<td align="right">1,427,898</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">898,832</td>
<td align="right">1,055,786</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">561,673</td>
<td align="right">659,388</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,088,305</td>
<td align="right">3,622,678</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">751,339</td>
<td align="right">873,806</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,340,753</td>
<td align="right">3,876,989</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,340,753</td>
<td align="right">3,876,989</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,340,753</td>
<td align="right">3,876,989</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">763,673</td>
<td align="right">886,068</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,876,407</td>
<td align="right">2,175,881</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,296,763</td>
<td align="right">1,503,685</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">39,287,574</td>
<td align="right">45,263,526</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">34,967,523</td>
<td align="right">40,079,773</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">997,658</td>
<td align="right">1,135,606</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,644,224</td>
<td align="right">1,864,872</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,256,130</td>
<td align="right">1,422,891</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">632,220</td>
<td align="right">715,569</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,629,851</td>
<td align="right">6,318,972</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">846,053</td>
<td align="right">949,513</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,853,010</td>
<td align="right">4,322,573</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,185,064</td>
<td align="right">2,440,847</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,782,935</td>
<td align="right">1,988,814</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,201,603</td>
<td align="right">5,771,357</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">484,632</td>
<td align="right">533,485</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">484,727</td>
<td align="right">533,589</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,727</td>
<td align="right">533,589</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">484,727</td>
<td align="right">533,589</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">488,766</td>
<td align="right">537,624</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,233,653</td>
<td align="right">1,341,677</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,792,107</td>
<td align="right">1,936,915</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,792,107</td>
<td align="right">1,936,915</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">7,511,686</td>
<td align="right">8,082,841</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,633,124</td>
<td align="right">1,741,220</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">547,846</td>
<td align="right">582,405</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">551,082</td>
<td align="right">585,641</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">551,082</td>
<td align="right">585,641</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">551,060</td>
<td align="right">585,547</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">551,060</td>
<td align="right">585,547</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">888,294</td>
<td align="right">937,156</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">892,414</td>
<td align="right">941,299</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,800,408</td>
<td align="right">7,149,091</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,800,408</td>
<td align="right">7,149,091</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,103,019</td>
<td align="right">2,151,872</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,507,468</td>
<td align="right">2,556,321</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,471</td>
<td align="right">399,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,471</td>
<td align="right">399,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,471</td>
<td align="right">399,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,471</td>
<td align="right">399,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,471</td>
<td align="right">399,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,214,843</td>
<td align="right">1,214,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">812,135</td>
<td align="right">812,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">697,307</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
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
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,471</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">301,480</td>
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
<td align="left">_GUARD_TOS_FLOAT</td>
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
<td align="right">214</td>
<td align="right">214</td>
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
Stats gathered on: 2025-04-24
